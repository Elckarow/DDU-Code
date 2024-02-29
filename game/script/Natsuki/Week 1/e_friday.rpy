label week_1_friday_natsuki:
    stop music fadeout 2.0
    call calendar_transition(day=27, hour=15, minute=40) from _call_calendar_transition_15
    camera master
    scene bg club_day
    with dissolve_scene_full
    $ set_internet(False)
    play music pensive
    show bg:
        align (1.0, 0.6) zoom 1.8 
    show sayori turned e2c md at i44
    with NonBlockingDissolve(0.4)

    "Part of me has kept an eye on Sayori, pretty much all day."
    _mc turned tail nostrands ec mh "Of course it has; I’m worried about her."
    _mc ef "I almost made her something for lunch this morning, but decided against it. All it would do is make her feel worse."
    _mc ea bd "I don’t understand; how did this happen? How could I have allowed this to happen?"
    _mc eg bi mm "This is my best friend, suffering in silence, with no-one else having a clue!"
    _mc ec mh ba "It’s... unfair."
    _mc "Sayori deserves better."
    "..."
    "I haven’t even touched my book, just held it in front of me while my eyes, and thoughts, wander."
    _mc ef "... What do I do?"
    _mc bg "How can I help her?"
    _mc ea bf "Isn’t it amazing how quickly everything can fall apart? I thought I knew her."
    _mc eg bi mm  "... And here I am, having learned nothing from my mistakes."
    _mc mh "What a waste."
    $ autofocus.block("natsuki")
    camera master:
        blur 0.0
        easeout 0.2 blur 1.0
    show natsuki turned mh lhip b3a onlayer above_master:
        xpos 0.0 xanchor 0.7 zoom 1.9 ypos 1.0 yanchor 0.67
        matrixtransform RotateMatrix(0, 0, 0) xoffset 0 matrixanchor (0.5, 1.0)
        ease 0.2 matrixtransform RotateMatrix(0, 0, 35) xoffset 150
    n "Hey."
    hide sayori
    show bg:
        zoom 1.0 blur 0.0
    camera master
    hide natsuki
    show natsuki turned ldown mm nb e1b b3d at i11
    with None
    camera master at vpunch
    play sound smack
    "!!"
    show natsuki mj na e1a 
    "I jump from my seat, startled by the sudden appearance of a certain pink-haired club member."
    $ autofocus.unblock("natsuki")
    n cross e2a b1d mh "Geez dude, creepy as hell."
    show natsuki mj
    mc eb bd nb mg "M- M- Me?"
    n e1d mi "Yeah. You think I didn’t notice you?"
    show natsuki mj
    mc bi ec ml "Notice what?"
    n e2a b1a mg "You’re staring."
    n turned b1d e1a mh "Kinda creepy."
    show natsuki lhip rhip mj
    mc ef ba mg "I, ah, don’t know-"
    n rdown b1a e2a mg "... Look. She told me. I’m sorry you found out this way."
    show natsuki ldown mj
    mc na ea ba ml "You knew?"
    n e3c b3a mh "Of course I knew. She’s my best friend."
    show natsuki e1a md
    mc mf ef bi "... Of course you knew. I..."
    n b1a mh "Don’t beat yourself up over it; no-one else in the club knows."
    show natsuki me
    mc ea ba ml "But I-"
    n b1d mh "You {i}were{/i} her best friend. Take some time to consider that, alright?"
    show natsuki mj at thide
    mc ef mh "..."
    show natsuki e2a md:
        easein 0.4 xoffset -200
        "natsuki turned e1b nb md b3a"
        hop
    play sound ["<silence 0.4>", audio.phone_notification]
    "As Natsuki starts to slink away, she suddenly jumps at the sound of a phone on silent."
    n e1a b3a nb mh "S- Sorry, that's..."
    show natsuki b1d e2a md at lhide
    hide natsuki
    "Reaching into her bookbag, she fumbles with a device for a moment, throwing the club an offhand wave as she takes off out of the room."
    _mc thinking ec "Was that a satellite phone? Why the hell would she need one of those out here?"
    show sayori turned md at t33
    show monika turned nb mc at t32
    show yuri turned lup e1d me at t31
    "Returning my gaze to the remaining club members, it's clear that Monika and Yuri are just as surprised as I am - Sayori, however..."
    s e2a mg "{size=-5}Not {i}that{/i} phone again...{/size}"
    show sayori md
    show monika na
    mc ldown ea mg "Everything alright?"
    show yuri md
    s e1a mh lup "Well... It's just that every time she pulls out that phone, she vanishes for a few days."
    show sayori md
    mc ef ml "That doesn't sound good."
    show sayori e2c ldown
    "Sayori doesn't say any more, but she doesn't meet my gaze."
    y e2a b1d mb "She- She did mention she has work, and that it comes up suddenly?"
    show yuri ma
    mc mg ea "Then I don't really see a need to worry too much, I guess."
    show sayori e2a mj b1b
    "My attempt to alleviate the concern on Sayori's face seems pointless as she turns even further away from us."
    s mg "Then... Why does she always come back hurt?"
    show sayori md
    "No-one, it seems, has an answer for her question."
    s mg e3c "I'll just..."
    show monika bc
    s e1a b1a mh "Monika, could you...?"
    show sayori md
    show monika ma ba
    "Monika looks confused for a brief moment, but shakes it off quickly and returns to her natural smile."
    show yuri e1d b1a
    m mb lpoint "Of course I'll take a walk with you. Yuri, would you mind locking up? I think we're done here for the day."
    show monika ma
    y mg "O- Oh, yes, I can do that..."
    show yuri e3c ma at t42
    show monika eb at lhide zorder 1
    hide monika
    show sayori b2c e2a at t51
    "Yuri reluctantly takes the keys and nods, giving Monika a wave as the two of them leave through the door."
    s mg "S... Sorry. I just..."
    show sayori e2b shadow nb md
    show yuri e1a md
    "Unable to say a word to her, I watch in silence as those sapphire eyes glisten with a deep fear."
    show sayori e3c at thide
    hide sayori
    "After a moment, she looks down at her feet, finally stepping away and following Monika."
    _mc ec mh "Useless, yet again."
    show yuri shy ea ma ba at t11
    y "S- So... MC, I take it you're..."
    mc mg ea "Oh, no, I don't have to leave just yet. Amelia's helping the robotics club with something this afternoon, so I don't have anywhere to be until the end of club time."
    y bb eb "I- I see..."
    "I can't quite tell if Yuri's disappointed or happy, the way she's hiding behind her bangs."
    mc mb "Did you want me to stick around?"
    y turned e1d mb nb b1a lup "Y- Yes! Please do!"
    show yuri e2a b2b ma
    _mc ec ma "Well, that answers that. Sometimes just asking is the best policy, I guess."
    mc mb ea "Alright, guess it's just you and me."
    y b1a e1d mh "Erm... Unless you want to be somewhere?"
    show yuri md na
    mc ml "I mean, I'd like to be right here?"
    _mc ec mh"... I feel like this conversation is going in circles."
    _mc ea ma "Let's speed this up, shall we?"
    mc mg "So, Yuri, did you want to get something to eat?"
    y e2a ldown mb "I've already eaten, thank you..."
    show yuri ma
    _mc ec mh "Shit."
    _mc ef bi ma"Turns out, I'm about as good at small talk as I thought I was."
    y e1d mh "B- But, we can go get something, if you'd like...?"
    show yuri md
    _mc eg ba ma nb "Oh, good, she's just as bad as I am. That's... comforting."
    mc mg na ea "No, I'm... Look, do you just want to study for a little while? I'll help you where I can."
    show yuri ma
    "Her eyes seem to light up a little in response."
    y lup e1a mb "O- Oh! Yes, actually, I had a couple questions about our history class."
    show yuri ma
    mc mb "That I can help with - I just finished compiling my notes last night!"
    _mc ec ma "Seems I can save this conversation after all..."
    
    stop music fadeout 2.0
    scene black
    show bg school_street_afternoon
    show amelia turned eb md:
        matrixcolor TintMatrix("#ffecdb")
        i11
    with longfade
    $ set_date(hour=16, minute=43)
    play music hnt

    "I make my way home slowly, trudging along the sidewalk."
    hide black
    show layer master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("amelia")
    "Amelia slowed her own pace just to keep up with me. It’s strange. When we first met, I was the strong one, pulling her up when she needed it."
    _mc turned tail nostrands ec mh "Now, I feel like a limp noodle she’s carrying around in her pocket."
    am me "What is it, Mel?"
    show amelia ea md with say_dissolve
    mc "..."
    mc ef mf "Nothing, just..."
    am lup me ed "Whatever happened yesterday?"
    show amelia md with say_dissolve
    mc ml "... Yeah."
    am me "Well, just because something happened, doesn’t mean you need to be weighed down by it, right?"
    am eb bb mb ldown "You two didn’t seem to be on poor terms, so I don’t know what the problem is."
    show amelia md ba with say_dissolve
    mc bi mf "... It’s complicated."
    am bb mb "Well, maybe I can help?"
    show amelia ec ba md with say_dissolve
    mc ec mg "It’s also personal."
    show amelia ed bh mg with say_dissolve
    "She frowns."
    am ec me "Maybe so, but is it really so important that you keep it to yourself, when you’re clearly suffering because of it?"
    show amelia mg with say_dissolve
    mc mf "... Yes."
    show amelia ee mc bi with say_dissolve
    "She sighs, clicking her tongue."
    am ea mb bd "Look, Melody, I think we both know something the other doesn’t."
    am ba ec me "I never considered it before yesterday, but I think I understand."
    show amelia ea md with say_dissolve
    mc ea ba ml "Understand what?"
    am ed bd mb "... It must be rough, yeah?"
    am ea rup "Being stuck in a position like yours."
    show amelia bb eb me rdown with say_dissolve
    mc eb bd mg nb "What position? What do you think you know?"
    show amelia ea bd ma with say_dissolve
    mc bi ef ml "... Sorry. I didn’t mean to snap."
    call close_eyes(duration=0.2) from _call_close_eyes_9
    "I sigh, putting a hand to my head. There I go, blowing up again over nothing."
    hide amelia 
    am turned bd ed mb "It’s alright, I understand how you feel. It’s a nightmare sometimes, trying to understand our own feelings."
    am bb eb me "Sayori was the girl you once liked, right?"
    show amelia md:
        i11
        matrixcolor TintMatrix("#ffecdb")
    call open_eyes from _call_open_eyes_6
    mc ec mh na ba "..."
    am ee ba me "So, that means there are bound to be some feelings that have been unresolved, and they’re bubbling to the surface because of it."
    am lup ed bd mb "I... I know how you feel."
    am me ldown "Worse, you’ve probably been dealing with the nagging in the back of your mind over what it means to like her, right?"
    show amelia ea ma with say_dissolve
    mc ef "..."
    am ba ee mb "I mean, you’re both girls. It shouldn’t bother you, but it does."
    show amelia ma with say_dissolve
    mc mg "... At the time, it didn’t matter."
    show amelia ea with say_dissolve
    mc eg bi mb "Of course it didn’t; we were best friends. Neither of us would have listened to any talk like that."
    am bb eb me "But now it does?"
    show amelia md with say_dissolve
    mc ef ba mh "..."
    mc ml "Now, it feels like..."
    extend eg bi mf " Like I don’t know."
    show amelia bc ea ma with say_dissolve
    mc eb bd mg "How could I know? I don’t even know if I still like her."
    am bb eb me "Is that it?"
    am ec ba "Or are you just jealous?"
    show amelia md with None
    show layer master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I stop dead in my tracks."
    $ autofocus.unblock("amelia")
    am lup ed me "Jealous that you’ve been replaced."
    show amelia ea md
    "My fist balls as I whirl around to face Amelia."
    mc mm eb bd nb "You-"
    am ldown ee mf "Yeah. Someone had to bring it to the surface. I guess that someone was me."
    show amelia mg bh ec
    "My lip twitches as I bite down on it."
    am ed ba mh "I know you didn’t want to hear it, but you can’t ignore the sensation."
    am ec me "I saw how you reacted when Sayori mentioned she wanted to invite her friend yesterday. I’m not blind."
    show amelia mg
    mc ef bi mh "..."
    "I breathe a deep sigh."
    am rup ea bb me "Even if you aren’t interested in her anymore, you have to face the fact that you aren’t her first priority anymore."
    show amelia ba md
    mc eg ba na mh "..."
    am mb bc rdown "But remember, you don’t have to be. Just because something is different, doesn’t mean it is bad."
    am ed lup ba "She obviously still cares about you, possibly as her second priority, but that doesn’t mean she cares less."
    am ea ldown me "She’s just found someone who means as much to her as you once did."
    show amelia ma eb
    mc ef "..."
    mc bg mf "Sayori..."
    am ec mb "You get it, don’t you?"
    am eb bb me "It doesn’t matter if you love her or not. She will still be around, because she wants to be."
    show amelia md
    mc mh "..."
    am ee me ba "So?"
    am eb "What’s it gonna be?"
    show amelia md
    mc ba ml "... I don’t know."
    show black with NonBlockingDissolve(0.5):
        alpha 0.5
    _mc mh "That’s the truth. I have no idea what she means to me anymore."
    _mc ea "Sayori was my best friend, and even now, she still feels like it."
    _mc ec "I’m just not hers, anymore."
    _mc ea "... I want to say I’m not jealous. I want to scream it, to make sure everyone understands, but-"
    extend ef " That would be a lie."
    show amelia ma
    _mc bi "It hurts to admit, but... I’m jealous of Natsuki, for how close she is with her."
    _mc ec "How close she is with my best friend."
    hide black with NonBlockingDissolve(0.5)
    _mc ba "... Yeah. My best friend. I don’t... I’m not in love with her. Not anymore."
    am ee mb "You look like you’ve made up your mind."
    show amelia ma ea
    mc ef ml "... Yeah."
    mc ea mg "I have. Sayori means the world to me, but-"
    extend eg mb " I won’t ruin her happiness."
    mc ea mg "She has someone who can protect her, keep her happy, in Natsuki. I’ll have to trust her."
    am ef bb mb "I’m happy you’ve made a decision. Now you just have to stick to it."
    show amelia ma
    mc ml ef "... Yeah."
    "I bite my lip. Easier said than done; there was a reason I fell for her last time."
    _mc ef bi mh "... Now, it feels like I’m losing, and I always hated that."
    am ee me ba "You’ll be alright. I’m pretty confident in your abilities to keep on top of everything."
    am ed lup mb "All you have to think is that it’s just another hurdle for you to jump on your quest to graduation."
    show amelia bi mc ldown
    mc eg bi mj "... I cannot, for the life of me, comprehend how stupid of a thing to say that was."
    am ec bh mf "But hey, could be worse! I could have said something poetic and meaningful."
    show amelia mg
    mc ed md ba "... Somehow, yeah. That would be worse."
    show amelia ma ef bb
    "We chuckle, as we reach the intersection where we turn off."
    show amelia eb
    mc ea mb "Well, I’ll see you tomorrow, Amelia."
    am rup mb "Sure will! Don’t go moping about, okay? You’ll make us both feel bad."
    show amelia ef ma rdown
    mc eh md "Wouldn’t dream of it."

    scene black with Dissolve(1.5)
    $ set_date(hour=23, minute=40)
    if preferences.language is None:
        $ auto_advance_date_mult = 0.57
    $ set_internet(True)

    "Tossing and turning, I struggle to sleep that night."
    "Maybe it’s the cacophony of thoughts swirling about my head, or simply a state of exhaustion beyond what sleep would allow, but it changes little."
    "The fact of the matter is, I cannot sleep."
    "..."
    _mc turned messy naked nostrands ec mh "The wall is nice."
    _mc ef ma "Yeah. That’s a good wall."
    _mc mh "Not like I’ve been staring at it for years, or anything."
    _mc ea "... Honestly, I’ve probably spent years of my life staring at this one wall."
    _mc ec "It’d almost be impressive if it weren’t so sad."
    _mc "Yeah. That’s it. Sad. Exactly what I’d call this situation."
    _mc ef "... That, and disappointing."
    _mc eg bi "I’ve always been a light sleeper, but come on - why can I not sleep?"
    _mc "Typical that it ends up this way. I just keep getting the short end of the stick."
    _mc ma "... Hah, maybe it’s that exact mindset that’s keeping me spinning my wheels."
    _mc ec ba mh "Pessimism. The state of mind where everything taken at face value is viewed to have the worst possible outcome or state of being."
    _mc "That was Amelia, when I first met her. The whole world was against her, kept pushing her down."
    _mc ef "When did we swap?"
    _mc bi "... Swap is the wrong word. I was already there, just... moreso, now."
    _mc ea ba ma "We should try to be more like Sayori, who does her best to see the best in everyone."
    _mc ef "Or more like Monika, who at least understands flaws are just strengths that have yet to be developed."
    _mc mh"... And less like me."
    _mc bi "Even Amelia’s grown out of her edgy phase."
    "I sigh as my hand falls onto the bed."
    _mc eg mj "God dammit. I’m always being left behind."
    _mc mh "I guess that’s the fate of someone like me; all grown up on the outside, but never had time to be a teenager."
    _mc ec ba "... Maybe it’s time I started, even if it is a bit late."
    _mc ea "I’ve got around five months of school left; I may as well give it a go before I have to graduate."
    "I chuckle. I suppose being a teenager might be fun, even though by all accounts I’m an adult."
    _mc eg ma "Never hurt to try, at least."

    $ add_calendar_description(calendar_descriptions["natsuki"][2])

    call week_1_saturday_natsuki from _call_week_1_saturday_natsuki
    return