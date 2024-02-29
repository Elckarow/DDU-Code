define dissolve_scene_full = Fade(1.0, 1.0, 1.0)

init -3 python:
    def NonBlockingTransition(trans):
        return {
            layer: trans 
            for layer in master_layers # see options.rpy
        }

    def NonBlockingDissolve(*args, **kwargs):
        return NonBlockingTransition(Dissolve(*args, **kwargs))

    # now we can have a wipe in any direction
    def Wipe(time=0.5, theta=-90, ramplen=64, **kwargs):
        return ImageDissolve(
            Flatten(
                Fixed(
                    "#fff",
                    Gradient("#00000000", "#000", theta=theta)
                )
            ),
            time,
            ramplen=ramplen,
            **kwargs
        )

    wipeleft = Wipe()
    wiperight = Wipe(theta=90)
    wipeup = Wipe(theta=180)
    wipedown = Wipe(theta=0)

    def WipeScene(time=0.5, pause=0.25, theta=-90, color=Color("#000")):
        return MultipleTransition(
            [
                False, Wipe(time=time, theta=theta),
                Solid(color), Pause(pause),
                Solid(color), Wipe(time=time, theta=theta),
                True
            ]
        )
    
    wipeleft_scene = WipeScene()

    def PovSwitch(color, fade=False):
        return (                                  # see definitions.rpy
            WipeScene(0.35, pause=0.3, theta=-(90 - angle_from_tl_to_br), color=color)
            if not fade 
            else Fade(0.6, 0.2, 0.6, color=color)
        )

    monika_pov  = renpy.partial(PovSwitch, "#08c008")
    sayori_pov  = renpy.partial(PovSwitch, "#227ef8")
    natsuki_pov = renpy.partial(PovSwitch, "#fbb")
    yuri_pov    = renpy.partial(PovSwitch, "#760da1")
    mc_pov      = renpy.partial(PovSwitch, "#3a2527")
    amelia_pov  = renpy.partial(PovSwitch, "#ffe22e")

    fastfade = Fade(0.25, 0.0, 0.25)
    longfade = Fade(1.0, 0.0, 1.0)

    # mostly useful for the Glitch transition
    # when doing shit with screens
    def NewWidgetTransition(trans):
        """
        A transition that always displays the new scene.
        """
        def inner(old_widget, new_widget):
            return trans(old_widget=new_widget, new_widget=new_widget)
        return inner

# transition
# function
# show layer at 
#
# me omw to code 1000 ways to show a glitch effect
transform Glitch(t, number=10, times=(0.24, 0.24), offsetRange=(0, 50), chroma=True, key=None, render_child=True, old_widget=None, new_widget=None):
    events False delay t
    At(old_widget, TearDisplayable(number=number, times=times, offsetRange=offsetRange, chroma=chroma, key=key, render_child=render_child))
    t
    new_widget

init python:
    def glitch(t, *args, show_window_after=True, **kwargs):
        renpy.show_screen("tear", *args, **kwargs)
        _window_hide(None, auto=True)
        pause(t)
        if show_window_after:
            _window_show(None, True)
        renpy.hide_screen("tear")






# https://github.com/renpy/renpy/issues/4532
transform _close_eyes(duration, base_blur):
    easein_quad duration blur base_blur + 3.0

transform _close_eyes_color(duration):
    alpha 0.0
    easein_quad duration alpha 1.0

transform _open_eyes(duration, base_blur):
    easein_quad duration blur base_blur

transform _open_eyes_color(duration):
    alpha 1.0
    easein_quad duration alpha 0.0

transform _blink_eyes(duration, base_blur):
    easein_cubic duration / 2.0 blur base_blur + 3.0
    easeout_quad duration / 2.0 blur base_blur

transform _blink_eyes_color(duration):
    alpha 0.0
    easein_cubic duration / 2.0 alpha 1.0
    easeout_quad duration / 2.0 alpha 0.0

label _eyes(duration, mode, color, wait, base_blur):
    python:
        if mode not in ("close", "open", "blink"):
            raise Exception(mode)

    if wait:
        window hide

    if mode == "close":
        camera master at _close_eyes(duration, base_blur)
        #                                  im stuff
        show expression Solid(color) as _eyes_stuff zorder 50 at _close_eyes_color(duration)
    elif mode == "open":
        camera master at _open_eyes(duration, base_blur)
        show expression Solid(color) as _eyes_stuff zorder 50 at _open_eyes_color(duration)
    else: # mode == "blink":
        camera master at _blink_eyes(duration, base_blur)
        show expression Solid(color) as _eyes_stuff zorder 50 at _blink_eyes_color(duration)

    if wait:
        pause duration
        window auto
    return

label open_eyes(duration=1.0, color="#000", wait=False, base_blur=0):
    call _eyes(duration, "open", color, wait, base_blur) from _call__eyes
    return

label close_eyes(duration=1.0, color="#000", wait=False, base_blur=0):
    call _eyes(duration, "close", color, wait, base_blur) from _call__eyes_1
    return

label blink(duration=0.5, color="#000", wait=False, base_blur=0):
    call _eyes(duration, "blink", color, wait, base_blur) from _call__eyes_2
    return