init python in custom_keymap:
    import pygame_sdl2 as pygame
    from renpy import config, store
    from store import preferences, Function, Preference, ShowMenu, Hide, __, _, persistent, MenuReturn

    config.keymap["game_menu"]         = [ ]
    config.keymap["toggle_skip"]       = [ ]
    config.keymap["hide_windows"]      = [ "mouseup_3", "mouseup_2" ]
    config.keymap["self_voicing"]      = [ ]
    config.keymap["clipboard_voicing"] = [ ]
    config.keymap["screenshot"]        = [ ]
    config.keymap["toggle_fullscreen"] = [ ]
    config.keymap["accessibility"]     = [ ]
    config.keymap["launch_editor"]     = [ ]

    config.always_shown_screens.append("custom_keymap")

###################################################

    def _run_action(action, *args, main_menu=True, quick_menu_showing=True, game_menu=True, developer=False, **kwargs):
        """
        `action`: Action | tuple[Action] | list[Action]
            An action or a list of actions to be ran.

        `main_menu`: bool
            Should the action be ran when called on the main menu?

        `game_menu`: bool
            Should the action be ran when called in the game menu?

        `quick_menu_showing`: bool
            Should the action be ran only when the quick menu is showing?

        `developer`: bool
            If true, can only be used in dev mode.
        """

        def inner():
            if developer and not config.developer: return
            if store.main_menu and not main_menu: return
            if (renpy.context()._menu and not store.main_menu) and not game_menu: return
            if not store.quick_menu and quick_menu_showing: return
            return renpy.run(action(*args, **kwargs))

        return inner

    def increase_volume(mixer):
        current = preferences.get_mixer(mixer)
        preferences.set_mixer(mixer, min(current + 0.1, 1.0))

    def decrease_volume(mixer):
        current = preferences.get_mixer(mixer)
        preferences.set_mixer(mixer, max(current - 0.1, 0.0))
    
    def toggle_screen(s):
        return MenuReturn() if renpy.get_screen(s) is not None else ShowMenu(s)
    
    def save_menu():
        return toggle_screen("load" if store.main_menu else "ig_file_slots")

    def settings():
        return toggle_screen("configuration" if store.main_menu else "ig_configuration")

    _keymap = dict(
        screenshot=Function(store._screenshot),
        afm=_run_action(Preference, "auto-forward", "toggle", main_menu=False, quick_menu_showing=False),

        increase_general_volume=Function(increase_volume, "main"),
        increase_music_volume=Function(increase_volume, "music"),
        increase_sfx_volume=Function(increase_volume, "sfx"),
        increase_ambient_volume=Function(increase_volume, "ambient"),

        decrease_general_volume=Function(decrease_volume, "main"),
        decrease_music_volume=Function(decrease_volume, "music"),
        decrease_sfx_volume=Function(decrease_volume, "sfx"),
        decrease_ambient_volume=Function(decrease_volume, "ambient"),

        mute_all=_run_action(Preference, "all mute", "toggle"),

        save_menu=_run_action(save_menu),
        settings=_run_action(settings),

        iconify=Function(renpy.iconify),
        toggle_fullscreen=Function(renpy.toggle_fullscreen),
    )

    default_custom_keymap = dict(
        screenshot=["K_s"],
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
        toggle_fullscreen=["shift_K_f"],
    )

    if default_custom_keymap.keys() != _keymap.keys():
        raise Exception("default_custom_keymap.keys() != _keymap.keys()")
    
    # since the player can't modify the keymap on android
    # this is safe
    config.gestures = {
        "n": default_custom_keymap["save_menu"],
        "s": "hide_windows",
        "e": "skip",
        "w": default_custom_keymap["mute_all"]
    }

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

    custom_keymap_version = 1.2

    if persistent.custom_keymap_version is None:
        renpy.log("DDU -- Initializing Custom Keymap")
        persistent.keymap = dict(default_custom_keymap)
        persistent.multiple_keymap = set(default_custom_keymap_multiple)
        persistent.custom_keymap_version = custom_keymap_version
        renpy.save_persistent()

    elif persistent.custom_keymap_version != custom_keymap_version:
        renpy.log("DDU -- Updating Custom Keymap")

        for k, v in default_custom_keymap.items():
            persistent.keymap.setdefault(k, v)
        del k, v

        persistent.multiple_keymap |= default_custom_keymap_multiple
        persistent.custom_keymap_version = custom_keymap_version
        renpy.save_persistent()

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
            return self.bind in persistent.multiple_keymap

        def update_keys(self):
            keys = persistent.keymap[self.bind]

            self.pressed_keys.clear()
            self.required_keys.clear()
            self.keymap.clear()

            if self.multiple_key:
                self.required_keys |= set(getattr(pygame.constants, key) for key in keys)
            else:
                self.keymap |= {key: self.action for key in keys}

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
                    # than the `discard` one
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
        if keymap.always or custom_keymap.allowed:
            add keymap

###################################################

init python in custom_keymap:
    def format_key(bind):
        """
        Ugly way of formating a keymap into a readable string.

        `bind`: str
            A key of `persistent.keymap`.
        """
        keys = [ ]

        for key in persistent.keymap[bind]:
            mod, k = key.replace("KP", "").split("K_")
            if k not in ("UP", "DOWN", "LEFT", "RIGHT"): k = k.lower()
            k = "'" + mod.replace("_", "' + '") + k + "'"

            keys.append(k)

        return __(" + ").join(keys)

    def current_key(b):
        return __("{key}").format(key=format_key(b))

    def update(bind=None):
        for keymap in keymaps:
            if bind is not None and keymap.bind != bind: continue
            keymap.update_keys()

    def reset():
        persistent.keymap.update(default_custom_keymap)
        persistent.multiple_keymap = set(default_custom_keymap_multiple)
        renpy.save_persistent()
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
                for what, keys in persistent.keymap.items()
                if what != bind
                and what not in persistent.multiple_keymap
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

            renpy.transition(store.Dissolve(0.1))
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

                persistent.keymap[self.bind] = key
                persistent.multiple_keymap.discard(self.bind)
                renpy.save_persistent()

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
                set(persistent.keymap[what])
                for what in persistent.multiple_keymap
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

                    persistent.multiple_keymap.add(self.bind)
                    persistent.keymap[self.bind] = self.double_key
                    renpy.save_persistent()

                    self._done = True
                    raise self.hide_screen()

            raise renpy.display.core.IgnoreEvent()

    def input_key(bind, display_text, double):
        if double:
            return SelectDoubleleKey(bind, display_text)
        else:
            return SelectKey(bind, display_text)

screen register_keymap(bind, display_text, double, current):
    modal True zorder 501
    style_prefix "key_input"

    add custom_keymap.input_key(bind, display_text, double)

    add Solid("#000"):
        alpha 0.6

    frame at Flatten style "empty":
        at transform:
            subpixel True
            on show:
                alpha 0.0 zoom 0.8
                easein_quart 0.4 alpha 1.0 zoom 1.0
            on hide:
                easein_quart 0.4 alpha 0.0 zoom 0.8
        
        align (0.5, 0.5)
        padding (20, 20)
        xysize (900, 400)
        background Solid("#FDFDFD")

        add Solid("#000") xysize (125, 3) offset (-20, -20) at unfurl
        add Solid("#000") xysize (300, 1) offset (-20, -20) at unfurl

        text "[display_text!t]:" font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf" align (0.0, 0.0)
        
        hbox style "empty":
            spacing 5 align (1.0, 0.0)

            text _("Currently: ") font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"
            text current

        vbox style "empty":
            yalign 0.4 spacing 30

            vbox:
                text _("{u}USE YOUR MOUSE TO CANCEL{/u}")
                text _("Press any key you would want to use.")
                text _("For multiple keys, hold the first key, then press the second key.")

            vbox:
                text _("Any key from [[a-z] to [[0-9], as well as 'ESCAPE' is usable.")
                text _("The 'alt' and 'shift' modifiers are also available.\n('shift' doesn't work with numbers)")
                text _("{u}In multiple key mode, the arrowkeys are available, while 'alt' and 'shift' aren't.{/u}")


        textbutton _("Double Key Mode: [double!t]") align (0.0, 1.0):
            text_font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
            text_style "key_input_text"
            text_color "#fff"
            text_align (0.5, 0.5)
            padding (10,10)
            background "#a7a7a7"

    on "show" action SetField(custom_keymap, "allowed", False)
    on "hide" action SetField(custom_keymap, "allowed", True)

style key_input_text is empty:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Light.ttf"
    outlines []
    color "#121212"
    size 21

style key_input_vbox is empty:
    spacing 6

screen keymap_preferences(gm):
    default double = False
    style_prefix "keymap"

    grid 2 2 align (0.5, 0.5):
        vbox:
            at keymap_appear(1)
            text _("VOLUME UP"):
                if gm:
                    color "#fff"
            for b, t in zip(
                ("increase_general_volume", "increase_music_volume", "increase_sfx_volume", "increase_ambient_volume"),
                (_("Increase General Volume"), _("Increase Music Volume"), _("Increase Sound Volume"), _("Increase Ambient Volume"))
            ):
                hbox:
                    # too lazy to do frame and shit
                    textbutton t:
                        if gm:
                            xsize 200 text_size 12
                    textbutton custom_keymap.current_key(b) at keybind_hover xsize 150 text_xalign 0.5:
                        action Show("register_keymap", Dissolve(0.1), bind=b, display_text=t, double=double, current=custom_keymap.current_key(b))
        vbox:
            at keymap_appear(3)
            text _("VOLUME DOWN"):
                if gm:
                    color "#fff"
            for b, t in zip(
                ("decrease_general_volume", "decrease_music_volume", "decrease_sfx_volume", "decrease_ambient_volume"),
                (_("Decrease General Volume"), _("Decrease Music Volume"), _("Decrease Sound Volume"), _("Decrease Ambient Volume"))
            ):
                hbox:
                    textbutton t:
                        if gm:
                            xsize 200 text_size 12
                    textbutton custom_keymap.current_key(b) at keybind_hover xsize 150 text_xalign 0.5:
                        action Show("register_keymap", Dissolve(0.1), bind=b, display_text=t, double=double, current=custom_keymap.current_key(b))
        vbox:
            at keymap_appear(2)
            text _("MISC"):
                if gm:
                    color "#fff"
            for b, t in zip(
                ("toggle_fullscreen", "iconify", "screenshot", "afm", "mute_all"),
                (_("Toggle Fullscreen"), _("Iconify"), _("Screenshot"), _("Toggle Auto-Forward Mode"), _("Mute All"))
            ):
                hbox:
                    textbutton t:
                        if gm:
                            xsize 200 text_size 12
                    textbutton custom_keymap.current_key(b) at keybind_hover xsize 150 text_xalign 0.5:
                        action Show("register_keymap", Dissolve(0.1), bind=b, display_text=t, double=double, current=custom_keymap.current_key(b))
        vbox:
            at keymap_appear(4)
            text _("MENU SHORTCUTS"):
                if gm:
                    color "#fff"
            for b, t in zip(
                ("save_menu", "settings"),
                (_("Open Save Menu"), _("Open Settings"))
            ):
                hbox:
                    textbutton t:
                        if gm:
                            xsize 200 text_size 12
                    textbutton custom_keymap.current_key(b) at keybind_hover xsize 150 text_xalign 0.5:
                        action Show("register_keymap", Dissolve(0.1), bind=b, display_text=t, double=double, current=custom_keymap.current_key(b))

    hbox align (0.5, 0.9):
        at keymap_appear(5)
        textbutton _("Double Key") at keybind_hover:
            style_prefix "display"
            action ToggleLocalVariable("double")

        textbutton _("Reset") at keybind_hover:
            style_prefix "display"
            action Confirm(message=_("Reset the keymap to its original settings?"), yes_action=(Function(custom_keymap.reset), Hide("confirm")), no_action=Hide("confirm"))

transform keymap_appear(i):
    alpha 0.0
    i / 20
    ease 0.2 alpha 1.0

screen keymap():
    use keymap_preferences(False)
        
transform keybind_hover():
    on idle:
        easein_quint 0.5 matrixcolor BrightnessMatrix(0.0)
    on hover:
        easein_quint 0.5 matrixcolor BrightnessMatrix(-0.1)

style keymap_grid is empty:
    spacing 20

style keymap_button is empty:
    xpadding 5
    background Solid("#E8E8E8")
    xysize (400, 22)

style keymap_text is empty:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"
    outlines []
    color "#121212"
    size 21

style keymap_button_text is keymap_text:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
    size 16
    yalign 0.5

style keymap_vbox is empty:
    first_spacing 2
    spacing 5

style keymap_hbox is empty:
    spacing 3
