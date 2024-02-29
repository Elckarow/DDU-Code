label calendar_transition(clear=True, **kwargs):        
    $ custom_keymap.allowed = False

    if clear:
        window auto hide
        python:
            clear_layers()
            stop_channels(2.0)
        show black
        with Dissolve(1.5)
        pause 0.3
    
    python:
        set_date(**kwargs)

    if not renpy.is_skipping():
        call screen calendar_transition
        pause 0.1
        
    $ custom_keymap.allowed = True
    return

label main_menu_return:
    $ stop_channels()
    $ clear_layers()
    scene white
    $ pause(random.uniform(1.0, 1.7))
    $ renpy.full_restart(Dissolve(1.5, time_warp=_warper.ease))

    return

default language = None

label set_vars:
    $ _dismiss_pause = config.developer
    $ quick_menu = True
    $ allow_skipping = True
    $ language = preferences.language
    $ config.allow_skipping = True  
    $ phone.system.date = datetime.datetime(year=2017, day=23, month=10, hour=15, minute=5, second=7) 

    return

label set_vars_actI:
    call set_vars from _call_set_vars
    stop music
    pause 0.5
    return

# label main_menu:
#     return

label start:
    call set_vars_actI from _call_set_vars_actI_1
    $ aika_name = "???"

    call week_1_monday_common from _call_week_1_monday_common
    call week_1_tuesday_common from _call_week_1_tuesday_common

    jump actI

label actI:
    python hide:
        lit_club.add_character("mc")

        for c in phone.character.get_all():
            for gc in phone.data[c.key]["group_chats"]:
                phone.group_chat.group_chat(gc).unread = False
    
    call expression ("week_1_wednesday_%s" % branches.to_doki(branches.get_current())) from _call_expression_3

    python in phone.calendar:
        add_calendar_to_all_characters(
            year=2017, month=11, first_day=MONDAY
        )
    
    call expression ("week_2_wednesday_%s" % branches.to_doki(branches.get_current())) from _call_expression_4
    call sleepover from _call_sleepover
    call expression ("week_2_sunday_%s" % branches.to_doki(branches.get_current())) from _call_expression_5
    call end from _call_end

    return

label end:
    window auto hide
    python:
        stop_channels(2.5)
        clear_layers()
    show black
    with Dissolve(1.5)
    pause 1.0

    play sound_loop hum fadein 0.1
    python in console:
        show(None)
        pause(0.5)
        input(__("Branch {i}%s{/i} completed.") % store.branches.names[store.branches.get_current()], cps=None)
        pause(random.uniform(2.0, 3.0))
        hide(None, delay=-1)
    stop sound_loop

    scene white
    pause 2.0
    $ renpy.full_restart(Dissolve(1.5, time_warp=_warper.ease))
    return

image act_I_card = "mod_assets/STUFF/act_cards/act_I.png"
image act_I_n_card = At("mod_assets/STUFF/act_cards/act_I_n.png", GlicthedDisplayable().add_glitch(d="act_I_card", center=(660, 139), cols=14, rows=3, size=(10, 10), box=(883, 161, 216, 231)))
image act_I_s_card = At("mod_assets/STUFF/act_cards/act_I_s.png", GlicthedDisplayable().add_glitch(d="act_I_card", center=(660, 139), cols=14, rows=3, size=(10, 10), box=(756, 238, 144, 470)))
image act_I_y_card = At("mod_assets/STUFF/act_cards/act_I_y.png", GlicthedDisplayable().add_glitch(d="act_I_card", center=(660, 139), cols=14, rows=3, size=(10, 10), box=(433, 237, 307, 329)))
image act_I_m_card = At("mod_assets/STUFF/act_cards/act_I_m.png", GlicthedDisplayable().add_glitch(d="act_I_card", center=(660, 139), cols=14, rows=3, size=(10, 10), box=(990, 391, 270, 264)))

label act_card(card):
    $ custom_keymap.allowed = False
    window auto hide
    python:
        stop_channels(1.8)
        clear_layers()
    show black
    with Dissolve(1.8)
    pause 0.8
    play music "mod_assets/BGM/act_card.mp3" noloop 
    scene expression card with Dissolve(1.5)
    pause (7.0 - 1.5)
    scene black with Dissolve(2.0)
    $ custom_keymap.allowed = True
    return

init python in branches:
    FEELINGS, BLOOD, SNARED, FATE = range(4)

    def get_current():
        return _current

    def set_current(b):
        global _current; _current = b

    names = {
        None: _("A Series of Unfortunate Events"),
        FEELINGS: _("Feelings Rekindled"),
        BLOOD: _("The Heart Beats with Blood"),
        FATE: _("Challenging Fate"),
        SNARED: _("Snared by the Flytrap")
    }

    def is_current(b):
        return _current == b

    _to_doki = {
        None: "sussy baka",
        FEELINGS: "sayori",
        BLOOD: "natsuki",
        FATE: "yuri",
        SNARED: "monika"
    }

    def to_doki(b):
        return _to_doki[b]

    _to_book = {
        SNARED:   _("{i}Confessions of a Mask{/i}"),
        FEELINGS: _("{i}Wuthering Heights{/i}"),
        BLOOD:    _("{i}Oliver Twist{/i}"),
        FATE:     _("{i}The Black Cat{/i}")
    }

    def to_book(b):
        return _to_book[b]

default branches._current = None
default book = None

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    return

label before_main_menu:
    return

label quit:
    return