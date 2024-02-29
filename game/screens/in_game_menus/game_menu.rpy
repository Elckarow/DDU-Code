screen ig_game_menu():
    default nav_entries = (
        (_("History"), ShowMenu("ig_history")),
        (_("Save States"), ShowMenu("ig_file_slots")),
        (_("Configuration"), ShowMenu("ig_configuration")),
        (_("Main Menu"), Confirm(layout.MAIN_MENU, Call("main_menu_return"))),
        (_("Quit"), Quit()),
    )
    default outlines_width = 2

    add "#000":
        at transform:
            on default:
                alpha 0.75
            on show:
                alpha 0.0
                easein_quint 0.5 alpha 0.75

    fixed xysize (920, 607) anchor (0.0, 0.5) pos (0.05, 0.5):
        use game_menu_border_with_anim(outlines_width)

        frame style "empty" padding (outlines_width, outlines_width) xysize (1.0, 1.0):
            transclude

    text phone.system.get_date().strftime(__(phone.config.date_format)) style "empty":
        font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Light.ttf"
        color "#fff"
        outlines []
        size 20 yalign 0.255 xanchor 0.0 xpos 0.8
    text phone.system.get_date().strftime(__(phone.config.time_format)) style "clock" yalign 0.3 xanchor 0.0 xpos 0.8

    fixed style "empty":
        fit_first True xanchor 0.0 xpos 0.8 ycenter 0.56
        
        vbox style "empty" spacing 1 yoffset 1 xoffset 40:
            for i, (nav_text, nav_action) in enumerate(nav_entries):
                textbutton nav_text:
                    action nav_action
                    text_style "ig_navigation"
                    text_hover_underline True
        
        vbox style "empty":
            at transform:
                subpixel True yalign 0.5
                yzoom 0.0 alpha 0.0
                0.3
                easein_quart 0.5 alpha 1.0 yzoom 1.0

            fixed style "empty" yoffset -5 xysize (15, 15):
                circle border 1
                circle xysize (3, 3) align (0.5, 0.5)

            add "#fff" xysize (1, 1.0) xalign 0.5

            fixed style "empty" yoffset 5 xysize (15, 15):
                circle border 1
                circle xysize (3, 3) align (0.5, 0.5)

    hbox spacing 2 yalign 0.8 xanchor 0.0 xpos 0.8:
        at transform:
            alpha 0.0
            0.6
            alpha 1.0

    button background "#fff" action MenuReturn():
        xysize (108, 31) yalign 0.8 xanchor 0.0 xpos 0.8
        
        at transform:
            parallel:
                0.66
                easein_quart 0.5 alpha 1.0
            parallel:
                on idle:
                    matrixcolor BrightnessMatrix(0.0)
                on hover:
                    matrixcolor BrightnessMatrix(-0.2)

        text _("RETURN") style "return_button_text"

screen game_menu_border_with_anim(outlines_width):
    add Solid("#fff", xsize=outlines_width) xalign 0.0:
        at transform:
            subpixel True
            ysize 0.0
            0.25
            easein_quint 0.4 ysize 1.0

    add Solid("#fff", xsize=outlines_width) xalign 1.0:
        at transform:
            subpixel True
            ysize 0.0
            0.5
            easein_quint 0.4 ysize 1.0

    add Solid("#fff", ysize=outlines_width) yalign 0.0:
        at transform:
            subpixel True
            xsize 0.0
            0.25
            easein_quint 0.4 xsize 1.0

    add Solid("#fff", ysize=outlines_width) yalign 1.0:
        at transform:
            subpixel True
            xsize 0.0
            0.5
            easein_quint 0.4 xsize 1.0

style clock:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"
    size 80
    text_align 0.0
    outlines []
    color "#fff"

style ig_label:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"
    outlines []
    color "#000"
    align (0.5, 0.5)
    size 20
    text_align 0.5

style return_button_text:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf"
    color "#000"
    outlines []
    size 18
    align (0.5, 0.5)
    text_align 0.5
    kerning -1

style ig_navigation:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Medium.ttf"
    color "#fff"
    outlines []
    size 18
    text_align 0.0
    kerning -1
