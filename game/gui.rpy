init offset = -10

default persistent.ui_alpha = 0.6

init python:
    gui.init(1280, 720)

define gui.history_height = None
define gui.show_name = False
define gui.about = ""


define gui.default_font = "gui/font/Aller_Rg.ttf"


define gui.sample_textbox_width = 600
define gui.sample_textbox_height = 150


define gui.textbox_width = 989
define gui.textbox_height = 134

define gui.textbox_xalign = 0.5
define gui.textbox_yalign = 0.99

define gui.textbox_padding = (27, 20)
define gui.textbox_round_radius = 20

define gui.text_color = "#ffffff"
define gui.text_size = 24

define gui.text_xalign = 0.5
define gui.text_yalign = 0.0

define gui.name_color = "#ffffff"
define gui.name_outlines_color = "#585858"
define gui.name_outlines_hover_color = "#b8b8b8"


define gui.namebox_width = 177
define gui.namebox_height = 54

define gui.namebox_xpos = 0.16
define gui.namebox_ypos = 0.806

define gui.namebox_padding = (35, 16, 35, 8)
define gui.namebox_tile = False

define gui.name_font = "gui/font/RifficFree-Bold.ttf"
define gui.name_text_size = 24
define gui.name_xalign = 0.5
define gui.name_yalign = 0.5


define gui.accent_color = "#ffffff"
define gui.accent_outlines_color = "#b59"
define gui.accent_outlines_hover_color = "#fac"


define gui.navigation_button_background = Transform(Solid("#fff"), alpha=0.4)
define gui.navigation_button_size = (243, 50)

define gui.navigation_button_text_font = "mod_assets/STUFF/bradhitc.ttf"
define gui.navigation_button_text_outlines = [(absolute(1), "#000", absolute(0), absolute(0))]
define gui.navigation_button_text_color = "#000"
define gui.navigation_button_text_size = 32
define gui.navigation_button_text_insensitive_color = "#333333"
define gui.navigation_button_text_xalign = 0.5
define gui.navigation_button_text_yalign = 0.5

define gui.shameless_button_size = 45
define gui.shameless_hbox_spacing = 6

define gui.interface_text_font = gui.default_font
define gui.interface_text_size = 24
define gui.interface_text_color = "#000000"
define gui.interface_text_outlines = [(absolute(1), "#000", absolute(0), absolute(0))]


define gui.hover_sound = "gui/sfx/hover.ogg"
define gui.activate_sound = "gui/sfx/select.ogg"
define gui.activate_sound_glitch = "gui/sfx/select_glitch.ogg"


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

define gui.quick_menu_save_align = (0.136, 0.868)
define gui.quick_menu_settings_align = (0.132, 0.966)
define gui.quick_menu_button_margin = (0, 0)
define gui.quick_menu_afm_pos = (0.853, 0.821)
define gui.quick_menu_afm_button_margin = (1, 1)
define gui.quick_menu_skip_pos = (0.853, 0.861)

define gui.notify_text_size = 16


define gui.slot_page_hbox_spacing = 8
define gui.slot_page_button_margin = (0, 0)
define gui.slot_page_button_text_size = 24

define gui.slot_drag_handle_height = 20
define gui.slot_xpadding = 15


define gui.phone_zoom = 0.8
define gui.phone_xsize = 389
define gui.phone_ysize = 803

define gui.phone_call_xpos = 0.07

define gui.phone_message_frame_padding = (8, 6, 8, 8)
define gui.phone_message_label_null_height = 4

init python hide:
    if renpy.variant(["small", "mobile"]):
        gui.textbox_height = 150

        gui.text_size = 25


        gui.namebox_ypos = 0.784

        gui.name_text_size = 25


        gui.shameless_button_size = 60
        gui.shameless_hbox_spacing = 9


        bar_margin = 4
        gui.bar_borders.left = bar_margin
        gui.bar_borders.top = bar_margin
        gui.bar_borders.right = bar_margin
        gui.bar_borders.bottom = bar_margin


        gui.quick_menu_save_align = (0.136, 0.852)
        gui.quick_menu_button_margin = (3, 3)
        gui.quick_menu_skip_align = (0.869, 0.842)
        gui.quick_menu_skip_button_margin = (5, 5)


        gui.notify_text_size = 20


        gui.slot_page_hbox_spacing = 10
        gui.slot_page_button_margin = (3, 3)
        gui.slot_page_button_text_size = 27

        gui.slot_drag_handle_height = 25


# not used but renpy is a sussy baka
define gui.button_width = None
define gui.button_height = 36
define gui.button_tile = False
define gui.button_borders = Borders(0, 0, 0, 0)

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc