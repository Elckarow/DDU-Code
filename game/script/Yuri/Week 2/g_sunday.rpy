label week_2_sunday_yuri:
    call calendar_transition(day=5, hour=8, minute=53) from _call_calendar_transition_47
    pause 0.5
    scene bg s_living_room with mc_pov(True)
    show sayori turned casual e2a me at t11
    $ set_pov("mc")
    play music ohayou

    "As I walk around the house, I find Sayori already cleaning up the living room."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc turned casual mb "H- Hey, don't you need any help?"
    s mg e1a "Oh! I didn't know you were awake."
    s mb "Sure~ Help me then!"
    show sayori ma with say_dissolve
    mc ml nb "I mean... starting cleaning without us...?"
    show sayori md with say_dissolve
    mc bg mg "You're not the {i}only one{/i} that made a mess you know."
    s mn e3d b1d "S-stop being so responsible~"
    show sayori e2a b2b ma with say_dissolve
    "Sayori gives a little laugh and looks away for a few seconds, not wanting to make direct eye contact."
    s mg na "Sorry..."
    s b2a mb e1a "I wanted to get it done and over with."
    s me "Let you all sleep and such..."
    show sayori md with say_dissolve
    mc ba na "Don't say sorry, I meant... You shouldn't do all this alone, okay?"
    show sayori e1a with say_dissolve
    mc mb "Like... really, we're always ready to help."
    show sayori me b1a e3c with say_dissolve
    "Sayori sighs, then quickly takes on a smile."
    s mi "Okaaay..."
    s e1a mb lup "Then... You can start by getting all the dirt off the floor!"
    show sayori ma with say_dissolve
    mc ed md "Quick to assign me a task, I see~"
    show sayori ldown
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I grab a broom, and move all of the dirt and garbage on the floor to a corner so it can be easily grabbed with a dustpan."
    show sayori md
    mc mg ea "Hey, Sayori. What did you think of the sleepover?"
    $ autofocus.unblock("sayori")
    s e2a mg "... I enjoyed it."
    s e1a mb "How about you?"
    show sayori ma
    mc eh md "Same here. It's the most fun I've had in a while, really."
    mc ea mb "We should do this kind of stuff more often, you know?" # im stuff
    s e3d mb "Yeah! I agree."
    show sayori ma
    "..."
    mc ef ma "..."
    show sayori e1a
    mc ea ml "Hmm... Do you think that-"
    show sayori at t21
    show yuri turned casual lup b1d e2a at t22
    "Suddenly, Yuri walks into the room."
    y mb "Hey..."
    show yuri ma
    mc mb "Hey... Morning Yuri."
    show sayori lup rup mb e3d at hop
    s "Mooornninggg!"
    show sayori ma
    y e1d mh b1a "Could I talk with you later, MC?"
    show yuri ma
    show sayori ldown rdown e1a
    mc "Yeah. I'll be there when we're done, okay?"
    show yuri e3c
    "Yuri nods."
    y e2a ldown b1d mb "I'll wait upstairs..."
    show yuri ma at thide
    mc eg ma "Okay."
    hide yuri
    show sayori e1d b1d md at t11
    "As Yuri goes upstairs once more, Sayori looks at me confused."
    $ autofocus.block("sayori")
    s "..."
    $ autofocus.unblock("sayori")
    s mg "Huh."
    show sayori md
    mc ea mf "Hmm?"
    s lup e1a b1a mh "What do you think she wants to talk about?"
    show sayori md
    mc ef mg "Could be anything."
    show sayori ldown
    mc ea mb "I'm doing what you said, remember?"
    mc ef mg "Supporting Yuri."
    show sayori e1b mh at hop
    s "Oh!" 
    s e2a mg "... That's right."
    s e1a mb "Thanks, Melly."
    s e3c b2b mh "I just worry about her sometimes, that's all."
    show sayori md
    mc ml bg "So do I."
    show sayori e1a ma b1a
    mc bf ea mb "But... that's a good thing, no?"
    s e2a mb "Yeah..."
    show sayori ma with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "I look at Sayori, and smirk."
    show sayori e1a md with say_dissolve
    mc ed md ba "Now, to speed it up... let's get scrubbing!"
    mc ea bd mb "This house ain't cleaning itself!"
    show sayori e1b me with say_dissolve
    mc ed md "Person who cleans the most wins!"
    s lup e1d b1d mb "Oooh, you're on!"
    show sayori ma with say_dissolve
    
    scene bg s_house_corridor_day
    camera master
    show natsuki turned casual notail noband me b3a at i21
    show monika turned casual nb mc at i22
    with fade
    $ say_transition = False
    $ autofocus.unblock("sayori")
    $ advance_date(minutes=43)

    "As Sayori and I clean nearly all of the house, Natsuki and Monika stare at us in disbelief from up the stairs."
    n nb mg "They're making such a ruckus..."
    n e1b b1d mh "... Do you think they've gone insane?"
    show natsuki me
    show monika ma ed ma
    "Monika chuckles."
    m mb "Maybe."
    show monika ma

    scene bg s_living_room
    show sayori turned casual me nb e1b b1d at i11
    with wipeleft
    show sayori at t31
    show natsuki turned casual notail noband at t32
    show monika turned casual mc at t33
    $ advance_date(minutes=5)

    "Monika and Natsuki slowly enter the living room, looking at our little competition."
    m md "Do you... two need our help?"
    show monika mc nb
    show sayori mh at hop
    s "No! I'm winning!"
    show sayori mj
    mc turned casual nb ec md bi "You're not!"
    show natsuki cross b1d e2c ma
    show monika na eb ma
    "Natsuki trades a glance with Monika."
    n mb "So... insane?"
    show natsuki ma
    m bb mb ec "Yeah."
    show monika ma

    scene bg s_living_room:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    show sayori turned casual me b2b e3c nb at i11
    with fade
    $ autofocus.block("sayori")
    $ say_transition = True
    $ set_date(hour=11, minute=4)

    "After a long and vigorous battle, we sit on the couch, as exhausted as one can be."
    mc turned casual bi mb eg nb "Haah... I won.."
    s b1d mh "You did not..."
    show sayori mj with say_dissolve
    mc ec md "Got any proof otherwise...?"
    s lup mh e1d "Got any proof {i}you{/i} won...?"
    show sayori md with None
    show sayori at i21
    show yuri turned casual md e1d lup at i22
    show bg:    
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    "Out of nowhere, Yuri enters the living room."
    show yuri nb e1b mj
    "As she looks around, she quickly realises she made a mistake entering the room."
    $ autofocus.unblock("sayori")
    s ldown mi "Hey, Yuri...!"
    show sayori mj
    y me b2b e1a "H- Huh?"
    s mh na "Who won?"
    show sayori md
    y b4 mg e1d na "What...?"
    show yuri b1a md
    s mb e1a b1a "The dangerous cleaning battle!"
    show sayori ma
    y mk ldown e2c b2b "Uh..."
    show yuri mj at thide
    hide yuri
    show sayori md at t11
    "Yuri slowly backs out of the room."
    mc bi mf ef "Talk about supporting her..."
    s e3c b1d "Hmpf..."
    mc ea na ml ba "Well..."
    mc ef bi mf "What time is it...?"
    "I look at the slightly tilted clock."
    show sayori b1a e1a
    mc ba ea ml "It's 11:05!"
    mc mg bb nb "We've been cleaning almost all morning!"
    s tap mb eb "No wonder I'm so hungry..."
    show sayori turned ma at t41
    show natsuki cross casual noband at t42
    show monika turned casual at t43
    show yuri turned casual at t44
    "Yuri, Monika and Natsuki enter the room, hoping we've stopped with our dangerous cleaning battle."
    m mb "So... I think it's about time for me to go."
    show monika ma
    show sayori md
    n e2a mh "Same here, can't be home too late."
    show natsuki mj
    s mh "Oh- That's fair..."
    show sayori md
    m mb "It was fun though!"
    show sayori ma
    show natsuki e1a ma
    m rhip ed "Thanks, Sayori."
    show monika ma
    show sayori e3c
    "Sayori rolls her eyes, making her voice sound grandiose."
    s lup e3c mi "Of course, my dearest friends. The pleasure is my utmost."
    show sayori e3d mn
    m mb "Bye Sayori!"
    show monika ma at thide
    n turned mc "See you tomorrow."
    show natsuki ma at thide
    hide natsuki
    hide monika
    show yuri lup md e1d at t22
    show sayori at t21
    "As Monika and Natsuki leave, Yuri looks at me, her jacket donned."
    _mc eb bg mh "Oh crap, I almost forgot."
    show sayori md e1a ldown at t11
    show yuri at thide
    hide yuri
    mc ea mg bb "I'll be back in a second, Sayori."
    show sayori e3b rup ma
    "Sayori gives a thumbs up."

    scene bg s_house_entrance_day
    show yuri turned casual rup at i11
    with wipeleft

    "I approach Yuri who's waiting in the hall, she's holding her bag in her hands."
    _mc turned casual ec "She seems relaxed..."
    y e2c mb "Mind if we... talk outside?"
    show yuri ma
    mc ea mb "Fine by me. Let me grab my coat."
    y e3c mb "Alright. I'll wait outside."
    show yuri ma at thide
    hide yuri
    "As Yuri goes on ahead, I put on my jacket, put on my shoes..."
    "And head on outside."
    
    stop music fadeout 1.5
    play ambient ext_day fadein 3.0
    scene white with Dissolve(0.9, time_warp=_warper.easeout_quart)
    pause 0.2
    scene sky_day at moving_sky with Dissolve(3.0, time_warp=_warper.ease)
    pause 1.5
    scene bg s_house_day
    show yuri turned casual lup e2a md at i11
    with Dissolve(2.4)

    "Yuri stands next to a wall, staring into the sky."
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "As I approach her, her gaze does not waver."
    mc turned coat_casual mg "What did you want to talk about?"
    y "..."
    y mg ldown "... MC, after the festival, I'll be taking a week off."
    show yuri md with say_dissolve
    mc mf "Huh?"
    mc bd ml "Off the club? School?"
    y b1d mg "Both..."
    show yuri b1a e1a ma with say_dissolve
    "Yuri lowers her gaze to meet mine."
    y lup e1d mh "Remember those family issues I talked about?"
    y e2a b1d mg "I need some time to deal with them."
    show yuri md with say_dissolve
    mc ef bg mf "Oh..."
    mc ea bf mb "Will you be okay?"
    y b2b mb "Y- Yes, of course."
    y mh "I wanted you to know this."
    show yuri md with say_dissolve
    mc ml bg "... Is there any way I can help?"
    show yuri b1d e3c mj with say_dissolve
    "Yuri shakes her head."
    y e1d mg "I... think I need to do this alone."
    show yuri md ldown with say_dissolve
    "Looking at Yuri, I see her words are genuine."
    mc ef mg "Alright... I understand."
    y mg e2a b1a "And..."
    show yuri mj e3c nb with say_dissolve
    "Yuri shuffles in place."
    y shy mc eb na "If you need me... you can always call me."
    y ea "You... have my phone number, right?"
    mc ea ba ml "Yeah, I do."
    mc mb "Want me to do anything for you during that week?"
    y turned rup b2a e2a mb "N- No, just...Take care of the others, okay?"
    y ldown rdown b2b e3c mh "If they worry about me, tell them that I am okay."
    show yuri me e2a with say_dissolve
    "Yuri then falls silent, considering her next words."
    y b1a mg "I'll..."
    y e1a mb "I'll be back at the literature club before you know it. Alright?"
    show yuri ma with say_dissolve
    "Processing the conversation, I slowly give a smile."
    mc eg mb "Alright. You have nothing to worry about."
    mc ea mg "And same goes to you, alright?"
    mc ef ml "If you need me..."
    "I make a phone gesture with my hand, placing it next to my ear."
    mc eh bg md "Call me."
    show yuri e3c with say_dissolve
    "Yuri smiles back."
    y mb "I will."
    show yuri ma with say_dissolve
    "..."
    y e2a b1d mb "I'll need to go now, so..."
    y e1d b1a mh "Could you say bye to Sayori for me?"
    show yuri ma with say_dissolve
    mc ea mb ba "Of course!"
    mc bf "Take it slow, okay?"
    mc bg eg "We're always here for you."
    show yuri e2a b2b with say_dissolve
    "Yuri averts her gaze, most likely processing the conversation as well."
    y mb "Thanks."
    y e1d b1a "I'll see you tomorrow, MC."
    show yuri ma with say_dissolve
    mc eh md ba na "See you!"
    camera master:
        align (0.0, 1.0) zoom 1.3
    show bg residential_day:
        blur 1.0 align (0.1, 0.0) zoom 1.2 
    show yuri:
        ypos 1.03 yanchor 1.0 xcenter 220 zoom 0.57
    with Dissolve(0.3)
    $ say_transition = False
    "Yuri walks away, slowly disappearing into the distance."
    show yuri lup e1a with say_dissolve
    "Before she fully disappears out of view, I think I can make out a wave."
    "I wave back."
    hide yuri
    show bg:
        blur 0.0
    with Dissolve(0.5)
    "Once I can no longer see her, I head back inside."
    
    stop ambient fadeout 2.0
    scene bg s_living_room 
    camera master
    show sayori turned casual md at i11
    with wipeleft
    play music a_sunshine
    $ autofocus.unblock("yuri")

    mc turned casual mg "Yuri had to go, she wanted me to say bye for her."
    s mg e2a b2a "Ah... Everyone leaving so quickly."
    show sayori ma
    "Sayori looks a little sad, but she seems to understand."
    s b1a e3c mb "Ha... Well, no round two I suppose."
    show sayori e2a b1d md
    "Sayori then pouts."
    s e3c mi lup "Not like I need one!"
    s e1a b1a mh "How about you, Melody?"
    show sayori ma
    mc ef ml "I'll be leaving in a bit as well."
    mc ea mb "Just have to gather my things."
    s ldown mb "Alright. If you can't find them, you're not the cleaning master~"
    show sayori ma
    mc ed md "Hey, neither are you!"
    s mn e1d b1d "Hehe."
   
    scene bg s_house_corridor_day with wipeleft

    "As I go upstairs and grab my things, I take one last glance around the house in which we had our sleepover."
    _mc turned casual ec "It was fun."
    _mc ea "I really hope we'll do something like this again soon."
    _mc eg "It made me finally feel my age."
    _mc ec "I hope everyone enjoyed it."
    _mc ef "But... I think I'll hear about that tomorrow."

    scene bg s_living_room 
    show sayori turned casual at i11
    with wipeleft

    mc turned coat_casual mb "Alright, I'll be going now Sayori!"
    mc eh md "Thanks again for today."
    s e3c mb "No, thank you for coming, Melly."
    show sayori ma
    "I give a smile, put on my shoes and jacket again, and take my leave."
    
    scene bg s_house_day with wipeleft

    _mc turned coat_casual ec "Ah... Time to go home and relax."
    _mc eg "These two weeks have surely been something."
    _mc mh "I hope Yuri will be alright."
    _mc ef "I know she said she will, but..."
    _mc bg "..."
    _mc bi eg "Yeah, she'll be alright."
    _mc ea ba "I hope she got home safe with the same route we always take."
    _mc ec "That said..."
    _mc ea thinking "I wonder what her family troubles are about...?"
    _mc ldown nb ef "Ah, I... probably shouldn't put my nose in someone else's business."
    _mc eg na "Once she feels comfortable, she might tell me herself."
    _mc ec "... Or not. That's her choice too, and I accept that."
    
    scene bg residential_day with wipeleft

    "Instead of heading home, I decide to go for a wander."
    play sound widenekoflap
    _mc turned coat_casual mh "Hm...?"
    _mc eb ma "Oh!"
    show bg:
        align (0.7, 0.9) zoom 2.5
    show widenekoflap:
        align (0.5, 1.0) zoom 0.8
    with Dissolve(0.2)
    mc mb ea "Hey, kitty cat!"
    _mc ec ma "It's the same small, black cat..."
    camera master:
        align (0.5, 1.0) zoom 1.3
    with Dissolve(0.2)
    "I approach the cat to pet it."
    mc ea mg thinking "You're quite far from home!"
    mc mb ldown "Have you seen Yuri passing by, maybe?"
    "I look at the cat, searching for a name tag."
    mc mf "Huh. No name tag."
    mc bg ml "Are you a stray?"
    mc ea mb ba "Well, you're free to come to my house, if you feel like-"
    mc ef bi ml "... Ah, wait. I might not be able to care for you..."
    mc eg mb ba "You can come by every so often, if you need a place to rest your head, but I'm afraid that's all I can offer you, little one."
    "The cat looks up at me, checks its surroundings, then starts to scratch its head before giving me a meow."
    _mc ec ma "... Like this cat would actually understand my ramblings, haha..."
    mc ea mb "Well, I'll see you around, hey?"
    hide widenekoflap
    show bg:
        zoom 1.0
    camera master
    with Dissolve(0.2)
    "I leave the cat behind me, returning to my homely abode for the day."
    
    scene bg mc_bedroom_day_open with wipeleft_scene
    $ set_date(hour=15, minute=32)

    "As time passes, I can't help but feel satisfied."
    _mc turned casual eg "In two weeks I've managed to make new friends..."
    _mc ef "Reunited with an old friend..."
    _mc eg "And, most importantly, I feel like I finally belong somewhere."
    _mc ec mh "I won't see Yuri there for a while, but that's not the end of the world."
    _mc ea ma "Perhaps one day, she might trust me enough to lean on me a little more, but-"
    _mc eg "-In the meantime, I'll wait patiently. It'll come one day, I'm sure."
    $ add_calendar_description(_("Yuri returns"), day=13)
    "I look at my calendar, marking down the week when Yuri will return."
    _mc ec "Soon."
    
    $ persistent.yuri.mark_ending(1)
    return