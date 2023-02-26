define game_menu_transition = Dissolve(0.1)

default persistent.disable_afm_on_game_menu = True

screen game_menu(game_menu_info, menu_style):
    if menu_style == "computer":
        use game_menu_computer(game_menu_info):
            transclude

    elif menu_style == "book":
        use game_menu_book(game_menu_info):
            transclude
    
    elif menu_style == "board":
        use game_menu_board(game_menu_info):
            transclude
    
    else:
        add Solid("#000")
        text _("unknown menu style: [menu_style]") align (0.5, 0.5) text_align 0.5
        dismiss action MenuReturn()
    
    on "show" action If(_preferences.afm_enable and persistent.disable_afm_on_game_menu, true=Preference("auto-forward", "disable"))
    
###################################################

define BOOK_XOFFSET = 80

default persistent.tip_turn_page = False

screen game_menu_book(game_menu_info):
    default args = game_menu_info.args

    # why default these variables?
    # it makes the screen more stable and the scope is faster to be updated
    default screen = None
    default icon = None

    add "mod_assets/STUFF/game_menu/game_menu_board_wood.jpg"
    add "bg/poem.jpg":
        at transform:
            subpixel True
            anchor (1.0, 0.0) pos (0.01, 0.394)
            rotate -60 transform_anchor True
            xysize (500, 830)
    add "mod_assets/STUFF/game_menu/game_menu_book_book.png" at (DropShadow(), Transform(xoffset=BOOK_XOFFSET))

    fixed style "game_menu_book_fixed_button":
        vbox style "game_menu_book_vbox_button":
            for info in args:
                $ screen, icon = info.screen, info.icon

                showif info.condition:
                    showif renpy.get_screen(screen) is None:
                        imagebutton:
                            idle icon.idle
                            action info.get_action()
                
                    else:
                        imagebutton:
                            action NullAction()
                            idle icon.selected
                            sensitive False

        hbox style "game_menu_book_hbox_button_back":
            textbutton _("Return"):
                text_style "game_menu_book_button_text"
                action MenuReturn()

            showif not main_menu:
                textbutton _("Main Menu"):
                    text_style "game_menu_book_button_text"
                    action MainMenu(confirm=True)
        
    frame style "game_menu_book_frame_main":
        transclude
        
    key "K_UP" action game_menu_info.previous_screen()
    key "K_DOWN" action game_menu_info.next_screen()

    on "show" action If(not persistent.tip_turn_page, true=Show("dialog", game_menu_transition, message=__("Tip!\nYou can click the sides of the book\nto turn the page."), ok_action=(Hide("dialog"), SetField(persistent, "tip_turn_page", True))))
    on "replace" action If(not persistent.tip_turn_page, true=Show("dialog", game_menu_transition, message=__("Tip!\nYou can click the sides of the book\nto turn the page."), ok_action=(Hide("dialog"), SetField(persistent, "tip_turn_page", True))))

style game_menu_book_fixed_button:
    pos (0.001, 0.5)
    ysize 0.499

style game_menu_book_vbox_button:
    spacing 21

style game_menu_book_hbox_button_back:
    spacing 5
    yalign 1.0
    xanchor 1.0
    xpos 0.5

style game_menu_book_button_text is default:
    outlines []
    line_spacing 0
    color "#000"
    font "mod_assets/STUFF/Cavolini.ttf"

style game_menu_book_frame_main:
    align (0.5, 0.5)
    xysize (1080, 646)
    xoffset BOOK_XOFFSET

style game_menu_book_hbox_page:
    spacing 1

style game_menu_book_page_1:
    padding (68, 26, 30, 27)
    xsize 538

style game_menu_book_page_2:
    padding (27, 26, 50, 27)
    xsize 538

###################################################

define BOARD_FRAME_XYSIZE = (1100, 619)
define BOARD_FRAME_PADDING = (32, 27, 26, 21)

define BOARD_XOFFSET = 80

transform board_button:
    on idle:
        matrixcolor BrightnessMatrix(0.0)
    on hover:
        matrixcolor BrightnessMatrix(-0.2)

screen game_menu_board(game_menu_info):
    default args = game_menu_info.args

    default screen = None
    default icon = None

    add "mod_assets/STUFF/game_menu/game_menu_board_wood.jpg"
    add "mod_assets/STUFF/game_menu/game_menu_board_board.png" at (DropShadow(), Transform(xoffset=BOARD_XOFFSET))

    vbox style "game_menu_board_button_vbox":
        for info in args:
            $ screen, icon = info.screen, info.icon

            showif info.condition:
                showif renpy.get_screen(screen) is None:
                    imagebutton:
                        at board_button
                        style "game_menu_board_button"
                        idle icon.idle
                        action info.get_action()
                
                else:
                    imagebutton:
                        at transform:
                            matrixcolor BrightnessMatrix(-0.3)
                        style "game_menu_board_button"
                        action NullAction()
                        idle icon.selected
                        sensitive False
        
    vbox style "game_menu_board_button_vbox_back":
        textbutton _("Return"):
            at board_button
            style "game_menu_board_button"
            action MenuReturn()

        showif not main_menu:
            textbutton _("Main Menu"):
                at board_button
                style "game_menu_board_button"
                action MainMenu(confirm=True) 

    frame style "game_menu_board_frame_main":
        transclude
        
    key "K_UP" action game_menu_info.previous_screen()
    key "K_DOWN" action game_menu_info.next_screen()

style game_menu_board_button_vbox:
    ypos 0.05
    spacing 20

style game_menu_board_button_vbox_back is game_menu_board_button_vbox:
    ypos 0.95
    yanchor 1.0

style game_menu_board_button:
    background Frame(Transform("mod_assets/STUFF/game_menu/game_menu_board_paper.png", matrixcolor=TintMatrix("#c9c9c9")))
    xsize absolute((91 * 0.87) + BOARD_XOFFSET)
    padding (5, 8)

style game_menu_board_button_text is game_menu_book_button_text:
    align (0.5, 0.5)

style game_menu_board_frame_main:
    align (0.5, 0.5)
    xoffset BOARD_XOFFSET
    xysize BOARD_FRAME_XYSIZE
    padding BOARD_FRAME_PADDING 

###################################################

transform game_menu_computer_header_button:
    on idle:
        easeout 0.2 matrixcolor BrightnessMatrix(0.0)
    on hover:
        easein 0.2 matrixcolor BrightnessMatrix(0.1)

transform game_menu_computer_back_button:
    on idle:
        easeout 0.2 matrixcolor BrightnessMatrix(0.0)
    on hover:
        easein 0.2 matrixcolor BrightnessMatrix(-0.1)

define COMPUTER_BUTTON_ALPHA = 0.7
define COMPUTER_BUTTON_SELECTED_ALPHA = 0.51

screen game_menu_computer(game_menu_info):
    default args = game_menu_info.args
    default ms = game_menu_info.len

    default title = ""

    default screen = None
    default text = None
    default icon = None

    use main_menu_bg()

    fixed style "game_menu_computer_header_fixed":
        hbox style "game_menu_computer_select_screen_button_hbox":
            for i, info in enumerate(args):
                $ screen, text, icon = info.screen, info.text, info.icon

                showif info.condition:
                    # no `showif`
                    # because of the variable `title`
                    # slightly slower but hey
                    if renpy.get_screen(screen) is None:
                        imagebutton:
                            action info.get_action()
                            idle icon.idle
                            at game_menu_computer_header_button
                            style "game_menu_computer_select_screen_button%s" % ("_rounded" if i == ms else "")

                    else:
                        $ title = text
                        imagebutton:
                            action NullAction()
                            idle icon.selected
                            style "game_menu_computer_select_screen_button%s_selected" % ("_rounded" if i == ms else "")
                            sensitive False

        hbox style "game_menu_computer_back_button_hbox":
            imagebutton:
                idle icon_return.idle
                style "game_menu_computer_back_button_return"
                at game_menu_computer_back_button
                action MenuReturn()
                keysym "mouseup_3"

            imagebutton:
                idle icon_main_menu.idle
                style "game_menu_computer_back_button_main"

                if main_menu:
                    at transform:
                        matrixcolor BrightnessMatrix(-0.1)
                    action NullAction()
                    sensitive False
                else:
                    at game_menu_computer_back_button
                    action MainMenu(confirm=True)

        frame style "game_menu_computer_title_frame":
            text "[title!t]" style "game_menu_computer_title"

    frame style "game_menu_computer_outer_frame":
        frame style "game_menu_computer_screen_frame":
            transclude

    key "K_LEFT" action game_menu_info.previous_screen()
    key "K_RIGHT" action game_menu_info.next_screen()

    use computer_description()

style game_menu_computer_header_fixed:
    align (0.5, 0.0)
    ysize 50

style game_menu_computer_outer_frame:
    padding (19, 90, 19, 30)

style game_menu_computer_inner_vbox:
    spacing 0

style game_menu_computer_title_frame:
    background RoundedFrame(Transform(Solid("#fff"), alpha=COMPUTER_BUTTON_ALPHA), radius=(0, 0, 30, 0))
    top_padding 10
    bottom_padding 6
    align (1.0, 0.0)
    xsize 300
    yfill True
    xoffset 1

style game_menu_computer_title:
    align (0.5, 0.5)
    text_align 0.5
    font "mod_assets/STUFF/GothamRoundedLight.otf"
    color "#4e8ed1"
    outlines [(absolute(1), "#0472bf", absolute(0), absolute(0))]
    outline_scaling "step"
    size 34

style game_menu_computer_select_screen_button_hbox:
    align (0.0, 0.0)
    spacing 0

style game_menu_computer_select_screen_button:
    xysize (50, 50)
    background Transform(Solid("#fff"), alpha=0.7)
    ypadding 10
    keyboard_focus False

style game_menu_computer_select_screen_button_rounded is game_menu_computer_select_screen_button:
    background RoundedFrame(Transform(Solid("#fff"), alpha=COMPUTER_BUTTON_ALPHA), radius=(20, 0, 0, 0))

style game_menu_computer_select_screen_button_selected is game_menu_computer_select_screen_button:
    background Transform(Solid("#fff"), alpha=COMPUTER_BUTTON_SELECTED_ALPHA)

style game_menu_computer_select_screen_button_rounded_selected is game_menu_computer_select_screen_button:
    background RoundedFrame(Transform(Solid("#fff"), alpha=COMPUTER_BUTTON_SELECTED_ALPHA), radius=(20, 0, 0, 0))

style game_menu_computer_back_button_hbox:
    align (0.5, 0.0)

style game_menu_computer_back_button is game_menu_computer_select_screen_button:
    xsize 80

style game_menu_computer_back_button_return is game_menu_computer_back_button:
    background RoundedFrame(Transform(Solid("#fff"), alpha=COMPUTER_BUTTON_ALPHA), radius=(0, 0, 20, 0))

style game_menu_computer_back_button_main is game_menu_computer_back_button:
    background RoundedFrame(Transform(Solid("#fff"), alpha=COMPUTER_BUTTON_ALPHA), radius=(20, 0, 0, 0))

style game_menu_computer_screen_frame:
    background RoundedFrame(Transform(Solid("#fff"), alpha=COMPUTER_BUTTON_ALPHA), radius=30)
    padding (30, 20)
    xfill True
    yfill True
