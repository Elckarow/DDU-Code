define NOTIFY_TIMER = 1.8

screen base_notify(message):
    frame style_prefix "notify":
        text message

    add "#00000090" xysize (500, 10) yoffset 45 at unfurl()
    add "#00000090" xysize (300, 10) yoffset 58 at unfurl(t=0.1)

screen notify(message):
    zorder 400

    fixed at notify_appear:
        use base_notify(message)

    timer NOTIFY_TIMER action Hide("notify")

screen screenshot_notify(d, message):
    zorder 400

    gradient "#000" "#fff0" theta 270 xoffset -200 at notify_gradient
    gradient "#000" "#fff0" theta 90 xoffset 200 at notify_gradient

    frame:
        use base_notify(message)
        at screenshot_appear(direction=-1)
        
    add Frame(d, xysize=(256, 144)) at screenshot_appear(direction=1)

    timer NOTIFY_TIMER action Hide("screenshot_notify")

style notify_frame is empty:
    background "#00000090"
    yoffset 10
    padding (16, 5)

style notify_text is empty:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Medium.ttf"
    color "#fff"
    outlines []
    size gui.notify_text_size

transform notify_appear:
    subpixel True
    yanchor 1.0 ypos 0.0 alpha 0.0
    on show:
        easein_quint 0.5 alpha 1.0 yanchor 0.0
    on hide:
        easeout 0.5 alpha 0.0 yanchor 1.0

transform notify_gradient:
    alpha 0.25
    on show:
        alpha 0.0
        easein_quint 0.5 alpha 0.2
    on hide:
        easeout 0.5 alpha 0.0

transform screenshot_appear(direction=1):
    yalign 0.0 xoffset direction * 30 alpha 1.0 xalign 1.0
    on show:
        alpha 0.0
        easein_quint 0.5 xoffset 0 alpha 1.0
    on hide:
        easein_quint 0.5 xoffset direction * 30 alpha 0.0
