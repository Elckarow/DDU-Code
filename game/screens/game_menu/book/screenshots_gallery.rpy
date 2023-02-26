default persistent.save_screenshots = False
default persistent.screenshots = { }

init python:
    def ScreenshotButton(date, d, file):
        message = date.strftime(__("{#screenshot_time}Taken the %m/%d/%Y at %H:%M"))

        image = im.Data(d, file)
        disp = VBox(
                    Thumbnail(image, zoom=1.1),
                    Text(message, style="screenshot_button_text", size=15)
                )

        return ImageButton(
            idle_image=disp,
            hover_image=Transform(disp, matrixcolor=BrightnessMatrix(0.2)),
            action=Show("screenshot_preview", store.dissolve, d=image, message=message),
            alternate=Confirm(message=__("Delete this screenshot?"), yes_action=[Function(operator.delitem, persistent.screenshots, date), Function(renpy.save_persistent), Hide("confirm")], no_action=Hide("confirm"))
        )

screen screenshot_gallery():
    tag menu

    use game_menu(GalleryMenuInfo, menu_style="book"):
        style_prefix "screenshot"
        
        if not persistent.screenshots:
            frame style "screenshot_page_1":
                text _("You haven't saved any screenshots\n(see the \"Save Screenshot\" option in the \"Display\" section)")
    
        else:
            default page = 0
            default number = 4

            python:
                l = (len(persistent.screenshots) - 1) // number
                page = min(page, l)

            for i, (date, (d, file)) in enumerate(iterPage(persistent.screenshots.items(), page, number)):
                add ScreenshotButton(date, d, file):
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

style screenshot_page_1 is game_menu_book_page_1

style screenshot_grid:
    align (0.5, 0.495)
    xspacing 233
    yspacing 70

style screenshot_text is book_text:
    size 22

style screenshot_button_text is screenshot_text:
    size 24
    xalign 0.5
    text_align 0.5

screen screenshot_preview(d, message):
    zorder 50
    modal True
    default _message = True

    add d:
        fit "contain"

    showif _message:
        text message yalign 1.0

    key "K_SPACE" action ToggleLocalVariable("_message")
    key ["mouseup_1", "mouseup_3", "K_ESCAPE"] action Hide("screenshot_preview", dissolve)