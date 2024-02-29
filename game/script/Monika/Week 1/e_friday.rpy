label week_1_friday_monika:
    call calendar_transition(day=27, hour=6, minute=32) from _call_calendar_transition_4
    scene black with Dissolve(1.0)
    scene bg mc_bedroom_day_closed
    camera master:
        blur 5.0
    with mc_pov(True)
    $ set_pov("mc")
    $ set_internet(True)
    play music ohayou

    "I wake with a start."
    "My limbs feel weak, but I smile at the good dream I’ve woken from."
    _mc turned naked nostrands messy ec "Morpheus was kind."
    call blink(2.0) from _call_blink_5
    "I slowly rise from my bed, and spend a moment to brush the powder from my eyes. The club flits through my mind and my smile grows ever wider."
    _mc ea mh "What will we do today, I wonder?"
    _mc ma "And how is Monika?"
    "I build my own story in answer, daydreaming through the morning, right until I’m halfway up the road."

    scene bg residential_day with wipeleft_scene
    $ set_date(hour=7, minute=50)
    $ set_internet(False)

    s turned e3d mb "Heyya!"
    show sayori e1a ma  at t11
    "I turn and grin."
    s mb "Can I walk with you?"
    show sayori md
    mc turned mb "No."
    s tap eb bc ma "Well, I’m walking behind you then."
    show sayori ea 
    mc ef mg "Then I guess I very well can’t stop you, can I?"
    show sayori turned lup e3d
    "I jog back to her and she grabs my hand."
    show sayori ldown mb e1a
    "She pulls me into her playful skip towards school, and I can’t help laughing at her obvious joy."
    show sayori ma
    _mc ea ma "So oddly innocent."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:    
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc mb "So, Miss Katsuragi, what are you doing today?" 
    s mb e1b "Ooh, yeah. Arts club after school."
    show sayori e1a md with say_dissolve
    mc ed md "Does Monika know you’re cheating on her?"
    s mh "Oh, yeah. She said I could."
    show sayori ma with say_dissolve
    mc ml ea "Well, I might just join you, then."
    s e3d mb "Ooh, yeah!"
    show sayori ma with say_dissolve
    mc mb "Great, it’s settled."
    show sayori e1a me with say_dissolve
    mc mg thinking "Is Natsuki coming too?"
    show sayori e3d mn with say_dissolve
    n cross e1d b1d mb "Why? Do you want to paint me like one of your French girls?"
    hide sayori 
    show natsuki e1a ma at i11
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("sayori")
    "I jump and turn."
    n e2a b1a mh "Nice to see you too, weirdo."
    show natsuki turned mc e1a b3a at t21
    show sayori turned at t22
    n "Hello, Sayori."
    show natsuki ma
    s e3d mc "Yay! Hi!"
    show sayori lup rup ma:
        subpixel True
        ease_cubic 0.2 xoffset -250.0
    show natsuki:
        subpixel True
        pause 0.17
        "natsuki turned e3d b3a"
    "Sayori runs and hugs her." 
    s rdown e1a mb "How are you?"
    show sayori ma zorder 4
    n mh e1a "Good, thank you. Though I’ve recently learned I’ll be accompanied to the art club."
    show sayori me
    n e1d b1d mi lhip rhip "Which upsets me, Melody can keep her stick-men to herself."
    show natsuki md
    show sayori md ldown:
        subpixel True
        easein 0.2 xoffset 0.0
    mc ldown "I’ll have you know I can draw, actually."
    show sayori ma zorder 2
    show natsuki ldown rdown e1a b3a
    mc md ed "Better than you, Miss Manga, I’d wager."
    n cross e3c mi "Please, do, I could use some change."
    show natsuki e1d b1a ma
    mc "You’re on, then."
    show natsuki turned e1d b1d at dip 
    show sayori me
    "She extends her hand and I take it."
    show sayori e1d b1d ma
    "Sayori’s grinning mischievously."
    show natsuki b3a me e1a
    s e1a b1a mb "Can I join in?"
    show sayori ma
    n cross b1d mc "Sure. How much would you both like to bet?"
    show natsuki b1a me
    s e1a b1a mb "How about one-thousand-five-hundred yen?"
    show sayori ma
    n turned b3a mh "Oh, er. Sure."
    show natsuki ma e2a b1a
    show sayori e3d
    "I glance over at Natsuki, surprised by her response."
    _mc ec mh "She’s clearly uncomfortable with the amount."
    _mc "She clearly won’t say anything, though."
    _mc ea "But - I certainly will."
    show natsuki me e1a b3a
    show sayori e1a md
    mc mg "Mind making that seven-hundred-fifty? Hours haven’t been too good this month."
    s lup mb "Oh, sure. No worries~"
    show sayori e3d ma
    show natsuki ma b1a at dip
    "Natsuki silently bumps my shoulder and we continue walking, banter continuing."
    show sayori ldown e1a
    n b3a mh "So, Sayori, I heard you tried to join the cooking club?"
    show natsuki ma
    s b1d e1d mh "And, uh, what’s so funny about that?"
    show sayori md
    show natsuki b2a e1b mn
    mc ed md "Oh, I don’t know, the idea of you cooking."
    show sayori lup rup xd ml b1a at hop
    s "Hey!"
    show sayori e2a b1d md ldown rdown nb
    show natsuki b3a e3d ma
    mc "What, like you {i}wouldn’t{/i} burn the school down?"
    show natsuki e1a
    s mg "Like you’d complain?"
    show sayori md
    n cross e3c mi "Unlike you, we concentrate."
    show natsuki b1a e1a ma 
    s e1a mi "I concentrate!"
    show sayori mj
    mc "-On food."
    n turned lhip mc b3a "Mind you don’t cut yourself on that tongue, Melody."
    n e1d b1d mb "Sayori’s not {b}that{/b} bad~"
    show natsuki:
        on hide:
            subpixel True
            "natsuki turned b3a"
            ease_quad 0.4 xoffset 250.0
            "natsuki turned b3a e3d me"
            hop()
            "natsuki turned b3a e2a"
            ease 0.4 xoffset -1000.0
    show sayori:
        pause 0.125
        "sayori turned me"
        pause 0.34
        "sayori turned e1b md"
        pause 0.07
        "sayori turned e3d"
    hide natsuki
    "Natsuki brushes past me, pecks Sayori on the cheek, and starts jogging ahead without so much as a glance back."
    show sayori e3d b1a na ma at thide
    n turned mc b3a "Come on, we’ll be late."
    hide sayori
    "Slightly bewildered, I follow suit."
    _mc bd eb nb mf "Are- Are they an item?"
    _mc mh "Or am I just..."

    stop music fadeout 2.0
    scene bg art_class_afternoon with longfade
    $ set_date(hour=16, minute=4)

    play music school
    _mc turned ec mh "Well, that went rather poorly."
    show natsuki turned lhip rhip b3a e3d mo:
        matrixcolor TintMatrix("#f1d6bb")
        i21
        xoffset 50
    show sayori tap eb bc:
        matrixcolor TintMatrix("#f1d6bb")
        i22
        xoffset -50
    show bg:
        blur 1.5
    camera master: 
        align (0.5, 0.23) zoom 1.3
    with Dissolve(0.2)
    _mc ea "As soon as we arrived, we were divided into pairs. Natsuki clung to Sayori, so I was left in the dust."
    hide sayori
    hide natsuki
    show amelia turned md:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    _mc ma "Though, it wasn’t all bad. As luck would have it, my old friend Amelia just so happened to be passing through and saw my dilemma."
    _mc ef mh "... I can’t say I’m particularly proud of the art I’ve created."
    am bh ec me "C’mon, let me look! You drew me, the least you could do is show!"
    show amelia md
    mc ea ml "Ah, no, it’s alright. Why don’t you take your go now?"
    show amelia ed mc bi at dip
    "She pouts as we swap seats."
    _mc eb bd nb mh "All I can think of, though, is losing that money. I don’t know what happened! I was focused on what I was doing, and then..."
    _mc bi ef pout na "It just turned out so poorly. Like mid-way through, my concentration left me."
    camera master:
        align (0.5, 1.0) zoom 2.0
    show amelia:
        blur 2.0
    show expression Window(
        Transform(Transform("_amelia turned noblink", crop=(224, 120, 686 - 224, 1.0)), pixellate=3, xsize=150, fit="contain", align=(0.5, 1.0)),
        background="#e4bd93", style="empty", padding=(20, 10)
    ) as stuff zorder 5:
        align (0.5, 0.95)
    with Dissolve(0.2)
    "I pull the artwork up in front of me, and look at it again, but only for the briefest of moments." # she's 17 at the time smh my head
    _mc mf ea ba "Oh."
    _mc bi mm eg "Oooh, no."
    _mc mh "Yeah, I can’t show her that."
    _mc ec "Oh man, I can’t show her that."
    _mc ea ba "I mean, the sketch itself is pretty fine on its own, but..."
    _mc eb bd nb "... Why the hell is there so much detail around her lower half?"
    _mc "Is my subconscious that perverted?"
    camera master:
        align (0.0, 0.3) zoom 1.3
    show amelia ea md ba:
        blur 1.3
    hide stuff
    with Dissolve(0.2)
    _mc ef mh bi "C’mon, this is Amelia we’re talking about! She’s like- well-"
    extend ea ba na "... What is she like? Just an acquaintance?"
    _mc eg mm bi "Argh! It doesn’t matter - I can’t believe I would do something like this!"
    show amelia turned eb:
        blur 0.0
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    _mc ec mh ba "Sorry, Meelz..."
    _mc ef ma "... I suppose everyone has a little bit of perversion in them."
    show amelia:
        blur 2.0
    show bg:
        blur 0.0
    camera master:
        align (1.0, 0.2) zoom 1.8
    with Dissolve(0.2)
    _mc eg mh "But yeah, I can’t show her this. No way."
    _mc ec "That’s going to the grave with me."
    camera master:
        zoom 2.0 yalign 1.0
    with Dissolve(0.2)
    _mc ef ma "Either that, or getting burned."
    show amelia mg ec bi:
        blur 0.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:    
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    am mf "Hey, stop moving, ya dingus! Do you have any idea how hard it is to draw you when you keep moving?"
    show amelia mg with say_dissolve
    mc ea mg bd "I’m trying, alright?"
    am ed bh me "No you’re not, you’re just looking at that picture you won’t show me!"
    show amelia md with None
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    "I sigh, folding the artwork back up, and assuming the pose."
    _mc nb mh ba ef "I make sure I keep my skirt closed, something she had forgotten to do, which was what lead to the... incident. Don’t want any... unfortunate incidents of my own."
    show amelia ba ee me
    _mc eg bi ma "Well, any {b}more{/b} of them."
    show amelia ea md rup:
        blur 2.1
    camera master:
        align (0.0, 0.1) zoom 2.3
    with Dissolve(0.2)
    _mc bd eb mh "But seriously, what came over me? Drawing anyone like that is wild, especially for me, but Amelia?"
    _mc ec bi na "Something’s going on in my head today."
    show amelia bh ec:
        blur 1.5
    camera master:
        align (0.95, 0.5) zoom 1.4
    with Dissolve(0.2)
    _mc ef ba "I can’t quite put my finger on it, but..."
    _mc bi "It feels wrong."
    _mc ec "Like I’ve messed up, somewhere."
    show amelia ee bi mg:
        blur 2.0
    camera master:
        align (1.0, 1.0) zoom 1.8
    with Dissolve(0.2)
    _mc ef ba "... It’s not that I..."
    _mc ea mf "Ah. I get it."
    show amelia mi: 
        blur 0.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    am rdown bh ec mf "Dude, for real! You’re screwing up my whole sketch!"
    show amelia mg with say_dissolve
    mc bg mb nb "Sorry!"
    show amelia ee md
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I shake my head, trying to clear my mind."
    show amelia eb ba rup
    _mc ec mh ba na "Just... stay still. Don’t think about anything."
    "..."
    "..."
    _mc ea "Wait, hold on."
    _mc eb bd "Amelia’s doing it again."
    _mc "Is she-"
    _mc ec bi nc "She’s not doing it on purpose, is she?"
    $ autofocus.unblock("amelia")
    am ec bg me rdown "Your face is red."
    show amelia md
    "I stammer out a few weak lines, trying desperately to avert my eyes."
    show amelia eb ba me 
    "Finally, she looks down, and turns a shade of pink herself."
    show amelia ed bd ma at dip
    "Closing her legs entirely, she shakes it off and returns to her drawing."
    show amelia md ea ba rup
    _mc eg mm bi nb "What the hell is wrong with me? It’s not like I haven’t seen that sort of thing before!"
    _mc ec mh "Hell, I’ve seen my own a lot closer than that. Sayori’s too, when we were a little younger."
    _mc bb eb nd mf "W- Wait, not like that, I mean, through the clothes, ah-"
    am ee bb mf rdown "That’s it, I can’t work with this."
    am ed ba me "I’m just gonna leave it half-done."
    show amelia ea md lup
    "She points at me."
    am ec me "You, me. Outside, now."
    show amelia md at thide
    hide amelia 

    scene bg school_corridor_1_afternoon
    show amelia turned md:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with wipeleft 

    "I half expected her to slap me."
    show amelia ma bd
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    "But instead, she just looks concerned."
    am bb eb me "What the hell was all that about? It’s not like you haven’t seen some skin before, right?"
    show amelia md with say_dissolve
    mc turned mf nb "Well, yes, but ah-"
    am bd ea me "Do you like me or something? Oh god, please no..."
    show amelia ed md lup with say_dissolve
    "She groans at the thought."
    am ba me "You know why it won’t work."
    show amelia ea md with say_dissolve
    mc mg bg "N- No, I don’t like you, it was just..."
    mc mb ef bf "I don’t know what came over me. I just became really... aware of it, you know?"
    am "..."
    am ee me "Yeah, I do."
    show amelia ma ea with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She sighs, placing a hand on my shoulder."
    $ autofocus.unblock("amelia")
    am mb "Walk with me."
    show amelia ma at thide
    hide amelia

    scene bg school_courtyard_afternoon
    show amelia turned ee md:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with wipeleft
    show amelia at dip

    "We come to the garden area, and Amelia plops herself down on a bench, beckoning me to follow suit."
    show amelia ea
    show bg:
        blur 2.0 offset (-150, -100)
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    "I oblige, and she looks at me."
    am eb me "I heard you officially joined that literature club."
    show amelia md with say_dissolve
    mc turned ed md "You heard right."
    am ed me "So..."
    am bb eb mb "Has it been fun?"
    show amelia ma ba with say_dissolve
    mc ml ea "I suppose."
    mc mb "Wait, no, it’s been heaps of fun. I reconnected with Sayori a little, who I haven’t spoken to in years."
    mc mg "And I started talking to Monika more. We didn’t really talk all that much while we were in the same class last year."
    am ec mb "Well, I was in that class too, so, you were a little busy~"
    show amelia ma with say_dissolve
    "She snickers, gently elbowing me."
    mc ed md "Hah, maybe that’s true."
    am eb bb mb "C’mon, I’ve known you for a little while now."
    am ba me "What’s on your mind?"
    show amelia md with say_dissolve
    mc ef mf "Well..."
    show amelia ea ma with say_dissolve
    mc mb "I’ve been a little restless the past couple nights."
    am mb "Oh? Been seeing some boys?"
    show amelia ef ma with say_dissolve
    mc ef bi mg "No, not that kind of restless! Geez..."
    show amelia ee me with say_dissolve
    "She starts to laugh, but instead just breathes a heavy sigh."
    am lup bd ed mb "I’m sorry, I shouldn’t joke about that."
    show amelia md with say_dissolve
    mc ea ba mg "Why not? We’re all adults around here."
    am ee ba ldown me "It’s..."
    show amelia md with None
    hide amelia
    show bg:
        blur 0.0 offset (0, 0)
    camera master:
        align (0.0, 0.5) zoom 2.0
    with Dissolve(0.2)
    $ autofocus.unblock("amelia")
    $ say_transition = False
    "I look away from her."
    _mc ef mh "It’s probably to do with the reason she doesn’t have many friends."
    _mc bi "I totally get it; I don’t either, but that’s more by my own choice. Hers seems... forced."
    _mc ba "We only really started talking at the end of middle school, and by that stage, I think I was the only one who ever looked her way."
    _mc "I never heard any rumours, so I have no idea what happened, and I’ve never had the heart to ask."
    mc mf "No, it’s..."
    show amelia turned md:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    camera master
    with Dissolve(0.2)
    mc ea mg "I don’t know, really."
    am ed me "I get that feeling. Something’s going on, but you’re not sure what."
    show amelia md
    mc mb "That’s the one, yeah."
    am ee me bd "That must suck. How long’s it been happening for?"
    show amelia ea ba md
    mc thinking mf ed "Hmm... Probably since not long after I joined the club?"
    am mb "That was only a few days ago though, it might be nothing."
    show amelia ma
    mc ea mb "You’re probably right."
    am eb me "Oh, wait, I know exactly what it is."
    show amelia ba ee ma at dip
    "She reaches into her bag, and pulls out a tub of yoghourt."
    am eb mb rup "Ice-cream works better, but it also melts."
    am ed me "Sorry, I don’t have a spare spoon."
    show amelia rdown ma
    "I take it, thinking for a moment what she might be referring to."
    am eb me "Make sure you drink plenty of water, and if it gets really bad, go see the nurse for a heat pack."
    am ea mb "I’ve got some painkillers too, if that helps?"
    show amelia ma
    "Only then does it click for me."
    show amelia eb md
    mc ldown nb mg ea "Oh, no, it’s not that, that’s not due for another week or two..."
    mc ml "I just..."
    mc ef na mf bi "I dunno."
    show amelia ec ma
    "She gives me a sidelong smile, and a gentle hug."
    am mb "Well, whatever it is, I’ve got your back, ’kay?"
    show amelia ma
    mc bg mb ea "Yeah, thanks Amelia. I really appreciate it."
    show amelia eb at thide
    hide amelia
    "With that, she takes off, eager to get home for the day and back to her video games."
    _mc ef ma ba "Lucky."

    scene bg school_corridor_1_afternoon with fade

    "After making my way back inside, I start to wait outside the art room."
    _mc turned "I’m not sure why, but I feel compelled to walk home with Sayori today. Maybe part of me wants to discuss what’s been running through my mind for the past few days, with someone I know I can trust."
    _mc ec mh "Not that I don’t trust Amelia, but..."
    _mc ef "Sayori just feels... closer."
    stop music fadeout 2.0
    show monika turned rhip md:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    m "Oh, MC! Fancy seeing you here!"
    show monika ma
    mc ea mg "Oh, hey Monika!"
    play music okev_m
    m rdown mb "Are you waiting for Sayori too?"
    show monika ma
    mc mb "Yeah, I am. I was going to ask if she wanted to walk home with me today."
    m ed mb "Oh, that sounds like fun!"
    m ea md "I’ll borrow her another time, then."
    show monika mc
    mc ml "You need her for something? Sure, I’m not in a rush or anything."
    m eb md "Oh, no, it’s..."
    m ea mb "Just some club-related stuff, but it will take a little while to sort through. I can just ask her tomorrow." # im stuff
    show monika ma
    mc mb "Oh, please, don’t let me intrude. I’m sure the club is extremely busy at the moment."
    m ec mb "Thanks, MC. I appreciate your concern."
    show monika eb ma
    "After a moment, a slightly awkward atmosphere rings out."
    show bg art_class_afternoon as stuff onlayer above_master
    show natsuki turned lhip b3a mc onlayer above_master:
        matrixcolor TintMatrix("#f1d6bb")
        i21
    show sayori turned rup b1d e1b mj onlayer above_master:
        matrixcolor TintMatrix("#f1d6bb")
        i22
    with Dissolve(0.2) 
    "I glance inside to see everyone still deeply entrenched into their work."
    $ renpy.scene("above_master")
    show monika ea mc
    with Dissolve(0.2)
    mc ec ml "Looks like it’ll be a while."
    m mb "I see. Did you want to go for a walk then, while we’re waiting?"
    show monika ma
    mc bb ea mg "Oh, ah- Sure, Monika."
    _mc mh "Monika’s asking me to spend some time with her? I mean, I am a member of her club, and I did help her with her studies at the start of the week..."
    m mb "Cool! Come with me to the music room. I have something I’d like to show you."
    show monika ed ma with None

    $ advance_date(minutes=12)
    scene sky_afternoon at moving_sky with Dissolve(4.0)
    pause 2.0
    scene bg music_class_afternoon:
        align (0.0, 0.5) zoom 2.8
    show monika turned ec mc bc:
        matrixcolor TintMatrix("#f1d6bb")
        xcenter 0.3 zoom 0.8 ypos 1.0 yanchor 0.95
    with Dissolve(4.0)
    pause 0.06
    _mc turned mh "Woah... She’s so good."
    camera master:
        align (0.0, 1.0) zoom 2.3
    with Dissolve(0.2)
    "Her fingers gracefully tap the piano keys, with the notes beautifully meshing together, creating a tune that isn’t only catchy, but pleasing to the ears."
    show monika ea
    camera master:
        align (0.0, 0.2) zoom 1.6
    show bg:
        blur 1.0
    with Dissolve(0.2)
    "Her eyes bear the flames of determination, likely to put on the best performance that she can."
    _mc ec thinking "When was she this good at instruments...?"
    _mc ea "Not only is she president of a club, she’s also a top student in school."
    _mc ma "Add that with her sporting ability, and now this?"
    _mc ec ldown "What {b}can’t{/b} she do?"
    show monika nb md ec with say_dissolve

    play music2 add_playback_info(audio.okev, get_pos()) fadein 2.0
    stop music fadeout 2.0

    "The melodious song soon comes to its conclusion, with a rather loud breath of relief from Monika."
    camera master
    show monika ba na ea mc at i11
    show bg:
        blur 0.0 zoom 1.0
    with Dissolve(0.2)
    m mb "So.... how was it?"
    show monika mc
    mc mg ea "... It’s just... just amazing, really."
    m md "Oh...? How so?"
    show monika mc
    mc ef ml "I can’t describe it much in words... but the tune was not only very memorable, but also... very calming."
    mc ea mb "Maybe, you would think of a beach at sunset, dipping your feet in the water of the shore as the waves rise and fall..."
    show monika ma
    "Monika’s eyes light up upon hearing my analysis, probably signalling that she approves of it."
    m rhip ed mb "Almost exactly what I wanted to portray. Hehe, my composition has gotten a whole lot better since the last time."
    show monika ma
    mc mf "You... made this song?"
    m lpoint rdown nb mb ea "Ah... yes. I did. It reminded me of how, in music, there’s no boundaries to what you can make."
    m ldown ec na md "A life with you as the sole creator, and the sole catalyst to your destiny."
    m eb mb "To be free of choice. To be only what you want for yourself."
    m ea md "That is the meaning behind this song."
    show monika ma
    _mc ec mh "... How sentimental..."
    m mb "Did you like my use of seventh chords?"
    show monika mc
    mc thinking ed bm mf "Seventh... chords?"
    m rhip ec bb md "Oh my, apologies for my oversight in this matter. I forgot that you didn’t have much knowledge of music..."
    show monika mc
    mc mg ba ea "No, it’s alright. You can still ask me things."
    m bc ea md rdown "Hm... allow me to rephrase that..."
    m ba mb lpoint "How do you like the bassline?"
    show monika ma
    mc ldown mb "That’s like what you’re playing on the left hand, right?"
    m ed mb ldown "Bingo!"
    show monika ma
    mc ml "I would say that it did a very good job of helping to portray the message that you wanted."
    m eb mb "... That’s... good then."
    show monika ea ma
    mc mf "Do you compose often?"
    m ec md "Hm... I don’t compose much compared to others that I know."
    show monika mc ea
    mc ec mg "But to you, do you think you spend a lot of time on it?"
    m lpoint mb "Ah... yes. In fact, I would call that the most enjoyable thing about studying music. Crafting your own emotions into a song. It’s like, you leave yourself out there when you write tunes."
    show monika ma
    mc ef ml "... It’s something like literature, isn’t it?"
    m ldown mb "Exactly so. Whilst in literary works we use words and descriptions, in composing we use musical notes."
    m rhip md "Every form of art can be linked back to each other, don’t you think?"
    show monika ma
    mc ea mb "Now that you say it... yeah. They all seem to be quite in tune with each other."
    m ec "Mhm..."
    m rdown eb mb "Unfortunately, I’m not that good at expressing my ideas in music as much as with words, so I shall continue my musical studies so that I can produce a more... high quality piece."
    show monika mc ea 
    mc ed md "This is high quality, you know?"
    m mb "I- Is that so? Then I shall make it even higher quality when I next show you a piece..."
    show monika ma
    mc mb eh "And I will be looking forward to it. Trust me, I can’t wait to see how it gets more amazing than this."
    m eb bb mb "O- Oh... Don’t flatter me, MC."
    m ba ea md "It’s not good for me to be overconfident."
    show monika mc
    mc ea mg "I’m only telling you my thoughts on the piece, and in my head, it’s a master work of art."
    m bb ec mb "Thank you. I appreciate your comments."
    m eb bc md "I- If you would like, then, since you like my compositions so much..."
    m ea ba mb "Would you care to hear some more?"
    show monika ed ma
    mc ed md "I would love to."
    "She smiles, her hands returning to the keys once more."
    
    scene bg music_class_night
    show monika turned ec:
        matrixcolor TintMatrix("#48276e") * SaturationMatrix(0.6) * BrightnessMatrix(-0.02)
        i11
    with longfade
    $ set_date(hour=19, minute=21)

    "A long time passes before we return to our senses."
    "Enveloped in the atmosphere of the music room, the sound of the keys and the timbre of the piano itself, we were enraptured for much longer than we had originally anticipated."
    m ea md nb "Oh, look at the time! We both wanted to speak with Sayori, but..."
    show monika mc
    mc turned ef mf "She’s surely gone home by now."
    show monika ec md bb
    "We both sigh, our plans thoroughly ruined, but neither of us make any moves to leave."
    m eb ba "Should we... head home?"
    show monika ea ma
    mc ea ml "Yes, I believe that’s for the best."
    show monika mc
    mc mb "Shall I walk you home?"
    m nb md "Oh, no, I don’t believe that’s-"
    show monika mc
    mc ec ml "No, Monika, it’s late. I insist."
    m na bb md rhip "How will you get home, then?"
    show monika mc
    mc ea mg "I’ll work something out. I know these streets pretty well; if I stick to main roads, I’ll be fine."
    m ec md "Our houses are in opposite directions. It would be well and truly dark by the time you got home. I won’t allow that."
    show monika ea mc
    "I start to retort, but pause. She’s right, and I don’t know why I went out of my way like that."
    _mc ec mh "It’s not exactly like me to put myself in harm’s way for no real reason."
    _mc ef "Strange, it’s almost as if I wanted to spend more time with Monika."
    m eb ba md rdown "If you’re that way inclined, however... perhaps we could meet up for breakfast tomorrow?"
    show monika ea mc 
    mc ea ml nb "Oh, sorry, I’ve got work tomorrow. We could meet afterward, perhaps? I get off at three."
    show monika eb bb
    "She clicks her tongue, looking away dejectedly."
    m bc ec md "Sorry, I’m busy for most of the day tomorrow."
    show monika mc
    mc mb na "Could we aim for an evening meetup then? Maybe at one of the local restaurants?"
    m ea md ba "That should be alright, I suppose. You’ll confirm the details?"
    show monika ma
    mc ed md "Yeah, I’ll send you a text tomorrow letting you know the time and place."
    mc ea ml "See you then?"
    m ed mb "Sure, MC, see you then."
    show monika ma
    
    stop music2 fadeout 2.0
    scene bg mc_living_room with longfade
    $ advance_date(minutes=32)
    $ set_internet(True)
    play music a_sunshine

    mc turned eg "Alright, time to sit down and watch some anime-"
    play sound phone_notification
    phone register "mc_s":
        time auto True
        "s" "Hey, I’m outside."
    _mc ea mh "Hmm?"
    phone discussion "mc_s":
        pause
    phone end discussion
    _mc ec ma "Alright, change of plans. Not anime tonight, apparently."

    scene bg mc_house_entrance_night
    with wipeleft
    show sayori turned jacket at t11

    "I make my way over to the door, and open it up, letting Sayori inside."
    mc turned ed md "Hey, what’s up?"
    s mh "Oh, not all that much, Natsuki just mentioned that you wanted to talk to me."
    show sayori md
    mc eg mg bi "How did Natsuki... Never mind, it’s not important. I really just wanted to walk home with you. It’s been a long time."
    s lup e2a mb "Ooooh~ I see! Well, if you wanted to walk home, you could have at least waited!"
    show sayori e1a md
    mc ea mg ba "I did wait, I got chatting with Monika."
    s ldown e1d b1d mi "But you were nowhere to be found after school!"
    show sayori md
    mc ef mb bg nb "Well, we kinda went for a walk while waiting."
    show sayori lup rup xd b2a ml at hop
    s "Then how was anyone supposed to find you?"
    show sayori e1d b1d md rdown at dip 
    "She pokes her tongue out at me, gently elbowing me."
    show sayori ldown e1a b1a
    mc eh bf md "Ahaha, that’s true. We were in the music room. Monika was showing me her piano skills."
    s mh "Is that so? Was she any good?"
    show sayori ma
    mc ea ba mb na "She was amazing! Like something out of a dream..."
    s b1d e1d mb "Okay, okay, no need to have hearts in your eyes."
    show sayori e3d b1a ma
    "She nudges me again, and my attention returns to her."
    show sayori me e1a
    mc bd ml "What do you mean?"
    s e1b lup ml "You’re kidding, right? Listen to you, it’s like you’re fawning over her."
    s e1a mh "Come to think of it, you’ve sorta been doing that since you first joined the club."
    show sayori md
    mc bm ml ed "Who, me?"
    show sayori ldown
    mc ea ba mg "Over Monika? I think you’re exaggerating."
    s mg e3c "Hmm, I think time will tell that one."
    show sayori e1a ma
    mc ed md ba "Alright, you’re on. I’m gonna play super seriously next week. Not even a hint that there’s anything going on."
    s e1d b1d mb "Is that so? And what happens if you lose?"
    show sayori rup lup e1b mf b1a
    mc mb ea "I’ll make you lunch for a whole week."
    show sayori me e1a
    mc ed md "But if I win, you gotta tell me something super secret."
    s ldown rdown e3d mb "Ohoho, you’ve got yourself a deal."
    show sayori e1a ma at dip
    "We even shake on it, the competitive spirit inside me ignited."
    _mc mh ec "Part of me wonders why I’m so ready to prove I don’t have a crush on Monika, but what’s the harm? I haven’t known her that long. It’d be incredibly stupid if I’d fallen for her already, right?"
    s mh "Don’t you get cold feet now, alright? I’ll be watching you."
    show sayori ma
    mc ea ml "Just so we’re clear, the only rule is no flirting?"
    s e1d b1d mb "Yep. For an entire week."
    show sayori e1a b1a me
    mc mg "And just with Monika? So anyone else is fair game?"
    show sayori b4 md
    "She raises an eyebrow, a little confused."
    s mh "Y- Yeah?"
    show sayori md
    mc ed md bd "Well then..."
    show sayori ldown b1a ml e1b

    camera master:
        subpixel True align (0.5, 0.3)
        blur 0.0 zoom 1.0
        ease_quart 0.4 blur 3.0 zoom 1.7
        0.1
        blur 0.0 zoom 1.0
    show sayori:
        subpixel True
        0.5
        "sayori turned jacket lup rup mb e3d nb"
        zoom 1.6 yoffset 550
    show expression Gradient("#d8d0cc", "#75696b") zorder 1:
        alpha 0.0
        0.5
        alpha 1.0
    show black:
        alpha 0.0
        ease 0.4 alpha 1.0
        0.2
        ease 1.0 alpha 0.0
    play sound ["<silence 0.4>", audio.fall]

    "I jump at her, my fingers aimed directly at her sides."
    $ autofocus.block("sayori")
    $ say_transition = True
    mc bi ec "Time to take advantage!"
    s b2b xd ml nb lup rup "No- No! That’s no faaaiiiir~"
    show sayori mk with say_dissolve
    mc mb ed bd "No take-backsies! I earned this!"
    mc eh mb "Mwahaha!"
    s mb e3b b2a nc "Wait, no- Hold on, I gotta- Catch my-"
    show sayori mk b2b xd with say_dissolve
    mc bd ed md "Never! You will suffer my wrath!"
    s ml "B- But wait- That’s not-"
    s b2c e1a tears_a mb ldown rdown "Fair-"
    show sayori e3d notears b2a mo nb with say_dissolve
    mc mb eb nb "All’s fair in love and war! And this is WAR!"
    "The rest of the evening is spent with the two of us simply spending time together, locked in a never-ending back-and-forth."

    $ add_calendar_description(calendar_descriptions["monika"][2])

    call week_1_saturday_monika from _call_week_1_saturday_monika
    return