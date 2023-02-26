screen computer_description():
    style_prefix "computer_description"

    default text = None
    $ text = GetTooltip()

    nearrect:
        focus "tooltip"

        showif text is not None:
            frame:
                text "[text!t]"

style computer_description_frame:
    background RoundedFrame(Solid("#fff"), radius=10)
    padding (13, 9)
    align (0.0, 1.0)

style computer_description_text is say_dialogue:
    yalign 0.5