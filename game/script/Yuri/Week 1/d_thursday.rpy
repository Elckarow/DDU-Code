label week_1_thrusday_yuri:
    call calendar_transition(day=26, hour=6, minute=15, second=16) from _call_calendar_transition_37
    scene bg mc_bedroom_day_open with dissolve_scene_full
    play ambient ext_day fadein 2.0

    "I wake up tired."
    _mc turned messy naked nostrands ec mh "Poems aren't as easy as people think, it seems."
    _mc ea "It only brings questions, questions that keep me up at night..."
    mc eh bg mg "Huaaaa..."
    _mc ea mh ba "But the biggest question?"
    _mc ec thinking "Where Yuri went off to."

    scene bg school_street_day with fade
    $ set_date(hour=7, minute=50)

    "The streets are surprisingly bustling today, even though I avoid walking anywhere near the busy town on my route to school."
    _mc turned ec mh "How thoroughly odd."
    "Even so, I am left to ponder my thoughts in relative peace, largely ignoring the bustle around me of people and things."
    _mc ea "Questions of science, of logic, of life-"
    _mc ec ma "-Are normally what I'd think of, but not today."
    _mc ea "No, today... I'm wondering what kind of person Yuri is."
    _mc thinking mh "Is her shyness attached to what she thinks of others, or...?"
    _mc ec "Does she have other hobbies I don't know about?"
    _mc eg ma "And most important of all..."
    _mc ef ma "... What does she think of the many popular malls in the country?"
    _mc ldown eg "It all remains a mystery."

    stop ambient fadeout 2.0
    scene black
    show bg club_day 
    with longfade
    $ set_date(hour=15, minute=20, second=30)
    play music playwme

    "The classes went as usual, but-"
    "I enter the Literature Club and am met with an eerie sight."
    show natsuki cross mj b1d at i11
    hide black
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.5)
    "It's Natsuki..."
    "Just standing there, {i}menacingly{/i}." # :tardmelly:
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    n mg "Want something from me?"
    show natsuki md
    mc turned nb mf "Huh? What?"
    n turned e1d mg "You're staring at me."
    show natsuki md
    mc ml bb "I am? I mean-"
    mc ef bg mb "S- Sorry!"
    show natsuki e3c b1a
    "Natsuki scoffs."
    hide natsuki
    show yuri turned e2a md b1d at i42
    show bg:
        align (0.0, 0.8) zoom 1.9
    with Dissolve(0.2)
    "I pass her by and set my eyes on a certain purple haired girl, deeply invested in her book."
    mc mg na ea ba "Yuri!"
    show yuri b2a e1b mk lup rup nb at hop
    y "A- Aaah!"
    y mg rdown e3c b1d "D- Don't scare me like that!"
    show yuri md
    mc ml "You mean, scare you in a different way?"
    y e2a ldown na b2a mb "N- No thank you..."
    show yuri ma
    mc mg bg "Are you alright, Yuri? You disappeared yesterday."
    y b1d mg "I... had to go."
    show yuri md
    mc ba ml "Appointment...?"
    y shy eb "Uh..."
    show yuri ma
    _mc ec mh "She seems nervous..."
    mc ea mb "Do you... want to talk? Maybe walk and talk?"
    $ autofocus.block("yuri")
    y ea "..."
    "Yuri watches me silently, as she processes what I said."
    $ autofocus.unblock("yuri")
    y eb nb bc "You mean... Leave the classroom?"
    "Yuri looks around, nervously."
    y ba "Shouldn't we stay here?..."
    y ea "Monika might have something planned for the club..."
    mc thinking ec mf "Hmm... But there's not much privacy to be found here."
    mc ea mb ldown "I'll make sure we will be back before anything important happens, alright?"
    y eb na "S... Sure."
    show yuri turned lup md e1a at dip
    "Yuri stands up, and puts her book in her bag."
    y mg "Where to...?"
    show yuri md
    "I smile at her, hoping to quell her thoughts."
    _mc ec ma "She's definitely high-maintainance, though - I can't really talk. Maybe it'll be good for me to have a friend like that."
    mc ea mb "Have you ever been to the park?"
    show yuri e3c ldown at dip
    "Yuri gives an anticipatory nod."
    y e1d mg "I have, but... isn't that a bit too far away to quickly get back to the club?"
    y mh "Maybe we could walk in the school courtyard at least..."
    show yuri md
    mc ec bi mh "Hmm..."
    _mc ea ba "I wonder if the courtyard could even be considered a private place..."
    _mc ma "Only one way to find out..."
    mc mb "Sure, let's do that."
    show yuri e2a at lhide
    hide yuri
    "With our path set, the two of us leave the clubroom, thankfully uninterrupted."
    show bg club_closet_day:
        zoom 1.0
    show natsuki cross e2a mj at i11
    with NonBlockingDissolve(0.5)
    "I can almost imagine the look Natsuki might have given me on our way out, but by the time I look back, she isn't even looking at me."
    
    stop music fadeout 3.0 
    scene bg school_courtyard_day
    show yuri turned rup e1d me at i11
    with wipeleft_scene
    $ advance_date(minutes=5)

    "Yuri looks at me, still quite the nervous expression on her face."
    y mg "Wait..."
    y lup mk b2b e1b "You're not... angry at me, are you?"
    y shy mb eb bb "Because of me... running, leaving so suddenly yesterday?"
    mc turned bd ml "Why would I-"
    y ne md "No no no..."
    y ec ba nb "I'm sorry MC! Yesterday I just-"
    y bc eb ma "Got too nervous...!"
    y turned lup rup e2a nb mk b2b "I- I don't know how to-"
    show yuri e1b me b2a at hop
    mc bb mg "Yuri."
    show yuri b2b e1a md
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    play music violetsolo
    $ autofocus.block("yuri")
    $ say_transition = True
    "I put a hand on her shoulder."
    mc bg mb "Please, calm down and listen for a moment. I'm not upset."
    y e2b mb rdown "Oh.. Uh..."
    show yuri ma with say_dissolve
    mc ba mg "If you feel uncomfortable around me, just say so, alright?"
    y mi b1a e1b rup "No, it's not that...!"
    show yuri md with say_dissolve
    mc ml "Then what is it?"
    y shy md ee bb "I... Uh... Nothing."
    show yuri mb with say_dissolve
    _mc bd eb mh "Has Yuri ever been like this?"
    _mc ea "What's gotten into her? She was fine yesterday..."
    mc ef ba ml "Let's just... take a walk."
    show yuri turned md rup lup e3c b2a with say_dissolve
    "Yuri clasps her hands together, clearly attempting to calm down."
    y e2a me "... O- Okay."
    show yuri md with None
    hide yuri
    show cg yuri 2 
    camera master
    show bg:
        blur 0.0
    with cg_dissolve
    $ persistent.yuri.mark_cg(2)

    # [Full Voice Acting]
    "We find a concrete path circling the courtyard and begin our walk."
    "I look around- the courtyard is much calmer than it usually is."
    "Maybe it isn't surprising, considering most students are probably in their clubs right now... or at home."
    "Yuri still avoids looking at me."
    _mc bg ea mh "Am I pushing her too much?"
    _mc ef ba "Like, now that I think about it, people don't bring their friends out on a walk casually."
    _mc bi eg "Uh... Well, good job thinking ahead, Melody."
    _mc ea bb "I don't even know what I want to talk to her about."
    mc ba ml "So... It's nice weather today, right?"
    show cg turn with cg_dissolve
    y turned mh e1d "I suppose so...?"
    "We look at each other silently for a few seconds."
    show cg neutral with cg_dissolve
    "Afterwards, Yuri looks away awkwardly."
    "It's pretty clear that she has no idea what to say either..."
    mc ml nb "What do you think about... the others?"
    mc ef mg "Like, Monika... Sayori... and uh, the dangerous pink haired girl."
    show cg smile with cg_dissolve
    y e2a b1d mb "I think they're nice..."
    mc na ea ml "Why's that?"
    show cg neutral with cg_dissolve
    "Yuri pauses, collecting her thoughts."
    y e2a mb b1a "They... don't judge me."
    y e3c b1d "People usually do that... judge, I mean..."
    mc bg eg ml "I'm sorry."
    show cg turn with cg_dissolve
    "Yuri looks at me for a second."
    mc ef bi mb "People aren't really fun to begin with."
    "Yuri's eyes glow."
    y e1d mh b1a "Huh...? Usually... people don't agree with me on that."
    mc ba ea mg "Even people close to you can hurt you in some way."
    y mg "People close to you...?"
    mc eg bi mj "Sorry, let's talk about something more fun."
    show cg neutral with cg_dissolve
    y e2a b1d "O- Oh, okay."
    mc thinking ml ba ea "Hm... Why do you like the books you read?"
    y md "..."
    show cg smile with cg_dissolve
    y b1a mb "I suppose I like the stories they tell."
    y mg b1d "I- I mean-"
    y e1d mb b1a "There's all kinds of different worlds."
    y e2c mh "Some happy stories... Some sad stories..."
    y e3c mb "... I like gothic stories the most."
    show cg turn with cg_dissolve
    mc mg "Because of their elements of horror and threat of the past coming back to haunt the main character?"
    y me e1d "You...?"
    mc ldown eh md bb "Mhm. I've been reading a lot of H.P Lovecraft recently."
    "Yuri looks at me, visibly surprised."
    y mb "I didn't know you read those too."
    mc ef mb ba "We don't really talk much about our interests, now I think about it..."
    y mg "What is there to talk about?"
    y e2a b1d mh "I mean, I just read a lot..."
    show cg neutral with cg_dissolve
    "We stare at each other for a moment, before looking out at the courtyard around us."
    _mc ef mh ba "It's so difficult talking to people."
    _mc ea "I don't share many interests, and have nothing to talk about."
    _mc mf "Maybe Yuri would be interested in-"
    show cg turn with cg_dissolve
    y e1d b1d mg "Have you been hurt by people close to you...?"
    _mc eb nb mh "!!"
    mc ef mg na ba "I-... It's difficult."
    mc bi ml "Well, I don't think about it much."
    mc ea ba mg "Yet, it did shape my life into what it is now."
    "..."
    mc bd ml "... Are you sure you want to know?"
    mc ef bi mf "I mean, it's not a happy topic."
    show cg neutral with cg_dissolve
    y e1a md b1a "..."
    y e2a mh "As long as you're comfortable, MC."
    y mg b1d "I wouldn't want to push you if you don't..."
    mc ba mh "..."
    mc ml "I've been living alone for a while now."
    mc ea mg "When I was thirteen, my parents just..."
    show cg turn with cg_dissolve
    mc eg bi mb "Up and left."
    mc ef mg ba "They were busy a lot."
    mc bi ml "So, I never really saw them."
    _mc ec mh "... A bit of a white lie, but I don't need to get into all the details."
    mc ba ef mg "At first, I didn't realise how lonely life became."
    mc bi ml "But as it set in that I might never spend time with my parents again..."
    show cg neutral with cg_dissolve
    mc mf "It left me feeling..."
    mc bg ml "Hurt. Hopeless."
    mc eg bi mg "... Then, eventually, empty. Alone."
    mc mh "..."
    mc ef ba ml "They were never really great parents, especially not around the time they left, but..."
    "I let out a hefty sigh."
    show cg understand with cg_dissolve
    "Yuri gives me a gentle smile, attempting to comfort me."
    "As if to reassure me that everything is okay."
    "I see her take a good look at me, and give a little smile."
    y e1d b1a mg "MC..."
    y mb b2b e1a "It's okay."
    y b1d mh e2a "What you've gone through..."
    y e1a mb b1a "It must've hurt."
    "I give a silent nod."
    mc ea ba mg na "I had to learn a lot of things myself."
    mc ml "Eventually, I got a job, which I still work at today."
    mc ef mb "My boss is the closest person I've got to a family now..."
    mc eg bi "At least, a family that {i}actually{/i} cares about me."
    show cg neutral with cg_dissolve
    "Yuri grimaces."
    y e2a b2b mj "..."
    y e3c mg "I'm sorry..."
    mc ef ba mg na "It doesn't bother me much any more."
    "I sigh, and we both stare into the distance."

    # [End Voice Acting]
    hide cg
    show yuri turned md b1a e2a at i11
    with cg_dissolve
    $ say_transition = False

    "..."
    y "..."
    "..."
    y "..."
    mc ea ml "Should we go back to the club...?"
    show yuri e3c at dip
    "Yuri, likely still processing, nods."
    y e2a lup "..."
    y me b1d "H..."
    $ autofocus.unblock("yuri")
    y e1d b1a mg "Hey..."
    show yuri md
    mc mf "Hm?"
    y e2a mg b1d ldown "If you... ever feel like talking..."
    y b1a e1a mb "You know where to find me..."
    show yuri ma
    "I give her the strongest smile I can muster, while somewhere inside me, a tiny stick snaps."
    mc eg mb "Thanks, Yuri."

    stop music fadeout 2.0
    scene bg club_day with longfade
    $ advance_date(minutes=5)
    play music okev

    "After some time, we find ourselves back at the Literature Club, wherein we sit back down in our preferred seats."
    "I really didn't expect I'd be talking about that today."
    "My goal was to get Yuri to open up, but-"
    _mc turned ec "-Funny. I opened up instead."
    _mc ea mh "I hope Yuri doesn't find it weird, or-"
    _mc eg mm bi "Ugh. Don't overthink, MC."
    show yuri turned md b1a e2a lup at i42
    show bg:
        align (0.0, 0.8) zoom 1.9
    with Dissolve(0.2)
    "I take a good look at Yuri. Her face has returned to how it usually is."
    _mc ec mh ba "Perhaps she doesn't like to reveal her thoughts."
    _mc ea ma "I really hope I can get to know what she likes to think about some day."
    _mc mh "But for now..."
    _mc eg ma "This book will suffice."

    scene bg club_afternoon with wipeleft_scene

    "Time passes in the Literature Club."
    "Ironically enough, Yuri had been right; everyone else was just reading their own books and mainly keeping to themselves today."
    _mc turned ec "I guess we didn't end up missing anything, probably."
    "But before I know it-"
    show monika turned lpoint ma:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    m md "Well, it's about time to wrap up..."
    m mb "It was fun seeing everyone again!"
    m ed ldown "See you all tomorrow!"
    show monika ma ea at t21
    show sayori turned lup rup mb e3d:
        matrixcolor TintMatrix("#f1d6bb")
        t22
    s "See ya!"
    show monika at t31
    show sayori ma at t32
    show natsuki turned md:
        matrixcolor TintMatrix("#f1d6bb")
        t33
    n mc "Bye."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    show natsuki ma at thide
    hide natsuki
    "We all pack our things, and as the others head out..."
    show yuri turned md b1a e2a lup:
        matrixcolor TintMatrix("#f1d6bb")
        i42
    show bg:
        align (0.0, 0.8) zoom 1.9
    with Dissolve(0.2)
    "I cast my eyes back on Yuri, for one last time today."
    "..."
    _mc ef "Yeah-"
    _mc eg "See you tomorrow..."
    _mc "Yuri."

    $ add_calendar_description(calendar_descriptions["yuri"][1])

    call week_1_friday_yuri from _call_week_1_friday_yuri
    return