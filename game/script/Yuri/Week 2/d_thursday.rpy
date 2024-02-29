label week_2_thursday_yuri:
    call calendar_transition(day=2, hour=15, minute=23) from _call_calendar_transition_44
    scene bg club_gray with dissolve_scene_full
    play music okev

    _mc turned "Another day in the Literature Club."
    _mc ec mh "Outside seems to be the perfect weather-"
    _mc ea ma "-The perfect weather to talk to Yuri some more."
    show bg:
        align (0.0, 0.8) zoom 1.9
    show yuri turned lup md b1d e2a:
        i42
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
    with Dissolve(0.2)
    "As I've learned is somewhat usual, a Yuri that is reading seems to pay no attention to the world outside of her book."
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("yuri")
    mc mb nb "H- Hey Yuri!"
    y me "Hmm?"
    "Yuri looks up from her book, not saying a word."
    show yuri md with say_dissolve
    mc mg na "How do you feel?"
    y ldown e1a "..."
    "She stares at me blankly."
    stop music fadeout 3.0
    mc ml "... Yuri...?"
    "I feel a hand grab my shoulder."
    "A cold hand."
    "It's enough to freeze my shoulder."
    camera master
    show bg:
        blur 0.0 zoom 1.0
    hide yuri
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("yuri")
    "As I turn around, I can see what I can only describe as..."
    show natsuki turned me b1d cut_b:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    play music jm
    "Natsuki, but with blood on her face, holding a knife."
    mc mf na "N- Natsuki?"
    mc bg "W- What are you?!--"
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    show natsuki e1b mm
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("natsuki")
    "She puts her bloody hand on my mouth."
    n me "Be... quiet."
    n mg e1d "Yuri doesn't want to talk to you right now."
    n e1a mh "Have you kept her safe?"
    n e1b mm "Have you {i}helped{/i} her?"
    "I try to give a response, but not even a mumble comes out."
    n cross e1a mh b3a "If I find her sad ever again..."
    n b1d mg "It's on you."
    n e1d mm "And you..."
    n turned e1a mh "Will get this beautiful knife."
    n mg b3a e1b "Got me?"
    show natsuki mj with say_dissolve
    "I nod nervously."
    show black
    camera master
    show bg:
        blur 0.0
    hide natsuki
    play sound fall
    $ say_transition = False
    $ autofocus.unblock("natsuki")
    "Natsuki pushes me towards the wall, causing me to fall down to the ground."
    hide black with NonBlockingDissolve(1.0)
    "And as I look up again, she's gone."
    _mc eb mh "What is..."
    _mc bg "What is going on?"
    show yuri turned b1d md:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    "Yuri lifts up from her seat, before standing right in front of me."
    y mg "I want you to go."
    show yuri mj
    mc "What do you-"
    y mg "Leave."
    y lup rup mh b1a e1b "You wanted to leave the Literature Club, right?"
    y e1d b3d mi "Do it."
    y rdown e3c mg b1d "Your nosy nature is only causing me pain."
    y mm "... So, {i}so much{/i} pain."
    y ldown e1a mg "I don't want to see you."
    show yuri mj
    camera master:
        blur 0.0 matrixcolor BrightnessMatrix(0.0)
        linear 10.0 blur 2.0 matrixcolor BrightnessMatrix(-0.1)
    mc mf bf "Y- Yuri, please!"
    y e2a me "It's too late."
    y e1a mg "For you, and for me."
    y e3c me "Goodbye."
    show bg mc_bedroom_night_closed_off:
        align (1.0, 1.0) zoom 2.0
    camera master:
        matrixcolor None
        ease 2.0 blur 0.0
    hide yuri
    $ set_date(hour=4, minute=23)
    $ set_internet(True)
    stop music 
    play sound_loop heartbeat
    mc nostrands naked messy nb mg be "A- Ah!!!"
    stop sound_loop fadeout 5.0
    show bg:
        ease 0.15 zoom 1.0
    "I jolt upwards, a hand instantly brought to my face."
    _mc bf mh "It... It was just a dream?"
    _mc bg eg "Thank god..."
    camera master:
        linear 5.0 blur 1.0
    "As my racing heart steadies, a headache starts settling in, and with it, any chances of getting any more sleep."
    _mc ec bi "God... dammit..."
    
    scene bg mc_kitchen_day with Dissolve(1.0)

    "I stand up, and head to the kitchen to get something to drink."
    _mc turned messy naked nostrands mh "Where did that come from?"
    _mc ef "I don't normally dream..."
    "I clean my face using the kitchen sink, and after drinking a glass of water, I head back to the bedroom."

    scene bg mc_living_room with wipeleft
    stop sound_loop
    play sound widenekoflap volume 0.2 # I love this sound name - Victoria

    "Before I'm able to, however, a sound from outside draws my attention."
    camera master:
        ease 1.0 blur 0.0
    mc turned messy naked nostrands mf thinking "Is that... a cat?"
    "Raising an eyebrow, I open the curtains."
    show bg residential_night as stuff:
        align (0.5, 1.0) zoom 3.0
    show widenekoflap mc:
        align (0.5, 1.0) zoom 0.7
        matrixcolor TintMatrix("#352d63")
    with NonBlockingTransition(wipeleft)
    play ambient ext_night fadein 1.5
    "Waiting for me just behind the glass, I see the same small black cat from yesterday."
    mc ml "Oh, hello..."
    mc mb ldown "Did you follow me?"
    show widenekoflap ma with say_dissolve
    "The cat cleans itself in front of the window."
    mc ef bg ml "Can't let you in... Sorry about that."
    mc bi mf "I don't have any cat food and... yeah."
    mc ea ml ba "Maybe meet me..."
    mc mb "Meet {i}us{/i} again when I return from school?"
    mc mg "You know? The purple haired girl and me?"
    mc eg mb "The girl who holds infinite secrets?"
    _mc ec bi ma "What am I doing... The cat doesn't understand me."
    "I sigh."
    _mc mh ec "Really wish I had someone to talk to right now."
    _mc ef "..."
    _mc ba "Soon, Mel. Soon."
    stop ambient fadeout 2.0
    hide stuff
    hide widenekoflap
    with wiperight
    "Closing the curtains, I return to bed."
    
    scene black with Dissolve(1.5)
    pause 2.0
    call close_eyes(0.0) from _call_close_eyes_26
    hide black
    $ set_date(hour=15, minute=23)
    $ set_internet(False)
    show sayori turned lup at i11
    show bg club_day 

    who "Melly?"
    who "Melly...~?"
    who "Mel!"
    mc turned bun nostrands mj ec bi "H- Huh?"
    call open_eyes(0.0) from _call_open_eyes_18
    camera master:
        align (0.5, 0.2) zoom 1.5 blur 0.0
    show bg:
        blur 2.0 
    with Dissolve(0.3)
    play music a_sunshine
    $ say_transition = True
    $ autofocus.block("sayori")
    "I look around, and see the face of my childhood friend Sayori."
    s ldown e1d b1d mh "You were dozing off!"
    show sayori md with say_dissolve
    mc ml ba ea nb "I.. I was?"
    mc ef bi mf "Um. I..."
    show sayori e1a b1a with say_dissolve
    mc mg ba na "Didn't sleep that well last night."
    s mg "Huh? Why's that?"
    show sayori me with say_dissolve
    mc bi mf "Bad dream."
    mc ea mb ba "But, don't worry about me-"
    s md "..."
    s lup b4 mh "What are you talking about Melly?!"
    s b1d ldown mi "Bad dreams are bad!"
    show sayori md with say_dissolve
    "Sayori pouts at me."
    mc mg bd "Um. Thanks for the reminder."
    hide sayori
    camera master
    show bg:
        blur 0.0 align (0.0, 0.8) zoom 1.9
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    "I look around."
    mc mg thinking ba "Yuri's still not here?"
    show bg:
        zoom 1.0
    show sayori turned md at i11
    with Dissolve(0.2)
    s lup mh "Seems like it, why?"
    s mb e1d b1d "Waiting for her~?"
    s mh ldown e1a b1a "I noticed you two walking home together yesterday."
    show sayori ma
    mc mj ec bi ldown "I'm trying to get to know her better, that's all."
    s e3c mi "Suuure."
    s mh e1a "Well, maybe she's just a bit late?"
    s lup rup e3d mb "Everyone gets late sometimes!"
    show sayori ma
    mc ml bd ea "Sayori..."
    s ldown rdown me e1a "Hmm?"
    show sayori md
    mc mg ba "I only remember {i}you{/i} being late these two weeks."
    s e1b ml "W- Wha-"
    s tap eb "Th- That's beside the point!"
    mc ed md "Suuure~"
    phone discussion "mc_y"
    "I check my phone. No message from Yuri either."
    phone end discussion
    mc ec ml "Alright... Well..."
    show sayori ea
    mc ea mg thinking "Any plans for today, Sayori?"
    s turned lup b1d e3c mh "None."
    s e2a b1a mb "Well, except going home and... playing video games maybe?"
    show sayori ldown ma
    mc eg bi mb ldown "Big surprise."
    s mh b1d e1a "As if you never play games!"
    show sayori md
    mc ed md ba "See- {i}I{/i} spend my time studying. You know, for my {i}grades{/i}~?"
    s e1b rup mi "{i}I{/i} study!"
    show sayori md
    mc bm ml ed "When?"
    s rdown e2a b2a mb "... When I feel like it."
    show sayori ma
    mc ec mj ba "Uh-huh."
    mc eg mg "And you'll get into Tokyo real quick with that attitude."
    s lup e3d mn b1a "I will! The final exams are the ones that matter, and I'll have your help~!"
    _mc ea bd mh "This girl - Does she seriously think I'll have time next term to help her get her grades up? I'm going to have my hands full just getting my own grades-"
    _mc eb "- {b}my{/b} grades - up! When I'm competing with Natsuki and Monika, not to mention Chiaki, how am I supposed to stand out? If I want a scolarship..."
    play sound_loop running_int fadein 2.0
    $ renpy.music.set_volume(0.3, 2.0)
    show sayori ldown me e1a
    "!!"
    "My attention is drawn, as is Sayori's, far from our conversation."
    show natsuki turned md at t22
    show sayori at t21
    "Footsteps can be heard from outside of the classroom, and most of us are already assembled."
    _mc mf ea ba nb "Is that..."
    show yuri turned me e1b nb lup at t31
    show natsuki at t33
    show sayori at t32
    stop sound_loop
    $ renpy.music.set_volume(1.0, 1.0)
    "As the door swings wide open, Yuri walks in and heads directly to me."
    y b2b e1d mk "MC, t- take this!"
    show yuri ma with None
    show yuri rup at i11
    hide monika
    hide natsuki
    hide sayori
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "She hands me one of those pin-on badges, though she almost drops it in the process in the middle of all her fumbling."
    _mc mh "A... cat badge?"
    _mc ec ma na "A black cat. Of course."
    y mb "I want to... thank you."
    show yuri ma with say_dissolve
    mc mf ea "Huh? For what?"
    y e2a mb "Walking home together. It was fun."
    show yuri ma with say_dissolve
    "I raise my eyebrow."
    _mc ec mh ba "All I remember is her cliffhanger..."
    show yuri ma with None
    show yuri md ldown e2a b1a na at i21
    show sayori turned at i22
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    s mb "Nice to see you Yuri!"
    s mh "How are things going?"
    show sayori ma
    $ autofocus.unblock("yuri")
    y mg b1d "Well. I think."
    show yuri md with None
    show yuri e1a
    hide sayori  
    show bg:
        blur 2.0
    camera master:
        align (0.25, 0.1) zoom 1.5 
    with Dissolve(0.2)
    "I look into her eyes. It's almost as if I see a blank stare."
    "It sends chills down my side."
    _mc ef ma "Seems like dreams do stay with you for a while..."
    _mc bi mh "... I am glad dreams are just dreams."
    _mc ea ba "Yet... It does make me wonder-"
    show natsuki turned me at i32
    show sayori turned at i33
    show yuri e2a at i31
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    "The world stops me from daydreaming, as Natsuki enters my field of vision."
    n mg "A cat badge?"
    show yuri e1a b1a
    n cross b3a mh "What's that for?"
    show natsuki md
    y lup e1d mh b4 "To... symbolise our friendship...?"
    y e2a b1a mb "And... we saw a cat yesterday, so..."
    show yuri ma
    n e2a mg "I see."
    n turned e3c mi "Well. Enjoy, whatev."
    show natsuki md with None
    hide yuri
    hide sayori
    show natsuki e1a me b1d
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "Before walking away, Natsuki eyes me, wordlessly implying that I should be careful."
    _mc ea mh ba na "Same to you, Natsuki."
    hide natsuki
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    show yuri turned lup e2a mb at t11
    y "L- Let's continue reading {i}Something Wicked This Way Comes{/i}, MC...?"
    show yuri ma
    mc mb "Sure thing."
    show black with NonBlockingDissolve(2.0)
    "As we start reading, I can't help but think about Monday."
    "It's been so long... Yet I still don't know... What really happened."
    "Maybe it's time to ask, before it's too late."
    "I speak to Yuri with a whisper." 
    mc mf "Yuri?"
    hide black
    show yuri e1d md b1a ldown at i42
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0 align (0.0, 0.8) zoom 1.9 
    with NonBlockingDissolve(0.5)
    "Yuri turns her head to face me."
    $ autofocus.block("yuri")
    $ say_transition = True
    y me "?..."
    mc bg ml "Can we talk about Monday?"
    show yuri b2a nb e1b md with say_dissolve
    "Yuri stares at me blankly, before her expression turns into fear."
    y e2b me "!..."
    camera master
    show bg:
        blur 0.0
    show yuri lup rup 
    with Dissolve(0.2)
    $ say_transition = False
    mc bb mg nb "Yuri, please. I want-"
    show yuri e1b b2b md
    "Yuri tries to stand up, before I grab her hand."
    mc ml ef bg "Sorry. Let's...talk about it another day."
    $ autofocus.unblock("yuri")
    y e3c me "M-mhm."
    show yuri e2a ldown rdown b1d md at dip
    "She sits back down again."
    _mc ec ba na mh "Once again without answers..."
    _mc ef "It seems like a sensitive topic to Yuri."
    _mc ea thinking "What the hell could've happened?"
    _mc ec "Hmm..."
    _mc bi "I think only one other person knows the answers..."
    _mc ldown eg "And even if I don't like it, it's either that or just quitting out right and ridding my hands of this whole thing."
    _mc ef "And I..."
    _mc eg mm "God help me, but I don't think I want to do that."
    
    stop music fadeout 2.0
    scene bg club_day:
        align (0.0, 0.8) zoom 1.9 blur 2.0
    camera master:
        align (0.5, 0.1) zoom 1.5
    show yuri turned e1d md at i42
    with fade
    $ advance_date(minutes=20)

    "The rest of the club day went as usual. That is... until Monika barges in."
    camera master
    show bg:
        zoom 1.0 blur 0.0
    hide yuri
    with Dissolve(0.2)
    show monika turned mb rhip ed nb at t11

    play music okev

    m "Hello everyone!"
    m ea rdown bb "Excuse me for being late, I had to talk to a teacher."
    show monika ma at t21
    show sayori turned lup rup ml e1b at t22
    "Sayori gasps."
    s mi b1d "Monika being in trouble with a teacher?!"
    s ldown rdown xd b2b mk nb "We're doomed!"
    show sayori me at t43
    show natsuki turned at t44
    show yuri turned at t41
    show monika na ed ba at t42
    "Monika chuckles a little."
    show sayori md e1a b1a na
    m lpoint md ea "Of course not, I just wanted more information about the festival."
    show monika mc
    mc turned bun nostrands mg thinking "Like, who's coming and who's not?"
    m rhip mb ldown "That, among other things."
    show monika ma rdown
    s mb lup "Tell us tell us!"
    show sayori ma
    m rhip md "People, all sorts of people will come and visit us."
    m eb bc "Not just to see what we do..."
    show yuri md e1d
    m ea mb ba "But to experience it themselves!"
    m rdown md "Take for example our poems."
    m lpoint mb "We could let them listen to them."
    show monika ma
    show natsuki md
    y mg lup "Um... M- Monika..."
    show yuri me
    m md ldown "Hmm?"
    show monika mc
    y mb e2a b1d "Are you... sure?"
    show yuri ma
    m md "Well... It could be the best way to draw new people in."
    m mb "Besides, we could maybe suggest that they try writing a poem of their own."
    show monika ma
    n lhip mh "Do you have any other plans?"
    show natsuki mj
    m md "You mean, besides poems?"
    show yuri e1a ma b1a
    m rhip ec bc md "Well... We have a lot of books in our storage room."
    m eb "... Reading {i}is{/i} what this club is all about, anyways."
    show monika mc
    "..."
    show monika ea ba
    mc ml ldown "Alright. Do you want us to prepare anything for it?"
    m rdown mb "Not today, no."
    m md lpoint "But, tomorrow we'll work on changing this classroom a little."
    m mb ldown "That's fine with everyone?"
    show monika ma
    mc mb "Fine with me!"
    y rup mb "Y- Yeah."
    show yuri ma ldown rdown
    s mb "Yep!"
    show sayori ma
    n ldown e2a mh "Sure."
    show natsuki md
    m mb "I have nothing on schedule today, so... enjoy reading, everyone!"
    show monika ma at thide
    hide monika  
    show sayori at thide 
    hide sayori
    show natsuki at thide 
    hide natsuki 
    show yuri at thide 
    hide yuri 
    "As everyone goes back to reading, a familiar feeling appears."
    _mc ec mh "..."
    _mc thinking ea "Is now the time to ask Monika about Yuri?"
    camera master:
        zoom 1.4 align (0.0, 0.7)
        ease 7.0 align (1.0, 0.5)
    with NonBlockingDissolve(0.5)
    "I scan the room, trying to make a strategic analysis."
    _mc ec "No, taking Monika outside now would cause a stir among the others... I think."
    _mc ef "... Tommorow."
    _mc eg ldown "For now, I'll just read a book."
    
    scene black
    camera master
    with Dissolve(0.5)

    "As Yuri and I continue reading, it becomes clear that time starts losing its meaning."
    _mc turned bun nostrands eg "Being together with Yuri just feels so... nice."
    _mc ea mh "Maybe I should ask her..."
    _mc ec ma "What's really bothering her, when we walk home together again."
    stop music fadeout 3.0
    "Looking down at the badge she gave me, I can't help but smile."
    _mc eg "I hope you feel the same way about me, Yuri."

    scene bg school_lockers_afternoon
    show yuri turned e2a md:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    camera master
    with wipeleft_scene
    $ set_date(minute=34, hour=16)

    mc turned bun nostrands mb "Ready to go, Yuri?"
    y mb b1d "Y- Yeah!"
    show yuri lup ma
    "We grab all our things, put on and tie our shoes, and go on walking."
    show bg school_gate_afternoon
    show yuri b1a e1a md ldown:
        matrixcolor TintMatrix("#f1d6bb")
    with NonBlockingDissolve(0.5)
    "But as we come to the gates of the school, Yuri stops to look back."
    y e2a mg "Hey, MC..."
    show yuri md
    mc mf "Hmm?"
    y lup e1d mh "What do you think of this school...?"
    show yuri md
    mc ml "I think it's an alright school, why do you ask?"
    show yuri e2a
    "Yuri glances between me and the school building in question."
    "It is a rather tall building..."
    y mh "At times, I wonder what would've happened if I didn't go to this school."
    y e3c mg "It would obviously mean me not meeting the others, but..."
    y e1d mh ldown "What would that cause, in the long run?"
    show yuri md
    mc mb "Well, who says that you wouldn't be in a fun club in the other school?"
    y e2a b1d mg "I don't know..."
    y lup rup b1a e3c mh "There's something that tells me life would be miserable..."
    y b2b e2a mb "Without the Literature Club."
    show yuri ma
    mc ml bf "Yuri..."
    show yuri e1a
    mc ef bi mf "I think I know how you feel."
    mc ea ba mg "But, mind if we start walking before I explain?"
    y rdown e2a mb "Y- Yeah. Sure."
    show yuri ma

    scene black with wipeleft
    $ advance_date(minutes=4)
    play ambient ext_night fadein 1.0

    "As we start walking, it gets more and more obvious that it's Thursday."
    "People aren't hanging around near shops..."
    "The streets are quieter..."
    "I can't find a single thing that catches my eye on the streets."
    show bg school_street_afternoon
    hide black
    camera master:
        align (0.5, 0.1) zoom 1.5
    camera above_master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    show yuri turned e2a md onlayer above_master:
        matrixcolor TintMatrix("#ffeede")
        i11
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True

    stop ambient fadeout 2.0
    play music violetsolo 

    "Yet, Yuri seems to fill that void."
    "Although... The way she talks at times..."
    "Feels like she is carrying a void of her own."
    show yuri e1a with say_dissolve
    mc turned bun nostrands eg mg "Yuri, I think what you are feeling is the difficulty of imagining a different life."
    mc ef ml "And of course it's difficult."
    mc ea mg bd "We're not meant to be living a trillion different lives!"
    mc ba mb "But another truth is that we're all human. And humans are defined by their adaptability."
    mc eg "It doesn't matter what life you're living."
    mc ef mg "Or what friends you have."
    mc bi ml "Or how alone you are."
    mc ea mb ba "You would find something you cherish in that life and latch onto it."
    mc eg ml "And then you'll find yourself having difficulty imagining how you could be happy in any other way."
    mc ea mg "Not because there isn't any other way for you to be happy, but because it would only cause you more harm to know those myriad of other ways you could've found that joy."
    y e2a lup b1d mg "I see..."
    y e1d b1a mh "That point of view leave me very... hollow."
    show yuri md with say_dissolve
    mc ml thinking "You think so?"
    y e2a b1d mg "Yes."
    y ldown e3c mh "It breaks down everything you value into what amounts to a coping mechanism."
    y b1a mi "Each thing you admire being some kind of trope you would fill no matter the circumstances."
    y e2a mg "I don't think I like that."
    y mb "I love the club. Natsuki, Sayori, you..."
    y mg nb "... Monika..."
    y e3c mb na "And I think that experience is special."
    y e1a "Unique."
    y e1d mh "Unreplicable."
    y lup e1a mb "Don't you?"
    show yuri ma with say_dissolve
    mc ldown ef mh "..."
    mc ml "All of you are great, but..."
    mc mf "..."
    show yuri md with say_dissolve
    mc eg bi mb "Maybe that's just how I rationalize it."
    mc ef ml ba "It's easier that way."
    y mh ldown "Why?"
    show yuri md with say_dissolve
    mc mh "..."
    mc bi ml "I don't know."
    mc eh md bf nb "But, yeah, no need to dwell on it!"
    show yuri e1a ma with say_dissolve
    "Yuri gives me a nod, still looking my direction."
    mc ef mf bi "I wonder-"
    show yuri md with say_dissolve
    mc ea mg ba na "What do you think about the festival?"
    y me "..."
    "..."
    y b1d mg e2a "It... kind of scares me."
    y b2b e3c mb "Especially if we have to share poems..."
    show yuri ma with say_dissolve
    mc mb "Why? I read your poem and I liked it, remember?"
    y e1d b1a me "I-"
    stop music fadeout 0.1
    play sound heartbeat
    show black onlayer above_master with NonBlockingDissolve(0.1):
        alpha 0.5
    mc bf eb mh nb "...!"
    hide black
    # TODO car
    # show expression "#000" as car zorder 1:
        # xysize (42, 42) pos (0.563, 0.472)
    show bg:
        blur 0.0
    camera master:
        xoffset -50 blur 0.0
    camera above_master:
        xoffset -130 blur 2.0
    with say_dissolve
    "Just as Yuri attempts to open her mouth, I see a car flying down the residential street."
    show yuri mg
    camera above_master:
        blur 0.0
    camera master:
        blur 2.0
    # show expression "#000" as car:
        # zoom 1.5
    with say_dissolve
    y "Th-"
    show yuri me
    camera above_master:
        blur 2.0
    camera master:
        blur 0.0
    # show expression "#000" as car:
        # zoom 2.0
    with say_dissolve
    play sound heartbeat
    mc mg "Yuri! Watch out!"
    show yuri mg
    camera above_master:
        blur 0.0
    camera master:
        blur 2.0
    # show expression "#000" as car:
        # zoom 3.0
    with say_dissolve
    y "Huh?"
    show yuri me:
        xzoom -1
    camera above_master:
        blur 2.0 xoffset -140
    camera master:
        blur 0.0 xoffset -70
    # show expression "#000" as car:
        # zoom 4.0
    with say_dissolve
    play sound heartbeat
    "She turns her head, but I notice she won't be able to respond in time-"
    play sound carmonkaw
    window auto hide
    pause 1.0
    play sound2 ["<silence 1.0>", audio.heartbeat]
    scene white onlayer above_master with Dissolve(2.3, time_warp=_warper.easeout_quart)
    camera master
    camera above_master
    # hide car
    hide yuri
    pause 1.7
    play sound_loop heartbeat fadein 5.0
    hide white
    scene black
    with Dissolve(2.0)
    $ say_transition = False
    scene bg school_street_afternoon with NonBlockingDissolve(1.0)
    "I grab her by the arm and pull her off the road we were walking on."
    mc turned bun nostrands ml eg bg "Haaah..."
    mc bi mj "Jesus Christ..."
    stop sound_loop fadeout 3.0
    "I pause to catch my breath, my heart racing."
    mc ea bf mg "Yuri, are you okay?"
    "..."
    mc ml be "... Yuri?"
    show yuri turned b2a lup rup e1b nb me:
        matrixcolor TintMatrix("#ffeede")
        matrixtransform OffsetMatrix(0, 0, 0) # "lhide" uses xoffset
        parallel:
            t11
        parallel:
            linear 0.06 matrixtransform OffsetMatrix(-0.75, 0, 0)
            linear 0.06 matrixtransform OffsetMatrix(0.75, 0, 0)
            repeat
    
    play music wtdgi
    
    "I turn to look at Yuri, who stares at me trembling in fear."
    y "..."
    $ autofocus.unblock("yuri")
    y mg "No, no no no no..."
    y mk e2b "Why did- Am I-"
    y mm e1b nd "I..."
    mc bg mf "Y- Yuri?"
    "Yuri continues to tremble in place, mumbling over and over to herself."
    y e3c tears_a b2b "J- Just let me go..."
    y ldown rdown e2d notears mh "S- Somewhere else..."
    y e2b mg "... Somewhere safe..."
    show yuri md at lhide
    hide yuri
    "As Yuri starts walking in the direction of her home, straying away from our usual path-"
    show yuri turned b2b me nb lup rup e2b:
        matrixcolor TintMatrix("#ffeede") matrixtransform OffsetMatrix(0, 0, 0)
        i11
        block:
            linear 0.06 matrixtransform OffsetMatrix(-0.75, 0, 0)
            linear 0.06 matrixtransform OffsetMatrix(0.75, 0, 0)
            repeat
    show bg city_street_3_afternoon
    with NonBlockingTransition(wipeleft)
    "I follow behind her, and try to grab her arm again-"
    show yuri e1d b3d mm nd
    play sound fall
    camera master at vpunch
    "Before Yuri yanks her arm out of my grasp, gripping it tightly in her own."
    mc eb mg bg nb "Yuri?!"
    y mi e1c b1a "DON'T TALK TO ME!"
    show yuri mm
    mc mm bf eh "Y- You're hurting me, Yuri!"
    mc mj "I- I am just trying to help you!"
    mc bg mg ea "Please, calm down! You're safe!"
    y mi e1b "No I'm not! I'm not, I'm not..."
    y b2a mk e2b nb ldown rdown "I need to go home, I need to go home, I need to go home, I need to go home!"
    y e1c mi b2c lup rup "I NEED TO GO HOME!"
    show yuri mm with None
    show yuri e3a b2a nb ldown rdown:
        pass
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.1) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "As a last ditch effort, I turn her around and grab both her arms."
    show yuri mj e3d b2c with say_dissolve
    "She attempts to break free, but her panic makes her unable to coordinate herself."
    show yuri e2b mk b2a with say_dissolve
    mc eb bf mg nb "Yuri! Please, relax!"
    show yuri e2d with say_dissolve
    mc ea mb bg "You're safe, nothing will happen to you."
    mc eg "I promise you Yuri. You're okay!"
    show yuri e2b mm with say_dissolve
    mc ea ml "Please, understand..."
    y mh "Haah- I... I need to..."
    show yuri mk with say_dissolve
    mc mg "Let me help you, Yuri..."
    y b2b e1d mg "Y- You... I..."
    y me e3c "I don't want to..."
    show yuri mm e3c tears_a:
        zoom 0.78
    show bg:
        align (0.5, 0.0) zoom 1.1 blur 2.0
    with Dissolve(0.2)
    "As she slowly stops struggling, she falls to her knees, with me kneeling down to support her."
    show yuri e1a mj with say_dissolve
    "She then looks at me with tears in her eyes."
    y mg "I- I..."
    y e3c tears_b ml "I'm s- s... SORRY!"
    y mh "I... I-I can't c- control... control myself..."
    y mk "I'm so- ... so scared..."
    show yuri mm nd with say_dissolve
    mc eg mb "It's... It's okay."
    mc ml "I'm here for you..."
    show yuri lup rup mk with say_dissolve
    mc mf "Y- Yuri..."
    mc ea bf mb "Please..."
    camera master:
        zoom 1.6
    show yuri mm
    with Dissolve(0.2)
    "Unable to find the words, I hold her tight..."
    show black with NonBlockingDissolve(0.8)
    "And give her a hug."
    $ say_transition = False
    y mj e3c tears_a "..."
    y e1a me "..."
    $ advance_date(minutes=5)
    hide black
    show yuri md ldown rdown
    with NonBlockingDissolve(0.8)
    $ say_transition = True
    "The glossy vision in her eyes seems to pass, as she slowly glances up at me, this time not past me, as she'd been doing the entire time."
    y lup me "Th-"
    y md e3c notears na "..."
    y mg e1a nb "Thank you... MC."
    show yuri md with say_dissolve
    mc eg bg "No matter what happens, I'm here for you..."
    y e2a me "I..."
    y mg "I want to go home..."
    show yuri mj with say_dissolve
    mc na ef mb bf "Th... That's okay."
    camera master
    show bg:
        blur 0.0 zoom 1.0
    show yuri at i11
    with Dissolve(0.2)
    $ say_transition = False
    "I stop hugging her, and look her in the eyes."
    mc ea bg mb "Let's go."
    mc ea ml "Take it slow."
    mc ef mg bi "And... let's try to avoid roads for now."
    show yuri ldown e3c md
    "Yuri silently nods."
    "We decide to take a different route, one with less roads, or at least ones that also have sidewalks."
    
    scene bg city_street_2_afternoon
    show yuri turned lup e2a b1d md:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    with wipeleft_scene
    $ advance_date(minutes=15)

    "She's quiet."
    show yuri e2c
    "Always looking around her."
    show yuri e2a
    "I'm unsure if it's to look for dangers..."
    "Or something worse."
    "Either way..."
    _mc turned bun nostrands ec mh "Her silence tells me enough."
    show yuri e2c
    _mc ef "If she doesn't want to talk, then I won't make her. If she wants to be alone, I'll leave her be, as soon as I know she's safe."
    show yuri e2a
    _mc bi "I just... don't understand what caused her to panic like that."
    _mc eg "Almost being run over is scary, but..."
    _mc ea ba "It's not that bad. I've been in pretty similar situations a few times, and it's never really gotten to me like that."
    show yuri e2a
    _mc ec "Her eyes, too... She didn't seem to even see me, just..."
    _mc bi "... As if I weren't there at all."
    mc ea ba mf "Yuri...?"
    show yuri ldown e1a
    "She turns her head, staring at me with a blank expression."
    mc bf ml "What happened...?"
    mc ef mf "It was as if you..."
    y "..."
    y "..."
    y e2c "..."
    $ autofocus.unblock("yuri")
    y e2a mg "I don't want to talk about it."
    show yuri md
    mc ml "A- Alright. Just... know I'm worried about you."
    show yuri e3c
    "She nods silently."

    scene bg y_house_afternoon
    show yuri turned md e2a b1d:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with wipeleft_scene

    "What followed had been another five minutes of silence, before we finally reach her home."
    y e3c mg "S- Sorry, MC."
    show yuri e1a md
    mc turned bun nostrands mb bg "It's okay."
    y e2a me "I'm... going in now."
    y e2c mg "I'll... see you tomorrow."
    show yuri e1a md at thide
    "I give her a smile, trying to cheer her up."
    mc bf eh "See you tomorrow, Yuri."
    hide yuri
    "Entering her home, she doesn't return a smile. Her blank expression sticks to her face like glue."
    "She closes the door, and I realise just how quiet it truly is out here."
    mc ea bf ml "Please..."
    mc mf bg eg "Be safe... Yuri."

    $ add_calendar_description(calendar_descriptions["yuri"][8])

    call week_2_friday_yuri from _call_week_2_friday_yuri
    return