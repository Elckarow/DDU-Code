init python:
    class GalleryCG(object):
        def __init__(self, cg, name, author, condition=None):
            self.cg = renpy.easy.displayable(cg)
            self.cg_name = name
            self.author = author

            self._condition = renpy.python.py_compile(condition or "True", mode="eval")

        @property
        def condition(self):
            return renpy.python.py_eval_bytecode(self._condition)

    cg_list = ( 
        GalleryCG("cg amelia 1", _("The Going Home Club"), _("Hanasaki Yunarin"), "persistent.amelia.cgs[0]"),
        GalleryCG("cg melody 1", _("The New Day"), _("Staticquit & Hanasaki Yunarin"), "persistent.mc.cgs[0]"),
        GalleryCG("cg melody 2", _("The Flowing of Ink"), _("Staticquit"), "persistent.mc.cgs[1]"),
        GalleryCG("cg sayori 1", _("Wuthering Heights"), "Hanasaki Yunarin", "persistent.sayori.cgs[0]"),
        GalleryCG("cg yuri 1", _("The Black Cat"), "Hanasaki Yunarin", "persistent.yuri.cgs[0]"),
        GalleryCG("cg monika 1", _("Confessions of a Mask"), "Hanasaki Yunarin", "persistent.monika.cgs[0]"),
        GalleryCG("cg natsuki 1", _("Oliver Twist"), _("Kuta Pinku"), "persistent.natsuki.cgs[0]"),

        GalleryCG("cg sayori 2", _("The Special Place"), "Hanasaki Yunarin", "persistent.sayori.cgs[1]"),
        GalleryCG("cg sayori 3", _("Trust Misplaced"), "Hanasaki Yunarin", "persistent.sayori.cgs[2]"),

        GalleryCG("cg natsuki 2", _("The Sleeping Prefect"), "Hanasaki Yunarin", "persistent.natsuki.cgs[1]"),

        GalleryCG("cg yuri 2", _("Opening Up"), "Hanasaki Yunarin", "persistent.yuri.cgs[1]"),

        GalleryCG("cg sleepover 1", _("A Sleepover by Any Other Name"), _("Errizzz"), "persistent.sleepover.cgs[0]"),
        GalleryCG("cg sleepover 2", _("Cause for Concern"), "Errizzz",  "persistent.sleepover.cgs[1]"),
        GalleryCG("cg sleepover 3", _("Battle Awaits"), "Errizzz", "persistent.sleepover.cgs[2]"),
        GalleryCG("cg sleepover 4", _("Midnight Cookies"), "Errizzz", "persistent.sleepover.cgs[3]"),
    )

define cg_size = (282, 158)

screen gallery():
    tag menu

    default cols = 4
    default rows = math.ceil(len(cg_list) / cols)

    use game_menu():
        style_prefix "gallery"

        frame style "empty" padding (60, 40) xysize (1.0, 1.0) xoffset -(gui.bar_size / 2.0):
            viewport id "gallery_vp":
                mousewheel True
                draggable True

                grid cols rows:
                    allow_underfull True 
                    xspacing 10 yspacing 20 

                    for i, cg in enumerate(cg_list):
                        vbox style "empty" xsize cg_size[0]:
                            at transform:
                                RoundedCorners(20)
                                yoffset 10 alpha 0.0
                                (i + 1) / 20
                                easein_quart 0.5 yoffset 0 alpha 1.0

                            button style "empty":
                                at transform:
                                    xysize (1.0, cg_size[1])
                                    on idle:
                                        matrixcolor BrightnessMatrix(0.0)
                                    on hover:
                                        matrixcolor BrightnessMatrix(0.13)

                                if cg.condition:
                                    add cg.cg at Transform(fit="contain")
                                    action Show("cg_display", dissolve, cg=cg)

                                else:
                                    action NullAction()

                                    frame style "empty" xysize (1.0, 1.0) background "#cecece":
                                        text "[[ LOCKED ]" style "gallery_button_text" align (0.5, 0.6) size 25 kerning 0

                            frame xsize 1.0 ysize 66 background "#e3e3e3":
                                padding (10, 10)

                                if cg.condition:
                                    vbox spacing -5:
                                        text phone.short_name(cg.cg_name, 23) style "gallery_button_text"
                                        text cg.author style "gallery_button_text_small"

                                else:
                                    text "???" style "gallery_button_text_small"
                    
        vbar value YScrollValue("gallery_vp") style "history_vbar" xalign 1.0

style gallery_button_text is empty:
    size 22
    color "#000"
    outlines []
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"
    kerning -1
    xfill True

style gallery_button_text_small is gallery_button_text:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
    size 17

screen cg_display(cg):
    zorder 50
    modal True

    add cg.cg at Flatten

    vbox style "empty" anchor (0.0, 1.0) pos (0.01, 0.99) spacing 1:
        text cg.cg_name style "gallery_button_text" color "#fff" 
        text cg.author style "gallery_button_text_small" color "#fff"

    key ["mouseup_1", "mouseup_3", "K_SPACE"] action Hide("cg_display", dissolve)

    on "show" action SetField(custom_keymap, "allowed", False)
    on "hide" action SetField(custom_keymap, "allowed", True)