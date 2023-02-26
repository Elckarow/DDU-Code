label start:
    $ anticheat = persistent.anticheat
    $ _dismiss_pause = config.developer
    $ quick_menu = True
    $ allow_skipping = True
    $ config.allow_skipping = True

    call week_1_monday_common from _call_week_1_monday_common
    call week_1_tuesday_common from _call_week_1_tuesday_common

    stop music fadeout 2.0
    scene black zorder 0
    show expression "gui/end.png" at truecenter
    with dissolve_scene_full
    pause 3.0
    scene black with Dissolve(1.0)

    $ renpy.utter_restart()

    return