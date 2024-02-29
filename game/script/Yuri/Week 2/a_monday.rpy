label week_2_monday_yuri:
    call calendar_transition(day=30, hour=8, minute=20) from _call_calendar_transition_41 
    scene bg school_corridor_3_day with dissolve_scene_full
    $ set_internet(False)
    play music playwme

    "Dragging this bag filled with decorations to school while also lugging my schoolbag-"
    _mc turned ec bi mh nb "-Seems to draw eyes in my direction."
    _mc ea ba "I mean, fair, but don't the other clubs have decorations of their own...?"
    "Shrugging it off, I place the bag inside my booklocker for safekeeping and head off toward my classroom on the third floor."
    
    scene bg school_corridor_1_day:
        xzoom -1
    with wipeleft
    $ advance_date(minutes=7)

    "As I arrive, I spy a certain purple haired individual outside."
    show yuri turned lup e2a b1d md at t11
    _mc turned mh "Yuri? Is something going on inside?"
    "The girl stands near the door, but seems to have little interest in walking inside herself."
    _mc ec "Is she waiting for something?"
    _mc bi "Or, someone...?"
    "Approaching her carefully, so as to not spook her again, I give her a wave."
    mc ea mb ba "Hey Yuri!"
    $ autofocus.block("yuri")
    y b1a nb e1b rup me "!"
    $ autofocus.unblock("yuri")
    y ldown b2b e3c mg "H- Hey MC!"
    show yuri e1a b1a ma na
    mc ml "Are you waiting for something? The teacher is already in the classroom."
    y rdown e2a b1d mg "No, no... just... standing here."
    show yuri md
    _mc bd mh "Is she alright?"
    _mc ec ba thinking "Hmm... Might be best to talk to her about it later, not when we're surrounded by the bustle of the entire cohort."
    mc ldown mb ea "Let's head into class, the bell's gonna go off any second."
    y e3c mg "Alright..."
    show yuri md
    "But before I step into class..."
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    show yuri shy ma
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("yuri")
    "Yuri grabs my arm."
    "Tightly."
    "She whispers."
    y bb eb "{size=-5}I... need to talk to you after classes...{/size}"
    y ea mc "Is that alright?"
    mc mf nb "A- Alright."
    y ba eb ma "T- Thanks."
    
    scene bg class_2_day:
        xzoom -1
    camera master
    with wipeleft
    $ say_transition = False
    $ autofocus.unblock("yuri")

    "She lets me go, and we head on into class as I shake my arm."
    "For some reason, everything feels tense, all of a sudden."
    show yuri turned md e2a at i11
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "Letting out a sigh, I glance Yuri's way, but she's already turned her attention to the board."
    "Shrugging, I follow her lead, taking my seat and preparing for the day."
    hide yuri
    hide bg
    show black
    camera master
    with Dissolve(0.3)
    "At times, I glance toward Yuri, whenever my curiosity gets the better of me."
    _mc turned ec mh thinking "I wonder what she wants to talk to me about."
    _mc ea "Could it be about last Friday?"
    _mc ec "Hmm..."

    scene bg club_day with wipeleft
    $ set_date(minute=17, hour=15)

    show monika turned at t11
    "As I step into the clubroom, I'm greeted by Monika, who gives me a wave."
    m mb "Nice to see you again, MC."
    show monika mc
    "She pauses, looking over me."
    $ autofocus.block("monika")
    m "..."
    $ autofocus.unblock("monika")
    m lpoint md "Did... you bring the festival decorations?"
    show monika mc
    mc turned mg bb nb eb "O- Oh!"
    show monika ma bb ldown
    mc bg eh md "I forgot to grab them back out of my locker - I'll be right back, okay?"
    m ed mb "Take your time!"
    show monika ma

    scene bg school_corridor_1_day with wipeleft

    "I head on out with a little bit of a sprint."
    
    scene bg school_lockers_day with wipeleft

    "Reaching my lockers, I grab the bag and head back."
    _mc turned nb mh "This festival is going to be quite something."
    _mc eb bd "Considering the weight of this bag..."
    
    scene bg club_day
    show yuri turned e2a b1d md at i31
    show monika turned eb mc at i32
    show natsuki cross e2c mj at i33
    with wipeleft_scene

    "Returning to the clubroom, I see everyone reading a book, or in Natsuki's case, manga."
    show monika ea
    show natsuki at thide
    show yuri at thide
    mc turned mf "Uh...?"
    hide natsuki
    hide yuri
    hide sayori
    show monika mb at t11
    m "Ah, thanks MC!"
    show monika ma at thide
    hide monika
    "Monika walks over to me, grabbing the decorations and walking to the closet over yonder." 
    m turned eb md "I don't have anything planned for today, so..."
    m ea mb "Just reading seems more suitable."
    mc mb ea "Suitable compared to what?"
    show monika ma at t11
    "Monika puts the decorations away, then walks back to me."
    m md "Worrying about the festival."
    m mb "Which is not something we should do yet."
    m ec "Not even you, MC."
    show monika ma
    mc thinking mg "Is the festival that big of a deal?"
    show monika mc ea bc
    "Monika squints her eyes."
    m md "Outside of us coming up to people, or the occasional person eavesdropping on us..."
    m ba lpoint "It's the only official way to {i}really{/i} promote our club."
    m mb "So, I think it's quite a big deal."
    show monika ma
    _mc mh ef ldown "Ah..."
    mc ea mb "That makes sense."
    show monika bc eb mc ldown
    "Monika then glances around, before giving me a slightly worried expression."
    m md rhip "By the way, have you seen Sayori?"
    show monika mc
    mc mh "Hmm?"
    _mc ec bi thinking "Now that I think about it... I have not seen her, huh."
    mc ea mg ba "I haven't, maybe she's late?"
    show monika ec md at dip
    "Monika sighs."
    m ed mb rdown ba "Well, hopefully she'll turn up soon."
    show monika ea ma
    mc mb ldown "Yeah, she's not one to skip out on the club, so... She might have been caught up planning this sleepover of hers, knowing her?"
    m eb mb "Yeah... Maybe. We might just have to wait and see."
    show monika ma
    "Monika seems to shrug, probably not too convinced by my half-hearted attempt at levity."
    "..."
    show monika ea
    mc mg "Well... I'm going to give the closet a look for myself."
    m mb ed "Okay!"
    show monika ma
    
    scene bg club_closet_day with wipeleft
    $ advance_date(minutes=10)

    _mc turned ec mh "Huh."
    camera master:
        align (0.5, 0.65) zoom 1.6
    with Dissolve(0.2)
    "This closet is more filled than I was expecting."
    _mc ea ma "Tons of books... boxes... Oh! And here's Monika's bag of decorations."
    _mc ec "It looks like everything is all there, so..."
    show bg club_day
    show sayori turned nb ml xd b2a at i11
    camera master
    with NonBlockingDissolve(0.5)
    "Speaking of Sayori... She shows up to the club, exhausted and breathing heavily."
    s b2c e3a lup mk "P- Phew, I'm not... late, am I?"
    show sayori me
    mc mg ed bm "You are, technically..." 
    "I look at my phone."
    _mc ec mh ba "About 15 minutes late."
    show sayori b2a e3c mg ldown at dip
    s "Darnit..."
    show sayori md
    mc mb  ea"Well, showing up is more important than coming on time, so..."
    s e1a mh b1a na "Really?"
    show sayori md at t22
    show monika turned rhip bc ec mc at t21
    "Monika chimes in, flabbergasted."
    m md ea "Please don't take that as an invitation to come late every day."
    show monika rdown ba ma
    s lup rup mb e3d "No worries, Monika~"
    show sayori ldown rdown ma at dip
    "She picks up her bag of decorations."
    s rup e1a mh "I remembered to bring this!"
    show sayori ma
    m mb "Ah, thanks Sayori! You can put it in the closet."
    show monika ma at thide
    show sayori rdown lup mj b1d e1b
    "Sayori gives a salute as if she's in the army, then heads off to put her bag down next to ours."
    show sayori ldown e3d b1a ma at rhide
    hide sayori
    hide monika
    _mc ec mh "Well, it's about time to talk to Yuri."
    "As I turn my head to look at Yuri..."

    show bg:
        align (0.0, 0.7) zoom 1.3
    show yuri turned e2a md:
        i41
        zoom 0.7
    show natsuki cross e2a mg:
        i42
        zoom 0.7
    with Dissolve(0.3)
    $ autofocus.block("natsuki")
    $ autofocus.block("yuri")
    $ say_transition = True
    $ autofocus.zorder = False
    _mc ea "Huh?"
    _mc "Natsuki's talking to her?"
    _mc ec bi "What's she up to?"
    show natsuki md with say_dissolve
    "I come a little closer, practising my stealth skills."
    camera master:
        align (0.5, 0.7) zoom 1.2
    show yuri e2c
    with Dissolve(0.2)
    n b1d mg "What I want to say is..."
    n turned b1a mh e3c "I'm... sorry, Yuri."
    n lhip e2a mb "About last week."
    show yuri ma b2a
    n mh b1d "I was worried about you."
    show natsuki md
    y lup rup b2b e3c mb "Thanks... Natsuki."
    show yuri ma
    hide natsuki
    with Dissolve(0.2)
    $ autofocus.zorder = True
    "Seemingly having more to say, but not having the confidence to do so, Natsuki goes back to her seat to read her manga."
    show yuri rdown e2a with say_dissolve
    _mc ec ma ba na "So Natsuki is not as menacing as I thought..."
    _mc ef "Kind of sweet, actua-"
    n turned b1d e1d mg "MC."
    _mc eb bd nb mh "!!"
    show bg:
        zoom 1.0 blur 2.0
    hide yuri
    camera master:
        align (0.5, 0.25) zoom 1.5
    show natsuki md at i11
    with Dissolve(0.2)
    mc ea ba mf "Natsuki?"
    n b1a e1a mh "Staring is rude."
    show natsuki md with say_dissolve
    mc ml bd na "I'm not staring."
    n cross e2a b1d mg "Tsk."
    show natsuki e1d mj with say_dissolve
    "Natsuki glances as me as if she tries to pierce my soul."
    mc mg bb "Seriously, I am not."
    mc ml ec bi "Why are you always so-"
    camera master
    show yuri turned lup md at i42
    show bg:
        align (0.0, 0.8) zoom 1.9 blur 0.0
    hide natsuki
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("natsuki")
    "But before I finish my sentence, I see Yuri looking at me."
    _mc mh "Right, let's not make a scene infront of Yuri."
    n turned b1d mh "Always what?"
    mc eg mj "Forget it."
    show bg:
        zoom 1.0
    hide yuri
    show natsuki me at i11
    with Dissolve(0.2) 
    "I walk past Natsuki, who's face almost smokes out of irritation."
    n e1b mg "You-"
    show natsuki me with None
    hide natsuki
    show bg:
        zoom 1.9 align (0.0, 0.8) blur 2.0
    show yuri turned e1d lup at i42
    camera master:
        align (0.5, 0.1) zoom 1.5
    with Dissolve(0.2)
    $ say_transition = True
    "Ignoring Natsuki's attempt at starting a fight, I head towards Yuri."
    mc ea ba mb na "Hey, Yuri. You wanted to talk?"
    show yuri e2a md with say_dissolve
    "Yuri glances down."
    y b1d e3c mg ldown "Um, do you mind if we talk later?"
    y e2a mh "I need some time to think..."
    show yuri md with say_dissolve
    mc ml "Alright. You know where to find me."
    camera master:
        zoom 1.7
    show bg:
        blur 2.5
    show yuri lup e1a b1d md 
    with Dissolve(0.2)
    "Suddenly, Yuri grabs my arm and whispers."
    y mg "Please don't start a fight."
    show yuri md
    "I raise my eyebrows."
    mc mh ba ea "Hmm."
    mc ef ml bi "... Sure."
    mc mg ba "Come to me whenever you are ready, okay?"
    show yuri e3c ldown b1a mj with say_dissolve
    "Yuri nods, and I head on my way to sit somewhere else."
    camera master
    hide yuri
    show expression split("bg class_2_day", "bg club_day") as bg:
        zoom 1.0 blur 0.0
    show natsuki cross mj e2a b1d at i33
    show monika turned mc bc at i31
    with Dissolve(0.2)
    $ autofocus.unblock("yuri")
    "As I move away from Yuri and look around the room..."
    "Seeing Natsuki's irritated face, Monika's eagle eyed stare at me..."
    "I can't help but think."
    show black:
        alpha 0.5
    with NonBlockingDissolve(0.2)
    _mc ea bd mh thinking "What's going on?"
    _mc ec bi "I feel like there's some gigantic secret hidden in the air."
    _mc eg "Yet, I am the only one who doesn't know it."
    _mc ldown "..."
    _mc mm "Ugh. I hate this idea but..."
    _mc ea ba mh "... Maybe I could talk to Natsuki about it?"
    _mc ec "Approaching her like that may be dangerous after a near miss, but..."
    _mc ef "I do have to get to know her at some point."
    _mc bi "Especially since that grudge of hers won't go away automatically."
    _mc ec "And neither will mine..."
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg club_day:
        blur 2.0 align (1.0, 0.9) zoom 1.2
    hide black
    hide monika
    show natsuki cross e1b b1d md at i11
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    "Full of confidence, I stand up, and sit next to Natsuki."
    n me "!..."
    n turned mg e1a "Why are you..."
    show natsuki me with say_dissolve
    mc mg ba ea na "Do you mind if I talk to you?"
    "Natsuki looks me over like a predator scanning its prey."
    stop music fadeout 2.0
    n e1d mg "I mind."
    show natsuki md with say_dissolve
    _mc ec mh "..."
    show natsuki e1a with say_dissolve
    mc ea mg thinking "How well do you know Yuri?"
    n mg "Well enough."
    show natsuki mj with say_dissolve
    mc ef bi ml "I feel like there's something going on with Yuri lately."
    mc ba mg "I don't understand what it is, but..."
    mc ea ml ldown "Maybe you know?"
    n cross mg e1d "I don't."
    show natsuki md with say_dissolve
    _mc ec bi mh "Gosh, those short responses don't really help."
    mc ea bd ml "What's your {i}damage?{/i}"
    n e1a me "..."

    play music myconfession

    n turned lhip rhip mi e1d "Are you stupid?"
    show natsuki mj with say_dissolve
    mc mf "What?"
    n cross b4 mh "Thursday."
    show natsuki mj with say_dissolve
    _mc ec bi mh "Thursday... Thursday..."
    _mc eg "What did I do that day?"
    _mc ea ba "Was that when I took Yuri to the courtyard?..."
    show natsuki e3c me b1d with say_dissolve
    mc ml bd "Are you angry about that?"
    n turned b3a mh ldown rdown e1a "MC, we don't just bail on the Literature Club."
    n e1d b1d mg "... Unless the club means nothing to you."
    show natsuki me with say_dissolve
    mc ba "Slow down a second, that's not-"
    n mg e3c "Don't"
    extend mh e1d " make"
    extend e1b mm " excuses."
    n cross mi e1a b3d "Take responsibility."
    show natsuki mj with say_dissolve
    "Natsuki's real pissed, while I'm just plain confused."
    mc mf bd "Take responsibility for... leaving for a bit during clubtime?"
    show natsuki e1d mm with say_dissolve
    mc ml ba "... I guess I'm sorry?"
    n turned mg e1b "Lose that tone and stop playing dumb."
    show natsuki md with say_dissolve
    mc eb bd nb mg "I'm not playing dumb! {i}You're{/i} just {i}being{/i} dumb!"
    n me "..."
    n b1d e1d mh "Okay, I'm giving you ten seconds to rephrase."
    show natsuki mj with say_dissolve
    mc ml ea na "What do you want me to say?"
    mc ba mg "Last I checked, it's not a crime to leave the club for a few moments."
    mc ec mj bi "And I'm not some repeat offender for you to talk to me like this."
    show natsuki e1b b3d with say_dissolve
    mc ea bd mg "If it really is about me \"leaving\" the club, then Monika would have this talk with me, not you."
    mc ml ba "Besides, we didn't miss anything."
    show natsuki mm with say_dissolve
    "Natsuki looks angrier than ever."
    "It's almost as if she's considering punting me out of the window."
    n mg "That's not the point, you idiot."
    n cross b1d e1d mh "Look at you, flapping your gums so proudly like you know anything..."
    n e1a mi "What if something did {i}happen?{/i}"
    show natsuki mj with say_dissolve
    mc ml bd "With Yuri, you mean? Because {i}that's{/i} the problem, right?"
    _mc ec bi mh "I promised Yuri I wouldn't start a fight, but bloody hell, this woman is testing my patience!"
    mc mg "What could have happened that's so bad you have to fret over Yuri like she's some lost child?"
    n turned mm "When I say manage your tone, {i}Melody{/i}, that's not an empty threat."
    show natsuki mj with say_dissolve
    _mc eb bd mh "Excuse me?"
    show natsuki e1a with say_dissolve
    mc mm "Who are you calling Melody?"
    mc ea mg "Who gave you that right?"
    show natsuki md with say_dissolve
    mc ec bi "Because last {i}I{/i} checked, it wasn't me."
    n e2c me "..."
    camera master
    show bg:
        blur 0.0 zoom 1.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("natsuki")
    n mg rhip "... Sorry, I didn't mean to, MC."
    show natsuki md
    mc mf "Uh huh."
    mc eg mj "Sure, fine. I suppose."
    "I have so much running through my mind, but I'm starting to realize this conversation isn't heading anywhere productive."
    mc ec mf "I'm just saying..."
    mc ml ea ba "Next time you want to gesture at violence, Natsuki..."
    show natsuki e2a
    mc mg ec bi "I implore you to remember the band around your arm."
    show natsuki mj e3c rdown
    mc eg mb "Because I have a little feeling that series of events is going to end {i}far{/i} worse for you than for me."
    show bg:
        align (0.0, 0.8) zoom 1.9 
    camera master
    hide natsuki
    show yuri turned e1a tears_a lup rup b2b mm:
        i42
        easein 0.3 xoffset -700
        alpha 0.0
    with Dissolve(0.2)
    "As I let my anger get the best of me while dealing with the pink mafia, in the corner of my eye, I notice Yuri leaving with tears on her face."
    mc mf bg na ea "Huh?"
    show natsuki turned me e2a b1d at t11
    "Natsuki looks in Yuri's direction, then to me, with a face of concern."
    n mh b2a "Did you say something to her?"
    show natsuki me
    mc bf mg nb "What? I didn't!"
    show natsuki b1d e2a md at lhide
    hide natsuki
    hide yuri
    "She looks at me unsatisfied, and heads off after Yuri."
    "I try to go after her, but..."
    n turned mi b3d "Don't follow me."
    n e2a b1d mh "You'll only make it worse."
    mc ef bi mh "..."
    show black with NonBlockingDissolve(0.5)
    "As she storms off, I I find myself wanting to storm right out as well."
    "Yet I'm frozen. The cloud of doubt and unease that's surrounded this club since that Thursday is paralyzing me like nerve gas."
    _mc eg ba na "The cloud that's surrounded me."
    hide black
    show bg:
        zoom 1.0
    with NonBlockingDissolve(0.5)
    "Defeated, I return to my seat, obeying Natsuki like the idiot I am."
    _mc bi "And after all my big talk..."
    _mc ec "Damn it."
    show sayori turned lup mh at t11
    s "Something wrong with them?"
    show sayori md
    "Sayori walks over, noticing what happened."
    mc mg ea ba "I don't know."
    mc ef bg ml "But, she..."
    "I trail off a little, not sure how much to say, but it seems Sayori's caught herself up regardless."
    s ldown e3c mg "Oh..."
    show sayori md
    "Sayori lets out a sigh of her own."
    $ autofocus.block("sayori")
    s e2a "..."
    $ autofocus.unblock("sayori")
    s e1a mh "Mind if I sit next to you?"
    show sayori md
    mc thinking mg ea ba "Something on your mind?"
    "Sayori pouts."
    s e1b ml "Wah-"
    s tap md bc "I can't sit next to a friend without a reason?"
    show sayori ma
    mc bd ldown "I didn't say that!"
    show sayori turned lup e3d mn at dip
    "Sayori pokes me on my nose and giggles."
    s ldown mb e1a "You take everything so seriously..."
    s mh "Anyway. I just saw you talking with Natsuki."
    s mb "How did it go?"
    show sayori ma
    mc ef mf bi "Uh."
    show sayori md
    mc ml "Somehow..."
    mc thinking ea bm mg "Better than expected."
    s mh "... What did you expect?"
    show sayori md nb
    mc ml bi ef ldown "I don't know, for her to pull a gun on me?"
    s lup b1d mh na "What? Natsuki doesn't even own a gun!"
    show sayori mj
    pause 0.8
    s e2a b2c mb nb "I think..."
    show sayori ma
    mc mg ba ea "How close are you two, actually?"
    show sayori ldown na b1a e1a md
    mc ml ef "I've seen you two together a lot last week."
    show sayori e2a ma
    "Sayori smiles, looking off into the distance."
    s mb "Natsuki's my best friend."
    s e3c mh "Although she can be a little intimidating--"
    show sayori me
    mc mb bi "That's the understatement of the century."
    s e1a mb "--once she gets to know you, she can be the kindest person in the world."
    show sayori ma
    mc ea ml ba "Really?"
    _mc ec mh "Colour me surprised."
    s e3c mi "That may be an exaggeration, but it sounds nicer that way."
    s lup mh e1a "She really cares about people."
    s mb "She's probably just suspicious of you - You're new, and the dynamic of the club is different now."
    show sayori ma ldown
    _mc bi "She's more than just suspicious..."
    mc ef ba "Hm."
    "..."
    $ autofocus.block("sayori")
    s md "..."
    "..."
    $ autofocus.unblock("sayori")
    s mg "Well?"
    show sayori md
    mc ea mf "Well what?"
    s tap md bc "What did you two taaaaalk abouuuuut???"
    s turned b2b e3c mh "Geez, Melly! You're quite out of it today."
    show sayori mj
    mc mb ef bg "Yeah..."
    show sayori b1a md e1a
    mc ea mg ba "Well, uh, I tried to talk to her about Yuri."
    mc mb "See what she knows."
    s e1d b1d mb "Old school interrogation, huh?"
    show sayori ma
    mc ec mj bi "Sayori..."
    show sayori e3d b1a mn
    "Sayori just widens her smile."
    s e1a mh "What?"
    s lup b1d e1d mb "Have you ever seen me {b}not{/b} make a joke about something~?"
    show sayori ma
    mc ef ml ba "... Fair."
    show sayori ldown e1a b1a md
    mc bi mf "And I didn't get any answer, because I may have escalated things."
    s mg "Melly, what did you do?"
    show sayori md
    mc ea ba mg "To be completely fair to me, she...!"
    mc ef bi ml "She..."
    "I pathetically whisper under my breath."
    show sayori b2b
    mc mf "{size=-5}She started it.{/size}"
    s mg "Melly..."
    show sayori md b1a
    mc eb bd mg "She threatened me, Sayori! She was acting like any second she'd lay me out on the ground."
    mc ef mm bi "And she kept talking to me like I was some criminal..."
    s mg lup "Mel..."
    s mb b2a "That's just how she is."
    show sayori ma
    mc ml nb ea bd "Even with you?"
    s e2a mh "Well, I don't do anything to make her mad, but if I did..."
    s me b1b "..."
    s e3c b2b mb ldown "You really shouldn't take it so personally."
    show sayori ma
    mc ef bi mh na "..."
    show sayori e1a
    mc eg mm "I don't get it."
    show sayori md
    mc ef mg "If that's just how she is, then why should I be expected to deal with her at all?"
    mc ea bd ml "You can't ask a tiger to change its stripes."
    $ autofocus.block("sayori")
    s e2a b2a "..."
    mc ef bi mh "..."
    show sayori e1a b1a
    mc ba ml "But... It's not like she did anything that actually hurt me, so..."
    mc eg mb bi "Maybe I'm just overreacting."
    $ autofocus.unblock("sayori")
    s mb b2b "Don't be like that. You're entitled to how you feel."
    show sayori ma 
    mc ef mf "But she's your friend and well..."
    mc ea bg mb "I wouldn't dare go against your judgement of character."
    s e2a mb "Ehe..."
    show sayori ma
    mc ef ba ml "That aside..."
    mc ea mb "Should we go read something?"
    s mb e1a b1a "Hmm? Sure! What did you have in mind?"
    show sayori ma
    call close_eyes(1.0) from _call_close_eyes_24 
    "As we start reading together..."
    _mc ec ma "It starts to feel just like old times."
    _mc eg "Sayori and I, just doing whatever friends do."
    _mc mh "It all felt so simple back then, yet now..."
    hide sayori
    $ advance_date(minutes=17)
    "The longer Yuri and Natsuki are away, the more concerned I become."
    show natsuki turned lhip cut_b e2a md at i11
    "Till suddenly, Natsuki walks in-"
    call open_eyes(0.3) from _call_open_eyes_16 
    stop music fadeout 3.0
    "-Blood dripping like a leaky faucet from an open gash upon her cheek."
    show natsuki at thide
    hide natsuki
    show monika turned nb mc at t21
    show sayori turned me at t22
    "It isn't long until Sayori and Monika also took notice."
    show natsuki turned cut_b lhip e2a md at t31
    show monika rhip md at t32
    show sayori at t33
    m "Natsuki?!"
    m bb "Are you okay?"
    show monika mc rdown
    n e1a ldown mh "I'm fine. Yuri went home early today."
    show natsuki e3c md at thide
    hide natsuki
    show monika at t21
    show sayori lup b2b at t22
    "She quickly moves towards her seat and packs up her book."
    s mh "Natsuki, you- Your cheek-"
    show sayori me at thide
    show monika at thide

    play music pensive

    n turned cut_b e2a mh "I am well aware."
    hide sayori
    hide monika
    show natsuki md at t11
    "I walk over as well, not saying a word."
    mc bg ml ea nb "What even happened?"
    show natsuki b1d e1a me with None
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "She glances towards me, almost as if she were about to bite."
    "I can see, however, that from the way her eyes seem to almost dance around looking me in the eye that she isn't mad at me."
    show natsuki e2a with say_dissolve
    "..."
    "She's mad at something else, distant. Elusive."
    $ autofocus.block("natsuki")
    show natsuki mg with say_dissolve
    n "Bye."
    show natsuki md with None
    hide natsuki
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    "Without any of us being able to say another word-"
    "-She leaves."
    mc mf bf "... What...?"
    show monika turned mc at t21
    show sayori turned b2c mb at t22
    s "I'll- I'll follow her."
    show sayori e2a md at lhide zorder 1
    hide sayori
    show monika at t11
    "As Sayori leaves the room, I am left alone with Monika again."
    $ autofocus.block("monika")
    m eb "..."
    show monika bc ec rhip at dip
    "Monika brings one hand to her face as she slumps loosely onto the desk in front of her."
    $ autofocus.unblock("monika")
    m md "{size=-5}Shit...{/size}"
    show monika mc with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    "I turn to face her, but even as she'd spoken, no hint of the distress she's obviously feeling shows anywhere on her features. A perfect mask."
    mc mg ba na "Monika?"
    show monika ea with say_dissolve 
    $ autofocus.block("monika")
    "Monika looks at me, seemingly almost surprised I'd noticed anything at all."
    m rdown ec ba md "Sorry. Ignore I said that."
    show monika ea mc with say_dissolve
    mc bd ml "Why should I ignore that?"
    show monika nb with say_dissolve
    mc ec bi mg "There's clearly something going on here, and nobody is telling me about it!"
    m eb md bb "It's... It's not that simple."
    show monika mc with say_dissolve
    mc ef ml "Yeah, I'm sure it isn't."
    mc eg bb mg "Two dramatic walk outs back to back..."
    mc bi mb "I mean, it can't be {i}that{/i} big of a deal, can it?"
    m ea "..."
    "As Monika stays silent, I decide I have enough."
    hide monika 
    camera master
    show bg:    
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("monika")
    $ say_transition = False
    "I go back to my spot and pack up my things."
    "Just as I make my way out, Monika calls out to me."
    show monika turned md bb nb at t11
    m "MC-"
    show monika mc 
    mc ea bd mg "What?"
    m eb "..."
    m md "I'm sorry."
    show monika mc
    mc ef mf bi "Sure."
    "I leave, deciding to just go home for the day."

    stop music fadeout 2.0
    scene bg residential_afternoon with longfade
    $ advance_date(minutes=24)

    _mc turned eg bi mh "Maybe I reacted a bit harshly towards Monika."
    _mc ef ba "I'm sure she's trying to protect everyone."
    _mc bi "But, it just frustrates me. So, so much..."
    _mc ea ba "I know, I haven't known Yuri that long yet."
    _mc ec "But..."
    _mc eg bi "How can I even think of being a friend if I don't know what's going on?"
    _mc ea ba thinking "Should I text Sayori about it?"
    _mc ec bi "No. Judging from before, I doubt she knows what I'm looking for."
    "..."
    _mc ldown mm eg "Ugh..."
    _mc ec ba mh "Yuri..."
    _mc ef "I think I need some alone time."
    _mc bi "Some time to think about where to go from here."

    show white_flashback
    show cg yuri 2 turn
    with Dissolve(0.3)

    _mc ea bg "..."

    $ add_calendar_description(calendar_descriptions["yuri"][5])

    call week_2_tuesday_yuri from _call_week_2_tuesday_yuri 
    return