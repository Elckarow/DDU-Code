default side_image_at_list = [ ]

screen say(who, what):
    zorder 1
    style_prefix "say"

    gradient "#fff0" "#fff" yoffset 600
    
    hbox style "empty":
        xalign 0.5 yanchor 0.0 ypos gui.textbox_ypos
        spacing gui.side_image_spacing

        fixed style "empty" xysize (gui.textbox_height, gui.textbox_height):
            add gui.textbox_background

            frame style "empty" xysize (1.0, 1.0):
                foreground Rectangle("#fff", 2) padding (2, 2)

                add SideImage():
                    at side_image_at_list
                    at transform:
                        fit "contain" align (0.5, 0.5)

        fixed style "empty":
            fit_first True
        
            window id "window":
                text what id "what":
                    if persistent.change_seen_text_color and renpy.is_seen():
                        color persistent.seen_text_color
        
            if who is not None:
                window style "namebox":
                    text __(who).upper() id "who"

            add "#fff" ysize 2 

            use quick_menu()

screen say_overlay():
    zorder 2

    default yoffset = -20

    $ skipping = renpy.is_skipping()
    $ skipping_or_afm = skipping or _preferences.afm_enable

    showif _window and not _windows_hidden:
        fixed style "empty":
            at transform:
                xysize (60, 60) align (0.86, 0.99)
                xoffset gui.xoffset_due_to_side_image

            if skipping_or_afm:
                at transform:
                    easein_quint 0.5 yoffset yoffset
            else:
                at transform:
                    easein_quint 0.5 yoffset 0

            fixed style "empty":
                if renpy.get_screen("ctc") is not None and not skipping_or_afm:
                    at transform:
                        easein_quad 0.5 alpha 0.8
                else:
                    at transform:
                        easein_quad 0.25 alpha 0.3

                circle align (0.5, 0.5) xysize (5, 5)
                circle border 1 radius 9 align (0.5, 0.5)

                circle border 1 length 0.25 radius 15 align (0.5, 0.5) at Transform(alpha=0.3):
                    if skipping:
                        at transform:
                            linear 0.3 rotate 360
                            rotate 0
                            repeat
                    else:
                        at transform:
                            easein_quint 2.0 rotate 360
                            rotate 0
                            1.0
                            repeat

                add Solid("#fff", xysize=(40, 1)) align (0.0, 0.5) xoffset -20
                
                add "#fff":
                    at transform:
                        align (0.0, 0.5) xoffset -28 xysize (3, 3)
                        RoundedCorners(2)

        showif skipping_or_afm:
            frame style "empty" padding (2, 2):
                xoffset 88 + gui.xoffset_due_to_side_image

                at transform:
                    subpixel True align (0.75, 0.987) alpha 0.0
                    on show:
                        easein_quart 0.5 yoffset yoffset alpha 0.3
                    on hide:
                        easein_quart 0.5 yoffset 0 alpha 0.0

                background Rectangle("#fff") 
                add "loading_bar"

define config.always_shown_screens += ["say_overlay"]

image loading_bar = Flatten(HBox(*[At(Solid("#fff", xysize=(8, 8)), loading_bar_trans(i)) for i in range(26)], spacing=1))

transform loading_bar_trans(delay=0):
    alpha 0.0
    pause delay / 30
    easein_quint 0.5 alpha 1.0
    easein_quint 0.5 alpha 0.0
    pause (26 - delay) / 30
    repeat

style window is empty:
    xysize (gui.textbox_width, gui.textbox_height)
    padding gui.textbox_padding
    background gui.textbox_background

style say_dialogue is empty:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Medium.ttf"
    size gui.text_size
    outlines [(2, "#000000aa", 0, 0)]
    align (0.0, 0.0)
    text_align 0.0
    layout "tex"

style say_label is empty:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"
    outlines [] color "#000"
    size gui.namebox_text_size
    text_align 0.5 align (0.5, 0.5)

style say_glitch is say_dialogue:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]

style namebox is empty:
    pos (0.0, 0.0) anchor (0.0, 1.0)
    xysize (gui.namebox_width, gui.namebox_height)
    background "#fff"