screen calendar_transition():
    default day_size = 100
    default calendar = phone.data["mc"]["calendars"][-1]
    default current_day = phone.system.get_date().day
    default delay_div = 70
    default alpha = 0.6
    default trans_time = 0.4

    default activate_hide = False

    add "#00000080"

    fixed at Transform(alpha=0.3):
        if activate_hide:
            at transform:
                alpha 1.0 xoffset 0.0
                (calendar.length(True) + 7 + 1) / delay_div
                easeout_quart trans_time alpha 0.0 xoffset 5.0
        else:
            at transform:
                alpha 0.0 xoffset -5
                (calendar.length(True) + 7 + 1) / delay_div
                easein_quart trans_time alpha 1.0 xoffset 0.0

        xysize (60, 60)
        align (0.95, 0.95)

        showif renpy.get_screen("calendar_transition_entry") is None:
            fixed:
                at transform:
                    on appear:
                        alpha 1.0
                    on show:
                        ease 0.4 alpha 1.0
                    on hide:
                        easeout 0.3 alpha 0.0

                circle xysize (5, 5) align (0.5, 0.5)
                circle border 1 radius 9 align (0.5, 0.5)

                circle border 1 length 0.25 radius 15 align (0.5, 0.5):
                    at transform:
                        block:
                            rotate 0
                            easein_quint 2.0 rotate 360
                            1.0
                            repeat

                add Solid("#fff", xysize=(40, 1)) align (0.0, 0.5) xoffset -20
                circle xysize (3, 3) align (0.0, 0.5) xoffset -28

    dismiss action SetScreenVariable("activate_hide", True)

    fixed at Flatten:
        vbox align (0.5, 0.5) style "empty" yoffset 30:
            hbox spacing 5:
                if activate_hide:
                    at transform:
                        subpixel True alpha 1.0 xoffset 0.0
                        0
                        easeout_quart trans_time alpha 0.0 xoffset 10.0
                else:
                    at transform:
                        subpixel True
                        xoffset -10 alpha 0.0
                        0
                        easein_quart trans_time xoffset 0 alpha 1.0

                text __(calendar.month_name).upper() style "month_transition"
                text str(calendar.year) style "month_transition" color "#909090"

            grid 7 calendar.rows + 1:
                spacing 3 style "empty"

                for i, day in enumerate(calendar.get_week_days()):
                    frame style "empty" xysize (day_size, 35) background "#00000080":
                        if activate_hide:
                            at transform:
                                nearest True
                                subpixel True alpha 1.0 xoffset 0.0
                                (i + 1) / delay_div
                                easeout_quart trans_time alpha 0.0 xoffset 10.0
                        else:
                            at transform:
                                nearest True
                                subpixel True
                                xoffset -10 alpha 0.0
                                (i + 1) / delay_div
                                easein_quart trans_time xoffset 0 alpha 1.0

                        rectangle "#fff":
                            at transform:
                                alpha alpha

                        text __(day) style "weekday_label":
                            at transform:
                                nearest False

                for j, entry in enumerate(calendar):
                    frame style "empty":
                        if entry and (entry.day == current_day):
                            at transform:
                                easeout 0.5 matrixcolor BrightnessMatrix(0.0)
                                easein 0.5 matrixcolor BrightnessMatrix(0.2)
                                repeat

                        button at day_trans:
                            if activate_hide:
                                at transform:
                                    nearest True
                                    subpixel True alpha 1.0 xoffset 0.0
                                    (j + 7 + 1) / delay_div
                                    easeout_quart trans_time alpha 0.0 xoffset 10.0
                            else:
                                at transform:
                                    nearest True
                                    subpixel True
                                    xoffset -10 alpha 0.0
                                    (j + 7 + 1) / delay_div
                                    easein_quart trans_time xoffset 0 alpha 1.0

                            style "empty"
                            xysize (day_size, day_size)
                            yoffset -58
                            sensitive (not activate_hide)
                            background "#00000080"

                            if entry is not None:
                                if entry.description is not None:
                                    action Show("calendar_transition_entry", desc=entry.description)

                                text str(entry.day) style "weekday_text":
                                    offset (5, 5) underline (entry.description is not None)
                                    color ("#fff" if entry.day >= current_day else "#777")
                                    at transform:
                                        nearest False

                            rectangle "#fff":
                                at transform:
                                    alpha alpha
    
    if activate_hide:
        timer (((calendar.length(True) + 7 + 1) / delay_div) + trans_time) action Return()

screen calendar_transition_entry(desc):
    modal True

    dismiss action Hide("calendar_transition_entry")

    add "#000":
        at transform:
            on show:
                alpha 0.0
                easeout 0.3 alpha 0.45
            on hide:
                ease 0.4 alpha 0.0

    fixed:
        at transform:
            align (0.5, 0.5)
            on show:
                alpha 0.0 zoom 0.7
                easeout 0.3 alpha 1.0 zoom 1.0
            on hide:
                ease 0.4 alpha 0.0 zoom 0.7

        frame style "empty":
            align (0.5, 0.5) xysize (400, 600) modal True

            add "#000000c4"
            rectangle "#fff" border 2:
                at transform:
                    alpha 0.8

            frame style "empty" modal True:
                xysize (1.0, 1.0) padding (20, 10)

                viewport style "empty" id "calendar_transition_entry_vp":
                    mousewheel True draggable True

                    text desc style "month_transition" size 19

transform day_trans:
    on idle:
        easein 0.2 matrixcolor BrightnessMatrix(0.0)
    on hover:
        easeout 0.2 matrixcolor BrightnessMatrix(0.4)

style month_transition:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"
    outlines []
    size 20

style weekday_text:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
    outlines []
    size 20

style weekday_label:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"
    outlines []
    align (0.5, 0.5)
    size 12
