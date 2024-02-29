init python:
    class AudioSettingsMixer(object):
        def __init__(self, mixer, title, sample=None):
            self.mixer = mixer
            self.title = title
            self.sample = sample

        def VolumeText(self, st, at):
            txt = ": {:.0f}%".format(preferences.get_mixer(self.mixer) * 100) if not preferences.get_mute(self.mixer) else _(": Muted")
            return Text(txt, style="dj_text", font="mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf", size=20), None

    audio_settings_mixers = (
        AudioSettingsMixer("main", _("Main")),
        AudioSettingsMixer("music", _("Music")),
        AudioSettingsMixer("sfx", _("Sound")),
        AudioSettingsMixer("ambient", _("Ambiance"))
    )

    class VoiceAudioSettings(object):
        def __init__(self, voice_tag, name, image_as_str, character_settings, sample=None):
            self.voice_tag = voice_tag
            self._name = name
            self._image_as_str = image_as_str
            self.sample = sample

            self.character_settings = character_settings

            persistent._character_volume.setdefault(voice_tag, 1.0)

        def VolumeText(self, st, at):
            txt = ": {:.0f}%".format(GetCharacterVolume(self.voice_tag) * 100) if self.voice_tag not in persistent._voice_mute else _(": Muted")
            return Text(txt, style="dj_text", font="mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf", size=20), None
    
        @property
        def name(self):
            return self.character_settings.get_string(self._name)
        
        @property
        def image(self):
            return self.character_settings.get_image(CharacterPortrait(self._image_as_str.split()))

    voice_actors = [
        VoiceAudioSettings("a", "Aika", "aika smug noblink", aika_character_settings),
        VoiceAudioSettings("am", "Amelia", "amelia turned noblink", amelia_character_settings),
        VoiceAudioSettings("s", "Sayori", "sayori turned mb noblink", sayori_character_settings),
        VoiceAudioSettings("y", "Yuri", "yuri shy mc noblink", yuri_character_settings),
        VoiceAudioSettings("m", "Monika", "monika turned noblink", monika_character_settings),
        VoiceAudioSettings("mc", "Melody", "melody turned ec thinking mh noblink", melody_character_settings),
        VoiceAudioSettings("bo", "Boss", "boss turned noblink", boss_character_settings),
        VoiceAudioSettings("n", "Natsuki", "natsuki turned noblink", natsuki_character_settings),
        VoiceAudioSettings("ka", "Kaito", "kaito turned lup bg noblink", kaito_character_settings),
    ]
    voice_actors.sort(key=lambda va: va._name)

screen voice_actors_preferences(gm):
    style_prefix "audio"

    hbox:
        if not gm:
            xalign 1.0 ysize 500 yalign 0.8 xoffset -50
        else:
            xalign 0.5 yalign 0.95 ysize 540

        frame style "empty" padding (3, 3) xoffset 30 xsize 550:
            if gm:
                xalign 0.5 yalign 1.0

            viewport id "va_vp":
                mousewheel True
                draggable True

                vbox style "empty" spacing 5 xalign 0.0:
                    for i, vo in enumerate(voice_actors):
                        frame:
                            at transform:
                                RoundedCorners(25)
                                subpixel True
                                alpha 0.0 yoffset -15
                                (i / 20) + 0.2
                                easein_quart 0.4 alpha 1.0 yoffset 0

                            background ("#ffffff95" if gm else "#00000010")
                            xysize (500, 100)

                            button style "empty":
                                at transform:
                                    on idle:
                                        matrixcolor BrightnessMatrix(0.0)
                                    on hover:
                                        matrixcolor BrightnessMatrix(-0.05)
                                
                                xysize (100, 1.0)
                                hover_foreground Transform("mod_assets/STUFF/main_menu/triangle.png", align=(0.5, 0.5), xysize=(30, 30), matrixtransform=Matrix.rotate(0, 0, 90), matrixcolor=BrightnessMatrix(1.0))

                                add "#00000050"
                                add vo.image:
                                    at transform:
                                        fit "contain"

                                action If(vo.sample is not None, PlayCharacterVoice(vo.voice_tag, vo.sample))

                            vbox yalign 0.5 xoffset 120:
                                hbox:
                                    text vo.name style "dj_text" font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf" size 20
                                    add DynamicDisplayable(vo.VolumeText)

                                button:
                                    hover_background Solid("#00000030")
                                    background Solid("#00000015")
                                    xysize (120, 20)
                                    action ToggleVoiceMute(vo.voice_tag)
                                    text _("MUTE"):
                                        color "#000"
                                        xalign 0.5
                                        style "branch_title"

                            bar align (0.925, 0.5) xsize 186:
                                if is_android():
                                    at Transform(yzoom=1.5, xzoom=1.09)

                                if vo.voice_tag in persistent._voice_mute:
                                    at transform:
                                        alpha (0.5 if not gm else 0.8)
                                else:
                                    at transform:
                                        alpha 1.0

                                value DictValue(persistent._character_volume, key=vo.voice_tag, range=1.0, style="audio_slider")

            vbar value YScrollValue("va_vp"):
                at transform:
                    xpos 1.0 xanchor 0.0 alpha 0.0 subpixel True
                    ease_quad 0.4 xanchor 1.0 alpha 1.0

screen audio_preferences(gm):
    style_prefix "audio"
        
    frame xysize (550, 300):
        align ((0.5, 0.5) if gm else (0.15, 0.47))

        vbox style "empty" spacing (8 if gm else 15):
            for i, a in enumerate(audio_settings_mixers):
                frame:
                    at transform:
                        RoundedCorners(20)
                        subpixel True alpha 0.0 xoffset -15
                        0.05
                        i / 20
                        easein_quart 0.4 alpha 1.0 xoffset 0

                    xysize (550, 90)
                    background ("#ffffff95" if gm else "#00000010")

                    vbox style "empty" anchor (0.0, 0.5) pos (0.1, 0.5):
                        hbox style "empty":
                            text a.title style "dj_text" font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf" size 20
                            add DynamicDisplayable(a.VolumeText)
                        
                        button:
                            hover_background Solid("#00000030")
                            background Solid("#00000015")
                            xysize (120, 20)
                            action (Preference("all mute", "toggle") if a.mixer == "main" else ToggleMute(a.mixer))
                            text _("MUTE"):
                                color "#000"
                                xalign 0.5
                                style "branch_title"

                    vbox style "empty" at Flatten:
                        add "#000" xysize (160, 2)
                        add "#000" xysize (100, 1)

                    bar align (0.8, 0.5) xsize 186:
                        if is_android():
                            at Transform(yzoom=1.5, xzoom=1.3, xoffset=5)

                        if preferences.get_mute(a.mixer):
                            at transform:
                                alpha (0.5 if not gm else 0.8)
                        else:
                            at transform:
                                alpha 1.0

                        value Preference(a.mixer + " volume")

                        if a.sample is not None:
                            released Play(a.mixer, a.sample)

screen audio_configuration():
    use voice_actors_preferences(False)
    use audio_preferences(False)


style audio_label is display_text:
    align (0.5, 0.5)
    size 15
style volume_label is pref_text:
    size 13
    align (0.5, 0.48) color "#000"
    
style dj_text:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf"
    size 28
    #align (0.5,0.55)

    text_align 0.0
    outlines []
    color "#000"
style mixer_label:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Light.ttf"
    size 15
    outlines []
    color "#000"
    text_align 1.0
    align (0.95,0.95)

style audio_main_vbox:
    spacing 9
    xsize 500

style audio_vbox:
    first_spacing 0
    spacing 4

style audio_slider is pref_slider:
    ysize int(gui.bar_size * 0.5)
    
style audio_text is pref_text
style audio_button is pref_button
style audio_button_text is pref_button_text

style audio_mute_button:
    background Solid("#E8E8E8")
    selected_background Solid("#868686")
    xysize (27, 27)
    yalign 0.5

style audio_mute is display_text:
    color "#150087"
    layout "nobreak"
    yalign 0.5
