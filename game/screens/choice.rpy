screen choice(items, voice=None):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton "[i.caption!t]":
                at transform:
                    on idle:
                        easeout 0.15 matrixcolor BrightnessMatrix(0.0)
                    on hover:
                        easein 0.15 matrixcolor BrightnessMatrix(0.3)

                action i.action
    
    if voice is not None:
        on "show" action PlayCharacterVoice(*voice)
        on "hide" action Stop("voice")

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5
    spacing 20
    xsize 390

style choice_button:
    background UIDisplayable(RoundedFrame(Solid("#fff"), radius=20))
    xfill True
    padding (20, 10)
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style choice_button_text is say_dialogue:
    outlines []
    yalign 0.5
    color "#000"