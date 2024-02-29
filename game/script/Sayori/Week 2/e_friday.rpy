label week_2_friday_sayori:
    call calendar_transition(day=3, hour=8, minute=4) from _call_calendar_transition_33
    scene bg s_house_day with dissolve_scene_full
    $ set_internet(False)
    play music hnt

    "I take a sidelong look at Sayori's house, before passing it by."
    "My face contorts in shame."
    _mc turned messy ec mh "Normally, I'd wait here for her."
    _mc ef "But even if she wanted to see me, I couldn't do it."
    show sayori turned:
        i11
        flash
    _mc eg "Her beautiful, smiling face would break me."
    _mc "She would bend my will simply by existing in my presence."
    _mc ef "I think the past few days have proven that."
    _mc ec "Today, I can't allow it to get to me."
    _mc eg bi "No, I won't."
    _mc "I made my choice."
    _mc "This is my divine punishment for the crime I committed."
    _mc ec "For hurting the most precious person in the universe."

    scene bg school_street_day with wipeleft_scene
    $ advance_date(minutes=12)

    "My slow, arduous trudge to school is painful."
    "I must be a sorry sight, drudging down the road like a limp, motherless duckling."
    "Lost and alone."
    show black with NonBlockingDissolve(12.0)
    _mc turned messy eg mh "I should have told her not to wait for me, that I'd already left."
    _mc ec "But I didn't have the heart."
    _mc ef "I just..."
    _mc bg "Walked away."
    _mc eg "Why?"
    _mc "How did it come to this?"
    _mc ea bf "All I ever wanted was to make her happy."
    _mc ec bg "But in the end, I know."
    _mc eg "She'll be happier when I'm gone."
    _mc "All I do is cause her pain."
    _mc ec ba "Cause myself... pain."
    _mc "That's no way to live."
    _mc eg "The only way to ensure that we both have the chance to live, is..."
    _mc ef "To be apart."
    _mc eg "I think I finally understand that now."
    "For the first time in a very long time, I decide to listen to some music."
    play music2 mp3song fadein 2.0
    $ renpy.music.set_volume(0.2, 2.0)
    "Pulling out my old MP3 Player, I load up the single song left on it."
    _mc ma "Honestly, I don't know why I keep it with me, but it's so small that it makes little difference."
    _mc ec mh "Usually, it sits inside my bag anyway."
    "Holding it in my hand, I place the headphones in my ears and listen to the song all the way through."
    "Then, like clockwork, I restart it."
    "Over, and over."
    "It's a cycle that's kept me sane, in the years since my family left."
    "The one thing that remains constant."
    "Honestly, I'm not even sure if the song itself matters to me anymore."
    "All that matters is that it doesn't change."
    "It, unlike everything else, has been there for me."
    "Again, I restart the song."
    "It's nothing special. Just something that I can listen to. It reminds me of days when my life was simpler."
    "Easier."
    "When I didn't have to worry about my bills, or about food, or about getting the best grades I could, just to be able to support myself."
    "Days when Sayori was always by my side."
    "And then I remember."
    _mc "This song..."
    _mc ef bg "It was her favourite growing up."
    _mc "That's why..."
    _mc eg "That's why it meant so much to me."
    "My face contorted into a shade of green, envious rage."
    _mc bi mm "WHY!?"
    _mc eb bd "WHY WAS IT ALWAYS HER!?"
    _mc "WHY CAN'T I JUST BE HAPPY FOR MYSELF FOR ONCE!?"
    camera master:
        align (0.5, 1.0) zoom 3.0
        easein_cubic 0.35 zoom 1.0
    stop music2 fadeout 1.0
    $ renpy.music.set_volume(1.0, 0.2)
    hide black with NonBlockingDissolve(0.35)
    "Grabbing the MP3 Player, tearing it from my ears, I prepare to hurl it down the path in front of me."
    "And..."
    "..."
    _mc ef bf mh "I can't."
    show black with NonBlockingDissolve(6.0)
    stop music fadeout 10.0
    _mc bg "I'm just..."
    _mc eg "Not..."
    _mc "Strong enough."
    _mc ec "I know, deep down."
    _mc "I don't want to be rid of Sayori."
    _mc "It would kill me."
    _mc "But..."
    _mc ea bf "What choice do I have?"
    _mc eg bi mm "Ugh."
    _mc mh "I'm disgusted."
    _mc "Disgusted with myself."
    _mc "Disgusted with the fact that I can look her in the eye at all."
    _mc "How..."
    _mc "How very..."
    _mc "Disgusting."

    scene bg class_1_day with Fade(0.0, 1.0, 1.5)
    $ set_date(hour=15, minute=7)
    play ambient int_day fadein 1.0

    "School is slow."
    "On the plus side, I'm able to concentrate better than I have the past few days."
    "But I can't help but feel hollow."
    "I didn't move during lunch."
    camera above_master:
        align (0.5, 0.1) zoom 1.5
        flash
    show bg class_1_day onlayer above_master as stuff:
        blur 2.0
    show white_flashback onlayer above_master
    show yuri turned mh e1d lup at i11 onlayer above_master
    "I think Yuri approached me, but I don't remember."
    "Maybe she was worried about me yesterday."
    $ clear_layers("above_master")
    _mc turned messy mj eg "Honestly, it doesn't matter."
    _mc ec mh "I can't go to the club."
    _mc "I can't look her in the eye."
    "As I pack my things, ready to head home, I see a familiar face standing in front of my desk."
    show yuri turned lup mg e1d at t11
    y "I- Is everything alright, MC?"
    y mh ldown e2a b1d "Natsuki said you had a fever yesterday."
    show yuri md
    mc ea ml "Ah, yeah. To be honest, I'm still not feeling too well, Yuri, so I'll-"
    y mb b1a e1a "Did you want me to walk you to the nurse's office?"
    show yuri md
    mc mg "Oh, no, I was just planning on going home, actually."
    y mh lup nb e1d "B- But you can't do that, today's our last day of preparation for the festival..."
    show yuri md
    _mc ec mh "... I know that."
    mc ea mf "I..."
    y me e1b b2a "You aren't..."
    y shy bb eb ma "Dropping out of the festival, right?"
    show yuri ea
    mc eb mg "N- No, I just need..."
    y eb bc na "..."
    y turned ldown mb e1a b1a "Please, let me walk you to the nurse. Then we can go to the club together."
    show yuri ma
    mc ea mh "..."
    mc ef mf "I think..."
    mc mb "Yeah."
    mc eg "Let's do that."
    y e3d mb lup rup "Excellent. Your fever is under control, I take it?"
    show yuri ma
    mc ef mj "Err, well..."
    y ldown rdown mb e1a "Otherwise you wouldn't have come to school, right?"
    show yuri ma
    _mc ea mh "Ah."
    _mc bg eh nb teehee "She's got me there."
    mc ea mg bb "I- I... I'm feeling a little better, but still a little sick."
    y e1d mg "Well, if you're feeling better, you should be well enough to come to the festival on Monday."
    y e3d mb "And to start that, let's go to the club."
    show yuri ma
    mc nb ef mg ba "Yuri I... I don't know if I should risk anyone else catching it there."
    y lup e1d mh "Well Sayori is there, isn't she?"
    show yuri ma
    "I blush bright red."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc eb ba nc mh "She probably doesn't mean... that... does she?"
    _mc eg bi ma "N- No... Don't be silly..."
    _mc ef nb mf ba "But... Uhh-"
    _mc mh na "She makes a good point."
    _mc eg bi mm "Damn it."
    _mc mh "I really don't need to argue right now."
    _mc eb bd "Just... Damn you, Yuri. Can't you see I don't want to go?"
    hide black with NonBlockingDissolve(0.2)
    mc ec ml ba "Yes. Yes, she is."
    y ldown e1a mb "Then come on."
    show yuri ma with None
    
    scene bg school_corridor_3_day:
        blur 2.0 
    show yuri turned lup e1d md at i11
    camera master:
        align (0.5, 0.1) zoom 1.5
    with fade
    $ advance_date(minutes=2)

    "As we walk, Yuri keeps trying to make small talk, to no avail."
    camera master
    show bg:
        blur 0.0
    show yuri ldown e3c b1d mj
    with Dissolve(0.2)
    "Finally, she just turns to me."
    y e2a b1a mh "MC, what's ailing you? Something's wrong... or is it that you've given up on the club?"
    y e1d b1d mg "Which is it?"
    show yuri md
    "Yuri's tone surprises me."
    "She's normally so calm, collected, but now-"
    "I daresay this classifies as confrontational."
    mc turned messy ml "I-"
    show yuri e1d b1a
    mc ef mg "Yes. Something is wrong."
    y lup me "Yes?"
    show yuri md
    "Her face takes on a soft tone."
    _mc thinking bi mh "Do I want to tell her?"
    _mc ba "This really isn't her business but..."
    _mc ec "I may as well tell her, mightn't I?"
    
    menu:
        "Tell her.":
            $ fr_told_yuri = True
            if preferences.language is None:
                $ auto_advance_date_mult = 0.66
            stop ambient fadeout 3.0
            play music ["<silence 0.2>", audio.faith]

            mc ef ml ldown "Look, I'll tell you what's been on my mind, but..."
            mc ea bd mg "Please, please keep it a secret."
            mc eg bi mb "Honestly, I'm not sure about half of this myself, so other people finding out would just make it more confusing."
            y mb e1a ldown "Of course, you have my word."
            show yuri ma
            mc "Thanks."
            camera master:
                align (0.5, 0.1) zoom 1.5
            show bg:
                blur 2.0
            show yuri md
            with Dissolve(0.2)
            $ autofocus.block("yuri")
            $ say_transition = True
            mc thinking ef ml ba "So... Where to begin..."
            mc ea mg "Essentially, Sayori and I..."
            y lup e1d mh "You two have a thing, right?"
            show yuri md with say_dissolve
            mc ldown ec mg bi "Huh?"
            y e2a b1d mg "Well, I know you've only recently reunited, but it seemed fairly obvious that something's been going on between you two."
            y ldown mb e3c b1a "Not to mention Sayori was taking care of you while you had a fever."
            show yuri ma with say_dissolve
            mc ef mj ba "Ah, that's true."
            y lup e1d mh "You do need to work on your lies, by the way. It was abundantly transparent."
            show yuri ma with say_dissolve
            "Yuri flashes me a small smile."
            y ldown mg "So, I already could have inferred all of that. What's been bothering you?"
            show yuri e1a md with say_dissolve
            mc ef mh "..."
            show yuri e1d with say_dissolve
            mc mg bb "We didn't exactly stop talking on good terms."
            y b4 mg "Really?"
            y b1a e1a mb "The way Sayori talks about you, you'd think you were the greatest person on the planet."
            show yuri md with say_dissolve
            mc ea bd ml "Huh?"
            y mg b1d "You didn't know that?"
            y mh b4 e1d "You are aware that she thinks the world of you, right?"
            show yuri md with say_dissolve
            mc ef bg ml "... Then why do I keep hurting her?"
            y mg e3c b1d "Oh, MC. I don't think you've ever really hurt her. Shocked, perhaps, but never hurt."
            y e1a mb b1a "I don't think you could."
            show yuri ma with say_dissolve
            mc ea bf mf "But..."
            y lup e1d mh "Tell me, have you ever stopped to consider her feelings?"
            show yuri md with say_dissolve
            mc bd mg "Of course I have, that's all I ever think about-"
            y mh ldown e3c b1d "No, listen."
            y mg e1a "Have you ever stopped, and considered what her opinion might be on your actions?"
            show yuri md b1a with say_dissolve
            mc ed bm mg "Well I know her. She thinks the same way I do, we grew up together."
            y e3c mh "Perhaps you did think the same way once, but do you really believe Sayori hasn't grown in the time you've been apart?"
            show yuri md with say_dissolve
            mc ea mh ba "..."
            y e1d mg "Did you ever really take the time to consider how she felt, about anything?"
            y mb e3c "You know, before you ever came to the club, Sayori used to talk about this incredible person."
            y mh "Someone who was brave, and smart, and attractive, and so much of a hero to her."
            y lup e2a mb "That person meant everything to her, growing up."
            y mg e1a b1d "Now, consider my surprise when, one day, you walk in the door."
            y b1a e1d mb "And when you do, what name does she speak first?"
            y mg e2a "Who was it that meant the world to her?"
            y e1a mb "It was you."
            show yuri md ldown with say_dissolve
            mc mg bi eg "No, no no no no no!"
            mc ef mg bg "You... You don't understand..."
            mc ml "I did something..."
            mc eg bi mm "Something I cannot take back."
            mc bb eb mg "I hurt her. I hurt my best friend."
            mc ef ml bg "She trusted me."
            y e3c mh "And she still does."
            y e1d b1d lup mg "Did you ever talk to her about how you felt?"
            show yuri md with say_dissolve
            mc eb bd nb mg "I knew how she felt!"
            mc "I could see it in her eyes!"
            mc ef bi "She's too polite to say it, but I did!"
            mc mf "I..."
            mc ec ml na "I did this..."
            y "..."
            y mg ldown e3c "Maybe you are the monster here."
            show yuri md with say_dissolve
            mc mf "Huh?"
            y e2a b1a mg "Maybe, just maybe, you're right."
            y e1a b1d "But tell me this."
            y mh b1a e1d "Is a person defined by their past?"
            y mi e3c lup rup "By their mistakes?"
            show yuri md with say_dissolve
            mc ea ba na ml "Well, I-"
            y ldown rdown e1d b1d mh "Because if they are, then you deserve to feel terrible."
            y mg e3c "But don't come crawling back to me when you feel sorry for yourself."
            show yuri md with None
            hide yuri
            show bg:
                blur 0.0
            camera master
            with Dissolve(0.2)
            $ autofocus.unblock("yuri")
            $ say_transition = False
            "Yuri starts to stride off."
            mc mg bb "W- Wait..."
            mc ef ml ba "Yuri..."
            show yuri shy ee bc at t11
            "She turns back toward me, her face shrouded in her hair."
            y ea "Yes?"
            "Her voice cut through the air like a knife."
            mc ea bg ml "What should I do..."
            y eb "You should have faith."
            y bb ea "You should trust in your best friend, instead of assuming you know what's best for them."
            mc mh "..."
            y turned mg e3c b1d "And, most of all, you should trust in yourself."
            y b1a e1d mb lup "It isn't as bad as you make it out to be."
            y e2a mg "If you trust yourself to make the right decisions, you'll start to make them, instead of second-guessing yourself all the time."
            y mh e1d "It isn't poor decisions that are hurting you."
            y mg e1a ldown "It's your lack of ability to actually make a decision."
            show yuri md
            mc thinking bi ef mf "So you mean..."
            mc ea ba mg "Any decision is a good decision?"
            y e3c mg "That's... one way to put it."
            y e1d mh "More like, making a decision will always benefit you more than not making one, because if you don't decide, the universe will decide for you. "
            y mg e1a b1d "And you won't like its choice."
            show yuri md at thide
            hide yuri
            "And with that, she leaves."
            _mc ef mh ba "I think..."
            _mc ldown eg "I think I get it."
            _mc ec "I've been hurting Sayori, yes..."
            _mc "But my inability to come to terms with my actions up to this point, and my refusal to make any form of decision, has been what has been causing her the most pain."
            _mc eg bi "The conclusion I had come to this morning was wrong."
            _mc ec "Not that it was the wrong decision, but that I didn't consult Sayori."
            _mc ea ba "If I make one choice today, it must be this."
            _mc eg "Sayori will be the one to decide."
            _mc "I won't make any assumptions."
            _mc "I won't speak for her."
            _mc "I'll listen to what she has to say, and that will be it."
            _mc "No fancy words, no overcomplicating it."
            _mc ec "Just... Sayori."
            if preferences.language is None:
                $ auto_advance_date_mult = 1.0
            stop music fadeout 2.0

        "Don't.":
            _mc ldown bi eg mh "Ah, no, that would only hurt Sayori."
            _mc ec ba "I don't want to make this any more complicated than it already is."
            _mc "Best to keep it to myself."
            mc ea mg "Yuri, I truly appreciate the sentiment, and thank you for caring, but I..."
            mc ef ml "It's just something I need to take care of on my own terms."
            mc ea bg mb "I'm not leaving the club, or anything, I just needed some time to..."
            mc ef ml "To collect my thoughts."
            y e2a b1d mg "O- Oh. I see."
            y ldown e3c mb "I can't force you to tell me, and if you aren't leaving the club, I guess it's alright."
            y e1d mg b1a "But if you ever need advice, or someone to lean on, please ask."
            show yuri ma
            mc ea mb "I will."
            show yuri md e2a with None
            show black with NonBlockingDissolve(3.0):
                alpha 0.5
            stop ambient fadeout 4.0
            "The rest of the walk is in silence."
            "Just me and my thoughts."
            _mc mh "I want to see her."
            _mc "That's undeniable."
            _mc eg "But I know that will only make it worse for me."
            _mc ec ba "Best to let it play out, I suppose."

    scene bg club_day with wipeleft_scene
    $ set_date(minute=22)

    "Stepping into the clubroom, I see the members hard at work."
    show yuri turned e2a b1d at t41
    show monika turned at t42
    show natsuki turned me at t43
    show sayori turned rup mj e1b b1d at t44

    play music okev

    "Yuri's already walked in, and is talking to Monika, and Natsuki is helping Sayori with hanging some of the paper decorations we had made a few days ago."
    "There's a stack of candles laying on one of the desks, no doubt for ambiance."
    "Monika's even holding a curtain rack, preparing to hang it in front of the window."
    show monika lpoint
    hide sayori
    hide natsuki
    hide yuri
    camera master:
        align (0.1, 0.2) zoom 1.3
    with Dissolve(0.2)
    "As I fully enter the room, Monika motions to me."
    show monika ldown at i11
    camera master
    with Dissolve(0.2)
    m mb "Ah, MC, you're back. I hope you're feeling better, after yesterday?"
    show monika ma
    mc turned messy md eh bg nb "Yeah, a lot better, thanks."
    show monika ed
    "Monika gives me a wide smile, and I feel a little bad for lying to her."
    m md ea "Is there any chance you could help us hang the curtains?"
    m rhip mb nb eb bb "Sayori and Natsuki can't quite reach the railing, so we could use an extra pair of hands."
    show monika ma
    mc ea mg ba na "Yeah, sure. Just point me where you need me."
    hide monika
    camera master:
        align (1.0, 0.1) zoom 3.0
    with Dissolve(0.2)
    "Grabbing Monika's rack, I reach upward, placing it on a hook."
    "They're right, Sayori wouldn't have a hope of reaching this without standing on a chair."
    "It reminds me how short she is."
    "Next, I slide the curtain onto the rack, ensuring it sits neatly."
    "The curtain is made of a thick, heavy fabric, making it difficult to manoeuvre properly."
    "After some work, I managed to thread it onto the shaft, and slide it down."
    camera master
    with Dissolve(0.2)
    "Taking a step back, I admire my handiwork."
    mc ml "Ah, shoot."
    "It's on backwards."
    show monika turned eb bc at t11
    "Turning to face Monika, I can see her smiling, a snicker crossing her face."
    m ec mb "Well, at least we know it fits."
    show monika ma
    "I smile back."
    mc ef mg "It was always going to fit, the hole stretches."
    hide monika
    show yuri shy eb mc:
        i41
        zoom 0.75
    show bg:
        align (0.0, 1.0) zoom 1.3
    with Dissolve(0.2)
    "I notice Yuri hiding behind her bangs, but I can clearly see her embarrassed face."
    show bg:
        zoom 1.0
    hide yuri 
    show monika turned at i11
    with Dissolve(0.2)
    mc ea "Well, I suppose I should try again."
    m ed mb "Second time's the charm, as they say."
    show monika ma with None
    hide monika
    camera master:
        align (1.0, 0.1) zoom 3.0
    with Dissolve(0.2)
    "Taking it off, I slide the curtain back down the shaft, slowly letting it pool onto the ground."
    "I then wade through the black mess, finding the other end, and proceed the process anew."
    "Slowly pushing the shaft into the black, elastic hole."
    "..."
    _mc bd eb nb mh "Wait..."
    "As I place the rack back onto the hook, a thought occurs to me."
    _mc eg bi mm "What the hell am I thinking about?"
    _mc mh na "It's just hanging curtains."
    _mc ef ba "So why..."
    _mc ea "Why does my mind drift to Sayori?"
    "My thoughts settle on a single line, one that I had yesterday."
    camera above_master:
        align (0.5, 0.75) zoom 1.7
        alpha 0.0 mesh True
        linear 6.0 alpha 1.0
    show sayori turned pyjama2 e2a md at i11 onlayer above_master
    show bg mc_living_room as stuff onlayer above_master:
        blur 2.5
    show black onlayer above_master:
        alpha 0.7
    "The thought of her wearing my clothes."
    "And that thought was followed by another."
    "One of her..."
    "Not wearing my clothes."
    camera master
    $ clear_layers("above_master")
    with fastfade
    "Shaking my head, I drive any inkling from my brain of that thought."
    show monika turned rhip at t11
    "Turning back toward Monika, I ask,"
    mc mg "What else needs doing to prepare for the festival?"
    m mb eb "Ah, well, on Sunday there will be a few things to do. Natsuki will be baking cupcakes, and there will be some last-minute decorations, but other than that..."
    m ea rdown md "Oh, actually, is there any chance you could help Natsuki make a run to the Debate Club?"
    m mb "We're borrowing some of their microphones and speakers."
    show monika mc
    mc thinking ml "Oh, sure. Why wouldn't you be going though?"
    m eb md "I've..."
    m mb "Got some things to handle here first, and that needs doing asap so we can set it up."
    show monika ea ma
    mc mb ldown "Got it. I'm on my way."
    show monika ma ea at thide
    hide monika
    show natsuki turned md at t51
    "Calling out to Natsuki, I watch as she rises, and follows me out of the room."
    
    scene bg school_corridor_1_day with wipeleft
    pause 0.02
    show bg:
        blur 2.0
    show natsuki cross mj b3a at i11
    camera master:
        align (0.5, 0.25) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    $ advance_date(minutes=4)

    "As we leave the clubroom, Natsuki, who had been walking by my side, gets suspiciously close to me."
    n mh "So, what's been happening?"
    show natsuki mj with say_dissolve
    mc turned messy ml bm ed "What do you mean?"
    show natsuki ma e2c b1a with say_dissolve
    "Natsuki rolls her eyes, a small grin on her face."
    n e1d b4 mb "I mean, with Sayori."
    show natsuki ma with say_dissolve
    mc ef mj "Oh, that."
    show natsuki md e1a b1d 
    camera master:
        xoffset 0 
        ease 30.0 xoffset -100 zoom 1.37
    with say_dissolve
    "Her expression sours a little, as we keep walking."
    n turned lhip rhip mi e1d "Don't you, 'Oh, that' me. You knew that's what I was talking about."
    n ldown rdown mg b3a e1a "Do you... not want to talk about it?"
    show natsuki mj with say_dissolve
    mc ec bi ml "... Not really, no."
    n cross mg b1d e1d "Well, I do."
    n e1a b1a mh "You know you ditched her this morning, right?"
    show natsuki md with say_dissolve
    mc thinking ed bm mg "I don't think I could possibly not have known that I didn't ditch her?" # tardlilly
    n me "Wh-"
    n mg e1b b1d "That doesn't even make any-"
    n e3c mm "Ah, forget it."
    n turned mh b1a e1a "The point is, you realise that hurt her, right?"
    
    stop music fadeout 2.0

    show natsuki md with say_dissolve
    mc ldown bi ef mg "... Of course I do."
    n lhip rhip mi b1d e1b "Then what the hell?"
    show natsuki mm with None
    show natsuki e1d
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Natsuki grabs my sleeve, whirling me around to face her."
    "It was only then, that I realised, I'd been walking quite quickly, perhaps a subconscious effort to escape her."
    $ autofocus.unblock("natsuki")
    n mh e1a ldown rdown "Why would you ditch her like that?"
    show natsuki mj
    mc ec mf "I told you, I don't want to talk about it."
    show bg school_corridor_1_day as stuff onlayer above_master:
        alpha 1.0 xzoom -1
        0.5 + 0.1
        easein 0.2 alpha 0.0
    camera master:
        align (0.5, 0.25) zoom 1.0
        0.5 + 0.1
        easein_back 0.27 zoom 1.3
    show bg:
        blur 0.0
        0.5 + 0.1
        easein_back 0.27 blur 1.0
    show natsuki lhip rhip e1d b1d mm
    with NonBlockingTransition(wiperight)
    play sound ["<silence 0.6>", audio.fall]
    "Shrugging her off, I attempt to start walking again, only to be halted by Natsuki's surprisingly strong grip."
    $ say_transition = True
    $ autofocus.block("natsuki")
    n mg "Don't you dare walk away from this."
    n mm e1b b1a "I thought I could trust you."
    n mh "I thought you were the person my best friend trusted more than anything. The person she could rely on."
    n cross b1d e1a mg "And you would just walk away from her?"
    n e1b mm "Not once, but twice?"
    mc ef mh "..."
    show black onlayer above_master
    hide natsuki
    with NonBlockingDissolve(0.3)
    "I look away from Natsuki."
    "I'm sure she can see the conflicted look on my face, but I don't care anymore."
    mc bd ea ml "Why can't you just mind your own business?"
    n turned b3a mh e1a ldown rdown "When it isn't my business, I just ignore it."
    n e1d b1d mg "But you've hurt my best friend."
    _mc ef bi mh "... She's right."
    n b1a e1a mh "Now, you have six seconds to explain yourself."
    mc ec mf "And if I don't?"
    show natsuki me b1d at i11
    hide black onlayer above_master
    camera master:
        zoom 1.7
    show bg:
        blur 2.5
    show layer master at vpunch
    play sound fall
    play music nsc
    "Natsuki pulls me around once more to face her."
    "Her small stature, not even reaching five feet, meant nothing when I was met with the fire in her eyes."
    "If I didn't know any better, I'd almost say there was bloodlust hidden in there."
    n b3a mg e1b "Then your life might just end up a living hell."
    n mb "So miserable that you might wish for the sweet release of death."
    n mh "But it won't come."
    show natsuki mg e1d b1d
    camera master:
        zoom 1.74
    show bg:
        blur 2.7
    show expression "#ff3e3e" onlayer above_master
    camera above_master:
        alpha 0.05
    with NonBlockingTransition(fastfade)
    n "You"
    show natsuki e1a b1a mh
    camera master:
        zoom 1.8
    camera above_master:
        alpha 0.1
    with NonBlockingTransition(fastfade)
    extend " Will" 
    show natsuki e1b mg
    camera master:
        zoom 1.9
    camera above_master:
        alpha 0.15
    with NonBlockingTransition(fastfade)
    extend " Not" 
    show natsuki mm
    camera master:
        zoom 2.0
    show bg:
        blur 3.0
    camera above_master:
        alpha 0.2
    with NonBlockingTransition(fastfade)
    extend " Hurt"
    show natsuki mg b3a
    camera master:
        zoom 2.15
    camera above_master:
        alpha 0.25
    with NonBlockingTransition(fastfade)
    extend " My" 
    show natsuki mh
    camera master:
        zoom 2.3
    show bg:
        blur 3.2
    camera above_master:
        alpha 0.3
    with NonBlockingTransition(fastfade)
    extend " Best" 
    show natsuki b1d mm
    camera master:
        zoom 2.5
    show bg:
        blur 3.5
    camera above_master:
        alpha 0.35
    with NonBlockingTransition(fastfade)
    extend " Friend."
    camera master
    show bg:
        blur 0.0
    show natsuki b3a e1a ma
    $ clear_layers("above_master")
    $ say_transition = False
    stop music 
    play ambient int_day
    "And with that, her grip releases and she steps away."
    "Her face, like a switch, instantly returns to her normal, cute self."
    "And, with a smile on her dial, she speaks."
    $ autofocus.unblock("natsuki")
    n mb "So, why did you hurt Sayori~?"
    show natsuki ma with None
    show bg school_corridor_1_day as stuff onlayer above_master:
        xzoom -1
    with NonBlockingDissolve(0.5)
    "I momentarily glance around me, stepping further back, though she advances once more to keep pace."
    "It seems the halls are empty - Not a soul seems to have noticed."
    _mc ec mh ba na "Naturally, of course. I doubt she'd do something like that if there were eyes to see it..."
    hide stuff with NonBlockingDissolve(0.5)
    "My heart still pounding, I take a few moments to recompose myself."
    mc ec ml ba "You... you want to know the truth?"
    n lhip rhip mb e1d b1d "Anything less, and you'd be in for some hurt~"
    show natsuki ma
    stop sound_loop fadeout 3.0
    mc ef "Point taken..."
    "{i}Best to reveal the truth. I don't know what she might do to me if I don't.{/i}"
    stop ambient fadeout 3.0
    show natsuki ldown rdown mj e1a b1a
    mc eg mj "Well, here goes."
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("natsuki")
    "After a deep breath, I start from the beginning."

    play music faith

    mc ec ml "This is my take on it, at least."
    mc ea mg "I've known Sayori for longer than I can remember."
    mc ef mb "She was my best friend, my muse, my companion. We did everything together."
    mc ea "Whenever one of our families went away, we'd always beg for the other to come with us."
    mc "So, naturally, as kids, whenever my parents left on trips, I stayed with Sayori's family."
    mc mh "..."
    show natsuki md with say_dissolve
    mc ef mg "When we were in middle school, we started getting teased for being around each-other all the time."
    mc ea "I don't think either of us actually paid any attention to it, quite the contrary, in fact."
    mc mb "It made our bond stronger."
    mc ef mg "But, with that bond, and the hormones that accompany that age, something in me changed."
    mc bi ml "I..."
    mc ea mg ba "I felt something I'd never felt before. And for Sayori, no less."
    mc ml "The person who'd been with me through everything."
    show natsuki b3a with say_dissolve
    mc ec "Because of that..."
    mc ef "I did something stupid."
    mc mf bi "I..."
    show natsuki e2a with say_dissolve
    mc ba ea mg "One day after school, as we hung out on the beach on our walk the long way home, I..."
    show natsuki me b1d with say_dissolve
    mc ef ml "I kissed her."
    mc eg bi mb "I don't know what came over me."
    mc ef ba ml "To be honest, I still don't know."
    mc eb bd mg "But the look on her face..."
    show natsuki e1d with say_dissolve
    mc ef bg ml "It told me everything."
    show natsuki e3c with say_dissolve
    mc eg "It was then, at that moment, that I knew."
    mc mm bi "I'd done something unforgivable."
    mc mf bg "So..."
    show natsuki md with say_dissolve
    mc ef bf ml "I didn't try."
    camera master:
        blur 0.0
        ease 40.0 blur 1.0
    mc ea mg bf "There was no way she'd ever outwardly hold it against me, it simply wasn't in her nature."
    mc ef bg ml "But deep down, I knew that I'd ruined our friendship."
    mc mm eg bi "In that one, stupid act, I'd destroyed what the past who-knows-how-many years of our lives had been."
    mc ef ba ml "And I left."
    show natsuki mj e1a b1a with say_dissolve
    mc "I had no right to look her in the face."
    mc mf "So..."
    mc eg ml "I ran away."
    mc mg "From her, from our friendship, from the possibility of ever looking her in the eye again."
    mc ef ml "It was better that way."
    mc ea mg "Better for me, and for her."
    "All of a sudden, I realise that I'm choking up."
    "Reliving those memories has perhaps been the hardest thing I'd had to face, since seeing Sayori's face again only two weeks ago."
    "I hadn't meant to pour my heart out to Natsuki, but here we are."
    n me "..."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    n mg "... What..."
    n cross b2a e3d mo "What a stupid story!"
    n turned lhip b3a e1a mc "Did you never think, even once, to actually ask her about how she felt?"
    show natsuki ma
    mc ec bi ml "I could tell."
    "A weak excuse."
    n mb ldown "You could 'tell', could you?"
    n cross e1d b1d mm "Then why does she still, even after all the crap you've put her through, speak so highly of you?"
    n e1b mh "Why are you all she ever talks about?"
    n mm "Why does she like you {i}more than me{/i}?"
    n b1a mi "Do you have any idea what you mean to her?"
    n mm "Any at all?"
    show natsuki md
    mc mh ef ba "..."
    n turned mg e1d b1d "I didn't think so."
    n lhip rhip mh "But you won't even face that."
    n b3a e1a mg ldown rdown "You know what you are?"
    n e3c mi "A coward."
    n cross e1a b1a mh "You let your insecurities rule you, instead of facing them."
    n turned lhip e2a mb "You claim to have your whole life together, and I'm sure you do."
    n ldown b1d e1d mm "But don't you dare claim to know what's best for Sayori."
    show natsuki mj
    mc "..."
    mc mf "I know."
    mc ml "In fact, I'd already come to that conclusion."
    show natsuki b1a e1a md
    mc ea mg "I was going to talk to Sayori tonight."
    mc mf "And..."
    mc ef ml "I was going to let her decide."
    $ autofocus.block("natsuki")
    n me b3a "..."
    show natsuki b2a ma at dip
    "Natsuki's face softens."
    "She gently places a hand on my shoulder."
    $ autofocus.unblock("natsuki")
    n e3c mb "Thank you."
    n lhip mh b3a e2a "I won't apologise for that."
    show natsuki mj
    mc mb bg "I don't expect you to."
    n b1d mg "But, I think I understand you better now."
    n ldown b1a e2c mh "If anyone could one day be good enough for Sayori..."
    n e3c b3a mi "With a lot of work, and I mean, a LOT of work..."
    n mb e1a "You might amount to something."
    show natsuki ma 
    mc eg mb "... Thank you."
    mc ea be "That means more to me than you realise."
    n mb e3c "I know."
    show natsuki ma
    "The rest of our trip is made in silence, as we soak in what we'd just been through."

    stop music fadeout 2.0
    scene bg school_corridor_2_day with longfade
    $ advance_date(minutes=4)
    $ renpy.music.set_volume(0.3, 0.0, "ambient")
    play ambient students fadein 3.0

    "Soon, we have the classroom in which the Debate Club is located in sight."
    "The noise blasting out from inside the room is intense and constant."
    "The Literature Club is practically silent in comparison."
    _mc turned messy thinking ec mh "Guess that's how a big club runs."
    "..."
    "Worry still floats in my mind."
    "Worries about what's to come."
    _mc ldown ef "I don't want to hurt her again. I've done it too many times-"
    show natsuki turned lhip rhip e1d b1d mh at t11
    n "Oi, what are you waiting for?"
    show natsuki mj
    "I realise I'm standing right in front of the door leading to the club room."
    mc ea mg nb "Sorry."
    show natsuki ldown rdown b1a e1a md
    _mc eg bi mh "Just focus on the task at hand... I'll worry about Sayori later."
    play sound door_knock
    "I knock loudly on the door, though part of me is a little concerned with the amount of noise coming from inside the lecture hall."
    "..."
    "Realizing that they probably didn't hear me, I go to knock agai-"

    $ renpy.music.set_volume(1.0, 1.0, "ambient")
    $ renpy.music.set_volume(0.3, 0.0)
    play music playwme fadein 3.0

    show aika turned at t21
    show natsuki ma at t22
    "Aika walks out, swinging the door open widely."
    a mb "Oh, hey Natsuki and MC! How can I help you two?"
    show natsuki md
    show aika ma
    mc na ef ba mj "Well..."
    n b3a mh "We're looking for microphones. We need to borrow some for our..."
    show natsuki me b1a e2a at t33
    "Natsuki seems to clam up all of a sudden, moving behind me and tugging slightly on my sleeve."
    _mc eb bd nb mh "Nat? What the hell's gotten-"
    # TODO crowd
    show bg club_day onlayer above_master as stuff:
        xzoom -1
    hide aika
    with NonBlockingDissolve(0.5)
    $ autofocus.block("aika")
    "As I glance past Aika, I suddenly see a huge bustle going on. The noise wasn't all for show, it seems."
    show natsuki md
    a turned mf "Oh? Monika's Literature Club, right?"
    a mb "Sure thing."
    show aika turned md ec at i21
    $ renpy.scene("above_master")
    with {"above_master": Dissolve(0.5)}
    "Aika's grin draws me back, to the conversation, but Natsuki doesn't budge from her spot."
    show aika ed ma at t51
    "Aika looks back into her clubroom and calls out, seemingly unfazed by the cacophony within."
    $ autofocus.unblock("aika")
    a rhip mc "Hey, Kei! Can you grab some of the spare microphones from the back?"
    show aika ma
    "I can vaguely hear footsteps approaching the door from further in the room, once they're close enough, though I can't get a good look at this angle at who it might be."
    vp "Microphones? What for?"
    a ea mb "These two girls need some for their culture festival event."
    show aika me ed
    vp "We're not just a charity, Aika..."
    "Whomever Aika's speaking to on the other side lets out a sigh."
    a rdown mg eb "I know Kei, it's for those Literature Club girls over yonder. Besides, it's a request from a member of the student council."
    show aika me
    "..."
    "Besides the cacophony happening in the room next to us, silence."
    show aika ma
    vp "Fine. I'll grab them."
    show aika ea
    mc thinking ml ea ba na "Problem?"
    "I raise my eyebrow, not quite certain what to make of the curt conversation."
    a ed mb "I'm sorry about that. She just doesn't mingle with other clubs well."
    show aika ma
    mc ef ml "Right."
    show natsuki b1d
    "I shrug, not really concerned, but the tug on my sleeve grows ever so slightly stronger."
    mc mf "Well-"
    show aika ea
    "I start to speak, but Aika beats me to it."
    a mf "And how have you been, MC?"
    show natsuki e1a 
    a smug mb "Been a hot minute since our lunch chat, hasn't it?"
    show aika ma
    mc ldown mg "Yeah, you could say that..."
    show natsuki me
    "Natsuki looks over at us from behind me, as if she's about to say something, but ultimately doesn't."
    show natsuki md b1a
    a turned mb "What about you, Natsuki?"
    a rhip mf "Student council holding up?"
    show aika ma
    n nb mg b3a "O- Oh, you know."
    n cross e2a b1a na mh "Just busywork with Chiaki and the like..."
    n b3a e1a mb "And I do mean busywork. Sometimes, we're up to our necks in papers."
    show natsuki ma
    a rdown eb mb "Oh, believe me, I know what you mean."
    show aika me ea nb
    show natsuki turned mj b1a 
    camera master at Move((0, 4), (0, -4), 0.10, bounce=True, repeat=True, delay=0.275)
    play sound smack volume 0.7
    "Just then, we hear the thump of a box hitting the ground from a small height."
    vp "There, your {b}donations{/b}."
    "Before any of us can respond, the girl's footsteps echo as she walks away."
    a ed mg nb "Wh- Kei-!"
    show aika me ea na
    n rhip e2c mg "It's fine. Tell her we said thanks."
    show natsuki e1a md
    "Natsuki shrugs herself off, moving to pick up the box, but before she can, it's already in my hands."
    n rdown b1d mg "Hey! That was my job, you know?"
    show natsuki md
    mc ed bm ml "Really? You {i}don't{/i} want someone else to carry the box and give you less work?"
    n b1d e3c mg "Sheesh..."
    show aika ma
    n b3a e2c mh "I'll... open the door for you."
    show natsuki md at thide
    hide natsuki
    "Natsuki walks on ahead, leading the way."
    show aika mb at thide
    hide aika
    a turned mb "Check out our festival if you've got the time~"
    _mc ec ma ba "Sly girl, still advertising even when she's this busy."
    mc mb ea "I shan't make any promises I wouldn't be confident I can keep!"
    _mc ec ma "She should have heard that."

    stop ambient fadeout 2.0
    stop music fadeout 2.0
    scene bg school_corridor_1_afternoon with wipeleft_scene
    $ advance_date(minutes=5)
    play ambient int_day

    "After walking about half-way back to the clubroom, I decide to peek inside the box."
    "Quite a few tiny microphones and speakers sit within."
    show natsuki turned mj:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    "I then lift my head back up to ask Natsuki something."
    $ renpy.music.set_volume(1.0, 0.0)
    show natsuki md
    mc turned messy mg "Hey, Nat, why are you so close with Sayori, anyway?"
    n lhip b3a mh "Well, she's nice to me. I enjoy her company, she's smart, and talented, and she enjoys manga and anime."
    n ldown mm b1a e1b "Wait, what did you just call me?"
    mc ed bm mg thinking "I mean, that's all well and good, but it must have only been in the past couple of years, right?"
    n cross e1d mh "Oh yeah, sure, fine, just ignore me."
    show natsuki ma e2c b1a
    "She rolls her eyes and shakes her head, a small smirk crossing her face."
    n turned b3a e1a mh "Well, I met her on my first day of high school."
    n lhip b1a e2a mb "I didn't know anyone here, see, so she just walked over to me and introduced herself."
    n e3c mg "It seemed like she had a lot of friends, so it surprised me that she spent so much time with me, but eventually I got used to it."
    n e2c ldown mb "Besides, it wasn't like I was complaining or anything."
    show natsuki ma
    mc md ldown ba "Yeah, she sorta grows on you, doesn't she?"
    n mb e3c "Hah, you can say that again."
    n e1a mh "But, to my confusion, she never left. Never went back to her friends, never said... well, anything."
    n e3c mi "Whenever I'd ask about her friends, all she would ever mention was this one person. The one that she grew up with, the kindest, smartest, most incredible person in the whole world."
    n e1a b3a mb "And when she did, her face would just shine. It was a while before I realised, she talked about them, the same way that I talk about her."
    n cross e2a b1d mc "Sayori... She's stood up for me. She's had my back these past three years. I couldn't imagine how high school would have turned out without her."
    show natsuki ma
    mc ef mb "Honestly, I couldn't imagine life without her."

    play music myconfession
    stop ambient fadeout 2.0

    n turned e1a b2a mg "Then why?"
    show natsuki e1a tears_a md
    "Natsuki looks at me, and small tears start to well in her eyes."
    mc ec ml "Because I was afraid. I was afraid of hurting her."
    mc ef mb bi "Well, you can see how that turned out."
    $ autofocus.block("natsuki")
    n b1d mj nb e3c notears lhip "..."
    $ autofocus.unblock("natsuki")
    n ldown e2a mg na "She doesn't have any friends, you know?"
    n e1a mh b1a "Outside of the club, I mean."
    n e2c mb b2a "We would hang out all the time after school, but even that stopped pretty abruptly too a while back."
    show natsuki mj 
    mc mj bg "Ah, her parents..."
    n b1d e1a mg "Huh?"
    show natsuki me
    mc ea ba mg nb "Oh, ah, nevermind."
    mc ef ml na "It's something she'll tell you when she's ready."
    $ autofocus.block("natsuki")
    n md "..."
    $ autofocus.unblock("natsuki")
    n cross mg e1d b1d "Do you think she doesn't trust me?"
    show natsuki b1a mj e1a
    mc ba ml "No, I think she trusts you more than even me, at the moment."
    mc ea mg "It's something I discovered through necessity, rather than good faith."
    mc mf "But..."
    mc eg ml "I'm sorry, I can't tell you any more than that."
    mc ea bg mb "Just know that she really, really likes you, Natsuki."
    n e2a mg "... I know."
    show natsuki mj
    n mh "Deep down, I've always known that."
    n me b1d "It's just..."
    n turned e3c b3a mi "Sometimes, I think to myself, what did I do to deserve someone so special, thinking so highly of me?"
    show natsuki mj
    mc ef ba mh "..."
    mc mf "Me too."

    stop music fadeout 2.0
    scene bg club_afternoon with longfade

    "After we return with the gear, I bite the bullet."
    _mc turned messy ec bi mh "I'm going to fix this. I {b}have{/b} to."
    _mc eg "If I don't start thinking for myself, I'll go mad."
    show monika turned mc:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "I tap Monika on the shoulder, interrupting her paperwork."
    mc ea ba nb mg "Can... Can we talk?"
    show monika ec ma with say_dissolve
    "She smiles warmly at me, giving me a nod."
    m ea mb "Absolutely, MC. What's on your mind?"
    show monika ma with say_dissolve
    mc ef ml "N- No, I mean... Not here."
    show monika eb bc mc with say_dissolve
    "She looks around the clubroom for a second, probably weighing up the things on her mind."
    m ec md rhip "Sure. Come with me."
    show monika mc with None
    camera master
    show bg:    
        blur 0.0
    show yuri turned md lup:
        matrixcolor TintMatrix("#f1d6bb")
        i41
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        i43
    show natsuki turned md:
        matrixcolor TintMatrix("#f1d6bb")
        i44
    show monika rdown ea ba ma at i42 zorder 3
    with Dissolve(0.2)
    $ say_transition = False
    "Standing, Monika gives the club members a wave."
    $ autofocus.unblock("monika")
    m md lpoint "Sayori, would you mind taking charge of packing up? I'd do it myself, but-"
    show monika mc
    n cross e2a mi "We'll handle it, Monika."
    show natsuki mj with None
    hide monika
    hide sayori
    camera master:
        align (1.0, 0.25) zoom 1.5
    show bg:
        blur 2.0
    show natsuki e1a ma
    with Dissolve(0.2)
    "The girl throws me a knowing look as I offer a small nod."

    if fr_told_yuri:
        camera master:
            align (0.0, 0.1)
        hide natsuki
        show yuri ma
        with Dissolve(0.2)
        "Yuri does the same, a smile crossing her features."
    
    camera master
    show bg:
        blur 0.0
    hide yuri
    show monika turned ec:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    with Dissolve(0.2)
    $ say_transition = False
    "Monika stacks her papers into a neat pile and places them into a filing cabinet, before turning to face me."
    $ autofocus.unblock("monika")
    m mb ea "Shall we?"
    show monika ma at lhide
    hide monika
    "Offering her a nod, she steps out of the room, with me following in tow."

    scene bg music_class_afternoon with wipeleft_scene
    show monika turned bc ec mc:
        matrixcolor TintMatrix("#f1d6bb")
        t11

    m mb "This should do~"
    show monika ea ma ba
    "After leading me to the far end of the building, she steps into one of the music rooms."
    m rhip md eb "These are built to dampen sound, so it should be enough to keep our conversation private."
    show monika mc with None
    show monika rdown:
        xcenter 0.3 zoom 0.8 ypos 1.0 yanchor 0.95
    show bg:
        align (0.0, 0.5) zoom 2.8 blur 2.0
    camera master:
        align (0.0, 0.2) zoom 1.6
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "She sighs as she sits upon the piano stool."
    m ea md "This is about reconnecting with Sayori, yes?"
    show monika mc with say_dissolve
    mc turned messy mg "It is, but it's also not."
    m eb md "I'll let you find the words and start from the beginning."
    show monika ea ma with say_dissolve
    "She gestures for me to start when I'm ready."
    "It only takes me a moment to find the words."

    play music pensive

    show monika mc with say_dissolve
    mc ef ml "I'm lost. I feel so..."
    mc eg bi mb "Two weeks ago I didn't have to worry about friends, or relationships, or talking with people, or-"
    mc ea ml nb bb "-I just-"
    mc bg mb "I don't know what to do."
    m bb mb "Slow down. What is it that's getting to you?"
    show monika mc with say_dissolve
    mc eb bd mg "E- Everything! And yet-"
    show monika ba with say_dissolve
    mc mm eg bi "I feel so stupid. I know what I have to do, I've known for a long time, but how do I- Why do I-"
    mc ef mh "..."
    show monika ma with say_dissolve
    "Monika says nothing, simply waiting patiently."
    show monika mc with say_dissolve
    mc eg mg "I feel like I'm spinning my wheels. I don't know what to do, and I've been so lost for so long that it's hard for me to really grapple with anything anymore."
    mc eb bd "I'm supposed to be an adult, supposed to be able to take care of myself and feed myself and clothe myself and pay my bills and-"
    mc ea bg "-So why is this so hard?"
    mc "What do I do?"
    m rhip md "... I'm afraid I might need a little more context than that, but it sounds to me like you're struggling with some personal matters?"
    show monika mc with say_dissolve
    mc mb na "You've known her forever, Monika. Out of anyone, you're the one who can step back and see things for what they are."
    m rdown eb bc md "If you're after advice, I'm not quite sure what to start with without knowing who or what-"
    show monika nb ea ba mc with say_dissolve
    mc ba nb mg "Sayori. I- I'm in love with Sayori."
    "Monika blinks at me, stupefied for a brief moment."
    m md "I- Well, that's-"
    show monika mc eb with say_dissolve
    "She looks to the wall, then to the piano to her side."
    m na "..."
    m ea bc md "For how long?"
    show monika mc ba with say_dissolve
    mc ef ml na "... Since we were about twelve."
    mc ea bb "At least, that's when I realised."
    m bc md rhip "Right."
    m eb bb mb "Y- You know, normally when people say these kinds of things, they say it's 'a friend' or something-"
    show monika ea mc ba with say_dissolve
    mc ed bg ml"Monika, please."
    show monika bc rdown with say_dissolve
    "She meets my gaze once more."
    m nb md ba "Then you're serious. I- Well, I don't know if she reciprocates, but there's a chance that..."
    show monika mc eb bb with say_dissolve
    "Her words drift off, the room deadening the sound before they properly reach my ears."
    m md "... I can't assure you of anything."
    show monika mc with say_dissolve
    mc ea mg nb "That's not what I... L- Look, just want some advice."
    m bc md na "I- MC, this isn't really my field of expertise-"
    show monika ea ba mc with say_dissolve
    "In her motion to brush me aside, she accidentally locks eyes with me again."
    m bb md "... This is bothering you, isn't it?"
    m ba "Not just a little."
    show monika mc with say_dissolve
    mc ef ml "I wouldn't be here otherwise."
    m ec bc mb "Then... I'll do my best."
    show monika ea ma with say_dissolve
    mc eg mb  "... I appreciate it."
    show monika ec ba with say_dissolve
    "We both take a moment to breathe."
    show monika ea with say_dissolve
    mc na ml ea ba "Where do I start?"
    m lpoint md "How about the most recent development, rather than the beginning?"
    show monika ma with say_dissolve
    mc thinking ml "So that we can then work backward? Alright."
    show monika ldown ed with say_dissolve
    "She nods, clicking her tongue."
    m mb ea "Indeed."
    show monika ma with say_dissolve
    mc ef mg "Sayori... She's been my best friend for longer than I can remember."
    m ec md "The end, not the beginning, MC."
    show monika mc ba with say_dissolve
    mc ldown ea mg nb ba "Oh, right, right. Sorry."
    show monika ea with say_dissolve
    _mc eg bi ma "Seems I defaulted to the start of the story."
    mc ef ml ba na "She doesn't seem to... want to be around me at the moment."
    mc ea mg "Or, to be more specific, I don't know if I want to be around {i}her{/i}."
    m rhip md "Did you have a fight?"
    show monika mc with say_dissolve
    mc eb nb "No! No, no no, I just..."
    mc ml ea na "I don't know how to act."
    m bc rdown md "You don't know where you stand?"
    show monika ba mc with say_dissolve
    mc mb bb eb "Yes! That's exactly it!"
    m eb md "I see. Unfortunately, I'm a touch inexperienced with this..."
    m ea mb "But I know someone who is better with advice than I'll ever be."
    m bc eb md "... Unfortunately, I believe she's in the middle of an exam right now."
    show monika mc with say_dissolve
    mc ed bm thinking ml "... Okay?"
    show monika ba ec with say_dissolve
    "Monika shrugs, shaking her head."
    m md "{size=-3}Guess it's up to me, then...{/size}"
    m ea mb "MC, you've been hard at work with your studies, right?"
    show monika ma with say_dissolve 
    mc ed md ba ldown "Of course. You don't keep Rank 4 without the legwork."
    m mb "And how much of this study has revolved around interacting with your peers?"
    show monika mc with say_dissolve
    mc ec ml "... None."
    m bc md rhip "So..."
    show monika ba mc with say_dissolve
    mc ea mg "Yeah. That's... That's the problem, truthfully."
    mc ml ef bg "I'm just not confident in my ability to be a teenager."
    mc ea ba mg "The only person my age, before I joined the club, that I interacted with was Amelia."
    mc bi eg mb "... And she's not exactly winning any awards for being well-adjusted."
    m md "Amelia...? Sorry, I don't believe I'm familiar."
    show monika mc rdown with say_dissolve
    mc mg ea ba "She's in Aika and Natsuki's classes - Other than Chemistry."
    mc ml thinking "Blonde hair, president of the 'Going Home Club'?"
    show monika ec bc with say_dissolve
    "Monika shakes her head."
    m ea ba md "No, sorry."
    show monika mc with say_dissolve
    mc ldown eg ml "It's fine, it's not really relevant anyway. Just know that my circle is small and insular."
    mc ef mg "And now I'm faced with the prospect of joining in activities that are much bigger than I am, and..."
    mc ea bg ml "I'm scared."
    m md rhip "It's not just the Culture Festival?"
    show monika mc with say_dissolve
    mc mg ba "No, I'm not opposed to public speaking when it boils down to it, I just..."
    mc mb bg "It's the 'getting to know people' part that trips me up."
    show monika ma rdown at i11
    show bg:
        blur 0.0 zoom 1.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    "She grins, standing up."
    $ autofocus.unblock("monika")
    m mb "So that's what you really wanted my help for."
    show monika ma
    mc ef ml "Yeah. I'm just scared that if I do something stupid, she'll... we'll go back to the way we were."
    m mb rhip bb "I understand now. MC, you're not alone, alright?"
    m ba md "Whenever you feel isolated and alone, that's just the demons in your mind. The other club members want to support you, yes?"
    show monika ma
    mc ea ba "I take it they've told you then?"
    m rdown md "Everyone's been worried about you, MC, but I see that there's no need."
    m mb "You sought out help, and that means you're ready to start being more active in your own destiny."
    show monika ma
    mc ef ml bg "That's my hope."
    mc ea mb bf "All I really needed was... someone to help me coalesce my thoughts."
    m lpoint ed mb "Happy to help~"
    show monika ma
    mc eh md ba "I don't know what I'd do without you~"
    m ldown ea mb "Remember, MC. The club is more than just a daily gathering. We're a family."
    show monika ma
    mc ed "I'll not forget it~!"
    show monika ec at t55
    "She walks past me, her white ribbon wafting behind her as she moves to the door."
    m bc ea mb "Coming? If we stay much longer, Natsuki might catch us on one of her patrols and give us a detention~"
    show monika ma
    mc bg mb eh "Detention with you? Oh, the calamity~!"
    show monika ed ba
    "She chuckles as she slides open the door."
    m mb ea "It certainly would be, spending all that time locked in a room with one of my club members~"
    show monika ma
    mc ea mg ba "Not unlike a certain club time?"
    m ed mb "Not unlike a certain club time~"
    show monika ma at thide
    hide monika
    "I can't contain a giggle as we vacate the room."
    "Seems I was right to change my stance - I need to be more clear, and before anything else, I {i}need{/i} to sit down and talk with Sayori about all this."
    "Before we decide anything, we need to have that conversation."  

    stop music fadeout 2.0
    scene bg mc_living_room with Fade(1.0, 0.6, 1.0)
    $ set_internet(True)
    $ set_date(hour=17, minute=22)

    "Shaking my head, I finally manage to trudge through the front door."
    _mc turned messy ec mh "That was a long day, if I'm honest."
    _mc eg mj "Too long."
    _mc ea mh "After what happened with everyone today... I'm honestly glad I was able to talk it out with Monika, rather than getting yelled at again."
    _mc ec "But, Sayori..."
    _mc ef "I didn't say a single word to her."
    _mc "Not a one."
    _mc ec "On the entire trip home, not even a greeting or goodbye."
    _mc ea thinking "Not that I didn't want to, mind you."
    _mc ef mf "I just..."
    _mc eg mh "After what Natsuki said to me..."
    _mc bi ldown "I just couldn't find the right way to start."
    _mc ec ba "I'm going to think carefully about what words to say while I take a shower."
    _mc ea "Where that conversation starts."
    _mc eg "Then I'll let Sayori decide. Until then, I'm not going to assume anything."

    stop music fadeout 2.0
    scene bg mc_kitchen_day with fade
    $ set_date(hour=18, minute=7)
    play ambient int_night

    "After my long, probably too long, shower, I remember that I have work tomorrow."
    "After that sobering thought, I start to throw together something for dinner."
    "It may still be really early for it, but honestly, I'm just keen for this day to end, even if it means I need to work sooner."
    "And if I make a large enough meal, I can have it for dinner before the sleepover tomorrow as well."
    _mc turned messy casual "Oh yeah, Sayori's sleepover tomorrow."
    _mc eg "I should probably do something about that."
    _mc mh "Hell, is there anything I can do? Other than talk it out with Sayori?"
    _mc ec "I don't think we'd be able to go that long without letting everyone in on there being something going on with us."
    _mc eg "So best to resolve it sooner."
    _mc bi "Dammit."
    _mc ec ba "That does mean, though, that I can't just go to bed tonight, now's the only time I have left between now and then.."
    phone register "mc_s":
        time auto True
        "s" "We need to talk."
    play sound phone_notification
    "As I start throwing some vegetables together, preparing to blend a stew, I feel my pocket vibrate."
    "Curious, I place the veggies into the pot, and pull out my phone."
    "There's a text message there."
    phone discussion "mc_s":
        pause
    phone end discussion

    scene black
    show bg mc_living_room
    with Dissolve(1.5)
    $ advance_date(minutes=40)

    "After finishing dinner, I place myself on the floor, legs crossed."
    "It's an old technique my father taught me before he left, something I use to fend off stress."
    "I still haven't found exactly what I want to say, but I think I'm starting to find it."
    "An old form of meditation."
    "Sayori will be around sometime after she finishes her own dinner, and there's no way I'll be able to do anything else but worry until then."
    "The carefree Sayori had been so serious in our short talk over the phone earlier."
    "It's time I face her head-on, and talk this out."
    "But with no other way to kill my time, I simply wait."
    "I feel my breathing slow, and my heart-rate dip along with it."
    "Like a turbulent hurricane, my emotions wash over me, barraging me with all of that which had tormented me for so long."
    "Flinching with each wave, my heart is assailed with the pain I've inflicted on myself, every day, not being able to see Sayori but through a window."
    "My previously open palms clenched into fists, as I relive the day that started it all."
    "And slowly, every day since."
    "Even the light at the end of the tunnel, being reunited with her, is met with a sour bite."
    "I've done nothing but wallow in my own shame since."
    "Even with her support, it's been too much for my weak soul to handle."
    "I feel myself washed away with the torrent of wind, buffeted by every last chance I had to talk to her over the past three years."
    "Every opportunity to make it right."
    window hide Dissolve(0.4)
    play sound ["<silence 0.8>", audio.fall]
    stop ambient fadeout 2.0
    show sayori turned zorder 5:
        i11
        alpha 0.0
        easeout_quart 0.8 alpha 1.0
    show white:
        alpha 0.0 
        0.65
        easein 0.12 alpha 1.0
    pause 3.3
    hide sayori
    window auto show Dissolve(0.5)
    "And, all at once, the tempest halts."
    "All of the pain vanishes, in an instant."
    "I feel warmth, unlike anything I'd known."
    "It feels like..."
    mc turned messy casual mf "Sayori."
    hide white with NonBlockingDissolve(4.0)

    play music wtdgi

    "Slowly, I feel myself return to my body, and with it, my senses, with haste."
    "There's a wetness on my shoulder."
    "I smell a cool, soft air of roses."
    "I feel a slight constriction around my arms, and softness upon my cheek."    
    show bg:    
        blur 2.7
    hide black
    camera master:
        align (0.5, 0.2) zoom 2.0
    show sayori turned casual lup rup mk b2c nb e3c tears_b at i11
    with Dissolve(0.5)
    "Opening my eyes, I see her."
    "As she sobs into my shoulder, the ribbon in her hair shines, like the light, glinting at the end of the far-off tunnel."
    show sayori e2a notears b2a md nd ldown rdown
    camera master:
        zoom 1.0
    show bg:
        blur 0.0
    with Fade(1.0, 0.1, 1.0)
    $ advance_date(minutes=15)
    "After an eternity in each-other's arms, Sayori finally pulls away, and we get up off of the floor."
    "Her eyes are red from the sobbing, and I can't help but wipe the remaining tears from her face."
    show sayori e1a tears_a
    camera master:
        zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "In the softest voice I can muster, I bring my hand to her cheek."
    mc bg ml "Hey, no need to cry, alright?"
    mc mb "I'm right here."
    show sayori lup e3c b2b with say_dissolve
    "Through the sniffles, she responds."
    s me "But..."
    s mg "You weren't."
    s e1a mh b2c ldown "You weren't when I needed you most."
    s ml "You left me, Melody."
    s e3c tears_b b2b mm "You abandoned me, just like my own family."
    s mk tears_a "Just like yours."
    s e2a b2a mg "Will..."
    s e1a mh nb "Will you abandon the club, too?"
    show sayori md with say_dissolve
    _mc ec ba mh "So that's what this was all about."
    _mc eg bi ma "I really am a monster."
    _mc "After all this time, I couldn't even see that I'd hurt her so badly."
    _mc ef ba mh "I'd caused all of this pain for her, and I'd been too busy with my own to see it."
    _mc ec "I don't deserve her."
    _mc eg "But here I am."
    _mc "I don't think I'll ever be good enough for her."
    _mc ea bg "But Natsuki believes in me."
    mc ef ml "Sayori..."
    mc ea bf mg "I'm so, so sorry."
    mc ef bg ml "Words cannot do justice to just how sorry I am."
    mc eg mg "This, everything, is all my fault."
    show sayori e3c notears mj na
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Sayori pulls away from me."
    $ autofocus.unblock("sayori")
    s e2a mg "Did you think that I wanted an apology?"
    s e3c mh nb "Some hollow promise that it won't happen again?"
    s ml nc b2c e1a tears_a lup "You left me."
    s mk tears_b nd "You let me rot for five years, Mel."
    s e2a tears_a b2b mh nc "I should be mad at you."
    s e2a mg nb notears "I should be furious."
    s md "..."
    show sayori ldown e3c na me at dip
    "She sighs, more at herself than at me."
    s mg "But I'm not."
    s e1a mb b2c "I never was."
    s mg "I never could be."
    show sayori mk e3c b2b at dip
    s "All I am, Melly, is scared."
    s e1a tears_a lup b2a mg "Scared that you'll do it again."
    s me e2a "Scared... that I'll lose you."
    show sayori b2b e3c rup mm nc at dip
    s "I can't go through that again."
    s e1a tears_b ml b2a "Please, {i}don't make me go through that again!{/i}"
    show sayori mm 
    "The tears well in her eyes once again."
    mc ec bi ml "I won't."
    "I'd already made my decision. I hadn't thought about it that way before, but honestly, I'd made my decision long ago."
    mc ea bg ml nb "I'm sorry, Sayori."
    show sayori mj tears_a rdown ldown
    mc ef "I'm sorry that I hurt you."
    mc bf mb "I know I haven't been the best friend to you..."
    show sayori e2a b1b notears bags md nb
    mc ea be na "But please, let me make it up to you."
    $ autofocus.block("sayori")
    s me "..."
    $ autofocus.unblock("sayori")
    s mg e3c na "Again, with the empty promises."
    s mh lup e1a "How do I know you aren't just going to run off with Natsuki, or Monika, or Yuri?"
    show sayori md
    mc nb bd mg "Why would I do that?"
    _mc mh bf "She really doesn't trust me."
    _mc ef bg "I just wish it wasn't all warranted."
    s e1a tears_a mg nobags b2b "Because I'm just..."
    s mb b2a "Me."
    show sayori ma
    "I can't bear to see her crying anymore."
    show black
    hide sayori
    with NonBlockingDissolve(1.0)
    "It's barely a moment after our eyes meet, that our lips follow suit."
    _mc ea na ba mh "Words?"
    _mc ec "Those can be faked."
    _mc "We both know that."
    _mc eg "If I want her to never doubt herself again, I needed to convey that."
    "It doesn't take long for our heart-to-heart to devolve into this."
    "I lose myself to her, my fingers disappearing into the softness of her hair."
    "My arms, wrapped around her, wishing never to let go."
    "Sayori's breathing is laboured, hot, and heavy."
    "Her shirt has slipped down to one side, exposing a large portion of her arm."
    "I reach to place it back, but she instead takes my hand."
    s turned casual e3c notears b1b mb na "Don't bother with that..."
    "Something in the way she speaks, oozing with a soft, yet sweet tone, causes me to almost recoil."
    _mc eb bd "Is this really Sayori?"
    _mc "My sweet, bashful childhood friend?"

    scene black with Dissolve(1.5)

    "Taking my hand, she gently walks up the stairs."
    "I follow, allowing the conflicted feelings to well within me, before stuffing them out." # im stuff
    show bg mc_house_corridor_day
    show sayori turned casual md b2b at i11
    hide black
    with NonBlockingDissolve(0.7)
    "Arriving outside my door, she looks deep into my eyes."
    s me "You'll..."
    s mb "You'll stay with me, right?"
    s b2a lup "And no matter what happens, you'll trust me, right?"
    show sayori ma with None
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    $ say_transition = True
    "I look her in the eye."
    mc turned messy casual ml bi ec "I will."
    $ autofocus.block("sayori")
    show black with NonBlockingDissolve(1.0)
    "I don't know what makes me scoop Sayori up into my arms and carry her across the threshold of my room doorway."
    camera master
    show bg mc_bedroom_night_closed_on:
        align (0.0, 0.5) zoom 1.2 blur 1.0 
    show sayori lup rup b1a e3d mo:
        matrixtransform RotateMatrix(0, 0, -80) * ScaleMatrix(2.0, 2.0, 2.0) * OffsetMatrix(-60, -100, 0)
        xalign 1.0
    hide black
    with NonBlockingTransition(fade)
    s "Eeee! Ahahah! What's this all about?"
    "Perhaps I'm trying to relieve the tension that's hung so cloyingly over the entire day like a toxic miasma."
    show sayori e1a ma with say_dissolve
    mc ed md ba "Don't you remember? You always used to enjoy it so much whenever I picked you up and carried you." 
    mc eh mb "Over storm drains, puddles... the spots of imaginary lava on the floor."
    show sayori md e1b with say_dissolve
    mc ed md "And judging from that excited giggle, I think you still do."
    s e2a mb b2b "I... I have the right to remain silent~"
    s mn b1a e3d "It feels so much like old times... which I've always remembered. Makes me happy you do, too."
    s mb e1d "And yet, tonight... It's somehow also enjoyable in a different sort of way."
    show sayori ma with say_dissolve
    "Or perhaps I'm doing so in recognition of what this moment signifies."
    "The moment when seven years' worth of indecision, fumbling, hemming and hawing at long last melt away."
    "Replaced by both clarity of thought and purposefulness of action."
    "The long-awaited consummation of an intimate bond lasting well over a decade."
    "A moment almost akin to a wedding night."
    "Whatever my true motivation might be, the giddy light in Sayori's eyes, which shine like two sapphires in the dark?" 
    "It makes that sudden move of mine completely worth it." 
    show bg:
        easeout_cubic 1.2 zoom 1.75 align (1.0, 1.0) blur 0.0
        easein_back 0.2 zoom 2.0
    show sayori:
        easein 1.1 alpha 0.0
    play sound ["<silence 1.3>", audio.fall]
    show black onlayer above_master:
        alpha 0.0
        1.35
        ease 0.2 alpha 1.0
    mc "I'll show you just how enjoyable things can get. Alley oop."
    hide sayori
    s turned casual mb xd b2a "Kyaaahahahah! Warn me before you toss me onto the bed like that, will you?"
    show sayori ma
    mc eh bb "Tch. Where's the fun in spoiling~"
    hide bg
    show expression Gradient("#7f7870", "#979089")
    show sayori b2b mo e3d:
        matrixtransform None zoom 2.0 ypos 1.0 yanchor 0.53 xalign 0.5 alpha 1.0
    hide black onlayer above_master with {"above_master": Dissolve(3.0)}
    "Before Sayori can squirm aside, I've deposited myself practically on top of her." 
    show sayori e1d nc ma b1a with {"master": say_dissolve["master"]}
    "And amidst a cacophony of squeals, laughs, gasps and pants, our embracing begins anew."
    "It takes mere seconds for cheeky tickling and mischievous wrestling to segue into a much less chaste blend of playtime."
    show sayori b1b e3c with {"master": say_dissolve["master"]}
    "Sayori's eyes flutter shut as our mouths hungrily reunite, and the night is only growing younger." 

    stop music fadeout 3.0
    scene black with Dissolve(2.0)
    pause 2.0
    $ advance_date(hours=2)
    play music dawn fadein 3.0

    "I allow myself a slight smirk of satisfaction."
    "I can't help but be pleased with myself over what I've managed to achieve."
    show sayori turned naked mn b2a nd e3d:
        zoom 2.0 ypos 1.0 yanchor 0.53 xalign 0.5
    show expression Gradient("#7f7870", "#979089")
    hide black with NonBlockingDissolve(0.5)
    "Sayori must notice my air of smugness, for she opens her mouth in a half-smile of her own amidst her heavy panting, as if on the verge of saying something..."
    show sayori md e2a b2b nb with say_dissolve
    "... Only to swiftly clam up, smiling no more, another wave of doubt clearly starting to creep in."
    mc turned messy nostrands naked nb mg bf "What's wrong?"
    s mb e1d b1b na "I was about to ask you just where you learned how to do things like that."
    s mg e2a b1a "But the thought of you... working up experience with somebody else..."
    s e3c b1d mm "It's the last thing I want permanently taking up residence in my brain."
    show sayori mj with say_dissolve
    mc ba nc ed mb "Beginner's luck is all it is. Honest."
    s e1d mh b1b "You'd sure as hell better not be lying, Melody."
    s mg e2a "Because if there was anybody else..."
    show sayori md with say_dissolve
    "Her voice trails off and she looks away, her moody pout equal parts adorable and heartrending."
    mc bg ea na mg "Hey."
    show sayori e1a b1a me 
    camera master:
        align (0.5, 0.2) zoom 1.2
    with Dissolve(0.2)
    "I drew her close for a cuddle."
    mc eg ba mb "There never was. And there never, ever will be."
    show sayori e1b b2b me with say_dissolve
    "Sayori stiffens at first as I encircle her with my arms."
    show sayori lup rup mo e3d b1a with say_dissolve
    "But as soon as the headpats come into play, she's a snuggly little blob of custard once more."
    "I dare not to mention what revelations that had come to bear fruit on this eve; the fabric and foam on the floor speak for themselves, and I'm sure she would much rather not be reminded of such a thing in a moment like this."
    _mc bg ea mh "... Sayori. The fact that she feels the need to... resort to such measures for her own self-worth fills my heart with a sensation I cannot quite describe."
    _mc ef "Pads. I'd hardly even seen one before today. Sure, I may not have all that much, myself, but considering how much time I've spent over my teenage years worrying about how to live to the next day, it never really... crossed my mind."
    _mc eb bf "Now, however, I hold doubt I'll ever manage to banish the thought at all. I'm not that much larger than her; what if that's not big enough?"
    _mc mm eg bi "N- No, Sayori told me herself that it was fine, I should... I mean, I want to trust her, but what would she know? Hell, what would {i}I{/i} know? It's..."
    _mc eb be nb mh "What if she was just saying that? What if she only said it to make me feel better?"
    _mc ec bg na "When I told her it was okay, I meant it. I truly did. Maybe I'll just have to trust that she would do the same for me."
    show sayori md e1a with say_dissolve
    "..."
    camera master
    show sayori ldown ma b2b
    with Dissolve(0.2)
    "Sayori looks up at me, her fingers gently running through my hair."
    s mb "You okay?"
    show sayori md with say_dissolve
    mc ef mb bf nb "Y- Yeah, I just... got thinking."
    s e2a mg "Ah..."
    show sayori ma e1a b2a with say_dissolve
    "She places her hand upon my face, a soft, warm smile eking across it as she does."
    s e1d b1d mh "Well, you tell those bad thoughts that they aren't welcome when I'm around, okay?"
    show sayori ma e1a b1a with say_dissolve
    mc eg ba na mb "Yeah. I will."
    show sayori mn e3d with say_dissolve
    "Again, a playful boop on the nose, triggering that magnificently musical titter of mirth."
    s rdown "Ehe~."
    show black with NonBlockingDissolve(2.0)
    "We find ourselves curled up, near-motionless, in one another's embrace."
    "Floating, basking, peacefully in that delicious half-awake, half-dreaming state that accompanies a rosy, mellow afterglow."
    "The previous days' doubt and conflict cast to the aether and gone."
    "I smile contentedly into Sayori's auburn locks, inhaling deeply of that strawberry aroma, that ambrosial scent."
    "Once again, everything is right with the world."
    "Right with our bond."
    "My bond with Sayori."
    "The best friend one could ever ask for."

    $ add_calendar_description(calendar_descriptions["sayori"][8])

    call week_2_saturday_sayori from _call_week_2_saturday_sayori
    return