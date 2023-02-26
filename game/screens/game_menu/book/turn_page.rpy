screen book_turn_page(action1, action2):
    imagebutton:
        at transform:
            subpixel True
            xalign 0.0
            ypos 0.017 yanchor 0.0
        idle Transform(Solid("#fff"), alpha=0.0)
        hover Fixed(Transform(Solid("#fff"), alpha=0.3, subpixel=True, perspective=True, matrixtransform=Matrix.rotate(0.0, -48.0, 0.0)))
        activate_sound audio.page_turn
        xysize (40, 0.95)
        action action1
        keyboard_focus False
    
    imagebutton:
        at transform:
            subpixel True
            xalign 1.0
            ypos 0.017 yanchor 0.0
        idle Transform(Solid("#fff"), alpha=0.0)
        hover Fixed(Transform(Solid("#fff"), alpha=0.3, subpixel=True, perspective=True, matrixtransform=Matrix.rotate(0.0, 40.0, 0.0)))
        activate_sound audio.page_turn
        xysize (36, 0.95)
        action action2
        keyboard_focus False
