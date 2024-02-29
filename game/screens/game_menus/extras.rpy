define extra_buttons = (
    (_("Companion Chronicles"), Show("dialog", message=_("Feature is not available at this time.")), 65),
    (_("Opening"), Show("dialog", message=_("Feature is not available at this time.")), 90),
    (_("Games"), Show("dialog", message=_("Feature is not available at this time.")), 115),
    (_("Music Room"), Show("dialog", message=_("Feature is not available at this time.")), 245),
    (_("Gallery"), ShowMenu("gallery"), 270),
    (_("Characters"), ShowMenu("character_preview", _transition=Dissolve(0.2)), 295),
)

screen extras():
    tag menu

    use game_menu():
        circle align (0.5, 0.5) radius 256

        for i, (extra_text, extra_action, degree) in enumerate(extra_buttons):
            button:
                background Solid("#FDFDFD")
                add Solid("#000000", xysize=(149, 2))
                xysize (238,63) anchor (0.5, 0.5)
                text extra_text style "extra_text"
                action extra_action

                at transform:
                    subpixel True
                    around (0.5, 0.5) angle degree
                    radius absolute(256 + 130) alpha 0.0
                    0.4 + (i / 10)
                    easein_quart 0.5 radius absolute(256 + 180) alpha 1.0

                    on hover:
                        easein_quart 0.5 matrixcolor BrightnessMatrix(-0.05)
                    on idle:
                        easein_quart 0.5 matrixcolor BrightnessMatrix(0.0)

        #the sticks
        add "#000":
            at transform:
                RoundedCorners(6)
                xysize (9, 68)
                subpixel True anchor (0.5, 0.5) around (0.5, 0.5) radius absolute(200 + (0.75 / 2) + 6) alpha 0.0 matrixtransform RotateMatrix(0, 0, 135) angle -45
                0.5
                easein_quart 0.5 radius absolute(200 + (0.75 / 2)) alpha 1.0

        add "#000":
            at transform:
                RoundedCorners(6)
                xysize (9, 68)
                subpixel True anchor (0.5, 0.5) around (0.5, 0.5) radius absolute(200 + (0.75 / 2) + 6) matrixtransform RotateMatrix(0, 0, 135) angle 135 alpha 0.0
                0.5
                easein_quart 0.5 radius absolute(200 + (0.75 / 2)) alpha 1.0

        circle color "#000" radius 7 align (0.5, 0.5)

        circle:
            color "#000" border 2 xysize (180, 180) anchor (0.5, 0.5) pos (0.5, 0.5)
            at transform:
                subpixel True zoom 0.8 alpha 0.0
                0.3
                easein_quart 0.5 zoom 1.0 alpha 1.0
        circle:
            color "#000" border 2 xysize (30, 30) anchor (0.5, 0.5) pos (0.5, 0.5)
            at transform:
                subpixel True zoom 0.8 alpha 0.0
                0.4
                easein_quart 0.5 zoom 1.0 alpha 1.0

        add "mod_assets/STUFF/main_menu/triangle.png" anchor (0.5, 0.5) pos (0.5, 0.448) xysize (20,15) yzoom -1 xoffset 1:
            at transform:
                subpixel True alpha 0.0 yoffset -10
                0.5
                easein_quart 0.5 yoffset 0 alpha 1.0

        default xof = 0.22
        default yof = 0.01
        #the numbers
        add Solid("#fff", xysize=(90,128)) anchor (0.5, 0.5) pos (0.135 + xof, 0.5 + yof)
        text "01" style "version_num" pos (0.135 + xof, 0.495 + yof) anchor (0.5, 0.5)

        add "mod_assets/STUFF/main_menu/number_holder.png" anchor (0.5, 0.5) pos (0.135 + xof, 0.54 + yof)
        text "3.012" style "version_num" color "#fff" size 15 anchor(0.5, 0.5) pos (0.1364 + xof, 0.54 + yof) yoffset 1
        text "5.122" style "version_num" size 15 anchor(0.5, 0.5) pos (0.1364 + xof, 0.57 + yof) yoffset -3
        #squares
        add "mod_assets/STUFF/main_menu/cross.png" anchor (0.5, 0.5) pos (0.12 + xof, 0.445 + yof)
        #row1
        add Solid("#000", xysize=(12, 3)) anchor (0.0, 0.5) pos (0.133 + xof, 0.432 + yof) at unfurl
        add Solid("#000", xysize=(19, 3)) anchor (0.0, 0.5) pos (0.146 + xof, 0.432 + yof) at unfurl(0.3)
        #row2
        add Solid("#000", xysize=(19, 3)) anchor (0.0, 0.5) pos (0.133 + xof, 0.442 + yof) at unfurl(0.35)
        add Solid("#000", xysize=(12, 3)) anchor (0.0, 0.5) pos (0.149 + xof, 0.442 + yof) at unfurl(0.45)
        #row3
        add Solid("#000", xysize=(12, 3)) anchor (0.0, 0.5) pos (0.133 + xof, 0.452 + yof) at unfurl(0.33)

        for speed, _zoom, on_hide_time in (
            (0.3, 0.7, 0.3),
            (1,  0.96, 0.4),
            (4,   1.0, 0.5)
        ):
            circle color "#000" radius 140 length 0.25 border 3 align (0.5, 0.5):
                at transform:
                    parallel:
                        zoom 0.0 alpha 0.0
                        easein_cubic 0.8 zoom _zoom alpha 1.0
                    parallel:
                        function RotateMouseSmooth(0, speed, ypos=config.screen_height * 0.55)

style extra_text:
    color "#000"
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Medium.ttf"
    size 21
    outlines []
    align (0.5, 0.5)
    text_align 0.5
