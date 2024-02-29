define config.name = _("Doki Doki Undercurrents")
define config.version = "demo 2.1.0"

define config.developer = False
define config.autoreload = False

define DEFAULT_TEXT_CPS = 125
define DEFAULT_AFM_TIME = 15
define DEFAULT_MUSIC_VOLUME = 0.80
define DEFAULT_SFX_VOLUME = 0.80
define DEFAULT_AMBIENT_VOLUME = 0.80
define DEFAULT_VOICE_VOLUME = 0.80

# phone
define config.early_start_store = False

default preferences.text_cps = DEFAULT_TEXT_CPS
default preferences.afm_time = DEFAULT_AFM_TIME
default preferences.music_volume = DEFAULT_MUSIC_VOLUME
default preferences.sfx_volume = DEFAULT_SFX_VOLUME

define config.linear_fades = True

# these config variables are useless btw
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = audio.title

define config.enter_transition = Dissolve(0.2)
define config.exit_transition = Dissolve(0.2)

define config.enter_yesno_transition = None

define config.after_load_transition = None
define config.end_splash_transition = Dissolve(1.0, time_warp=_warper.easeout)

define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

define config.narrator_menu = True
define 5 config.mouse_hide_time = persistent.mouse_hide_time

define config.save_directory = "Undercurrents_DEMO_2_SLEEPOVER"
define config.window_icon = "mod_assets/STUFF/logo_small.png"

define config.hard_rollback_limit = 100 * bool(config.developer)

define config.image_cache_size = 64
define config.predict_statements = 50
define config.history_length = 35

define config.rollback_enabled = config.developer
define config.allow_skipping = True

define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0

# "master" layers are added later
define config.layers = ["transient", "screens", "overlay", "front"]
define config.menu_clear_layers = ["front"]

define config.gl2 = True
define config.gl_test_image = "white"

define config.voice_filename_format = "mod_assets/Voice/{filename}"
default preferences.emphasize_audio = True

define config.tag_zorder["white_flashback"] = 10
define config.tag_zorder["cg"] = 7
define config.tag_zorder["white"] = 5
define config.tag_zorder["black"] = 5
define config.tag_zorder["bg"]    = 0 # useless but f u

define config.thumbnail_width = 256
define config.thumbnail_height = 144

define config.skip_indicator = False

# android gestures are handled in custom_keymap.rpy
init python hide:
    config.window_auto_hide.remove("menu")
    
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    _preferences.pad_enabled = False

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

    config.adjust_view_size = force_integer_multiplier

                                                    # because fuck you
    config.start_callbacks.append(lambda: renpy.run(Preference("auto-forward", "disable")))
    config.start_callbacks.append(lambda: renpy.run(FilePage(1)))

    if config.developer:
        config.start_callbacks.append(lambda: renpy.run(Preference("rollback side", "left")))

    config.self_closing_custom_text_tags["glitch"] = \
        lambda tag, x: [
            (renpy.TEXT_TEXT, "".join(random.choices("¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž", k=int(x)))),
        ]
    config.self_closing_custom_text_tags["url"] = \
        lambda tag, url: [
            (renpy.TEXT_TAG, "a={}".format(url)),
            (renpy.TEXT_TEXT, url),
            (renpy.TEXT_TAG, "/a"),
        ]

    def screenshot_callback(path):
        message = __("Saved screenshot as {path}.").format(path=path)

        with open(path, "rb") as g:
            data = g.read()

        if data:
            if persistent.save_screenshots:
                date = datetime.datetime.now()
                persistent.screenshots[date] = (data, path)
                renpy.save_persistent()

            if renpy.get_screen("screenshot_notify") is not None:
                renpy.hide_screen("screenshot_notify")

            renpy.show_screen("screenshot_notify", d=im.Data(data, path), message=message)

        else:
            renpy.notify(message)

    config.screenshot_callback = screenshot_callback

    @config.save_json_callbacks.append
    def json_date(d):
        d["date"] = phone.system.get_date().timetuple()
    
    @config.save_json_callbacks.append
    def json_branch_name(d):
        d["branch_name"] = branches.names[branches.get_current()]
    
    @config.save_json_callbacks.append
    def save_last_said_dialogue(d):
        d["last_dialogue"] = store._last_say_what
    
    @config.save_json_callbacks.append
    def save_last_said_dialogue(d):
        d["language"] = store.language

    @config.history_callbacks.append
    def save_say_side_image(h):
        def history_side_image_adjust_attrs(attrs):
            if "blink" in attrs:
                attrs.remove("blink")

            # no need to check if the attribute exists
            # the error message only appears with dev mode on
            # :monikk:
            attrs.append("noblink")
            return attrs

        h.say_side_image = GetSayCharacterPortrait(adjust_attrs=history_side_image_adjust_attrs)
    
    def add_detached_layer(layer):
        config.detached_layers.append(layer)
        config.layer_clipping[layer] = (0, 0, config.screen_width, config.screen_height)
    
    add_detached_layer("detached_layer_1")

    def say_attribute_transition_callback(tag, mode, pre, post):
        trans = _say_attribute_transition_map.get(tag, say_dissolve) if say_transition else None
        return trans, config.say_attribute_transition_layer

    config.say_attribute_transition_callback = say_attribute_transition_callback

init python:
    master_layers = ["master", "above_master"]
    config.layers = master_layers + config.layers
    config.sticky_layers.extend(master_layers[1:])

    cg_dissolve = NonBlockingDissolve(0.4)
    say_dissolve = NonBlockingDissolve(0.15)

    _say_attribute_transition_map = {
        "cg": cg_dissolve
    }

default say_transition = False

# /!\ IMPORTANT /!\
# `old` and `new` need to have the same dimension ratio
# or it'll look weird
transform _side_image_transform(t, old, new):
    Transform(old, xysize=(average_character_crop_width, average_character_crop_height))
    Transform(new, xysize=(average_character_crop_width, average_character_crop_height)) with Dissolve(t, mipmap=True, time_warp=_warper.ease)

init python:
    config.side_image_null = Null(average_character_crop_width, average_character_crop_height)
    config.side_image_only_not_showing = True
    config.side_image_change_transform = _side_image_transform(0.1)
    config.side_image_same_transform = _side_image_transform(0.15)

init python hide:
    class AdjustAttributes(object):
        def __init__(self, *fs):
            self.fs = fs
        
        def __call__(self, d):
            d = list(d)
            all_attributes = set(renpy.get_attributes(d[0]) or ()) | set(d)

            for f in self.fs:
                f(d, all_attributes)
            
            return tuple(d)

    def _nat_cut(d, all_attributes):
        if auto_nat_cut and not any(cut in all_attributes for cut in ("nocut", "cut_a", "cut_b")):
            if "nocut" in d:
                d.remove("nocut")
            d.append("cut_a")
        
    config.adjust_attributes["natsuki"] = AdjustAttributes(_nat_cut)

    def _mel_hairclip(d, all_attributes):
        if auto_mel_hairclip and not any(hairclip in all_attributes for hairclip in ("nohairclip", "hairclip")):
            if "nohairclip" in d:
                d.remove("nohairclip")
            d.append("hairclip")
        
    config.adjust_attributes["melody"] = AdjustAttributes(_mel_hairclip)

    # have `d=("side", "tag")` call `config.adjust_attributes["tag"]`
    def _side_adjust_attributes(d):
        f = config.adjust_attributes.get(d[1], config.adjust_attributes.get(None))
        if f is not None:
            d = (d[0],) + f(d[1:])
        return d

    config.adjust_attributes["side"] = _side_adjust_attributes

default auto_nat_cut = False

default auto_mel_hairclip = False

#############################################################################################################
#############################################################################################################
#############################################################################################################

init python:
    build.name = "DokiDokiUndercurrents"
    build.directory_name = build.name

    build.package("Renpy8-DDLCMod", "zip", "windows linux mac renpy mod",
        description="Ren'Py 8 DDLC Compliant Mod")

    build.archive("scripts", "mod")
    build.archive("mod_assets", "mod")

    try:
        build.renpy_patterns.remove(("renpy.py", ["all"]))
        build.classify_renpy("renpy.py", "renpy all")
    except: pass

    try:
        build.early_base_patterns.remove(("*.sh", None))
        build.classify("LinuxLauncher.sh", "linux")
        build.classify("*.sh", None)
    except: pass

    build.classify("credits.txt", "mod all")
    build.classify("game/python-packages/**", "mod all")
    build.classify("game/tl/**", "mod all")
    build.classify("game/**.rpa", None)

    build.classify("**.rpy", None)
    build.classify("game/screens/**", "scripts all")
    build.classify("game/scripts/**", "scripts all")
    build.classify("game/splash/**", "scripts all")
    build.classify("game/**.rpyc", "scripts all")

    build.classify("game/mod_assets/**", "mod_assets all")
    build.classify("game/os/**", "mod_assets all")
    build.classify("game/phone/**", "mod_assets all")
    build.classify("game/displayables/**", "mod_assets all")

    build.classify("game/cache/*.*", None)
    build.classify("game/saves/**", None)
    build.classify("**.md", None)
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**.DS_Store", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**.psd", None)
    build.classify("**.sublime-project", None)
    build.classify("**.sublime-workspace", None)
    build.classify("script-regex.txt", None)
    build.classify("game/10", None)
    build.classify("README.html","mod all")
    build.classify("README.linux", "linux")

    build.include_old_themes = False

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
