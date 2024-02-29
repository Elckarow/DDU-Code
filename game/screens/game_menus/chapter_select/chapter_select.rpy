# this shit
# is a complete mess

init python:
    def do_shit_for_the_common_route(branch):
        branches.set_current(branch)
        book = branches.to_book(branch)

        for i, desc in enumerate(calendar_descriptions[None]):
            add_calendar_description(desc, day=23 + i)
        
        phone.discussion.register_date("mc_m", *([True] * 6))
        phone.discussion.register_message("mc_m", "m", "I'm on my way~")

label start_sayori:
    call start_actI_branch(branches.FEELINGS) from _call_start_actI_branch

label start_yuri:
    call start_actI_branch(branches.FATE) from _call_start_actI_branch_1

label start_monika:
    call start_actI_branch(branches.SNARED) from _call_start_actI_branch_2

label start_natsuki:
    call start_actI_branch(branches.BLOOD) from _call_start_actI_branch_3

label start_actI_branch(branch):
    call set_vars_actI from _call_set_vars_actI
    $ do_shit_for_the_common_route(branch)

    jump actI

# TODO
# kinda sucks
# TODO²
# my fucking head hurts
init python:
    class ChapterSelectCard(object):
        def __init__(self, name, chapters, d, descriptions, cgs=(), endings=((),)):
            self.name = name
            self.chapters = chapters
            self.d = renpy.displayable(d)
            self.descriptions = descriptions
            self.cgs = [renpy.python.py_compile(cg, mode="eval") for cg in cgs]

            if len(endings) != len(chapters): raise Exception("breh")
            if len(endings) != len(descriptions) - 1: raise Exception("breh²")

            self.endings = [
                [renpy.python.py_compile(ending, mode="eval") for ending in _endings]
                for _endings in endings
            ]

        @staticmethod
        def get_unlocked(l, _all=True):
            rv = 0
            for thing in l:
                if isinstance(thing, (list, tuple)):
                    rv += (all if _all else any)(renpy.python.py_eval_bytecode(t) for t in thing)
                else:
                    rv += bool(renpy.python.py_eval_bytecode(thing))
            return rv

    chapter_select_cards = (
        ChapterSelectCard(
            _("A Series of Unfortunate Events"),
            [
                #   name                   label_name
                (_("Feelings Rekindled"), "start_sayori"),
                (_("The Heart Beats with Blood"), "start_natsuki"),
                (_("Snared by the Flytrap"), "start_monika"),
                (_("Challenging Fate"), "start_yuri")
            ],
            Transform("_melody turned best noblink", crop=character_crops["melody turned"]),
            # descriptions
            # 1st one is the act
            # rest is for the branches
            [
                _("""\
            As the girls scramble to find themselves amidst a turbulent sea of troubles, more and more evident does it become that they are less in command than they'd like. What had began as a battle to discover themselves putrefies into a war to simply stay alive, let alone on their feet.
            
            All the while, a lone pair of eyes watches them, waiting for the right moment to make their move."""),
                _("\
                Feelings of forlonging plague her heart; times long gone and words not spent. To great heights she goes, affections unmeant."),
                _("\
                A life twisted and upturned, she'll learn her view of the world is unheard. Her view, bleaker with every beat."),
                _("\
                In time's bind, masks blind. All parties equally ensnared, judgements are intrinsically impaired. "),
                _("\
                The pen blots, the black ink clots. The seamstress halts her weaving, destiny no longer conceiving. The true author begins their work.")
            ],
            [
                "persistent.amelia.cgs[0]",

                "persistent.mc.cgs[0]",
                "persistent.mc.cgs[1]",

                "persistent.sayori.cgs[0]",
                "persistent.sayori.cgs[1]",
                "persistent.sayori.cgs[2]",

                "persistent.natsuki.cgs[0]",
                "persistent.natsuki.cgs[1]",

                "persistent.monika.cgs[0]",

                "persistent.yuri.cgs[0]",
                "persistent.yuri.cgs[1]",
            ],
            [
                ["persistent.sayori.endings[0]"],
                ["persistent.natsuki.endings[0]"],
                ["persistent.monika.endings[0]"],
                ["persistent.yuri.endings[0]"]
            ]
        ),
    )

    # lasagna
    # but idk. it works fine so :fridge:
    class ActObjectBecauseRenpyAUUUUGH(object):
        def __init__(self):
            self.act_selected = None
            self.branch_selected = None

style act_number_text is display_text:
    size 16
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"

screen ch_select():
    tag menu

    default num_cards = len(chapter_select_cards)
    default act_object = ActObjectBecauseRenpyAUUUUGH()

    default phase = True

    use game_menu():
        gradient "#00000020" "#fff0" theta 270 xoffset -650:
            at transform:
                alpha 0.0
                easein_quart 0.4 alpha 1.0

        frame style "empty" at Flatten:
            at transform:
                easein_quint 0.4:
                    zoom (1.0 if phase else 0.8)
                    yoffset (0 if phase else -50)
                    alpha (1.0 if phase else 0.2)

            background None xysize (491, 491) anchor (0.5, 0.5) pos (0.7, 0.5)

            use decorations()

        vbox spacing 5:
            at transform:
                subpixel True xsize 400
                yalign 0.5 xalign 0.02
                xoffset -40 alpha 0.0
                easein_quart 0.4 xoffset 0 alpha 1.0

            for i, card in enumerate(chapter_select_cards):
                vbox style "empty" spacing 5:
                    button:
                        at transform:
                            subpixel True
                            on hover:
                                easein_quart 0.4 alpha 0.9
                            on idle:
                                easein_quart 0.4 alpha 0.6
                            on selected_idle:
                                easein_quart 0.4 alpha 1.0

                        add card.d:
                            at transform:
                                subpixel True xcenter 0.7
                                alpha 0.3 fit "contain" mesh True gl_drawable_resolution False
                                matrixcolor TintMatrix("#000")

                        xysize (1.0, 125) background Solid("#fdfdfd")

                        action [
                            If(act_object.act_selected != i,
                                true=(Show("branch_info", card=card, act_object=act_object), SetField(act_object, "act_selected", i)),
                                false=(Hide("branch_info"), SetField(act_object, "act_selected", None))
                            ),
                            If(act_object.act_selected != i,
                                true=(SetScreenVariable("phase", False)),
                                false=(SetScreenVariable("phase", True))
                            ),
                            SelectedIf(act_object.act_selected == i),
                            SetField(act_object, "branch_selected", None)
                        ]

                        hbox yanchor 0.5 pos (0.05, 0.85) spacing 10:
                            style_prefix "act_number"
                            text (str(i + 1).zfill((num_cards // 10) + 2) + ": ") color "#909090"
                            text card.name.upper()

                    showif act_object.act_selected == i:
                        frame at Flatten:
                            background Transform("#D9D9D9", alpha = 0.35)
                            xfill True
                            ysize 200

                            at transform:
                                subpixel True
                                on show:
                                    crop (0.0, 0.0, 1.0, 0.0)
                                    easein_quart 0.5 crop (0.0, 0.0, 1.0, 1.0)
                                on hide:
                                    easein_quart 0.5 crop (0.0, 0.0, 1.0, 0.0)

                            vbox yalign 0.5 spacing 5:
                                for b, (chapter, _label) in enumerate(card.chapters):
                                    $ unlocked = card.get_unlocked(card.endings[b], False)
                                    button:
                                        at transform:
                                            subpixel True
                                            on idle:
                                                easein 0.5 alpha 0.7 xoffset 0
                                            on hover, selected_idle, selected_hover:
                                                easein_quint 0.5 alpha 1.0 xoffset 3

                                        xfill True
                                        background At("#c9c9c9", RoundedCorners(13))
                                        hover_background "chapter_hovered"
                                        selected_background "chapter_hovered"
                                        left_margin 10 right_margin 10

                                        if unlocked:
                                            action [
                                                If(act_object.branch_selected != b,
                                                    true=SetField(act_object, "branch_selected", b),
                                                    false=SetField(act_object, "branch_selected", None)
                                                ),
                                                SelectedIf(act_object.branch_selected == b),
                                            ]
                                        else:
                                            action SetField(act_object, "branch_selected", None)
                                            selected False

                                        text (chapter if unlocked else "???") style "under_light":
                                            color "#121212"
                                            font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Medium.ttf"
                                            #font "mod_assets/STUFF/main_menu/AdventPro-Medium.ttf"
                                            size 16 anchor(0.0, 0.5) pos (0.1, 0.5)

                                        frame:
                                            at transform:
                                                subpixel True xysize (21, 21)
                                                anchor (0.5, 0.5) pos (0.05, 0.5)

                                            padding (3, 3) background CircleDisplayable(1, color="#000")
                                            circle color "#000" border 1

    on "replaced" action Hide("branch_info")

style branch_info_button:
    hover_background Solid("#414141")
    background Solid("#41414190")
    insensitive_background Solid("#79797980")
    xysize (194, 36)

style branch_info_button_text is load_option:
    size 18

screen branch_info(card, act_object):
    use asoue_nodes(card, act_object)

    add "#000":
        at transform:
            xycenter (0.66, 0.82) xsize 800 ysize absolute(1.5)
            FadingBorders((100, 0, 100, 0))

            on show:
                alpha 0 xzoom 0.0
                easein_quart 0.4 alpha 1.0 xzoom 1.0
            on hide:
                ease 0.4 alpha 0.0 xzoom 0.0

    hbox at drop_reveal style_prefix "branch_info":
        spacing 5
        align (0.975, 0.79)

        textbutton _("NEW TAKE"):
            action Start()
        
        textbutton _("LOAD BRANCH"):
            if act_object.branch_selected is not None and card.get_unlocked(card.endings[act_object.branch_selected], False):
                action Start(chapter_select_cards[act_object.act_selected].chapters[act_object.branch_selected][1])

    frame at Flatten:
        align (0.93, 0.94) xysize (800, 100)

        at transform:
            subpixel True
            on show:
                alpha 0 yoffset 5
                easein_quart 0.4 alpha 1.0 yoffset 0
            on hide:
                ease 0.4 alpha 0.0 yoffset 5

        hbox align (0.5, 0.5) spacing 35:
            add "#000":
                at transform:
                    yalign 0.5 ysize 60 xsize absolute(1.5)
                    FadingBorders((0, 15, 0, 15))

            text __("BRANCHES COMPLETED: ") + (
                str(card.get_unlocked(card.endings))
                + "/"
                + str(len(card.endings))
            ) align (0.5, 0.5) style "route_desc"

            add "#000":
                at transform:
                    yalign 0.5 ysize 60 xsize absolute(1.5)
                    FadingBorders((0, 15, 0, 15))

            text __("CGs SEEN: ") + (
                str(card.get_unlocked(card.cgs))
                + "/"
                + str(len(card.cgs))
            ) align (0.5, 0.5) style "route_desc"

            add "#000":
                at transform:
                    yalign 0.5 ysize 60 xsize absolute(1.5)
                    FadingBorders((0, 15, 0, 15))

            text __("ENDINGS REACHED: ") + (
                str(card.get_unlocked(card.endings, False))
                + "/"
                + str(sum(len(endings) for endings in card.endings))
            ) align (0.5, 0.5) style "route_desc"

            add "#000":
                at transform:
                    yalign 0.5 ysize 60 xsize absolute(1.5)
                    FadingBorders((0, 15, 0, 15))

style route_desc:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
    outlines []
    color "#121212"
    size 16
    line_leading 0 line_spacing 0

define chapter_hovered_triangle_xpos = 0.67
define chapter_hovered_triangle_spacing = 0.07

image chapter_hovered:
    contains:
        At("#b5b5b5", RoundedCorners(13))
    contains:
        "mod_assets/STUFF/main_menu/triangle.png"
        subpixel True fit "contain"
        matrixcolor BrightnessMatrix(1.0)
        alpha 0.08 xanchor 0.5 xpos chapter_hovered_triangle_xpos + (chapter_hovered_triangle_spacing * 0)
    contains:
        "mod_assets/STUFF/main_menu/triangle.png"
        subpixel True fit "contain"
        matrixcolor BrightnessMatrix(1.0)
        alpha 0.06 xanchor 0.5 xpos chapter_hovered_triangle_xpos + (chapter_hovered_triangle_spacing * 1)
        yzoom -1.0
    contains:
        "mod_assets/STUFF/main_menu/triangle.png"
        subpixel True fit "contain"
        matrixcolor BrightnessMatrix(1.0)
        alpha 0.15 xanchor 0.5 xpos chapter_hovered_triangle_xpos + (chapter_hovered_triangle_spacing * 2)
    contains:
        "mod_assets/STUFF/main_menu/triangle.png"
        subpixel True fit "contain"
        matrixcolor BrightnessMatrix(1.0)
        alpha 0.12 xanchor 0.5 xpos chapter_hovered_triangle_xpos + (chapter_hovered_triangle_spacing * 3)
        yzoom -1.0

transform radial_zoom(d=0):
    subpixel True
    zoom 0.8 alpha 0.0
    d
    easein_quart 0.4 zoom 1.0 alpha 1.0

screen decorations():
    circle radius 245

    circle color "#000" radius 7 align (0.5, 0.5)
    circle color "#000" radius 14 border 2 align (0.5, 0.5) at radial_zoom(0.1)
    circle color "#000" radius 82 border 3 align (0.5, 0.5) at radial_zoom(0.2)
    circle color "#000" radius 200 border 2 align (0.5, 0.5) at radial_zoom(0.3)

    add "#000":
        at transform:
            RoundedCorners(6)
            xysize (9, 68) 
            subpixel True anchor (0.5, 0.5) around (0.5, 0.5) radius absolute(200 + 0.75 / 2) alpha 0.0 matrixtransform RotateMatrix(0, 0, 135) angle 330
            0.5
            easein_quart 0.5 radius absolute(200 + 0.75 / 2) alpha 1.0 angle 315
    
    add "#000":
        at transform:
            RoundedCorners(6)
            xysize (9, 68) 
            subpixel True anchor (0.5, 0.5) around (0.5, 0.5) radius absolute(200 + 0.75 / 2) matrixtransform RotateMatrix(0, 0, 135) angle 150 alpha 0.0
            0.5
            easein_quart 0.5 radius absolute(200 + 0.75 / 2) alpha 1.0 angle 135

    add "mod_assets/STUFF/main_menu/triangle.png" xysize (20,15) yzoom -1 align (0.5, 0.45):
        at transform:
            subpixel True alpha 0.0 yoffset -10
            0.5
            easein_quart 0.5 yoffset 0 alpha 1.0

    circle color "#000" radius 105 length 0.25 border 2.1 align (0.5, 0.5):
        at transform:
            subpixel True 
            parallel:
                zoom 0.5 alpha 0.0
                easein_quart 0.5 zoom 1.0 alpha 1.0
            parallel:
                rotate 0
                linear 15 rotate 360
                repeat

    circle color "#000" radius 98 length 0.25 border 2.1 align (0.5, 0.5):
        at transform:
            subpixel True 
            parallel:
                zoom 0.5 alpha 0.0
                easein_quart 0.5 zoom 1.0 alpha 1.0
            parallel:
                rotate 90
                linear 17.5 rotate 450
                repeat

    circle color "#000" radius 90 length 0.25 border 2.1 align (0.5, 0.5):
        at transform:
            subpixel True 
            parallel:
                zoom 0.5 alpha 0.0
                easein_quart 0.5 zoom 1.0 alpha 1.0
            parallel:
                rotate 20
                linear 20 rotate 380
                repeat
