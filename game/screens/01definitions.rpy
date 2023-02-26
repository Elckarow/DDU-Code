init offset = -5

init python:
    _("True")
    _("False")

init -10 python:
    def new_render(crend, shader):
        rv = renpy.Render(*crend.get_size())
        rv.mesh = True
        rv.blit(crend, (0, 0))
        rv.shaders = None
        rv.add_shader(shader)
        return rv

    def gaussian_blur_linear(render, blur):
        def apply_blur(render, blur, direction):
            rv = new_render(render, "shaders.gaussian_blur_linear")

            SIGMA = blur / 2.0
            rv.add_uniform("u_radius", blur)
            rv.add_uniform("u_lod_bias", 0.5)
            rv.add_uniform("u_sigma", SIGMA)
            rv.add_uniform("u_sqr_sigma", SIGMA * SIGMA)
            rv.add_uniform("u_direction", direction)
            return rv

        render = apply_blur(render, blur, (0.0, 1.0))
        rv     = apply_blur(render, blur, (1.0, 0.0))
        return rv
        
###################################################

    class GaussianBlur(renpy.display.core.Displayable):
        def __init__(self, blur, **kwargs):
            super(GaussianBlur, self).__init__(**kwargs)

            self.blur = blur
        
        def __call__(self, child):
            self.child = renpy.displayable(child)
            return self
        
        def render(self, w, h, st, at):
            cr = self.child.render(w, h, st, at)
            rv = gaussian_blur_linear(cr, self.blur)
            return rv

###################################################
    # WM's drop shadow code
    class Silhouette(renpy.display.core.Displayable):
        def __init__(self, child, color, **kwargs):
            super(Silhouette, self).__init__(**kwargs)
            self.child = renpy.displayable(child)
            self.color = Color(color)

        def render(self, width, height, st, at):
            cr = self.child.render(width, height, st, at)
            cw, ch = cr.get_size()

            rv = renpy.Render(cw, ch)
            rv.mesh = True
            rv.blit(cr, (0, 0))
            rv.add_shader("shaders.silhouette")
            rv.add_uniform("u_color", self.color)
            return rv

    class DropShadowCore(renpy.display.core.Displayable):
        def __init__(self, child, color="#000", xoffset=0, yoffset=0, blur=5.0, **kwargs):
            super(DropShadowCore, self).__init__(**kwargs)
            self.blur = blur
            self.xoffset = xoffset
            self.yoffset = yoffset

            self.child = renpy.displayable(child)
            self.shadow = Silhouette(child, Color(color))

        def shadow_render(self, width, height, st, at):
            cr = self.shadow.render(width, height, st, at)
            cw, ch = cr.get_size()

            rw = cw + self.blur * 2 * 40
            rh = ch + self.blur * 2 * 40

            rv = renpy.Render(rw, rh)
            rv.absolute_blit(cr, (self.blur * 40, self.blur * 40))

            return rv

        def render(self, width, height, st, at):
            cr = self.child.render(width, height, st, at)

            sr = self.shadow_render(width, height, st, at)
            sr = gaussian_blur_linear(sr, self.blur)

            rv = renpy.Render(*cr.get_size())
            rv.absolute_blit(sr, (-self.blur * 40 + self.xoffset, -self.blur * 40 + self.yoffset), focus=False, main=False)
            rv.blit(cr, (0, 0))

            return rv

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

    class DropShadow(object):
        def __init__(self, color="#000", xoff=0, yoff=0, blur=10.0, **kwargs):
            self.color = color
            self.xoff, self.yoff = xoff, yoff
            self.blur = blur
            self.kwargs = kwargs

        def __call__(self, child):
            return DropShadowCore(child, color=self.color, xoffset=self.xoff, yoffset=self.yoff, blur=self.blur, **self.kwargs)

###################################################
    # WM's rounded frame code
    class RoundedFrame(renpy.display.image.Frame):
        def __init__(self, image, *args, radius=0.0, **kwargs):
            super(RoundedFrame, self).__init__(image, *args, **kwargs)
            
            if not isinstance(radius, tuple):
                radius = (radius,) * 4

            self.radius = radius

        def render(self, width, height, st, at):
            rv = super(RoundedFrame, self).render(width, height, st, at)

            if self.radius:
                rv.mesh = True
                rv.add_property("gl_pixel_perfect", True)
                rv.add_property("gl_mipmap", False)
                rv.add_shader("shader.rounded_corners")
                rv.add_uniform("u_radius", self.radius)
                rv.add_property("texture_scaling", "nearest")

            return rv

###################################################

    def Thumbnail(d, zoom=1.0):
        return Transform(d, xysize=(config.thumbnail_width, config.thumbnail_height), zoom=zoom)

###################################################

    class POVDisplayable(renpy.display.layout.DynamicDisplayable):
        def __init__(self, d):
            self._child = renpy.displayable(d)

            super(POVDisplayable, self).__init__(self._render_function)
        
        def _render_function(self, st, at):
            return Transform(self._child, matrixcolor=TintMatrix(pov_color())), None

###################################################

    class UIDisplayable(renpy.display.layout.DynamicDisplayable):
        def __init__(self, d):
            self._child = renpy.displayable(d)

            super(UIDisplayable, self).__init__(self._render_function)
        
        def _render_function(self, st, at):
            return Transform(self._child, alpha=persistent.ui_alpha), 0.0

#############################################################################################################
#############################################################################################################
#############################################################################################################

style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style button:   
    properties gui.button_properties("button")

style button_text is default:
    yalign 0.5

style frame is empty

image _scrollbar_thumb = RoundedFrame(Solid("#004eff"), ysize=gui.bar_size, radius=gui.bar_radius * (5.0 / 8.0))
image _bar_base = RoundedFrame(VBox(Null(height=gui.bar_margin), Solid("#6c99ff"), Null(height=gui.bar_margin)), ysize=gui.bar_size, radius=gui.bar_radius)

image _vscrollbar_thumb = RoundedFrame(Solid("#004eff"), xsize=gui.bar_size, radius=gui.bar_radius * (5.0 / 8.0))
image _vbar_base = RoundedFrame(HBox(Null(width=gui.bar_margin), Solid("#6c99ff"), Null(width=gui.bar_margin)), xsize=gui.bar_size, radius=gui.bar_radius)

image _all_bar_top = RoundedFrame(Solid("#0045e0"), radius=gui.bar_radius)

style bar:
    thumb "_scrollbar_thumb"
    base_bar "_bar_base"

style scrollbar:
    thumb "_scrollbar_thumb"
    base_bar "_bar_base"
    unscrollable "hide"
    bar_invert True

style slider:
    ysize gui.bar_size
    top_bar "_all_bar_top"
    bottom_bar "_bar_base"
    
style vbar:
    thumb "_vscrollbar_thumb"
    base_bar "_vbar_base"

style vscrollbar:
    xsize gui.bar_size
    thumb "_vscrollbar_thumb"
    base_bar "_vbar_base"
    unscrollable "hide"
    bar_invert True

style vslider:
    xsize gui.bar_size
    top_bar "_all_bar_top"
    bottom_bar "_vbar_base"

#############################################################################################################
#############################################################################################################
#############################################################################################################

init python:
    class ScreenIcon(object):
        def __init__(self, idle, selected=None):
            self.idle = renpy.displayable(idle)
            self.selected = renpy.easy.displayable_or_none(selected) or self.idle
    
    icon_main_menu = ScreenIcon(
        Transform("mod_assets/STUFF/game_menu/icon_main_menu.png", align=(0.5, 0.5))
    )

    icon_return = ScreenIcon(
        Transform("mod_assets/STUFF/game_menu/icon_return.png", align=(0.5, 0.5))
    )
 
    icon_history = ScreenIcon(
        Transform("mod_assets/STUFF/game_menu/icon_history_idle.png", align=(0.5, 0.5)),
        Transform("mod_assets/STUFF/game_menu/icon_history_selected.png", align=(0.5, 0.5))
    )

    icon_audio = ScreenIcon(
        Transform("mod_assets/STUFF/game_menu/icon_audio_idle.png", align=(0.5, 0.5)),
        Transform("mod_assets/STUFF/game_menu/icon_audio_selected.png", align=(0.5, 0.5))
    )

    icon_text = ScreenIcon(
        Transform("mod_assets/STUFF/game_menu/icon_text_idle.png", align=(0.5, 0.5))
    )

    icon_display = ScreenIcon(
        Transform("mod_assets/STUFF/game_menu/icon_display_idle.png", align=(0.5, 0.5)),
        Transform("mod_assets/STUFF/game_menu/icon_display_selected.png", align=(0.5, 0.5))
    )

    icon_keymap = ScreenIcon(
        Transform("mod_assets/STUFF/game_menu/icon_keymap_idle.png", align=(0.5, 0.5))
    )

    icon_gallery = ScreenIcon(
        Text(_("Gallery"), style="game_menu_book_button_text"),
        Window(Text(_("Gallery"), style="game_menu_book_button_text"), style="screen_icon_book_selected")
    )

    icon_screenshot = ScreenIcon(
        Text(_("Screenshots"), style="game_menu_book_button_text"),
        Window(Text(_("Screenshots"), style="game_menu_book_button_text"), style="screen_icon_book_selected")
    )

    icon_characters = ScreenIcon(
        Text(_("Characters"), style="game_menu_book_button_text"),
        Window(Text(_("Characters"), style="game_menu_book_button_text"), style="screen_icon_book_selected")
    )

    icon_credits = ScreenIcon(
        Text(_("Credits"), style="game_menu_book_button_text"),
        Window(Text(_("Credits"), style="game_menu_book_button_text"), style="screen_icon_book_selected")
    )

    icon_extras = icon_save = ScreenIcon(
        Text(_("Extras"), style="game_menu_board_button_text")
    )

    icon_save = ScreenIcon(
        Text(_("Save"), style="game_menu_board_button_text")
    )

    icon_load = ScreenIcon(
        Text(_("Load"), style="game_menu_board_button_text")
    )

style screen_icon_book_selected:
    background Frame("gui/scrollbar/horizontal_poem_bar.png", ysize=3, yalign=1.0)

#############################################################################################################
#############################################################################################################
#############################################################################################################

init python:
    def Confirm(**kwargs):
        return Show("confirm", config.enter_yesno_transition, **kwargs)
    
    def Dialogue(**kwargs):
        return Show("dialog", config.enter_yesno_transition, **kwargs)

    def SaveMenu(*args, **kwargs):
        kwargs.setdefault("_transition", config.enter_transition)
        if store.main_menu:
            return ShowMenu("load", *args, **kwargs)
        return ShowMenu("save", *args, **kwargs)
        
    def SettingsMenu(*args, **kwargs):
        kwargs.setdefault("_transition", config.enter_transition)
        if store.main_menu:
            return ShowMenu("audio_settings", *args, **kwargs)
        return ShowMenu("history", *args, **kwargs)
    
    def ExtraMenu(*args, **kwargs):
        kwargs.setdefault("_transition", config.enter_transition)
        return ShowMenu("extras", *args, **kwargs)
    
    def CharactersMenu(*args, **kwargs):
        kwargs.setdefault("_transition", config.enter_transition)
        return ShowMenu("character_preview", *args, **kwargs)
    
    def GalleryMenu(*args, **kwargs):
        kwargs.setdefault("_transition", config.enter_transition)
        return ShowMenu("gallery", *args, **kwargs)
    
    # def OSTMenu(*args, **kwargs):
    #     kwargs.setdefault("_transition", config.enter_transition)
    #     return ShowMenu("music_room", *args, **kwargs)
    
    def CreditsMenu(*args, **kwargs):
        kwargs.setdefault("_transition", config.enter_transition)
        return ShowMenu("credits", *args, **kwargs)


    def MenuReturn(value=None):
        return [Return(value), If(store.main_menu, true=With(config.exit_transition))]

#############################################################################################################
#############################################################################################################
#############################################################################################################

init python:
    class ScreenMenuInfo(object):
        """
        `_screen`: str
            The name of a screen to show

        `_text`: str
            A text to display (not always used)

        `_icon`: ScreenIcon
            A ScreenIcon... Duh...

        `_condition`: str | None
            If not `None`, an expression that detemines whether the screen button should show or not.

        Other positional arguments and keyword arguments are passed to the screen when needed.
        """
        def __init__(self, _screen, _text, _icon, *args, _condition=None, **kwargs):
            if not renpy.has_screen(_screen):
                raise ValueError(f"screen {_screen!r} doesn't exist")
            if not isinstance(_text, basestring):
                raise TypeError(f"expected str, got {type(_text)}")
            if not isinstance(_icon, ScreenIcon):
                raise TypeError(f"expected ScreenIcon instance, got {type(_icon)}")
            
            self.screen = _screen
            self.text = _text
            self.icon = _icon

            self._condition = renpy.python.py_compile(_condition or "True", mode="eval")

            self.args = args
            self.kwargs = kwargs
        
        @property
        def condition(self):
            return renpy.python.py_eval_bytecode(self._condition)
                
        def get_action(self):
            """
            Called in the game menu.
            """
            kwargs = self.kwargs.copy()
            kwargs.setdefault("_transition", store.game_menu_transition)
            return ShowMenu(self.screen, *self.args, **kwargs)


    class GameMenuInfo(object):
        """
        Object passed to the game menu as the `game_menu_info` parameter.
        This should be the same for all screens that are showing "together".
        """
        def __init__(self, *args):
            for arg in args:
                if not isinstance(arg, ScreenMenuInfo):
                    raise TypeError(f"expected ScreenMenuInfo instance, got {type(arg)}")
                
            self.args = args
            self.len = len(args) - 1
        
        def _find_showing(self):
            for i, arg in enumerate(self.args):
                if renpy.get_screen(arg.screen) is not None:
                    return i
            
            return 0
        
        def next_screen(self):
            i = self._find_showing()

            for _ in range(self.len):
                i = i + 1 if i != self.len else 0
                info = self.args[i]

                if info.condition:
                    return info.get_action()
            
            return NullAction()
            
        def previous_screen(self):
            i = self._find_showing()

            for _ in range(self.len):
                i = i - 1 if i != 0 else self.len
                info = self.args[i]

                if info.condition:
                    return info.get_action()
            
            return NullAction()
            
    SaveMenuInfo = GameMenuInfo(
        ScreenMenuInfo("save", _("Save"), icon_save, _condition="not main_menu"),
        ScreenMenuInfo("load", _("Load"), icon_load)
    )

    if renpy.variant("pc"):
        SettingsMenuInfo = GameMenuInfo(
            ScreenMenuInfo("history", _("History"), icon_history, _condition="not main_menu"),
            ScreenMenuInfo("audio_settings", _("Audio"), icon_audio),
            ScreenMenuInfo("text_settings", _("Text"), icon_text),
            ScreenMenuInfo("display", _("Display"), icon_display),
            ScreenMenuInfo("keymap", _("Controls"), icon_keymap)
        )
    
    else:
        SettingsMenuInfo = GameMenuInfo(
            ScreenMenuInfo("history", _("History"), icon_history, _condition="not main_menu"),
            ScreenMenuInfo("audio_settings", _("Audio"), icon_audio),
            ScreenMenuInfo("text_settings", _("Text"), icon_text),
            ScreenMenuInfo("display", _("Display"), icon_display)
        )
    
    ExtraMenuInfo = GameMenuInfo(
        ScreenMenuInfo("extras", _("Extras"), icon_extras)
    )

    CreditsMenuInfo = GameMenuInfo(
        ScreenMenuInfo("credits", _("Credits"), icon_credits)
    )

    GalleryMenuInfo = GameMenuInfo(
        ScreenMenuInfo("gallery", _("Gallery"), icon_gallery),
        ScreenMenuInfo("screenshot_gallery", _("Screenshots"), icon_screenshot)
    )
 
    CharactersMenuInfo = GameMenuInfo(
        ScreenMenuInfo("character_preview", _("Characters"), icon_characters)
    )
