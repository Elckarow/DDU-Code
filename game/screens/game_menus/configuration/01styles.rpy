style pref_text is empty:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Medium.ttf"
    color "#000" selected_color "#fff"
    outlines []
    align (0.5, 0.5) text_align 0.5
    layout "tex"
    size 18

style pref_button:
    background Solid("#E8E8E8")
    selected_background Solid("#868686")

style pref_button_text is pref_text

style pref_label is empty
style pref_label_text is pref_text:
    size 20 text_align 0.0 xalign 0.0

style pref_slider is slider