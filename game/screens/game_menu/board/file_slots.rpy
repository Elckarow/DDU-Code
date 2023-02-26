default persistent.drag_outside = False

init python:
    def FileAction(what, *args, **kwargs):
        if what == "save":
            return FileSave(*args, **kwargs)
        elif what == "load":
            return FileLoad(*args, **kwargs)
        elif what == "delete":
            return FileDelete(*args, **kwargs)
        raise Exception(f"{what} not known by save screen")

    def FileButton(slot, what):
        if not FileLoadable(slot):
            image = Fixed(
                Text(_("No data"), style="slot_text_empty"),
                xysize=(config.thumbnail_width, config.thumbnail_height)
            )
        
        else:
            scrn = FileScreenshot(slot)        
            time = Text(FileTime(slot, format=__("{#file_time}%A, %B %d %Y, %H:%M")), style="slot_text")
            chap_info = Text(__("Week {week} - {day}").format(week=FileJson(slot, "week"), day=__(FileJson(slot, "day"))), style="slot_text")
            
            image = VBox(scrn, time, chap_info, xsize=config.thumbnail_width)
        
        return ImageButton(
            idle_image=image,
            hover_image=Transform(image, matrixcolor=BrightnessMatrix(0.1)),
            action=[FileAction(what, slot), If(what == "save" and not persistent.drag_outside, true=Show("dialog", game_menu_transition, message=__("Tip!\nYou can drag the save slots outside the board\nto delete them."), ok_action=(Hide("dialog"), SetField(persistent, "drag_outside", True))))]
        )

    @renpy.curry
    def slot_dragged(slot, drags, drop):
        i = slot - 1

        drag = drags[0]
        frame_x, frame_y = store.BOARD_FRAME_XYSIZE

        mouse_x, mouse_y = renpy.get_mouse_pos()

        mid_frame_x, mid_frame_y = frame_x / 2, frame_y / 2
        mid_x, mid_y = (config.screen_width / 2) + store.BOARD_XOFFSET, config.screen_height / 2

        top, bottom = mid_y - mid_frame_y, mid_y + mid_frame_y
        left, right = mid_x - mid_frame_x, mid_x + mid_frame_x

        if mouse_x < left or mouse_x > right or mouse_y < top or mouse_y > bottom:
            renpy.run(FileAction("delete", slot))
            target_x, target_y = slot_position(i)

        else: 
            drag_x, drag_y = drag.x, drag.y
            drag_w = drag.w
            drag_h = gui.slot_drag_handle_height

            left_padding, top_padding, right_padding, bottom_padding = store.BOARD_FRAME_PADDING

            top, left = 0, 0
            bottom, right = frame_y - top_padding - bottom_padding, frame_x - left_padding - right_padding

            if drag_x < left:
                target_x = left
            elif drag_x + drag_w > right:
                target_x = right - drag_w
            else:
                target_x = drag_x
    
            if drag_y < top:
                target_y = top
            elif drag_y + drag_h > bottom:
                target_y = bottom - drag_h
            else:
                target_y = drag_y
            
            target_x = absolute(target_x)
            target_y = absolute(target_y)

            persistent.slots_positions[int(FilePageName())][i] = (target_x, target_y)
            renpy.save_persistent()

        drag.snap(
            target_x,
            target_y,
            0.0
        )

        renpy.restart_interaction()
    
    def slot_position(i):
        return persistent.slots_positions[int(FilePageName())][i]       

define _BASE_SLOTS_POSITION = [
    (0.05, 0.1), (0.35, 0.1), (0.65, 0.1),
    (0.05, 0.5), (0.35, 0.5), (0.65, 0.5)
]

# persistent.slots_position[0] isn't used
# since the file pages are [1, 9]
default persistent.slots_positions = [
    list(_BASE_SLOTS_POSITION)
    for i in range(10)
]

screen save():
    tag menu
    use file_slots("save")

screen load():
    tag menu
    use file_slots("load")

screen file_slots(what):
    use game_menu(SaveMenuInfo, menu_style="board"):
        frame:
            style_prefix "slot_page"
            hbox:
                for p in range(1, 10):
                    textbutton "[p]" action (FilePage(p), With(store.game_menu_transition))

        draggroup:
            style_prefix "slot"
            for i in range(6):
                $ slot = i + 1

                drag:
                    drag_handle (0, 0, 1.0, gui.slot_drag_handle_height)
                    draggable True
                    drag_raise True
                    droppable False
                    drag_offscreen True
                    dragged slot_dragged(slot)
                    pos slot_position(i)

                    fixed at Flatten:
                        frame:                          
                            add FileButton(slot, what)
                        add Solid("#7f500a", ysize=gui.slot_drag_handle_height, xsize=config.thumbnail_width + gui.slot_xpadding + gui.slot_xpadding):
                            at transform:
                                alpha 0.7
    
    textbutton _("Reset") at board_button:
        style "game_menu_board_button"
        xsize None
        align (1.0, 0.0)
        action Confirm(message=__("Reset the game?"), yes_action=Function(delete_all_data), no_action=Hide("confirm"))

style slot_page_frame:
    background Frame("mod_assets/STUFF/game_menu/game_menu_board_torn_paper.png")
    padding (1, 4, 2, 7)
    modal True
    align (0.0, 1.0)
    offset (BOARD_XOFFSET - 21, 46)

style slot_page_hbox:
    spacing gui.slot_page_hbox_spacing

style slot_page_button:
    selected_background Transform(Frame("gui/scrollbar/horizontal_poem_bar.png", ysize=5, yalign=1.0), xzoom=-1.0)
    margin gui.slot_page_button_margin

style slot_page_button_text is board_text:
    size gui.slot_page_button_text_size

style slot_text is say_dialogue:
    size 15
    outlines []
    color "#000"

style slot_text_empty is slot_text:
    yalign 0.5

style slot_fixed:
    xfit True
    yfit True

style slot_frame:
    background Frame("mod_assets/STUFF/game_menu/game_menu_board_paper.png")
    padding (gui.slot_xpadding, 10 + gui.slot_drag_handle_height, gui.slot_xpadding, 5)