python early:
    import singleton
    me = singleton.SingleInstance()

    import re
    import random
    import datetime
    import math
    import operator
    import os
    import time
    import discord_rpc
    import collections
    import pprint
    import threading
    import subprocess
    import functools
    import pygame_sdl2 as pygame

define -20 DDU_multi_persistent = MultiPersistent("DDU_multi_persistent")

init python:
    if DDU_multi_persistent.demo1 is None:
        DDU_multi_persistent.demo1 = True
        DDU_multi_persistent.save()

    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    renpy.music.register_channel("ambient", mixer="ambient", loop=True)

    def get_pos(channel="music"):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
        
    def pause(time=None):
        if time is None:
            ui.saybehavior(afm=" ")
            ui.interact(mouse='pause', type="pause", roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)
    
    def set_pov(new):
        store.current_pov = new
    
    color_map = {
        "mc": "#714045",
        "sayori": "#22Abf8",
        "natsuki": "#fbb",
        "monika": "#0a0",
        "yuri": "#a327d6"
    }
    
    def pov_color():
        return store.color_map[store.current_pov]
    
    def format_music_string(music, pos=0):
        """
        Given a filename `music` and a position `pos`, returns a string that will make the music start from `pos`,
        replacing the previous `from XXX` should it be found in `music`.

        3 possible cases:
        ```
        format_music_string("music/song_1.ogg", 3.0)
        >>> "<from 3.0>music/song_1.ogg"

        format_music_string("<loop 4.0 to 26.55>music/song_1.ogg", 3.0)
        >>> "<from 3.0 loop 4.0 to 26.55>music/song_1.ogg"

        format_music_string("<loop 80 from 69>music/song_1.ogg", 3.0)
        >>> "<loop 80 from 3.0>music/song_1.ogg"
        ```
        """
        if re.match(r"^<.*?>", music): # if the string looks like "<...>music/song_1.ogg"
            PATTERN = re.compile(r"from( *)((\d+\.\d*)|(\d+)|(\.\d+))") # "<from 0.0>..." or "<from 0.>..." or "<from 0>..." or "<from .0>..." 
            info, gt, path = music.partition(">")

            if PATTERN.search(info):
                info = PATTERN.sub("from {}".format(pos), info)
                music = info + gt + path
            else:
                music = "<from {} {}".format(pos, music[1:])
        else:
            music = "<from {}>{}".format(pos, music)

        return music
    
    def is_playing(audio, channel="music", exact=False):
        """
        Returns if the current audio playing on the channel `channel` is the same as `audio` by comparing their filenames.
        If `exact` is true, the partial playback information is also compared.

        Say the audio "<from 3 loop 5 to 4>ayaya.ogg" is playing:
        ```
        # same filename
        is_playing("ayaya.ogg")
        >>> True

        is_playing("<from 69>ayaya.ogg")
        >>> True

        # partial playback information isn't the same
        is_playing("<from 69>ayaya.ogg", exact=True)
        >>> False

        # order doesn't matter and x == float(x) if x is an integer
        is_playing("<loop 5.0 to 4.0 from 3.0>ayaya.ogg", exact=True)
        >>> True
        ```
        """
        current = renpy.music.get_playing(channel)
        if current is None: return False

        PLAYBACK_INFO_PATTERN = re.compile(r"(<(.*)>)?(.*)")

        current_match = PLAYBACK_INFO_PATTERN.match(current)
        audio_match = PLAYBACK_INFO_PATTERN.match(audio)

        if current_match is None or audio_match is None:
            return False

        if exact:       
            current_playback_info = current_match.group(2)
            audio_playback_info = audio_match.group(2)

            if current_playback_info is None and audio_playback_info is None:
                pass
            elif current_playback_info is None or audio_playback_info is None:
                return False
            else:
                # from renpy.audio.audio's Channel.split_filename method
                def get_specs(specs):
                    def expect_channel():
                        if not specs:
                            raise Exception("expected channel at end.")

                        v = spec.pop(0)

                        try:
                            return renpy.audio.audio.get_channel(v)
                        except Exception:
                            raise Exception("expected channel, got {!r}.".format(v))

                    def expect_float():
                        if not specs:
                            raise Exception("expected float at end.")

                        v = specs.pop(0)

                        try:
                            return float(v)
                        except Exception:
                            raise Exception("expected float, got {!r}.".format(v)) 

                    rv = {}

                    while specs:
                        spec = specs.pop(0)

                        if spec == "sync":
                            f = expect_channel
                        else:
                            f = expect_float
                    
                        rv[spec] = f()
            
                    return rv

                if get_specs(current_playback_info.split()) != get_specs(audio_playback_info.split()):
                    return False
            
        return current_match.group(3) == audio_match.group(3)
    
    def apply_transform_on_all_but_one_tag(tag, at_list, layer="master"):
        tags = renpy.get_showing_tags(layer)
        if tag not in tags: return
        tags.remove(tag)

        for _tag in tags:
            renpy.show(_tag, at_list=at_list, layer=layer)
    
    def focus_tag(tag, f_brightness, f_blur, t, warper=_warper.linear, layer="master"):
        at_list=[
            focus(
                i_brightness=0.0, f_brightness=f_brightness,
                i_blur=0.0, f_blur=f_blur, t=t, warper=warper
            )
        ]
        apply_transform_on_all_but_one_tag(tag, at_list=at_list, layer=layer)
    
    def unfocus_tag(tag, i_brightness, i_blur, t, warper=_warper.linear, layer="master"):
        at_list=[
            focus(
                i_brightness=i_brightness, f_brightness=0.0,
                i_blur=i_blur, f_blur=0.0, t=t, warper=warper
            )
        ]
        apply_transform_on_all_but_one_tag(tag, at_list=at_list, layer=layer)  

    def iterPage(iterable, page, step):
        """
        Yields values (at best `step` values) of an iterable where the index `i` of a value is
        `(page * step) <= i < ((page + 1) * step)`.

        The iterable has to be ordered for this function to make sense.

        It's essentially `iterable[(page * step):((page + 1) * step)]` but not every object has support for slices.
        """
        for i, e in enumerate(iterable):
            if (page * step) <= i < ((page + 1) * step):
                yield e
    
    def delete_all_data():
        """
        Clears the persistent data, deletes all saves, and restarts the game.
        """
        for savegame in renpy.list_saved_games(fast=True): renpy.unlink_save(savegame)
        persistent._clear(progress=True)
        for action in (
            Preference("all mute", "disable"), Preference("text speed", store.DEFAULT_TEXT_CPS),
            Preference("main volume", 0.8), Preference("music volume", store.DEFAULT_MUSIC_VOLUME), Preference("sound volume", store.DEFAULT_SFX_VOLUME),
            Preference("voice volume", store.DEFAULT_VOICE_VOLUME), Preference("mixer ambient volume", store.DEFAULT_AMBIENT_VOLUME), Preference("auto-forward time", store.DEFAULT_AFM_TIME),
            Preference("skip", "seen"), Preference("transitions", "all")
        ): renpy.run(action)
        custom_keymap.reset()
        renpy.utter_restart()
    
    def hyperlink_functions_style(name):
        """
        Hyperlink functions but the style `name` is used.

        `name`: str
            The style to use.
        """
        style_object = getattr(style, name)
        return (lambda target: style_object,) + style.default.hyperlink_functions[1:]
    
    def split(*args, mode=None):
        """
        Returns a new displayable composed of the displayables in `args`, by cropping and placing them
        from left to right (mode="vertically") or from top to bottom (mode="horizontally").
        """
        if mode is None:
            raise ValueError("keyword argument 'mode' not found")
        if mode not in ["horizontally", "vertically"]:
            raise ValueError(f"unknown mode: {mode}")
        
        images = [ ]

        num = len(args)
        
        xspacing = config.screen_width / num
        yspacing = config.screen_height / num

        for i, img in enumerate(args):
            if mode == "vertically":
                crop_args = [
                    absolute(xspacing * i),
                    0,
                    absolute(xspacing * (i + 1)),
                    config.screen_height
                ]
                pos_tuple = (absolute(xspacing * i), 0)

            else:
                crop_args = [
                    0,
                    absolute(yspacing * i),
                    config.screen_width,
                    absolute(yspacing * (i + 1))
                ]
                pos_tuple = (0, absolute(yspacing * i))

            images.append(pos_tuple)
            images.append(Transform(img, crop=crop_args, subpixel=True))
        
        return Flatten(Composite((config.screen_width, config.screen_height), *images))

default current_pov = "mc"        

define audio.ohayou = "<loop 4.499>bgm/2.ogg"
define audio.dolal = "<loop 19.451>bgm/4.ogg"
define audio.okev = "<loop 4.444>bgm/5.ogg"
define audio.okev_s = "<loop 4.444>bgm/5_sayori.ogg"
define audio.okev_n = "<loop 4.444>bgm/5_natsuki.ogg"
define audio.okev_y = "<loop 4.444>bgm/5_yuri.ogg"
define audio.okev_m = "<loop 4.444>bgm/5_monika.ogg"
define audio.playwme = "<loop 10.893>bgm/6.ogg"
define audio.poempanic = "<loop 2.291>bgm/7.ogg"
define audio.daijoubu = "<loop 9.938>bgm/8.ogg"
define audio.myfeelings = "<loop 3.172>bgm/9.ogg"
define audio.myconfession = "<loop 5.861>bgm/10.ogg"
define audio.jm = "<loop 0>bgm/m1.ogg"

define audio.title = "<loop 0>mod_assets/BGM/Undercurrents.mp3"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.fall2 = "sfx/fall2.ogg"
define audio.schoolbell = "mod_assets/SFX/bell.ogg"
define audio.glitch = "sfx/s_kill_glitch1.ogg"

define audio.rain_int = "<loop 2.102>mod_assets/Ambiance/rain_int.ogg"


image black = Solid("#000")
image white = Solid("#fff")
image bg notebook = "bg/notebook.png"

image blink:
    "black"
    alpha 0.0
    easein 0.1 alpha 1.0
    easeout 0.1 alpha 0.0

image blink_w:
    "white"
    alpha 0.0
    easein 0.1 alpha 1.0
    easeout 0.1 alpha 0.0

image bg residential_day = "bg/residential.png"
image bg residential_gray = At("bg/residential.png", variant(0.39, -0.15, "#cbcbcb"))
image bg residential_afternoon = At("bg/residential.png", afternoon)
image bg residential_night = At("bg/residential.png", night)

image bg class_day = "bg/class.png"
image bg class_gray = At("bg/class.png", variant(0.4, -0.15, "#cfcfcf"))
image bg class_afternoon = At("bg/class.png", afternoon)
image bg class_night = At("bg/class.png", night)

image bg school_day = "mod_assets/BG/school_day.jpg"
image bg school_afternoon = "mod_assets/BG/school_afternoon.jpg"

image bg school_corridor_day = "bg/corridor.png"
image bg school_corridor_gray = At("bg/corridor.png", variant(0.37, -0.14, "#cfcfcf"))
image bg school_corridor_afternoon = At("bg/corridor.png", afternoon)
image bg school_corridor_night = At("bg/corridor.png", night)

image bg school_lockers_day = "mod_assets/BG/school_lockers.png"
image bg school_lockers_afternoon= At("mod_assets/BG/school_lockers.png", afternoon)
image bg school_lockers_night = At("mod_assets/BG/school_lockers.png", night)

image bg school_library_day = "mod_assets/BG/school_library_day.jpg"
image bg school_library_afternoon = "mod_assets/BG/school_library_afternoon.jpg"

image bg school_stairs_day = "mod_assets/BG/school_stairs_day.jpg"
image bg school_stairs_gray = At("mod_assets/BG/school_stairs_day.jpg", variant(0.8, -0.1, "#dbdbdb"))

image bg club_day = "bg/club.png"
image bg club_gray = At("bg/club.png", variant(0.38, -0.19, "#cfcfcf"))
image bg club_afternoon = At("bg/club.png", afternoon)
image bg club_night = At("bg/club.png", night)

image bg club_closet_day = "bg/closet.png"
image bg club_closet_afternoon = At("bg/closet.png", afternoon)
image bg club_closet_night = At("bg/closet.png", night)

image bg mc_bedroom_day_open = At("mod_assets/BG/mc_bedroom_open.png", variant(color="#daf8fd", light=-0.01))
image bg mc_bedroom_day_closed = At("mod_assets/BG/mc_bedroom_closed.png", variant(color="#daf8ea", light=-0.03))
image bg mc_bedroom_afternoon_open = "mod_assets/BG/mc_bedroom_afternoon_open.png"
image bg mc_bedroom_rain_open = "mod_assets/BG/mc_bedroom_rain_open.png"

image bg mc_living_room = "mod_assets/BG/mc_living_room.png"

image bg mc_kitchen_day = "bg/kitchen.png"
image bg mc_kitchen_afternoon = At("bg/kitchen.png", afternoon)
image bg mc_kitchen_night = At("bg/kitchen.png", night)

image bg s_bedroom_day = "bg/sayori_bedroom.png"
image bg s_bedroom_afternoon = At("bg/sayori_bedroom.png", afternoon)
image bg s_bedroom_night = At("bg/sayori_bedroom.png", night)

image bg s_house_day = "bg/house.png"
image bg s_house_afternoon = At("bg/house.png", afternoon)
image bg s_house_night = At("bg/house.png", night)

image bg street_day = "mod_assets/BG/street_day.jpg"
image bg street_afternoon = "mod_assets/BG/street_afternoon.jpg"


define narrator = Character(ctc="ctc", ctc_position="fixed")

define _base_char = Character(None, what_prefix='"', what_suffix='"', kind=narrator)

define who = Character("???", kind=_base_char)
define amogus = Character(kind=who, voice_tag="amogus")

define mc = Character(_("Melody"), kind=_base_char, voice_tag="mc")
define s = DynamicCharacter("s_name", image="sayori", kind=_base_char, voice_tag="s")
define m = DynamicCharacter("m_name", image="monika", kind=_base_char, voice_tag="m")
define n = DynamicCharacter("n_name", image="natsuki", kind=_base_char, voice_tag="n")
define y = DynamicCharacter("y_name", image="yuri", kind=_base_char, voice_tag="y")
define a = DynamicCharacter("aika_name", image="aika", kind=_base_char, voice_tag="a")
define am = DynamicCharacter("amelia_name", image="amelia", kind=_base_char, voice_tag="am")
define k = DynamicCharacter("kaito_name", image="kaito", kind=_base_char, voice_tag="k")

# Autofocus function
# it just calls renpy.character.Character
define cg_mc = BaseCharacter(image="cg", kind=mc)
define cg_s = BaseCharacter(image="cg", kind=s)
define cg_m = BaseCharacter(image="cg", kind=m)
define cg_n = BaseCharacter(image="cg", kind=n)
define cg_y = BaseCharacter(image="cg", kind=y)
define cg_am = BaseCharacter(image="cg", kind=am)

default s_name = _("Sayori")
default m_name = _("Monika")
default n_name = _("Natsuki")
default y_name = _("Yuri")
default aika_name = _("???")
default amelia_name = _("Amelia")
default kaito_name = _("Kaito")

define _dismiss_pause = config.developer
default allow_skipping = True
default basedir = config.basedir
default currentpos = 0

default week = 1
default day = _("Monday")



# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
