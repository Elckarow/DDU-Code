label week_1_tuesday_common:
    call calendar_transition(day=24, hour=6, minute=15, second=16) from _call_calendar_transition_1
    scene bg mc_bedroom_gray_closed with dissolve_scene_full
    play music childlikesmile

    "As I awaken, I feel a slight pulse of joy within my core."
    "It takes me a few seconds to place it."
    "And when I do, I feel a great rush of happiness and more than a little nervousness."
    _mc turned naked messy nostrands "I’m going to be attending {b}Monika’s{/b} club."

    scene black with wipeleft
    $ advance_date(minutes=75, seconds=22)

    "Whilst I was in the shower, I mulled things over."
    _mc turned bb messy naked nostrands "It’s been something like out of a dream, the past twenty-four hours."
    _mc thinking eg mh ba "How will I fare?"
    _mc ec "I’m definitely not illiterate, but I wouldn’t call myself crazy about English literature, either; more of a 'stick to my own language' kinda gal."
    _mc bi eg ma "Certainly not to the point where I’d normally join a club devoted to the subject."
    _mc ldown mi ef bi "Damn, I can't even say that with a straight face - This coming from the girl who learned Latin for fun?"
    _mc eg ba mh "It'll be fine, though, I'm sure - With any luck, I won’t be subject to too much scrutiny or get asked too many questions."
    _mc ma "By anybody who isn’t Monika, that is."
    _mc ef "I’d be lying if I said I wasn't hoping for a little elucidation from this mysterious 'Rank #1', herself."
    _mc ec mh "And on that note..."
    "I finish my shower, put on a towel and return to my room to change."

    scene bg mc_bedroom_gray_closed with wipeleft
    $ advance_date(minutes=10, seconds=27)

    "... But, I find myself stopping by my mirror, looking at my reflection."
    show cg melody 1 with cg_dissolve
    $ persistent.mc.mark_cg(1)
    _mc turned naked thinking ec mh messy nostrands "What sort of hairdo should I go with today...?"
    _mc eg "I normally don’t worry that much about these sorts of things, but..."
    _mc ma ea "I want to make a good impression for Monika and her club."
    _mc ef mh "Who knows if anyone else is in the club with her?"
    _mc eg bi "This is really just... the first time in a long while that I bothered looking at my reflection while combing out my hair..."
    show cg towel2 with cg_dissolve
    _mc ldown ea mf bb tail "... Is it okay like it is right now, just let down?"
    _mc ef ba ma "I’ve always enjoyed changing up my hairstyle every day. It just gives me a sense of... freedom, or maybe control, that I otherwise lack in my life."
    _mc mh "... But in cases like today, where I’m almost running late to school, such freedom comes to bite me in the rear."
    _mc bi eg mm "I just can’t decide! There’s so many different hairstyles I could go with, each one with their own unique appearance and feel."
    _mc eb mf bb "Like, say, how a ponytail could be seen as a cute hairstyle, letting your hair wrap around you in a soft coil."
    _mc ec ba ma braid "... While a braid exudes a more reserved and caring personality. The care a girl takes in braiding her hair can also be seen in how she treats those around her."
    _mc eb bb bun "... And buns are just the cutest. Or, well... a single bun is more casual, an easy way to keep your hair out of the way."
    _mc eh "But when you form two hair buns, it just turns from casual into ultra cute."
    _mc md bg nb "... I’m really going off on a tangent, aren’t I?"
    _mc ec na ba mh "Just pick a hairstyle and go with it, MC. Come on, it isn’t {b}that{/b} hard."
    "..."
    _mc eg mf "... I guess this one will do..."
    show cg uniform with fastfade
    $ advance_date(minutes=10, seconds=41)
    "Settling on a hairstyle for the day, I finish getting dressed."
    _mc ec ma uniform braid strands "Yeah, this one will do."

    scene bg residential_gray with wipeleft_scene
    $ advance_date(minutes=10, seconds=2)

    "As I sling my bookbag and head out the door, I contemplate what bold new direction my life might perhaps take as of today."

    stop music fadeout 2.8
    scene black with Fade(2.0, 0.5, 1.0)
    play ambient rain_int fadein 3.5
    show monika turned lpoint mb turned zorder 5:
        i11
        alpha 0.0
        easeout_quart 0.8 alpha 1.0
    show white:
        alpha 0.0 
        0.65
        easein 0.12 alpha 1.0
    pause 1.5
    hide monika
    show bg class_2_gray_rain
    hide white
    hide black
    with Dissolve(1.3)
    $ set_date(hour=15, minute=14, second=40)

    "My classes drift by in a haze of words and images of a white ribbon."
    "I look back and forth at the clock."
    "The dismissal bell should ring right about..."
    play sound school_bell
    "Now."
    "A mixture of excitement and nervousness at what’s about to come builds in me."
    _mc turned ec "I’m entering Monika’s domain."
    "I try to calm myself."
    _mc ea mh "Yesterday’s study session with her went well, no? This shouldn’t be too different."

    scene bg school_corridor_2_gray_rain with wipeleft

    "Stepping out of the classroom, I mentally recount the narrative of the book I chose."
    _mc turned bb "I really enjoyed it. I hope I can remember enough to make light conversation."
    "Then it dawns on me that Monika never told me where I was going."
    _mc ef mf "I hope she didn’t do so by design, as a brush-off to ensure we would never meet again."
    _mc mh ba "..."
    _mc eg bi "Oh come on, MC. Stop being silly. She’s a better person than that."
    "I stop and think for a moment."
    "No way I’ll be there on time if I try and find the clubroom randomly."
    "So I figure I’ll stop by the Debate Club and ask."
    "Monika headed it previously; someone there might know something."
    "I know that it’s around here somewhere."
    "D4... D5... D6... here. D7."
    stop music fadeout 2.0
    show bg class_2_gray_rain as stuff with Dissolve(0.2):
        xzoom -1
    "I pop my head around the door."
    mc ea bb mg "Hello, uh... Does anybody here know where the Literature Club meets?"
    show aika turned:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i11
    hide stuff 
    with Dissolve(0.2)
    $ persistent.aika_seen = True
    #TODO Aika theme
    "Only one of the room’s occupants pays me heed."
    "Her long braid sweeps past her shoulders as she turns to face me, and a soft smile breaks across her face."
    "I vaguely recall that she currently runs the Debate Club, but she’s otherwise a stranger to me."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("aika")
    $ say_transition = True
    a mb "Hello! Melody, right?"
    show aika ma with say_dissolve
    mc ml ec bi "I, ah, usually go by MC, but yes. Nice to meet you - you are...?"
    $ aika_name = _("Aika")
    a rhip eb mb "Aika! I head the Debate Club. Difficult act to follow after Monika left, though."
    a rdown ea mf "Speaking of her, you wanted the Literature Club, right?"
    show aika me with say_dissolve
    mc ea ba thinking ml "Yeah, she invited me to attend, but didn’t specify the venue."
    a mf eb "That would be the place that’s short for closure."
    show aika me with say_dissolve
    mc bm ec mf "Pardon?"
    a smug mb ea "Ahah, it’s a riddle whose answer tells you how to get to the Literature Club. Monika came up with that one."
    show aika ma with say_dissolve
    _mc ldown ef bi ma "Oh, that wily Monika."
    mc ea ba ml "Ah... Thanks, I guess."
    "My mind is a whirl as I try to make sense of what she’s just told me."
    "Can’t linger. I’ll have to do my thinking on the move."
    mc mb "I’ve got to dash. Have yourself a nice club session, Aika."
    a turned ec mb "Enjoy yours, too... if you ever find it!"
    show aika ma with None
    hide aika
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ autofocus.unblock("aika")
    $ say_transition = False
    "I hurry along, thoughts racing as fast as my legs are carrying me."
    _mc thinking bi mh eg "Short for closure."
    _mc ba eb "What the heck is that supposed to mean?"
    camera master:
        align (0.45, 0.3) zoom 2.0
    with Dissolve(0.2)
    _mc ea mf "Might this have something to do with D Block?"
    _mc mh ec "They’re going to be temporarily closing that part of the school for renovations pretty soon."
    _mc ldown ma "Worth a try."

    scene bg school_stairs_gray
    camera master
    with wipeleft
    $ advance_date(minutes=4)

    "Tearing down the stairs leading into D Block, I barge into its only classroom currently in use..."
    show bg class_4_gray_rain with Dissolve(0.2)
    "... And receive dirty looks from all those in detention."
    "I beat a hasty retreat."

    scene bg school_stairs_gray with wiperight
    
    _mc turned ec mh "Evidently I was wrong."
    "I take a second to reconsider the riddle and-"
    _mc ea mf "Oh."
    _mc bb mh eb "OH."
    _mc ea ml "Short for closure."
    _mc eb ma "It means shorthand for shutting something down."
    _mc thinking ec mh ba "The keyboard shortcut to shutdown a computer or program is..."
    _mc ea ma "... Alternate-F4."
    _mc ldown eg bi "Oh Monika..."
    _mc bd ea "You tricky, tricky girl."

    scene bg school_corridor_1_gray with wipeleft
    $ advance_date(minutes=3, seconds=31)

    _mc turned bg mj eg "At long last, here we are."
    _mc ec mh ba "Classroom F4."
    "I can hear a familiar voice emanating from within, which confirms the solution beyond all doubt."
    "Taking a moment to compose myself, I knock on the door and enter."

    stop music fadeout 1.0
    scene bg club_gray_rain with wipeleft
    play music okev

    m "MC! You made it! I’m so glad!"
    show monika turned:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    _mc turned eg bb "Ah, MC. It’s nice to hear my nickname again. I feel like too many people have been calling me that old name lately; I hardly..."
    _mc ec bi mh "It reminds me of the witch who gave me that name."
    _mc ea ba "The number of people who remember my real name dwindles with time, thankfully, so it's been less and less of an issue as time's gone on."
    _mc ec ma "Only Amelia has managed to get away with it. Well, people who’ve known me for a while, which really only includes Amelia."
    show monika at t22
    show yuri turned rup b1c e1d mg:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t21
    y "Oh... There’s a fresh face here...!"
    show yuri ma rdown
    _mc thinking ea mf "Oh? That’s Yuri Kuroyanagi from my class, right? Interesting. I didn’t think I’d see her here, though she strikes me as the type to be interested in literature."
    _mc ma "It’s a shame I’ve never really talked to her before; that would have been a fantastic ice-breaker."
    show yuri md b1a at t31
    show monika at t32
    show natsuki turned lhip mi:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t33
    n "Who are you? Nobody said there’d be a new arrival."
    show natsuki mj
    _mc ec mh "She looks strongly familiar, but I can't quite place it. The arm-band represents the-"
    "..."
    "I stand there and gawk."
    "Not so much at the sight of so many pretty girls standing right before me, but at who the last one of them to meet my eyes is."
    mc ldown ea mf nb "S- Sayori...?"
    show natsuki md
    mc bf ml "W- What... I... haven’t..."
    show yuri at t41
    show monika mc at t42
    show natsuki at t43
    show sayori turned mg onlayer above_master:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t44
    s "{size=-6}... Melody?{/size}"
    show natsuki ldown
    show sayori md onlayer above_master

    "Sayori whispers it, completely inaudible, but it’s unmistakable. She said... my name."

    python hide:
        duration = 7.0
        music = add_playback_info(audio.okev_s, get_pos())

        renpy.music.stop(fadeout=duration)
        renpy.music.set_volume(0.5, duration, "ambient")
        renpy.music.play(music, channel="music_poem", fadein=duration, relative_volume=0.5, loop=True)
    
    if preferences.language is None:
        $ auto_advance_date_mult = 0.0
    show sayori b2b

    camera master:
        matrixcolor BrightnessMatrix(0.0) blur 0.0
        linear 7.0 matrixcolor BrightnessMatrix(-0.2) blur 3.0

    camera above_master:
        matrixcolor BrightnessMatrix(0.0)
        linear 7.0 matrixcolor BrightnessMatrix(0.04)

    "Time seems to stand still as we regard one another, and a multitude of emotions churn within me."
    _mc ed mi bg "Sayori, my childhood friend, from whom I drifted apart..."
    _mc ba ea mh na "Could it be fate that has reunited us here?"
    _mc mf "Provided us with an opportunity to reestablish our bond?"
    show sayori ma
    "Her bittersweet expression tugs at my heartstrings, and I can’t help but smile back to reassure her."
    "My happiness at stumbling upon her here is genuine, and I want to show her that."
    show sayori b1a onlayer above_master
    "The gesture seems to work."
    "Even if my smile comes out somewhat clumsily, with my lips drawn way up over my teeth and my gaze being a trifle too fixed."
    show monika ma
    "She breaks into that familiar broad grin, and my worry is dispelled."

    if preferences.language is None:
        $ auto_advance_date_mult = 1.0

    python hide:
        duration = 1.1
        music = add_playback_info(audio.okev, get_pos("music_poem"))

        renpy.music.stop("music_poem", fadeout=duration)
        renpy.music.set_volume(1.0, duration, "ambient")
        renpy.music.play(music, channel="music", fadein=duration, loop=True)
    
    camera master:
        linear 1.1 matrixcolor BrightnessMatrix(0.0) blur 0.0

    camera above_master:
        linear 1.1 matrixcolor BrightnessMatrix(0.0)

    m lpoint md "So the two of you know each other?"
    show monika mc
    mc mb "Yeah, Sayori and I were thick as thieves growing up."
    hide sayori onlayer above_master
    show sayori turned:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i44
    show monika ldown
    s e3d lup rup mb "That’s right! And now that she’s here, things can go back to the way they used to be!"
    show sayori e1b rdown mk nb
    show yuri ma
    m mb "Maybe you could tell us a hilariously awkward story or two about Sayori, then, MC?"
    show monika ma ed
    show sayori tap mb eb ba nb
    show natsuki ma
    n cross mo e3d b3a "Or maybe YOU could tell us a hilariously awkward story or two about her instead, Sayori."
    n e1a mc b1a "She’s definitely the type to embarrass herself."
    show natsuki b1d me
    show monika ea
    show sayori turned e2a me b4 na
    y e2b mb rup "N- Natsuki, we shouldn't be telling any tales but the pulchritudinous ones emitted from our pens..."
    show yuri ma
    show sayori e1b b1d me
    n turned e2a mg "What in the world is that? Pulchri..."
    show yuri e1d md
    show sayori b1a e3d ma
    n e1a mh "... Poultry tude..."
    show natsuki e1d mj
    y rdown e1a mb "Pulchritudinous..."
    show yuri e1d me
    show sayori e1a me
    n cross b3d mi "Ugh, however you say that stupid word! Can’t you cut it out?"
    show natsuki mj
    show monika mc
    y mh rup nb "... But words such as those help show how refined our language is..."
    show yuri e2a mk nc
    show sayori b2a md
    show monika bc
    n e1a mm "Fancy shmancy whatever, you-"
    show yuri shy bc eb
    s mh b2b e3c nb "Guys, that’s enough..."
    show natsuki md b1d
    show sayori mj
    m md "I have to agree. Please, stop."
    show monika mc
    show sayori e1a b2c
    n e2a mm nd "Argh, she started it!"
    show yuri ea md
    "Yuri seems to remember that I’m here, and flusters."
    show sayori e2a
    y turned e3c nb mg rup lup b2b "I- I’m so sorry Natsuki. I shouldn’t have said that."
    show natsuki e1a
    show monika ec
    show sayori ma
    y e2a mb "Now is hardly the time to argue, especially since we have a guest."
    show monika ea 
    show yuri ma
    show natsuki e2c
    "Her pink-haired opposite number, Natsuki, rolls her eyes and exhales audibly."
    show monika ba ma
    show sayori b1b e3c
    n turned lhip rhip e1a mi b1d nb "Oh, alright then. Truce. Hmph."
    show sayori na e1a b1a
    show natsuki mj na
    show monika rdown
    "An awkward silence continues for a moment."
    show yuri e3c
    "Which Yuri then breaks."
    y ldown e1a mb nb b1a "Oh, forgive me for being so rude. Welcome to the Literature Club. MC, was it?"
    show sayori b1a
    show yuri ma na
    show natsuki md 
    mc "Yes, you’re correct."
    y e2a mh "Quite an... interesting name. Would it, perchance, stand for something... like um... initials...?"
    show yuri e1d me
    mc ef ml "Actually yes, but... That’s not really worth discussing at this present moment, I feel..."
    y b3a mg e2a nc "... Of course, yes..."
    show yuri ma nd
    n cross e2a mh "MC? Huh."
    show sayori e3d:
        subpixel True
        easein 0.17 xoffset -40
        easeout 0.17 xoffset 0
    show natsuki:
        subpixel True
        pause 0.16
        "natsuki turned nd e1b mm b3d"
        easein 0.14 xoffset -20
        easeout 0.14 xoffset 0
    "Sayori gives Natsuki a nudge."
    n cross e2a mi nb b1a "Okay, sheesh... Nice to meet you MC, season’s greetings and all that jazz."
    show sayori e1a
    show yuri ma e1a na b1a
    show monika ma
    show natsuki mj
    s lup rup e3d mc "That’s more like it, Nat."
    show sayori ma
    m lpoint mb "Now that Yuri and Natsuki gave their greetings, is there anything else you’d like to tell us about yourself?"
    show monika ldown ma
    show natsuki turned md e2a na
    show sayori e1a rdown
    "I feel an embarrassed blush tinge my cheeks."
    mc ea mg "Well, my name isn’t a mystery to you anymore, so I’ll dispense with that."
    show sayori ldown
    mc thinking ml ec "I’m almost certainly nowhere near as accomplished a writer or as voracious a reader as any of you."
    mc mb ea ldown "But I do have my moments."
    show yuri md
    show natsuki e1a
    mc ef mg bb "I’ve digested some prominent works of literature, along with... well... the odd manga title."
    show monika ed
    mc ec md ba "I do okay at English, or so Monika tells me."
    show monika ea
    show yuri ma
    mc ea mb "And I’m always keen to improve, as well as to get to know everybody here better."
    m mb "Rest assured, we’re all eager to know you better, too."
    show monika ma
    n e2c mh "Manga, huh...? I... guess I might not mind you joining us, after all."
    show natsuki e1a md
    "Hark. Is that a common interest that I detect, which I can use to break the ice with Natsuki further?"
    "I’ll definitely have to get back to that."
    y mb "The same goes for me, MC."
    y e2c mg "The regular classroom setting hasn’t given us much of an opportunity to do that, so perhaps this more um... intimate environment will."
    show sayori e3d
    y shy eb mc "Emmm..."
    "The significance of Yuri’s words dawns upon me as I take them in."
    _mc thinking bb mh "She’s right, you know - come to think of it, we actually DO share the same classes, but we haven’t really interacted much, if at all."
    _mc ef ba ma "Not necessarily surprising, given that she seems a bit of the wallflower type."
    stop music fadeout 1.5
    _mc ldown ec "But maybe that flower will eventually come into full bloom."
    show monika at i11
    show sayori:
        alpha 0.0
    show yuri turned e1a b1a ma na:
        alpha 0.0
    show natsuki ma:
        alpha 0.0
    camera master:  
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True

    play music playwme

    m lpoint ed mb "Right, let’s get down to business, shall we?"
    show sayori e1a
    m ea mb "You’ll find that creative writing, be it of stories or poems, is a staple of our club time, MC."
    m md eb "I’m thinking we’ll do some poetry writing and sharing today, with a bit of a twist."
    m ldown ea mb "We’ll randomise our poems after writing them, and then leave each other to work out who wrote what."
    show natsuki e2a md
    m ed ma "That way, we’ll gain a greater appreciation of each other’s writing styles."
    m ea mb "As well as create an additional get-to-know-you exercise for our new member."
    show monika ma ed with say_dissolve
    mc ea mb "Sounds good to me."
    show monika at i42
    show sayori:
        alpha 1.0
    show yuri:
        alpha 1.0
    show natsuki ma e1a:
        alpha 1.0
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("monika")
    $ say_transition = False
    m ea mb "Wonderful."
    show monika ma
    y e3d lup mb "Perhaps we can settle on a common theme of some kind? It might make things interesting."
    show yuri e1a ma
    s mb lup rup "I like that idea! It’ll save us having to think too much about what to write."
    show natsuki b1c e1d md
    show yuri e2a
    s tap eb mb nb "Or save ME having to think too much about what to write, at any rate. Eheheh."
    m rhip mb "How about we let MC choose the theme? Since she’s the new member."
    show sayori turned e1a ma na
    show monika ma
    show natsuki e1a b1a
    show yuri e1a ldown
    mc mg nb bb eb "... Me?"
    show natsuki ma
    m rdown ed mb "Yes, you. Consider it an honour."
    show monika ma ea
    _mc ea mh ba "So much for not being put on the spot."
    _mc thinking ec mh na "That being said, it would be rude not to accept."
    _mc ef "Plus, this might be my opportunity to shine."
    _mc ldown bb eg ma "Ah, me. The things I do for a fair face."
    show sayori e3d
    mc ea ba mb "It’s an honour I’ll gladly accept, Madame Presidente."
    m ed mb "That’s settled, then!"
    show sayori e1a
    m ea lpoint "We’ll give you a moment to come up with something."
    show monika ldown ma
    n cross mh b1d "Better not be anything weird, you hear?"
    show natsuki md

    show black:
        alpha 0.0
        linear 4.5 alpha 0.6
    camera master:
        matrixcolor BrightnessMatrix(0.0)
        linear 4.5 matrixcolor BrightnessMatrix(-0.1)

    $ renpy.music.set_volume(0.5, 4.5)
    $ renpy.music.set_volume(0.5, 4.5, "ambient")

    "One can practically hear the gears turning in my brain as I rack it for a suitable idea."
    "The feeling of four expectant pairs of eyes upon me isn’t really helping to move things along."
    "Then all of a sudden,"

    show black:
        easeout_quad 0.07 alpha 0.0
    camera master:
        easeout_quad 0.07 matrixcolor BrightnessMatrix(0.6)
        ease_cubic 1.6 matrixcolor BrightnessMatrix(0.0)

    $ renpy.music.set_volume(1.0, 0.5)
    $ renpy.music.set_volume(1.0, 0.5, "ambient")

    extend " a bolt of inspiration comes from right out of the blue."

    stop music fadeout 2.0
    show natsuki turned b1a
    show sayori mj
    show yuri lup e1d mf
    show monika mc
    mc mb "How about we make it rainfall? Or an aquatic theme in general."

    window auto hide

    show yuri:
        pause 1.9
        "yuri turned e1a ma lup"

    show natsuki:
        pause 1.0
        "natsuki turned e1d mj b1d"
        pause 0.3
        "natsuki turned e2a mj"

    show monika ma
    show sayori b2c ma

    pause 4.0
    $ advance_date(seconds=40)

    call blink(0.34) from _call_blink_1
    "I blink once."
    call blink(0.5) from _call_blink_2
    extend " Twice."
    "Are my eyes deceiving me, or does everybody look a tad unenthusiastic now?"
    mc mg "Unless of course you’d rather go for something else, in which case I can give it another-"
    show yuri md e2a
    m bc ec md "No."
    show monika mc
    mc bm mf ed "No?"
    m md ea ba "No, as in you don’t have to suggest an alternative."
    m ec mb "It’s all good, MC. We’ll run with this, won’t we?"
    show monika ea ma at thide
    show sayori me b1a at thide
    show yuri e1d at thide
    show natsuki turned me at thide
    "There is a low murmur of assent from the rest."
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    "And with that, all the girls shuffle off to different desks and get to work."
    _mc thinking ed mh "How odd."
    _mc ec "I wonder what’s gotten into them."
    _mc ldown bb eg ma "Can't wonder for too long, though; it's time for me to get cracking as well."
    _mc mh "..."
    _mc ba eb "Wait..."
    _mc ea bg "Was it too unoriginal?"
    _mc ea ba mb "'Oh, it's raining outside, let's write about rain!'"
    _mc eg bi mm "God dammit, Mel, you dumbass... Way to make a good impression."

    play music okev

    show cg melody 2 with cg_dissolve
    $ persistent.mc.mark_cg(2)
    "As I put pen to paper, I inwardly thank the heavens for the literal brainstorm."
    _mc thinking me ed bd "Sayori was right; having a guiding theme does make things far simpler."
    "The ink flows from the nib as I move it across the blank surface, like droplets forming a river..."
    "... Which then meanders its way into the sea."
    "Slowly but surely, my poem takes shape along similar lines."

    $ show_poem(mc_poem_2)
    # for those skipping
    # resets the camera since it bugs out when the light effect above happens
    camera master

    hide cg with cg_dissolve
    _mc ma ldown ba ec "I reckon it’s alright, even if I do say so myself."
    _mc ea "Hopefully, the others share the same opinion."
    _mc ef "Well, at least one of them in particular, whom my gaze presently drifts over to."

    play music_poem add_playback_info(getattr(audio, "okev_" + branches.to_doki(branches.get_current())[0]), get_pos()) fadein 2.0
    stop music fadeout 2.0
    call expression "week_1_tuesday_%s_1" % branches.to_doki(branches.get_current()) from _call_expression
    play music add_playback_info(audio.okev, get_pos("music_poem")) fadein 2.0
    stop music_poem fadeout 2.0

    show monika turned ea mb ba lpoint na:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    m "How are we all doing?"
    show monika ma
    mc ea ba ml na ldown "I’m done with mine."
    show monika ldown at t21
    show sayori turned mb:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t22
    s "Same here."
    show monika at t31
    show sayori ma at t32
    show natsuki turned e2a mh:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t33
    n "Nothing to it."
    show yuri turned e3c mh b1d:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t41
    show monika at t42
    show sayori at t43
    show natsuki md at t44
    y "Not my finest effort, but I think I did adequately given the constraints I set for myself."
    show yuri e1a b1a ma at thide
    m ec mb rhip "I swear, I have the best club members."
    m md "So sporting. So talented."
    m ea mb rdown "Alright, let’s divvy our poems up and start guessing who’s written them!"
    show monika ma at thide
    show sayori at thide
    show natsuki at thide
    hide yuri
    hide monika
    hide sayori
    hide natsuki
    "With that, she collects our sheets of verse."
    "Carefully folding them to keep their contents concealed, she shuffles them once, twice, thrice..."
    "Before handing them back to us at random."
    $ renpy.set_tag_attributes("melody ma")
    "I unfurl and carefully scrutinise what I’ve received."
    "Who might its creator be?"

    python:
        renpy.music.set_volume(0.5, 3.0, "ambient")
        show_poem(renpy.random.choice([sayori_poem_1, natsuki_poem_1, monika_poem_1, yuri_poem_1]), music=False)
        guess("natsuki", "monika", "yuri", "sayori")
        renpy.music.set_volume(1.0, 2.0, "ambient")
        advance_date(minutes=2, seconds=27)

    call expression "week_1_tuesday_%s_%s" % (poem_last_author, "right" if guessed() else "wrong") from _call_expression_1

    stop ambient fadeout 2.0
    stop music fadeout 2.0
    scene bg club_afternoon with longfade
    play music daijoubu
    $ set_date(hour=16, minute=8, second=34)

    "The rain comes to an end..."
    "... And with it, the poetry game."
    "It’s a testament to the girls’ experience as literature aficionados that they managed to correctly identify my poem almost right off the bat."
    "Sure, their reception towards my writing itself is favourable on the whole, and I’m grateful for that..."
    show monika turned mb mb:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    m "Every bit as good as what you showed me yesterday. Poetry AND storytelling - quite the all rounder, aren’t you?"
    show monika ma at t22
    show yuri turned lup e3c mb:
        matrixcolor TintMatrix("#f1d6bb")
        t21
    y "New horizons, fresh vistas, full of exciting possibilities... Themes that make for an inspired piece."
    show yuri e1a ma at t31
    show monika at t32
    show sayori turned lup rup e3d mb:
        matrixcolor TintMatrix("#f1d6bb")
        t33
    s "Looks like you’ve found your voice as an author too, Melly! I’m so glad!"
    show yuri at t41
    show monika at t42
    show sayori ma at t43
    show natsuki turned e2c mh:
        matrixcolor TintMatrix("#f1d6bb")
        t44
    n "It’s not bad, I guess. Could be a little lighter on the fancy-schmancy wordplay, but otherwise not bad."
    show natsuki md
    _mc turned eb mh "... But their ability to pick me out just like that, as well as their nuanced critiques, leaves me humbled."
    _mc ed ma "If I can eventually become half as good as them in those departments, perhaps I’ll be able to properly fit in and call myself a worthy member."
    _mc ec mh "Perhaps."
    _mc ea "But regardless..."
    show monika ec
    "Monika appears to have something else in store for us now, so I prick my ears up and pay attention."
    show monika at i11
    hide sayori
    hide natsuki
    hide yuri
    camera master:  
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    m ea lpoint mb "That was a fun little diversion, wasn’t it?"
    m ed "Now that we’ve all exercised our brain cells for today, how about we kick back and unwind with a bit of free reading?"
    show monika ma with None
    hide monika
    show yuri turned lup e3c b1d:
        matrixcolor TintMatrix("#f1d6bb")
        i31
        xoffset 100
    show sayori turned e3d:
        matrixcolor TintMatrix("#f1d6bb")
        i32
    show natsuki turned e3c:
        matrixcolor TintMatrix("#f1d6bb")
        i33
        xoffset -100
    camera master:
        zoom 1.2
    show bg:
        blur 1.0
    with Dissolve(0.2)
    $ autofocus.unblock("monika")
    $ say_transition = False
    "The others collectively nod, and I’m more than amenable myself."
    hide natsuki
    hide yuri
    hide sayori
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    "Everyone moves off to their own sections of the club room."
    $ renpy.set_tag_attributes("melody na ba ma ea ldown")

    call expression "week_1_tuesday_%s_2" % branches.to_doki(branches.get_current()) from _call_expression_2

    if not is_playing(audio.daijoubu):
        stop music fadeout 1.0
    
    $ autofocus.unblock("monika")
    $ autofocus.unblock("sayori")

    show monika turned lpoint ea na ba mb:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    m "Okay, everyone!"

    if not is_playing(audio.daijoubu):
        play music daijoubu

    show monika ma at t42
    show yuri turned:
        matrixcolor TintMatrix("#f1d6bb")
        t41
    show natsuki turned:
        matrixcolor TintMatrix("#f1d6bb")
        t43
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        t44
    "Everyone’s attention is brought to Monika."
    m mb "Club time is about to come to a close. Has everyone had fun today?"
    show monika ma ldown
    y mb rup "Reading is always a pleasing experience, so I would have to say yes."
    show yuri ma
    show sayori e1b mf b1d
    n mc "Yep. I’m looking forward to tomorrow."
    show natsuki ma
    show yuri e3d
    s lup rup b1a mh e1b "Oooh! What’ll we do next club meeting?"
    show sayori mf b1d
    m mb ec rhip "Now, now, Sayori... That’s a question for tomorrow."
    show monika ed ma
    s tap eb mb "Aww..."
    show sayori ea
    show yuri e1a
    m rdown ea mb "That said, if everyone’s satisfied, we can conclude today’s meeting."
    show monika ma
    show sayori turned e3d ma at dip
    show yuri rdown at dip
    show natsuki at dip
    "Everyone gives a collective series of nods,"
    show monika at thide
    show sayori e1a at thide
    show yuri lup e2a b3a at thide
    show natsuki e2c mj at thide
    extend " begins packing up their bags,"
    hide monika
    hide sayori
    hide yuri
    hide natsuki
    extend " and leaving the clubroom."
    m turned lpoint md "Oh, MC?"
    show monika mc:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    show bg class_2_afternoon
    with NonBlockingDissolve(0.2)
    "I pause, halfway out the door. Monika’s behind the teacher’s podium, cleaning up the rest of the club’s materials."
    mc ea ml ldown na ba "... Yes, Monika?"
    m ldown mb "Now that you've visited us today and officially become a member of our club, I'll be adding you to our group chat!"
    m md eb rhip "It might take a little while though, since..."
    show monika mc ea
    mc mb "Extracurriculars and stuff like that, right? I get it. I'll keep my eyes out!"
    show monika ma ec rdown at dip
    "Monika nods her head, relieved at having not to explain herself further."
    m mb ea "Take care!"
    show monika ma ed
    "She smiles and waves. I return her gesture and leave the club room."

    $ add_calendar_description(calendar_descriptions[None][1])

    return