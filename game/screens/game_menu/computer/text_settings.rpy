default persistent.change_seen_text_color = False
default persistent.seen_text_color = Color((212, 234, 85))

screen text_settings():
    tag menu

    default translations = renpy.known_languages()

    default red = int(persistent.seen_text_color.rgb[0] * 255)
    default green = int(persistent.seen_text_color.rgb[1] * 255)
    default blue = int(persistent.seen_text_color.rgb[2] * 255)

    use game_menu(SettingsMenuInfo, menu_style="computer"):
        style_prefix "text"
        
        vbox:
            style "text_vbox_main"
            xalign 0.0

            vbox:
                hbox style "s_label_hbox":
                    s_label _("Text Speed")
                    add DynamicDisplayable(lambda st, at: (Text(str(_preferences.text_cps), style="s_label_text"), None))
               
                bar:
                    value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)
                    tooltip _("Set the text cps\n(See the upper-right window)")


            vbox:
                hbox style "s_label_hbox":
                    s_label _("Auto-Forward Time")
                    add DynamicDisplayable(lambda st, at: (Text("{:.2f}".format(_preferences.afm_time), style="s_label_text"), None))
               
                bar:
                    value Preference("auto-forward time")
                    tooltip _("Set the delay between lines\nin Auto-Forward Mode")
        
            vbox:
                s_label _("Skip")

                hbox:
                    textbutton _("Unseen Text"):
                        action Preference("skip", "toggle")
                        tooltip _("Allow skipping unseen text")

                    textbutton _("After Choices"):
                        action Preference("after choices", "toggle")
                        tooltip _("Skipping won't be disabled upon exiting a choice")
        
            vbox:
                s_label _("AFM on Menu")

                hbox:
                    textbutton _("Enable"):
                        action SetField(persistent, "disable_afm_on_game_menu", False)
                        tooltip _("Entering a menu won't disable AFM")
                
                    textbutton _("Disable"):
                        action SetField(persistent, "disable_afm_on_game_menu", True)
                        tooltip _("Entering a menu will disable AFM")
        
            vbox:
                first_spacing 0
                spacing 2
                s_label _("Change Seen Text Color")

                hbox:
                    textbutton _("On"):
                        action SetField(persistent, "change_seen_text_color", True)
                        tooltip _("Change the text color when a line of dialogue has already been read")
                
                    textbutton _("Off"):
                        action SetField(persistent, "change_seen_text_color", False)
                        tooltip _("Keep the same color whether a line has been read or not")

            hbox:
                spacing 10

                vbox:
                    style_prefix "color_picker"
                    for color, value in zip(
                        (_("red"), _("green"), _("blue")),
                        (red, green, blue)
                    ):
                        hbox:
                            bar:
                                value ScreenVariableValue(color, 255, style="color_picker_slider")
                                tooltip __("Set the value of the {color} channel").format(color=__(color))
                                released SetField(persistent, "seen_text_color", Color((red, green, blue)))
                        
                            text "[value]":
                                yoffset -7
                
                text _("This line has been read"):
                    style "say_dialogue"
                    yalign 0.3
                    if persistent.change_seen_text_color:
                        color Color((red, green, blue))

        vbox:
            style "text_settings_below_sample_textbox"
            xalign 1.0

            use sample_textbox()

            vbox:
                hbox style "s_label_hbox":
                    s_label _("Language")
                    text __("(Current: {language})").format(language=_preferences.language or "English"):
                        style "s_label_text"
                
                style_prefix "translation"

                viewport:
                    draggable True
                    mousewheel True

                    if not translations:
                        fixed:
                            text _("No other language was found.\nI guess you'll have to play in English :)")
                    
                    else:
                        vbox:
                            textbutton "English":
                                action Language(None)
                                tooltip _("Revert the language\nback to English")

                            for t in translations:
                                textbutton t:
                                    action Language(t)
                                    tooltip __("Change the language to {language}").format(language=t)
    
style text_vbox_main:
    spacing 20
    xsize 500

style text_settings_below_sample_textbox is below_sample_textbox:
    first_spacing 20
    spacing 10

style text_slider is computer_slider

style text_hbox:
    spacing 2

style text_button is computer_button
style text_button_text is computer_button_text


style color_picker_vbox:
    spacing 10
    xsize 250

style color_picker_hbox:
    spacing 2

style color_picker_slider is computer_slider:
    xsize 0.8

style color_picker_text is default


style translation_viewport:
    align (0.5, 0.0)
    xfill True
    yfill True

style translation_text is say_dialogue

style translation_vbox:
    align (0.5, 0.0)
    xfill True
    spacing 10

style translation_button:
    xalign 0.5

style translation_button_text is translation_text