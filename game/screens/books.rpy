screen desk():
    fixed at desk_arrive:
        add "mod_assets/STUFF/desk.png" at desk
        
        transclude

image chibi_monika 1 = "gui/poemgame/m_sticker_1.png"
image chibi_monika 2 = "gui/poemgame/m_sticker_2.png"

image chibi_sayori 1 = "gui/poemgame/s_sticker_1.png"
image chibi_sayori 2 = "gui/poemgame/s_sticker_2.png"

image chibi_natsuki 1 = "gui/poemgame/n_sticker_1.png"
image chibi_natsuki 2 = "gui/poemgame/n_sticker_2.png"

image chibi_yuri 1 = "gui/poemgame/y_sticker_1.png"
image chibi_yuri 2 = "gui/poemgame/y_sticker_2.png"

transform desk_arrive:
    on show:
        subpixel True ypos 1.0
        alpha 0.0 yanchor 0.0
        easein 1.3 alpha 1.0 yanchor 1.0

transform desk:
    subpixel True align (0.5, 1.0)
    zoom 1.45

transform desk_button:
    subpixel True align (0.5, 0.65)
    on idle:
        easeout 0.18 matrixcolor BrightnessMatrix(0.0) yoffset 0
    on hover:
        easein 0.18 matrixcolor BrightnessMatrix(0.15) yoffset -25

#############################################################################################################
#############################################################################################################
#############################################################################################################

screen route_choice(*choices):
    use desk():
        hbox:
            align (0.56, 0.84)
            spacing 40

            for who in choices:
                imagebutton at (desk_button, Transform(zoom=0.5, subpixel=True)):
                    idle BookButton(who, "idle")
                    hover BookButton(who, "hover")
                    action [Return(who), With(dissolve)]

init python:
    def BookButton(who, what, chibi=True):
        if not chibi:
            chibi = Null()
        
        else:
            d = {"idle": 1, "hover": 2}
            name = f"chibi_{who} {d[what]}"
            chibi = Transform(name, zoom=0.71, subpixel=True)

        PATH = "mod_assets/STUFF/books/%s.png"

        cc = getattr(persistent, who)
        if isinstance(cc, CharacterCompletion) and cc.completed:
            PATH %= "%s_completed"
        
            image = PATH % who
        
            # chibi and book combined
            book = Fixed(image, chibi, fit_first=True)
        
        else:
            book = PATH % who

        return book
    
    def route_choice(*choices):
        _window_hide()
        rv = renpy.call_screen("route_choice", *choices)
        store._window_auto = True
        return rv

define book_map = {
    "monika": _("{i}Confessions of a Mask{/i}"),
    "sayori": _("{i}Wuthering Heights{/i}"),
    "natsuki": _("{i}Oliver Twist{/i}"),
    "yuri": _("{i}The Black Cat{/i}")
}

default route = "sayori"
default book = book_map[route]

#############################################################################################################
#############################################################################################################
#############################################################################################################

screen guess(*choices, guess_text=_("{size=+5}Who wrote this poem?{/size}\nChoose wisely!")):
    style_prefix "guess"

    use desk():
        vbox:
            text "[guess_text!t]"

            hbox:
                for choice in choices:
                    imagebutton:
                        at desk_button

                        idle "chibi_%s 1" % choice
                        hover "chibi_%s 2" % choice
                        action [Return(choice), With(dissolve)]

style guess_text is default:
    align (0.5, 0.22)
    text_align 0.5

style guess_vbox:
    yfill True
    xalign 0.5

style guess_hbox:
    xsize 1000
    xfill True
    align (0.5, 0.84)

init python:
    def guess(*choices):
        _window_hide()
        rv = renpy.call_screen("guess", *choices)
        store._window_auto = True
        store._guessed = rv
    
    def guessed(who=None):
        if who is not None:
            return who == store._guessed
        return store.poem_last_author == store._guessed

default _guessed = False