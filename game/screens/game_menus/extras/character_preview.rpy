init python:
    class CharacterPreview(object):
        def __init__(self, name, text, d, character_settings):
            self._name = name
            self._text = text
            self._image = renpy.displayable(d)
            self.character_settings = character_settings
        
        @property
        def name(self):
            return self.character_settings.get_string(self._name)
    
        @property
        def text(self):
            return self.character_settings.get_string(self._text)
    
        @property
        def image(self):
            return self.character_settings.get_image(self._image)

    character_previews = (
    CharacterPreview("[persistent.mc_preview_name!ti]", _("""\
The main character of this story is Melody, an independent and rash young woman who, through some circumstances surrounding her childhood, grew up many years sooner than any child should.
As such, she has little patience for life at school and chooses to spend her time working, seeing the former as only a means to an end.

Now, with only six months left to her final year, Melody reaches ever closer towards her goal of graduating and escaping the judgmental eyes of those who would call her a child.
Sometimes, however, being older is not all that it seems..."""),
"_melody turned ec thinking mh noblink", melody_character_settings),

    CharacterPreview("[persistent.sayori_preview_name!it]", _("""\
Sayori is Melody’s long-time childhood friend. They drifted apart some time ago after an unfortunate misunderstanding occurred between the two.

Sayori is much like her usual self, bubbly and cheerful as ever, always being the one to mediate a group or argument.
But when worse comes to worst, there may be something frightening underneath her playful demeanour."""),
"_sayori turned lup rup mb noblink", sayori_character_settings),

    CharacterPreview("[persistent.natsuki_preview_name!ti]", _("""\
While Melody may have had Amelia during her high school years, Sayori had Natsuki.
The two grew quite close together over their senior school years, and at some point it seems Sayori convinced the girl to run for the Student Council, resulting in her holding the Vice-Presidency for their final year of school.

Natsuki is, as one might expect, a bit brash on the outside and reluctant to share her aspirations.
Not even to Sayori."""),
"_natsuki turned lhip noblink", natsuki_character_settings),

    CharacterPreview("[persistent.yuri_preview_name!ti]", _("""\
Yuri is very quiet and often keeps to herself, her only real friend being Monika.
One might mistake this for being shy, but the truth is always stranger than fiction.

Always seemingly troubled, Yuri avoids confrontations with others.
It could be said she has her own inner demons to face."""),
"_yuri shy mc noblink", yuri_character_settings),

    CharacterPreview("[persistent.monika_preview_name!ti]", _("""\
Monika, daughter of an illustrious law empire and born into unimaginable wealth, is an unbelievably popular girl around school, and as of recently, the founder of the recently re-opened Literature Club, the likes of which haven't been seen at the school for a decade.

Her departure from the Debate Dlub has left some scars on both sides, in turn creating friction between the girl and her former Vice-President.

With the tense atmosphere at home, however, opening a new club appears to be the least of her worries..."""),
Transform("_monika turned rhip noblink", yoffset=monika_yoffset_cem_babyrage), monika_character_settings),

    CharacterPreview("[persistent.aika_preview_name!it]", _("""\
Aika is the Debate club’s new leader, having taken the spot after Monika left to form her own club.

Sly and meticulous, her love for puzzles and mysteries make it seem like she knows more than she’s letting on."""),
"_aika smug noblink", aika_character_settings),

    CharacterPreview("[persistent.amelia_preview_name!it]", _("""\
Fiercely loyal but surprisingly closed off, she holds something of a past herself; something she would prefer to keep to herself even on the best of days. Unfortunately, she is rather inexperienced in comparison to her friend, a naïve streak which may become her undoing..."""),
"_amelia turned rup noblink", amelia_character_settings),

    CharacterPreview("[persistent.ellen_preview_name!ti]", _("""\
The gamer girl's younger sister, Ellen prides herself on this fact - It seems to be a large part of who she is, as the sister to Amelia.

She's fashionable and hip with her peers, and the lack of a true age gap between the two has lead to them being closer than most siblings might normally find themselves, on all but a single, key issue..."""),
"_ellen turned vest lup noblink", ellen_character_settings),

    CharacterPreview("[persistent.kaito_preview_name!it]", _("""\
Kaito is a weed, poking out from the grass wherever he's least expected and spreading his seeds to all who might play ball.

His natural habitat has him stringing along three or four partners at once, typically until they either catch wind of the others or until he grows bored of them, but the eyes he once had for two girls - the first he grew to seriously see as more than objects - still seem to linger in the back of his mind."""),
"_kaito turned lup bg noblink", kaito_character_settings),

    CharacterPreview(_("Boss"), _("""\
An almost timeless air to him, in Melody's eyes he seems to have not aged a day in the near two decades she's known him.

Having helped raise now two generations of both Nakamura and Katsuragi, the owner of the local café has a lifetime of mystery behind him, questions Melody's never had the stomach to ask, but he keeps an eye on her all the same."""),
Transform("_boss turned ed mc noapron noblink", crop=(0.1, 0.0, 1.0, 1.0)), boss_character_settings),
    )

default persistent.kaito_preview_name = _("Kaito")
default persistent.amelia_preview_name = _("Amelia")
default persistent.ellen_preview_name = _("Ellen")
default persistent.aika_preview_name = _("Aika")
default persistent.mc_preview_name = _("Melody")
default persistent.sayori_preview_name = _("Sayori")
default persistent.yuri_preview_name = _("Yuri")
default persistent.natsuki_preview_name = _("Natsuki")
default persistent.monika_preview_name = _("Monika")

screen character_preview():
    tag menu

    default trans = Dissolve(0.1)

    default m = len(character_previews) - 1
    default n = 0

    $ cp = character_previews[n]

    use game_menu(waves=False):
        style_prefix "character"

        hbox:
            null width 200                

            vbox yanchor 0.0 ypos 0.05 xsize 500:
                text cp.name style "character_name"
                text cp.text

            add cp.image:
                at transform:
                    subpixel True mesh True gl_drawable_resolution False
                    offset (-100, -42) zoom 0.75 

        vbox align (0.05, 0.95) spacing 5 xoffset 160.5:
            if is_android():
                at transform:
                    yoffset -5

            hbox spacing 5:
                for i in range(m + 1):
                    button action (SetScreenVariable("n", i), With(trans)) style "empty":
                        at transform:
                            xysize (50, 4) nearest True
                            on idle:
                                alpha (1.0 if n == i else 0.3)
                            on hover:
                                alpha 1.0

                        add "#636363"

            hbox spacing 5:
                add Solid("#636363", xysize=(5, 5), yalign=0.5)
                text (str(n + 1).zfill(2) + "/" + str(m + 1).zfill(2)) yalign 1.0
                add Solid("#636363", xysize=(5, 5), yalign=0.5)

                null width 100

            hbox spacing 5:
                if is_android():
                    at transform:
                        zoom 1.2

                button:
                    add Transform("mod_assets/STUFF/main_menu/triangle.png", matrixtransform=Matrix.rotate(0, 0, 270), matrixcolor=BrightnessMatrix(1), align=(0.5,0.5), zoom=0.4, fit="contain")
                    action (SetScreenVariable("n", (n - 1 if n != 0 else m)), With(trans))
                    style "ch_prev_iter_button"

                button:
                    add Transform("mod_assets/STUFF/main_menu/triangle.png", matrixtransform=Matrix.rotate(0, 0, 90), matrixcolor=BrightnessMatrix(1), align=(0.5,0.5), zoom=0.4, fit="contain")
                    action (SetScreenVariable("n", (n + 1 if n != m else 0)), With(trans))
                    style "ch_prev_iter_button"
        
style ch_prev_iter_button:
    yalign 0.5
    background "#000"
    hover_background "#636363"
    xysize (30, 30)

style character_outer_frame is empty:
    background Solid("#fff")
    padding (21, 21)

style character_inner_frame is empty

style character_text is credit_text:
    align (0.0, 0.0)
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
    size 20
    color "#5a5a5a"
    text_align 0.0

style character_name is cast_name:
    xalign 0.0
    size 60
    color "#636363"
    text_align 0.0