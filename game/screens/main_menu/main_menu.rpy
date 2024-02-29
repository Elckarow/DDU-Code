screen main_menu_info():
    default show_info = False

    default urls = (
        (_("WEBSITE"), "https://dokidokiundercurrents.com/"), 
        (_("DISCORD"), "https://discord.com/invite/hbrc9FaAEZ"),
        (_("TWITTER"), "https://twitter.com/StudiouSilver"),
        (_("YOUTUBE"), "https://www.youtube.com/@StudioSilverS")
    )

    showif not show_info:
        button style "empty" xysize (27, 27) pos (0.01, 0.02):
            at transform:
                on appear:
                    alpha 1.0
                on show:
                    easein 0.4 alpha 1.0
                on hide:
                    easein 0.4 alpha 0.0
            
            action SetLocalVariable("show_info", True)

            circle border 1.5 color "#000"
            text "i" align (0.5, 0.5):
                style "project_text" yoffset 1
    
    else:
        frame style "empty" xysize (1.0, 1.0) modal True:
            at transform:
                on show:
                    alpha 0.0
                    easein 0.4 alpha 1.0
                on hide:
                    easein 0.4 alpha 0.0
            
            button style "empty" action SetLocalVariable("show_info", False) xysize (1.0, 1.0) activate_sound gui.activate_sound
            
            add "#000":
                at transform:
                    alpha 0.7
            
            frame style "empty" modal True:
                xysize (400, 1.0)

                add "#000":
                    at transform:
                        alpha 0.7
            
                vbox xsize 1.0 spacing 20:
                    for txt, url in urls:
                        button xysize (1.0, 55):
                            hover_background "#ffffffc5"

                            action OpenURL(url)

                            text txt style "undercurrents_text" align (0.5, 0.5) size 24
            
            text "v" + config.version.split()[-1]:
                style "undercurrents_text" align (0.0, 1.0) offset (3, -3) size 16

image pellets:
    "#D9D9D9"
    RoundedCorners(43)
    xysize (90, 229)
    alpha 0.0
    linear 5.0 alpha 6 / random.randint(12, 48)

screen crosshairs():
    default crosshair_color = Solid("#989898")

    fixed style "empty":
        at transform:
            subpixel True ysize 25 
            yalign 0.9 mesh True gl_drawable_resolution False
            block:
                xpan 0
                linear 70 xpan 360
                repeat

        add crosshair_color:
            xysize (1.0, 2) align (0.5, 0.5)

        hbox style "empty" spacing 30:
            for i in range(40):
                add crosshair_color xysize (2, 25)

image _main_menu_bg:
    contains:
        "mod_assets/STUFF/main_menu/main_menu_bg.png"
    contains:
        ConditionSwitch(
            "persistent.natsuki.completed", Transform("mod_assets/STUFF/main_menu/main_menu_bg_castle.png", pos=(308, 588)),
            "True", Null()
        )
    mesh True

screen main_menu_bg:
    modal True

    add "_main_menu_bg"
    
    dismiss action Hide("main_menu_bg", transition=Dissolve(0.4))

screen main_menu():
    tag menu
    add Solid("#F8F8F8")

    add SnowBlossom(
        d="pellets",
        border=229,
        xspeed=(0, 0),
        yspeed=(20, 100),
        start=5,
        fast=True,
        count=8
    )

    use crosshairs()

    default uhhhh_xpos = 0.29
    default uhhhh_ypos = 0.5

    circle radius 256 xycenter (uhhhh_xpos, uhhhh_ypos)

    button style "empty" xycenter (uhhhh_xpos, uhhhh_ypos) focus_mask True:
        at transform:
            on idle:
                easeout 0.25 matrixcolor BrightnessMatrix(0.0)
            on hover:
                easein  0.25 matrixcolor BrightnessMatrix(-0.2)

        add AlphaMask(
            Transform("mod_assets/STUFF/main_menu/main_menu_bg.png", ysize=300, fit="contain"),
            CircleDisplayable(align=(0.5, 0.5))
        )

        action Show("main_menu_bg", transition=Dissolve(0.4)) 
        
    circle radius 7 xycenter (uhhhh_xpos, uhhhh_ypos)

    circle:
        color "#fff" border 2 xysize (180, 180) xycenter (uhhhh_xpos, uhhhh_ypos)
        at transform:
            subpixel True zoom 0.8 alpha 0.0
            0.3
            easein_quart 0.5 zoom 1.0 alpha 1.0

    circle:
        color "#fff" border 2 xysize (30, 30) xycenter (uhhhh_xpos, uhhhh_ypos)
        at transform:
            subpixel True zoom 0.8 alpha 0.0
            0.4
            easein_quart 0.5 zoom 1.0 alpha 1.0

    add "mod_assets/STUFF/main_menu/triangle.png" xycenter (uhhhh_xpos, uhhhh_ypos - 0.035) xysize (20,15) yzoom -1 xoffset 1:
        at transform:
            subpixel True alpha 0.0 yoffset -10 matrixcolor InvertMatrix(1)
            0.5
            easein_quart 0.5 yoffset 0 alpha 1.0

    circle:
        color "#000" border 1.5 xysize (400, 400) xycenter (uhhhh_xpos, uhhhh_ypos)

    add Solid("#fff") xysize (158, 84) xycenter (uhhhh_xpos, uhhhh_ypos + 0.27)

    circle radius 5 color "#000":
        at transform:
            alignaround (0.29, 0.5) radius 0.2745
            angle 45 alpha 0.0
            0.7
            easein_quart 0.5 angle 50 alpha 1.0

    circle:
        color "#000" border 1.5 xysize (40, 40) anchor (0.5, 0.5)
        at transform:
            subpixel True
            alignaround (0.29, 0.5) radius 0.268 angle 48.7
            zoom 0.0 alpha 0.0
            0.8
            easein_quart 0.5 zoom 1.0 alpha 1.0

    for i in range(4):
        circle color "#000" xysize (10, 10):
            at transform:
                subpixel True anchor (0.5,0.5) around (0.41, 0.3235) radius 0.038
                parallel:
                    angle 90 * i
                    linear 3 angle (90 * i) + 360
                    repeat
                parallel:
                    alpha 0.0 radius 0.0
                    0.88
                    easein_quart 0.5 alpha 1.0 radius 0.038

    add "#fff" xysize (90, 128) xycenter (0.135, 0.5)
    text "01" style "version_num" xycenter (0.135, 0.5)

    text "N. 224" style "counting_down" xycenter (0.427, 0.5)
    add "mod_assets/STUFF/main_menu/number_holder.png" xycenter (0.135, 0.545)
    text "3.012" style "version_num" color "#fff" size 15 xycenter (0.1364, 0.546)
    text "5.122" style "version_num" size 15 xycenter (0.1364, 0.57)

    default stuff_radius = absolute(200 + (0.75 / 2))

    for angle in (-45, 135):
        add "#000":
            at transform:
                xysize (9, 68) 
                RoundedCorners(6)
                subpixel True anchor (0.5, 0.5) around (0.29, 0.5) radius absolute(stuff_radius + 6) alpha 0.0 matrixtransform RotateMatrix(0, 0, 135) angle angle
                0.5
                easein_quart 0.5 radius stuff_radius alpha 1.0

    add "mod_assets/STUFF/main_menu/cross.png" xycenter (0.12, 0.445)

    add Solid("#000", xysize=(12, 3)) anchor (0.0, 0.5) pos (0.133, 0.432) at unfurl
    add Solid("#000", xysize=(19, 3)) anchor (0.0, 0.5) pos (0.146, 0.432) at unfurl(0.3)

    add Solid("#000", xysize=(19, 3)) anchor (0.0, 0.5) pos (0.133, 0.442) at unfurl(0.35)
    add Solid("#000", xysize=(12, 3)) anchor (0.0, 0.5) pos (0.149, 0.442) at unfurl(0.45)

    add Solid("#000", xysize=(12, 3)) anchor (0.0, 0.5) pos (0.133, 0.452) at unfurl(0.33)

    for i in range(4):
        add "mod_assets/STUFF/main_menu/pill.png":
            at transform:
                subpixel True anchor (0.5, 0.5) around (0.29, 0.5) radius absolute(stuff_radius - 12) angle 163 + (i * 11) matrixtransform RotateMatrix(0, 0, 163 + (i * 11))

    for i in range(3):
        add "mod_assets/STUFF/main_menu/small_pill.png":
            at transform:
                subpixel True anchor (0.5, 0.5) around (0.29, 0.5) radius absolute(185) angle 205 + (i * 2) matrixtransform RotateMatrix(0, 0, 205 + (i * 2))
    
    use menu_nav()

    use main_menu_info()
    
    key "K_ESCAPE" action Quit(confirm=False)

transform unfurl(t=0):
    subpixel True xzoom 0.0
    t
    easein_quart 0.5 xzoom 1.0

style version_num is empty:
    font "mod_assets/STUFF/main_menu/Mukta-Regular.ttf"
    size 60
    color "#000"
    outlines []

style counting_down is empty:
    color "#000"
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf"
    size 11
    outlines []

screen menu_nav():
    default nav_entries = (
        (_("Launch"), ShowMenu("ch_select", _transition=config.enter_transition)),
        (_("Save States"), ShowMenu("load", _transition=config.enter_transition)),
        (_("Configuration"), ShowMenu("configuration", _transition=config.enter_transition)),
        (_("Resources"), ShowMenu("extras", _transition=config.enter_transition)),
        (_("Contributors"), ShowMenu("credits", _transition=config.enter_transition)),
        (_("Logout"), Quit(confirm=True)),
    )
    frame:
        background Solid("#fff")
        xysize (337, 712)
        align (0.8, 0.5)

        vbox:
            align (0.4, 0.5)
            text "PROJECT" style "project_text" xoffset 30

            frame:
                xoffset 30
                background "#000"
                xpadding 10 ypadding 10
                text "UNDERCURRENTS" style "undercurrents_text"

            null height 20

            for i, (nav_text, nav_action) in enumerate(nav_entries):
                button:
                    hover_background "nav_hovered"
                    xfill True
                    text nav_text style "nav_text" xoffset 40
                    action nav_action
                    ysize gui.main_menu_button_ysize 

define nav_triangle_xpos = (0.67 if not is_android() else 0.65)
define nav_triangle_spacing = (0.07 if not is_android() else 0.084)

image nav_hovered:
    contains:
        Solid("#D9D9D940")
    contains:
        "mod_assets/STUFF/main_menu/triangle.png"
        subpixel True fit "contain"
        xanchor 0.5 xpos nav_triangle_xpos + (nav_triangle_spacing * 0)
        alpha 0.08
        block:
            choice:
                linear 1.0 alpha 0.03
                random.randint(1, 3)
            choice:
                linear 1.0 alpha 0.12
                random.randint(1, 3)
            repeat
    contains:
        "mod_assets/STUFF/main_menu/triangle.png"
        subpixel True fit "contain"
        xanchor 0.5 xpos nav_triangle_xpos + (nav_triangle_spacing * 1)
        yzoom -1.0
        alpha 0.06
        block:
            choice:
                linear 1.0 alpha 0.01
                random.randint(1, 3)
            choice:
                linear 1.0 alpha 0.11
                random.randint(1, 3)
            repeat
    contains:
        "mod_assets/STUFF/main_menu/triangle.png"
        subpixel True fit "contain"
        xanchor 0.5 xpos nav_triangle_xpos + (nav_triangle_spacing * 2)
        alpha 0.15
        block:
            choice:
                linear 1.0 alpha 0.10
                renpy.random.randint(1, 3)
            choice:
                linear 1.0 alpha 0.20
                random.randint(1, 3)
            repeat
    contains:
        "mod_assets/STUFF/main_menu/triangle.png"
        subpixel True fit "contain"
        xanchor 0.5 xpos nav_triangle_xpos + (nav_triangle_spacing * 3)
        yzoom -1.0
        alpha 0.05
        block:
            choice:
                linear 1.0 alpha 0.0
                random.randint(1, 3)
            choice:
                linear 1.0 alpha 0.10
                random.randint(1, 3)
            repeat

style nav_text is empty:
    color "#000"
    size 22
    yalign 0.5
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Medium.ttf"
    outlines []

style project_text is empty:
    color "#000"
    outlines []
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf"
    size 13

style undercurrents_text is empty:
    color "#fff"
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf"
    size 26
    outlines []
    xalign 0.5

style under_text is empty:
    font "mod_assets/STUFF/main_menu/AdventPro-SemiBold.ttf"
    outlines []
    color "#121212"
    size 60
    line_leading 0 line_spacing 0

style under_light is empty:
    font "mod_assets/STUFF/main_menu/AdventPro-Light.ttf"
    outlines []
    color "#121212"
    size 30
    line_leading 0 line_spacing 0
