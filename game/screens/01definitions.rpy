init offset = -5

init python:
    _("True")
    _("False")

style default:
    font gui.default_font
    size gui.text_size
    color "#fff"
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style button is empty:
    properties gui.button_properties("button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style no_sound is button:
    hover_sound None
    activate_sound None

style frame is empty

image _bar_thumb = Solid("#737373")
image _bar_base = Solid("C7C7C7")
image _bar_top = Solid("#737373")

transform _bar_hover:
    matrixcolor BrightnessMatrix(-0.1)

style bar is empty:
    ysize gui.bar_size
    thumb "_bar_thumb"
    hover_thumb At("_bar_thumb", _bar_hover)
    base_bar "_bar_base"
    hover_base_bar At("_bar_base", _bar_hover)

style scrollbar is empty:
    ysize gui.bar_size
    thumb "_bar_thumb"
    hover_thumb At("_bar_thumb", _bar_hover)
    base_bar "_bar_base"
    hover_base_bar At("_bar_base", _bar_hover)
    unscrollable "hide"
    bar_invert True

style slider is empty:
    ysize gui.bar_size
    top_bar "_bar_top"
    hover_top_bar At("_bar_top", _bar_hover)
    bottom_bar "_bar_base"
    hover_bottom_bar At("_bar_base", _bar_hover)


style vbar is bar:
    xsize gui.bar_size ysize None

style vscrollbar is scrollbar:
    xsize gui.bar_size ysize None

style vslider is slider:
    xsize gui.bar_size ysize None

#############################################################################################################
#############################################################################################################
#############################################################################################################

init python:
    def LocalVariableValue(name, range, max_is_zero=False, style="bar", offset=0, step=None, action=None, force_step=False):
        return DictValue(
            dict=sys._getframe(1).f_locals,
            key=name,
            range=range,
            max_is_zero=max_is_zero,
            style=style,
            offset=offset,
            step=step, 
            action=action,
            force_step=force_step
        )

    def Confirm(*args, **kwargs):
        return Show("confirm", config.enter_yesno_transition, *args, **kwargs)

    def Dialogue(*args, **kwargs):
        return Show("dialog", config.enter_yesno_transition, *args, **kwargs)

    def MenuReturn(value=None):
        return [Return(value), If(store.main_menu, true=With(config.exit_transition))]

#############################################################################################################
#############################################################################################################
#############################################################################################################
