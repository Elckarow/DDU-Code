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

        def button(self):
            smol = Thumbnail(self.cg, zoom=1.1)

            if self.condition:
                thumbnail = VBox(
                                smol,
                                Text(self.cg_name, style="gallery_button_text"),
                                Text(_("by {#cg author}") + self.author, style="gallery_button_text_small")
                            )
                action = Show("cg_display", dissolve, cg=self.cg)

            else:
                thumbnail = VBox(
                                At(smol, Transform(matrixcolor=SaturationMatrix(0.0) * BrightnessMatrix(-0.4)), GaussianBlur(25)),
                                Transform(Text(_("[[ LOCKED ]"), style="gallery_button_text"), align=(0.5, 0.5))
                            )
                action = NullAction()
                        
            return ImageButton(
                        idle_image=thumbnail,
                        hover_image=Transform(thumbnail, matrixcolor=BrightnessMatrix(0.2)),
                        action=action
                    )            
    
    cg_list = (
        GalleryCG("cg amelia 1", _("The Going Home Club"), "Hanasaki Yunarin", "persistent.amelia._cgs[0]"),
        GalleryCG("cg melody 1", _("The New Day"), "Staticquit &\nHanasaki Yunarin", "persistent.mc._cgs[0]"),
        GalleryCG("cg melody 2", _("The Flowing of Ink"), "Staticquit", "persistent.mc._cgs[1]"),
        GalleryCG("cg sayori 1", _("Wuthering Heights"), "Hanasaki Yunarin", "persistent.sayori._cgs[0]"),
        GalleryCG("cg yuri 1", _("The Black Cat"), "Hanasaki Yunarin", "persistent.yuri._cgs[0]"),
        GalleryCG("cg monika 1", _("Confessions of a Mask"), "Hanasaki Yunarin", "persistent.monika._cgs[0]"),
        GalleryCG("cg natsuki 1", _("Oliver Twist"), "Kuta Pinku", "persistent.natsuki._cgs[0]"),
    )

    cg_positions = (
        (0.14, 0.1),
        (0.14, 0.55),
        (0.6, 0.1),
        (0.6, 0.55)
    )

screen gallery():
    tag menu

    default page = 0
    default number = 4
    default m = (len(cg_list) - 1) // number

    use game_menu(GalleryMenuInfo, menu_style="book"):
        style_prefix "gallery"

        for i, cg in enumerate(iterPage(cg_list, page, number)):
            add cg.button():
                pos cg_positions[i]
        
        use book_turn_page(
            If(
                page != 0,
                true=(SetLocalVariable("page", page - 1), With(game_menu_transition))
            ),
            If(
                page != m,
                true=(SetLocalVariable("page", page + 1), With(game_menu_transition))
            )
        )

style gallery_button_text is screenshot_button_text:
    size 22
    color "#000"
style gallery_button_text_small is gallery_button_text:
    size 17

screen cg_display(cg):
    zorder 50
    modal True

    add cg at CG # see cgs.rpy

    key ["mouseup_1", "mouseup_3", "K_ESCAPE", "K_SPACE"] action Hide("cg_display", dissolve)
