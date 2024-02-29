label week_1_friday_yuri:
    call calendar_transition(day=27, hour=13, minute=30, second=45) from _call_calendar_transition_38
    scene black with Dissolve(1.5)
    $ set_internet(False)
    play music playwme

    _mc turned tail nostrands eg "New day..."
    _mc "New chances."
    _mc mh "At least, school seems to think so."
    _mc bi "Yet..."

    scene bg class_2_day with Dissolve(0.2)

    "I feel a sharp poke in my cheek."
    mc turned tail nostrands eb bd mf "Huh?"
    camera master:
        align (0.0, 0.25) zoom 1.7
    show bg:
        blur 2.5 yoffset -200
    show natsuki cross mj e1d b1d at i41
    with Dissolve(0.3)
    $ say_transition = True
    $ autofocus.block("natsuki")
    "I look to my left and see Natsuki looking at me with a glaringly dangerous expression."
    n mh "Pay."
    n mm b1a e1b "Attention."
    show natsuki mj with say_dissolve
    _mc ba mh ea nb "Oh right - I'm in chemistry right now."
    mc mf "I..."
    n e2a b1d me "Tsk..."
    show natsuki md with say_dissolve
    "She quickly turns her head away from me."
    camera master
    show bg:
        blur 0.0 offset (0, 0)
    hide natsuki
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("natsuki")
    _mc ec mh "Sitting next to Natsuki might've been the scariest decision I've made today."
    _mc ea na "Although, she seems to be annoyed... More annoyed than usual that is."
    _mc thinking "Is that because of me daydreaming, or...?"
    _mc ec ma ldown "Better to not dwell on it - Natsuki is always in a sour mood, it seems."
    _mc ea mh "She is right though, I should be paying more attention."
    _mc ef "Since yesterday, I've been feeling off."
    _mc bi "Broaching my own insecurities like that, when I was expecting to help Yuri with hers..."
    _mc ec "It leaves me feeling a tad off-kilter."
    
    call close_eyes(0.4) from _call_close_eyes_21

    "With that though, I continue through my classes."
    "Each one generally the same as the day before, until eventually-"

    show bg club_day
    call open_eyes(0.2) from _call_open_eyes_13
    $ set_date(hour=15, minute=30)

    "-I find myself in the Literature Club."
    show monika turned ma lpoint at t11
    m mb "Thanks for coming by, everyone!"
    show monika ma
    "We all look up at Monika as she's standing near the blackboard."
    m mb ed rhip "Today, we'll be sharing poems with each other!"
    m ldown ea "Poems we wrote ourselves, of course. We already did other poems yesterday."
    show monika ma
    _mc eb bd nb mh "E- Eh? I don't have a poem!"
    m mb rdown ec "Through this, the idea is that we'll all learn more about each other."
    show monika ma with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show monika ea
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    m md "Additionally, it should help you better grasp your understanding of literary devices in poems."
    show monika ma with say_dissolve
    "For some reason, Monika was looking at me while saying that."
    _mc mf ec bi na "Is she politely calling me a noob?"
    hide monika
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("monika")
    "I mentally sigh."
    _mc eg mj "Time to see who I'll be spending time with..."
    show bg:
        align (1.0, 0.6) zoom 1.8
    show sayori turned e2a md at i44
    with Dissolve(0.2)
    "I look toward Sayori, near the front of the room."
    _mc ea mh ba "I haven't spent much time with her this week."
    _mc ma "Maybe I should-"
    show sayori e1b rup lup mf 
    show natsuki turned e2c b3a mg at t43
    "Natsuki approaches Sayori before I could even finish my thoughts."
    show sayori mb e3d
    show natsuki cross ma
    "..."
    _mc ec mh "I guess that answers that."
    hide natsuki
    hide sayori
    show yuri turned e2a md lup b1d at i42
    show bg:
        align (0.0, 0.8) zoom 1.9
    with Dissolve(0.2)
    "I stand up, head towards Yuri, and sit next to her."
    show yuri mf e1d b1a
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("yuri")
    y ldown e1a mb "H- Hello, MC."
    y e1d mh "Not going to share poems with Sayo-"
    show yuri me with None
    camera master
    show bg:
        blur 0.0 align (1.0, 0.6) zoom 1.8
    show sayori turned b1d e1b mj at i44
    show natsuki turned b3a mh at i43
    hide yuri
    with Dissolve(0.2)
    "She takes a quick look behind me and pauses, Sayori and Natsuki already squabbling about their poems."
    hide natsuki
    hide sayori
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0 align (0.0, 0.8) zoom 1.9
    show yuri turned md at i42
    with Dissolve(0.2)
    "I shake my head, shrugging nonchalantly."
    mc ed bg nb md "I think those two will be inseparable for a while..."
    show yuri e2a ma with say_dissolve
    mc ea mb ba na "But hey, it's fun sharing poems with each other, no?"
    y lup mb b2a "I- I guess?"
    show yuri ma with say_dissolve
    mc ef mg "... Oh, except, uh, I almost forgot I don't have any..."
    show yuri e1d me b1a with say_dissolve
    mc ea ml "Did I miss a memo or something?"
    y mg "That's okay..."
    show yuri ldown e2c md with say_dissolve
    "Yuri briefly takes a glance around."
    y e3c mb "... I don't {i}think{/i} you missed a memo..."
    y e2a b1d mg "Monika likes doing things like this from time to time."
    show yuri md with say_dissolve
    mc mg thinking "Do you think she did this on purpose?"
    mc ef bi ml "I mean, not like I really mind, just..."
    show yuri e3c with say_dissolve
    "Yuri ponders my question."
    y lup e2a b1a mg "... Maybe. I don't know for sure though..."
    show yuri md with say_dissolve
    "I shrug my shoulders and give a light sigh."
    show yuri e1d with say_dissolve
    mc eg mj ba ldown "Well, it's whatever."
    mc ea mb "Would you like to share a poem of yours?"
    y mg nb "U- Uh...  O- Okay..."
    show yuri ldown e2a b1d md with say_dissolve
    "She looks a bit nervous while rummaging through her notebook."
    show yuri e1a b1a ma na with say_dissolve
    "After a while, she procures a piece of paper, itself containing a small poem."

    $ show_poem(yuri_poem_3, music=False)
    $ advance_date(minutes=5)

    show yuri md
    "Yuri looks at me, her expression nervous."
    mc ea mh "..."
    show yuri e1d with say_dissolve
    mc mb "I like it."
    y mg "Are you... sure?"
    show yuri md with say_dissolve
    mc ml bm "Yeah?"
    mc bd mg "What do you mean? Why would I say I like it if I don't?"
    y b1d e2a lup mg "I..."
    extend e3c mb " Nevermind."
    show yuri e2a b1a md ldown with say_dissolve
    "..."
    y "..."
    show yuri e1a with say_dissolve
    "..."
    y me lup "Um..."
    show yuri e3c b1d mg with say_dissolve
    "Yuri takes a deep breath."
    y mh e2a "Let's... dissect the poem."
    y mg "It's the least we should do..."
    show yuri md e1d b1a with say_dissolve
    mc ml ba "Like Wednesday...?"
    mc mb "Except, you being the writer of it and all."
    show yuri ldown e3c ma with say_dissolve
    "Yuri gives a stern nod."
    show yuri e1a with say_dissolve
    mc md eh "Alright."
    show yuri mf e1d rup with say_dissolve
    "I take a hold of the paper, but before I can even read the poem again, Yuri interrupts me."
    y mg "Hey, MC?..."
    show yuri me with say_dissolve
    mc mf ea "Hmm?"
    y shy ma ea ba "{size=-7}Good luck...{/size}" 
    _mc ec ma "Luck... Huh."
    _mc eg "That probably means I'll need it..."
    _mc ea "Thanks, Yuri."
    _mc thinking mh ec "Ahem, Let's see..."
    show yuri turned e1d md with say_dissolve
    mc ea mg "I won't ask for confirmation, but..."
    mc ef ml "I think this poem is about how..."
    mc mf "Life can be so busy, that sometimes..."
    show yuri e2a ma with say_dissolve
    extend mg ea ldown " it's best to just stand still, and appreciate what you see around you."
    y b1d lup md "Hmm..."
    mc ea mb "I'm sure it has many more meanings, but-"
    "Before I know it, I sense a disturbance behind me."
    "I turn my head, slowly..."
    hide yuri
    show natsuki cross md b1d at i11
    camera master
    show bg:
        blur 0.0 zoom 1.0
    with Dissolve(0.5)
    $ say_transition = False
    $ autofocus.unblock("yuri")
    "There, behind my seat, stands a menacing yet short... pink-haired Natsuki."

    # [Full Voice Acting including Narrator]
    n mg "MC."
    show natsuki md
    mc ml "Natsuki?"
    n turned b1a mh "I need to borrow Yuri."
    show natsuki md e2a
    mc mg bm ed "Uh... Sure? She's not exactly 'mine' to keep?"
    "I find myself stuttering from Natsuki's sudden request, somewhere between surprised and confused."
    "Nonetheless, Natsuki completely avoids looking at me."
    n e1a b3a mh "That alright with you, Yuri?"
    show yuri turned lup rup md b2a at t21
    show natsuki md b1a at t22
    "Yuri tenses up slightly, sharing some of my concern."
    y b1a rdown e1d mg "W- What's wrong?"
    show yuri md
    n rhip e2a mg b1d "Nothing."
    show natsuki md
    _mc ec mh bi "Oh boy, the way she said 'nothing' had a lot of strength to it."
    _mc ef "... It definitely isn't 'nothing.'"
    show yuri b1d e3c ldown me at dip
    "Yuri takes in a deep breath, then lets it out."
    y e2a mg "... Alright."

    # [End Voice Acting]
    show yuri md at lhide
    hide yuri
    show natsuki rdown at lhide
    hide natsuki
    "Yuri stands up, and Natsuki leads her away from the classroom."
    play sound phone_notification
    "As if it was intentional, soon after Yuri leaves my vision, my phone vibrates."
    phone register "mc_am":
        time auto True
        "am" "Heeeeey Melody! Let's go bowling!"
    mc ea bd mf "Huh?"
    phone discussion "mc_am":
        "am" "I hope you got that reference. If not, we aren't friends anymore."
        "am" "Anyway. Do you mind if I swing on by sometime this week? I've got something I want to show you."
        "mc" "What is it?"
        "am" "Obviously not going to tell you."
        "mc" "Alright then, keep your secrets."
        "mc" "You can come over if you want, how about today?"
        "am" "What? Don't plan things on the same day, Mel!"
        "am" "You'll see me around when I feel like it."
        "mc" "Okay...?"
        "am" "Bye! Good luck with the literature club!"
        "mc" "Wait, you meant you're gonna swing by after I get out?"
    phone end discussion
    $ phone_available = True
    "As I leave that final message, Amelia quickly goes offline."
    _mc ec ba mh "... What was that about?"
    _mc ea "Sounds like she was in a rush."
    "Knowing Amelia's thought process has always been weird, I shrug and scan the room."
    _mc ec "Yuri isn't back yet, what's taking them so long?"
    _mc ea mf "Wait."
    show sayori turned e2c md at i44
    show bg:
        align (1.0, 1.0) zoom 1.3
    with Dissolve(0.2)
    _mc mh "Sayori seems to be alone now...? Huh."
    _mc thinking "Maybe she knows more as to what Natsuki wants from Yuri?"
    show sayori me e1a
    camera master:
        align (1.0, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("sayori")
    "Being curious, I approach Sayori."
    mc ldown mb "Hey Sayori? I was wondering-"
    s mg e2a "No clue."
    show sayori md with say_dissolve
    mc ml bd "I didn't even-"
    s mb e1d b1d lup "You know I'm a mind reader, riiight?~"
    s e1a mh b1a "Besides, it's not that difficult to predict. You want to know what those two are up to."
    show sayori md with say_dissolve
    mc ef mf bi "Yeah..."
    show sayori ldown with say_dissolve
    "..."
    "A few seconds of staring at each other pass."
    mc ea mg ba "Do you... really not know anything?"
    s e3c mi "Weelll... Natsuki has been very agitated today."
    s e2a mh "Maybe Yuri forgot something Natsuki asked her to do or bring...?"
    s e1b lup mg b1d "Or... Yuri stole her favourite book?"
    show sayori md with say_dissolve
    mc bg nb ml eb "Y- Yuri stole a book?"
    s mn ldown e3d b1a "No, silly... You just don't know Yuri well yet!"
    show sayori md e1a with say_dissolve
    mc bi mj eg "And {i}you{/i} don't know that you almost gave me a heart attack."
    s mg "Oh? Why's that?"
    s e1d mh b1d "Do you..."
    extend mb e1a b1a lup " maybe like her?"
    show sayori ma with say_dissolve
    mc bd ea mg "H- Huh? How do heart attacks correlate to liking someone?"
    s ldown e3c mn "Just teasing you Melly, teehee~"
    show sayori ma with say_dissolve
    mc ml ba ef "Ha ha... But seriously now."
    show sayori e1a with say_dissolve
    mc ea na mg thinking "Are you saying Natsuki normally {i}isn't{/i} this irritated?"
    s mh "I know she looks menacing at times, but she's not a grumpy cat."
    show sayori md with say_dissolve
    mc mb ef bi ldown "... Is she now..."
    show sayori e1d b1d mj with say_dissolve
    "Sayori looks at me with a similar glare as Natsuki."
    s e1a lup mb b1a "Nope~"
    show sayori ma with say_dissolve
    mc ml ba ea "Do you think I should take a look...?"
    show sayori ldown with say_dissolve
    m "Now now... let them talk, I doubt it's anything serious."
    show sayori at i44
    show monika turned rhip at i43
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Monika joins the conversation, seemingly unconcerned with the situation."
    m rdown mb "They've never had any serious quarrels in the past, so why would that change?"
    show monika ma
    _mc  mh "That surprises me."
    show monika mc
    mc ml"Monika?"
    m md "Yeah, MC?"
    show monika mc
    "..."
    show sayori md
    mc ef mg bg "Do you think this may have something to do with me?"
    show monika rhip
    "Monika raises an eyebrow."
    m md "Why do you say that?"
    show monika mc
    show sayori b2a ma
    mc ea ml ba "Natsuki looked like she was irritated with me this morning."
    mc ef mb bi "I mean... I wasn't paying attention, but..."
    mc ea mg ba "She usually looks... normal during class. Kind of stoic, maybe."
    $ autofocus.unblock("sayori")
    s mb "Maybe she got out on the wrong side of bed this morning?"
    show sayori ma with None
    hide sayori
    hide monika
    show bg:
        zoom 1.0
    show natsuki turned lhip e2a md at i11
    with Dissolve(0.2)
    "Before either of us have the chance to open our mouths again, Natsuki steps into the room."
    "Seemingly, without Yuri."
    show natsuki e1a b1d ldown
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    "Without thinking, I stand up and block Natsuki's path."

    # [Full Voice Acting]
    show natsuki e1a b1a md with say_dissolve
    mc bd ml "Where's Yuri?"
    n "..."
    n mg e2a "Inside the restroom."
    show natsuki md with say_dissolve
    mc mg ba "What did you two talk about?"
    n cross b1d mg "None"
    extend e1a b1a me " of"
    extend mg e1d b1d " your"
    extend e1b mm b1a" business."
    show natsuki mj with None
    show natsuki md b1a e3c at i41
    camera master
    show bg:
        blur 0.0
        align (0.4, 0.6) zoom 1.9
    with Dissolve(0.2)
    $ say_transition = False
    "She shoves me aside and sits a couple of seats away from us."
    show natsuki me
    "..."
    show natsuki md e2a
    "Now staring at her table, she holds a different expression from this morning."
    "Instead of being irritated, she looks..."
    show natsuki mj b2a
    "Sad?"
    hide natsuki
    show bg:
        zoom 1.0
    show monika turned mc at i21
    show sayori turned mj b2b at i22
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    s mb lup b2a "I'll talk to her."
    show sayori mj e2a ldown at lhide
    hide sayori
    show monika at t11
    mc mf "Did Natsuki..."
    m md rhip ec bc "No, Natsuki wouldn't hurt Yuri."
    show monika mc ba ea nb rdown
    camera master at vpunch
    play sound slam
    stop music
    "Just then, I hear a loud bang coming from Natsuki's direction."
    hide monika
    show natsuki turned mm e1b b1d at i41
    show sayori turned lup b2c nb me at i42
    show bg:
        zoom 1.9
    with Dissolve(0.3)
    n cross mh e2a "J- Just leave me alone for a while."
    show natsuki md at lhide
    hide natsuki
    show sayori e2a ldown mj 
    "She stands up and heads for the restrooms as well."
    show sayori turned b2a e2a mk at i21
    show monika turned mc at i22
    show bg:
        zoom 1.0
    with Dissolve(0.2)
    play ambient int_day fadein 3.0
    "Sayori backs off towards us."
    s mg "S- Sorry, Natsuki..."
    show sayori mj 
    show monika bc ec md rdown 
    "Monika sighs to herself."
    m eb md "I think it's about time I figure out what's going on."
    show monika at lhide zorder 1
    hide monika
    show sayori at t11
    "She then leaves the room after Natsuki."

    # [End Voice Acting]
    mc bg nb "G- Geez..."
    s mh e1a "So remember how you asked if this was about you...?" 
    show sayori b1b e2a me lup
    "Sayori looks around her, as if she's about to say something meant only for my ears."
    s b1a e1a mg "I..."
    extend b1b e2a me " don't think this is about you..."
    show sayori mj ldown 
    mc thinking ed ml "Hmm... shouldn't we do something?"
    s b1a mg na "All we can do for now is stay here and wait it out."
    show sayori md
    "I let out a sigh."
    mc ldown ef mg "... Alright."
    "Sayori and I sit down next to each other for the first time in a while, talking about all sorts of things."
    "While it helps distract me, it doesn't clear my mind of what just happened."
    _mc bi eg mh "Yuri... What's going on?"
    show bg club_afternoon:
    show sayori mj:
        matrixcolor TintMatrix("#f1d6bb")
    with NonBlockingDissolve(3.0)
    $ advance_date(minutes=57)
    "Eventually, the sky began to glow an orange hue."
    "Looking at the clock on the wall, I can see it's close to closing time."
    show sayori e1a md
    _mc ea mh ba "Where are the others?"
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("sayori")
    "I look over at Sayori, and she seems to realize what I'm thinking."
    s mg lup "Well... if they're still out, I guess I could end the meeting as vice president?"
    show sayori md with say_dissolve
    mc ef mg "I don't mean to push this onto you, but it is getting late..."
    mc thinking ml "Before we do... Maybe we should check-"
    camera master
    hide sayori
    show bg:
        blur 0.0
    show monika turned mc ec:
        matrixcolor TintMatrix("#f1d6bb")
        i33
    show natsuki lhip rhip md e2a b1d turned:
        matrixcolor TintMatrix("#f1d6bb")
        i32
    show yuri shy eb:
        matrixcolor TintMatrix("#f1d6bb")
        i31
    with Dissolve(0.2)
    stop ambient fadeout 2.5
    "Thankfully, neither of us get to finish this line of thought, as the three others return."
    hide monika
    hide natsuki
    show yuri ea at i11
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.1) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ autofocus.block("yuri")
    $ say_transition = True
    play music myfeelings
    "Yuri, specifically, walks past me, catching me by surprise."
    mc mf ea bg ldown "Yuri?"
    "She stands still for a few seconds, her back facing towards me."
    y bb "I... I'm sorry, MC."
    mc mg "Sorry? What for?"
    show yuri ma with None
    hide yuri
    show bg:
        blur 0.0
    with NonBlockingDissolve(0.5)
    "Without saying a word, she continues on towards her seat."
    _mc bd mf "What even?..."
    show natsuki turned e2a md:
        matrixcolor TintMatrix("#f1d6bb")
        i21
    show monika turned mc eb:
        matrixcolor TintMatrix("#f1d6bb")
        i22
    camera master
    with Dissolve(0.2)
    "I take a quick look at Natsuki from the corner of my eye. She seems calm."
    "So does Monika."
    _mc eb mh "What even happened there?"
    show monika at thide
    show natsuki at thide
    hide monika
    hide natsuki
    show sayori turned b2b mg e2a lup:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    s "Maybe it's best if we let it be for today..."
    show sayori mj
    mc ml bg ea "What? Why?"
    mc bd mg "What if-"
    hide sayori
    show yuri turned e2a md b1d:
        i21
        matrixcolor TintMatrix("#f1d6bb")
    show bg:
        align (0.0, 0.8) zoom 1.9
    with Dissolve(0.2)
    "In the corner of my eye, I see Yuri once again."
    show bg:
        blur 0.0
    hide yuri
    with Dissolve(0.2)
    $ autofocus.unblock("yuri")
    $ say_transition = False
    "She packs her things, and leaves just as quickly as she entered the room."
    show monika turned mb rhip:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    show bg:
        zoom 1.0
    with Dissolve(0.2)
    m "Considering the time... I wish you all a nice weekend."
    show monika ma at t21
    show sayori turned e3d mb:
        matrixcolor TintMatrix("#f1d6bb")
        t22
    s "See you all!~"
    show monika at t32
    show sayori ma at t33
    show natsuki cross mg e2a:
        matrixcolor TintMatrix("#f1d6bb")
        t31
    n "Bye."
    show monika at lhide
    hide monika
    show natsuki md at lhide
    hide natsuki
    show sayori at t11
    s e2a mb "I'm not sure what's going on, but..."
    s mg "I think everything will be fine."
    s md b1b "..."
    s e1a b1a mb "See you."
    show sayori ma e2a at lhide
    hide sayori
    "..."
    _mc eb bd mh "... Wait, huh?"
    _mc ea "What's going on? Are we going to pretend nothing happened?"
    "..."
    show black with NonBlockingDissolve(0.5)
    _mc ec bi mh "Maybe everyone just needs time..."
    "As I pack my stuff, I feel a hand on my shoulder." # im stuff
    show monika turned nb eb bb:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    hide black
    with Dissolve(0.5)
    $ autofocus.block("monika")
    $ say_transition = True
    m mb "Hey, MC..."
    m ec md bb "Sorry about today."
    show monika mc with say_dissolve
    mc bb ea ml "No, it isn't your fault, but..."
    show monika ea with say_dissolve
    mc mg na ba "What happened between those two?"
    show monika eb bc na with say_dissolve
    "Monika glances around, before returning her eyes to me."
    m ea md ba "Natsuki was worried about Yuri."
    m eb "But as Yuri was already stressed, she couldn't take any more and locked herself in the restroom."
    show monika mc with say_dissolve
    mc thinking "What was she worried about?"
    show monika bc with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False    
    m "..."
    $ autofocus.unblock("monika")
    m md ec rhip "Well..."
    m mc "..."
    m mb "It's not that important, now I think about it."
    show monika mc
    mc ml bd ldown "Important or not, I'd like to know."
    mc ba mg "Yuri was involved so-"
    show monika ba ea rdown
    "Monika raises her brows."
    m md "Talk to Yuri tomorrow."
    show monika mc
    "I look at her in confusion."
    _mc thinking mh "Is this some sort of test?"
    _mc ec bi "See how long I can bear being given the minimum amount of information?"
    _mc ef ba ldown "I get that I'm new..."
    _mc ec bi "No, this is wrong."
    mc eg mm "Why?"
    mc ea bd mg "Why are you all being so secretive?"
    mc ml ba "Is it something about me?"
    mc mg bd "Something about the club?"
    mc ec mg bi "Help me understand."
    show monika eb
    "Monika looks around her."
    _mc ea ba mh "Is she looking for a way out?"
    _mc ec bi "No, Monika wouldn't run."
    _mc eg "She doesn't seem the type."
    m md "MC."
    m rhip ea "This situation is not as simple as 'knowing' what's going on."
    m eb bc "It's... deeper that that."
    m mb ea ba "That's why I said, talk to Yuri tomorrow."
    m bb rdown "Okay?"
    show monika bc eb md
    "She mutters something under her breath."
    show monika ea ba mc
    mc mg bi ec "Repeat that?"
    m md "You mean, okay?"
    show monika mc
    mc ea bd ml "No, I meant..."
    "I sigh."
    mc eg bi mj "Nevermind."
    _mc ec mh "I swear I heard her say something under her breath..."
    m mb "Afterwards, talk to me."
    show monika ma
    mc ef ml ba "Fine, I guess."
    show monika mc at thide
    hide monika
    "I head over to my things, to prepare to pack up."
    m turned md "And... MC."
    show monika ma:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "I turn my head to face Monika once more."
    m md lpoint "Natsuki might be fierce, but that doesn't mean she has no heart."
    m ldown mb bb "Please understand."
    show monika ma with say_dissolve
    _mc ec ma bi "Difficult to imagine."
    _mc ef mh ba "But I'll put up with her for now."
    mc mf "... Fine."
    camera master
    show bg:
        blur 0.0
    show monika ec bc md
    with Dissolve(0.2)
    $ say_transition = False
    "Monika then lets out a sigh. Not one of frustration, but just tired."
    $ autofocus.unblock("monika")
    m rhip eb ba mb "Well, if you don't mind, I think I'll be going home too."
    m rdown ea "Enjoy your weekend, okay?"
    show monika ma 
    mc mb ba ea na "I will. You too, Monika." 
    show monika at thide
    hide monika
    "We both pack our stuff, and head on home." # im stuff
    _mc ec ma "She's right. I shouldn't be so judgmental about Natsuki."
    _mc eg mh bg "I just hope Yuri's alright."

    stop music fadeout 2.0
    scene black with monika_pov(True)
    play ambient ext_night fadein 3.0
    $ set_pov("m")
    $ advance_date(minutes=10)

    # [Full Voice Acting including Narrator]
    m turned md bb "Oh, Melody..."
    _m mc "She seems so concerned about Yuri."
    _m ec bc "Maybe I should've told her more...?"
    "..."
    _m eb "No, that's something only Yuri can tell her."
    "I let out yet another sigh today."
    _m ec ba md "Yuri's panic attacks have been getting worse lately."
    _m mc "If they were to get too bad..."
    _m ea "Would Melody be there to help her?"
    m eb md "I do hope so."
    "The wind rustles around me as I continue walking."
    _m ea bc mc "... But what if I'm wrong?"
    _m ba "Placing the burden onto Melody isn't good for either of them."
    _m eb "And if Melody doesn't respond in the way Yuri expects..."
    _m bc "That just might cause even more panic attacks instead."
    show sky_night at moving_sky
    show sky_afternoon at moving_sky:
        alpha 0.4
    hide black
    with NonBlockingDissolve(2.0)
    "I sigh, staring into the clouds slowly darkening the sky as the evening approaches."
    _m ec ba "I guess it wouldn't hurt keeping my eyes on the two."
    _m "See how they develop, and..."
    extend " if the conditions are right..."
    _m ma "Prosper."

    $ add_calendar_description(calendar_descriptions["yuri"][2])

    call week_1_saturday_yuri from _call_week_1_saturday_yuri
    return