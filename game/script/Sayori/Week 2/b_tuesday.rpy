label week_2_tuesday_sayori:
    call calendar_transition(day=31, hour=7, minute=54) from _call_calendar_transition_30
    scene bg residential_day with dissolve_scene_full
    play ambient ext_day fadein 2.0

    "As I close the front door, I sigh."
    "I didn't hear so much of a peep from Sayori all night."
    "I guess what happened yesterday really hurt her feelings."
    _mc turned bun nostrands ec mh "It's not that I blame her, but I just..."
    _mc ef "I want her to be happy."
    _mc eb "Like, she's my best friend, of course I want her to be happy."
    show bg s_house_day with Dissolve(0.5)
    "Stopping in front of her door, I move to knock, but pause."
    _mc thinking ea "Should I take her not talking to me as a sign that she wants to be left alone, or do I press her to make sure she's alright?"
    "My face curls into a grimace, and I turn my back."
    _mc ldown eg bi "When she wants to talk, she'll find me."
    _mc ef ba "Best to leave it up to her."
    
    stop ambient fadeout 1.5
    scene bg club_day with wipeleft_scene
    $ set_date(hour=15, minute=20)

    "School was uneventful, though Aika invited me to lunch again. We got some study done, so I can't complain, but..."
    "I know I'd much rather be hanging out with Sayori."
    "And as I sit inside the clubroom, reading, I can't bring myself to concentrate."
    show bg:
        align (1.0, 0.6) zoom 1.8
    show sayori turned e2a me b1b at i44
    with Dissolve(0.2)
    "There she is, on the other side of the room."
    "It feels like a world away."
    "She looks like she's reading, but I can tell that she isn't. She hasn't turned a page in over five minutes."
    "Maybe..."
    "Maybe she's bothered too?"
    "As much as I want to ask her what's wrong, I just..."
    "I want her to come to me when she has a problem, not just bottle it up."
    "Maybe if we talked about it, we would get somewhere."
    "I sigh yet again."
    
    scene bg club_afternoon with fade
    $ set_date(hour=16, minute=35)

    "After what could have been an eternity, simply gazing upon Sayori's sombre figure, I hear the distinct sound of Monika clapping."
    
    play music playwme
    
    show monika turned lpoint md:
        matrixcolor TintMatrix("#f1d6bb")
        t31
    m "Alright everyone, that's a wrap for the day. We went on a little late, so no group activity today."
    m ed mb ldown "I hope everyone has a good rest of their day, but I've gotta run, so Sayori, would you mind locking up?"
    show monika ma
    show sayori turned me:
        matrixcolor TintMatrix("#f1d6bb")
        t55
    "Sayori suddenly jerks up at the sound of her name."
    show monika ea mc
    s e1b b2a mg "Ah, wha- Huh?"
    show sayori md
    m md "Could you lock up, please?"
    show monika ma
    s e1a b1a mh nb "Oh, ah, sure, Monika."
    show sayori md
    "That was uncharacteristically unconfident for Sayori. She must really not be feeling all that hot."
    show monika at hop
    show sayori me lup na
    "Monika throws the keys toward Sayori, who proceeds to catch with the reaction time of roadkill."
    show monika nb mc
    show sayori:
        0.15
        "sayori turned lup xd ml nb b2c"
        hop
    show white at flash
    play sound ["<silence 0.15>", audio.slap]
    "The keys hit her directly in the noggin."
    s e3c mk ldown b2b "Uuuu..."
    show sayori md
    m mb bb "Ah, sorry Sayori! I should have given you a heads-up!"
    show monika mc na
    s b1a lup e1a mg "Ah, no, it's..."
    show sayori md ldown
    mc turned bun nostrands mb "It's alright, you run, Monika. You're pretty clearly running late. I'll take care of it!"
    m mb ba ed "Ah, thanks, MC! Shall do!"
    show sayori b1b e2c na at thide
    show monika ma at thide
    hide monika
    "With that, she proceeds to leave the clubroom."
    show yuri turned lup e2c md:
        matrixcolor TintMatrix("#f1d6bb")
        t51
    "Yuri quickly vacates the room, after glancing at Sayori with a look of slight concern, then to my expression."
    show yuri at thide
    hide yuri
    "She clearly doesn't want to bother us."
    hide sayori
    show natsuki cross me:
        matrixcolor TintMatrix("#f1d6bb")
        t41
    "Natsuki motions me over to her desk in the corner."
    show natsuki md at i42
    show bg:
        blur 2.0
    camera master:
        align (0.3, 0.25) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    "Not really wanting to confront Sayori just yet, as she appears to have fallen back into her deep thoughts, I oblige her."
    n turned e2c mh "Hey, what's going on with Sayori?"
    n e1d b1d mg "What did you do?"
    show natsuki md with say_dissolve
    mc bd ml "Me? What makes you think I did anything?"
    n b3a e1a mh "Well, I didn't see you two walking to school today. And Sayori was pretty late to class."
    n lhip e2a b1d mg "Not to mention..." 
    n b1a e1a mh "Ya know, that."
    show natsuki ldown e2c md with say_dissolve
    "She gestures toward Sayori."
    show natsuki e1a with say_dissolve
    mc ba ef thinking mf "Ah, that's fair."
    mc bd eb ml "Hold up. How did you know we didn't walk to school together?"
    n b3a mh "I... walk along the same route."
    show natsuki md with say_dissolve
    mc ldown ba ea ml "And you've never stopped us to walk with us?"
    n cross e2a b1a mi "Oh, it's not like I want to, or anything. Just something I've noticed."
    show natsuki mj with say_dissolve
    mc ml "Well, you're more than welcome to."
    mc ec mg bd "And, besides that, she has her own life. What actually makes you think that I did something?"
    n b1d mg "Well..."
    n turned e3c mb "Look, I won't tell anyone this, of course, but..."
    n b3a mh e1a "I saw you two walk out of your house together yesterday morning."
    show natsuki mj with say_dissolve
    mc bb eb nb mg "Wha-"
    show black with NonBlockingDissolve(0.2):
        alpha 0.5 
    _mc mf "Oh no."
    _mc nc "No no no no."
    _mc "This isn't happening."
    _mc "Oh, this cannot be happening."
    _mc "She SAW us?"
    _mc bc mh "Does that mean she thinks we..."
    hide black with NonBlockingDissolve(0.2)
    mc ba nb mg "Ok, whatever you saw, it isn't what it looks like."
    n e3c mi "Suuure."
    n lhip b1a e1a mb "I'm not going to rat you out, okay?"
    n ldown mh "I'm just saying, you need to be a little more careful. If someone from the school catches you, or your parents, or something, it could be pretty bad."
    show natsuki mj with say_dissolve
    "I grimace. The thought of my good-for-nothing parents giving even close to that much of a crap about me makes me more angry than I care to admit."
    "Though, I could say the same for Sayori's parents."
    mc ed bd ml na "Look. I'm glad that you noticed, and not someone else, but I'm telling you, it isn't like that. We're just... friends, alright?"
    n lhip e2a mh "I'm just saying, if you want some advice, feel free to come to me."
    show natsuki md with say_dissolve
    mc mh ec bi "..."
    mc ml ea bd "Why are you being so nice to me, all of a sudden?"
    n ldown e1b mm "Wh- Are you implying that I'm not nice?"
    show natsuki mj with say_dissolve
    mc thinking mg ba "Well, you're usually... how do I put this... a little abrasive."
    n nb mk b2a "!!"
    n b1d e1a mg "I-..."
    n cross e2a mb "I'm doing it for Sayori. Because I know she'd do the same for me."
    show natsuki ma nc with say_dissolve
    "At that, Natsuki blushes a little and turns away."
    "I can't help but smile."
    mc eg mb ba ldown "So that's what it was. You're a good friend, Natsuki. Thank you."
    n mg "It's not for you... or anything..."
    show natsuki md with say_dissolve
    mc ea "I know. But thank you regardless."
    n b1a mh "Just... You better apologise for whatever you did before tomorrow, alright?"
    show natsuki mj with say_dissolve
    mc eg "I will, don't worry."
    hide natsuki
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    "Natsuki scurries out of the room, leaving just myself and Sayori."
    show bg:
        align (1.0, 0.6) zoom 1.8
    with Dissolve(0.2)
    stop music fadeout 2.5
    "Or so I would have thought."
    mc eb mh "Wait, where'd she go?"
    mc eg bi mm "She was in charge of locking up, dammit!"
    show bg:
        zoom 1.0
    with Dissolve(0.2)
    "Finding the keys left exactly where they fell, I grab them, lock up, then head out."
    "If I want to catch her, I'd better move quickly."

    scene bg school_street_afternoon
    show sayori turned e2c b1b md:
        matrixcolor TintMatrix("#ffeede")
        i55    
    with wipeleft_scene
    $ advance_date(minutes=10)
    $ autofocus.block("sayori")

    mc turned bun nostrands eb nb mg "Sayori!"
    mc bb "Wait up!"
    "Sayori is moving quite quickly down the road."
    "I get the feeling she's avoiding me, and I know I said I'd give her space..."
    "But I just..."
    "I can't bear to see her like this."
    "So here I am, chasing hopelessly after her."
    mc "Sayori, please, just listen to me!"
    mc ea ba "You don't have to stop, I just wanted to apologise!"
    mc ef bi "I wasn't thinking, you know that! Just..."
    mc ea be "Please, let me make it up to you..."
    show sayori e3c at t44
    "Sayori's running slows."
    show sayori e1a at t11
    "She turns slowly around to face me."
    s "..."
    "As I run to reach her, I hold something out."
    show sayori e1b b2a me
    "When her eyes come to rest upon it, her face morphs into one of confusion."
    $ autofocus.unblock("sayori")
    s mg "But..."
    s e1a lup mh b2b "You said you didn't..."
    show sayori md
    mc eg bg ml "I know what I said. And I was wrong, and I'm sorry."
    mc ea be mg "Please, just let me make this up to you."
    $ autofocus.block("sayori")
    s b1b ldown "..."

    play music daijoubu

    $ autofocus.unblock("sayori")
    s b1a mh "Alright. The usual, I take it?"
    show sayori ma
    mc mb "Yeah. Just like old times."
    s mh "Okay. I need to run home to sort some stuff out, so I'll meet you at yours in an hour?" # im stuff
    show sayori md
    mc na ba "Yeah, absolutely."
    s mg "I'll see you then."
    show sayori md at thide
    hide sayori
    "With that curt reply, she jogs off."
    "I'm left standing in the middle of the footpath, gazing at her back."
    _mc thinking ec mh ba "Did I do something wrong, again?"
    _mc ea "Why is she so upset with me?"
    "With those questions at the forefront of my mind, I head back toward town."
    "I have some shopping to do."

    scene bg mc_living_room with fade
    $ set_date(hour=17, minute=47)

    "I arrive home, bag in hand."
    "Sayori won't be long; just gotta make sure everything is ready."
    "Loading up the old TV series, our favourite, I set the bag onto the coffee table."
    show black with NonBlockingDissolve(0.3)
    "I slowly unpack everything, taking as much care as I can muster."
    "Once I finish, I fetch some glasses from the kitchen, laying them onto the table."
    "Smiling, I dust my hands off, symbolising to myself that my work here is done."
    "I take a deep breath, and brush down the couch, preparing it for the arrival of the most important of visitors."
    hide black with NonBlockingDissolve(0.3)
    $ set_date(hour=18, minute=5)
    play sound door_knock
    "Not long later, I hear a knock on the door."

    scene bg mc_house_entrance_afternoon with wipeleft

    "I rush over, and before answering, I take a moment to brush myself off."
    show sayori turned:
        matrixcolor TintMatrix("#ffdfc0")
        t11
    "I open the door, and see Sayori standing in front of me."
    s mn e3d "Sorry I'm late~ I got caught up in something, but it's all sorted now, ehe~"
    show sayori ma 
    "Her grin starkly contrasted the face she had worn just over an hour ago. It was almost impressive how quickly her mood could swing."
    mc turned bun nostrands mb "No, it's alright. It's still warm."
    show sayori at thide
    hide sayori

    scene bg mc_living_room with wipeleft
    show sayori turned e3d at t11

    "Sayori steps inside, placing herself squarely in the centre of the couch, before kicking her legs up, taking up the entire space."
    "I can't help but grin."
    "She's a lot taller than she used to be. I used to still have room to sit where her feet are, but no more."
    show sayori e1a rup at dip
    "As I move over, she sits up, motioning for me to sit where her head was."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show sayori rdown
    with Dissolve(0.2)
    "I oblige, expecting her to sit on the couch like a normal person."
    "I pour both of us a glass of soft drink, before I notice she hasn't moved."
    show sayori lup e3c with say_dissolve
    "She takes the glass from me, placing it on the table, and then does something I never expected:"
    show cg sayori 2 onlayer above_master
    show bg:
        blur 0.0
    with cg_dissolve
    $ persistent.sayori.mark_cg(2)
    "Places her head in my lap."
    mc turned bun nostrands eb bb nb mf "!!"
    _mc "Wh- What is she thinking!?"
    "I shoot a glance down at her, but her eyes are focused on what's directly in front of her face."
    "The thing I went out of my way to get."
    "Pizza."
    "She reaches forward, grabs a slice, then turns her head to face upward, along with the rest of her body."
    "Now, she's looking directly at me."
    show cg smiling with cg_dissolve
    "A small, yet distinct, grin appears on her face."
    show cg pizza with cg_dissolve
    "And as it does, she takes that slice of pizza, and shoves the entire thing into her mouth."
    "I have to force myself to not burst out laughing."
    "She then grabs another slice, and holds it to my face."
    "I take a bite, a sizable chunk, but not anything close to as impressive as her recent showing of dominance in the mouth department."
    show cg normal with cg_dissolve
    "She swallows."
    "Then, to my horror..."
    show cg pizza with cg_dissolve
    "She takes the half-eaten slice, and proceeds to fit all of that into her mouth too."
    "I-"
    _mc ec ma ba "I'm not even mad."
    "Honestly, I'm so happy that she's letting loose that I reach down, grab half of the loaf of garlic bread, and shove it into my mouth too."
    _mc ea mh na "Ah, that might have been a mistake."
    "It's larger than I expected."
    show black zorder 15 onlayer above_master with NonBlockingDissolve(0.2):
        alpha 0.5
    $ renpy.music.set_volume(0.5, 0.5, "music")
    "In fact, it's so large that I start to panic."
    show cg normal with cg_dissolve
    mc be eb mh nc "Hgg-"
    $ renpy.music.set_volume(0.0, 4.0, "music")
    camera above_master:
        blur 0.0
        ease 6.0 blur 2.0
    "I can't breathe."
    "I..."
    "I'm choking on it!"
    _mc "Abort! Abort!"
    play sound heartbeat
    _mc "Sayori, save me-"
    camera master
    $ clear_layers("above_master")
    show sayori uniform md lup
    with fastfade
    $ renpy.music.set_volume(1.0, 0.5, "music")
    _mc ea bk mf nb "Huh?"
    "As if she responded to my prayer, I realise that I am free."
    "Sayori is now holding a lump of half-chewed mess of garlic bread."
    "She..."
    _mc bd eb mh nb "Fished it out of my mouth to help me?"
    _mc ec bi na "What kind of rescue was that?"
    show sayori e3c ldown at dip
    "She places the lump onto the top half of the pizza box, and looks at me."
    s e1a mh "Well, what did we learn?"
    show sayori md
    mc thinking ed md ba na "That you've got the bigger mouth."
    show sayori b1d e1d mj at dip
    show white at flash
    play sound ["<silence 0.1>", audio.slap]
    "I receive a sharp jab to my stomach."
    s lup b4 mg "Uuuu~"
    show sayori md
    mc ldown mg eg "Alright, alright. I learned that you can do more with your mouth than I can."
    show sayori e3c mj b1d ldown at dip
    show white at flash
    play sound ["<silence 0.1>", audio.slap]
    mc mm bf "Hggh-"
    "Another jab. I definitely deserved this one."
    mc ed mb nb be "... That you're more proficient at using your mouth?"
    s e1d mg "Last chance."
    show sayori md
    mc be eh md "Okay, okay."
    mc ea mb ba na "That you'll always help me out of sticky situations, no matter what."
    s mg b1b e2a mg "Not exactly what I was looking for."
    show sayori md
    mc ml "Well, what lesson would you like me to learn?"
    s mb b1a e1a "Not to stick big things in your mouth when I'm not around."
    show sayori ma
    mc eh md "Hahaha, alright, fair enough."
    _mc ea mh "Wait, was that..."
    _mc ec "No way. Sayori doesn't make dirty jokes."
    _mc ea "But she understood the ones I made just before..."
    _mc eb "Oh no, I've corrupted her!"
    show cg sayori 2 zorder 4 with fade
    "We watch some TV, while we snack on the remaining pizza. Sayori splits her half of the garlic bread with me, making a rather..."
    show cg smiling with cg_dissolve
    "Interesting movement with it toward her mouth before she does."
    show black with NonBlockingDissolve(0.3):
        alpha 0.5
    "I can't help but feel a little..."
    _mc ec ba na mh "Well, a lot of things, really."
    _mc ea "Well, what am I supposed to feel?"
    _mc ef "She's resting on my lap, after all."
    _mc nb "Her head is inches from..."
    _mc eg bi mm "Nononono. We talked about this."
    _mc ec mh "Just, stop."
    _mc ea ba "It may seem that she's doing it intentionally, but she's just Sayori."
    _mc ma na bg "... Right?"
    stop music fadeout 3.0
    show black with NonBlockingDissolve(1.5):
        alpha 1.0
    $ set_date(hour=19, minute=12)
    "As the night progresses, we start to settle. I've grown rather accustomed to having Sayori in my lap, it would appear."
    _mc ec ma ba "She just looks so... at home, there, somehow."
    "With the pizza long gone, all we can do is watch the TV."
    
    scene bg mc_living_room:
        blur 2.0
    show sayori turned e2a md at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(2.0, time_warp=_warper.easeout)
    $ advance_date(minutes=24)
    play ambient int_night fadein 1.0

    "Sayori stirs a short time later."
    show sayori e1a with say_dissolve
    "She looks up at me, and I pause the TV."
    mc turned bun nostrands mg "What's up, Sayori?"
    show sayori ma with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "She flashes me a small smile, then proceeds to stand up."
    s e2a mb "Sorry, Melly, but I should be heading home."
    show sayori ma
    mc mb "Oh, sure. I'll walk you over there."
    s mh e1a "Ah, no, it's fine. Don't need you to get cold, too."
    show sayori ma
    mc mg "No, I insist. It's pretty late."
    show sayori at lhide
    hide sayori
    "Sayori walks to the front door, grabbing her stuff." # im stuff
    stop ambient fadeout 2.0
    play ambient2 ext_night fadein 1.0
    show sayori turned e2a at i11
    show bg mc_house_entrance_night
    with NonBlockingTransition(wipeleft)
    "She then turns back toward me."
    s e1a mb "Thanks, for tonight. I really did have a lot of fun."
    s mg "So..."
    show sayori e1d ma
    "She looks at me with eyes that I've never seen before."
    "I can't describe it."
    "They're like... deep oceans. Swirling around in a vast, open, yet volatile sphere."
    "It reminds me of a snow globe after being violently shaken."
    s mb "Melly..."
    show sayori ma with None
    show sayori lup rup b2a e3c mg
    camera master:
        align (0.5, 0.2) zoom 2.0
    show bg:
        blur 2.5
    show black
    with NonBlockingDissolve(0.3)
    stop ambient2 fadeout 3.0
    "Suddenly, I find her in my arms."
    "But not just that."
    "No, so much more than that."
    "It's something I've only experienced once before."
    "Something... {b}{i}We've{/b}{/i} only experienced once before."
    hide black with NonBlockingDissolve(1.0)
    play sound heartbeat
    "Her lips have locked with mine."
    "I want to question it, I want to pause to think, but I just can't."
    "I don't think I'll ever be able to think again."
    "Last time was nothing compared to this."
    show sayori mh nb b1b with say_dissolve
    "She's..."
    "Sayori..."
    play sound heartbeat
    "She's kissing me."
    "We're kissing."
    "How did this happen?"
    "Does this mean she likes me after all?"
    "Ah, who am I to complain?"
    show sayori mg with say_dissolve
    "Right?"
    show sayori e1d b1a ldown rdown nc ma
    camera master
    show bg:
        blur 0.0
    with fade
    "After what I wish could have lasted an eternity, she finally breaks away."
    "Her cheeks are flushed a crimson I've never seen on her before."
    show sayori e2a
    "Her small smile speaks a thousand words, words I couldn't portray through poetry even if they existed in any language."
    show sayori e1a at thide
    "And her eyes..."
    "Those eyes. Their endless blue."
    "She's... just... immaculate."
    "Utter perfection."
    hide sayori
    "And with that, she slowly slides out of the door."
    camera master:
        align (0.4, 1.0) zoom 1.0
        ease_quad 0.5 zoom 2.0
    show black:
        alpha 0.0
        easein 0.3 alpha 1.0
    play sound ["<silence 0.15>", audio.fall]
    play sound_loop heartbeat fadein 3.0
    "Once the door clicks shut, I drop limply to the floor."
    "I simply can't hold it together anymore."
    "My mind is running a million miles a second;"
    "A swirl of emotion barrages me like a tsunami."
    "My heart beats like it knows it has hours left to live."
    "And my lips quiver, now cold and lonely."
    _mc eb be nb mf "What..."
    _mc "What have I done?"
    _mc ea "That..."
    _mc mh "I can't take that back."
    _mc eb "We kissed."
    _mc "Sayori and I..."
    _mc "What does that mean?"
    _mc "How did this happen?"
    _mc ef bg "I thought I had tried so hard to avoid giving her the wrong signals, but did she pick up on me anyway?"
    _mc eb be "Should I have tried harder?"
    _mc eg bg "No, that's not it."
    _mc ef "It was yesterday."
    _mc "Yesterday, when she left without so much as a word."
    _mc "She just..."
    _mc ea bf "Maybe she felt guilty for that."
    _mc eb be "Oh god, she felt guilty for something I did?"
    _mc "No, that's so like her!"
    _mc "Did I..."
    _mc "Did she feel forced into that because of guilt?"
    _mc "And if so, does that mean she's still feeling guilty?"
    _mc "Does that mean she thinks that our first time kissing was out of guilt too?"
    _mc ef bf mf "No, that would mean..."

    $ add_calendar_description(calendar_descriptions["sayori"][5])

    return