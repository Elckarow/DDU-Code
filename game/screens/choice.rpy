screen choice(items, voice=None):
    default l = len(items)
    default margin = 30
    default trans_time = 0.3

    style_prefix "choice"

    add "#000":
        at transform:
            on show:
                alpha 0.0
                easein trans_time alpha 0.5
            on hide:
                easeout trans_time alpha 0.0

    fixed yanchor 1.0 ypos gui.textbox_ypos:
        xoffset gui.xoffset_due_to_side_image

        fixed fit_first "height" yalign 1.0:
            vbox:
                xalign 0.24
                spacing 20 + int(18 * (1 / l))

                null height margin

                for i, item in enumerate(items):
                    frame style "empty":
                        at transform:
                            alpha 0.0 xoffset -10.0
                            (l - i) / 15
                            easein_quart trans_time * (4 / 3) alpha 1.0 xoffset 0.0

                        button action item.action:
                            at transform:
                                on idle:
                                    easeout 0.15 matrixcolor BrightnessMatrix(0.0) xoffset 0.0
                                on hover:
                                    easein 0.15 matrixcolor BrightnessMatrix(0.3) xoffset 5.0

                            rectangle "#ccc" border 2

                            text item.caption style "choice_button_text"
                
                null height margin
            
            vbox xsize 15 xalign 0.14 yalign 1.0:
                at transform:
                    ysize 0.0
                    easein trans_time ysize 1.0

                # circle color "#fff" border 1

                add "#fff" xsize 2 xalign 0.5

    if voice is not None:
        on "show" action PlayCharacterVoice(*voice)
        on "hide" action Stop("voice")

style choice_vbox is empty
style choice_fixed is empty

style choice_button:
    ysize 40 xsize 300
    background "#0000009a"
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style choice_button_text is say_dialogue:
    outlines []
    yalign 0.5
    xalign 0.0
    color "#fff"
    xoffset 20
