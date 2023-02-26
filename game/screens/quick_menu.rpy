default quick_menu = True

image quick_menu_save = POVDisplayable("mod_assets/STUFF/quick_menu/quick_menu_save_frame_1.png")
image _quick_menu_save_hover:
    animation
    "mod_assets/STUFF/quick_menu/quick_menu_save_frame_1.png"
    pause 0.18
    "mod_assets/STUFF/quick_menu/quick_menu_save_frame_2.png"
    pause 0.18
    "mod_assets/STUFF/quick_menu/quick_menu_save_frame_3.png"
    pause 0.18
    "mod_assets/STUFF/quick_menu/quick_menu_save_frame_2.png"
    pause 0.18
    repeat
image quick_menu_save_hover = POVDisplayable("_quick_menu_save_hover")

image quick_menu_settings = POVDisplayable("mod_assets/STUFF/quick_menu/quick_menu_settings_frame_1.png")
image _quick_menu_settings_hover:
    animation
    "mod_assets/STUFF/quick_menu/quick_menu_settings_frame_1.png"
    pause 0.1
    "mod_assets/STUFF/quick_menu/quick_menu_settings_frame_2.png"
    pause 0.1
    repeat
image quick_menu_settings_hover = POVDisplayable("_quick_menu_settings_hover")

image quick_menu_skip_afm = POVDisplayable("mod_assets/STUFF/quick_menu/quick_menu_skip_afm.png")

screen quick_menu():
    zorder 100

    showif quick_menu:
        imagebutton:
            idle "quick_menu_save"
            hover "quick_menu_save_hover"
            align gui.quick_menu_save_align
            margin gui.quick_menu_button_margin
            action SaveMenu()

        imagebutton:
            idle "quick_menu_settings"
            hover "quick_menu_settings_hover"
            align gui.quick_menu_settings_align
            action SettingsMenu()

        textbutton "▸":
            if _preferences.afm_enable:
                at transform:
                    matrixcolor BrightnessMatrix(-0.2)

            pos gui.quick_menu_afm_pos
            text_style "quick_menu_afm_skip_text"
            text_color pov_color()
            margin gui.quick_menu_afm_button_margin

            action Preference("auto-forward", "toggle")
        
        textbutton "▸▸":
            if renpy.is_skipping():
                at transform:
                    matrixcolor BrightnessMatrix(-0.2)

            pos gui.quick_menu_skip_pos
            text_style "quick_menu_afm_skip_text"
            text_color pov_color()
            margin gui.quick_menu_afm_button_margin
            
            action Skip()

            

style quick_menu_afm_skip_text is default:
    outlines []
    size 25
    font "DejaVuSans.ttf"

style quick_menu_calendar_button:
    xysize (50, 50)
    align (1.0, 0.0)
    background UIDisplayable(RoundedFrame(Solid("#fff"), radius=(0, 0, 20, 0)))