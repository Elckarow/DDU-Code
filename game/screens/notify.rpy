transform notify_appear:
    yanchor 1.0 ypos 0.0 alpha 0.0 
    on show:
        easein 0.5 alpha 1.0 yanchor 0.0
    on hide:
        easeout 0.5 alpha 0.0 yanchor 1.0

define NOTIFY_TIMER = 2.4

screen base_notify(message):
    style_prefix "notify"
    frame:
        text message

style notify_frame is empty:
    background UIDisplayable(RoundedFrame(Solid("#fff"), radius=(20, 0, 0, 0)))
    padding (16, 5)

style notify_text is default:
    size gui.notify_text_size

screen notify(message):
    zorder 400

    fixed at notify_appear:
        use base_notify(message)
    
    timer NOTIFY_TIMER action Hide("notify")

screen screenshot_notify(d, message):
    zorder 400

    vbox at (Flatten, notify_appear):
        use base_notify(message)
        add Thumbnail(d)
    
    timer NOTIFY_TIMER action Hide("screenshot_notify")