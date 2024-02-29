screen asoue_nodes(card, act_object):
    on "replace" action Hide("asoue_nodes")
    on "replaced" action Hide("asoue_nodes")

    vbox:
        at transform:
            subpixel True
            on show:
                alpha 0.0 zoom 0.8 xoffset -90
                easein_quint 0.5 alpha 1.0 zoom 1.0 xoffset 0
            on hide:
                easein_quad 0.5 alpha 0.0
                
        align (0.97, 0.165)

        hbox spacing 5:
            text _("Branch:") style "branch_indicator" color "#707070" font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-SemiBold.ttf"
            if act_object.branch_selected is not None:
                text card.chapters[act_object.branch_selected][0] style "branch_indicator"
            else:
                text _("No Branch Selected") style "branch_indicator" color "#707070a8"

        frame:
            add Solid("#000", xysize=(125,3)) at unfurl:
                offset (-10,-10)
            add Solid("#000", xysize=(300,1)) at unfurl:
                offset (-10,-10)
            xysize (830, 140)
            padding (10, 10, 5, 5)
            background Transform("#D9D9D9", alpha = 0.35)

            viewport:
                mousewheel True draggable True
                text (card.descriptions[0] if act_object.branch_selected is None else card.descriptions[act_object.branch_selected + 1]):
                    style "under_light" size 15 font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"




style branch_indicator is under_text:
    font "mod_assets/STUFF/main_menu/Montserrat/Montserrat-Regular.ttf"
    size 20

image node_selected_background:
    contains:
        CircleDisplayable(color="#000", radius=15, border=1, align=(0.5, 0.5))
    contains:
        CircleDisplayable(radius=5, color="#000", align=(0.5, 0.5))

transform node_button:
    subpixel True alpha 0.6
    on hover, selected_idle, selected_hover:
        easein_quint 0.5 zoom 1.1 alpha 1.0
    on idle:
        easein_cubic 0.5 zoom 1.0 alpha 0.6
