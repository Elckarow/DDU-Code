label week_2_monday_sayori:
    call calendar_transition(day=30, hour=12, minute=12) from _call_calendar_transition_29
    $ autofocus.unblock("sayori")
    phone register "lit_club":
        time hour 8 minute 2 day True
        "s" "That sounds fine to me! Sleepover at 5pm, guys?"
        "n" "Works for me."
        "m" "Looks like I'll be able to attend!"
        "y" "As will I."
    scene black with Dissolve(1.0)
    scene bg music_class_day with sayori_pov(True)
    $ set_pov("s")

    "The door slides open easily as I gingerly meander inside."
    _s turned b1b e3c md "I feel like I'm about to be interrogated."

    play music pensive

    show monika turned mc at t11
    s e2a mh "... Hi, Monika."
    m rhip bc mb "Wow, who took the wind out of your sails today?"
    show monika ba mc
    s mn nb e3d b1a "Oh- Oh, nothing! I'm perfectly upbeat~"
    "She raises an eyebrow, but doesn't press it."
    _s na b1b e3c mj "Good job, Sayori. If she wasn't going to lecture you before, she absolutely will now."
    m eb mb rdown "Thanks for joining me, Sayori. I wasn't sure if you'd spare the time..."
    show monika ma
    s mh b1a e1a "It's Monday, so Natsuki has a student council meeting."
    m ea md "... What about MC? Wouldn't she want to spend time with you?"
    show monika mc
    s b1b e2a me "I..."
    show monika bc ec at dip
    "She frowns as she readjusts herself on the seat."
    m md ea bb "Everything alright?"
    show monika mc
    s e3c mh "... I don't know how to tell her."
    show monika ma ba ec at dip
    "Monika taps the bench, offering me to sit down."
    show monika ea mc
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("monika")
    "I oblige her, though a little reluctantly."
    s mg e2a b2b "I've known for so long that... It just aches, Monika."
    s mh b2a e1a "I don't want to make her worry."
    m lpoint md "You can't hide it from her forever, Sayori."
    show monika ldown mc with say_dissolve
    s mj e2a "..."
    m bc md "The longer you put this off, the more it will come as a shock."
    show monika mc with say_dissolve
    s mb b2a "But if I... If I leave her in the dark, maybe a time will come where-"
    m nb md "Sayori, listen to yourself."
    m ba na "What if it was her mother?"
    m rhip bc "Would you want to be told, or would you want to keep it a secret?"
    show monika mc with say_dissolve
    s b1b mg "... I would want to know."
    m rdown ba md "Then..."
    show monika mc with say_dissolve
    s b1a mh "I'll tell her when I get the chance."
    show monika ma with say_dissolve
    "Monika smiles at me warmly."
    _s e1a b1b md "I know she means well, but..."
    m md "Something else is bothering you, isn't it?"
    show monika mc with say_dissolve
    s e2a "..."
    m eb md "We don't have to talk about it-"
    show monika ea mc with say_dissolve
    s mh b1a e1a "No, it's probably best."
    s e2a me "I've been..."
    s b1b mg "I haven't been sleeping well."
    m md rhip "Nightmares?"
    show monika mc with say_dissolve
    s md e3c "Mhm."
    s e2a me "They feel so..."
    show monika rdown bb with say_dissolve
    s b2b nb e2b mg "And worse, when I have them, it's always-"
    s me "..."
    s e2a na mg "I've started to..."
    "I stumble a little over myself, lost as to how to start."
    show monika ba with say_dissolve
    s b1d e3c mm "I'm sorry, I shouldn't have said anything-"
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I move to stand up, expecting her to stop me."
    $ autofocus.unblock("monika")
    m rhip bc ec md "... If that's how you feel."
    show monika mc
    "... Only she doesn't."
    s b1a e1a md "..."
    show monika ba ea
    s e3c b2b mb "Thank you. For trusting me."
    show monika ma rdown
    "Her smile is reassuring enough for me."
    "I take a deep breath, once more searching for the words."
    s b1a mh e1a "... Sometimes, I swear I can hear those voices while I'm awake."
    $ autofocus.block("monika")
    m eb mc "..."
    "She doesn't look my way, pondering my words."
    $ autofocus.unblock("monika")
    m md "Have you talked to Natsuki about it?"
    show monika ma
    s e2a mg "... You know how she is."
    m ea md "She'd be worried about you?"
    show monika mc
    s b1b e3c mh "No, she'd take it seriously-"
    m rhip md bc "{i}Because{/i} she's worried about you?"
    show monika ea ba
    s e2a md "..."
    m eb md "If you're... hearing things, maybe you should go see someone."
    show monika mc
    s mb "... You sound like Natsuki."
    m rdown ea mb "Maybe that's because we both care about your wellbeing?"
    show monika mc
    s e2a mg "... Maybe you shouldn't."
    camera master:
        align (0.5, 0.2) zoom 1.7
    show monika ea ba
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("monika")
    "Monika places a hand on my shoulder."
    m md "Sayori..."
    m mb ec "Please don't say that. You're our friend and we're going to fuss over you."
    show monika mc with say_dissolve
    s me "I never asked you to..."
    m bc ea md "No, but that doesn't mean we don't care."
    show monika mc with say_dissolve
    s e3c b1a mh "... That's exactly what she said."
    m ba mb "If you're feeling deja vu, then maybe that's supposed to tell you something."
    show monika ma with say_dissolve
    s e2a "... I'll consider it. After the festival."
    m md "You'll see someone?"
    show monika mc with say_dissolve
    s mg b1b "... Maybe."
    m md bb "Can it really wait that long?"
    show monika mc
    s e3c mg "... I won't go before."
    m eb md "I..."
    show monika mc with say_dissolve
    s b2a mb e1a "This festival is important to you, Monika. I owe it to you to make sure I'm there."
    m ea md "Sayori..."
    show monika mc with say_dissolve
    s e3c b2b mb "Just... Please trust me."
    m ec mb "... Alright."
    show monika ma with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She nods, letting me stand."
    show monika ba ea
    s mh b1a e1a "I can still tell the difference."
    s e2a mg "If that ever changes..."
    show monika bb
    s me b1b "Then maybe."
    $ autofocus.unblock("monika")
    m rhip mb "... Remember to talk to MC."
    show monika ma 
    s e3c mg "... When the moment is right."
    m ba md "The longer you put it off..."
    show monika mc
    s e1b b2a me "Don't. Please... Don't say it."
    show monika eb rdown
    "I feel my lips quiver at her words."
    _s b2b mj e1a "I don't want her to say it. I don't think I could survive if she did."
    _s e3c "I won't lose her. She'll be alright."
    _s ma "She has to be."

    stop music fadeout 3.0
    scene bg school_street_afternoon with mc_pov(True)
    $ set_pov("mc")
    $ set_date(hour=16, minute=45)
    play ambient ext_day fadein 2.0
    
    "As we walk home, a strange calm washes over me." 
    show sayori turned e2a:
        matrixcolor TintMatrix("#ffeede")
        t11
    "Sayori's by my side." 
    "I mean, she has been for a full week now, but..." 
    "I just feel..." 
    "Safer. More secure, when she's here with me."
    s mg e1a "Hey, Melly?"
    show sayori md
    mc turned ml "Yeah?"
    "Part of me wonders if she wants to talk about the sleepover she organised while I was asleep, but I don't think that's the case."
    s b1b e2a mg "Did..." 
    s mh e1a lup b1a "Did you want me to come over for dinner again tonight?" 
    show sayori md with None
    _mc ec mh "Yeah, I thought not-" 
    extend eb mf bb "Wait, what did she say?!"
    show black:
        alpha 0.0
        linear 0.2 alpha 0.5
    "I open my mouth to respond, but my cheeks flush before I can muster it." 
    "My thoughts rush back to this morning, when I woke up with Sayori." 
    "Will that happen again?" 
    "And, a better question, do I want that to happen again?" 
    hide black with NonBlockingDissolve(0.2)
    mc mg ea ba "Ah, you can do whatever you want, Sayori. I already inconvenienced you by inviting you over last night." 
    show sayori e2a ldown b1b 
    "Sayori seems to contemplate my words." 
    s e1a b1a mb "Yeah, alright. Nothing that fancy, alright?"
    show sayori ma
    mc ef mb "Ah, sure. That was..." 
    "Honestly, I'm not sure what that was, myself." 
    s mb rup "Alright, should we do some shopping on the way home then?" 
    show sayori ma
    mc ed md "Oh yeah, sure~"
    extend ea mg " That would be pretty smart." 
    "Grabbing out my wallet, I search for the remaining cash." 
    "Hmm, a couple lucky bottle-caps, ten cents..." 
    "An electronic lock for the door at work..." 
    "Ah! There it is." 
    "I pull out the largest thing I can find." 
    show sayori rdown md
    "My grin disappears as I actually process what I hold in my hand." 
    mc bg eh md "Ah, we might just have to have leftovers tonight, I think." 
    "I dejectedly placed the two-hundred yen coin back into my wallet." 
    mc mb ed "Sorry, I don't get paid until tomorrow, so I've got nothing on me." 
    mc ea ba ml "I could run down to the bank, but that's in the opposite direction..."
    s mh "That's alright, I've got a little bit. Maybe we should just order some cheap pizza or something?" 
    show sayori ma
    mc "Are you sure?"
    mc ef mg "I don't usually eat takeout. It's not exactly healthy..." 
    s mh e1b "Oh, ah, of course!" 
    s mb e2a b2b "I don't eat takeout either, silly me..." 
    show sayori ma
    "Sayori quickly turns away from me." 
    "Did I say something wrong?"

    scene bg s_house_afternoon 
    show sayori turned nb md e2a b1b:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with wipeleft_scene

    "The rest of that walk home, after that, felt pretty awkward, all things considered." 
    "I feel pretty rough having for done that to Sayori; after all, she was just trying to help." 
    _mc turned ec mh "Hell, I would have enjoyed some pizza tonight, myself." 
    _mc thinking ea "Maybe I should treat her to some tomorrow for dinner, after I get paid?" 
    mc ldown ml "So, Sayori, did you want to-" 
    s mg "Ah, I think I might..." 
    s me "Eat alone tonight." 
    s mh na "Thanks for the offer though, Melly; I do appreciate it, and I do like spending time with you."
    show sayori md at thide
    hide sayori
    "With that, she walks to her front door, opens it, and walks inside, without another word or even looking back." 
    mc ef ml "Yeah, I deserve that."
    "I head inside. It's going to be a long night."

    $ add_calendar_description(calendar_descriptions["sayori"][4])

    call week_2_tuesday_sayori from _call_week_2_tuesday_sayori
    return