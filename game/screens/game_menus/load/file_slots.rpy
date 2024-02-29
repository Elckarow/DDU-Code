style page_button_text is branch_title:
    selected_font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"

init python:
    def load_file(s):
        lang = FileJson(s, key="language", empty=None, missing=None)
        return (
            FileLoad(s)
            if lang == preferences.language
            else Dialogue(__("This save was created in a different language (%s) than the current one (%s).") % (__(lang or "English"), __(preferences.language or "English")))
        )

screen load():
    tag menu

    default selected_slot = None
    
    use game_menu():
        vbox:
            align (0.1, 0.5) spacing 5

            grid 5 7 spacing 2:
                for i in range(35):
                    $ s = i + 1
                    
                    button xysize (128, 72):
                        background "#00000020"
                        hover_foreground "#00000030"

                        add FileScreenshot(s) xysize (1.0, 1.0)
                        
                        if not FileLoadable(s):
                            hover_sound None
                            activate_sound None
                            action SetScreenVariable("selected_slot", None)

                        else:
                            action SetScreenVariable("selected_slot", (s if selected_slot != s else None))

                        at transform:
                            xoffset -10 alpha 0.0
                            i / 70
                            easein_quart 0.4 xoffset 0 alpha 1.0

            hbox:
                for page in range(1, 10):
                    button:
                        selected_background Solid("#00000020")
                        hover_background Solid("#00000010")
                        background Solid("#00000008")
                        xysize (30, 30)
                        text str(page) style "page_button_text" align (0.5, 0.5)
                        action (FilePage(page), SetScreenVariable("selected_slot", None), SelectedIf(FilePage(page)))

                    null width 2

                null width 240

                button:
                    background Solid("#ff000090")
                    hover_background Solid("#ff0000")
                    xysize (120, 30)
                    action Confirm(message=_("Revert systems to original state? This can not be undone."), yes_action=Function(delete_all_data), no_action=Hide("confirm"))
                    text _("RESET"):
                        color "#fff"
                        xalign 0.5
                        style "branch_title"

        use info_extension(selected_slot)

screen info_extension(s=None):
    vbox:
        align (0.97, 0.35)
        vbox:
            frame style "empty":
                xysize (525, 20)
                hbox:
                    text _("Branch: ") style "branch_title" font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf"
                    null width 1
                    text FileJson(s, key="branch_name", empty="", missing="") style "branch_title"

                text FileTime(s, format=__("{#file_time}%B %d %Y, %H:%M")) style "branch_title" font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Bold.ttf" xalign 1.0
            
            frame:
                background Transform("#D9D9D9", alpha = 0.35)
                xysize (525, 223)

                add Solid("#000") xysize (300, 1) at unfurl
                add Solid("#000") xysize (125, 3) at unfurl

                add FileScreenshot(s) xysize (256, 144) align (0.9, 0.5)

                frame:
                    xysize (230, 223)
                    xpadding 8 ypadding 12
                    if s is not None:
                        text FileJson(s, key="last_dialogue", empty="", missing="") style "recent_dialogue"

                showif FileLoadable(s):
                    button:
                        hover_background Solid("#414141")
                        background Solid("#41414190")
                        xysize (257, 48) align (0.0, 1.0) yoffset 55
                        text _("LAUNCH") style "load_option"
                        action load_file(s)
                        at drop_reveal

                    button:
                        hover_background Solid("#797979")
                        background Solid("#79797980")
                        xysize (257, 48) align (1.0, 1.0) yoffset 55
                        text _("DELETE") style "load_option"
                        action FileDelete(s)
                        at drop_reveal

style recent_dialogue:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
    outlines []
    text_align 0.0
    size 14
    color "#000"

transform drop_reveal():
    subpixel True
    on show:
        alpha 0.0 yoffset -30
        easein_quint 0.5 alpha 1.0 yoffset 0
    on hide:
        easein_quart 0.5 alpha 0.0 yoffset -30

style branch_title:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
    outlines []
    text_align 0.0
    align (0.0,0.5)
    size 14
    color "#000"

style load_option:
    align (0.5,0.5)
    text_align 0.5
    color "#fff"
    outlines[]
    size 24
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"