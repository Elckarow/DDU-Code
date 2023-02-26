transform extra_button:
    on idle:
        matrixcolor BrightnessMatrix(0.0)
    on hover:
        matrixcolor BrightnessMatrix(-0.1)

screen extras():
    tag menu

    default text = None
    $ text = GetTooltip()
    
    use game_menu(ExtraMenuInfo, menu_style="board"):
        style_prefix "extra"

        textbutton _("Characters") at extra_button:
            yalign 0.325
            action CharactersMenu()
            tooltip _("Learn more about the characters")

        textbutton _("Gallery") at extra_button:
            yalign 0.675
            action GalleryMenu()
            tooltip _("Revisit key moments of the story")
        
        frame:
            at (DropShadow(),
                Transform(
                    subpixel=True, transform_anchor=True,
                    anchor=(1.0, 0.0), pos=(0.95, 0.11),
                    rotate=-5
                )
            )
            showif text is not None:
                text "[text!t]"
        
        add Solid("#63452a"):
            at transform:   
                subpixel True transform_anchor True
                anchor (1.0, 0.0) pos (0.452, 0.149)
                xysize (80, 20) rotate -34
        
        add Solid("#63452a"):
            at transform:   
                subpixel True transform_anchor True
                pos (0.89, 0.04) rotate 20
                xysize (80, 20)


style extra_button:
    background Frame("mod_assets/STUFF/game_menu/game_menu_board_torn_paper.png")
    xysize (170, 39)
    xalign 0.1

style extra_button_text is board_text:
    align (0.07, 0.5)

style extra_text is board_text:
    align (0.0, 0.0)
    size 22

style extra_frame:
    padding (7, 7, 7, 4)
    background Frame("bg/poem.jpg")
    xysize (550, 360)