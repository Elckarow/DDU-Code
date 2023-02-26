init python:
    class CharacterPreview(object):
        def __init__(self, name, text, d, background="bg club_day", **kwargs):
            self.name = name
            self.text = text

            self.background = Transform(background, crop=(absolute((config.screen_width / 2) - config.screen_height / 2), 0, config.screen_height, config.screen_height))

            kwargs.setdefault("fit", "contain")
            kwargs.setdefault("xalign", 0.5)
            self.image = Transform(d, **kwargs)
            
    character_previews = (
    CharacterPreview(_("Melody"), _("""\
The main character of this story is Melody, an independent and rash young woman who, through some circumstances surrounding her childhood, grew up many years sooner than any child should. As such, she has little patience for life at school and chooses to spend her time working, seeing the former as only a means to an end.

Now, with only six months left to her final year, Melody reaches ever closer towards her goal of graduating and escaping the judgmental eyes of those who would call her a child. Sometimes, however, being older is not all that it seems...

As mentioned previously, Melody is the main character, and as such, the voice from which you will experience the world of Undercurrents. She is strong-willed and will often throw her own weight around when she feels it necessary.

She may be wise for her age, but be wary of the amount of emotion she may throw into her decisions."""), Fixed(Transform(Placeholder(base="girl", text=_("coming soon")), align=(0.5, 1.0), fit="contain"), xysize=(960, 960))
),

    CharacterPreview(_("Sayori"), _("""\
Sayori is Melody’s long-time childhood friend. They drifted apart some time ago after an unfortunate misunderstanding occurred between the two.

Sayori is much like her usual self, bubbly and cheerful as ever, always being the one to mediate a group or argument.

But when worse comes to worst, there may be something frightening underneath her playful demeanour."""),
"mod_assets/STUFF/game_menu/character_previews/character_preview_sayori.png"),

    CharacterPreview(_("Natsuki"), _("""\
While Melody may have had Amelia during her high school years, Sayori had Natsuki.
The two grew quite close together.

Natsuki is, as one might expect, a bit brash on the outside and reluctant to share her aspirations.

Why would she stay this closed off from those around her? Perhaps she holds a dark secret, one that no one else can possibly know about, not even Sayori."""),
"mod_assets/STUFF/game_menu/character_previews/character_preview_natsuki.png"),

    CharacterPreview(_("Yuri"), _("""\
Yuri is very quiet and often keeps to herself, her only real friend being Monika. She both reads and practices exquisite language.
One might mistake this for being shy, but the truth is always stranger than fiction.

Always seemingly troubled, Yuri avoids confrontations with others. It could be said she has her own inner demons to face.

Is this truly the case, or is her demon more real than meets the eye?"""),
"mod_assets/STUFF/game_menu/character_previews/character_preview_yuri.png"),

    CharacterPreview(_("Monika"), _("""\
Monika is a fairly popular girl in her school, and as of recently, the founder of the new Literature club. Her departure from the Debate club has left some scorn from their members, as well as guilt to be carried by herself.

However, just running a new club isn’t Monika’s only concern. Back at home, one could say she isn’t having a pleasant conversation with anyone there.

How might she deal with these issues and further?"""),
"mod_assets/STUFF/game_menu/character_previews/character_preview_monika.png"),

    CharacterPreview(_("Aika"), _("""\
Aika is the Debate club’s new leader, having taken the spot after Monika left to form her own club.

While running the Debate club has been quite the undertaking, given its size and how much of a role it plays in the school, Aika has been managing it well with the help of her newly elected vice president.

Aika is both casual and flirty, but not afraid to be serious when the situation calls for it. With a passion for learning new things, especially music, Aika can be quite busy.

Sly and meticulous, her love for puzzles and mysteries make it seem like she knows more than she’s letting on."""),
"mod_assets/STUFF/game_menu/character_previews/character_preview_aika.png"),

    CharacterPreview(_("Amelia"), _("""\
Amelia is Melody’s best friend, although this isn’t very telling. They’ve known each other since the start of high school and work together surprisingly well.

They do not share any classes this year, so they have not been able to talk as often as they normally would, but the bond connecting them is still far stronger than Melody would care to admit.

Amelia has a keen sense of perception and a more loose moral compass, which often puts her on the other side of her best friend’s coin.

Fiercely loyal but surprisingly closed off, she holds something of a past herself; something she would prefer to keep to herself even on the best of days. Unfortunately, she is rather inexperienced in comparison to her friend, a naïve streak which may become her undoing..."""),
"mod_assets/STUFF/game_menu/character_previews/character_preview_amelia.png")
    )

screen character_preview():
    tag menu

    default m = len(character_previews) - 1
    default n = 0

    $ cp = character_previews[n]

    use game_menu(CharactersMenuInfo, menu_style="book"):
        style_prefix "character"
        
        hbox:
            frame style "character_page_1" at Flatten:
                frame style "character_outer_frame":
                    at (DropShadow(), Transform(fit="contain"))

                    frame style "character_inner_frame":
                        background Frame(cp.background)
                        add cp.image

            frame style "character_page_2":
                vbox:
                    text "[cp.name!t]" style "character_name"

                    viewport:
                        draggable True
                        mousewheel True

                        text "[cp.text!t]"
    
        use book_turn_page(
            [
                SetLocalVariable("n", (n - 1 if n != 0 else m)),
                With(game_menu_transition)
            ],
            [
                SetLocalVariable("n", (n + 1 if n != m else 0)), 
                With(game_menu_transition)
            ]
        )

style character_page_1 is game_menu_book_page_1:
    padding (68, 26, 18, 37)
    yalign 0.45

style character_page_2 is game_menu_book_page_2

style character_outer_frame is empty:
    background Solid("#fff")
    padding (21, 21)

style character_inner_frame is empty

style character_hbox is game_menu_book_hbox_page

style character_text is book_text
style character_name is book_title

style character_vbox is book_title_vbox
