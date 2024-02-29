init python:
    class TeamCredit(object):
        def __init__(self, name, title, desc=None):
            self.name = name
            self.title = title
            self.desc = desc or title

    credits_list = [
        TeamCredit(*stuff)
        for stuff in (
            ("Tiffany", _("Project Director"), _("The project’s lead for the longest time, helping direct everything and making sure everyone contributed. He’s also one of the main writers, having written a solid million words of the script, as well as a VA for one of the characters (can you guess who?)")),
            ("Staticquit", _("Art Director"), _("Static for short, is the team's art director, contributing both CGs and sprites to the project, as well as lightening the mood for everyone around him and dedicating endless hours to ensuring consistency across our team.")),
            ("Pivot", _("Deputy Director"), _("Full name 'Pivot Whiteground Lever', is the team's proofreader and project organiser. She helps keep things up to date and readily accessible, but she's also contributed with writing/editing and voice acting, among other trades.")),
            ("Kasumi Sato", _("Music Lead"), _("Sumi for short, is the team's lead musician, as well as a prominent writer. He's helped set the theme for this project, as well as maintain quality assurance.")),
            ("Arcannite", _("Art Supervisor"), _("Lovingly referred to as Arcy, is the team's concept artist. While he may be a little snarky, he's helped with not just art, but also writing and coding.")),
            ("Elckarow", _("Code Lead"), _("The team's lead coder, the one who brought the project to life in mod form. He's coded the majority of this project and has worked on the UI alongside -2.")),
            ("Sekhmet D", _("Project Founder and Writer")),
            ("Beatrice", _("Project Founder and Writer")),
            ("-2", _("UI Designer")),
            ("cemsthetic", _("Coder")),
            ("DatBlackScientist", _("Website Designer")),
            ("Slayer Rabbit", _("Writer")),
            ("Victoria Valentine", _("Writer")),
            ("F i T", _("Promotional Artist, Playtester, Artist, Writer")),
            ("Ichigo_soap", _("Promotional Artist")),
            ("Gordon_Rammstein", _("Sprite Artist")),
            ("Raezoo", _("CG Artist")),
            ("Errizz", _("CG Artist")),
            ("Stormblaze", _("CG and Sprite Artist")),
            ("Hanasaki Yunarin", _("CG and Sprite Artist")),
            ("Kutabare", _("CG and Sprite Artist")),
            ("Amish_anime", _("BG Artist")),
            ("AkuVT", _("Voice Actor")),
            ("Gidget", _("Writer and Voice Actor")),
            ("Stewmiester", _("Writer and Voice Actor")),
            ("Soggyusagi", _("Voice Actor")),
            ("Firearts", _("Voice Actor")),
            ("Alice Gaming", _("Music Composer")),
            ("Two Colours", _("Music Composer and Arranger")),
            ("MC.Dummy.Composer", _("Music Arranger")),
            ("Inksaw114", _("Playtester")),
            ("SomeDudeNamedAyat", _("Playtester"))
        )
    ]

define main_cols = 3
define main_rows = 2

screen credits():
    tag menu
    default spotlight = credits_list[0]

    use game_menu():
        frame style "empty" xalign 0.98:
            hbox:
                viewport:
                    id "credits_vp"
                    draggable True
                    mousewheel True
                    xfill False

                    vbox spacing 10:
                        null height 20

                        grid main_cols main_rows spacing 10:
                            for i, main_member in enumerate(credits_list[:main_cols * main_rows]):
                                use credit_member(main_member, i, True)

                        for j, member in enumerate(credits_list[main_cols * main_rows:]):
                            use credit_member(member, j, False)
                                
                        null height 10

                null width 10

                vbar value YScrollValue("credits_vp") at Transform(xzoom=0.5)

        use cast_spotlight(spotlight)

screen credit_member(member, i, main):
    button:
        at transform:
            subpixel True 
            xoffset 5 alpha 0.0
            (((main_cols * main_rows) if main else len(credits_list)) - i) * (0.08 if main else 0.03)
            easein_quart 0.5 xoffset 0 alpha 1.0

            on idle:
                ease 0.2 matrixcolor BrightnessMatrix(0.0) yoffset 0
            on hover:
                ease 0.2 matrixcolor BrightnessMatrix(-0.1) yoffset -4
    
        xysize ((220, 210) if main else (680, 42))
        background "#D9D9D980"
        selected_background "#D9D9D9"
        action SelectedIf(SetScreenVariable("spotlight", member))
        
        if main:
            vbox style "empty" align (0.5, 0.5):
                text member.name style "cast_name"
                text member.title style "cast_name" font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf" size 18

        else:
            xpadding 10

            text member.name style "credit_text"
            text member.title xalign 1.0 style "credit_text" font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
        
screen cast_spotlight(spotlight):
    frame:
        at transform:
            subpixel True
            xoffset -30 alpha 0.0
            easein_quart 0.4 xoffset 0 alpha 1.0

        padding (20, 20)
        xycenter (0.225, 0.5)
        xysize (475, 600)

        vbox:
            text spotlight.name style "cast_name" align (0.0, 0.0)
            text spotlight.title style "cast_name" align (0.0, 0.0) font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf" size 20
            
            add Solid("#000", ysize=1):
                at transform:
                    subpixel True
                    alpha 0.0 xsize 0.01
                    0.3
                    easein_quart 0.5 alpha 1.0 xsize 1.0

            null height 10

            text spotlight.desc style "cast_name" align (0.0, 0.0) font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf" size 20 color "#5a5a5a" text_align 0.0

style cast_name:
    align (0.5, 0.5)
    text_align 0.5
    color "#000"
    outlines[]
    size 32
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf"

style credit_text:
    yalign 0.5
    text_align 0.5
    color "#000"
    outlines[]
    size 18
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Medium.ttf"
