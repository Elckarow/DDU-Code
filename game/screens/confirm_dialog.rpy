screen base_confirm_dialog():
    add Solid("#00000040") at base_confirm_bg_show
    frame at [Flatten, confirm_dialog_show]:
        align (0.5, 0.5)
        xysize (700, 300)
        background Solid("#FDFDFD")

        add Solid("#000", xysize=(125, 3)) at unfurl
        add Solid("#000", xysize=(300, 1)) at unfurl

        transclude

screen dialog(message, ok_action=Hide("dialog")):
    modal True zorder 501

    use base_confirm_dialog():
        style_prefix "confirm"

        vbox:
            text message style "confirm_prompt"

            button at confirm_popup:
                style "confirm_button_ok"
                text _("OK") style "load_option"
                action ok_action

screen confirm(message, yes_action, no_action=Hide("confirm")):
    modal True zorder 501

    use base_confirm_dialog():
        style_prefix "confirm"

        vbox:
            spacing 60
            text message style "confirm_prompt"

            hbox at confirm_popup:
                spacing 5
                button:
                    style "confirm_button_yes"
                    text _("YES") style "load_option"
                    action yes_action
                button:
                    style "confirm_button_no"
                    text _("NO") style "load_option"
                    action no_action

transform confirm_popup:
    subpixel True
    yoffset 30 alpha 0.0
    easein_quart 0.4 alpha 1.0 yoffset 0

transform base_confirm_bg_show:
    on show:
        alpha 0
        easein_quart 0.4 alpha 1.0
    on hide:
        easein_quart 0.4 alpha 0.0

transform confirm_dialog_show:
    subpixel True
    on show:
        alpha 0.0 zoom 0.8
        easein_quart 0.4 alpha 1.0 zoom 1.0
    on hide:
        easein_quart 0.4 alpha 0.0 zoom 0.8

style confirm_vbox:
    align (0.5, 0.5)
    spacing 30

style confirm_prompt:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
    align (0.5,0.5)
    text_align 0.5
    size 20
    color "#000"
    outlines []
    layout "subtitle"

style confirm_hbox:
    xalign 0.5
    spacing 100

style confirm_button:
    # hover_sound gui.hover_sound
    # activate_sound gui.activate_sound
    xysize (257, 48)

style confirm_button_yes is confirm_button:
    hover_background Solid("#414141")
    background Solid("#41414190")

style confirm_button_ok is confirm_button_yes:
    xalign 0.5

style confirm_button_no is confirm_button:
    hover_background Solid("#797979")
    background Solid("#79797980")
