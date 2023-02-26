screen main_menu_bg():
    add "mod_assets/STUFF/main_menu/main_menu_bg.png"

    showif persistent.natsuki.completed:
        add "mod_assets/STUFF/main_menu/main_menu_bg_castle.png":
            pos (308, 588)

screen mm_bg():
    modal True

    dismiss action Hide("mm_bg", dissolve) #keysym ["K_SPACE", "K_ESCAPE"]
    use main_menu_bg()

    key ["K_SPACE", "K_ESCAPE"] action Hide("mm_bg", dissolve)

screen main_menu():
    tag menu

    use main_menu_bg()

    add "mod_assets/STUFF/main_menu/logo.png":
        at transform:
            xsize 211 fit "contain" subpixel True
            xanchor 0.5 xpos 0.12 yanchor 0.0 ypos 0.02

    use navigation()

    key "K_ESCAPE" action Quit(confirm=False)
    key "mouseup_3" action Show("mm_bg", dissolve)