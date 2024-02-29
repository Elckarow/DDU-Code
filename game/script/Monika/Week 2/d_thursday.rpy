label week_2_thursday_monika:
    call calendar_transition(day=2, minute=0, hour=12) from _call_calendar_transition_9
    scene bg class_1_day with dissolve_scene_full
    $ set_internet(False)
    play sound school_bell

    _mc turned nostrands tail ec mh "... Finally."
    
    scene bg school_corridor_1_day with wipeleft
    play music rgb

    _mc turned nostrands tail bi eg mm "Geez, what’s gotten into me? This past week has been..."
    _mc ec mh ba "Just terrible."
    _mc "As soon as I realised how I felt about Monika, it’s been all downhill."
    _mc ef "... Maybe that’s just an omen of what’s to come, should I pursue her."
    _mc ma "Might be worth just... dropping it, altogether."
    show monika turned:
        i11
        flash
    _mc mh "... Monika."
    _mc eg "I... don’t know if I can do that."
    _mc "It’s been so long since I’ve felt this way, about anyone."
    _mc ea "... Am I..."
    _mc ec bi "Wait..."
    show amelia turned bh me ec at t11
    am "Yo, chuckstick. What’s cooking up in that brain of yours? Stalling the traffic, dude."
    show amelia ef ma bb
    mc ea ba ml "Huh? Oh, Amelia."
    show amelia eb ba
    mc ef mg "Don’t mind me, I’m just... thinking."
    am ea me "Yeah, I could smell it from my classroom."
    am eb bb mb "C’mon, walk with me."
    am rup ee "Grab your lunch, let’s eat on the roof."
    show amelia ma at thide
    "I shrug and follow her."
    hide amelia
    
    scene bg school_rooftop_day
    show amelia turned eb at i11
    with wipeleft

    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    am mb "So, what’s on your mind? Something’s gotta be turning those gears into overdrive."
    show amelia ma with say_dissolve
    mc turned nostrands tail ml "Yeah, well, I..."
    show amelia md with say_dissolve
    mc ef mg "It’s hard to really describe."
    am ec ba me "Look, it’s all over your face. You got dumped, or turned down, or whatever, right?"
    show amelia md with say_dissolve
    mc eb bb nb mg "Wh- What? No, don’t be-"
    am bh ee mb "... Do you think I’m stupid? C’mon, I’d know that trademark look of despair anywhere."
    am eb ba me "So? Who was it?"
    show amelia md with say_dissolve
    mc ef ba mh "..."
    am rup ee me "Don’t wanna tell me? That’s a real shame, ya know? I might be able to help fill the hole!"
    am eb bb mi rdown "Ah, wait-"
    "I let out a small snicker."
    am ec bh me "Aw, come on, you know what I meant."
    am bd eb lup mb "Man, I’m usually the one baiting everyone else, not myself..."
    show amelia eb ma ldown with say_dissolve
    mc ed ba md na "Please. We all know I’m the master baiter."
    show amelia bb with say_dissolve
    mc bb nd mh eb "!!"
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("amelia")
    $ say_transition = False
    am mb ef "Ahaha! I cannot {i}believe{/i} you fell for that!"
    show amelia at dip
    am "OH GOD!"
    am eb ba "So perfect!"
    show amelia ma
    mc mj eg bi nb "... C’mon, that was so cheap!"
    am mb ef "Cheap, but still works! Hah!"
    show amelia eb ma
    "I roll my eyes."
    _mc ef mh na "Man, what the hell. First I don’t have the energy for class, which is rare, and now I’m so slow I get baited by Amelia? What is going on with me today?"
    am me "But no, for real. What’s on your mind?"
    show amelia md
    mc ba "..."
    mc ml "I dunno, I’ve been thinking lately."
    mc ea mg "... Did I ever tell you about what life was like before I met you?"
    am ea mb bh "Cold, dark and irritating? Oh, and super edgy?"
    show amelia ma
    mc ec ma "..."
    show amelia ba md
    mc ef ml "I meant before all that. Before things went all... well, wrong."
    "I sigh."
    mc eg mg "It’s... I had a friend once. A friend I valued over absolutely everything."
    show amelia bd ec ma
    mc ec ml "And I... Well. Let’s just say I messed it up."
    am ed mb be lup "Ah. I get you. Sometimes all it takes is saying one wrong word, and it all comes... tumbling down."
    show amelia ma
    mc ef mb bg "Yeah."
    am ldown eb ba me "Wait, you’re not..."
    show amelia bh md ea with None
    camera master:
        align (0.5, 0.15) zoom 2.0
    show bg:
        blur 2.5
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    "She stands up, frowning, as she moves over right next to me, pushing right into my personal space as she eyes me closely."
    am mh "You’re not saying what I think you’re saying, right?"
    am eb ba me "Sayori, right?"
    show amelia md with say_dissolve
    mc ba ml "Yeah."
    am me "You’ve mentioned her a couple times. An old friend, right?"
    am mb bd "But it’s more than that, isn’t it? You..."
    show amelia ma with say_dissolve
    mc mg "... I did, once."
    am ed mb "I get it."
    show amelia ee mg ba with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She leans back, thinking to herself for a moment."
    $ autofocus.unblock("amelia")
    am me "I suppose I’ve never really thought about it like that, huh?"
    am bd mb ea "You’re worried though, aren’t you?"
    am lup me ed lup ba "About what people might think."
    show amelia md
    mc eg mj "... Maybe."
    am ldown eb mb "Because now, it’s someone new, and one thing hasn’t changed;"
    extend ea ba me " it’s a girl."
    show amelia md
    "I nod."
    show amelia bd ee rup ma at dip
    "I expect her to laugh, or make fun of me, or something, like she usually does, but now, she just places a hand on my shoulder."
    am ed mb "I... I suppose that’s something you’ll have to come to terms with. I’m sorry, I can’t really relate, but..."
    am eb bb me "For me, I just don’t quite get 'love' in general."
    am mh ec ba rdown "It seems like such a waste of time and effort."
    show amelia eb ma
    mc ec mh "..."
    mc ea ml "Maybe it is, yeah."
    show amelia ef
    mc mg "Maybe it’s not worth the time to worry so much over."
    am eb bb me "There ya go. Best to push away those sentimental thoughts and get some real brain cells pumping."
    am ec bh mb "Just like you’re used to, bring back the old, grumpy Melody."
    show amelia ma
    "I roll my eyes."
    mc ed md "I could punch you."
    am lup ee bi mb "You could, but there’s no telling if I’d be into that."
    show amelia ma
    "I sigh. It’s impossible to win with her, sometimes."
    "Though, maybe that’s just a sign that I have room to improve."
    _mc ec ma "Sometimes, I’m glad she’s around."
    _mc ea "It makes my life a little more bearable."
    
    stop music fadeout 2.0
    scene bg club_day with longfade
    $ set_date(hour=15, minute=35)

    _mc turned nostrands tail eg "Well, here we are. Time to pretend everything is alright."
    show sayori turned lup rup mb e3d at t11
    s "Heeey, Melody’s here!"
    show sayori e1a me
    mc ea ml "Yeah, here I am..."
    show sayori ldown rdown b1d e1d md at t32
    show natsuki cross b1d e1d mj at t33
    show monika turned mc bc at t31
    "Sayori, and just about everyone else in the room, frowns."
    n mh "C’mon dude, don’t just sour the mood like that."
    show natsuki mj
    show monika ba
    show sayori e1a b1a me
    mc ea mf "S- Sorry, I just..."
    _mc ec mh "Nothing gets by her. Even if I’d managed to act normal, she’d have known."
    mc ea mg "Where’s Yuri?"
    show natsuki e1a b3a md
    m mb "Actually, I managed to talk to her yesterday. I think we’re all on the same page again, at last."
    show monika mc
    show sayori ma
    mc bb ml "Oh, really?"
    show sayori md
    m rhip eb md "... Well, mostly. Actually, MC, could I... could I speak to you, alone, for a moment?"
    show monika mc at thide
    "I nod, and we make our way over to the closet."
    show natsuki at thide
    show sayori at thide
    hide sayori
    hide natsuki
    hide monika
    
    scene bg club_closet_day
    show monika turned eb mc at i11
    with wipeleft
    play music ["<silence 0.2>", audio.myconfession]

    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    m md ea "Hey, look, I just... I wanted to talk about the message I sent you the other day. Apparently Yuri got the wrong impression the other day about what happened over the weekend, and that’s why she was so defensive about it."
    show monika mc with say_dissolve
    mc turned nostrands tail mf "Ah. I..."
    _mc ec mh "I knew that was why, but there’s no way I would say that out loud."
    m bc ec md rhip "What I don’t understand is where she got that impression from."
    m ba ea mb "I was hoping you’d be able to clarify. Is there anyone who might have seen us and gossiped about it?"
    m rdown eb md "I don’t even know how anyone found out... This is a nightmare..."
    show monika mc bc ec with say_dissolve
    "She brings her hand to her temple, sighing despondently."
    m lpoint ea ba md "It’s bad enough that the entire club now knows, but if they do, that means the gossip must have spread to half the school by now."
    m bb eb "Our reputations would be in shambles... and it’s all my fault."
    show monika mc ldown with say_dissolve
    "She bites her lip."
    m ec md "I’m sorry. I never intended for any of this to happen."
    m mb eb "If I’d never invited you out, under such vague terms, or if we’d picked something else to do, maybe we could have avoided this."
    show monika ea mc ba with say_dissolve
    mc bg ml nb "N- No, Monika, I’m... I’m sorry."
    m md "Hm?"
    m md "Whatever for-"
    m bc rhip "Ah. You told them, didn’t you?"
    show monika mc with say_dissolve
    mc ef mh "..."
    m ec md "At least, if we’re lucky, that confines it to the club members..."
    show monika rdown mc with say_dissolve
    "She clicks her tongue, sighing once again."
    m eb md "If only I’d managed this a little better..."
    show monika mc ba with say_dissolve
    mc ea bf mb "Also... It’s not your fault. It’s mine."
    show monika ea with say_dissolve
    mc mg bg eg "I was the one who told them, yes, and also the one that gave them the wrong impression. I’m... sorry."
    mc ef mb "But I was also the one who invited you out. It was my fault, and my misinterpretation of what that meant."
    m md "... I..."
    m ec bc "I see."
    m eb rhip "So you..."
    show monika ea ba mc with say_dissolve
    mc be eb nc mg "I, ah, panicked a little. I wasn’t sure what you thought it was..."
    m eb nb mb rdown bb "O- Oh, right, yes, of course. You wouldn’t- No, that would be silly!"
    show monika ma with say_dissolve
    mc bf eh md nb "Haha, no, not at all! Crazy!"
    "Monika awkwardly shuffles on her feet."
    _mc ec ma ba na "Yeah, I don’t think either of us are fooled."
    _mc ea "But it’s probably better than the alternative, at least for now."
    
    scene bg city_street_afternoon
    show yuri turned lup b2b e2a:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    camera master
    with monika_pov(True)
    $ autofocus.unblock("monika")
    $ set_pov("m")

    _m turned bb ec nb mc "How..."
    _m ea "What do I do?"
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    _m bc na "Ah, never mind that; I have more important things on my mind."
    y e1a mg "Monika, I..."
    show yuri md with say_dissolve
    m ec md ba "No, I know. This is my fault."
    y rup mb "... Thank you."
    y e3c mg "You’ve no idea how much it means to me that you’d show me the time of day after what I put you through."
    show yuri md with say_dissolve
    m eb mb bb "I wish we could have handled it better, and not..."
    y shy ea bb mb "I know I apologised yesterday, but I still... feel awful for making you doubt your abilities as president."
    y eb ba ma "I know how much that means to you."
    "I bite my lip."
    m md "I..."
    _m ea bc mc "... Still can’t believe she’d abuse something like that, to hurt me."
    y bb ee mb "I’m sorry, I just... I have no excuse."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I stop in my tracks. Why did she do any of this?"
    show yuri turned lup rdown e1d b1a md
    "Yuri notices, turning to face me."
    $ autofocus.unblock("yuri")
    y mg "What is it?"
    show yuri me
    m eb md "Why were you so concerned about what happens in my life?"
    y b2b mk e2a nb "I..."
    _m bb nb ea mc "Oh, no, nonono."
    y e3c mh "It’s nothing nefarious, I swear to you. I was just... concerned."
    y ldown e1a mb na "Monika, you’re my best friend. I would be horrified if something hurt your reputation, or worse, hurt you."
    show yuri ma
    "I sigh. It sounds so much like her."
    _m ec ma ba na "She’s a good friend of mine, after all. Of course she’d want to test out anyone who might be wanting to get close to me."
    _m mc ea "But was it really the right way to go about it?"
    m md "I just think... Maybe there was a better way to go about it."
    y shy bb ea ma nc "... I’ll admit what I did was rash. You have every right to be upset with me for that."
    show yuri mb
    "Her face disappears behind her bangs. A nervous tick, for her."
    y ba ma "It just..."
    y ee bb mb "I don’t know what I was thinking."
    m bc md "Because if you ask me, it felt like what you did would have hurt me more than anyone else."
    m bb mb "It just... wasn’t like you, Yuri. You always think things through."
    m md ba "Why would you even conceive an idea that throws me under the bus, unless it was directed at me?"
    show yuri eb ma
    m bc "... Unless you were willing to do just that?"
    show yuri mb ne
    "Yuri’s face vanishes in shame."
    y md "Monika, I-"
    show yuri mb
    "I nod, letting her find the words."
    y nd ea ma "... I don’t know. I didn’t do it for anyone or anything in particular, it just... happened."
    m ba "So you really didn’t mean to hurt me?"
    y turned lup rup e1b nb mk "N- No, of course I didn’t..."
    show yuri md
    m ec bb mb "... I’m sorry I doubted you, Yuri."
    show yuri e1d
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "I smile, bringing her in for a hug."
    show yuri b1a nc e3c ma with say_dissolve
    "She loosens up, wrapping her arms around me tightly."
    y mb "Th- Thank you..."
    show yuri ma with say_dissolve
    m ba "It’s alright, Yuri. You’re incredibly special to me."
    m "I’m happy you’re around."
    y mb "G- Glad to be of service..."
    show yuri ma
    show black:
        alpha 0.75
    with NonBlockingDissolve(0.2)
    _m ma "Her hair is so soft and silken. I could never get my hair like that, no matter how hard I try."
    _m "It’s fluffy, like running my fingers through a cloud."
    _m "I’d ask her what her secret is, but... I don’t want to ruin the moment."
    _m ea "I’ll text her tonight about it, I think."
    _m ec "She’s too good to me, sometimes, I swear."

    stop music fadeout 2.0    
    scene bg city_street_3_night_off
    camera master
    with mc_pov(True)
    $ autofocus.unblock("yuri")
    $ say_transition = False
    $ set_date(hour=21, minute=40)
    $ set_pov("mc")

    play music a_sunshine

    _mc turned nostrands tail mh ec "What a day."
    _mc ea "Welp, Monika knows now. Nothing more I can do about it."
    _mc ef ma "... I’ve never been very good at hiding this stuff, have I?" # im stuff
    _mc ec "It’s all just..."
    show natsuki cross noband e2a mj:
        xcenter 0.33 zoom 0.8 ypos 1.0 yanchor 0.95
        matrixcolor TintMatrix("#d7caff") * BrightnessMatrix(-0.04)
    show bg:
        align (0.05, 0.6) zoom 1.9
    with Dissolve(0.2)
    _mc ea mh "Huh? I swear that’s Natsuki up ahead, leaning on a light post."
    #Full Voice Acting with Narrator
    n mh b1d "Hey."
    show natsuki md
    mc mf "What...?"
    n turned e3c mi b3a "Don’t mind me. Just wanted to drop by and see how you were doing."
    show natsuki ma
    mc bd mg "What do you mean? Is it not late as hell?"
    show natsuki md e1a
    mc ec ml bi "You don’t want to be out this late, Nat."
    n e1d b1d mh lhip rhip "And you do?"
    show natsuki mj
    mc ea ba mg "Well, no, I was heading home from work."
    n rdown mc e1a b1a "So, best to have someone walk with you, so that you aren’t alone, no?"
    show natsuki ma
    call blink(0.3) from _call_blink_6
    "I blink a couple times, trying to wrap my head around the level of idiocy currently in front of me."
    show natsuki ldown md
    mc mm bi eg "Okay, first off, all that time you spent alone puts you at greater risk than me. Second, you’ll have to walk home, which makes it even harder on you because you’ll be out even later."
    n e3d b3a mo lhip rhip "Yeah, but that’s fine. I’m pretty tough."
    show natsuki e1a md
    mc eb bd mg "I- I can’t- What is with you?"
    n cross e1d b3d mi "Me? Think about yourself! You..."
    n e2a b1d mm "Look. Just... walk with me."
    show natsuki md
    "I shake my head. Stubborn as she is, there’s no way I’m getting her to back down."
    mc ef bi ml "Fine... If that’ll make you happy."
    show natsuki mj e3c
    "She looks away for a moment, hiding her face."
    n b3a mi "Yeah, it would."
    show natsuki mj 

    scene bg school_street_night_off
    camera master
    show natsuki turned noband b3a md:
        matrixcolor TintMatrix("#4a4ea2")
        i11
    with wipeleft_scene
    $ advance_date(minutes=7)

    mc turned nostrands tail mg "It’s gotten really late. I don’t want you walking home and getting jumped."
    show natsuki me
    mc mb "Come on in; I’ll find somewhere you can sleep for the night."
    n b2a mg "Oh, wait, no, you don’t have to-"
    show natsuki b1a me
    mc ec bi ml "I insist. It’s insane enough you were out this late."
    show natsuki md
    mc ea ba mg "I wouldn’t normally be out this late; I got held up at work."
    n e2a b1d mg "... So that’s why you took so long..."
    show natsuki md
    "I want to ask why she went to all this effort, but honestly, I don’t have the energy anymore."
    _mc eg mh "All I want is to curl up and sleep."
    
    scene bg mc_living_room
    show natsuki turned noband at i11
    with fade
    $ advance_date(minutes=5)
    $ set_internet(True)

    mc turned nostrands tail mg "Oh, don’t mind the mess, I..."
    mc ef ml "Don’t get many visitors."
    n mb e2a b1d "Yeah, it’s okay, neither do I."
    n b3a e1a mh "So... You excited for the weekend?"
    show natsuki ma
    mc ea mb "Yeah, actually. Sayori’s sleepover is gonna be a big hit, I think. It’ll help bring us back together as a team, before the festival gets underway."
    n cross mb e2a b1a "Right? I’m looking forward to it. It’s been a while since I’ve stayed over at Sayori’s."
    show natsuki b2a ma nb
    "Her face darkens a little."
    show natsuki b1a e1a me
    mc ml "Why’s that?"
    n b3a mh e2a "... She, uh... struggles, sometimes, with people."
    show natsuki mj
    mc ef bi "Ohh, I get that. She was always so bubbly around me, I guess I never stopped to notice that it isn’t the same with others."
    "I click my tongue."
    show natsuki e3c b2a
    mc eg mf "If I’d noticed sooner..."
    n mb "Y- Yeah, if only..."
    n turned e1b b3a mk nc "Ah, I mean, nono, it’s fine! Everything’s fine!"
    show natsuki e1a me 
    "I give Natsuki a small smile."
    mc ea bg mb "It’s alright, you don’t have to pretend with me. I get it, we’ve all had a pretty raw deal. If I’d been a better friend to her, maybe things might have turned out better."
    n mg e2a b2a na "Yeah... But on the other hand, she might not have met me."
    show natsuki ma
    mc ba mg thinking "That’s true. I’ve been meaning to ask, honestly, about how you two met."
    n b3a e1a lhip mh "Us? It wasn’t anything special. Just the first day of high school."
    show natsuki md
    mc eg mb ldown "Ah, I see. Must have been some day, right? I’m sure she did something crazy."
    n e2a b1a mb "No, not really. Just... walked up to me, and said hello."
    n ldown e3c b3a mh "It wasn’t exactly anything super fancy, but I suppose... that’s what made it memorable."
    show natsuki md
    "I smile at her."
    _mc ec ma "She understands Sayori, alright."
    _mc ea "It’s good that she has people she can rely on."
    show natsuki e1a
    mc eg mb "Thank you."
    n cross e1d b1d mb "For looking after Sayori? Heh. Of course, she’s..."
    show natsuki ma
    mc ef "She really is something, right?"
    n e2a mb "... Yeah."
    show natsuki e1b b3a md
    mc ea mg "Want a coffee, or something?"
    n mn b2a "Pff-"
    mc ec ml bi "What?"
    n e1a b1d mb "Are you propositioning me?"
    show natsuki ma
    "Confused, I look her way."
    n turned mh lhip rhip e1d "Hah, of course not. You realise what 'coffee' this late means, right?"
    show natsuki md
    mc bm ml ed "... No?"
    n rdown ldown b1a mb "Sex. You’re asking for sex."
    show natsuki ma with None
    hide natsuki
    camera master:
        align (0.35, 0.2) zoom 1.7
    with Dissolve(0.2)
    "I blush furiously, glancing away from her."
    $ autofocus.block("natsuki")
    n turned noband b3a mh "Relax, I know you didn’t mean it that way. I really would like some, actually."
    show natsuki cross md at i11
    camera master
    with Dissolve(0.2)
    "I turn back toward her, prepared with a comeback for my recent embarrassment."
    $ autofocus.unblock("natsuki")
    n turned lhip rhip mh e1d b1d "The coffee, not the sex."
    show natsuki b1d e1a ma
    "I click my tongue. She beat me to the punch."
    n rdown e3a mc b1a "Yeah, don’t think that I didn’t see that one coming."
    n b3a ldown mh e1a "C’mon. Besides, I reckon there’s stuff we can do for a bit of fun tonight." # im stuff
    show natsuki ma
    mc ea mf ba na "Hm?"
    n e1d b1d mb "You’ll have to wait and see, won’t you?"
    show natsuki ma
    "She chuckles as I make my way toward the kitchen."

    stop music fadeout 2.0
    scene bg mc_living_room:
        blur 2.0
    camera master:
        align (0.5, 0.25) zoom 1.5
    show natsuki turned notail noband at i11
    with longfade
    $ advance_date(minutes=42, hours=1)
    $ autofocus.block("natsuki")
    $ say_transition = True
    play music dollaort

    "A few hours later, I find myself sitting on the sofa, with Natsuki beside me."
    n e1d b1d mb "I don’t believe for a single second you didn’t see that coming. Come on, be serious!"
    show natsuki ma with say_dissolve
    mc turned nostrands tail nb eb mg bb "No, seriously! I had literally no idea it was gonna happen! She just turned around one day and was like, 'I don’t like Kaito!'"
    show natsuki b3a e3d with say_dissolve
    mc eh md na "I was convinced, for ages!"
    n b1d e1a mc "God, that’s stupid! She’s not into guys like that."
    show natsuki me b1a with say_dissolve
    mc ba ea mb "Well, what kind of guys is she into? Maybe we should hook her up, sometime!"
    n cross noband b1d e2a mb nb "Ah, yeah, uh..."
    show natsuki ma with say_dissolve
    mc ef bg nb "O- Or, we could give her space, let her do her own thing, it was just an idea-"
    n turned noband b3a e1a mh na "No, yeah, it sounds like fun! It’s more that she hasn’t really responded well to anything like that, so it might be more trouble than it’s worth..."
    show natsuki ma with say_dissolve
    mc eg "Ah, right..."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I put down the glass of wine onto the coffee table, awkwardly."
    $ autofocus.unblock("natsuki")
    n lhip rhip e3c b1d mb "She’s a handful, too, so it would be a nightmare getting someone to stay..."
    show natsuki ma
    mc ec bi mg na "Who are you calling a handful? Have you met yourself, miss 'I’m gonna wait around in the dark for you so that you don’t get mugged, don’t mind me putting myself at risk of the exact same thing?'"
    n cross e2a mb "Hah, look, I told you, mistakes were made! It’s not like anything bad happened, did it?"
    show natsuki ma
    mc ea ba "Still, maybe think things through a little more, next time, hey?"
    show natsuki e3c b1a
    "I give her a slight nudge."
    n turned noband lhip mh e2a "... I’ll... take it under advisement."
    show natsuki b2a ma e1a
    "She gives me a small, but warm, smile."
    n b3a mh ldown "Oh yeah, the thing I was gonna do."
    show natsuki md e2a b1d 
    "She pulls out her phone, dialling a number."
    show natsuki b3a e1a ma at dip
    "Then, she hands it to me."
    mc mf "Who-"
    phone call "m"
    $ set_pov("n")
    phone_m "Hey, Natsuki, it’s extremely late, is everything-"
    phone_mc "H- Hey."
    phone_m "MC? Oh, sorry, I wasn’t expecting you, I thought this was Natsuki’s number-"
    phone_mc "It-It is, she gave me her phone."
    show natsuki lean with NonBlockingDissolve(0.3)
    "I look toward Natsuki, who simply smiles playfully at me."
    phone_m "What? Is she with you?"
    show natsuki turned with NonBlockingDissolve(0.3)
    phone_mc "Y- Yeah, we caught up after work."
    phone_m "I... I see."
    phone_m "Well, that sounds... like a lot of fun."
    phone_mc "Oh, yeah, it’s good fun, we, ah, just..."
    phone_m "Have you been drinking?"
    phone_mc "Me? Oh, well, what makes you say that?"
    phone_m "Because you don’t usually stumble over your words this much. Is everything alright?"
    phone_mc "N-No, yeah, it’s fine! It was just unexpected when Natsuki handed me her phone, that’s all!"
    phone_m "Not as unexpecting as me, I suspect."
    phone_mc "Aha, true! That must have been a shock!"
    "{i}I want to kick myself.{/i}"
    "{i}No, correction: I want to kick {b}Natsuki{/b}.{/i}"
    "{i}All this time, she’s worn this goofy smile, listening to our conversation.{/i}"
    phone_m "W- Well, I hope you two have a good night! I’ll see you tomorrow at school!"
    phone_mc "Y- Yeah, have a good night, Monika!"
    phone end call
    $ set_pov("mc")
    "I take a slow, deliberate breath."
    mc eg ba ml "Natsuki."
    n mh "Well? How’d it go?"
    show natsuki ma
    mc bd eb mg "How do you think it went, picking up the phone, only to realise that it’s someone else, this late?"
    show natsuki me b1a
    mc ea ml "Do you have any idea what she might be thinking about us, now?"
    n b4 mg "Yes?"
    show natsuki me
    "Confused, I throw her a look."
    n lhip rhip e1d b1d mh "You don’t get it. If it seems like someone else is making a move on you, you’ll seem more attractive. That’s how our brains are wired to function."
    n b1a e1a mc "So, if she thinks, even for a second, that I might make a move on you, that’s your chance to jump on."
    n rdown e2a mb "Even now, I’ll bet she’s mulling it over."
    show natsuki ma
    mc ba mf "What about-"
    n ldown e3c b3a mi "Do you honestly think she would tell anyone about this? No. She’s not that kind of person, Melody."
    show natsuki e1a ma
    mc ef ba ml "... Fine. I’ll trust you."
    mc ec mg bi "And who gave you the right to call me Melody?"
    n e1d b1d mb "I did~ You know, when I started making moves on you to impress Monika~?"
    show natsuki ma rhip at dip
    "She lightly elbows me, before emptying her glass."
    n rdown e1a b1a mc "C’mon, let’s have another."
    show natsuki ma

    scene bg mc_bedroom_night_closed_on
    show natsuki turned notail noband e1d b1d nc at i11
    with wipeleft_scene
    $ advance_date(minutes=33)

    n mb "Soooo- This is the place where the magic happens? {w=0.03}{nw}"
    show natsuki at hop
    extend "-hic-"
    show natsuki ma
    mc turned nostrands tail nb eh md "Yep, this is my room!"
    n b3a e3c mh "You gonna {w=0.03}{nw}"
    show natsuki at hop
    extend "-hic-{w=0.02} take Monika up here, and give her the ol’ cunning linguist? {w=0.03}{nw}" # jesus fuck natsooki
    show natsuki at hop
    extend "hic-"
    show natsuki ma
    mc ef mb nd "I, ah, have no idea what you mean, ahahaha..."
    n e1d b1d mn "C’mon, we both {w=0.03}{nw}"
    show natsuki at hop
    extend "-hic-{w=0.02} know how good your poetry is, just imagine what those tongue muscles would be capable of..."
    n b3a e3c mb "Maybe during all this time pretending, I should {w=0.03}{nw}"
    show natsuki at hop
    extend "-hic-{w=0.02} take you for a test drive~"
    show natsuki ma
    mc eg ba nb mg "Aaaand we’re done here!"
    show natsuki e3a md
    "I stumble as I lead her out of the room."
    n lhip rhip e1d na b1d mh "You know I’m kidding, just messing with you..."
    n rdown e2a b1a mb "Geez, you fluster so easily... makes you so cute and fun to tease..."
    show natsuki e1a b1a ma
    mc ed md nb "Speak for yourself, huh? How easy are you to get all hot and bothered?"
    n ldown e1d b1d mb "Oh, all you gotta do is say the word... {w=0.1}{nw}"
    show natsuki at hop
    extend "-hic-"
    show natsuki ma
    #End Voice Acting
    "I shake my head, too tired and drunk to deal with this nonsense. I know she’s screwing with me, but I don’t want any ideas getting into the back of my brain that there’s something else going on."
    
    scene bg mc_bedroom_night_closed_on with fade
    $ advance_date(minutes=5)

    "After getting her sorted in my parents’ old room, I tuck myself in for the night. What a day..."

    $ add_calendar_description(calendar_descriptions["monika"][7], day=2)

    call week_2_friday_monika from _call_week_2_friday_monika
    return