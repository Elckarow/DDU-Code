init -200:
    define gui.phone_margin = (15, 81, 15, 94)
    define gui.phone_zoom = 0.8
    define gui.phone_xsize = 389
    define gui.phone_ysize = 803

    define gui.phone_status_bar_height = 22

    define gui.phone_call_xpos = 0.07

    define gui.phone_message_frame_padding = (8, 8, 8, 8)

    define gui.phone_message_label_null_height = 4

    define gui.phone_application_frame_padding = 16
    define gui.phone_application_icon_size = 65
    define gui.phone_application_rounded_corners_radius = 17

    define gui.phone_calendar_button_size = 40

    define gui.phone_control_center_spacing = 10
    define gui.phone_control_center_block_size = 70
    define gui.phone_control_center_block_scaling_factor = 0.75
    define gui.phone_control_center_block_rounded_corners_radius = 22

init offset = -10

init python:
    gui.init(1280, 720)

define gui.default_font = "gui/font/Aller_Rg.ttf"

define gui.main_menu_button_ysize = 36

define gui.text_size = 20

define gui.textbox_width = 989
define gui.textbox_height = 134

define gui.textbox_ypos = 0.81
define gui.textbox_padding = (60, 23, 80, 0)

define gui.textbox_background = "#000000ad"

define gui.namebox_width = 230
define gui.namebox_height = 31
define gui.namebox_text_size = 21

define gui.side_image_spacing = 10
# after adjusting the gui values according to renpy.variant
define 50 gui.xoffset_due_to_side_image = (gui.textbox_height + gui.side_image_spacing) / 2.0

define gui.quick_menu_button_margin = (0, 0)
define gui.quick_menu_afm_pos = (0.925, 9)
define gui.quick_menu_afm_button_margin = (1, 1)
define gui.quick_menu_skip_pos = (0.95, 9)


define gui.config_nav_buttons_size = (169, 32)
define gui.config_nav_buttons_spacing = 2


define gui.config_display_left_side_xsize = 460
define gui.config_display_spacing = 20
define gui.config_display_right_side_spacing = 5
define gui.config_display_buttons_size = (169, 32)

define gui.notify_text_size = 18

define gui.hover_sound = "mod_assets/STUFF/hover_sound.ogg"
define gui.activate_sound = "mod_assets/STUFF/activate_sound.ogg"

define gui.unscrollable = "hide"

define gui.bar_tile = False
define gui.bar_size = 18
define gui.bar_margin = absolute(gui.bar_size * (2.0 / 9.0))
define gui.bar_radius = 8
define gui.bar_borders = Borders(0, 0, 0, 0)

define gui.scrollbar_tile = False
define gui.scrollbar_borders = gui.bar_borders

define gui.slider_tile = False
define gui.slider_borders = gui.bar_borders

define gui.vbar_borders = gui.bar_borders
define gui.vscrollbar_borders = gui.bar_borders
define gui.vslider_borders = gui.bar_borders

init python hide:
    if is_android():
        gui.main_menu_button_ysize = 43
        

        gui.bar_size = 25    

        bar_margin = 4
        gui.bar_borders.left = bar_margin
        gui.bar_borders.top = bar_margin
        gui.bar_borders.right = bar_margin
        gui.bar_borders.bottom = bar_margin


        gui.quick_menu_button_margin = (3, 3)


        gui.config_nav_buttons_size = (300, 40)
        gui.config_nav_buttons_spacing = 20

        gui.config_display_left_side_xsize = 500
        gui.config_display_spacing = 60
        gui.config_display_right_side_spacing = 9
        gui.config_display_buttons_size = (200, 38)


        gui.notify_text_size = 20


# not used but renpy is a sussy baka
define gui.button_width = None
define gui.button_height = 36
define gui.button_tile = False
define gui.button_borders = Borders(0, 0, 0, 0)

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
