screen configuration():
    tag menu
    # predict False

    default screens = (
        ("display", "display_configuration"),
        ("audio", "audio_configuration"),
    ) + ((("keybinds", "keymap"),) if not is_android() else ())
    default screen_to_use = screens[0][1]

    use game_menu():
        frame style "empty":
            yalign 0.105 xpos 0.108 xanchor 0.0 background None

            vbox xsize 1.0:
                hbox style_prefix "pref":
                    spacing gui.config_nav_buttons_spacing

                    for name, s in screens:
                        textbutton __(name).upper() at tab_hover xysize gui.config_nav_buttons_size:
                            action (
                                If(s != screen_to_use, SetScreenVariable("screen_to_use", s)),
                                SelectedIf(s == screen_to_use),
                            )

                add Solid("#000"):
                    at transform:
                        subpixel True ysize 1 nearest True
                        xsize 0.0 yoffset 3
                        easein_quart 0.8 xsize 1.0

        use expression screen_to_use pass ()

transform tab_hover():
    alpha 0.4
    on hover:
        easein_quart 0.5 alpha 0.8
    on idle:
        easein_quart 0.5 alpha 0.4
    on selected_hover:
        easein_quart 0.5 alpha 0.8
    on selected_idle:
        easein_quart 0.5 alpha 1.0