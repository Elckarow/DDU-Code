label week_1_tuesday_common:
    $ day = _("Tuesday")
    stop music fadeout 2.0
    scene bg mc_bedroom_rain_open with dissolve_scene_full
    play music okev

    "As I awaken, I feel a slight pulse of joy within my core."
    "It takes me a few seconds to place it."
    "And when I do, I feel a great rush of happiness and more than a little nervousness."
    "{i}I’m going to be attending {b}Monika’s{/b} club.{/i}"

    scene black with wipeleft

    "Whilst I was in the shower, I mulled things over."
    "{i}It’s been something like out of a dream, the past twenty-four hours.{/i}"
    "{i}How will I fare?{/i}"
    "{i}I’m definitely not illiterate, but I wouldn’t call myself crazy about literature, either.{/i}"
    "{i}Certainly not to the point where I’d normally join a club devoted to the subject.{/i}"
    "{i}With any luck, I won’t be subject to too much scrutiny or get asked too many questions.{/i}"
    "{i}By anybody who isn’t Monika, that is.{/i}"
    "{i}I’m hoping for a little attention from this Madame Presidente, herself.{/i}"
    "{i}And on that note...{/i}"
    "I finish my shower, put on a towel and return to my room to change."

    scene bg mc_bedroom_rain_open with wipeleft

    "... But, I find myself stopping by my mirror, looking at my reflection."

    show cg melody 1 at CG
    $ persistent.mc.mark_cg(1)

    "{i}What sort of hairdo should I go with today...?{/i}"
    "{i}I normally don’t worry that much about these sorts of things, but...{/i}"
    "{i}I want to make a good impression for Monika and her club.{/i}"
    "{i}Who knows if anyone else is in the club with her?{/i}"
    "{i}This is really just... The first time in a long while that I bothered looking at my reflection while combing out my hair...{/i}"
    show cg towel2 with cg_dissolve
    "{i}... Is it okay like it is right now, just let down?{/i}"
    "{i}I’ve always enjoyed changing up my hairstyle every day. It just gives me a sense of... Freedom, or maybe control, that I otherwise lack in my life.{/i}"
    "{i}... But in cases like today, where I’m almost running late to school, such freedom comes to bite me in the rear.{/i}"
    "{i}I just can’t decide! There’s so many different hairstyles I could go with, each one with their own unique appearance and feel.{/i}"
    "{i}Like, say, how a ponytail could be seen as a cute hairstyle, letting your hair wrap around you in a soft coil.{/i}"
    "{i}... While a braid exudes a more reserved and caring personality. The care a girl takes in braiding her hair can also be seen in how she treats those around her.{/i}"
    "{i}... And buns are just the cutest. Or, well... A single bun is more casual, an easy way to keep your hair out of the way.{/i}"
    "{i}But when you form two hair buns, it just turns from casual into ultra cute.{/i}"
    "{i}... I’m really going off on a tangent, aren’t I?{/i}"
    "{i}Just pick a hairstyle and go with it, Melody. Come on, it isn’t {b}that{/b} hard.{/i}"
    "..."
    "{i}... I guess this one will do...{/i}"
    show cg uniform with cg_dissolve
    "Settling on a hairstyle for the day, I finish getting dressed."
    "..."
    "{i}Yeah, this one will do.{/i}"

    stop music fadeout 2.5
    scene bg residential_gray with wipeleft

    "As I sling my bookbag and head out the door, I contemplate what bold new direction my life might perhaps take as of today."


    scene bg class_gray with wipeleft_scene
    play ambient rain_int fadein 2.0

    "My classes drift by in a haze of words and images of a white ribbon."
    "I look back and forth at the clock."
    "The dismissal bell should ring right about..."

    play sound schoolbell

    "Now."

    play music daijoubu

    "A mixture of excitement and nervousness at what’s about to come builds in me."
    "{i}I’m entering Monika’s domain.{/i}"
    "I try to calm myself."
    "{i}Yesterday’s study session with her went well, no? This shouldn’t be too different.{/i}"

    scene bg school_corridor_gray with wipeleft

    "Stepping out of the classroom, I mentally recount the narrative of the book I chose."
    "{i}I really enjoyed it. I hope I can remember enough to make light conversation.{/i}"
    "Then it dawns on me that Monika never told me where I was going."
    "{i}I hope she didn’t do so by design, as a brush-off to ensure we would never meet again.{/i}"
    "{i}...{/i}"
    "{i}Oh come on, MC. Stop being silly. She’s a better person than that.{/i}"
    "I stop and think for a moment."
    "No way I’ll be there on time if I try and find the clubroom randomly."
    "So I figure I’ll stop by the Debate Club and ask."
    "Monika headed it previously; someone there might know something."
    "I know that it’s around here somewhere."
    "E4... E5... E6... here. E7."
    "I pop my head around the door."
    mc "Hello, uh... Does anybody here know where the Literature Club meets?"
    show aika turned gray at t11
    "Only one of the room’s occupants pays me heed."
    "Her long braid sweeps past her shoulders as she turns to face me, and a soft smile breaks across her face."
    "I vaguely recall that she currently runs the Debate Club, but she’s otherwise a stranger to me."

    a mb "Hello! Melody, right?"
    show aika ma
    mc "I usually go by MC, but yes. Nice to meet you - you are...?"
    $ aika_name = "Aika"
    a rhip eb mb "Aika! I head the Debate Club. Difficult act to follow after Monika left, though."
    a rdown ea mf "Speaking of her, you wanted the Literature Club, right?"
    show aika me
    mc "Yeah, she invited me to attend, but didn’t specify the venue."
    a mf eb "That would be the place that’s short for closure."
    show aika me
    mc "Pardon?"
    a smug mb ea "Ahah, it’s a riddle whose answer tells you how to get to the Literature Club. Monika came up with that one."
    show aika ma
    "{i}Oh, that wily Monika.{/i}"
    mc "Ah... Thanks, I guess."
    "My mind is a whirl as I try to make sense of what she’s just told me."
    "Can’t linger. I’ll have to do my thinking on the move."
    mc "I’ve got to dash. Have yourself a nice club session, Aika."
    a turned ec mb "Enjoy yours, too... if you ever find it!"
    show aika ma at thide
    hide aika
    "I hurry along, thoughts racing as fast as my legs are carrying me."
    "{i}Short for closure.{/i}"
    "{i}What the heck is that supposed to mean?{/i}"
    "{i}Might this have something to do with E Block?{/i}"
    "{i}They’re going to be temporarily closing that part of the school for renovations pretty soon.{/i}"
    "{i}Worth a try.{/i}"

    scene bg school_stairs_gray with wipeleft

    "Tearing down the stairs leading into E Block, I barge into its only classroom currently in use..."
    "... And receive dirty looks from all those in detention."
    "I beat a hasty retreat."
    "{i}Evidently I was wrong.{/i}"
    "I take a second to reconsider the riddle and-"
    "{i}Oh.{/i}"
    "{i}OH.{/i}"
    "{i}Short for closure.{/i}"
    "{i}It means shorthand for shutting something down.{/i}"
    "{i}The keyboard shortcut to shutdown a computer or program is...{/i}"
    "{i}... Alternate-F4.{/i}"
    "{i}Oh Monika...{/i}"
    "{i}You tricky, tricky girl.{/i}"

    scene bg school_corridor_gray with wipeleft

    "{i}At long last, here we are.{/i}"
    "{i}Classroom F4.{/i}"
    "I can hear a familiar voice emanating from within, which confirms the solution beyond all doubt."
    "Taking a moment to compose myself, I knock on the door and enter."

    stop music fadeout 0.8
    scene bg club_gray with wipeleft
    play music okev


    m "MC! You made it! I’m so glad!"
    show monika turned gray at t11
    "{i}Ah, MC. It’s nice to hear my nickname again. I feel like too many people have been calling me Melody lately...I don’t care all that much, but...{/i}"
    "{i}It reminds me of the witch who gave me that name.{/i}"
    "{i}Besides, there aren’t too many people who even remember my real name these days, so it’s not that much of an issue anymore.{/i}"
    "{i}Only Amelia has gotten away with it. Well, people who’ve known me for a while, which really only includes Amelia.{/i}"
    show monika at t22
    show yuri turned gray rup b1c e1d mg at t21
    y "Oh... There’s a fresh face here...!"
    show yuri ma rdown
    "{i}Oh? That’s Yuri from my form class, right? Interesting. I didn’t think I’d see her here. Though she strikes me as the type to be interested in literature.{/i}"
    "{i}It’s a shame I’ve never really talked to her before.{/i}"
    show yuri md b1a at t31
    show monika at t32
    show natsuki turned gray lhip mi at t33
    n "Who are you? Nobody said there’d be a new arrival."
    show natsuki mj
    "I stand there and gawk."
    "Not so much at the sight of so many pretty girls standing right before me, but at who the last one of them to meet my eyes is."
    mc "S- Sayori...?"
    show natsuki md
    mc "W- What... I... haven’t..."
    show yuri at t41
    show monika mc at t42
    show natsuki at t43
    show sayori turned gray mg at t44
    s "{size=-6}... Melody?{/size}"
    show natsuki ldown
    show sayori md


    "Sayori whispers it, completely inaudible, but it’s unmistakable. She said... My name."

    python hide:
        duration = 7.0
        music = format_music_string(audio.okev_s, get_pos())
        relative_volume = 0.5

        renpy.music.stop(fadeout=duration)
        renpy.music.set_volume(0.5, duration, "ambient")
        renpy.music.play(music, channel="music_poem", fadein=duration, relative_volume=relative_volume, loop=True)
        focus_tag("sayori", -0.32, 3.5, duration)
        renpy.show("sayori", at_list=[focus(0.0, 0.1, 0.0, 0.0, duration)])

    "Time seems to stand still as we regard one another, and a multitude of emotions churn within me."
    "{i}Sayori, my childhood friend, from whom I drifted apart...{/i}"
    "{i}Could it be fate that has reunited us here?{/i}"
    "{i}Provided us with an opportunity to reestablish our bond?{/i}"
    "Her bittersweet expression tugs at my heartstrings, and I can’t help but smile back to reassure her."
    "My happiness at stumbling upon her here is genuine, and I want to show her that."
    show sayori ma
    "The gesture seems to work."
    "Even if my smile comes out somewhat clumsily, with my lips drawn way up over my teeth and my gaze being a trifle too fixed."
    show monika ma
    "She breaks into that familiar broad grin, and my worry is dispelled."

    python hide:
        duration = 1.4
        music = format_music_string(audio.okev, get_pos("music_poem"))

        renpy.music.stop("music_poem", fadeout=duration)
        renpy.music.set_volume(1.0, duration, "ambient")
        renpy.music.play(music, channel="music", fadein=duration, loop=True)
        unfocus_tag("sayori", -0.32, 3.5, duration)
        renpy.show("sayori", at_list=[focus(0.1, 0.0, 0.0, 0.0, duration)])

    m lpoint md "So the two of you know each other?"
    show monika mc
    mc "Yeah, Sayori and I were thick as thieves growing up."
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
    y e2a mh "Quite an... Interesting name. Would it, perchance, stand for something... Like um... Initials...?"
    show yuri e1d me
    mc "Actually yes, but... That’s not really worth discussing at this present moment, I feel..."
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
        "natsuki turned gray nd e1b mm b3d"
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
    "I feel a blush tinge my cheeks."
    mc "Well, my name isn’t a mystery to you anymore, so I’ll dispense with that."
    show sayori ldown
    mc "I’m almost certainly nowhere near as accomplished a writer or as voracious a reader as any of you."
    mc "But I do have my moments."
    show yuri md
    show natsuki e1a
    mc "I’ve digested some prominent works of literature, along with... Well... The odd manga title."
    show monika ed
    mc "I do okay at English, or so Monika tells me."
    show monika ea
    show yuri ma
    mc "And I’m always keen to improve, as well as to get to know everybody here better."
    m mb "Rest assured, we’re all eager to know you better, too."
    show monika ma
    n e2c mh "Manga, huh...? I... Guess I might not mind you joining us, after all."
    show natsuki e1a md
    "Hark. Is that a common interest that I detect, which I can use to break the ice with Natsuki further?"
    "I’ll definitely have to get back to that."
    y mb "The same goes for me, MC."
    y e2c mg "The regular classroom setting hasn’t given us much of an opportunity to do that, so perhaps this more um... Intimate environment will."
    show sayori e3d
    y shy eb mc "Emmm..."
    "The significance of Yuri’s words dawns upon me as I take them in."
    "{i}She’s right, you know - come to think of it, we actually DO share the same classes, but we haven’t really interacted much, if at all.{/i}"
    "{i}Not necessarily surprising, given that she seems a bit of the wallflower type.{/i}"

    stop music fadeout 1.0

    "{i}But maybe that flower will eventually come into full bloom.{/i}"

    play music playwme

    show yuri turned e1a b1a ma na
    show natsuki ma
    m lpoint ed mb "Right, let’s get down to business, shall we?"
    show sayori e1a
    m ea mb "You’ll find that creative writing, be it of stories or poems, is a staple of our club time, MC."
    m md eb "I’m thinking we’ll do some poetry writing and sharing today, with a bit of a twist."
    m ldown ea mb "We’ll randomise our poems after writing them, and then leave each other to work out who wrote what."
    show natsuki e2a md
    m ed ma "That way, we’ll gain a greater appreciation of each other’s writing styles."
    m ea mb "As well as create an additional get-to-know-you exercise for our new member."
    show monika ma ed
    mc "Sounds good to me."
    show natsuki ma e1a
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
    mc "... Me?"
    show natsuki ma
    m rdown ed mb "Yes, you. Consider it an honour."
    show monika ma ea
    "{i}So much for not being put on the spot.{/i}"
    "{i}That being said, it would be rude not to accept.{/i}"
    "{i}Plus, this might be my opportunity to shine.{/i}"
    "{i}Ah, me. The things I do for a fair face.{/i}"
    show sayori e3d
    mc "It’s an honour I’ll gladly accept, Madame Presidente."
    m ed mb "That’s settled, then!"
    show sayori e1a
    m ea lpoint "We’ll give you a moment to come up with something."
    show monika ldown ma
    n cross mh b3d "Better not be anything weird, you hear?"
    show natsuki md

    camera master:
        matrixcolor BrightnessMatrix(0.0)
        linear 4.5 matrixcolor BrightnessMatrix(-0.3)

    $ renpy.music.set_volume(0.5, 4.5)
    $ renpy.music.set_volume(0.5, 4.5, "ambient")

    "One can practically hear the gears turning in my brain as I rack it for a suitable idea."
    "The feeling of four expectant pairs of eyes upon me isn’t really helping to move things along."
    "Then all of a sudden,"

    camera master:
        matrixcolor BrightnessMatrix(-0.3)
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
    mc "How about we make it rainfall? Or an aquatic theme in general."

    window hide

    show yuri:
        pause 1.9
        "yuri turned gray e1a ma lup"

    show natsuki:
        pause 1.0
        "natsuki turned gray e1d mj b1d"
        pause 0.5
        "natsuki turned gray e2a mj"

    show monika ma
    show sayori b2c ma

    pause 4.0
    window auto

    show blink
    "I blink once."
    show blink
    extend " Twice."
    hide blink
    "Are my eyes deceiving me, or does everybody look a tad unenthusiastic now?"
    mc "Unless of course you’d rather go for something else, in which case I can give it another-"
    show yuri md e2a
    m bc ec md "No."
    show monika mc
    mc "No?"
    m ma ea ba "No, as in you don’t have to suggest an alternative."
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
    "..."
    "{i}How odd.{/i}"
    "{i}I wonder what’s gotten into them.{/i}"
    show cg melody 2 at CG

    $ persistent.mc.mark_cg(2)

    "As I put pen to paper, I inwardly thank the heavens for the literal brainstorm."
    "{i}Sayori was right; having a guiding theme does make things far simpler.{/i}"
    "The ink flows from the nib as I move it across the blank surface, like droplets forming a river..."
    "... Which then meanders its way into the sea."
    "Slowly but surely, my poem takes shape along similar lines."

    $ show_poem(mc_poem_2)

    hide cg
    play music playwme
    "{i}I reckon it’s alright, even if I do say so myself.{/i}"
    "{i}Hopefully, the others share the same opinion.{/i}"
    "{i}Well, at least one of them in particular, whom my gaze presently drifts over to.{/i}"

    call expression "week_1_tuesday_%s_1" % route from _call_expression

    show monika turned gray ea mb ba lpoint na at t11
    m "How are we all doing?"
    show monika ma
    mc "I’m done with mine."
    show monika ldown at t21
    show sayori turned gray mb at t22
    s "Same here."
    show monika at t31
    show sayori ma at t32
    show natsuki turned gray e2a mh at t33
    n "Nothing to it."
    show yuri turned gray e3c mh b1d at t41
    show monika at t42
    show sayori at t43
    show natsuki md at t44
    y "Not my finest effort, but I think I did adequately given the constraints I set for myself."
    show yuri e1a b1a ma at thide
    m ec mb rhip "I swear, I have the best club members."
    m ma "So sporting. So talented."
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
    "I unfurl and carefully scrutinise what I’ve received."
    "Who might its creator be?"

    python:
        renpy.music.set_volume(0.5, 3.0, "ambient")
        show_poem(renpy.random.choice([sayori_poem_1, natsuki_poem_1, monika_poem_1, yuri_poem_1]), music=False)
        guess("natsuki", "monika", "yuri", "sayori")
        renpy.music.set_volume(1.0, 2.0, "ambient")

    call expression "week_1_tuesday_%s_%s" % (poem_last_author, "right" if guessed() else "wrong") from _call_expression_1

    stop ambient fadeout 1.0
    stop music fadeout 1.0
    scene bg club_afternoon with wipeleft_scene
    play music daijoubu

    "The rain comes to an end..."
    "... And with it, the poetry game."
    "It’s a testament to the girls’ experience as literature aficionados that they managed to correctly identify my poem almost right off the bat."
    "Sure, their reception towards my writing itself is favourable on the whole, and I’m grateful for that..."
    show monika turned mb afternoon mb at t11
    m "Every bit as good as what you showed me yesterday. Poetry AND storytelling - quite the all rounder, aren’t you?"
    show monika ma at t22
    show yuri turned afternoon lup e3c mb at t21
    y "New horizons, fresh vistas, full of exciting possibilities... Themes that make for an inspired piece."
    show yuri e1a ma at t31
    show monika at t32
    show sayori turned afternoon lup rup e3d mb at t33
    s "Looks like you’ve found your voice as an author too, Melody! I’m so glad!"
    show yuri at t41
    show monika at t42
    show sayori ma at t43
    show natsuki turned afternoon e2c mh at t44
    n "It’s not bad, I guess. Could be a little lighter on the fancy-schmancy wordplay, but otherwise not bad."
    show natsuki md
    "{i}... But their ability to pick me out just like that, as well as their nuanced critiques, leaves me humbled.{/i}"
    "{i}If I can eventually become half as good as them in those departments, perhaps I’ll be able to properly fit in and call myself a worthy member.{/i}"
    "{i}Perhaps.{/i}"
    "{i}But regardless...{/i}"
    show monika ec
    "Monika appears to have something else in store for us now, so I prick my ears up and pay attention."
    show natsuki e1a ma
    show sayori e1a ldown rdown
    show yuri ldown
    m ea lpoint mb "That was a fun little diversion, wasn’t it?"
    m ed "Now that we’ve all exercised our brain cells for today, how about we kick back and unwind with a bit of free reading?"
    show monika ma
    show yuri at dip
    show sayori e3d at dip
    show natsuki at dip
    "The others collectively nod, and I’m more than amenable myself."
    show monika at thide
    show sayori at thide
    show natsuki at thide
    show yuri at thide
    hide monika
    hide sayori
    hide natsuki
    hide yuri
    "Everyone moves off to their own sections of the club room."

    call expression "week_1_tuesday_%s_2" % route from _call_expression_2

    if not is_playing(audio.daijoubu):
        stop music fadeout 1.0

    show monika turned afternoon lpoint ea na ba mb at t11
    m "Okay, everyone!"

    if not is_playing(audio.daijoubu):
        play music daijoubu

    show monika ma at t42
    show yuri turned afternoon at t41
    show natsuki turned afternoon at t43
    show sayori turned afternoon at t44
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
    m "Oh, MC?"
    show monika turned afternoon mc at t11
    "I pause, halfway out the door. Monika’s behind the teacher’s podium, cleaning up the rest of the club’s materials."
    mc "... Yes, Monika?"
    m mb "Take care!"
    show monika ma ed
    "Monika smiles and waves. I return her gesture and leave the club room."

    stop music fadeout 2.0
    return
