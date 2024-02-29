init -100 python hide:
    for archive in ["audio", "images", "fonts"]:
        if not archive in config.archives:
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")

# sussy baka
define console.sussy_cps = 28

screen splashload(duration, glitch_effect):
    default done = False

    add "#000"
    default outlines_width = 1
    default start_time = time.time()

    hbox align (0.5, 0.5) spacing 80:
        for i in range(15):
            add Solid("#fff", xsize=1):
                at transform:
                    alpha 0.0
                    i / 20
                    easein_quint 0.3 alpha 0.2

    vbox align (0.5, 0.5) spacing 80:
        for i in range(12):
            add Solid("#fff", ysize=1):
                at transform:
                    alpha 0.0
                    i / 20
                    easein_quint 0.3 alpha 0.2

    default delay1 = 1.5
    default delay2 = 0.25

    default bar_hide = 0.65
    default welcome_show = 0.52

    fixed style "empty":
        if glitch_effect and done:
            at transform:
                matrixcolor TintMatrix("#b3221d")

        fixed style "empty":
            xysize (700, 300)
            align (0.5, 0.55)

            hbox xalign 0.05 yalign 0.05 spacing 3:
                for i in range(3):
                    circle border 1 radius 10:    
                        at transform:
                            xoffset -5 alpha 0.0 subpixel True
                            delay2
                            i / 10
                            easein_quart 0.5 alpha 1.0 xoffset 0

            add Solid("#fff", xsize=outlines_width) xalign 0.0:
                at transform:
                    subpixel True
                    ysize 0.0
                    delay2
                    easein_quart 0.4 ysize 1.0

            add Solid("#fff", xsize=outlines_width) xalign 1.0:
                at transform:
                    subpixel True
                    ysize 0.0
                    delay2 * 2
                    easein_quart 0.4 ysize 1.0

            add Solid("#fff", ysize=outlines_width) yalign 0.0:
                at transform:
                    subpixel True
                    xsize 0.0
                    delay2
                    easein_quart 0.4 xsize 1.0

            add Solid("#fff", ysize=outlines_width) yalign 1.0:
                at transform:
                    subpixel True
                    xsize 0.0
                    delay2 * 2
                    easein_quart 0.4 xsize 1.0

            timer (
                duration * (random.uniform(0.6, 0.78) if glitch_effect else 1.0)
                + delay1
                + (0.2 if not glitch_effect else 0.0)
            ) action SetScreenVariable("done", True)

            if done:
                vbox xalign 0.5 spacing -3 yalign 0.45:
                    if glitch_effect:
                        text "ACCESS DENIED" style "splashload"
                        text "0x0090-0x03" style "splashload" size 16 xalign 0.0 font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Light.ttf"
                    else:
                        text _("Welcome") style "splashload" color "#fff" italic True:
                            at transform:
                                alpha 0.0 yoffset 30
                                bar_hide * 0.8
                                ease welcome_show alpha 1.0 yoffset 0

        if not (glitch_effect and done):
            fixed:
                if done:
                    at transform:
                        alpha 1.0 yoffset 0
                        0.2
                        ease bar_hide alpha 0.0 yoffset 30

                fixed style "empty":
                    at transform:
                        nearest True
                        align (0.5, 0.52) xysize (400, 20)

                    add Solid("#fff", xsize=outlines_width) xalign 0.0:
                        at transform:
                            subpixel True
                            ysize 0.0
                            (delay1 * 0.66) + delay2
                            easein_quart 0.4 ysize 1.0

                    add Solid("#fff", xsize=outlines_width) xalign 1.0:
                        at transform:
                            subpixel True
                            ysize 0.0
                            (delay1 * 0.66) + (delay2 * 2)
                            easein_quart 0.4 ysize 1.0

                    add Solid("#fff", ysize=outlines_width) yalign 0.0:
                        at transform:
                            subpixel True
                            xsize 0.0
                            (delay1 * 0.66) + delay2
                            easein_quart 0.4 xsize 1.0

                    add Solid("#fff", ysize=outlines_width) yalign 1.0:
                        at transform:
                            subpixel True
                            xsize 0.0
                            (delay1 * 0.66) + (delay2 * 2)
                            easein_quart 0.4 xsize 1.0

                    frame style "empty":
                        xysize (1.0, 1.0) padding ((outlines_width * 2) + 2, (outlines_width * 2) + 2)
                        yalign 0.5

                        add "#fff":
                            at transform:
                                subpixel True xsize 0.0
                                delay1
                                linear duration xsize 1.0

                default cd = False
                timer delay1 action SetScreenVariable("cd", True)

                if cd:
                    add DynamicDisplayable(
                        lambda st, at, start_time, duration: (Text("{:.2f}%".format(min((time.time() - start_time) / duration, 1.0) * 100), style="progress_text"), 0.0),
                        start_time=start_time + delay1,
                        duration=duration
                    ):
                        at transform:
                            alpha 0.0
                            easein_cubic 0.2 alpha 1.0

    if done:
        timer (0.0001 if glitch_effect else (bar_hide + welcome_show + 0.7)):
            action (
                Return(),
                If(
                    not glitch_effect,
                    true=With(Dissolve(1.7, time_warp=_warper.easeout_quad)),
                    false=(With(Glitch(1.2, number=5, times=(5.0, 0.0), offsetRange=(0, 150), chroma=False)), Play("sound_loop", audio.glitch3))
                )
            )

style progress_text:
    size 20
    color "#fff"
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Light.ttf"
    outlines []
    align (0.37, 0.488)

style splashload:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf"
    outlines []
    size 50

default persistent.intro_flag_1 = True
default persistent.intro_flag_2 = False

default persistent.tos = False

label splashscreen:
    # return
    $ custom_keymap.allowed = False
    $ config.allow_skipping = config.developer
    play sound_loop hum

    python in console:
        show(None, 1.2 + random.uniform(0.5, 1.0))
        input(__("Reading files at {path}").format(path=store.get_safe_path(store.config.basedir.replace("\\", "/"))), cps=None, delay=random.uniform(1.2, 1.9))
        input(__("Reading persistent data at {path}").format(path=store.get_safe_path(store.config.savedir.replace("\\", "/")) + "/persistent"), cps=None, delay=random.uniform(2.3, 3.7))

    if not persistent.tos:
        python hide in console:
            input(_("Terms of Service not accepted"), cps=None, delay=random.uniform(0.4, 0.85))
            output(_("[config.name!t] is a Doki Doki Literature Club fan mod that is not affiliated with Team Salvato."), cps=30, delay=None)
            output(_("It is designed to be played only after the official game has been completed, and contains spoilers for the official game."), cps=30, delay=None)
            output(_("Game files for DDLC are required to play this mod and can be downloaded for free at {url=http://ddlc.moe} or from Steam."), cps=30, delay=None)
            output(_("By playing [config.name!t] you agree that you have completed DDLC and accept spoilers contained within (type y/n and enter)."), cps=30, delay=-1)

            rv = interact(length=1, allow="ynYN", empty=False, input_entry=True)

            if rv.lower() == "n":
                pause(random.uniform(0.5, 1.0))
                renpy.quit()

        stop sound_loop
        play sound glitch
        $ glitch(0.5, number=12, offsetRange=(0, 80), show_window_after=False)

        python:
            console.hide(None, -1)
            console.clean_history()

            preferences.volumes["ambient"] = DEFAULT_AMBIENT_VOLUME
            preferences.volumes["voice"] = DEFAULT_VOICE_VOLUME
            quick_menu = False

        call prologue from _call_prologue

        play sound_loop hum 
        $ console.clear_history()
        $ console.show(None, delay=1.0)

    python in console:
        input(_("Loading OS from {path}").format(path=store.get_safe_path(store.config.basedir.replace("\\", "/")) + "/" + store.build.executable_name), cps=None, delay=random.uniform(0.2, 0.5))
        input(_("Loading OS"), cps=None, delay=random.uniform(2.3, 3.1))
        renpy.music.stop("sound_loop")
        pause(random.uniform(0.05, 0.2))
        hide(None)
        clear_history()

    call screen splashload(3.0, not persistent.intro_flag_1)
    scene black
    show white

    if not persistent.intro_flag_1:
        pause 1.2
        $ stop_channels(0.05)
        pause 2.5
    else:
        pause 1.8
        $ stop_channels(0.05)
        pause 1.9

    if persistent.intro_flag_1:
        if persistent.intro_flag_2:
            pass

        else:
            hide white 
            stop sound_loop
            $ console.show(None, delay=-1)
            $ console.input(_("Atta boy."), cps=None)
            play sound glitch2
            with NewWidgetTransition(Glitch(0.4, number=12, offsetRange=(0, 80), times=(5.0, 0.0)))
            play sound_loop hum

            python in console:
                input(_("Geez, I almost let that one slip."), cps=sussy_cps)
                pause()
                input(_("Let's not get ahead of ourselves, darling."), cps=sussy_cps)
                pause()
                input(_("It's better if you... {i}experience{/i} this world first..."), cps=sussy_cps)
                pause()
                input(_("Then, I'll let you in."), cps=sussy_cps)
                pause()
                input(_("Got it?"), cps=sussy_cps)
                pause()
                input(_("I know you'll understand."), cps=sussy_cps)
                pause()
                input(_("And I..."), cps=sussy_cps)
                pause()
                input(_("I'm sorry."), cps=None)
                renpy.music.stop("sound_loop")
            
            play sound_loop glitch3
            with NewWidgetTransition(Glitch(1.0, number=12, offsetRange=(0, 80), times=(5.0, 0.0)))
            stop sound_loop

            python:
                console.hide(None, -1)
                console.clear_history()

                persistent.intro_flag_1 = False
                renpy.save_persistent()
    
    $ config.allow_skipping = False
    
    play music config.main_menu_music

    scene white zorder 0
    with None
    
    show expression "mod_assets/STUFF/studiosilver.png":
        subpixel True xsize 270 fit "contain"
        align (0.5, 0.5)

    with Dissolve(0.5)
    pause 3.494817
    scene white zorder 0 with Dissolve(0.983882)

    $ splash_message.splash_message()

    if not persistent.tos:
        $ persistent.tos = True
        show text _("Click to proceed"):
            subpixel True
            anchor (1.0, 1.0) pos (0.97, 0.97)
            alpha 0.0
            block:
                easein 0.8 alpha 1.0
                easeout 0.8 alpha 0.0
                repeat

    $ pause()

    scene white with Dissolve(0.5)

    $ config.allow_skipping = True
    $ custom_keymap.allowed = True
    window auto
    return

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc