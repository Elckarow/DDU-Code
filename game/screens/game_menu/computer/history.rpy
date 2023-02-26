screen history():
    predict False tag menu

    use game_menu(SettingsMenuInfo, menu_style="computer"):
        style_prefix "history"
        
        viewport id "history_vp":
            mousewheel True
            draggable True
            yinitial 1.0

            vbox:
                if not _history_list:
                    text _("The dialogue history is empty."):
                        style "history_empty"
            
                else:
                    for h in _history_list:
                        vbox:
                            style "history_vbox_dialogue"

                            if h.who:
                                text h.who style "history_name":
                                    outlines [(3, h.pov_color, 0, 0), (1, h.pov_color, 1, 1)]

                            text h.what
        
        vbar value YScrollValue("history_vp") style "history_vbar"

    key ["repeat_K_UP", "K_UP"] action Scroll("history_vp", "vertical decrease", 20)
    key ["repeat_K_DOWN", "K_DOWN"] action Scroll("history_vp", "vertical increase", 20)

style history_viewport:
    yfill True
    xalign 0.5
    xsize 750

style history_vbox:
    spacing 15
    xalign 0.5
    xfill True

style history_vbox_dialogue is history_vbox:
    spacing -3

style history_text:
    xalign 0.5
    text_align 0.5

style history_name is say_label

style history_empty is history_text:
    size 30

style history_vbar is vscrollbar:
    align (1.0, 0.5)
    yfill True