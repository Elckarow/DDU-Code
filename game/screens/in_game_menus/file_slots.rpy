screen ig_file_slots():
    tag menu

    default slot_delay_div = 70

    default cols = 5
    default rows = 7

    default selected_slot = 0
    default trans = With(Dissolve(0.5, time_warp=_warper.easein_quint))
    default reset_slot = (SetScreenVariable("selected_slot", 0), trans)

    default rect = Transform(Rectangle("#fff", 2), alpha=0.3)

    use ig_game_menu() id "ig_game_menu":
        hbox spacing 0 ysize 1.0 yfill True style "empty":
            vbox style "empty" spacing 5 xoffset 20 yalign 0.585:
                hbox style "empty" spacing 3:
                    grid cols rows at Flatten:
                        spacing 3

                        for i in range(cols * rows):
                            $ slot = i + 1

                            fixed xysize (117, 65):
                                at transform:
                                    subpixel True
                                    xoffset -10 alpha 0.0
                                    i / slot_delay_div
                                    easein_quart 0.4 xoffset 0 alpha 1.0

                                add "#00000070"

                                if FileLoadable(slot):
                                    add FileScreenshot(slot):
                                        at transform:
                                            xysize (1.0, 1.0)

                                    if not is_android():
                                        # for keyboard focusing
                                        if selected_slot != slot:
                                            # mousearea hovered (SetScreenVariable("selected_slot", slot), trans)
                                            button xysize (1.0, 1.0) activate_sound None:
                                                action NullAction() hovered (SetScreenVariable("selected_slot", slot), trans)

                                        else:
                                            add "#00000030"
                                            use slot_options(selected_slot, reset_slot)

                                            add rect

                                    else:
                                        button xysize (1.0, 1.0) activate_sound None:
                                            action (SelectedIf(ToggleScreenVariable("selected_slot", slot, 0)), trans)
                                            selected_child "#00000071"

                                else:
                                    button:
                                        xysize (1.0, 1.0)
                                        action FileSave(slot)

                                        if not is_android():
                                            hover_child rect
                            
                                if is_android():
                                    add rect
                hbox:
                    if is_android():
                        at transform:
                            zoom 1.2 yoffset 12

                    for page in range(1, 10):
                        button xysize (30, 30):
                            at transform:
                                alpha 0.0
                                ((page - 1) / slot_delay_div) * cols
                                easein_quart 0.4 alpha 1.0

                            background "#ffffff10"
                            hover_background "#ffffff20"
                            selected_idle_background "#ffffff30"
                            selected_hover_background "#ffffff40"

                            text str(page) style "page_button_text" color "#fff" align (0.5, 0.5)
                            action (
                                SelectedIf(FilePage(page)),
                                reset_slot,
                            ) 

            showif selected_slot != 0:
                use ig_info_extension(selected_slot, reset_slot)

screen ig_info_extension(slot, reset_action):
    frame style "empty":
        if not is_android():
            at transform:
                on show:
                    alpha 0.0
                    easein_quint 0.5 alpha 1.0
                on hide:
                    alpha 0.0

        xysize (1.0, 1.0) padding (5, 5, 3, 5)
        background Gradient("#000", "#fff0", theta=90)

        frame:
            xysize (0.9, 1.0) xalign 1.0 yalign 0.0 padding (0, 5, 5, 5)
            vbox anchor (0.0, 0.0) pos (0, 0.18) xoffset -5:
                vbox:
                    text FileJson(s, key="branch_name", empty="", missing="") style "branch_title" font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf" color "#fff" size 14
                    text FileTime(slot, format=__("{#file_time}%B %d %Y, %H:%M")) style "branch_title" size 12 font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf" color "#bbb"
                
                null height 5
                
                text FileJson(slot, key="last_dialogue", empty="", missing="") style "recent_dialogue" color "#bbb" size 14

    if is_android():
        vbox style "empty" ypos 0.895 yanchor 1.0 xanchor 1.0 xoffset -220 yoffset -3 spacing 2:
            textbutton _("SAVE")   action (load_file(slot), reset_action) text_style "return_button_text" text_color "#fff" text_hover_underline True
            textbutton _("LOAD")   action (FileLoad(slot), reset_action) text_style "return_button_text" text_color "#fff" text_hover_underline True
            textbutton _("DELETE") action (FileDelete(slot), reset_action) text_style "return_button_text" text_color "#fff" text_hover_underline True

screen slot_options(slot, reset_action):
    default slot_entries = (
        (Transform("mod_assets/STUFF/main_menu/triangle.png", anchor=(0.5, 0.5), matrixtransform=Matrix.rotate(0, 0, 90), matrixcolor=BrightnessMatrix(1), zoom=0.005), load_file),
        (Transform(phone.asset("quick_menu_save_idle.png"), zoom=0.45), FileSave),
        (Transform("mod_assets/STUFF/main_menu/trash.png", zoom=0.05, matrixcolor=BrightnessMatrix(1.0)), FileDelete),
    )

    grid 2 2 at Flatten:
        at transform:
            on show:
                alpha 0.0
                easein_quint 0.5 alpha 1.0
            on hide:
                easein_quint 0.5 alpha 0.0

        for i, (d, slot_action) in enumerate(slot_entries):
            button style "empty":
                default_focus (i == 0)

                at transform:
                    on idle:
                        easein_quint 0.4 matrixcolor BrightnessMatrix(0.0)
                    on hover:
                        easein_quint 0.4 matrixcolor BrightnessMatrix(0.4)

                xysize (0.5, 0.5)
                background "#00000080"
                action slot_action(slot), reset_action

                add d align (0.5, 0.5)

        button style "empty":
            xysize (0.5, 0.5)
            action reset_action keyboard_focus False