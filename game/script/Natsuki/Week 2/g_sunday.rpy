label week_2_sunday_natsuki:
    call calendar_transition(day=5, hour=11, minute=20) from _call_calendar_transition_24
    scene black with Dissolve(1.0)
    scene bg s_living_room
    show sayori turned casual e3c at i11
    with mc_pov(True)
    $ set_pov("mc")

    "As I help Sayori pack up, she hums to herself wistfully."
    _mc turned casual "I don’t think she could possibly be in a better mood."
    _mc ec mh "I goddamn hate myself."
    _mc bi eg "I’m about to ruin her mood."
    _mc ec "And there’s nothing I can do about it."
    mc ea ba ml "Sayori, I..."
    s me e1a "Hm?"
    s mb lup "What’s up?"
    show sayori ma
    mc ef mg "Look, I..."
    show sayori md ldown
    mc mf bi "We..."
    show bg s_living_room as stuff zorder 5 with Dissolve(0.3):
        align (1.0, 0.6) zoom 2.5
    "I look away, racking my brain for something, {i}anything{/i} to say."
    "The words to make this better, or easier, or-"
    _mc eg mh "... No."
    _mc ec "Because all that does is make it easier on me."
    _mc ef "Not on her."
    _mc ec "And that is so unbelievably selfish."
    hide stuff
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc ea bd mg "We need to talk."
    s mg "What’s up?"
    show sayori md with say_dissolve
    mc ml ef bi "... There’s something you need to know, and I..."
    extend mg ec " I want you to be prepared for it."
    show sayori mj b2b
    show black:
        alpha 0.5
    with NonBlockingDissolve(0.5)
    "She nods silently, picking up the change in mood."
    "I bite my lip."
    "Grit my teeth."
    hide black with NonBlockingDissolve(0.5)

    play music wtdgi

    "And swallow my pride."
    #[Full Voice Acting]
    mc ef ml ba "Sayori..."
    mc ea mg bg "Your mother’s dying."
    show sayori b1a md with say_dissolve
    "I watch her somewhat happy demeanour melt from her face."
    show sayori e1b b2b me with say_dissolve
    "Replaced with a look of horror."
    s mg "Y- You... What?"
    s shadow lup e2b nb mh "N- No, but I... I just-"
    s rup ldown e2d b2a mk "I just saw her, this year, she was in good health, and-"
    s mi lup rdown e2b "I mean, sure, she was taking a lot more medication, and more trips to the hospital, and- But that doesn’t mean that she-"
    show sayori mk with None
    show sayori ldown e1b mm b2c
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    "I reach out to place my hand on her shoulder, but she backs away."
    $ autofocus.unblock("sayori")
    s lup rup mi "N- No, don’t touch me!"
    show sayori at t21
    s rdown e2b mh "You... She... My mother!"
    s b2b mg "I- But I- She was right-"
    show sayori at t22
    s ldown e3c mk "N- No, that’s not right!"
    show sayori at t21
    s ml b1d "It can’t be!"
    show sayori at t22
    s rup e2d b2a mh "She was- I swear she was-"
    show sayori at t11
    s b2b mk "N- No! It can’t... It can’t be!"
    show sayori lup mm e3c
    "She shakes her head violently back and forth, desperate to unhear the words I spoke."
    s mk "I- No! But- I-"
    show sayori at t21
    s mi "Please! Just make it stop!"
    show sayori at t22
    s ml e3d b2a "Make it all stop! I swear it! I’ll be good! I won’t misbehave! I’ll do my best at school!"
    show sayori at t21
    s e3c tears_a b2b mh "And I’ll..."
    s me "..."
    s ldown rdown mk "... Please, don’t leave me, mom..."
    show sayori mj
    mc ml "Sayori, I’m so, so sorry."
    s e2a notears b1b mg na bags "... How long have you known?"
    show sayori me
    mc ef mh "..."
    s b2b e1a mh "Who told you?"
    s e2c mg "Is she..."
    s b1b me e2a "Can I..."
    "Listlessly, she stares at the wall."
    "A vacant gaze, lifeless."
    mc mg "I found out last night."
    show sayori md
    mc eg mb "I... I couldn’t ruin your party, the one you’d spent so long planning."
    "I can see how much anger wills to well up inside her, but it doesn’t."
    "How much she wants to deny it, but she doesn’t."
    s me "... I see."
    s mg "Can I..."
    s mh "Can I be alone, for a little while?"
    show sayori md
    mc ea mh bf "..."
    mc bg mb "Alright. I’m just next door if you need me, okay?"
    $ autofocus.block("sayori")
    s "..."
    $ autofocus.unblock("sayori")
    s me "Yeah."
    show sayori md

    scene black with Dissolve(1.5)
    $ advance_date(minutes=6)
    play sound fall
    if preferences.language is None:
        $ auto_advance_date_mult = 4

    "I hardly made it inside the door before I collapsed myself."
    _mc turned casual eb bg nb mh "I’ve... never seen Sayori like that."
    _mc ea "I didn’t want to leave her, but at the same time, I don’t dare push her."
    _mc ec ba na "She needs this time to process it."
    "..."
    _mc eg "I thought I was stronger than this."
    _mc bi mm "I wanted to be a rock she could lean upon, but here I am, lying in a heap on the floor."
    _mc ea bg mh "I’m sorry, Sayori. I thought I’d hardened my heart."
    _mc ef "But clearly, I haven’t come close."
    _mc ba "... I suppose time will tell whether that was a good thing or not."
    _mc ea "Natsuki would be upset if she found out any of this."
    _mc bi eg "That I waited to tell her, and that I’m taking it just as poorly, now that it’s hit me."
    _mc ma bg ea "... I can’t remember a time without Misato. She was... almost as much of a mother as-"
    _mc ef mh "... No, she was more of-"
    "..."
    _mc ec ba "Now, I don’t know what to think."
    _mc thinking ea "How would I react if I were in her situation?"
    "..."
    _mc ec "I would cry."
    _mc ldown ef "As angry as I am with that woman, as furious as all these years have made me-"
    _mc bg "I don’t think I could ever stay strong if I..."
    _mc eg "If I lost my own mother."
    _mc ea bf "Sayori... She’s wiser, stronger- She’s everything I’ve ever aspired to be and more."
    _mc eg bi "And I’ve just shattered her world."
    play sound phone_notification
    phone register "mc_n":
        time auto True
        "n" "I’m disappointed."
    pause 0.5
    phone discussion "mc_n":
        pause
    phone end discussion 

    _mc ec "As am I."
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    
    $ persistent.natsuki.mark_ending(1)
    return