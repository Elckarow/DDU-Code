transform skip_triangle(delay):
    subpixel True alpha 0.0
    pause delay

    block:
        easein 0.3 alpha 1.0 yoffset -7.0
        easeout 0.3 alpha 0.0 yoffset 0.0
        pause 0.6
        repeat

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame at notify_appear:
        hbox:
            text _("Skipping") style "skip_skipping"
            text "▸" at skip_triangle(0.1)
            text "▸" at skip_triangle(0.2)
            text "▸" at skip_triangle(0.3)

style skip_frame is notify_frame

style skip_hbox:
    spacing 6

style skip_skipping is notify_text
style skip_text is skip_skipping:
    font "DejaVuSans.ttf"