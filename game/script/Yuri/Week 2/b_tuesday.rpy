label week_2_tuesday_yuri:
    call calendar_transition(hour=6, minute=0, day=31) from _call_calendar_transition_42
    scene black with Dissolve(1.0)
    $ set_pov("m")
    scene bg m_bedroom_day with monika_pov(True)
    $ auto_nat_cut = True
    $ set_internet(True)
    phone register "mc_m":
        time auto True
        "mc" "I won't be coming today. Sorry."
    play ambient ext_day fadein 2.0

    "As I wake up, I quickly notice the change in temperature." 
    _m turned casual mc "Hmm, that's right. Today is warmer than this month is supposed to be."
    _m eb "They said that on the news yesterday."
    _m bc ec "Well, we might as well have a fun day today then..."
    _m ea "I just hope the club can get past what happened yesterday."
    "As I look at my phone to check the time, I notice a notification."
    m ba "..."
    "It's Melody."
    phone discussion "mc_m"
    m md bb md "Melody..."
    _m mc "Is this my doing?"
    "A touch of guilt wavers in my heart."
    phone end discussion
    _m md ec bc "Ugh, snap out of it Monika!"
    _m ea mc "This is something only Yuri can tell her."
    _m eb "But..."
    _m ba "Why hasn't she?"
    _m ea "They seem close..."
    _m bc ec "Hmm."
    "Putting the matter in the back of my head, I do my usual routine and head off to school."
    
    stop ambient fadeout 2.0
    scene bg class_2_day:
        xzoom -1
    with longfade
    play music school
    $ set_internet(False)

    t "To start, here's a warm up question to today's subject."
    t "What do you need to get from ten, to ten billion in one swift move?"
    t "And what, would such a scale be called?" 
    t "I will give you ten minutes."
    _m turned ec bc mc "Hmm... Maths, not my favourite subject, but not the most difficult either."
    _m eb ba "That would go to either literature or biology, in my opinion."
    _m ma "Sayori on the other hand..."
    _m ec bc "She probably disagrees."
    show sayori turned e1b b1d mj at t11
    "Sayori, sitting next to me, stares at the blackboard reading the questions over and over again."
    "As I glance at her notebook, I see incomprehensible mumbo jumbo supposedly being Sayori attempting to solve the questions."
    m ea md ba "Want my help...?"
    $ autofocus.block("sayori")
    s e1a b1a md "..."
    show sayori me
    "She bites on her pencil."
    s e2a "Uhm..."
    s mj e3c b1d "..."
    $ autofocus.unblock("sayori")
    s e2a b1a mg "Yes please..."
    show sayori md
    m mb "Alright."
    show sayori e1a 
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    m md "So, ten and ten billion sound very similar to each other, right...?"
    s mg "Yeah?"
    show sayori md with say_dissolve
    m mb "It's a scale, as the teacher said."
    m md "What is this scale called, Sayori?"
    s "..."
    s tap bc ma "I feel like i've read the answer somewhere...."
    "She pouts at me."
    m bc "It's called a logarithmic scale."
    m mb ba "And, what do logarithmic scales use?"
    s eb ba md "I uh..."
    s turned lup e3d mb "... Yeah."
    show sayori e2b b2a ma with say_dissolve
    "I sigh."
    show sayori md e1a b1a ldown with say_dissolve
    m mb "It's on page 110."
    show sayori me with say_dissolve
    m md "You studied it right?"
    s e1b ml "Wha-"
    s b2c e1a mk "Was that for today?"
    show sayori mj with say_dissolve
    "I nod."
    _m ec mc "Now I know why she always has such difficulty with maths..."
    show sayori b1d e1b md with say_dissolve
    "She rustles through the pages, eventually reaching page 110."
    s lup rup mi b1a "O- Oh! Oh!"
    s ldown rdown e1a mb "By using exponents!"
    show sayori ma e3d with say_dissolve
    m ea mb "Correct!"
    m md "And, if you use that knowledge..."
    show sayori lup e1b b1d mj with say_dissolve
    "Before I was able to finish my sentence, Sayori grabbed her calculator and punched in numbers."
    camera master:
        zoom 1.7
    show bg:
        blur 2.5
    with Dissolve(0.2)
    "Looking closer, I see she's manually checking every number..."
    m "Sa-"
    s me "{size=-7}No, it's not five...{/size}"
    m nb "Sayor-"
    s mm e3c "{size=-7}Not 8 either...{/size}"
    m bc "Sayori!"
    s rup e1b b1a mi "Booyah! The answer is ten!"
    show sayori ma with say_dissolve
    m na eb "That's correct..."
    show sayori e1a rdown ldown with say_dissolve
    m ea ba "But Sayori..."
    s mb "Yes, Monika?"
    show sayori ma with say_dissolve
    "Having the proudest smile on her face, I hate having to break it."
    camera master:
        zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    m bb mb "Can you count how many zeros there are after the ten on ten billion?"
    s b4 mh "What for?"
    show sayori md with say_dissolve
    m ba ec "You'll see."
    s mh b1a "One... Two..."
    s mg "Five... Six..."
    s me "Eight... Nine..."
    s md "..."
    s e2a b2a mb "Ten."
    show sayori ma with say_dissolve
    m ed "Ten to the power of ten."
    show sayori b2b e3c mj with say_dissolve
    "She puts her face onto her desk."
    s mh "Why does maths always taunt meee...."
    show sayori md with say_dissolve
    "I give her a pat."
    m "You'll get there one day. Don't worry."
    "As the class continues, so does Sayori's eternal struggle."
    
    stop music fadeout 3.0
    scene bg club_day:
        align (0.0, 0.8) zoom 1.9
    camera master
    show yuri turned md e2a at i42
    with longfade
    play ambient int_day fadein 1.0
    $ autofocus.unblock("sayori")
    $ say_transition = False

    "As I enter the literature club late, I see Yuri sitting all alone at her desk, calmly reading a book."
    "No Melody in sight."
    "While she may be a new member, her being away..."
    "Does quiet the atmosphere."
    show natsuki turned lhip cut_b e2a md at i11 onlayer above_master
    show bg club_day as stuff onlayer above_master
    show white_flashback onlayer above_master
    camera above_master at flash
    "That's when it hits me again, a flashback of Natsuki standing there, with blood on her face."
    $ clear_layers("above_master")
    show bg:
        align (1.0, 0.6) zoom 1.8
    hide yuri
    show natsuki cross e2a md at i44
    with Dissolve(0.2)
    "In the corner of my eye, Natsuki seems as calm as ever."
    _m turned bc mc "What truly happened yesterday?"
    "I decide to approach her."
    show natsuki e1a at i43
    camera master:
        align (0.65, 0.25) zoom 1.4
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ autofocus.block("sayori")
    $ say_transition = True
    "From up close, the cut from yesterday is still slightly visible." 
    m mb ba "Hey, Natsuki."
    n turned b3a mh "Oh, hey Prez."
    show natsuki mj with say_dissolve
    m md "Can we talk for a second?"
    n b1a "..."
    "Natsuki raises her eyes, her instincts seem to be kicking in."
    n e2a mg "About what?"
    show natsuki me with say_dissolve
    m bc md "Yesterday."
    n md b1d "..."
    "Natsuki grimaces."
    n mg "... Yuri, she..."
    n e3c mh "... She did it again."
    show natsuki mj with say_dissolve
    "I nearly take a step back out of shock."
    m bb md nb "... Oh God..."
    m ba "And you tried to...?"
    n lhip e2a b1a mg "Yep."
    show natsuki md with say_dissolve
    m na bc eb "That explains it..."
    m ea bb mb "Sorry you had to see that, Natsuki..."
    n e1a mg "It's fine, I've had worse." 
    n ldown e3c b2a mb "Yuri is my friend too."
    n cross b3a e2a mh "I just hope Melody isn't making it worse."
    show natsuki e1a me with say_dissolve
    "Natsuki pauses, glancing at me directly."
    n mg "Speaking of Melody..."
    n turned b1a mh "Where is she?"
    show natsuki md with say_dissolve
    _m ea bc mc "..."
    m ba mb "{i}MC's{/i} at home, she called in sick."
    n e1d b1d me "Hmm."
    n mg e2a "Figures."
    show natsuki b1a e1a md 
    show sayori turned lup rup e1b ml at i42
    with say_dissolve
    s "H- Hold on, did I hear {i}my{/i} Melly is sick?"
    show sayori mk with None
    camera master
    show bg:
        blur 0.0
    show sayori at i43
    show natsuki at i44
    with Dissolve(0.2)
    $ say_transition = False
    _m ec bc mc "Sayori, eavesdropping as always..."
    m eb ba md "Yeah. Let's hope she feels better soon."
    $ autofocus.unblock("sayori")
    s rdown mg e2a b2a "And on such a hot day too..."
    s ldown mh e3c b1d "That's no fun."
    show sayori mj
    m bb "Yeah..."
    show sayori b1b e3a md
    "I can see Sayori glimpsing at Natsuki's cut."
    show sayori b1a e3c mj
    "But, she doesn't say a thing."
    _m ec ma ba "Sayori's unwavering optimism, her instinct to avoid anything unfun, I am guessing."
    show sayori e1a md
    "..."
    m md ea "Well, I have nothing planned today, so..."
    m mb "Do what you'd like to do... like reading!"
    show natsuki ma at thide
    s mb "Okay, Monika!"
    hide natsuki
    show sayori ma at thide
    hide sayori
    _m eb mc "And in the meanwhile..."
    show bg:
        zoom 1.0
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    _m bc "I will speak to my friend."
    show sayori turned lup mh at t11 
    s "Oh, and Monika?"
    show sayori md
    "Sayori calls out to me, breaking me from my thoughts."
    m md ba ea "Hmm?"
    s ldown mb "You should relax every now and then too, you know!"
    show sayori ma at thide
    m mb "Ah... One day, Sayori."
    hide sayori
    m ec bc md "{size=-10}... One day...{/size}"
    show bg:
        blur 2.0 align (0.0, 0.8) zoom 1.9
    camera master:
        align (0.5, 0.1) zoom 1.5
    show yuri turned e2a md at i42
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "Leaving Sayori to read, I head to Yuri, still sitting alone."
    m ea ba mb "Hey, Yuri."
    y e1d lup mg nb "H- Hello."
    show yuri md na with say_dissolve
    m md "I'd like to talk to you, if that's fine with you."
    show yuri me with say_dissolve
    m eb "Somewhere private."
    show yuri b1d e2c md with say_dissolve
    "Yuri's eyes glance around the room nervously."
    y b2b mg "I... don't think-"
    show yuri b1a e1d md with say_dissolve
    m ea bc md "Yuri, it's important."
    y b2b rup e1a mg "Can't we-"
    show yuri e2a md with say_dissolve
    m ec "No."
    show yuri b1b me rdown with say_dissolve
    "Yuri sighs deeply."
    y e1a mb b1a ldown "Alright."
    show yuri md with say_dissolve
    m mb bb ea "Thank you, Yuri."
    m ea ba "Do you have a place in mind, or should I choose?"
    y me "..."
    y e2a "..."
    show yuri md with say_dissolve
    "Seeing her indecisiveness on her face, I decide to choose instead."
    show yuri e1d with say_dissolve
    m lpoint "How about an empty classroom?"
    show yuri b4 with say_dissolve
    "Yuri glances at me, confused."
    y lup mh "Don't you need keys for those...?"
    show yuri b1a me with say_dissolve
    m ldown ed "Mhm. But I have those keys."
    m ea "Being a club president has its perks, you know."
    y mb e1a ldown "Alright, lead the way..."
    show yuri ma with say_dissolve
    hide yuri
    show bg:
        blur 0.0 zoom 1.0
    camera master
    show sayori turned lup at i21
    show natsuki cross e2a mj at i22
    with Dissolve(0.2)
    $ say_transition = False
    "Telling Sayori and Natsuki we'll be right back, we leave to head to a few classrooms over."
    
    scene bg class_2_day:
        xzoom -1
    with wipeleft

    "As we enter the room, it is impossible to not notice the silence."
    show sky_day at moving_sky zorder 5 with NonBlockingDissolve(1.0)
    "We stare out of the window, seeing the outside world having the same busy lives as us."

    stop ambient fadeout 2.0
    play music faith fadein 2.0

    # Voice acting thing
    m turned md eb "Yuri..."
    hide sky_day
    show yuri turned md lup at i11
    with Dissolve(0.5)
    m ea mb "How well do you know MC?"
    y "..."
    $ autofocus.unblock("yuri")
    y b4 mh e1d "I... think I know her on average..."
    show yuri md
    m md "On average? What do you mean?"
    y e2a b1d mh "I feel like I know her... decently well, or... something like that..."
    show yuri md
    m bc "... Yuri, I think you two have gotten to know each other a {i}little{/i} better than that."
    m mb bb "... MC is concerned about you."
    show yuri mj b1a e1b
    "Yuri seems to recoil, as if she wasn't expecting to hear that."
    y mg "But, why?"
    y ldown mb e2a b2a "It's not like she-"
    show yuri me e1b at hop
    m md "Yuri."
    show yuri e1d b1a md
    "..."
    m mb ba "Haven't you noticed how she always goes to you on normal days?"
    m md "Can't help but glance at you?"
    y e3c mb b1d "Monika, I am trying to..."
    show yuri lup e2a b2b ma
    "Yuri grimaces."
    y mg "It's just, it's so difficult."
    y e3c mh "These... panic attacks I've been having."
    y mk e2a "They don't just prevent me from talking to people."
    y mm e2c b2a "They make me so nervous... All the time."
    y e3c b2b mk "Including around MC."
    y e2a rup b2a mh "Sometimes, when I look at her, I feel like she's judging me..."
    y mk "I know she isn't, but-"
    show yuri mj e1a b2b nb
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("yuri")
    "I put my hand on Yuri's shoulder, comforting her."
    m bb mb "Yuri, It's alright."
    m ba md "MC is just... confused, and just wishes to understand you better."
    m bb mb "... Especially after yesterday."
    y ldown rdown b2b e2a md "..."
    "I sigh, preparing to explain it to Yuri differently."
    "..."
    m ba md ".... Have you noticed that she's not here today?"
    show yuri e1a with say_dissolve
    "..."
    m eb bc "There's... a reason for that."
    y md b1a e1d "...?"
    m ea "She asked me about {b}you{/b}."
    m eb ba "Wanting to know... what's been going on."
    m bb "I know it might be hard for you, but..."
    "..."
    m ea mb "Could you tell her about it?"
    m ba md "About your panic attacks, and what causes them?"
    y me "I..."
    show yuri md with say_dissolve
    "..."
    show yuri e1a b1d mj na with say_dissolve
    "Yuri then glares at me, like I've offended her."
    y mg "Monika."
    y e3c mh "I don't want to."
    y e2a lup "You of all people should know this, but..."
    y b2b mg "It hurts so much just {i}thinking{/i} about it."
    y e3c mk "Let alone talking about it."
    y mh e1d b1a "Would MC even understand?"
    y ldown e1a b1d nb "Would she still want to spend time with me?"
    y b1a e1b mi "... I really don't know...!"
    show yuri b3d e1d mj with say_dissolve
    m bb "Oh, Yuri..."
    show yuri e2a b1d na with say_dissolve
    m mb "It's like you said- you did tell me."
    show yuri b2b md with say_dissolve
    m ed ba "And we're better friends now than ever before, right?"
    y e1a "..."
    y mb e3c lup rup "But... Monika, you are... special."
    show yuri ma with say_dissolve
    _m mc ea "... Special?"
    _m nb "... What is she trying to say...?"
    m md "What do you... mean?"
    y rdown e2a mh "You've always been there for me..."
    y mk e3c "So..."
    show yuri e1a md with say_dissolve
    m mb "That's just who I try to be, Yuri."
    m ed "Someone who supports others."
    m bc na eb md "But, this isn't about me."
    m ea "This is about you and Melody."
    y ldown e2a b1d mh "I... suppose."
    show yuri md with say_dissolve
    m mc "..."
    y "..."
    show yuri me e3c with say_dissolve
    "Yuri lets out another sigh."
    y e1a b1d mh lup "I don't want to tell someone simply because they want to know."
    y e2a mg b1a "While I appreciate her company and that she's taken an interest in me..."
    y mh ldown b1d "That doesn't entitle her to my..." 
    y mg e3c "... My vulnerabilities."
    y lup e1d mh b1a "Do you remember how long it took for you and I to form this connection of ours, Monika?"
    show yuri md e1a b1d with say_dissolve
    m eb md "... Yes."
    y mg b1a e3c "It took a long time for me to warm up to you, to share myself with you..."
    y ldown e1d b3d mi "Now, you're asking me to express these things to MC, in a tenth of the time?"
    show yuri mj with say_dissolve
    m ec mb "...You're right."
    m bc md "That is unreasonable."
    show yuri e1a b1d me with say_dissolve
    m eb bb "I'm..."
    m ea mb nb "I'm sorry for putting the burden of that decision on you, Yuri."
    show yuri e2a md with say_dissolve
    "I swallow the dry lump in throat, trying my hardest to put on a smile that would comfort her."
    y b2b "..."
    y e3c me "No..."
    y e2a b1a mg "Thinking back on it..."
    y mh b1d "I think you're right."
    y md "..."
    y mg e3c "She trusts me. Wants to get closer."
    y e2a b1a mh "Like that time she told me about her living conditions."
    y b1d mg lup "I- I won't go into detail, but..."
    y me "..."
    y mb lup rup e3c b2b "No, you're right. I apologize..."
    y rdown e2a mg "For... rambling on."
    show yuri ma ldown with say_dissolve
    m md na "You don't need to apologize."
    m eb "This is difficult, I understand."
    m mb bb ea "And... don't ever feel guilty for sharing your thoughts."
    m ba "Let her know what you think."
    show yuri e1d md b1a with say_dissolve
    m md "Even if it feels difficult, know that we are all by your side."
    m ec mb "There's no need to fear."
    y e1a b2b mb nc "T- Thanks, Monika."
    show yuri ma with say_dissolve
    "I give a smile."
    show black: 
        alpha 0.5
    with NonBlockingDissolve(0.5)
    _m mc ba ea na "While Yuri finds social interaction difficult..."
    _m ec ma "She has to know that there's only one remedy to survive hardships:"
    _m ea "Doing what you think is right."
    _m mc "Even if it takes more effort than ever."
    _m ec "I hope she'll show Melody that sentiment soon."
    _m bb "To let her know..."
    _m bc ea "But, we'll see."
    _m ma eb ba "I think Melody will understand."
    
    scene black
    camera master
    with Dissolve(0.5)
    $ say_transition = False
    $ autofocus.unblock("yuri")

    "As we talked and talked about several topics, like..."
    "The festival... books... my plans for the next few days..."
    "A smile slowly appeared on her face as well."
    "And that..."
    "Makes me happy."

    $ add_calendar_description(calendar_descriptions["yuri"][6])
    
    return