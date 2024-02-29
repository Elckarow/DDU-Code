label week_1_wednesday_natsuki:
    call act_card("act_I_n_card") from _call_act_card_2
    call calendar_transition(day=25, hour=15, minute=45, second=0) from _call_calendar_transition_13
    scene bg club_day
    with dissolve_scene_full
    play music okev
    $ set_internet(True)

    "The next day, I find myself once again in the clubroom. I don’t quite know why I’m so drawn to this place, but I’ll take it."
    "Everyone’s sitting down and reading at the moment, as we’re planning on sharing a short story each."
    _mc turned "It’ll be an interesting exercise, to be sure."
    _mc ec mh "I’m not quite certain what to make of the story I’ve selected; I picked it because of the interesting name, but it was really quite short. I finished it in only a few minutes, while everyone else was still concentrating."
    "So, instead, I think I’ll send Amelia a message, and see what she’s up to."

    phone discussion "mc_am":
        time auto True
        "mc" "Hey."
    "Doesn’t take long to get a response."
    phone discussion:
        "am" "Hey, how’s the club? Not bored already, I hope?"
        "mc" "Nah, I just finished my book early and didn’t want to bother anyone else."
        "am" "Couldn’t you read more from their collection?"
        "mc" "Huh. That’s a smart idea."
        "mc" "Thanks Amelia. I’ll catch you after the club."
        "am" "Sure, I’ll meet you out the front of the gate."
    phone end discussion
    $ phone_available = True

    "Turns out, Amelia ended up looking at the Home Economics Club today, inspired by my joining of the Literature Club. I was surprised when I heard, but it’s probably good for her."
    _mc ma "Besides, something about this club makes me feel more social today."
    _mc ea "I can’t quite put my finger on it, but I probably shouldn’t complain."
    "So, in light of her good idea, I walk over to the nearest club member."
    show natsuki turned e2a mj b1d at i11
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    mc mb "Hey, Natsuki, is there something else I could read? I finished my short story."
    "Without looking at me, I get a response. Seems she’s deep in thought."
    n mg "Hm? I mean, there’s Parfait Girls in the closet, if you want, but I-"
    n b1a e1a mh "Actually, sure, go for it. Top shelf."
    show natsuki md with say_dissolve
    mc ml "Top shelf? How do you reach it, then?"
    show natsuki e1d b1d mj with say_dissolve
    "She stops looking at her book for a moment to glare daggers at me."
    n mh "You really wanna go there?"
    show natsuki mj with say_dissolve
    mc bb nb mg "N- No, sorry, it was a genuine-"
    n lhip e2a b1a mg "I use another box, obviously."
    show natsuki mj with say_dissolve
    mc bg ef ml "I, ah, sorry, Natsuki. I didn’t mean to offend you."
    n rhip mi e3c "Sure, sure, short jokes are just the cream of the crop, aren’t they?"
    show natsuki mj with None
    show natsuki rdown ldown e2a mj
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She rolls her eyes and returns to her book."
    "Not really wanting to make it worse, I make for the closet."

    scene bg club_closet_day with wipeleft
    $ autofocus.unblock("natsuki")
    
    _mc turned mh "Well, I think I can see the box. Just have to get it down, I suppose."
    show bg with Dissolve(0.2):
        align (0.6, 0.9) zoom 2.2
    _mc ma "There’s actually quite a bit in here, now that I think of it. A tea set, an entire library of novels and novella."
    show bg with Dissolve(0.2):
        align (0.35, 0.9) zoom 2.0
    _mc "An almost complete collection of Tolkien’s work, in two languages? That’s incredible!"
    _mc thinking mh "If I had to guess, that’d probably be Monika’s. Yuri's probably read it, but I'm not sure if she'd want it in French, unless she's learning the language?"
    _mc ma "Though then again actually, maybe? The more I think about it, the more sense it makes."
    show bg with Dissolve(0.2):
        align (0.35, 0.4) zoom 2.0
    _mc ldown "Ah, the Poe collection over here would be hers, though."
    show bg with Dissolve(0.2):
        align (0.35, 0.7) zoom 2.0
    _mc thinking mh "Hm? Oh, there’s some stuff here Sayori would like, too." # im stuff
    _mc ec "I wonder if they all keep their collections stored here, for safekeeping."
    _mc "Though... I still can’t quite find anything that might interest Natsuki, outside of the one series."
    _mc ea "Interesting. It’s almost like that’s the only thing in here she owns."
    _mc ldown ma "Nah, that can’t be it. She probably just has interests that I don’t know about. I’ve hardly known her a day."
    show bg with Dissolve(0.2):
        align (0.56, 0.33) zoom 2.3
    _mc "Best to grab what I came for and not pry into anyone’s business, I think."
    show bg with Dissolve(0.2):
        zoom 1.0
    _mc ec "Alright, I’ve got the first volume. Let’s crack it open and-"
    _mc ea mh "... Huh. This is... somehow exactly what I expected."
    _mc ma "A group of cute girls on the front. Doesn’t exactly tell me what the manga is about, though."
    _mc eg "Let’s have a read, I suppose. No point judging it by its cover."

    scene bg club_closet_afternoon with fade
    $ advance_date(minutes=12, seconds=1)

    "I pause after a little while of reading."
    _mc turned ec mh "It’s surprisingly slow, even for a slice-of-life. Just gradually introducing characters and the setting. I wonder why this is so popular?"
    "As typical with manga volumes, it doesn’t exactly take me long to finish the entire thing."
    _mc ea "If I had to describe it in a word? Gradual."
    _mc ec "I can feel that it’s going somewhere, but I’ve no clue where, nor how long it will take to get there."
    _mc ef "Kind of strange, honestly. Usually the first volume tells you about the tone, feel and characters. But hey, I won’t judge."
    _mc ea thinking "There must be a reason Natsuki recommended it, and I’ll take her word that there’s something there."
    _mc ma ldown  "Oh, we’re being called back. I suppose I’ll keep reading tomorrow."

    scene bg club_afternoon
    show yuri turned e2a b1d lup:
        matrixcolor TintMatrix("#f1d6bb")
        i41
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        i43
    show monika turned:
        matrixcolor TintMatrix("#f1d6bb")
        i42
    show natsuki turned:
        matrixcolor TintMatrix("#f1d6bb")
        i44
    with wipeleft
    if preferences.language is None:
        $ auto_advance_date_mult = 0.727

    m lpoint mb "Alright everyone, how did we go?"
    show monika ldown ma
    y mb nb "I, ah... found it rather shallow, I must say."
    show yuri b1a e1a ma na
    show monika mc
    s mh "Mine was weird. I didn’t know what to make of it."
    show sayori md
    m md "Oh, really? I found mine fascinating."
    show yuri ldown
    show sayori ma
    m lpoint mb "It was about a man who went in search of a mythical planet, and when he got there, found quite an interesting dilemma."
    m ldown rhip eb "The reason it wasn’t talked about was that, even though it had cures for almost all ailments, no-one wanted to go near it, because it exercised free love."
    m ec md "It actually gave me something to think about, considering how restrictive our society can be on expression and free will."
    show monika rdown ea ma
    mc turned mg bb "Woah, that sounds like a lot to cover in a short story."
    m mb "It was actually a little closer to a novella in length. I’m surprised it was so concise, actually."
    show monika ma
    show sayori md
    mc mb ba "Well, what did you read, Sayori?"
    show natsuki mn e1b b2a
    s lup mh "Hm. I dunno!"
    show natsuki e3d mo b1a at hop
    show yuri lup e3d
    show monika ed
    show sayori mg b1d e1b nb
    "A chuckle washes over the club."
    _mc ec ma "That’s just like her."
    show monika ea
    show yuri e1a
    show natsuki e1a ma
    s lup rup e1b b4 mi "No, but really, it was odd. Oil rigs came alive and just sorta... chilled."
    show sayori b1a me e1a na
    n rhip mc "What, they just existed? And people did nothing?"
    show natsuki ma
    s rdown b1d mi "Well, no, they tried to fight them, of course, but the rigs were so big it was hard."
    s ldown e2a b2a mb nb "Eventually they just gave up and let them run free."
    show natsuki rdown
    show sayori na e1a b1a ma
    mc ea ml "So... What was the point?"
    s tap mb eb "... That’s what I’m trying to work out."
    show yuri e1d me
    s turned mh b1a "Maybe it was a message about things returning to nature? But it didn’t really feel like it, because the things were man-made in the first place."
    show sayori md
    y e1d mh "Hmm. I feel that I’ve read that one, myself. I found there was quite a bit more to it, actually. It’s been a while, but from memory, not only did the rigs come alive, but found a way to reproduce, correct?"
    show yuri e1a ma ldown
    s mh "Yeah, it was a bit strange."
    show sayori e1b mf
    m lpoint mb "How fascinating. Perhaps we’ll have to all have a read through sometime, and think about it together?"
    show monika ma ed
    s mc e3d "Oooh~ I like that idea!"
    show monika ea ldown
    show sayori ma
    n mc "It does sound like a fun way to spend a club meeting."
    show natsuki ma
    show sayori e1a
    m mb "Alright, let’s aim for next week, sometime."
    show monika ma
    y mb "I wouldn’t mind re-reading it, either."
    show yuri e1d rup md
    n mh "So, Yuri, what did you read?"
    show natsuki md
    y e2a mg b1d "Hmm. The tale I read was... Well, it was an old Poe story."
    show yuri e1d md b1c
    n mh b4 e1d "No surprise there, but I’d thought you’d read them all?"
    show natsuki e1a b3a me
    y e1a mb b1a rdown  "I have. It was a story I’d been meaning to return to, one of the tales that inspired Sherlock Holmes."
    show yuri e1d ma
    n mc b1a e1a "Oh, wait, I’ve read that one. It follows a detective that solves the mystery of a brutal murder."
    show natsuki ma
    y mb "I’m surprised you’ve read it. Though there are multiple stories, that was the one that I was most drawn to."
    show yuri e1a ma
    m md "I believe I’ve read that one too. I’m surprised, Yuri. I would have thought you’d go for something a little more out there."
    show monika ma zorder 1
    y lup mh e3c b3a "I was planning to, actually, but when I saw this story again, I simply couldn’t resist the chance to go over something that inspired me as a child."
    show yuri e1d b1c me
    show monika mc
    n cross e2a mb b1d "Heh, of course a story like that would inspire you."
    show sayori md
    n b1a mi e3c "Makes sense. You’re always looking at gothic horror."
    show natsuki e1a ma
    y e2a b1d nb mb "If you’ve read it, you’d understand. There’s a... draw to the unknown, within all of us."
    show yuri ma
    n e2a mm b1d nb "..."
    show natsuki md
    "Natsuki shuffles uncomfortably."
    n turned lhip rhip mh b3d "I don’t think there’s a book in existence that could compare to..."
    show yuri e1d md b1a na
    n mm nb b1d e2b ldown rdown  "!!"
    show sayori me b2a
    n mk e1b b3a "Ah, I, mean, it’s-"
    show natsuki fs eb mc bc nc at lhide zorder 0
    hide natsuki
    show sayori lup e2a mg
    show yuri rup e2b b2a nc mk
    show monika eb
    "She hides her face, panicking, before rushing out of the room."
    show monika ea bb
    show sayori mj ldown
    y shy ea mb ne "Wait, I didn’t mean to-"
    s e1a mb "No, it’s okay, I’ll go talk with her. I don’t think it was you, this time."
    show sayori md b2b e2a at lhide zorder 0
    hide sayori
    "Sayori races off after her, leaving Yuri and Monika, alongside myself, standing around awkwardly."
    mc mf "Should I..."
    show yuri at t21
    show monika md ba at t22
    m "No, I don’t think that’s necessary. Sayori knows her best, after all."
    show yuri ee nc ma bb
    m ec rhip "Besides, we still have your story to hear about."
    show monika ea mc
    mc mg bb "You want to continue without them?"
    y turned mb lup e2a nd "I don’t really see why not; it could be some time before they return."
    show yuri ma
    show monika ma rdown
    mc ef ml ba "Alright then..."
    _mc ec mh "Part of me does want to wait, but... I don’t really know Natsuki all that well, and Sayori will be fine, helping her out. I should trust them."
    show yuri e1a nb
    mc ea ml "Well, the story was very short, so it makes it a little challenging to really do justice with a summary. It’s better to experience it."
    mc thinking mb "But I’ll give it a go. Basically, there was a war, and stock of pretty much everything is out, so they’ve made replacements."
    show yuri ldown na
    mc mg "So a soldier reaches one of these bases and is given replacement food made of wood, because that’s all they’ve got. Which, you know, is just wood."
    mc ef bi ml "Not only does it not taste good, but there’s no nutrition in wood."
    mc ea ba mg ldown "But anyway, the point of the story is that at the end, he gets visited by one of the girls in the base, but all the women are dead. So it turns out, it’s a replacement woman, too."
    m lpoint md "Wait, so it’s a crossdresser?"
    show monika ldown ma
    mc mb "Yeah, one who pretends to be a woman to keep morale up, I suppose."
    mc ml "But uh, it was a little..."
    mc ef mb "Surprising, to say the least."
    y e3c lup mb "I see. A subversion based on setup. While the ending might have been predictable, it was the payoff, rather than the subversion itself, that makes the ending interesting."
    show yuri e1d b1c me
    mc bg "Y- Yes, that’s exactly right, though I could never have described it quite so eloquently..."
    y rup e2a b3a mh nb "O- Oh, my apologies, I never meant to outstrip you... It seems to be happening a lot, today..."
    show yuri e1a ma
    m rhip mb ed "Nonsense, Yuri. Just be you. MC was just complimenting your command of language, right?"
    show monika ma ea
    mc bb mg nb ea "Y- Yeah, I was, I just wasn’t expecting it, but it really did sum it up quite well."
    _mc ec ma ba na "And I thought my language skills were at least reasonably effective, geez..."
    _mc ea mh thinking "I wonder where she got such a command? Surely not from reading alone, right?"
    _mc ma ldown "Then again, anything’s possible."

    stop music fadeout 3.0
    scene bg club_afternoon
    show yuri turned e3d:
        matrixcolor TintMatrix("#f1d6bb")
        i21
    show monika turned lpoint mb:
        matrixcolor TintMatrix("#f1d6bb")
        i22
    with wipeleft_scene
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    $ advance_date(minutes=19)

    "We spend some time passing around small talk about our stories, and about some of the things that interest us, but neither Sayori nor Natsuki return."
    show yuri at thide
    hide yuri
    show monika ed ma at thide
    hide monika
    "At the end of club time, we go our separate ways."

    scene bg school_gate_afternoon
    show amelia turned ponytail md:
        matrixcolor TintMatrix("#f5d5b6")
        i11
    with wipeleft
    $ advance_date(minutes=3)

    am ec me "Took you long enough, geez. What held you up?"
    show amelia md
    mc turned ml "Oh, not much, I was just looking for one of the club members."
    mc ed md "Nothing too serious, don’t worry."
    show amelia ed ma
    "She shrugs, clearly not too upset that I kept her waiting."
    am eb bb mb "Alright, let’s hit the arcade, shall we?"
    show amelia ea ba ma
    mc ea mb "May as well, eh?"

    scene bg arcade:
        blur 2.0
    show amelia turned ponytail bh ec at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    with longfade
    $ say_transition = True
    $ autofocus.block("amelia")
    $ advance_date(minutes=33, seconds=17)
    $ set_internet(True)
    play music arcade

    #[Full Voice Acting]
    am mb "Look! I’ll bet you I can beat you at the crane game!"
    show amelia ma with say_dissolve
    mc turned eg mg "There’s no way in hell I’d take you up on that. I haven’t beaten you in one of those since we met!"
    am eb bb me "So, you admit it! You haven’t practised at all!"
    show amelia ec ba ma with say_dissolve
    mc ed bm ml "Of course not; I have more important things to do. School, ringing a bell? Grades?"
    am ed mb "Well aren’t you just a little ray of sunshine?"
    show amelia ma with say_dissolve
    mc ec ml bi "I have literally not, ever, in my entire existence, been a ray of sunshine. Partially because I am a human, not the refraction of light via water in the air."
    show amelia md ec with say_dissolve
    mc ef "And partially because I don’t care for positive attitudes."
    am rup me bb eb "Is that so? Then why join a literature club full of such bright personalities?"
    show amelia md ba with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    mc mf "... I don’t want to talk about it."
    show amelia rdown ed
    "Amelia pauses for a brief moment, peeling her eyes away from the game she’d started during our conversation."
    $ autofocus.unblock("amelia")
    am me bd "You okay?"
    show amelia ma
    mc eg mj ba "Yeah, I’m... fine."
    show amelia md
    mc bb mg "All sunshine and rainbows, here."
    show amelia mg bh ec
    "She frowns."
    am me "If you want to talk about it, you can, alright?"
    show amelia md with None
    hide amelia
    camera master:
        align (0.0, 0.2) zoom 2.5
    with Dissolve(0.2)
    "I look away from her."
    mc ef ba "It’s nothing major, just... You don’t know how it feels. Sayori was my best friend, and seeing her walk around with someone else taking that place..."
    mc bi ml "Even though it’s my own damn fault, it hurts."
    show amelia turned ponytail md at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("amelia")
    am me "You’re... jealous?"
    show amelia mg ec bh with say_dissolve
    "I expect her to make fun of me, but instead she turns her full attention onto me, only slightly wincing when her character dies."
    am ba me "Of what, the fact that Sayori has a friend?"
    show amelia md with say_dissolve
    mc eg bg mb nb "No, that’d be... ridiculous."
    am ec me "Or of the fact that other people moved on, while you’re stuck reliving those moments?"
    show amelia md with say_dissolve
    "..."
    mc ec mh ba na "..."
    camera master
    show bg:    
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I can’t look her in the eye."
    $ autofocus.unblock("amelia")
    am ed mb bd lup "... I know how it feels. Trust me, I do. You’ve tried to get on with your life, but nothing works. It’s like a loop; every time you think you’re past it, something makes you fall back again."
    am ldown eb bb me "But you have to remember that it’s happened. You’ll never forget what happened, never {i}not{/i} feel guilty for it, but at least come to terms with it. Know that while it did happen, it isn’t the end."
    am mb ba "While you still draw breath, you have the power to make things better."
    am ee "That’s all that matters, right? Righting those wrongs? Making life better, for you and all you care about?"
    show amelia ea ma
    mc ef bb mg "... But that’s the problem, isn’t it?"
    show amelia md
    extend ba ml " I don’t care. Not anymore."
    show amelia ma bd ec rup with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 1.5
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("amelia")
    "She places a hand on my face, drawing my gaze back toward her."
    am mb "You and I both know that’s not true. It was, not so long ago; but you know that's not the case anymore. Sayori and everyone at that club have awakened that back inside you."
    am ea "You’re not a heartless machine, Melody, and you never were. Just a cold, weary traveller, who’s had their heart defrosted."
    show amelia ba md with say_dissolve
    mc eg ml "... And you."
    am me "Hm?"
    show amelia ma with say_dissolve
    mc ea mb "You did, too."
    show amelia rdown with say_dissolve
    "I pull away from her hand, looking her in the face."
    mc bf "Who do you think gave me the strength to try?"
    show amelia eb md with say_dissolve
    mc bg eg "I’m sorry I’ve never said it before, but I owe you a debt I cannot repay, Amelia."
    am ed bd mb "N- No, you owe me nothing, alright? Just being around you is enough for me. You forget, you’re the only one who even looks at me..."
    show amelia ma with say_dissolve
    _mc ec mh ba "For such a long time, I’ve been wanting to ask what it is that she means by that, but I put it off. I wouldn’t dare ruin this moment for her."
    show amelia ee ba with say_dissolve
    "Instead, I ruffle her hair, a smile coming to my face."
    mc mb eg "Thanks, Amelia. I really needed this."
    am ec mb "Hehe, I know. Always happy to help."
    show amelia ea ma with say_dissolve
    mc ef "And... I’m sorry for getting so emotional."
    am ee mf lup bb "Nah, usually it’s me, so... It’s nice having the shoe on the other foot, for once. You’re so stone cold it’s hard to really get you to open up, sometimes."
    show amelia eb ma with say_dissolve
    mc mf "... Yeah."
    am ldown mb "But hey, if it helps? Let’s get something to eat. Food always makes you feel better, right?"
    show amelia ea ba ma with say_dissolve
    mc ea mg "Well, usually. I guess it couldn’t hurt."
    am ed mb "Besides, there’s one game where we both equally suck at."
    show amelia ma with say_dissolve
    mc ed md "Bowling?"
    am ef mb bb "Bowling."
    show amelia ea ba ma with say_dissolve
    "We share a smile, before heading toward the bowling alley."
    _mc ec ma "What a day this turned out to be."

    stop music fadeout 3.0
    scene bg school_street_afternoon
    camera master
    with fade
    $ say_transition = False
    $ autofocus.unblock("amelia")
    $ advance_date(minutes=47)
    $ set_internet(False)

    _mc turned mh "It’s been quite a while since I had the chance to go to an arcade, honestly."
    _mc ef "Even hanging out with Amelia has become less of an occurrence, lately. Don’t get me wrong, she’s probably one of the most genuine people I’ve met in a long time, but..."
    _mc ma "I guess I’ve just not really wanted to be around anyone recently."
    _mc ea mh "Strange, then, how social I’ve been lately. Joining a club, spending more time with Amelia, what next? If I’m not careful, I’ll end up like one of those social kids."
    _mc ec "... Like Kaito."
    _mc eg bi mm "Ugh, perish the thought. Even if I did become more social, I won’t be like him. I’ve got too much pride to stoop to his level."
    _mc ec mh "... That’s all he has, though. Pride. It’s what makes him arrogant, what makes him so difficult to be around."
    _mc ef "Sure, he’s a player, and a cheat, and God-knows-what-else, but... it’s all a mask to hide the child within."
    _mc eg ba "If I didn’t know better, I’d feel a little sorry for him. I do know better though - He deserves all of it."
    _mc ec mh "How cruel can one be, to string people along like that? To cheat on multiple partners at once? I don’t understand how he does it, either."
    _mc ea "For the life of me, I don’t know why people keep trusting him after these things happen."
    _mc eg bi "It blows my mind every time I hear about it, honestly."
    _mc ec ba "... I can’t feel too bad for those stupid enough to believe him; if they’re that gullible, they have it coming."
    _mc ea "Still, it’s far from my problem. Best to just keep on with my own life and problems."

    scene bg residential_afternoon with wipeleft_scene
    $ advance_date(minutes=12)

    _mc turned eg "Finally, time for home. Best to get some rest for tomorrow, I think."
    _mc ec "Amelia invited me out tomorrow afternoon, too, so I think I’ll take her up on that. Nothing better to do."
    
    $ add_calendar_description(calendar_descriptions["natsuki"][0])

    call week_1_thursday_natsuki from _call_week_1_thursday_natsuki
    return