define ig_configuration_squares = 16

screen ig_display_configuration():
    use display_preferences(True)

screen ig_audio_configuration():
    use audio_preferences(True)

screen ig_voice_actors_configuration():
    use voice_actors_preferences(True)

screen ig_keymap():
    use keymap_preferences(True)

screen ig_configuration():
    # predict False 
    tag menu

    default pref_screens = (
        (_("display"), "ig_display_configuration"),
        (_("audio"), "ig_audio_configuration"),
        (_("voiceover"), "ig_voice_actors_configuration"),
    ) + (((_("keybinds"), "ig_keymap"),) if not is_android() else ())
    default used_screen = pref_screens[0][1]

    use ig_game_menu() id "ig_game_menu":
        frame xysize (300, 300) align (0.5, 0.5):
            for i in range(ig_configuration_squares):
                add Solid("#ffffff20", xysize=(10, 10)):
                    at silver_case_radial_circles(i)

        frame style "empty":
            align (0.5, 0.05)
            background None

            hbox style_prefix "ig_pref":   
                for name, s in pref_screens:
                    textbutton __(name).upper():
                        action (If(used_screen != s, SetScreenVariable("used_screen", s)), SelectedIf(used_screen == s))

                        at transform:
                            on idle:
                                matrixcolor BrightnessMatrix(0.0)
                            on hover:
                                matrixcolor BrightnessMatrix(-0.15)

        use expression used_screen pass ()

transform silver_case_radial_circles(i):
    subpixel True
    around (0.5, 0.5)
    angle (360 / ig_configuration_squares) * i
    matrixtransform RotateMatrix(0, 0, (360 / ig_configuration_squares) * i)

    parallel:
        linear 30 angle (360 / ig_configuration_squares) * i + 360 matrixtransform RotateMatrix(0, 0, (360 / ig_configuration_squares) * i + 360)
        angle (360 / ig_configuration_squares) * i matrixtransform RotateMatrix(0, 0, (360 / ig_configuration_squares) * i)
        repeat

    parallel:
        radius absolute(120)
        block:
            (i * 0.5)
            easein_quint 0.5 radius absolute(180)
            easein_quint 0.5 radius absolute(120)
            (ig_configuration_squares / 2.0) - (i * 0.5)
            repeat

style ig_pref_hbox is empty:
    spacing 2 xalign 0.18

style ig_pref_button is pref_button:
    xysize (169, 32)

style ig_pref_button_text is pref_text