screen game_menu(waves=True):
    use bar_template(waves)

    fixed style "empty":
        xysize (1280, 720 - 78) align (0.5, 1.0)
        transclude

screen bar_template(waves=True):
    default nav_entries = (
        (_("Launch"), ShowMenu("ch_select")),
        (_("Save States"), ShowMenu("load")),
        (_("Configuration"), ShowMenu("configuration")),
        (_("Resources"), ShowMenu("extras")),
        (_("Contributors"), ShowMenu("credits"))
    )

    add Solid("#F8F8F8")
    add SnowBlossom(
        d="pellets",
        border=229,
        xspeed=(0,0),
        yspeed=(20,100),
        start=5,
        fast=True,
        count=8
    )

    if waves:
        for i, time_bias in enumerate((0.513, 0.87, 0.34)):
            wave:
                color "#00000030"
                vertical False amplitude 12
                thickness 3 period 0.17
                time_bias time_bias
                offset i * 70
                yalign 0.56

    frame:
        background Solid("#010101")
        xysize (1280, 78)
        align (0.5, 0.0)

        button action MenuReturn():
            at transform:
                on hover:
                    easein_quart 0.5 matrixcolor BrightnessMatrix(-0.2)
                on idle:
                    easein_quart 0.5 matrixcolor BrightnessMatrix(0.0)

            ysize 50 yalign 0.5 xalign 0.05 xpadding 30
            background "#FDFDFD"

            text _("RETURN") style "bar_text" color "#000"

        hbox align (0.9, 0.5) spacing 35:
            for i, (nav_text, nav_action) in enumerate(nav_entries):
                button action nav_action:
                    ysize 78 xpadding 30
                    hover_background "nav_hovered"
                    selected_background "nav_hovered"
                    selected_hover_foreground "#ffffff18"

                    # very ugly ahh
                    if nav_text == nav_entries[3][0]:                         
                        selected any(renpy.get_screen(s[1].screen) is not None for s in extra_buttons if isinstance(s[1], ShowMenu)) or (renpy.get_screen(nav_entries[3][1].screen) is not None)

                    text __(nav_text).upper() style "bar_text"
                    
style bar_text:
    color "#fff"
    size 16
    align (0.5, 0.5)
    text_align 0.5
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf"
    outlines []
