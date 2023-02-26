init python:
    class AudioSettingsMixer(object):
        def __init__(self, mixer, title, description, sample=None):
            self.mixer = mixer
            self.title = title
            self.description = description
            self.sample = sample
        
        def VolumeText(self, st, at):
            txt = "{:.2f}%".format(preferences.get_volume(self.mixer) * 100) if not preferences.get_mute(self.mixer) else _("Muted")
            return Text(txt, style="s_label_text", xalign=1.0), None

    audio_settings_mixers = (
        AudioSettingsMixer("main", _("Main Volume"), _("General volume")),
        AudioSettingsMixer("music", _("Music Volume"), _("Background music volume")),
        AudioSettingsMixer("sfx", _("Sound Volume"), _("Sound effect volume")),
        AudioSettingsMixer("ambient", _("Ambiance Volume"), _("Ambiance noise volume\n(rain, waves, etc...)"))
    )

screen audio_settings():
    tag menu

    use game_menu(SettingsMenuInfo, menu_style="computer"):
        style_prefix "audio"
        
        vbox:
            style "audio_main_vbox"
            xalign 0.0

            for a in audio_settings_mixers:
                vbox:
                    hbox style "s_label_hbox":
                        s_label a.title
                        add DynamicDisplayable(a.VolumeText)

                    bar:
                        value Preference(a.mixer + " volume")
                        tooltip a.description
                        if a.sample is not None:
                            released Play(a.mixer, a.sample)

                    hbox:
                        spacing 1

                        if a.mixer == "main":
                            button:
                                style "audio_mute_button"
                                action Preference("all mute", "toggle")
                        
                            text _("mute all"):
                                style "audio_mute"
                        
                        else:
                            button:
                                style "audio_mute_button"
                                action Preference(a.mixer + " mute", "toggle")

                            text _("mute"):
                                style "audio_mute"

style audio_main_vbox:
    spacing 9
    xsize 500

style audio_vbox:
    first_spacing 0
    spacing 4

style audio_slider is computer_slider
style audio_text is computer_text

style audio_button is computer_button
style audio_button_text is computer_button_text

style audio_mute_button:
    background RoundedFrame(Solid("#6ca7ff"), radius=10)
    selected_background RoundedFrame(Solid("#0045e0"), radius=10)
    xysize (27, 27)
    yalign 0.5

style audio_mute is audio_text:
    color "#150087"
    yalign 0.5