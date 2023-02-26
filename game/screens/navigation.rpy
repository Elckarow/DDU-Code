transform navigation_button:
    subpixel True
    on idle:
        easeout 0.27 matrixcolor BrightnessMatrix(0.0) xoffset 0
    on hover:
        easein 0.27 matrixcolor BrightnessMatrix(0.3) xoffset 25

transform shameless_button:
    subpixel True ysize gui.shameless_button_size
    fit "contain"

screen navigation():
    style_prefix "navigation"

    vbox:
        textbutton _("New Game") at navigation_button action Start()               
        textbutton _("Save Menu") at navigation_button action SaveMenu()
        textbutton _("Settings") at navigation_button action SettingsMenu()
        textbutton _("Extras") at navigation_button action ExtraMenu()
        textbutton _("Credits") at navigation_button action CreditsMenu()

        showif renpy.variant("pc"):
            textbutton _("Exit Game") at navigation_button action Quit(confirm=False)

    frame style_prefix "shameless":
        hbox:
            imagebutton:
                at shameless_button
                idle "mod_assets/STUFF/main_menu/about.png"
                action Dialogue(message=__("Demo 1.0.0"), ok_action=Hide("dialog"))
        
            imagebutton:
                at shameless_button
                idle "mod_assets/STUFF/main_menu/logo.png"
                action OpenURL("https://undercurrentsmod.weebly.com/")

            imagebutton:
                at shameless_button
                idle "mod_assets/STUFF/main_menu/discord_logo.png"
                action OpenURL("https://discord.com/invite/hbrc9FaAEZ")

            imagebutton:
                at shameless_button
                idle "mod_assets/STUFF/main_menu/twitter_logo.png"
                action OpenURL("https://twitter.com/StudiouSilver")
    
    nearrect:
        focus "tooltip"
        text "Demo 1.0.0"

style navigation_vbox:
    align (0.03, 0.923)
    spacing 20

style navigation_button:
    background gui.navigation_button_background
    activate_sound gui.activate_sound
    hover_sound gui.hover_sound
    xysize gui.navigation_button_size

style navigation_button_text:
    properties gui.text_properties("navigation_button")

style shameless_vbox:
    align (1.0, 1.0)

style shameless_button:
    keyboard_focus False

style shameless_frame:
    align (1.0, 1.0)
    background gui.navigation_button_background
    padding (7, 7)

style shameless_hbox:
    spacing gui.shameless_hbox_spacing
