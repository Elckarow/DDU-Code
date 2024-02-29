label week_1_wednesday_yuri:
    call act_card("act_I_y_card") from _call_act_card_4
    call calendar_transition(day=25, hour=8, minute=35, second=0) from _call_calendar_transition_36
    scene bg class_1_day with dissolve_scene_full
    play music playwme

    "I find myself in my first class of the day: Form."
    "It's always been pretty short, just serving as a head-count for the day."
    "... And I guess, a time for students to talk with each other without worrying about anything."
    camera master:
        align (0.0, 0.4) zoom 3.0
    with Dissolve(0.3)
    _mc turned ec thinking mh "... If that's so, then why do I feel so jittery...?"
    _mc ea "There's nothing to worry about... right?"
    _mc ef mh ldown "It's just a short roll call afterall."
    t "Miss Nakamura?"
    "As my thoughts still hold me occupied, my heart stops for a second after I hear my name."
    camera master:
        ease_quad 0.2 zoom 1.0
    mc bb eb nb mg "P- Present!"
    _mc ec bi mh "False alarm, it was just the roll call..."
    call close_eyes(duration=1.5) from _call_close_eyes_19
    _mc eg "... Geez, why am I getting so worked up...?"
    _mc "I just hear my name being called, and it causes me to nearly freeze?"
    _mc na "... Snap out of it, MC..."
    t "Miss Kuroyunagi."
    call open_eyes(duration=0.7) from _call_open_eyes_11
    _mc ec ba "That surname sounds familiar..."
    show yuri shy eb at t11
    y "P... Present."
    "Yuri raises her hand, rather meekly."
    t "Okay. You can put your hand down now."
    y turned mb e2b b2a "O- Oh! Right..."
    show yuri turned lup rdown mk e2a b1a at dip
    "Yuri does as was suggested by the teacher, retreating into her desk all the while."
    show yuri shy eb
    _mc thinking ea "That's right... Her surname... Yuri Kuroyunagi..."
    _mc ec "Looking at her gives me a feeling..."
    _mc bi "But what is this feeling?"
    _mc eg ldown "This daydreaming I'm doing- I should stop before it gets out of hand."
    _mc ea ba "Maybe I'm just tired?"
    _mc ef "Yet... I only feel that way when I'm looking upon Yuri."
    "The roll call soon comes to an end, and right after-"
    t "Miss Kuroyunagi."
    y turned nb e1d mg lup "Y- Yes?"
    show yuri me
    "Yuri perks up from her desk, almost having the same reaction I did."
    "I guess she wasn't expecting to be called on twice."
    y mg na "W- What is-"
    show yuri md
    t "Mr. Taro wanted me to remind you that you forgot your book in his classroom yesterday." 
    t "The lab, if you might recall."
    y mg b1d e2a "O- Oh, I did..."
    y mb e3c ldown "How... careless of me..."
    show yuri ma
    "Yuri awkwardly chuckles."
    show yuri b1a e1d md
    "The teacher stares at Yuri."
    y mg rup b1d e2a "I assume that's... the only thing I forgot, yes?"
    show yuri md b1a e1d
    t "No, you also forgot-"
    "The teacher clears her throat."
    t "... I apologise. You are correct, miss Kuroyunagi."
    y mh b4 rdown "I forgot...?"
    show yuri me
    t "It was a small joke. I meant to try and lift your spirits, miss Kuroyunagi."
    y mg e2a b1d lup "... O- Oh. Um..."
    y mb e1a b1a "Thank you."
    show yuri md ldown at dip
    "Yuri gives a small nod, before taking out one of her other books and burying her face behind it."
    show yuri at thide
    t "... Anyhow-"
    hide yuri
    "The teacher continues to call on other students, telling them various things for the day."
    "'There was a change to your schedule'. 'Miss So-and-so is expecting you'."
    "Things of that nature, though I soon zoned out."
    camera master:
        align (0.5, 0.1) zoom 1.3
    show bg:
        blur 2.0
    show yuri turned md at i11
    with Dissolve(0.2)
    "My attention instead focuses back on Yuri."
    show yuri e1d with say_dissolve
    _mc ec "'Lifting her spirits...'"
    "As I go deeper and deeper into my thoughts, I notice something..."
    _mc ea "Is Yuri staring back at me?"
    show yuri ma with say_dissolve
    "..."
    _mc eb bd nb "Yuri {b}is{/b} staring back!"
    show yuri md with None
    camera master:
        align (0.0, 0.4) zoom 3.0
    hide yuri
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "Our eyes meet, and I quickly dart to look elsewhere."
    "Just like that, my heart is racing again, just like it was only moments ago."

    scene bg class_1_day
    camera master
    with wipeleft_scene
    $ advance_date(minutes=30)

    "The rest of Form goes as expected, and soon enough-"
    play sound school_bell
    t "Well, there is the bell, everyone."
    t "Enjoy the rest of your day!"
    "The teacher leaves the classroom, giving us some time to ourselves."
    "I go to grab my copy of The Black Cat, so that I can re-read it while I wait."
    "-But I find myself pausing halfway."
    show yuri turned md at t11
    "Yuri is also slow to the uptake, only now putting down her book and noticing the teacher left."
    y nb mk e1b "O- Oh!"
    show yuri mj e3a b2a at dip
    "She quickly hurries to get out of her seat, but in doing so, almost trips over her chair."
    camera master:
        align (0.5, 0.1) zoom 1.3
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "Without thinking, I find myself rushing over to her."
    mc turned nb mg bg "Yuri? Are you alright?"
    y mk e1b b1a "A- Ah..."
    show yuri md e2a b1d na lup with say_dissolve
    "She carefully readjusts herself, looking at her now empty desk."
    y mg "... I, yes... I'm alright."
    y e3c mb "I just... let's say, delved too deep into the world of my book."
    show yuri ma with say_dissolve
    mc "Yuri... please be careful. You could have been hurt."
    y shy md eb "... Erm..."
    show yuri mb bb with say_dissolve
    "Yuri hides her face behind her book once more."
    "I take a glance at the book in question, to see what she was reading."
    _mc thinking na ba mh "'Something Wicked This Way Comes'...?"
    _mc ec "This one sounds oddly familiar..."
    y ea ba ma "Hmm...?"
    "Yuri puts down the book in question, then looks behind me."
    mc ea mf "Hmm?"
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I follow her gaze, landing on my empty desk, next to another desk, also empty."
    $ autofocus.unblock("yuri")
    y turned lup mg e1d "L- Let us continue this discussion, over there, perhaps?"
    show yuri md
    mc ml ldown "Ah, okay..."
    show bg:
        align (1.0, 0.9) zoom 1.6
    show yuri e2a ldown ma b1d at i22
    with Dissolve(0.3)
    "We both walk over to my desk, pushing the neighbouring desk over to connect, then pushing out the chairs."
    show yuri e3c at dip
    "Yuri places her bag down, as do I, then the both of us take our seats, sitting side by side."
    camera master:
        align (0.8, 0.09) zoom 1.4
    show bg:
        blur 2.0
    show yuri e1a b1a 
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    y e2a mg "... So..."
    y mb e1d "You were referring to my book, yes...?"
    show yuri ma with say_dissolve
    "Yuri gestures to the book in her hands."
    "I nod."
    mc mg "Yeah. I feel like I know it from somewhere. What is it about?"
    y e2a mb "Ah... Well..."
    y e1d mh "Would it surprise you if I said this was a Ray Bradbury book...?"
    y lup mb e1a "His style here is somewhat similar to Edgar Allan Poe's {i}The Black Cat.{/i}"
    show yuri ma with say_dissolve
    mc ml "That's right, we discussed that yesterday. I hadn't forgotten, I just didn't put the name to the book..."
    show yuri e1b me with say_dissolve
    "Yuri then pauses, eyes widening."
    y e2b mk nb "A- Ah, you asked what the book was about..."
    y e3c b2b mg rup "M- My apologies- Ahem..."
    y mh rdown ldown b1a e1d na "The story is focused around a town of strange happenings..."
    y e2a mg "From a carnival covered in smoke to a merry-go-round going in reverse..."
    y b1d mb "That is to say, of course, I have only just started reading it. I thought it would only be fair."
    y me e2b b1a "..."
    y shy eb "You know, so that we may both experience it together...?"
    show yuri ea mc with say_dissolve
    y "..."
    y eb mb nb "Ah... Though, maybe I should have waited until we both had the chance to read it together first..."
    y ee bb "... My apologies."
    y ma "I just had the time to spare, and since Form is usually not very demanding in attention..."
    y md eb "Erm..."
    show yuri ma ba ea na with say_dissolve
    mc mb bg "H- Hey, don't worry about it. I'll be sure to catch up... What page are you at, currently?"
    show yuri turned md e2a with say_dissolve
    "Yuri quickly opens her book to check, looking for a bookmark."
    show yuri e3c with say_dissolve
    "Upon finding her bookmark, she glances at the corner of the book, before closing it once more."
    y e1d mg "Around... two hundred, I think...?"
    y e2a mb b1d "The fine print is always hard to read..."
    show yuri md with say_dissolve
    _mc ba mh "She said she just started reading, and she's already at page two hundred...?"
    _mc eg bg ma "Gosh... That’ll take some time..."
    mc ea ba mg "Don't worry! I'll reach that in no time, then we'll be able to talk about it... right?"
    mc mb "Even if I don't, don't feel bad. You don't need permission to engage in your own hobbies, yeah?"
    show yuri e1a b1a with say_dissolve
    "Yuri looks at me, contemplating her response."
    y "..."
    y e2a b1d mg "I suppose you {i}are{/i} right..."
    y shy eb bb "I just... did not want to disappoint, after I promised yesterday to bring a new Ray Bradbury book we could read together..."
    y ee "..."
    y mc ba ea "... Thank you for your consideration..."
    "Yuri gives me a small smile, assuring me her worries are no more."
    "As I return her smile, another teacher walks into the classroom."
    t "All, be quiet."
    "The teacher glances around the room, spotting us. His irritated look quickly changes to a judgmental one."
    show yuri turned lup rup e1d md with say_dissolve
    t "You two, put the desks back where they belong."
    show yuri md e2a b1d with say_dissolve
    mc ml "Sorry - Yes, sir."
    _mc ec bi mh "Yikes, how did I get so distracted? That's weird. I guess it's just been a while since I had someone to talk to in class - Maybe I got a little too exited."
    camera master
    show bg:
        blur 0.0 zoom 1.0
    hide yuri
    with Dissolve(0.2)
    $ autofocus.unblock("yuri")
    $ say_transition = False
    "We both return the desks to normal positions, then sit back down."
    show yuri turned e2c md at t11
    "... With Yuri opting to sit in the once empty desk, still next to me."
    _mc ec ma ba "... Well, no one else was using it, so I guess it's fair game."

    scene bg class_1_day with wipeleft_scene
    $ set_date(hour=15, minute=15)
    play sound school_bell

    t "And that's it for today. Take care!"
    _mc turned eg "Finally time, eh?"
    "The last class now out of the way, I smile a little to myself."
    _mc ea "It's time to visit the club once more."

    scene bg school_corridor_3_day with wipeleft
    show yuri turned md e2a b1d at i11
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.1) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True

    mc turned nb mg bb eb "W- Woah!"
    y b1a e1b mk nb lup "A- Ah!"
    show bg:
        blur 0.0
    camera master
    show yuri b2b rup ma e2a
    with Dissolve(0.2)
    $ say_transition = False
    "I avoid nearly running right into Yuri as I step into the hall."
    mc ml bg ea "Y- Yuri?"
    $ autofocus.unblock("yuri")
    y mb "Y- Yes...?"
    show yuri ma
    mc mf "What were you-"
    mc ec na bi ml "I mean, how-"
    show yuri rdown me b1d e3c
    mc eg mg "-Geez, I {i}cannot{/i} speak today."
    "Yuri gathers her breath, watching as I pitifully stumble over my own words."
    y na e2a mg "I... was on the way out and paused..."
    y shy eb "You... must've run into me... I a- apologise..."
    y ma ea "I was... making my way to the Literature Club, actually..."
    _mc ec ba mh "Ah, I guess that explains it."
    mc ea ml "Sorry about that..."
    mc eh bg md nb "I, ah, guess I should've been more careful~"
    "I half-heartedly chuckle, more to myself than to anything else, but it seems to bring her mood up a little."
    y turned e2a b2a mb "Ah... Don't worry."
    y e3c b2b mh "I don't fault you..."
    y e2a b1d mb "... T- That said, we should make haste to the club..."
    show yuri ma
    mc mb na ba ea "Sure!"
    show yuri at lhide
    hide yuri
    "Both Yuri and I rush down the hallway and over to the Literature Club."
    _mc ec ma "Jumpy, isn't she? Almost feels like I'm babysitting a puppy..."

    scene bg school_corridor_1_day
    show yuri turned e2a b1d at i11
    with wipeleft
    $ advance_date(minutes=3)

    "After a quick jog, we make it just outside the clubroom."
    "The clubroom seems quiet - Nothing abnormal, at least at first glance."

    # [Full Voice Acting]
    y mb e3c "I suppose we did not need to rush, after all..."
    show yuri ma e1a b1a
    stop music fadeout 3.0
    "..."
    show yuri e1d md lup with None
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.1) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    y e1d mg lup "... MC...?"
    show yuri md with say_dissolve
    mc turned mf nb "Hm?"
    "Yuri turns to me, noticing my inactivity."
    mc bg eg mj "Me? Nah, I'm good. Just catching my breath is all."
    y e1a "..."
    y ldown mg e2a b1d "{size=-7}... I recognize that look in your eyes...{/size}"
    show yuri md with say_dissolve
    mc mg bd ea "Hah?"
    _mc mh ec bi"I have a look? What look?"
    y e3c mb "O- Oh, um... Nothing..."
    y e1d b1a mg "I was just saying, well..."
    y shy eb bb "If something is bothering you, perchance, would you be willing to, um..."
    extend ea mc ba " delve into it, with my presence to guide you...?"
    mc ba na "..."
    _mc ef "More perceptive than she appears, evidently."
    _mc ea "I only just 'met' Yuri yesterday, and although we've always shared a few classes together-"
    _mc thinking "-Would it be too much to lean on her with this?"
    show yuri ma with say_dissolve
    _mc "Maybe she'll understand?"
    _mc ec "It kinda feels like she'll probably work it out sooner or later anyway..."
    mc ldown ef mf "Well..."
    mc ea mg "Remember how I said that Sayori and I met before...?"
    y turned e1d mg b1a "... Yes?"
    show yuri me with say_dissolve
    mc ef "... Truth is, I've been a little... uneasy."
    mc ml "I've known Sayori for a long time, but..."
    show yuri e1a md with say_dissolve
    mc mh "..."
    y e2a b1d mg "You felt uncomfortable approaching her?"
    show yuri e1a b1a md with say_dissolve
    mc ea bg mg "We were separated for five years."
    mc ef ml "I just... don't know where to start, or if I even should."
    show yuri e2a b1d me with say_dissolve
    "Yuri processes the information I've provided her."
    show yuri e1a md with say_dissolve
    "The stare she gives me is rather uncomfortable..."
    _mc ea mh bf "I didn't do anything wrong, did I...?"
    y lup e3c mg "... While judging you would prove me a hypocrite..."
    y b1a e1d mh "I believe you should try to get along with her again."
    y mb e1a "The pained ting of uneasiness will go away the more you combat it."
    y mg e2a b1d "On the other hand..."
    y ldown e3c mh "Allowing it to comfort you and stay within your comfort zone will only make it worse."
    show yuri md with say_dissolve
    "..."
    show yuri e1a b1a with say_dissolve
    mc ml eg bi "Yeah, it feels like that's the right call. I guess just getting my thoughts out made me realise how stupid of a thing it is to be worried about..."
    mc ef mh "..."
    "Despite myself and my words, I still can't will myself to move."
    show yuri e3c md b1d with None
    show yuri rup
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    show yuri me at dip
    $ say_transition = False
    "Yuri lets out a sigh."
    show yuri b1a e3d md
    "Then, almost completely flipping what I've seen of her so far-"
    show yuri e1d ma rdown at thide
    "Yuri takes a deep breath and slides open the clubroom door."
    hide yuri

    scene bg club_day with wipeleft
    show yuri turned e3d at t11
    window auto show
    play music okev

    $ autofocus.unblock("yuri")
    y mb lup "H- Hello, everyone!"
    show yuri ma e1d nb at t21
    show sayori turned mb at t22
    s "Oh, hey Yuri!"
    show yuri at t31
    show monika turned md at t32
    show sayori ma at t33
    m "Oh my, welcome, Yuri..."
    show monika mc at t42
    show sayori b2a at t43
    show yuri e2a b1d at t41
    show natsuki cross b1d mg at t44
    n "Huh?"
    show natsuki me
    "Of all of them, Natsuki seems the most surprised."
    n mg turned "The hell's gotten into you?"
    show natsuki md
    show yuri turned b2a e2b ma
    y mn e3d b3d ldown "... W- What do you mean, I can't be excited to join the club and talk with all of you?"
    y e1d b1a mb "I- I- I also brought along our new member, MC."
    show yuri ma at thide
    hide yuri
    show monika turned at t31
    show sayori turned ma b1a at t32
    show natsuki cross me at t33
    "Everyone then turns their attention to me."
    show sayori b2b
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show monika:
        alpha 0.0
    show natsuki:
        alpha 0.0
    with Dissolve(0.2)
    "Sayori's eyes meet mine, and I freeze."
    mc turned mf nb "... Ah-"
    show sayori b2a
    show monika:
        alpha 1.0
    show natsuki:
        alpha 1.0
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    mc mb  "... Hi, everyone..."
    show yuri turned e3c lup mb at t41
    show monika at t42
    show sayori at t43
    show natsuki at t44
    _mc eb bg mh "Jesus, so many eyes - I almost forgot what being in crowds was like."
    y "D- Don't fret, for while you may be new here, none of us will bite."
    $ autofocus.block("natsuki")
    show yuri ma 
    n e1b md "..."
    _mc ec ba na "Huh."
    "Natsuki's giving us both a somewhat justified expression questioning just 'What the hell is going on here?'"
    y e1d mh "T- That said, let us..."
    y e2a b1d ldown mg "Take our..."
    y shy eb ma bb "Seats..."
    show yuri nb ba
    "Whatever caused Yuri's balloon to inflate immediately popped, as she loses all the newfound vigour she expressed mere seconds ago."
    mc eh bf md nb "Y- Yeah!"
    extend ef bg ma " ..."

    # [End Voice Acting]

    scene bg club_day with wipeleft_scene
    $ advance_date(minutes=3)
    $ autofocus.unblock("natsuki")

    "After a few awkward minutes pass, everyone seems to be back to doing what they were previously."
    show bg class_2_day as stuff:
        align (0.2, 0.55) zoom 2.0
    show monika turned md bc ec at i21
    with NonBlockingDissolve(0.2)
    "Monika is standing at the teacher's podium, working on paperwork,"
    hide stuff
    hide monika
    hide bg
    show bg club_closet_day zorder 1:
        crop (0.0, 0.0, 0.5, 1.0)
    show bg club_day as stuff:
        align (1.0, 0.6) zoom 1.8 
    camera master
    show sayori turned e2a at i44
    show natsuki cross e2a b1d md at i21
    with NonBlockingDissolve(0.2)
    extend " while Sayori and Natsuki are both into their own books."
    show natsuki e1a
    "I still catch glances from Natsuki every so often, her scepticism quite apparent."
    hide natsuki
    hide sayori
    hide stuff
    hide bg
    show bg club_day
    with Dissolve(0.2)
    _mc turned mh "I want to read that one book with Yuri, but-"
    _mc ec "-Now I feel too awkward to even approach her."
    _mc ea thinking "Just what was that, anyway...?"
    _mc "Was she trying to show me something...?"
    _mc bd eb "... No, wait."
    _mc ldown ec bi "She definitely was."
    _mc ea ba ma "She broke character, to show me that I can do that, too."
    show bg club_day:
        align (0.0, 0.8) zoom 1.9 blur 2.0
    show yuri turned me b1a e1d at i42
    camera master:
        align (0.5, 0.1) zoom 1.5
    with Dissolve(0.2)
    "I look over at Yuri, who catches my glance."
    show yuri e1a ma with say_dissolve
    "Instead of retreating behind her book, she maintains eye contact,"
    show yuri e2c:
        matrixtransform RotateMatrix(0, 0, 0) matrixanchor (0.5, 0.8)
        easein 0.1 matrixtransform RotateMatrix(0, 0, 1)
        easeout 0.1 matrixtransform RotateMatrix(0, 0, 0)
    extend " before looking off and barely pointing from behind her book."
    camera master:
        easein 1.0 xoffset -100
    with None
    show bg club_day onlayer above_master:
        align (1.0, 0.6) zoom 1.8 blur 0.0
    show sayori turned e2a at i44 onlayer above_master
    camera above_master:
        align (1.0, 0.2) zoom 1.0
        ease 0.7 zoom 1.1
    with NonBlockingDissolve(0.5)
    "I follow her gaze, eyes landing on Sayori."
    $ clear_layers(("master", "above_master"))
    show bg club_day
    with Dissolve(0.2)
    _mc turned ec "I guess Yuri really is trying to help, huh...?"
    _mc bi mh "Albeit, the way she did so was... definitely weird, but-"
    show sayori turned e2a at i44
    show bg:
        align (1.0, 0.6) zoom 1.8
    with Dissolve(0.2)
    "I walk over to Sayori, tapping her shoulder."
    $ autofocus.block("sayori")
    s e1a mg "Huh?"
    show sayori md
    "Sayori turns, noticing me."
    $ autofocus.unblock("sayori")
    s mb "Oh, hey Melody!"
    show sayori ma
    _mc ec mh ba "'Melody'..."
    mc ea ml "Ah... Hey."
    mc mb ef "Nice to... see you again."
    "I muster a smile."
    s mb e3d "Yeah, you too!"
    s lup mh e1a "Wanna sit together?"
    show sayori ma ldown
    mc ml nb ea "Y- Yeah..."
    show sayori at dip
    "Sayori pulls one of the nearby desks closer to hers, then pats the chair."
    camera master:
        align (1.0, 0.2) zoom 1.4
    show bg:    
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "I sit down."
    show sayori e3d lup rup at i43
    camera master:
        zoom 1.7 xalign 0.65
    show bg:
        blur 2.5
    with Dissolve(0.2)
    "Just as I do, Sayori wraps her arms around me tightly, placing her forehead on my shoulder."
    mc bf eb mg "S- Sayori?!"
    s b2b e3c mb "You were nervous, weren't you?"
    s e2a b2c mh "I don't know why, but Yuri was acting kind of weird earlier..."
    s e1a mg b1a "Then I saw you, and it kind of... clicked, you know?"
    show sayori ma with say_dissolve
    _mc bg mf "Huh...?"
    mc ea bd ml "N- No, wait, you got the wrong-"
    s b1d e1d mh "No, silly, I know what I said!"
    s e3d mb b1a "You wanted to hang out with me!"
    camera master:
        zoom 1.4
    camera master:
        xalign 1.0 zoom 1.4
    show sayori rdown ldown ma e1a at i44
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "Sayori parts the hug, returning my smile."
    s e3c b2b mb "... Thank you, Melly..."
    show sayori ma with say_dissolve
    mc ef mb bf "Y- Yeah. I guess I just didn't know where to start."
    _mc na ma bg "Melly. Now that's something I haven't been called in a long time..."

    scene black
    camera master
    show bg class_2_day
    with Dissolve(0.5)
    $ advance_date(minutes=5)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    call close_eyes(0.0, base_blur=0.0) from _call_close_eyes_20

    "After sharing some moments of silence together, both our heads on our respective desks, we're suddenly woken up."
    m turned rhip mb "Okay, everyone!"
    show monika at i11
    call open_eyes(0.5) from _call_open_eyes_12
    hide black
    m "Now that we've settled ourselves in for the day, I was thinking of a club activity we could do."
    m md eb bc rdown "Given this is the Literature Club, I was thinking..."
    m mb ba ea lpoint "... Why not read poems and interpret their meanings?"
    show monika ma with None
    hide monika
    show bg club_closet_day
    show natsuki turned b3a md at i33
    with Dissolve(0.2)
    n me "Hm?"
    hide natsuki
    show bg club_day:
        align (0.0, 0.8) zoom 1.9
    show yuri turned md lup e1d at i42
    with Dissolve(0.2)
    "Yuri's head perks up as well, curious like the rest of us."
    hide yuri 
    show sayori turned md at i44
    camera master:
        align (1.0, 0.2) zoom 1.5
    show bg:
        blur 2.0 align (1.0, 0.6) zoom 1.8
    with Dissolve(0.2)
    "Sayori, sitting next to me, is giving Monika her full attention."
    camera master
    show monika turned lpoint at i11
    show bg class_2_day:
        blur 0.0 zoom 1.0
    hide sayori
    with Dissolve(0.2)
    m md "Well, every piece of literature can have multiple interpretations, correct?"
    m eb "And while most people would settle on the status quo..."
    m ea ldown mb "... Would it not be fun to share our own thoughts on various poems?"
    m ec "Perhaps even enlightening us to different perspectives, or meanings we did not see before."
    show monika ma
    "..."
    m md ea "So...?"
    show monika mc
    s turned mb lup "I'm in!"
    hide monika
    show bg club_day:
        blur 2.0 align (1.0, 0.6) zoom 1.8
    show sayori ma at i44
    camera master:
        align (1.0, 0.2) zoom 1.5
    with Dissolve(0.2)
    "Sayori raises her hand, eager as always."
    hide sayori
    show natsuki cross e2a b3a md at i33
    show bg club_closet_day:
        blur 0.0 zoom 1.0
    camera master
    with Dissolve(0.2)
    n mi "I guess it could be pretty neat."
    show natsuki md with None
    hide natsuki
    show yuri turned at i42
    show bg club_day:
        align (0.0, 0.8) zoom 1.9
    with Dissolve(0.2)
    y mb lup "I agree. Writing {i}is{/i} all about sharing our own stories and perspectives, after all..."
    show yuri ma
    m turned md "MC?"
    show monika mc at i11
    hide yuri
    show bg class_2_day:
        zoom 1.0
    with Dissolve(0.2)
    "Monika turns to me, as does everyone else."
    mc turned mf "... Hm?"
    show monika ma
    mc mg "Well, I do admit it sounds like a pretty nice idea..."
    m mb "Then it's settled."
    m lpoint md "For this, you can split up into groups, or work on your own. However you like."
    m ed mb ldown "Come end of the club meeting, we will share our findings."
    show monika ec mc bc at dip
    "Monika takes out a stack of papers from a nearby printer, straightening them out on the teacher's desk she's been sitting behind."
    show monika ma ea ba
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "She then hands them out to each of us, three different poems."
    hide monika
    camera master
    show bg club_day:
        blur 0.0 
    with Dissolve(0.2)
    "I turn to Sayori."
    show sayori turned e2a md at i44
    camera master:
        align (1.0, 0.2) zoom 1.5
    show bg:
        blur 2.0 align (1.0, 0.6) zoom 1.8
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc ml "Well, Sayori...?"
    s me "Hmmm..."
    mc ec bi mf "... Sayori?"
    s mj e3c b1d "... Mmm..."
    _mc mh "... Is she pretending to not hear me?"
    mc ea bd mg "Sayo-"
    s e1b lup rup mi b1a "I know!"
    s ldown rdown e1a mb "Why don't you work with Yuri?"
    show sayori ma with say_dissolve
    mc mf ba ea "Huh?"
    mc ml nb "But we were just-"
    s e1d b1d mg "Nuh uh!"
    s lup mh e1a b1a "Yuri helped you out earlier, didn't she?"
    s ldown mb "So you should help her in return!"
    show sayori ma with say_dissolve
    "..."
    _mc ec ma na "I suppose she is right, from a certain point of view, but-"
    _mc ef mh "I can't help but feel twinge of disappointment."
    mc ea mb "Alright, I will."
    s e3d mb "Yeah!"
    s mh e1a "I'll still be here if you need me, Bard."
    show sayori e3b ma with say_dissolve
    "She throws a knowing wink my way, and I respond in kind."
    _mc ec ma "She's doing this for a good reason - All I have to do is trust her."
    mc eg mb "Of course, Mage."
    show sayori rup lup e3c at i43
    camera master:
        zoom 1.7 xalign 0.65
    show bg:
        blur 2.5
    with Dissolve(0.2)
    "I give Sayori another hug, as natural as could be, before leaving the desk and walking over to Yuri."
    hide sayori
    show bg:
        align (0.0, 0.8) zoom 1.9 blur 0.0
    show yuri turned e2a md b1d at i42
    camera master
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    if preferences.language is None:
        $ auto_advance_date_mult = 0.727

    "As I approach Yuri, I see her deeply invested in reading one of the poems."
    mc ea "Hey, Yuri?"
    show yuri b2a e1b mk lup rup nb at hop
    "She turns to me, startled."
    y rdown b2b mb e2a "E- Eh? S- Sorry!"
    show yuri ma
    mc bg ml "Sorry? For what?"
    y shy eb bb ma na "B- Beginning without you."
    "I look her in the eyes, smiling as broadly as I can muster."
    mc eh md ba "No biggie! That just means you have a head start."
    _mc ec ma "Best to scratch her back, after she scratched mine."
    show yuri ea ba
    "Yuri then pauses, studying me."
    $ autofocus.block("yuri")
    y "..."
    mc mf ea "Yuri?"
    y eb "..."
    $ autofocus.unblock("yuri")
    y turned e2a b1d mg "I just realised..."
    y mh e1d b1a "Aren't you going to work with Sayori...?"
    show yuri md
    mc ml "Oh! Uh, about that-"
    mc mb "Sayori said I should work with you."
    _mc ec ma "Not that I'm not also doing this a little for me, but hey - I don't mind either way."
    y e2a me "Is that so..."
    show yuri e1a ma b1a
    "Yuri gives me a smile."
    y mb "Very well. Let us proceed in this endeavour together."
    show yuri ma
    mc md eh "Yeah!"

    play music2 add_playback_info(audio.okev_y, get_pos()) fadein 2.0
    stop music fadeout 2.0

    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "I pull one of the nearby desks closer to Yuri's, then take a seat."
    mc mb ea "Mind if I see the poem you started with?"
    y rup mh e1d "You may go ahead."
    show yuri ma rdown with say_dissolve
    "Yuri puts the poem down, sliding it across the desk so I can read it."

    $ show_poem(yuri_poem_2, music=False)
    $ advance_date(minutes=3)

    mc ea mf thinking "I wonder what it means?"
    y mg rdown "Hmm... I think it's best to start from the top here."
    show yuri md with say_dissolve
    "I look at Yuri, curious as to what words she may say next."
    _mc ec mh "Considering her experience, she will likely decipher this in no time."
    y e3c mg lup "'A black sea... Shimmering in the dark'."
    y e1d mh "I think the author meant this:"
    y e2a mb "While the sea can't be looked through, during our darkest hours, it makes itself apparent."
    show yuri ma with say_dissolve
    _mc ldown ea "Huh! Why didn't I think of that? Well, I know {b}why{/b} I didn't, but..."
    mc mg "What makes you say that?"
    show yuri e1a ldown with say_dissolve
    "Yuri turns her head towards me, having a slight smile."
    y e1d mh "When something shimmers, what does that usually mean?"
    show yuri md with say_dissolve
    mc thinking ml "That it reflects light?"
    y e3c b1d mb "No, not in a literal sense, but... figuratively."
    show yuri ma e1a b1a with say_dissolve
    mc ec mh "Hmm..."
    y lup e1d mh "It means that the sea is trying to get your attention."
    show yuri ma with say_dissolve
    mc ml ea "That... makes some sense."
    y e1a mb ldown "You try the next one."
    show yuri ma with say_dissolve
    _mc ldown ec ma "Alright... Shouldn't be too hard. Let's have a look."
    "I take a good look at the paper once again."
    mc mf ec bi "'Its appearance unmatched... Its purpose unknown...'"
    mc ea ba mg "'Unmatched' as in 'unique', right?"
    show yuri e3c with say_dissolve
    "Yuri nods her head, curious as to how I will proceed."
    show yuri e1a with say_dissolve
    mc mb "'Purpose unknown' speaks for itself, doesn't it?"
    y lup rup mh e3c "Sometimes, things seem to speak for themselves, but the more you think about it..."
    y e1d mb "The more you find that it hides its true meaning."
    show yuri md ldown rdown with say_dissolve
    mc thinking ml "Do you think it means something other than 'nobody knows what it's for'?"
    y mh rup "It's always possible."
    y e2a mg b1d "What if..."
    extend e1d mh b1a " it has multiple meanings?"
    y e1a mb rdown "As a result, no-one knows which is the correct one."
    show yuri ma with say_dissolve
    mc bi ec mf "Huh. I didn't think about it that way."
    y e1d mb "You have to use that mindset if you want to interpret a story."
    y e2a mh "Don't think of just one reason, try to think of as many as possible."
    y b1d mg "That way-"
    show yuri b1a lup nb e2b mk with say_dissolve
    "Then, she abruptly pauses."
    y shy eb md bc "Ah! Sorry, I-I got carried away..."
    y mb bb "I never quite gave you a chance to speak, did I?"
    mc ldown bb mb ea "No, no, It's alright! I really like your advice, actually-"
    "A swell of emotions brushes past me, and I shake it off as quickly as it arrives."
    _mc ec bi mh "Aww geez, that slipped right past my brain without giving me the chance to think about it."
    show yuri ea ma with say_dissolve
    "Yuri looks at me, studying me after I gave my response."
    y turned lup rup b2b e3c nb mb "... Thank you, MC."
    show yuri e2a ma with say_dissolve
    "I look away, feeling a twinge of embarrassment upon my face."
    y e1d mh na rdown ldown b1a "I'll take the next one."
    y e1a mg "Let's see..."
    show yuri md with say_dissolve
    "Yuri peruses the paper with her finger."
    y mg "'It hides tears, events long marked...'"
    y e1d mh "My understanding of this line is that the sea hides some form of traumatic past, those 'events long marked'."
    show yuri md with say_dissolve
    mc mg ba ea "What if it hides how people {i}feel{/i} about said trauma?"
    mc mb "Given how dark it is, it would be hard to notice what's underneath, after all, which could tie in with how it's 'trying to be noticed'."
    y e3c mh "True. I suppose we agree on it being about the past, that one isn't hard to figure out."
    show yuri md with say_dissolve
    mc thinking mg "But where do those tears come from? That's the question."
    mc ef ml "Do the tears come {i}from{/i} the past, or what someone {i}thinks{/i} about the past?"
    show yuri b1d me with say_dissolve
    mc ea mf "Maybe the next sentences could make it clearer..."
    "Yuri, meanwhile, seems to be deep in her own thoughts."
    mc ldown eg mg "Ahem. 'Why must it hurt, events yet atoned?'"
    y e1a mg b1a "This leads credence to my trauma theory I mentioned earlier."
    y lup mh e2a "Of course, the same principle could be applied to any upsetting event in the past, not necessarily trauma, but..."
    show yuri mg e3c b1d with say_dissolve
    "Yuri takes a breath, in and out."
    show yuri e1a b1a md with say_dissolve
    "I do much of the same, before continuing."
    mc ea mb "Our consensus so far is that this poem is talking about the past, right?"
    y e1d mb ldown "I believe so, yes."
    show yuri ma with say_dissolve
    mc ml "Then your analysis would fit, wouldn't it?"
    mc ef bi mg "If someone were to have a past they were not happy about..."
    show yuri e2a with say_dissolve
    mc ml ba "Naturally, they would feel hurt by it."
    "I bite my lip a little."
    show yuri e1d with say_dissolve
    mc ea mg "Also, looking back on that first part, 'Why must it hurt'..."
    show yuri md with say_dissolve
    mc mb "If you think about it, it takes a certain force of will to get through certain past events, regardless of how deep they may be."
    y mg lup "Getting through them... As in, to be free from, or...?"
    show yuri md with say_dissolve
    "I give her a small smile, accompanied by a shrug."
    mc eg "Honestly? Probably both."
    mc ef ml "Freeing yourself from the past, and fighting against it..."
    mc mg "Both take a lot of effort and force of will."
    mc ea ml "... Which I guess leads to our next line."
    y mg ldown e3c b1d "'Only one knows, a person of will'."
    y e1d mh b1a "Only one person understands the sea and has the answers?"
    show yuri md with say_dissolve
    mc mb "That seems reasona-"
    y e3c mg b1d "No, I don't think it's that simple."
    show yuri mj with say_dissolve
    "I take a look at the paper, then back at Yuri."
    _mc ec mh thinking "'Not that simple', huh...?"
    mc ea mg "What do you mean?"
    y mg "If the sea hurts everyone..."
    y e2a mh "And everyone can have a force of will..."
    y md b1a e2b "..."
    "Yuri's eyes widen in realisation,"
    show yuri e3c ma b1a with say_dissolve
    extend " as she confidently takes in a deep breath."
    y mb e1a "I believe I understand."
    show yuri ma with say_dissolve
    _mc mh bb "Oh?"
    camera master:
        zoom 1.7
    show bg:
        blur 2.5
    with Dissolve(0.2)
    "I find myself leaning closer to her side of our two desks, looking over."
    y mb lup "'Only one knows,' as in, only one {i}type{/i} of person."
    show yuri ma with say_dissolve
    mc ldown ba ef ml "That makes sense, though..."
    mc ea mg "{i}What{/i} type of person is it referring to?"
    y e2a lup b1d mg "You see, everyone wants to be at their best."
    y e1a mh "But, how many people actually achieve that, MC?"
    show yuri md with say_dissolve
    "I briefly mull over the question."
    _mc ec mh "I mean, practically anyone would want to achieve the most they can."
    _mc ea "But the odds of that actually happening...?"
    _mc eg bi "Not to mention how we often have to fight with ourselves. Some people can have lofty ideals that need to be brought back down to Earth."
    _mc ef ba "While others, well..."
    "..."
    _mc bi "Yeah, she's definitely got a point."
    show yuri ldown b1a with say_dissolve
    mc ba ml "I don't think someone can {i}be{/i} 'their best'..."
    mc ea mg "Everyone changes daily, and so does their definition of 'best.'"
    mc thinking ml "In other words, to answer your question... 'No-one'?"
    y e2a mg "That's one way of looking at it, but..."
    y e1d mh "Very few people actually overcome their fears."
    y e3c mb b1d "Even if you believe you aren't afraid of something, that just means you don't {i}think{/i} about your fears."
    y e1a mg "But, when faced with them, it can make you... freeze. Caught in the headlights like a deer, pale as can be..."
    show yuri md with say_dissolve
    _mc ec mh ldown "It's rather uncanny, this one..."
    mc ea ml "That... is true."
    y e1d b1a mk nb "O- Oh, ah... I- I didn't mean... Um..."
    show yuri shy bb ee with say_dissolve
    "Yuri stumbles over herself."
    y ea "... It's really nothing, just an observation of mine. Don't pay it any mind, please."
    show yuri turned me b2a e3c with say_dissolve
    "Yuri then lets out a small sigh."
    y b1d e1a mg na "As we were discussing..."
    show yuri md with say_dissolve
    mc ef mb nb "Ah, right."
    y e1d mh b1a lup "It takes the right kind of mindset to overcome the past."
    show yuri md with say_dissolve
    mc ea na mg "And not everyone has that mindset, that experience that taught them how to treat the past."
    mc mb "That sort of person is a rarity. Someone you'd be hard pressed to come across in your life."
    y e3c mg "Yes, I believe so."
    y md b3b ldown "..."
    "There seems to be something on Yuri's mind, something more she wants to say, yet..."
    _mc ec bi mh "... I can't quite make out what."
    mc ea ml ba "Hey, Yuri..."
    show yuri shy with say_dissolve
    "She seems to be surprised, snapping out of whatever she had on her mind."
    y ma "H- Huh? Do you want to take a break, or...?"
    mc mb "Thanks for your help. You really got a knack for this, y'know?"
    y md eb ne "A- Ah... I- No, I'm-"
    show yuri turned lup rup b2b md e3c nc with say_dissolve
    "She clasps her hands over her chest."
    y me "... I'm only a novice."
    y mb e2a "A real expert would have finished this already."
    show yuri md with say_dissolve
    mc eh md "Oh, I don't think it's humanly possible to do it better than this."
    y shy eb bc ne "Now you're just trying to cheer me up..."
    show yuri mb with say_dissolve
    "I let out a sigh of my own." 
    _mc bi eg mh "It seems like her self esteem isn't that easy to pull up, compared to others."
    mc ea mg ba "Alright, I'll take the next one."
    show yuri na ea bb with say_dissolve
    mc ec bi mf "'As their past sinks, the sea weaves'."
    mc ea ml ba "I'm guessing this means 'sinking' as in... the past is fading away."
    y ma "Correct so far..."
    mc mb "Then, this one isn't that difficult. As you resolve your past..."
    mc mg "Whatever the sea contains, changes?"
    y turned e1d mg "You're improving, MC."
    show yuri md with say_dissolve
    mc ml bb "I am?"
    show yuri b2b ma e2a with say_dissolve
    "Yuri nods, a melancholic expression on her face."
    y b1d e3c md "..."
    "She then falls silent, contemplating something."
    mc bg mf "... Yuri?"
    y e1a mg "Why were you staring at me earlier today?"
    show yuri md with say_dissolve
    _mc eb bd mh nb "Crap, she noticed and definitely didn't forget."
    mc eh bg md "I was, uh... daydreaming."
    y mh e2a lup b1a "Ah... I thought it was something else."
    show yuri md with say_dissolve
    "She looks away for a minute, probably collecting her thoughts."
    y e3c b1d mg ldown "Where were we...?"
    y e1d b1a mh "'Cleansing its appearance, truth shows through the rill'."
    y e1a mb "Ah, it's as I thought..."
    y e2a mh "As the water clears, or in other words, the past..."
    y e1d mb "It all becomes clear."
    show yuri ma with say_dissolve
    mc ba ml ea na "Then the question is, how does it fit in with the last... sentence? What was it called?"
    y e1a mb "Stanza."
    show yuri ma with say_dissolve
    mc mb "The last stanza, yes."
    mc thinking ec mf "'After the black sea deceives'..."
    mc mh bi "Hmm..."
    show yuri e1d with say_dissolve
    "Yuri looks on, awaiting my response."
    mc ea ba mg "I'm guessing it means, the sea isn't fully forthcoming."
    mc mb ldown "It takes that specific person, the one with will, to see through it."
    mc ml "Sound about right?"
    show yuri e3c with say_dissolve
    "Yuri nods her head in agreement."
    y b1d e2a mg lup "If we piece all of this together..."
    y b1a e1a mb "What do you think this poem is about?"
    show yuri ma ldown with say_dissolve
    mc mf "Conflict?"
    show yuri md with say_dissolve
    "Yuri contemplates my response,"
    show yuri e3c ma with say_dissolve
    extend " before giving one of her own."
    y mh lup e1d "I was thinking more along the lines of 'being hurt'."
    y ldown e1a mb "But, both concepts involve wanting to be noticed, hiding our true feelings, and not always being resolved by just anyone."
    show yuri ma with say_dissolve
    mc mg "Once it does get resolved, it shows the truth?"
    show yuri ma e3d with say_dissolve
    "We both have smiles on our faces- it seems we cracked the code!"
    y mb e1d "This went well. Thank you for your help, MC."
    show yuri ma with say_dissolve
    mc eh bg nb md "N- No, thank you for helping me. I don't read poems very often, you know."
    show yuri e3c with say_dissolve
    "She nods."
    y mh e1d lup "Do you want to go onto the next one?"
    show yuri md with say_dissolve
    mc ea bg na ml "Oh geez, that's right. We have three more after this one..."
    y e2a b2a mb nb "Oh... I don't mind if you want to stop for now."
    show yuri ma with say_dissolve
    mc ba mb "No no, as long as we do this together, it'll be worth it."
    show yuri e1a na with say_dissolve
    "We continue on to the next poems, taking us as much time as that first one for every poem."
    "Despite the slow pace, we both enjoy it, being together and learning our views on each subject."

    play music add_playback_info(audio.okev, get_pos("music2")) fadein 2.0
    stop music2 fadeout 2.0
    scene bg club_afternoon:
        align (0.0, 0.8) zoom 1.9
    show yuri turned:
        matrixcolor TintMatrix("#f1d6bb")
        i42
    camera master
    with wipeleft_scene
    $ set_date(hour=16, minute=14)
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    $ say_transition = False

    mc turned mj eg bi "It looks like that's all of them... Whew."
    $ autofocus.unblock("yuri")
    y mb "Y- Yes, it was quite tough. But we did it."
    show yuri ma
    "We stare at each other, finally having time to talk to each other about non-poem related things."
    "..."
    mc mf ea ba "So-"
    m turned mb "How did the poems go, you two?"
    show yuri e1b mk lup at t21
    show monika ma lpoint rhip:
        matrixcolor TintMatrix("#f1d6bb")
        t22
    camera master at vpunch
    mc mg bf eb nb "AH!"
    show yuri e3c b1d mg
    "I nearly jump back out of my chair as Monika leans into my view."
    show yuri md
    m mb ldown eb nb "You okay, MC? Sorry for the jumpscare~"
    show monika ea ma
    y e1a b1a mb ldown na "Her ability to dissect a poem may soon rival my own, if expedience in one's learning is a representation of one's analytical skill."
    show yuri md
    show monika na
    "I regain my breath."
    mc ef mb ba "I had an unrivalled teacher, which made all the difference..."
    show yuri e2a ma nb
    "Yuri smiles nervously and looks away."
    _mc ma bg "It would seem I've given her one too many compliments for the day..."
    m mb "That's great!"
    show monika ma ed rdown
    "Monika smiles, proud of us."
    hide yuri
    show monika lpoint ea at i11    
    show bg:
        zoom 1.0
    with Dissolve(0.2)
    "She then turns our attention back to the classroom as she speaks."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    m mb ldown "Ahem, I hope everyone had fun today! Does anyone want to talk about their poems?"
    show monika ma with say_dissolve
    _mc ea mh ba na "Should I volunteer? Wait, no, Yuri seems tired... I don't want her to overdo herself."
    hide monika
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("monika")
    play sound chairmoving
    "On the other side of the classroom, loud chair movement can be heard."
    show natsuki cross:
        matrixcolor TintMatrix("#f1d6bb")
        i21
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        i22
    show bg club_closet_afternoon
    with Dissolve(0.2)
    n mc "We'll go! Right, Sayori?"
    show sayori e3d
    show natsuki ma 
    _mc ec "Ah, so that's who Sayori ended up working with."
    hide natsuki
    hide sayori
    show bg club_afternoon
    show monika turned lpoint rdown ma:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with Dissolve(0.2)
    m mb "Alright, step up, you two."
    show monika ma with None
    hide monika
    show natsuki cross mc e3c b1d:
        i21
        xoffset 50 matrixcolor TintMatrix("#f1d6bb")
    show sayori turned e3d:
        i22
        xoffset -50 matrixcolor TintMatrix("#f1d6bb")
    camera master:
        align (0.5, 0.23) zoom 1.5
    show bg class_2_afternoon:
        blur 2.0
    with Dissolve(0.2)
    "When they step up, Natsuki dissects one of their poems in a great exaggerated voice."
    "It's almost as if she's trying to prove herself, that she and Sayori are a duo not to be messed with lightly."
    _mc ea "I know I should pay attention, but..."
    hide natsuki
    hide sayori
    show yuri turned md:
        i42
        matrixcolor TintMatrix("#f1d6bb")
    camera master
    show bg club_afternoon:
        blur 0.0 zoom 1.9
    with Dissolve(0.2)
    "I whisper to Yuri."
    mc mf "Hey Yuri... Do you want to spend some time together tomorrow...?"
    y mg rup e1d "H- Huh?"
    y mh nb "Quite all of a sudden, why... how come...?"
    show yuri md
    "... Then I realize, I didn't think this through."
    "Clouded by my feelings, I decide to give her a small smile."
    mc mb "I just thought it would be fun."
    y e2a mb b1d rdown "A... Alright..."
    show yuri ma with None
    hide yuri
    show natsuki turned lhip rhip b3a e3c mi:
        matrixcolor TintMatrix("#f1d6bb")
        i21
    show sayori turned lup mb:
        matrixcolor TintMatrix("#f1d6bb")
        i22
    show bg class_2_afternoon:
        zoom 1.0
    with Dissolve(0.2)
    "Natsuki continues to talk about their poems in great detail, with Sayori pitching in here and there."
    show natsuki ldown rdown ma 
    show sayori ma ldown e3d 
    with None
    hide natsuki
    hide sayori
    show bg club_afternoon
    with Dissolve(0.2)
    "Eventually coming to a close, the two finally sit back down."
    show monika turned rhip mb:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    m "That was great, you two. Fine analysis from the both of you~"
    m ed rdown "That's all for today, but I hope to see you all again tomorrow!"
    show monika ma at thide
    hide monika
    "Everyone smiles at one another as they go to pack up their bags, and as I turn to Yuri..."
    show bg:
        zoom 1.9 
    camera master:
        align (0.5, 0.1) zoom 1.5
    with Dissolve(0.2)
    "... She's already gone?"
    _mc ea bd mh "Where did she go? How is she so fast? I hope she's okay."
    camera master
    show bg:
        blur 0.0 zoom 1.0
    with Dissolve(0.2)
    "Finishing up with packing, I attempt to walk as fast as I can to try to catch up with her-"

    scene bg school_corridor_1_afternoon with wipeleft

    "..."

    scene bg school_corridor_3_afternoon with wipeleft

    "..."
    "-But, she's nowhere to be seen."

    scene bg school_lockers_afternoon with wipeleft

    _mc turned ec mh "I suppose I'll head home, then..."
    _mc eg ma "See you tomorrow, Yuri."

    $ add_calendar_description(calendar_descriptions["yuri"][0])

    call week_1_thrusday_yuri from _call_week_1_thrusday_yuri
    return