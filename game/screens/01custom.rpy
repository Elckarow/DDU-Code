python early:
    renpy.register_sl_statement("s_label", 0).add_positional("txt").add_property_group("position").add_property_group("ui")

screen s_label(txt, **properties):
    style_prefix "s_label"

    fixed:
        style "s_label_fixed_main"
        properties properties
        
        hbox:
            spacing 6

            fixed at Flatten:
                style "s_label_fixed_icon"

                add Solid("#97b4d6"):
                    subpixel True
                    xysize (12, 12)

                add Solid("#5987ff"):
                    subpixel True
                    xysize (9, 9)
                    xpos 12
                    yalign 1.0

                add Solid("#004eff"):
                    subpixel True
                    xysize (5, 5)
                    xalign 1.0
                    ypos 6

            text "[txt!t]"


style s_label_fixed_main:
    fit_first True

style s_label_fixed_icon:
    xysize (24, 20)
    yalign 0.5

style s_label_text is default:
    color "#150087"
    outlines [ ]
    size 28

style s_label_hbox:
    spacing 10
