screen say(who, what):
    style_prefix "say"

    if who is not None:
        window:
            style "namebox"
            text who id "who":
                style "namebox_name"
                outlines [(3, pov_color(), 0, 0), (1, pov_color(), 1, 1)]

    window id "window":
        frame:
            text what id "what":
                if persistent.change_seen_text_color and renpy.is_seen():
                    color persistent.seen_text_color

    use quick_menu()

style say_frame is empty:
    xalign 0.5
    xpadding 4
    xmargin 38

style window:
    align (gui.textbox_xalign, gui.textbox_yalign)
    xysize (gui.textbox_width, gui.textbox_height)
    padding gui.textbox_padding
    background UIDisplayable(RoundedFrame(Solid("#fff"), radius=gui.textbox_round_radius))

style namebox:
    pos (gui.namebox_xpos, gui.namebox_ypos)
    anchor (0.0, 1.0)
    xysize (gui.namebox_width, gui.namebox_height)
    padding gui.namebox_padding
    background UIDisplayable(RoundedFrame(Solid("#fff"), radius=(0, 10, 0, 10)))

style say_label:
    color gui.name_color
    font gui.name_font
    size gui.name_text_size
    align (gui.name_xalign, gui.name_xalign)
    text_align gui.name_xalign

style say_dialogue is default:
    align (gui.text_xalign, gui.text_yalign)
    text_align gui.text_xalign
    layout "tex"

style say_glitch is say_dialogue:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]