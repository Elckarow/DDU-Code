define config.name = _("Doki Doki Undercurrents")
define config.version = "demo 1.0"

define config.developer = False 
define config.autoreload = False 

define DEFAULT_TEXT_CPS = 125
define DEFAULT_AFM_TIME = 15
define DEFAULT_MUSIC_VOLUME = 0.75
define DEFAULT_SFX_VOLUME = 0.60
define DEFAULT_AMBIENT_VOLUME = 0.75
define DEFAULT_VOICE_VOLUME = 0.80

default preferences.text_cps = DEFAULT_TEXT_CPS
default preferences.afm_time = DEFAULT_AFM_TIME
default preferences.music_volume = DEFAULT_MUSIC_VOLUME
default preferences.sfx_volume = DEFAULT_SFX_VOLUME

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = audio.title

define config.enter_transition = Dissolve(0.2)
define config.exit_transition = Dissolve(0.2)

define 5 config.enter_yesno_transition = game_menu_transition # screens/game_menu/game_menu.rpy

define config.after_load_transition = Dissolve(0.4)
define config.end_splash_transition = Dissolve(1.0, time_warp=_warper.easeout)

define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

define config.narrator_menu = True
define 5 config.mouse_hide_time = persistent.mouse_hide_time # screens/game_menu/computer/display.rpy

define config.save_directory = "Undercurrents_DEMO_1"
define config.window_icon = "mod_assets/STUFF/logo_small.png"

define config.image_cache_size = 64
define config.predict_statements = 50
define config.history_length = 50

define config.rollback_enabled = config.developer
define config.allow_skipping = True

define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0

define config.layers = [ "master", "transient", "screens", "overlay", "front" ]
define config.menu_clear_layers = [ "front" ]

define config.gl2 = True
define config.gl_test_image = "white"

define config.atl_start_on_show = True

define config.voice_filename_format = "mod_assets/Voice/{filename}"
default preferences.emphasize_audio = True

define config.main_menu_music = audio.title

define config.tag_zorder["cg"] = 7
define config.tag_zorder["blink"] = 6
define config.tag_zorder["white"] = 5
define config.tag_zorder["black"] = 5
define config.tag_zorder["bg"]    = 0 # useless but f u
define config.tag_zorder["split"] = 0

define config.thumbnail_width = 256
define config.thumbnail_height = 144

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    _preferences.pad_enabled = False

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)
        
    config.adjust_view_size = force_integer_multiplier

    def replace_text(s):
        s = s.replace(u"\u2026", "...")
        return s
    
    config.replace_text = replace_text
                                                    # because fuck you
    config.start_callbacks.append(lambda: renpy.run(Preference("auto-forward", "disable")))
    config.start_callbacks.append(lambda: renpy.run(FilePage(1)))

    if config.developer:
        config.start_callbacks.append(lambda: renpy.run(Preference("rollback side", "left")))

    def glitch(tag, x):
        return [
            (renpy.TEXT_TEXT, "".join(random.choices("¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž", k=int(x)))),
        ]

    config.self_closing_custom_text_tags["glitch"] = glitch

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

    def json_callback(d):
        d["week"] = store.week
        d["day"] = store.day

    config.save_json_callbacks.append(json_callback)

    def history_callback(h):
        h.pov_color = pov_color()
        h.voice_info = _get_voice_info()
    
    config.history_callbacks.append(history_callback)

    cg_dissolve = Dissolve(0.12)

    _say_attribute_transition_map = {
        "cg": cg_dissolve
    }

    def say_attribute_transition_callback(*args):
        return _say_attribute_transition_map.get(args[0], None), config.say_attribute_transition_layer
    
    config.say_attribute_transition_callback = say_attribute_transition_callback

#############################################################################################################
#############################################################################################################
#############################################################################################################

init python:
    build.name = "DokiDokiUndercurrents"
    build.directory_name = build.name + "D1"

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

    build.classify("game/python-packages/**", "mod all")
    build.classify("game/tl/**", "mod all")
    build.classify("credits.txt", "mod all")

    build.classify("game/mod_assets/**", "mod_assets all")
    
    build.classify("game/screens/**", "scripts all")
    build.classify("game/**.rpyc", "scripts all")

    build.classify("game/cache/*.*", None)
    build.classify("game/saves/**", None)
    build.classify("game/**.rpa", None)
    build.classify("**.md", None)
    build.classify("**.rpy", None)

    build.classify("**~", None)
    build.classify("**.bak", None)
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
