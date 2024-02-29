label week_2_saturday_monika:
    call calendar_transition(day=4, hour=16, minute=20) from _call_calendar_transition_11
    scene bg cafe_inside_afternoon
    camera master
    with dissolve_scene_full
    $ set_internet(True)
    play music cafe

    "As I finish up my shift at the cafe, I sigh to myself."
    _mc turned casual apron eg mj "So much has happened lately that it’s been hard to keep up."
    _mc ec mh "It makes everything a little... exhausting."
    _mc ef ma "Part of me isn’t sure what to do. Looks like I got shafted, same as Yuri."
    _mc mh "... I feel terrible for her, honestly."
    _mc ec "All she wanted was to protect her friend, someone she cared about, and I threatened that."
    _mc "Maybe there was some jealousy there, but that’s not the point. Whether I meant to or not, I tugged away at the strings holding them together, and pushed a rift between them."
    _mc ef bi "And for all that, I gained nothing."
    _mc eg "... Monika was right, I’m really not ready for a relationship."
    _mc ec ba "I think I’ll take some time to find out what it means, learn how to be a good friend again, before I let myself become so... so enamoured, again."
    _mc ea ma "I reckon this sleepover tonight will help. I’ll be able to hang around the club, as friends."
    _mc "We can just let bygones be bygones, for a little while."
    b turned me "Be good, kid."
    show boss md:
        matrixcolor TintMatrix("#f5e2bb")
        t11
    $ persistent.boss_seen = True
    _mc mf "Huh? Oh, the boss."
    b bb ec me "I know you’ve had something on yer mind, today, so make sure you behave while yer not in a perfect headspace."
    show boss ea ba md
    mc mb "I will. Thank you."
    show boss ec ma lup
    "I give him as warm of a smile as I can muster, while he ruffles my hair."
    _mc ec ma "The old guy’s been a father to me. I don’t know what I’d do without him."
    b ldown ea mb "And enjoy yer day off, tomorrow. This festival of yers’ll go well, I’m sure of it."
    show boss ma
    mc eh md "I don’t doubt. We’ve been preparing all week!"
    b ed mc "Well, I’ll see you next week, shall I?"
    mc ea mb bb "Sure will!"
    "I wave him off, and head out."
    
    scene bg cafe_outside_afternoon with wipeleft
    stop music fadeout 2.5

    "Before making my way home, I pause for a moment."
    _mc turned casual eg mf "My thoughts are swirling. I need to get in the right headspace for this."
    "I breathe in deeply, reigning in my focus."
    "And... out again."
    _mc ec mh "I think I’m ready."
    _mc ea ma "Let’s... do this."

    # goes back to script.rpy for the sleepover
    return