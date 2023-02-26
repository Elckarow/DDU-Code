default -5 persistent.mouse_hide_time = 30
default -1 persistent.character_blink = True

screen display():
    tag menu 

    use game_menu(SettingsMenuInfo, menu_style="computer"):
        style_prefix "display"
        
        fixed:
            xfit True
            xalign 0.0

            vbox:
                vbox:
                    spacing 0
                    s_label _("Display")
                    hbox:
                        textbutton _("Window"):
                            action Preference("display", "window")
                            tooltip _("Display the game\nin windowed mode")

                        textbutton _("Fullscreen"):
                            action Preference("display", "fullscreen")
                            tooltip _("Display the game\nin fullscreen mode")

                vbox:
                    spacing 0
                    s_label _("Transitions")
                    hbox:
                        textbutton _("On"):
                            action Preference("transitions", "all")
                            tooltip _("Allow transitions to happen")

                        textbutton _("Off"):
                            action Preference("transitions", "none")
                            tooltip _("Don't allow transitions to happen")

                vbox:
                    spacing 0
                    s_label _("Screenshot")

                    hbox:
                        spacing 2

                        textbutton _("Save"):
                            action SetField(persistent, "save_screenshots", True)
                            tooltip _("Screenshots taken will be saved\n(can cause performance issues)")

                        textbutton _("Don't save"):
                            action SetField(persistent, "save_screenshots", False)
                            tooltip _("Screenshots taken won't be saved")
                
                vbox:
                    spacing 0
                    s_label _("Character Blink")

                    hbox:
                        spacing 2

                        textbutton _("Enable"):
                            action SetField(persistent, "character_blink", True)
                            tooltip _("Characters sprites will blink")

                        textbutton _("Disable"):
                            action SetField(persistent, "character_blink", False)
                            tooltip _("Characters sprites won't blink")

                vbox:
                    spacing 0
                    s_label _("Hide Mouse")

                    grid 3 2:
                        for x in (10, 20, 30):
                            textbutton _("[x]sec"):
                                action [SetField(persistent, "mouse_hide_time", x), SetField(config, "mouse_hide_time", x)]
                                tooltip __("Hide the mouse after {x} seconds of inactivity").format(x=x)

                        textbutton _("Never"):
                            action [SetField(persistent, "mouse_hide_time", None), SetField(config, "mouse_hide_time", None)]
                            tooltip _("Never hide the mouse")

                        null
                        null
                
                if not renpy.android:
                    vbox:
                        spacing 0
                        s_label _("Discord Presence")
                        hbox:
                            textbutton _("Enable"):
                                action dp.TurnOn()
                                tooltip _("Turn on Discord Rich Presence")

                            textbutton _("Disable"):
                                action dp.TurnOff()
                                tooltip _("Turn off Discord Rich Presence")

        vbox:
            style "display_settings_below_sample_textbox"
            xalign 1.0

            use sample_textbox()

            vbox:
                spacing 0

                hbox style "s_label_hbox":
                    s_label _("UI Opacity")
                    add DynamicDisplayable(lambda st, at: (Text("{}%".format(round(persistent.ui_alpha * 100, 1)), style="s_label_text"), None))

                bar:
                    value FieldValue(persistent, "ui_alpha", 0.5, offset=0.3, style="slider")
                    tooltip _("Transparency of various UI elements")

            imagebutton:
                align (0.5, 1.0)
                idle Transform("bg club_day", fit="contain")
                action Show("show_display", game_menu_transition)
                tooltip _("See for yourself")

style display_button is computer_button
style display_button_text is computer_button_text

style display_vbox is computer_vbox

style display_hbox:
    spacing 2

style display_grid:
    spacing 2

style display_settings_below_sample_textbox is below_sample_textbox:
    spacing 2
    yfill True

screen show_display():
    modal True

    style_prefix "show_display"

    dismiss action Hide("show_display", game_menu_transition)

    add "bg club_day"

    window:
        frame:
            add SampleText(_("Click anywhere to hide this screen. This is how the text looks."), slow_cps=True, style="say_dialogue")

style show_display_button is computer_button
style show_display_button_text is computer_button_text

style show_display_frame is say_frame
