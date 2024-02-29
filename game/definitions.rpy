python early:
    import singleton
    me = singleton.SingleInstance()

    import re
    import random
    import datetime
    import math
    import os
    import io
    import time
    import collections
    import pprint
    import pygame_sdl2 as pygame
    import sys
    import subprocess
    import threading
    import traceback
    import array

define -500 DDU_multi_persistent = MultiPersistent("DDU_multi_persistent")

init -5 python:
    angle_from_tl_to_br = \
        math.degrees(
            math.asin(
                config.screen_height / math.hypot(config.screen_width, config.screen_height)
            )
        )

init -400 python:
    if DDU_multi_persistent.demo2 is None:
        DDU_multi_persistent.demo2 = True
        DDU_multi_persistent.save()

    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    renpy.music.register_channel("music2", mixer="music", loop=True)
    renpy.music.register_channel("ambient", mixer="ambient", loop=True)
    renpy.music.register_channel("ambient2", mixer="ambient", loop=True)
    renpy.music.register_channel("sound_loop", mixer="sfx", loop=True)
    renpy.music.register_channel("sound2", mixer="sfx", loop=False)

    def get_mixer(mixer):
        return preferences.get_mixer(mixer)

    def write_traceback(txt):
        try:
            # yes renpy.renpy is a thing
            renpy.renpy.error.report_exception(txt, editor=False)
        except Exception:
            pass

    @renpy.pure
    def is_renpy_version_or_above(major, minor, patch):
        """
        Checks if the current version of renpy is at least `(major, minor, patch)`.
        If renpy is on a py3 / r8 version, `(major + 1, minor - 5, patch)` is checked.

        I.e., if the game runs on renpy 8 and that this function is called to check for `7.5.0`, `8.0.0` (the py3 / r8 equivalent of `7.5.0`) is checked for.
        """
        current_version = renpy.version_tuple[:3]

        if not renpy.compat.PY2:
            r8version = (major + 1, minor - 5, patch)
            return current_version >= r8version

        return current_version >= (major, minor, patch)

    @renpy.pure
    def position(n, base, limit=False):
        if isinstance(n, (int, absolute)):
            return n
        else:
            if limit is None: pass
            elif limit is False: limit = base
            return min(absolute(n * base), limit)

    def get_pos(channel="music"):
        return renpy.music.get_pos(channel=channel) or 0.0
        
    def pause(time=None):
        if time is None:
            ui.saybehavior(afm=" ")
            ui.interact(mouse='pause', type="pause", roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)
    
    def set_pov(new):
        store.pov_key = new
        store.phone_available = new in ("mc", "m")
    
    def add_playback_info(audio, value, what="from"):
        """
        Adds the playback information `what` to the audio string `audio`, giving it the value `value`.
        """
        if what not in ("from", "to", "loop"): # don't bother with `sync`
            raise Exception("unknown partial playback info '%s'" % what)

        if re.match(r"^<.*?>", audio):
            PATTERN = re.compile(r"{}( *)((\d+\.\d*)|(\d+)|(\.\d+))".format(what))
            info, gt, path = audio.partition(">")

            if PATTERN.search(info):
                info = PATTERN.sub("{} {}".format(what, value), info)
                audio = info + gt + path
            else:
                audio = "<{} {} {}".format(what, value, audio[1:])
        else:
            audio = "<{} {}>{}".format(what, value, audio)

        return audio
    
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

                    rv = { }

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
        # custom_keymap.reset()
        renpy.utter_restart()
    
    def hyperlink_functions_style(name):
        """
        Hyperlink functions but the style `name` is used.

        `name`: str
            The style to use.
        """
        style_object = getattr(style, name)
        return (lambda target: style_object,) + style.default.hyperlink_functions[1:]
    
    def split(*args, vertically=True):
        """
        Returns a new displayable composed of the displayables in `args`, by cropping and placing them
        from left to right (vertically=False) or from top to bottom (vertically=True).
        """
        
        images = [ ]

        num = len(args)
        
        xspacing = config.screen_width / num
        yspacing = config.screen_height / num

        for i, img in enumerate(args):
            if vertically:
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

    def CharacterSilhouette(d):
        return Transform(d, matrixcolor=TintMatrix("#000"), blur=3, blur_gaussian=True)

    class Callbacks(object):
        def __init__(self, *callbacks):
            self.callbacks = callbacks
        
        def __call__(self, *args, **kwargs):
            for callback in self.callbacks:
                callback(*args, **kwargs)
    
    def mean(l):
        return sum(l) / len(l)
    
    character_crops = {
        "sayori turned": (325, 108, 330, 330),
        "sayori tap": (282, 105, 330, 330),

        "monika turned": (305, 110, 322, 322),

        "natsuki turned": (320, 160, 320, 320),
        "natsuki cross": (absolute(320 + _natsuki_cross_offset[0]), absolute(160 + _natsuki_cross_offset[1]), 320, 320),
        "natsuki lean": (absolute(320 + _natsuki_lean_offset[0] - 34), absolute(160 + _natsuki_lean_offset[1] + 9 + _natsuki_lean_ycrop), 320, 320),

        "yuri turned": (301, 59, 323, 323),
        "yuri shy": (306, 62, 323, 323),

        "aika turned": (334, 116, 320, 320),
        "aika smug": (306, 130, 320, 320),

        "boss turned": (480, 59, 260, 260),

        "amelia turned": (285, 120, 329, 329),

        "ellen turned": (285, 120, 329, 329),

        "kaito turned": (350, 57, 312, 312),

        "melody turned": (336, 95, 312, 312)
    }

    average_character_crop_width, average_character_crop_height = (absolute(mean([crop[i] for crop in character_crops.values()])) for i in (2, 3))

    def get_say_attributes():
        tag = renpy.get_say_image_tag()
        if tag is None: return None

        return [tag] + list(renpy.get_attributes(tag) or ())

    def GetCharacterCrop(attrs):
        if isinstance(attrs, basestring): attrs = attrs.split()
        tag, *attributes = attrs

        # only take the first one found.
        # say `attrs="natsuki turned fs"`,
        # if `"natsuki turned"` is found first,
        # it will be returned
        # even if `"natsuki turned fs"` exists
        for c, crop in character_crops.items():
            key, *rest = c.split()

            if key != tag or not all(attr in attributes for attr in rest):
                continue
            
            return crop
        
        # crop not found
        return None

    def GetSayCharacterPortrait(adjust_attrs=None):
        attrs = get_say_attributes()
        if attrs is None: return None

        return CharacterPortrait(attrs, adjust_attrs=adjust_attrs)

    def CharacterPortrait(attrs, adjust_attrs=None):
        attributes = list(attrs)

        if adjust_attrs is not None:
            attributes = adjust_attrs(attributes)

        crop = GetCharacterCrop(attributes)
        if crop is None: return None

        if attributes[0] in autofocus._autofocus_map:
            # take the non-autofocused version
            # if it doesn't exist then im dumb :monikk:
            attributes[0] = "_" + attributes[0]
            
        return Transform(" ".join(attributes), crop=crop)

    class CharacterSideImage(LayeredImageProxy):
        def _duplicate(self, args):
            rv = super(CharacterSideImage, self)._duplicate(args)  

            #                       remove "side"
            crop = GetCharacterCrop(args.name[1:] + tuple(args.args))
            if crop is not None:
                rv = Transform(rv, crop=crop)
            
            return rv

    def get_process_list():
        if renpy.windows:
            try:
                process_list = subprocess.run("wmic process get Description", shell=True, check=True, stdout=subprocess.PIPE).stdout.lower().decode("utf-8").replace("\r", "").replace(" ", "").strip().split("\n")
            except subprocess.CalledProcessError:
                try:
                    process_list = (x + ".exe" for x in subprocess.run("powershell (Get-Process).ProcessName", shell=True, check=True, stdout=subprocess.PIPE).stdout.lower().decode("utf-8").replace("\r", "").replace(" ", "").strip().split("\n"))
                except Exception: 
                    process_list = [ ]            
        else:
            try:
                process_list = subprocess.run("ps -A --format cmd", shell=True, check=True, stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n")
            except subprocess.CalledProcessError:
                process_list = subprocess.run("ps -A -o command", shell=True, check=True, stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n")

            process_list.pop(0)

        return process_list

    def _is_recording():
        return any(
                    process in (
                        "obs32.exe",
                        "obs64.exe",
                        "obs.exe",
                        "xsplit.core.exe",
                        "livehime.exe",
                        "pandatool.exe",
                        "yymixer.exe",
                        "douyutool.exe",
                        "huomaotool.exe"
                    )
                    for process in get_process_list()
                )
    
    _is_recording_cache = _is_recording()

    def is_recording(cache=False):
        global _is_recording_cache

        if not cache:
            _is_recording_cache = _is_recording()
        
        return _is_recording_cache

    def get_safe_path(path):
        # don't doxx streamers :monikk:
        if is_recording(cache=True):
            split = path.split("/")
            path = "/".join((split[0], "******", split[-1]))
        
        return path

    def get_player_name():
        if is_recording(cache=True): return __("Player")

        # stolen from Weiss' Mod Template, kinda
        for name in ("LOGNAME", "USER", "LNAME", "USERNAME"):
            user = os.environ.get(name, None)

            if user:
                return user

        # if we haven't found anything, set it to "Player"
        return  __("Player")

    def set_date(year=None, month=None, day=None, hour=None, minute=None, second=None):
        current_date = phone.system.get_date()

        if month is None:  month = current_date.month
        if day is None:    day = current_date.day
        if year is None:   year = current_date.year
        if hour is None:   hour = current_date.hour
        if minute is None: minute = current_date.minute
        if second is None: second = current_date.second

        phone.system.date = datetime.datetime(
            year=year, month=month, day=day,
            hour=hour, minute=minute, second=second
        )

    def advance_date(**kwargs):
        if phone.system.date is not None:
            phone.system.date += datetime.timedelta(**kwargs)
    
    def float_to_s_ms(x):
        seconds = int(x)
        milliseconds = (x - seconds) * 1000
        return seconds, milliseconds

    def get_auto_advance(s, mult):
        if not mult: return 0, 0

        r = len(s) / (auto_advance_date_ratio * (1.0 / mult)) 
        seconds, milliseconds = float_to_s_ms(r * 60)
        milliseconds /= 60
        return seconds, milliseconds

    def advance_date_str(s):
        s, ms = get_auto_advance(renpy.filter_text_tags(renpy.substitute(s, translate=False), allow=()), auto_advance_date_mult)
        advance_date(seconds=s, milliseconds=ms)

    # /!\ /!\ /!\ /!\ /!\ /!\ 
    # uses the translated version of the dialogue
    @config.all_character_callbacks.append
    def _auto_advance_date(event, interact=True, **kwargs):
        if event != "end": return

        last_dialogue = store._last_say_what
        if last_dialogue is None: return 

        last_dialogue = last_dialogue.split("{done}")[0]

        if _last_say_who == "extend":
            last_dialogue = last_dialogue.split(config.extend_interjection)[-1]

        advance_date_str(last_dialogue)

    @phone.config.discussion_callbacks.append
    def _auto_advance_phone(gc, event, callback_object):
        if event != "end": return

        if callback_object.type == phone.discussion.TEXT:
            c = phone.discussion.character(callback_object.source)
            seconds, milliseconds = get_auto_advance(callback_object.data, auto_advance_date_mult)
            seconds *= 2

        elif callback_object.type == phone.discussion.TYPING:
            seconds, milliseconds = float_to_s_ms(callback_object.data)
            seconds *= 5
        
        else:
            return

        advance_date(seconds=seconds, milliseconds=milliseconds)    

    @phone.config.discussion_callbacks.append
    def _auto_set_date_phone(gc, event, callback_object): 
        # only do it during a phone discussion
        # reason is
        # im too lazy to explain
        if event == "save" and phone.discussion._group_chat is not None:
            phone.group_chat.group_chat(gc).date = phone.system.get_date()  
    
    def clear_layers(layers=()):
        for layer in (renpy.easy.to_tuple(layers) or renpy.display.core.layers):
            renpy.scene(layer)
            renpy.show_layer_at(at_list=[], layer=layer, camera=True)
    
    def stop_channels(fadeout=0.0, channels=()):
        for channel in (renpy.easy.to_tuple(channels) or (c.name for c in renpy.audio.audio.all_channels)):
            renpy.music.stop(channel=channel, fadeout=fadeout)
    
    def set_internet(i):
        i = bool(i)
        phone.system.internet_connection = i
        phone.system.cellular_data = not i

    def invoke_in_thread(f, *args, **kwargs):
        """
        `renpy.invoke_in_thread` but without calling `renpy.restart_interaction`.
        """
        def run():
            try:
                f(*args, **kwargs)
            except Exception:
                traceback.print_exc()

        t = threading.Thread(target=run)
        t.daemon = True
        t.start()
    
    @renpy.pure
    def is_android():
        # return True
        return renpy.android

default auto_advance_date_mult = 1.0
define auto_advance_date_ratio = 400

define phone.config.enter_transition = Dissolve(0.3)
define phone.config.intra_transition = Dissolve(0.2)
define phone.config.exit_transition  = Dissolve(0.3)

define audio.ohayou = "<loop 4.499>bgm/2.ogg"
define audio.dolal = "<loop 19.451>bgm/4.ogg"
define audio.okev = "<loop 4.444>bgm/5.ogg"
define audio.okev_s = "<loop 4.444>bgm/5_sayori.ogg"
define audio.okev_n = "<loop 4.444>bgm/5_natsuki.ogg"
define audio.okev_y = "<loop 4.444>bgm/5_yuri.ogg"
define audio.okev_m = "<loop 4.444>bgm/5_monika.ogg"
define audio.playwme = "<loop 10.893>bgm/6.ogg"
define audio.playwme_muffled = "<loop 10.893>bgm/6o.ogg"
define audio.poempanic = "<loop 2.291>bgm/7.ogg"
define audio.daijoubu = "<loop 9.938>bgm/8.ogg"
define audio.myfeelings = "<loop 3.172>bgm/9.ogg"
define audio.myconfession = "<loop 5.861>bgm/10.ogg"
define audio.jm = "<loop 0.0>bgm/m1.ogg"

define audio.title = "<loop 0.0>mod_assets/BGM/Riptide.mp3" 
define audio.school = "<loop 13.734 to 68.591>mod_assets/BGM/Generic_School_Track_15.mp3"
define audio.friendly_endeavours = "<loop 0.0>mod_assets/BGM/Friendly_Endeavours.mp3"
define audio.a_sunshine = "<loop 0.0>mod_assets/BGM/Arpeggiated_Sunshine.ogg"
define audio.dollaort = "<loop 0.0>mod_assets/BGM/Dreams_of_Literature_Love_and_other_Romantic_Thoughts.mp3"
define audio.rgb = "<loop 0.0>mod_assets/BGM/RGB.mp3"
define audio.hnt = "<loop 0.0 to 130.0>mod_assets/BGM/Hitoribocchi_no_Taiyou.mp3"
define audio.mp3song = "<loop 0.0>mod_assets/BGM/MP3_Song.ogg"
define audio.nsc = "<loop 0.0>mod_assets/BGM/Not_so_Cute.mp3"
define audio.faith = "<loop 0.0>mod_assets/BGM/Faith.mp3"
define audio.wtdgi = "<loop 89.049>mod_assets/BGM/When_the_Dam_Gave_In.ogg"
define audio.dawn = "<loop 0.0>mod_assets/BGM/Dawn.mp3"
define audio.anewday = "<loop 0.0>mod_assets/BGM/A_New_Day.mp3"
define audio.cafe = "<loop 78.758 to 166.008>mod_assets/BGM/Cafe_au_Lait.mp3"
define audio.tswstd = "<loop 70.005 to 119.944>mod_assets/BGM/The_Sky_We_Saw_That_Day.mp3"
define audio.arcade         = "<loop 60.941 to 156.941>mod_assets/BGM/Blissful_Wind.mp3"
define audio.arcade_muffled = "<loop 60.941 to 156.941>mod_assets/BGM/Blissful_Wind_muffled.mp3"
define audio.tender_moment = "<loop 15.997 to 96.007>mod_assets/BGM/A_Tender_Moment.mp3" # loop 47.997
define audio.breeze = "<loop 0.0>mod_assets/BGM/Breeze_on_the_Hill.mp3"
define audio.pillow = "<loop 0.0>mod_assets/BGM/Pillow_Talk.mp3"
define audio.ahog = "<loop 0.0>mod_assets/BGM/A_Hint_of_Gray.mp3"
define audio.elegant_s = "<loop 0.0>mod_assets/BGM/Elegant_Slumber.mp3"
define audio.stars = "<loop 0.0>mod_assets/BGM/Stars_and_Illustrations.mp3"
define audio.violetsolo = "<loop 0.0>mod_assets/BGM/Violet_Solo.ogg"
define audio.yofukashinouta = "<loop 0.0>mod_assets/BGM/Yofukashi_no_Uta.mp3"
define audio.childlikesmile = "<loop 0.0>mod_assets/BGM/A_Childlike_Smile.mp3"
define audio.pensive = "<loop 0.0>mod_assets/BGM/Pensive.mp3"
define audio.ragtime = "<loop 1.980 to 111.635>mod_assets/BGM/Rascals_Ragtime.mp3"
define audio.dday_1 = "<loop 17.488 to 69.857>mod_assets/BGM/DDay.mp3"
define audio.dday_2 = "<from 74.225 loop 88.653 to 185.483>mod_assets/BGM/DDay.mp3"

define audio.slap = "sfx/slap.ogg"
define audio.smack = "sfx/smack.ogg"
define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.fall2 = "sfx/fall2.ogg"
define audio.school_bell = "mod_assets/SFX/school_bell.ogg"
define audio.clatter = "mod_assets/SFX/clatter.ogg"
define audio.heartbeat = "mod_assets/SFX/heartbeat.ogg"
define audio.tinnitus = "<loop 11.411 to 15.782>mod_assets/SFX/tinnitus.ogg"
define audio.slam = "mod_assets/SFX/slam.ogg"
define audio.door_knock = "mod_assets/SFX/door_knock.ogg"
define audio.beep = "mod_assets/SFX/beep.ogg"
define audio.train = "mod_assets/SFX/train.mp3"
define audio.thud = "mod_assets/SFX/thud.mp3"
define audio.static = "<loop 0.0>mod_assets/SFX/static.ogg"
define audio.frying_pan = "<loop 0.0>mod_assets/SFX/frying_pan.ogg"
define audio.wine_glass = "mod_assets/SFX/wine_glass.ogg"
define audio.doorbell = "mod_assets/SFX/doorbell.ogg"
define audio.chairmoving = "mod_assets/SFX/chair.ogg"
define audio.carmonkaw = "mod_assets/SFX/carmonkaw.ogg"
define audio.grumble = "mod_assets/SFX/grumble.mp3"
define audio.widenekoflap = "mod_assets/SFX/widenekoflap.mp3"
define audio.nerf_reload = "mod_assets/SFX/nerf_reload.mp3"
define audio.nerf_shot_1 = "mod_assets/SFX/nerf_shot_1.mp3"
define audio.nerf_shot_2 = "mod_assets/SFX/nerf_shot_2.mp3"
define audio.nerf_trigger = "mod_assets/SFX/nerf_trigger.mp3"
define audio.kettle1 = "<from 0 to 42.342 loop 28.428>mod_assets/SFX/kettle.ogg"
define audio.kettle2 = "<from 42.342>mod_assets/SFX/kettle.ogg"
define audio.running_int = "<loop 0.0>mod_assets/SFX/running_int.wav"
define audio.hum = "<loop 0.0>mod_assets/SFX/hum.ogg"
define audio.tap_water = "mod_assets/SFX/tap_water.ogg"
define audio.tap_water_loop = "<loop 15 to 34>mod_assets/SFX/tap_water.ogg"
define audio.phone_notification = "mod_assets/SFX/phone_notification.ogg"
define audio.phone_alarm = "<loop 0.0>mod_assets/SFX/phone_alarm.ogg"

define audio.glitch = "sfx/s_kill_glitch1.ogg"
define audio.glitch2 = "sfx/glitch3.ogg"
define audio.glitch3 = "sfx/interference.ogg"

define audio.rain_int = "<loop 2.102>mod_assets/Ambiance/rain_int.ogg"
define audio.ext_day = "<loop 3.090>mod_assets/Ambiance/ext_day.ogg"
define audio.ext_night = "<loop 4.103>mod_assets/Ambiance/ext_night.ogg"
define audio.int_day = "<loop 3.090>mod_assets/Ambiance/int_day.ogg"
define audio.int_night = "<loop 4.103>mod_assets/Ambiance/int_night.ogg"
define audio.students = "<loop 0.0>mod_assets/Ambiance/students.ogg"

####
define 200 cinematic_bars_y = absolute((config.screen_height * (1.0 - gui.textbox_ypos)) + gui.namebox_height)

image _cinematic_bar       = Solid("#000", xsize=1.5, xalign=0.5, ysize=700)
image cinematic_bar_top    = "_cinematic_bar"
image cinematic_bar_bottom = "_cinematic_bar"

transform cinematic_bar(is_top, on_show_anim=0.5, on_hide_anim=0.5):
    on show:
        alpha 0.0 yanchor (1.0 if is_top else 0.0) ypos (0.0 if is_top else 1.0)
        easein on_show_anim alpha 1.0 yanchor (1.0 if is_top else cinematic_bars_y) ypos (cinematic_bars_y if is_top else 1.0)
    on hide:
        alpha 1.0 yanchor (1.0 if is_top else cinematic_bars_y) ypos (cinematic_bars_y if is_top else 1.0)
        easein on_hide_anim alpha 0.0 yanchor (1.0 if is_top else absolute(0)) ypos (absolute(0) if is_top else 1.0)

####
define narrator = Character(None, ctc="ctc", ctc_position="fixed")

define _base_char = Character(what_prefix='"', what_suffix='"', kind=narrator)

define who = Character("???", kind=_base_char)
define amogus = Character(kind=who, voice_tag="amogus")

#########
define mc = DynamicCharacter("mc_name", image="melody", kind=_base_char, voice_tag="mc")
define _mc = Character(kind=narrator, what_italic=True, image=mc.image_tag, voice_tag=mc.voice_tag)

define dadmc  = Character("Dad", kind=_base_char)
define b = Character(_("Boss"), image="boss", kind=_base_char, voice_tag="b")

#########
define s = DynamicCharacter("s_name", image="sayori", kind=_base_char, voice_tag="s")
define _s = Character(kind=narrator, what_italic=True, image=s.image_tag, voice_tag=s.voice_tag)

define m = DynamicCharacter("m_name", image="monika", kind=_base_char, voice_tag="m")
define _m = Character(kind=narrator, what_italic=True, image=m.image_tag, voice_tag=m.voice_tag)

define n = DynamicCharacter("n_name", image="natsuki", kind=_base_char, voice_tag="n")
define _n = Character(kind=narrator, what_italic=True, image=n.image_tag, voice_tag=n.voice_tag)

define y = DynamicCharacter("y_name", image="yuri", kind=_base_char, voice_tag="y")
define _y = Character(kind=narrator, what_italic=True, image=y.image_tag, voice_tag=y.voice_tag)

#########
define a = DynamicCharacter("aika_name", image="aika", kind=_base_char, voice_tag="a")
define _a = Character(kind=narrator, what_italic=True, image=a.image_tag, voice_tag=a.voice_tag)

#########
define k = DynamicCharacter("kaito_name", image="kaito", kind=_base_char, voice_tag="k")

define am = DynamicCharacter("amelia_name", image="amelia", kind=_base_char, voice_tag="am")
define _am = Character(kind=narrator, what_italic=True, image=am.image_tag, voice_tag=am.voice_tag)

define e = DynamicCharacter("ellen_name", image="ellen", kind=_base_char, voice_tag="e")
define _e = Character(kind=narrator, what_italic=True, image=e.image_tag, voice_tag=e.voice_tag)

#########
define dadm  = DynamicCharacter("dadm_name", image="dadm", kind=_base_char, voice_tag="dadm")
define momm  = Character("Mother", image="momm", kind=_base_char, voice_tag="momm")

# common stuff
define t = Character(_("Teacher"), kind=_base_char)
define cu = Character(_("Customer"), kind=_base_char)

# nat route
image rc = At(CharacterSilhouette("mod_assets/STUFF/rude_customer_silhouette.png"), AutofocusDisplayable(name="rc"))
define rc = Character(_("Rude Customer"), image="rc", kind=_base_char)

# mc wiping the floor in Snared
image mrs_mills = At(CharacterSilhouette("mod_assets/STUFF/mrsidamybeloved.png"), AutofocusDisplayable(name="mrs_mills"))
define mrs_mills = Character(_("Mrs Mills"), kind=_base_char, image="mrs_mills")

# natsuki route. 2nd arcade scene
image goobi = CharacterSilhouette("mod_assets/STUFF/gubbeymybeloved.png")
image arcade_silhouette_1 = CharacterSilhouette("mod_assets/STUFF/arcade_silhouette_1.png")
image arcade_silhouette_2 = CharacterSilhouette("mod_assets/STUFF/arcade_silhouette_2.png")

image leo = At(CharacterSilhouette("mod_assets/STUFF/wallacemybeloved.png"), Transform(zoom=0.8), AutofocusDisplayable(name="leo"))
define l = DynamicCharacter("leo_name", image="leo", kind=_base_char, voice_tag="l")

# mc "eating" sayori scene
# god this sounds so bad
image rooftop_teacher_silhouette = CharacterSilhouette("mod_assets/STUFF/rooftop_teacher_silhouette.png")
define rooftop_teacher = Character(_("Teacher"), kind=_base_char, image="rooftop_teacher_silhouette", autofocus=False)

default widenekoflap_name = "???"
define wnf = DynamicCharacter("widenekoflap_name", kind=_base_char, image="widenekoflap", autofocus=False)

define vp = Character(_("Vice President"), kind=_base_char)

default mc_name = _("Melody")
default s_name = _("Sayori")
default m_name = _("Monika")
default n_name = _("Natsuki")
default y_name = _("Yuri")
default aika_name = _("Aika")
default amelia_name = _("Amelia")
default kaito_name = _("Kaito")
default ellen_name = _("Ellen")
default leo_name = _("???")
default dadm_name = _("Father")

define _dismiss_pause = config.developer
default allow_skipping = True
default basedir = config.basedir
default currentpos = 0

#       fr fr
# jk it's Feelings Rekindled
default fr_told_yuri = False

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
