default -5 persistent.mouse_hide_time = 30
default -1 persistent.character_blink = True
default persistent.seen_text_color = Color("#fff")

transform display_appear(i):
    alpha 0.0 xoffset -10
    i / 15
    ease 0.2 alpha 1.0 xoffset 0

screen select_language(translations):
    modal True zorder 150
    style_prefix "display"

    add "#000":
        at transform:
            on show:
                alpha 0.0 
                easein 0.3 alpha 0.5
            on hide:
                easein 0.3 alpha 0.0
    
    dismiss action Hide("select_language")
    
    frame style "empty" padding (12, 12) ysize 500 background "#f8f8f8" modal True:
        at transform:
            align (0.5, 0.5)
            on show:
                alpha 0.0 zoom 0.7 
                easein 0.3 alpha 1.0 zoom 1.0
            on hide:
                easein 0.3 alpha 0.0 zoom 0.7
        
        vpgrid cols 2 spacing 5:
            draggable True mousewheel True

            textbutton _("English") action (Language(None), Hide("select_language")) at display_preferences

            for l in translations:
                textbutton l action (Language(l), Hide("select_language")) at display_preferences

screen display_preferences(gm):
    default translations = renpy.known_languages()

    default square_size = (gui.bar_size * 3) +  (5 * 2)

    default red = int(persistent.seen_text_color.rgb[0] * 255)
    default green = int(persistent.seen_text_color.rgb[1] * 255)
    default blue = int(persistent.seen_text_color.rgb[2] * 255)

    default cols = 2
    default rows = 3

    style_prefix "display"

    frame:
        if not gm:
            xysize (1000, 650)
            align (0.48, 0.6)

        else:
            xysize (1.0, 1.0)

        hbox spacing gui.config_display_spacing:
            if not gm:  
                yalign 0.5 
                if is_android():
                    yoffset 10
            else:
                at Transform(zoom=0.85, anchor=(0.5, 0.5))
                align (0.5, 0.54)

            vbox xsize gui.config_display_left_side_xsize:
                at display_appear(2)
                spacing 15

                vbox:
                    label _("LANGUAGE"):
                        if gm:
                            text_color "#fff"

                    null height 1

                    textbutton (preferences.language or _("English")):
                        at display_preferences

                        action (
                            If(
                                main_menu,
                                If(
                                    translations,
                                    Show("select_language", translations=translations),
                                    Dialogue(_("No translations have been found in the /tl folder."))
                                ),
                                Dialogue(_("Please return to the Main Menu in order to change language."))
                            ),
                            SelectedIf(False)
                        )

                null height 10

                vbox:
                    label _("DISPLAY TEXT"):
                        if gm:
                            text_color "#fff"

                    null height 1
                    
                    vbox spacing 5:
                        hbox ysize gui.bar_size spacing 5:
                            frame background "#EBEBEB" xsize 70 ysize 1.0:
                                text _("SPEED") style "display_text"

                            bar xsize (gui.config_display_left_side_xsize - 70 - 47 - (5 * 2)):
                                value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                            frame xsize 47 background "#EBEBEB" ysize 1.0:
                                add DynamicDisplayable(lambda st, at: (Text(str(_preferences.text_cps), style="display_text", font="mod_assets/STUFF/main_menu/Montserrat/Montserrat-Medium.ttf"), None))

                        hbox spacing 5 ysize gui.bar_size:
                            frame xsize 70 background "#EBEBEB" ysize 1.0:
                                text _("AUTO")

                            bar xsize (gui.config_display_left_side_xsize - 70 - 47 - (5 * 2)):
                                value Preference("auto-forward time")

                            frame xsize 47 background "#EBEBEB" ysize 1.0:
                                add DynamicDisplayable(lambda st, at: (Text("{:.0f}".format(_preferences.afm_time), style="display_text", font="mod_assets/STUFF/main_menu/Montserrat/Montserrat-Medium.ttf"), None))

                null height 10

                vbox:
                    fixed fit_first "height":
                        label _("SEEN TEXT-COLOR"):
                            if gm:
                                text_color "#fff"

                        button action ToggleField(persistent, "change_seen_text_color"):
                            xysize (80, 22) yalign 0.5 xalign 1.0
                            background Solid("#D9D9D9")

                            $ change = persistent.change_seen_text_color
                            add Solid("#575757", xysize=(34, 16)):
                                yalign 0.5 xalign 0.1
                                at transform:
                                    subpixel True    # it's not a bug, it's a feature :monikk:
                                    easein_quart 0.5 matrixtransform OffsetMatrix((34 if not change else 0), 0, 0) matrixcolor BrightnessMatrix(0.25 if not change else 0.0)

                    null height 1

                    hbox:
                        fixed style "empty" xysize (square_size, square_size):
                            add Solid((red, green, blue))
                            # rectangle "#000" border 1

                        vbox spacing 5:
                            for color, value, hex_code in zip(
                                ("red", "green", "blue"),
                                (red, green, blue),
                                ("#FB6565","#47CD7D","#6A79FF")
                            ):
                                hbox spacing 5 ysize 18:
                                    bar xsize (gui.config_display_left_side_xsize - square_size - 47 - 5):
                                        value LocalVariableValue(color, 255, style="slider")
                                        released SetField(persistent, "seen_text_color", Color((red, green, blue)))
                                        top_bar Solid(hex_code)
                                        hover_top_bar At(Solid(hex_code), _bar_hover)
                                        bottom_bar "#ffffffff"
                                        hover_bottom_bar "#ffffffff"

                                    frame style "empty":
                                        background "#EBEBEB" xsize 47 ysize gui.bar_size
                                        text "[value]"
            
            vbox spacing gui.config_display_right_side_spacing:
                at display_appear(4)

                vbox:
                    label _("SCREEN"):
                        if gm:
                            text_color "#fff"

                    hbox:
                        textbutton _("WINDOWED") at display_preferences:
                            action Preference("display", "window")

                        textbutton _("FULLSCREEN") at display_preferences:
                            action Preference("display", "fullscreen")

                vbox:
                    label _("SKIP"):
                        if gm:
                            text_color "#fff"

                    hbox:
                        textbutton _("UNSEEN TEXT") at display_preferences:
                            action Preference("skip", "toggle")

                        textbutton _("AFTER CHOICES") at display_preferences:
                            action Preference("after choices", "toggle")

                vbox:
                    label _("BLUR"):
                        if gm:
                            text_color "#fff"

                    hbox:
                        spacing 2

                        textbutton _("DEFAULT") at display_preferences:
                            action SetField(persistent, "gaussian_blur", False)

                        textbutton _("GAUSSIAN") at display_preferences:
                            action SetField(persistent, "gaussian_blur", True)

                vbox:
                    label _("CHARACTER BLINK"):
                        if gm:
                            text_color "#fff"

                    hbox spacing 2:
                        textbutton _("ENABLED") at display_preferences:
                            action SetField(persistent, "character_blink", True)

                        textbutton _("DISABLED") at display_preferences:
                            action SetField(persistent, "character_blink", False)

                if not is_android():
                    vbox:
                        label _("DISCORD PRESENCE"):
                            if gm:
                                text_color "#fff"

                        hbox:
                            textbutton _("ENABLED") at display_preferences:
                                action discord_rpc.presence.TurnOn()

                            textbutton _("DISABLED") at display_preferences:
                                action discord_rpc.presence.TurnOff()
                vbox:
                    label _("HIDE MOUSE"):
                        if gm:
                            text_color "#fff"

                    hbox:
                        for x in (10, 20, 30):
                            textbutton _("[x] SEC") at display_preferences:
                                xsize absolute(gui.config_display_buttons_size[0] * 0.49)
                                ysize absolute(gui.config_display_buttons_size[1] * 0.94)

                                action [SetField(persistent, "mouse_hide_time", x), SetField(config, "mouse_hide_time", x)]

                        textbutton _("Never") at display_preferences:
                            xsize absolute(gui.config_display_buttons_size[0] * 0.49)
                            ysize absolute(gui.config_display_buttons_size[1] * 0.94)

                            action [SetField(persistent, "mouse_hide_time", None), SetField(config, "mouse_hide_time", None)]

screen display_configuration():
    use display_preferences(False)

transform display_preferences:
    on idle:
        matrixcolor BrightnessMatrix(0.0)
    on hover:
        matrixcolor BrightnessMatrix(-0.15)

style display_button is pref_button:
    xysize gui.config_display_buttons_size
style display_button_text is pref_button_text

style display_vbox is empty
style display_hbox is empty:
    spacing 2

style display_grid is empty:
    spacing 2

style display_text is pref_text:
    size 14 color "#000"

style display_label is pref_label
style display_label_text is pref_label_text