screen ig_history():
    tag menu

    default padding = 3
    default entry_ysize = 136
    default namebox_ysize = 26
    default outlines_width = 2

    default l = len(_history_list)

    use ig_game_menu() id "ig_game_menu":
        style_prefix "history"

        frame style "empty" padding (padding, padding, padding * 2 + gui.bar_size, padding) xysize (1.0, 1.0):
            viewport id "history_vp":
                mousewheel True arrowkeys False
                draggable True
                yinitial 1.0

                vbox spacing 2:
                    for i, h in enumerate(_history_list):
                        # TODO button for voice
                        hbox spacing 2:
                            at transform:
                                xoffset -5.0 alpha 0.0
                                (l - i) * 0.11
                                easein 0.3 xoffset 0.0 alpha 1.0

                            fixed style "empty" yalign 1.0 xysize (entry_ysize, entry_ysize):
                                rectangle "#fff" border outlines_width:
                                    at transform:
                                        alpha 0.1

                                frame style "empty" padding (outlines_width, outlines_width):
                                    if h.say_side_image is not None:
                                        add h.say_side_image:
                                            at transform:
                                                alpha 0.95 mesh True gl_drawable_resolution False
                                                fit "contain"

                            vbox:
                                if h.who is not None:
                                    frame:
                                        xysize (200, namebox_ysize)
                                        background "#fff"
                                        text __(h.who).upper() style "history_name" align (0.5, 0.5)

                                frame style "empty":
                                    padding gui.textbox_padding
                                    background "#00000033"
                                    xysize (1.0, entry_ysize)
                                    text h.what

            vbar value YScrollValue("history_vp") style "history_vbar" xoffset padding:
                at history_vbar_hover
                at transform:
                    alpha 0.0 
                    easein 0.5 alpha 1.0

transform history_vbar_hover:
    alpha 0.4 matrixcolor InvertMatrix(1)
    on hover:
        easein_quint 0.5 alpha 0.6
    on idle:
        easein_quint 0.5 alpha 0.4

style history_name is say_label
style history_viewport:
    yfill True
    xalign 0.5

style history_text is say_dialogue:
    size 17

style history_vbar is vscrollbar:
    xpos 1.0 xanchor 0.0
    yfill True

style history_vbox is empty