label week_2_monday_natsuki:
    call calendar_transition(day=30, hour=8, minute=10) from _call_calendar_transition_18
    scene bg school_street_day
    camera master:
        align (0.0, 0.8) zoom 2.2
    with dissolve_scene_full
    $ set_internet(False)
    play music school

    "Sayori and I find ourselves waiting by a street corner for Amelia to arrive."
    camera master:
        zoom 1.8 align (0.5, 0.2)
    show sayori turned at i11
    show bg:
        blur 2.2
    with Dissolve(0.2)
    "We pass the time with some small talk as we wait."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    mc turned ml "So, about that secret of-"
    show sayori e1b b1d mh at hop
    s "Shh! It's a secret!"
    show sayori md
    mc mg "But you texted everyone about it last-"
    s mn e3d b1a "I know~!"
    mc ec mh "..."
    s mb e1d b1d "Let's keep in on the down low~"
    show sayori ma
    "I roll my eyes, chuckling to myself."
    mc ed md "Sure, sure. Let's go with that~"
    s lup mb e1a b1a "Oh! Did you watch the new episode last night?"
    show sayori me
    mc eb mg nb "New episode? Oh, wait, it was Sunday! Shoot..."
    s e1d b1d mh ldown "Awww, Mel, you gotta keep up! Otherwise we won’t be able to talk about it..."
    show sayori md
    mc ef ml na "My bad, I was out."
    s e1a b1a mh "Oh? Where did you go?"
    show sayori md
    mc mg "... I went out for dinner."
    s tap eb "Without inviting me? Aww..."
    show sayori ea ma
    mc ea ml "Well, no, it’s not like I went without you, I was more with-"
    _mc ea mh "Huh. Something tells me I probably shouldn’t talk about it? Weird. It’s far from the first time we’ve gone out for dinner, so why do I feel guilty-"
    _mc ec "Ah."
    show sayori turned md e1a
    mc ea mg "I went out with Amelia for dinner."
    s mg "Oh."
    show sayori:
        0.08
        "sayori turned b2c e2a md"
        0.1
        "sayori turned b2c e2a mj"
        0.05
        "sayori turned b2a e2a ma"
        0.06
        "sayori turned b1a e1a ma"
    "A flash of emotion crosses her face, too fast for most people to catch."
    _mc ec mh "Unfortunately for her, I know her too well."
    show sayori mj
    mc ea ml "What is it?"
    s e2a b2c mg nb "I..."
    s e3d mb b1a "It’s nothing."
    show sayori e1a ma
    mc mg bg "It’s clearly not nothing, Sayori. I’m sorry that you’re not..."
    show sayori e2a b2a md

    phone register "mc_am":
        time auto True
        "am" "Hey dude, gonna have to pass on walking with you guys today, got a bad case of dying."

    mc mb "Not comfortable with the idea, but there’s nothing going on between us. Besides, it’s not like there’s anything to be concerned about anyway, right?"
    s mb nb "It’s not that I’m jealous or anything, it’s just..."
    s lup e1a b2c mg "Makes me feel left out."
    show sayori mj
    mc eg ba "... Yeah. I know that feeling."
    show sayori ldown na
    mc ea bg "I’m sorry for leaving you out."
    mc ba mg "Sometimes, I just want to spend some time doing other things though, you know?"
    s e2a b2a mb "... Yeah."
    show sayori mj nb
    "She looks away, biting her lip."
    _mc ec mh"I know this is hurting her, but it’ll be a lot easier for her to accept the pain now, than to have to find out later and feel more betrayed."
    s mb "You’re obviously allowed to spend time with other people, of course you are, but I..."
    s e1a b2c mg nd "I just got you back."
    show sayori mj
    mc ef ml "... I’m sorry."
    s e3c b2b mh "I know you are. You wouldn’t be telling me if you were."
    s e2a b2a mb lup "I know that things are different now, but I..."
    s b2c md nc ldown  "..."
    "She looks away, unsure what to say."
    _mc ec mh"... As do I."
    mc ea bg mb "Sayori, you’re my best friend, okay?"
    s mg "... I know."
    s b2a e1a mb "We’ll always be together, right?"
    show sayori ma
    mc ed md ba "The Bard protects the Mage, and so it is."
    show sayori e3d b1a na
    "We chuckle together, almost silently."
    show sayori e1a
    _mc ea thinking mh "... Wait, where’s Amelia? Shouldn’t she be here by now?"
    "I pull out my phone and check my messages."
    phone discussion "mc_am":
        pause
    _mc ec ldown "... Figures, she’s stayed home, sick."
    phone end discussion
    show sayori md
    mc ea mg "We... might have to run to school."
    s e2c b2a mb "Ehe, that’s... entirely deserved, I reckon."
    show sayori e1b b1a mk at lhide
    hide sayori
    "With that, we nod to each-other, and start to sprint down the road toward school."

    stop music fadeout 2.0
    scene bg class_1_day
    with wipeleft_scene
    $ set_date(hour=12, minute=4)
    play sound school_bell
    pause 0.5

    play music friendly_endeavours

    _mc turned eg "Ah, there it is. Lunch time."
    _mc ea "The perfect time for me to relax, get some nice shut-eye before the next class-"
    _mc ec mh "And right on cue, the girl returns from her mysterious 'job'."
    show natsuki cross at t11
    n e2a mh "Hey."
    show natsuki e1d b1d mj
    mc ea mb "Hey, Nat."
    n mg "Natsuki, to you."
    show natsuki mn with None
    camera master:
        align (0.5, 0.5) zoom 1.7
    show bg:
        blur 0.0
        xoffset -100 blur 2.0
    show natsuki turned e3c b3a ma:
        xoffset 150 yoffset 120 zoom 0.9
    with Dissolve(0.3)
    $ autofocus.block("natsuki")
    $ say_transition = True
    "She huffs, before putting her face close to my ear."
    n b3a mb "Unless... You want to call me that?"
    show natsuki ma with say_dissolve
    "The hairs on the back of my neck stand at attention, as do... many other things that are not hairs."
    show natsuki e1a with say_dissolve
    mc ef bg nb "I, ah, well-"
    show natsuki e3d mo b1a with say_dissolve
    n "Pff- Hah! You should see the look on your face! That’s some good intel; weak to ASMR!"
    camera master
    show bg:
        xoffset 0 blur 0.0
    show natsuki ma:
        offset (0, 0) zoom 0.8
    with Dissolve(0.15)
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    n e1a mc "C’mon, I’ll give you some lunch. Can’t expect that juicy piece of insider information to be free, after all~!"
    show natsuki ma at dip
    "She grabs me by the arm, dragging me away."
    show natsuki e2a at thide
    hide natsuki

    scene bg school_rooftop_day
    show natsuki turned at i11
    with wipeleft
    $ advance_date(minutes=2)

    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.25) zoom 1.5
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("natsuki")
    show natsuki b1d e1d mj with say_dissolve
    window auto show {"screens": config.window_show_transition}
    mc turned ea mg "So... Why are we here?"
    n b4 mh "To eat in peace?"
    n cross mc b1a e1a "C’mon, look. I made something nice for you."
    show natsuki nc b1d e1b mm with say_dissolve
    mc ed md "For me?"
    n turned e2b b3d mi "N- Wha- N- No, not {i}for{/i} you! I just happened to be making food, and it was there! I figured it wouldn’t go to waste if I gave it away! See!"
    show natsuki mm with say_dissolve
    mc eg ma "Mhm. Right."
    _mc ec mh thinking "Why do I feel like I’m in a manga right now?"
    _mc ea ma "Ah, it must just be the copious amounts of 'tsun' in the air."
    n e2c mh b1d nb "Besides, don’t you want to try some of my cooking? It’s the best there is! And if {i}you{/i} had it, I guess I wouldn’t mind..."
    show natsuki md with say_dissolve
    _mc ec "And there’s the 'dere'."
    mc ldown eg mb "Sure, I suppose I’ll lower myself to have a little."
    _mc ec ma "If there’s one thing I’ve learned, it’s that the best way to deal with these types is to give them exactly what they want."
    _mc ea "A challenge."
    n cross nc b3d e3c mc "L- Lower yourself? As if you’re above my amazing cooking! I’m the best around, and don’t you forget it!"
    show natsuki e1a ma with say_dissolve
    mc ed md "Yeah, sure, sure. You might be decent, but you’ve never had {i}my{/i} cooking before, right?"
    mc ea mb bd "You won’t know what hit you."
    n turned na mb e1d b1d "Hah! I’ll take you up on that challenge! You and me, let’s go!"
    show natsuki mn with say_dissolve
    mc ed md ba "Trade?"
    n mb "Trade!"
    show natsuki ma with None
    show natsuki e3d b1a 
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    show natsuki at dip
    $ say_transition = False
    "She shoves her lunchbox into my arms, snatching mine away from me."
    _mc ec ma "... Well, I suppose I’ll take it. Best to see if she’s as good as she claims."
    hide natsuki
    show bg:
        align (0.5, 1.0) zoom 2.0
    with NonBlockingDissolve(0.3)
    _mc ea mh "Here goes..."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc eg mf "... Hm."
    _mc ea mh "This is..."
    $ autofocus.unblock("natsuki")
    _mc ec "Perfectly serviceable."
    _mc ea "Nothing catastrophic, but nothing really standing out, either."
    _mc thinking ec "I wonder where she got half these spices from. It seems like she just grabbed half a pantry to see what sticks, but it turned out surprisingly well."
    _mc ea ma ldown "I’m genuinely impressed; it’s better than I thought it would be, but not as awful as I expected. It certainly doesn’t hold up to her claim of 'the best', at the very least."
    show natsuki turned e2a b1d md nb at i11
    show bg:
        zoom 1.0
    hide black
    with Dissolve(0.2)
    "I turn to look at Natsuki, who, in contrast to my surprised smile, wears a frown."
    "One could almost say a grimace."
    _mc thinking mh "Odd, I thought I’d done a decent job with today’s meal. Maybe I’d messed something up?"
    mc mg "It’s not that bad, is it?"
    n mg "... It’s good."
    n mh nd e3c "Really good."
    show natsuki md with None
    hide natsuki
    camera master:
        align (0.4, 0.5) zoom 2.7 
    with Dissolve(0.2)
    "With that, she quite literally jumps to her feet, closing the box, and walking back off toward the rooftop access."
    "... Taking my lunch with her."
    mc nb ldown bd "Hey! I need that for lunch tomorrow!"
    n turned nb b3a mc "You’ll get it back!"
    n b1d mi "Also! I’m making you lunch! Don’t you dare make your own!"
    mc eb "Wait, what?"
    n b3d "You heard me!"
    "And with that, the door slams behind her."
    camera master
    with Dissolve(0.3)
    _mc mh "... What just happened?"
    _mc ec na ba mh "I’ll admit, I was following along for the tsundere act, but she lost me with the storming off. Is she just trying really hard to act tough, when she enjoyed it?"
    _mc ea thinking "It seems like the most probable solution, at least. But if that’s the case... Why? I feel like I’m missing some valuable piece of information here."
    _mc ec ma "Ah, whatever. I shouldn’t complain about a free lunch."
    
    stop music fadeout 1.0
    scene bg mc_bedroom_night_closed_on with fastfade
    $ set_date(hour=21, minute=30)
    $ set_internet(True)

    _mc turned naked messy nostrands ec mh "... I never did get my lunch back."
    _mc ea "Not even at the club, where I gave her own box back."
    _mc ef ma "Was almost tempted to keep it as a hostage, but... that might just cause problems. She might just need it for making me lunch tomorrow."
    _mc ea "Besides, who am I to complain about free food? Saves me money, and the time it takes to make it each morning."
    _mc ec mh "Speaking of, I should probably remember to make a shopping list in the morning. Let me set an alarm for that..."
    _mc ea ma "... And there. Hopefully I’ll remember to bring it to school, so I can grab it on my way home."
    _mc mf thinking "Wait, I can’t do it tomorrow; I’ve got work."
    _mc ec mh "I’ll have to do it Wednesday; I’ll have plenty of supplies to last until then."
    _mc ldown ea ma "Still, best to make the list tomorrow, before I forget."
    _mc ec "... Putting all that aside, though, it’s definitely time to sleep."
    _mc eg "Sweet dreams, me..."

    show bg mc_bedroom_night_closed_off with None
    scene black with Dissolve(1.5)
    pause 1.5
    play sound phone_notification
    pause 0.5
    show bg mc_bedroom_night_closed_off:
        align (1.0, 1.0) zoom 2.0
    hide black
    window auto show None

    _mc turned messy naked nostrands mf ec bi "Who's calling this late...?"
    "Grabbing the phone from my bedside table, I fumble with the thing for a moment as I bring it to my ear."
    phone call "s"
    play music a_sunshine
    phone_mc "Hello...?"
    phone_s "Hi! Melly, wake up."
    phone_mc "Already have..."
    phone_mc "I guess, kinda...?"
    phone_s "No no, {i}up{/i} up!"
    phone_mc "Huh?"
    show bg:
        zoom 1.0
    with NonBlockingDissolve(1.0)
    "I get to my feet, my sleepy brain still not sure what words she's saying, let alone what meaning might lie behind them."
    phone_s "Listen~ I want to do something cool, but I need your help."
    phone_mc "Alright, shoot."
    "Rubbing the sleep from my eyes, I finally shrug myself awake."
    phone_s "Can we make something together?"
    phone_mc "What, like one of those build-a-bear things?"
    phone_s "No- Wait, actually yes! That's even better than the idea I had!"
    phone_mc "... Huh?"
    phone_s "I wanna make something for my mum when she comes back."
    phone_mc "Oh... Oh! Right! Yeah, we're on the same page now."
    phone_mc "So a stuffed toy?" # im stuff
    phone_s "Maybe? I dunno."
    phone_mc "I know what she would want, actually!"
    "I can hear her cheer through the window, let alone through the phone."
    phone_s "Tellmetellmetellme!"
    phone_mc "How about we make her a photo album?"
    "She doesn't say anything, instead letting out an excited yelp."
    phone_s "YES!"
    phone_s "That's perfect! I'm gonna go through all the photos!"
    phone_s "You better go through all yours too!"
    phone_mc "Alright, I'll have a look in the morning. We can put it together over the next week or so."
    phone_s "Yeah!"
    phone_mc "When are you expecting them back?"
    phone_s "..."
    "A pause."
    phone_s "I dunno."
    phone_s "I was hoping they'd be back for Christmas, but..."
    phone_mc "That's still a month or two away, we've got time."
    phone_s "N- No..."
    phone_mc "... Last Christmas."
    "Her silence affirms my statement."
    phone_mc "Sayori, I-"
    phone_s "Mh-mh. Don't even think about worrying about me."
    phone_s "I'm good! They'll be alright, always are."
    phone_mc "In that case, it should be an extra big surprise for their return. Maybe we should plan a party?"
    phone_s "Oooo~"
    phone_s "I like it!"
    phone_mc "Let's do that then, yeah?"
    phone_s "We can invite the relatives, and-"
    phone_s "O- Oh, crowds."
    phone_mc "Yeah! Get a big group together!"
    phone_s "You sure?"
    phone_mc "Absolutely."
    "I grit my teeth, pushing down the small bubble of anxiety welling in my gut."
    "{i}This is for Aunt Katsuragi - I'm not going to let some fear of crowds ruin anything.{/i}"
    phone_s "Then... I guess once we make the album, all we can do is wait?"
    phone_mc "I'm sure it won't be long. Let's hope that they {i}are{/i} gonna be home for Christmas this time, yeah?"
    phone_s "Yeah."
    "She stands by the window, placing her hand upon the glass."
    "From my room, I kneel on my bed, returning her gesture."
    phone_mc "Talk to you tomorrow?"
    phone_s "Talk to you tomorrow."
    phone end call
    "With that, I hang up the phone, relaxing back into the bed."
    "A warm sigh escapes my lips."
    _mc eg ba mf "You know what?"
    _mc ma "I've missed this."

    $ add_calendar_description(calendar_descriptions["natsuki"][5])

    call week_2_tuesday_natsuki from _call_week_2_tuesday_natsuki
    return