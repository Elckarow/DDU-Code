screen base_confirm_dialog():
    add "gui/overlay/confirm.png"
    
    frame:
        background Frame([ "gui/confirm_frame.png", "gui/frame.png" ], left=Borders(40, 40, 40, 40))
        padding (40, 40)
        align (0.5, 0.5)

        transclude

screen dialog(message, ok_action):
    modal True zorder 501

    use base_confirm_dialog():
        style_prefix "confirm"

        vbox:
            text "[message!t]" style "confirm_prompt"

            textbutton _("OK") action ok_action xalign 0.5
    
    on "hide" action With(config.enter_yesno_transition)

screen confirm(message, yes_action, no_action):
    modal True zorder 501

    use base_confirm_dialog():
        style_prefix "confirm"

        vbox:
            text "[message!t]" style "confirm_prompt"

            hbox:
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    on "hide" action With(config.enter_yesno_transition)

style confirm_vbox:
    align (0.5, 0.5)
    spacing 30

style confirm_prompt is say_dialogue:
    color "#000"
    outlines []
    layout "subtitle"

style confirm_hbox:
    xalign 0.5
    spacing 100

style confirm_button:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text:
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, gui.accent_outlines_color, 0, 0), (2, gui.accent_outlines_color, 2, 2)]
    hover_outlines [(4, gui.accent_outlines_hover_color, 0, 0), (2, gui.accent_outlines_hover_color, 2, 2)]