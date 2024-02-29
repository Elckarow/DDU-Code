default quick_menu = True
default phone_available = False

screen quick_menu():
    style_prefix "quick_menu"

    if quick_menu:
        hbox anchor (1.0, 1.0) pos (0.98, 0.0) spacing 3:
            button at quick_menu_button:
                fixed fit_first True:
                    add "mod_assets/STUFF/truck.png":
                        at transform:
                            fit "contain" ysize gui.namebox_height
                            matrixtransform RotateMatrix(0, 0, 180) * ScaleMatrix(-1, 1, 1)
                    
                    if phone_available:
                        fixed xysize (12, 19) align (0.5, 0.5):
                            at Flatten
                            
                            rectangle "#000"
                            rectangle "#000" xysize (0.55, 0.7):
                                anchor (0.5, 0.0) pos (0.5, 0.1)

                            circle xysize (3, 3) border 1 color "#000":
                                align (0.5, 0.92)

                if phone_available:
                    action PhoneMenu("phone")

            button background Solid("#fff"):
                xysize (gui.namebox_height, gui.namebox_height)
                at quick_menu_button

                for i in range(2):
                    circle color "#000" border 1 radius 8 + (3 * i) align (0.5, 0.5)
            
                action ShowMenu("ig_history")
        
        textbutton "▸" style "empty":
            if _preferences.afm_enable:
                at transform:
                    matrixcolor BrightnessMatrix(-0.2)

            pos gui.quick_menu_afm_pos
            margin gui.quick_menu_afm_button_margin
            text_style "quick_menu_button_text"

            action Preference("auto-forward", "toggle")

        textbutton "▸▸" style "empty":
            if renpy.is_skipping():
                at transform:
                    matrixcolor BrightnessMatrix(-0.2)

            pos gui.quick_menu_skip_pos
            margin gui.quick_menu_afm_button_margin
            text_style "quick_menu_button_text"

            action Skip()

style quick_menu_hbox is empty
style quick_menu_button is empty
    
style quick_menu_button_text is empty:
    outlines []
    size 25
    font "DejaVuSans.ttf"


transform quick_menu_button:
    subpixel True alpha 0.7
    on idle:
        easein_quint 0.5 alpha 0.7
    on hover:
        easein_quint 0.5 alpha 0.9