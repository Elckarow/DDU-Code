init python in custom_keymap:
    import pygame_sdl2 as pygame
    from renpy import config, store
    from store import preferences, Function, Preference, SaveMenu, SettingsMenu, Hide, __, _, DDU_multi_persistent

    config.keymap["game_menu"]    = [ ]
    config.keymap["toggle_skip"]  = [ ]
    config.keymap["hide_windows"] = [ "mouseup_3", "mouseup_2" ]

    if renpy.variant("pc"):
        config.keymap["self_voicing"]      = [ ]
        config.keymap["clipboard_voicing"] = [ ]
        config.keymap["screenshot"]        = [ ]
        config.keymap["toggle_fullscreen"] = [ ]
        config.keymap["accessibility"]     = [ ]

        config.always_shown_screens.append("custom_keymap")
    
###################################################

    def _run_action(action, main_menu=True, quick_menu_showing=True):
        """
        `action`: Action | tuple[Action] | list[Action]
            An action or a list of actions to be ran.
        
        `main_menu`: bool
            Should the action be ran when called on the main menu?
        
        `quick_menu_showing`: bool
            Should the action be ran only when the quick menu is showing?
        """
        if store.main_menu and not main_menu: return
        if not store.quick_menu and quick_menu_showing: return
        return renpy.run(action)
    
    def mute_all():
        return _run_action(Preference("all mute", "toggle"))

    def save_menu():
        return _run_action(SaveMenu())
    
    def settings():
        return _run_action(SettingsMenu())
    
    def afm():
        return _run_action(Preference("auto-forward", "toggle"), main_menu=False, quick_menu_showing=False)

    def increase_volume(mixer):
        current = preferences.get_volume(mixer)
        preferences.set_volume(mixer, min(current + 0.1, 1.0))
    
    def decrease_volume(mixer):
        current = preferences.get_volume(mixer)
        preferences.set_volume(mixer, max(current - 0.1, 0.0))

    _keymap = dict(
        screenshot=Function(store._screenshot),
        afm=Function(afm),

        increase_general_volume=Function(increase_volume, "main"),
        increase_music_volume=Function(increase_volume, "music"),
        increase_sfx_volume=Function(increase_volume, "sfx"),
        increase_ambient_volume=Function(increase_volume, "ambient"),

        decrease_general_volume=Function(decrease_volume, "main"),
        decrease_music_volume=Function(decrease_volume, "music"),
        decrease_sfx_volume=Function(decrease_volume, "sfx"),
        decrease_ambient_volume=Function(decrease_volume, "ambient"),

        mute_all=Function(mute_all),
        
        save_menu=Function(save_menu),
        settings=Function(settings),

        iconify=Function(renpy.iconify),
        toggle_fullscreen=Function(renpy.toggle_fullscreen)
    )

    default_custom_keymap = dict(
        screenshot=["K_z"],
        afm=["alt_K_f"],

        increase_general_volume=["K_g", "K_UP"],
        increase_music_volume=["K_m", "K_UP"],
        increase_sfx_volume=["K_s", "K_UP"],
        increase_ambient_volume=["K_a", "K_UP"],

        decrease_general_volume=["K_g", "K_DOWN"],
        decrease_music_volume=["K_m", "K_DOWN"],
        decrease_sfx_volume=["K_s", "K_DOWN"],
        decrease_ambient_volume=["K_a", "K_DOWN"],

        mute_all=["alt_K_m"],

        save_menu=["K_ESCAPE"],
        settings=["shift_K_s"],

        iconify=["shift_K_i"],
        toggle_fullscreen=["shift_K_f"]
    )

    if default_custom_keymap.keys() != _keymap.keys():
        raise Exception("default_custom_keymap.keys() != _keymap.keys()")

    custom_keymap_always = (
        "screenshot",
        "afm",

        "increase_general_volume",
        "increase_music_volume",
        "increase_sfx_volume",
        "increase_ambient_volume",

        "decrease_general_volume",
        "decrease_music_volume",
        "decrease_sfx_volume",
        "decrease_ambient_volume",

        "mute_all",

        "iconify",
        "toggle_fullscreen"
    )

    default_custom_keymap_multiple = {
        "increase_general_volume",
        "increase_music_volume",
        "increase_sfx_volume",
        "increase_ambient_volume",

        "decrease_general_volume",
        "decrease_music_volume",
        "decrease_sfx_volume",
        "decrease_ambient_volume"
    }

    unknown = default_custom_keymap_multiple.difference(_keymap)
    if unknown:
        raise Exception("".join(unknown) + " unknown")
    del unknown

###################################################
    
    custom_keymap_version = 1.0

    if DDU_multi_persistent.custom_keymap_version is None:
        print("DDU -- Initializing Custom Keymap")
        DDU_multi_persistent.keymap = dict(default_custom_keymap)
        DDU_multi_persistent.multiple_keymap = set(default_custom_keymap_multiple)
        DDU_multi_persistent.custom_keymap_version = custom_keymap_version
        DDU_multi_persistent.save()
    
    elif DDU_multi_persistent.custom_keymap_version != custom_keymap_version:
        print("DDU -- Updating Custom Keymap")
 
        for k, v in default_custom_keymap.items():
            DDU_multi_persistent.keymap.setdefault(k, v)
        del k, v

        DDU_multi_persistent.multiple_keymap |= default_custom_keymap_multiple
        DDU_multi_persistent.custom_keymap_version = custom_keymap_version
        DDU_multi_persistent.save()

###################################################

    class Keymap(renpy.display.behavior.Keymap):
        reset_after_run = "last"

        def __init__(self, bind, reset_after_run="last", **properties):
            renpy.display.layout.Null.__init__(self, **properties)

            self.bind = bind
            self.action = _keymap[bind]

            if reset_after_run not in ("last", "all", False):
                raise Exception(f"unknown reset_after_run: {reset_after_run}")
            self.reset_after_run = reset_after_run

            self.pressed_keys = set()
            self.required_keys = set()
            self.keymap = dict()
            self.update_keys()

            self.always = bind in custom_keymap_always
        
        @property
        def multiple_key(self):
            return self.bind in DDU_multi_persistent.multiple_keymap

        def update_keys(self):
            keys = DDU_multi_persistent.keymap[self.bind]

            self.pressed_keys.clear()

            if not self.multiple_key:
                self.keymap.clear(); self.keymap |= {key: self.action for key in keys}
                self.required_keys.clear()
            else:
                self.required_keys.clear(); self.required_keys |= set(getattr(pygame.constants, key) for key in keys)
                self.keymap.clear()
        
        def event(self, ev, x, y, st):
            if not self.multiple_key:
                return super(Keymap, self).event(ev, x, y, st)

            if ev.type == pygame.KEYDOWN:
                self.pressed_keys.add(ev.key)

            elif ev.type == pygame.KEYUP:
                self.pressed_keys.discard(ev.key)

            if (self.pressed_keys & self.required_keys) == self.required_keys:
                rv = renpy.run(self.action)

                if self.reset_after_run == "all":
                    self.pressed_keys.clear()
                elif self.reset_after_run == "last":
                    # we know ev.key is in the set
                    # the `remove` method is more appropriate here
                    self.pressed_keys.remove(ev.key)

                if rv is not None: return rv
                raise renpy.display.core.IgnoreEvent()

            return None
        
        def predict_one_action(self):
            renpy.display.behavior.predict_action(self.action)

    keymaps = tuple(Keymap(bind) for bind in _keymap)

# set to False during the splash screen
default custom_keymap.allowed = True

screen custom_keymap():
    zorder 500

    for keymap in custom_keymap.keymaps:
        showif keymap.always or custom_keymap.allowed:
            add keymap

###################################################

init python in custom_keymap:
    def format_key(bind):
        """
        Ugly way of formating a keymap into a readable string.

        `bind`: str
            A key of `DDU_multi_persistent.keymap`.
        """
        keys = [ ]

        for key in DDU_multi_persistent.keymap[bind]:
            mod, k = key.replace("KP", "").split("K_")
            k = "'" + mod.replace("_", "' + '") + k.lower() + "'"

            keys.append(k)

        return __(" and ").join(keys)
    
    def current_key(b):
        return __("Current: {key}").format(key=format_key(b))
    
    def update(bind=None):
        for keymap in keymaps:
            if bind is not None and keymap.bind != bind: continue
            keymap.update_keys()

    def reset():
        DDU_multi_persistent.keymap.update(default_custom_keymap)
        DDU_multi_persistent.multiple_keymap = set(default_custom_keymap_multiple)
        DDU_multi_persistent.save()
        update()

    class SelectKey(renpy.display.layout.Null):
        allowed_keys = {getattr(pygame.constants, k): k
            for k in [
                "K_ESCAPE",
                "K_a", "K_b", "K_c", "K_d", "K_e", "K_f", "K_g", "K_h", "K_i", "K_j", "K_k",
                "K_l", "K_m", "K_n", "K_o", "K_p", "K_q", "K_r", "K_s", "K_t", "K_u", "K_v",
                "K_w", "K_x", "K_y", "K_z",
                "K_KP0", "K_KP1", "K_KP2", "K_KP3", "K_KP4", "K_KP5", "K_KP6", "K_KP7", "K_KP8", "K_KP9"
            ]
        }

        key_already_used = _("This key is already being used\nPlease try again")
        key_not_allowed  = _("This key is not allowed\nPlease try a different key")

        def __init__(self, bind, display_text, **kwargs):
            super(SelectKey, self).__init__(**kwargs)

            self.bind = bind
            self.used_keys = [
                keys
                for what, keys in DDU_multi_persistent.keymap.items()
                if what != bind 
                and what not in DDU_multi_persistent.multiple_keymap
            ]

            self.display_text = display_text

            self._done = False
        
        def is_used_key(self, key):
            if isinstance(key, (list, tuple, set)):
                return any(map(self.is_used_key, key))

            for keys in self.used_keys:
                for k in keys:
                    if k == key:
                        return True

            return False

        def hide_screen(self, message=None):
            renpy.hide_screen("register_keymap")
            
            if message is not None:
                renpy.show_screen("dialog", message=__(message), ok_action=Hide("dialog"))
            elif self._done:
                self.done()
            
            renpy.transition(store.game_menu_transition)
            renpy.restart_interaction()
            return renpy.display.core.IgnoreEvent()
        
        def done(self):
            update(self.bind)
            renpy.show_screen("dialog", message=__("{display_text} has been set to\n{key}").format(display_text=__(self.display_text), key=format_key(self.bind)), ok_action=Hide("dialog"))
        
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP:
                raise self.hide_screen()

            if ev.type == pygame.KEYDOWN:
                key = self.allowed_keys.get(ev.key, None)
                
                if key is None:
                    if ev.key in [pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_LALT, pygame.K_RALT]:
                        raise renpy.display.core.IgnoreEvent()
                    else:
                        raise self.hide_screen(__(self.key_not_allowed))

                if ev.mod & pygame.KMOD_SHIFT:
                    key = [ "shift_" + key ]
                    if key == ["shift_K_r"] and config.developer:
                        raise self.hide_screen("dev mode is on you pepega")
                        
                elif ev.mod & pygame.KMOD_ALT:
                    key = [ "alt_" + key ]
                else:
                    key = [ key ]

                if self.is_used_key(key):
                    raise self.hide_screen(__(self.key_already_used))

                DDU_multi_persistent.keymap[self.bind] = key
                DDU_multi_persistent.multiple_keymap.discard(self.bind)
                DDU_multi_persistent.save()

                self._done = True
                raise self.hide_screen()

            raise renpy.display.core.IgnoreEvent()

    class SelectDoubleleKey(SelectKey):
        key_already_used = _("This combination of keys is already being used\nPlease try again")
        more_than_two    = _("More then 2 keys were registered.\nPlease try again")

        allowed_keys = {getattr(pygame.constants, k): k
            for k in [
                "K_ESCAPE",
                "K_a", "K_b", "K_c", "K_d", "K_e", "K_f", "K_g", "K_h", "K_i", "K_j", "K_k",
                "K_l", "K_m", "K_n", "K_o", "K_p", "K_q", "K_r", "K_s", "K_t", "K_u", "K_v",
                "K_w", "K_x", "K_y", "K_z",
                "K_LEFT", "K_RIGHT", "K_UP", "K_DOWN",
                "K_KP0", "K_KP1", "K_KP2", "K_KP3", "K_KP4", "K_KP5", "K_KP6", "K_KP7", "K_KP8", "K_KP9"
            ]
        }

        def __init__(self, bind, display_text, **properties):
            renpy.display.layout.Null.__init__(self, **properties)

            self.used_keys = [
                set(DDU_multi_persistent.keymap[what])
                for what in DDU_multi_persistent.multiple_keymap
                if what != bind
            ]

            self.bind = bind
            self.double_key = set()

            self.display_text = display_text

            self._done = False

        def is_used_key(self, key):
            return any(map(lambda s: s == key, self.used_keys))
        
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP:
                raise self.hide_screen()

            if ev.type == pygame.KEYUP:
                self.double_key.discard(ev.key)
                raise renpy.display.core.IgnoreEvent()
            
            elif ev.type == pygame.KEYDOWN:
                key = self.allowed_keys.get(ev.key, None)
                
                if key is None:
                    raise self.hide_screen(__(self.key_not_allowed))

                self.double_key.add(key)

                if len(self.double_key) > 2:
                    raise self.hide_screen(__(self.more_than_two))
                
                if len(self.double_key) == 2:
                    if self.is_used_key(self.double_key):
                        raise self.hide_screen(__(self.key_already_used))
                    
                    DDU_multi_persistent.multiple_keymap.add(self.bind)
                    DDU_multi_persistent.keymap[self.bind] = self.double_key
                    DDU_multi_persistent.save()

                    self._done = True
                    raise self.hide_screen()
                
            raise renpy.display.core.IgnoreEvent()
    
    def input_key(bind, display_text, double):
        if double:
            return SelectDoubleleKey(bind, display_text)
        else:
            return SelectKey(bind, display_text)

screen register_keymap(bind, display_text, double):
    modal True zorder 501
    style_prefix "key_input"

    add custom_keymap.input_key(bind, display_text, double)
    add Solid("#000"):
        alpha 0.6

    vbox:
        spacing 30

        vbox:
            text _("{u}USE YOUR MOUSE TO CANCEL{/u}")
            text _("Press any key you would want to use.")
            text _("For multiple keys, hold the first key, then press the second key.")
    
        vbox:
            text _("Any key from [[a-z] to [[0-9], as well as 'ESCAPE' is usable.")
            text _("The 'alt' and 'shift' modifiers are also available.\n('shift' doesn't work with numbers)")
            text _("{u}In multiple key mode, the arrowkeys are available, while 'alt' and 'shift' aren't.{/u}")
    
    text "[display_text!t]" align (0.0, 1.0)
    text _("Double Key: [double!t]") align (0.5, 1.0)

    on "show" action SetField(custom_keymap, "allowed", False)
    on "hide" action SetField(custom_keymap, "allowed", True)

style key_input_text is default:
    size 22

style key_input_vbox:
    spacing 6

screen keymap():
    tag menu
    default double = False

    use game_menu(SettingsMenuInfo, menu_style="computer"):
        style_prefix "keymap"
        
        hbox:
            vbox style "keymap_main_vbox":
                xalign 0.0

                vbox:
                    s_label _("Volume Up")
                    for b, t in zip(
                        ("increase_general_volume", "increase_music_volume", "increase_sfx_volume", "increase_ambient_volume"),
                        (_("Increase General Volume"), _("Increase Music Volume"), _("Increase Sound Volume"), _("Increase Ambient Volume"))
                    ):
                        textbutton "[t!t]":
                            action Show("register_keymap", game_menu_transition, bind=b, display_text=t, double=double)
                            tooltip custom_keymap.current_key(b)
            
                vbox:
                    s_label _("Misc")
                    for b, t in zip(
                        ("toggle_fullscreen", "iconify", "screenshot", "afm", "mute_all"),
                        (_("Toggle Fullscreen"), _("Iconify"), _("Screenshot"), _("Toggle AFM"), _("Mute All"))
                    ):
                        textbutton "[t!t]":
                            action Show("register_keymap", game_menu_transition, bind=b, display_text=t, double=double)
                            tooltip custom_keymap.current_key(b)
                
            vbox style "keymap_main_vbox":
                xalign 0.5

                vbox: 
                    s_label _("Volume Down")
                    for b, t in zip(
                        ("decrease_general_volume", "decrease_music_volume", "decrease_sfx_volume", "decrease_ambient_volume"),
                        (_("Decrease General Volume"), _("Decrease Music Volume"), _("Decrease Sound Volume"), _("Decrease Ambient Volume"))
                    ):
                        textbutton "[t!t]":
                            action Show("register_keymap", game_menu_transition, bind=b, display_text=t, double=double)
                            tooltip custom_keymap.current_key(b)    
        
            vbox style "keymap_main_vbox":
                xalign 1.0

                vbox:
                    s_label _("Menu Shortcuts")
                    for b, t in zip(
                        ("save_menu", "settings"),
                        (_("Open Save Menu"), _("Open Settings"))
                    ):
                        textbutton "[t!t]":
                            action Show("register_keymap", game_menu_transition, bind=b, display_text=t, double=double)
                            tooltip custom_keymap.current_key(b)

        textbutton _("Double Key"):
            style_prefix "computer"
            align (0.5, 1.0)
            action ToggleLocalVariable("double")
            tooltip _("Register two keys to press instead of one")
    
        textbutton _("Reset"):
            align (1.0, 1.0)
            style_prefix "computer"
            action Confirm(message=__("Reset the keymap?"), yes_action=(Function(custom_keymap.reset), Hide("confirm")), no_action=Hide("confirm"))
            tooltip _("Completely reset the keymap")

style keymap_main_vbox:
    spacing 20

style keymap_button_text is default:
    size 21

style keymap_vbox:
    first_spacing 2
    spacing -1

style keymap_hbox:
    xfill True