label week_1_sunday_natsuki:
    call calendar_transition(day=29, hour=15, minute=40) from _call_calendar_transition_17
    scene bg mc_living_room
    show bg mc_living_room as stuff:
        align (0.35, 0.2) zoom 1.7 alpha 1.0
        on hide:
            ease 0.3 alpha 0.0
    with dissolve_scene_full
    $ autofocus.unblock("sayori")

    play music rgb

    "A lazy day, is what I called it."
    "Normally I’d be out doing things on a day like today, or studying for any upcoming assessment, but I just don’t have the energy."
    _mc turned mh casual "It’s strange. I almost always have enough drive to get things done, but today? Like yesterday, I can hardly get up off of the couch."
    _mc ec thinking "Perhaps I should at least attempt to see if anyone is free?"
    _mc ea ma "Amelia might be; she doesn’t stream every Sunday."
    play sound phone_notification
    "I reach for my phone, only for it to buzz as I pick it up."

    phone call "am"
    phone_mc "Speak of the goddamn devil..."
    phone_am "Hey. Just wanted to see if you were up to much this afternoon."
    phone_mc "Nah, not really. Just relaxing, for the most part."
    phone_am "Well, wanna have a late lunch?"
    phone_am "My shout~"
    phone_mc "I hate how you know exactly how to get me up."
    phone_mc "-Out. I mean out of the house."
    phone_mc "Not up, or like, I mean, I was lying down, so it’s technically right, but-"
    phone_am "Relax~ I get it. C’mon. I know I can always entice you with free food."
    phone_am "Meet me by the arcade at 4:30, and wear something nice, alright?"
    phone_mc "I’m always wearing something nice. It’s called my own skin."
    "I can most certainly hear her chuckle over the phone."
    phone_am "Sure, sure. See you shortly, narcissist."
    phone_mc "Hey, if anyone’s gonna love me, it’s gonna be me."
    phone end call

    hide stuff
    "With that, I sit up."
    _mc ldown ec "I should probably get ready, yeah?"

    scene bg city_street_2_afternoon
    show amelia turned casual rpocket ed md lup:
        matrixcolor TintMatrix("#ffecdb")
        i11
    with wipeleft_scene
    $ set_date(hour=16, minute=21)
    $ set_internet(False)

    _mc turned coat_casual "Ah, there she is. Dressed up, I guess, in her own way."
    _mc ef mh "It probably shouldn’t be all that surprising, but for some reason, I’ve never actually seen her in anything nice before."
    _mc ec "... Makes me wonder what she does with all of the money she earns; if she was smart, she’d be saving it, like I told her to all those years ago."
    show amelia eb
    _mc ea ma "By now, who knows how much she’s saved. I suppose that’s why she’s willing to occasionally buy me food to win my attention."
    _mc ef "... I guess that says a lot about me, huh, that I can be bought with food."
    show amelia ea ma ldown rup
    _mc ea mh "Though, to be honest, it does make sense that I find myself in such a position. When we first met, we did end up going to a convenience store."
    _mc thinking ec mh "Wait, first met? No, that doesn’t seem quite right. I think it was after that. Strange, I can’t seem to remember."
    _mc ea ma "... Hah. Probably all the angst I had at the time clogging my memory."

    scene bg city_street_2_afternoon
    show melody turned coat_casual ef mh:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with amelia_pov()
    $ set_pov("am")

    _am turned casual eb md "She’s just... standing there."
    _am ec "Granted, I’m not complaining, considering how epic she looks with the wind rushing through her hair, but..."
    am mh "Uh... You gonna talk?"
    mc ea mf bc "Oh, yeah, I just-"
    mc mb ba "Got thinking, you know?"
    show melody ma
    am eb me "I do, yeah."
    show melody mh
    am mb "You gonna tell me what about?"
    mc ef mj "Ah, no, it’s..."
    show melody ma
    "She shrugs. Probably nothing important; sometimes she just zones out."
    _am ec ma "Off in her own world, sometimes. Never seen anyone quite like it; makes her seem broody and mysterious at first, but once you get used to it? Just odd."
    show melody ea
    am eb mb lup "C’mon, let’s go and get something to eat. I’ve got a good place in mind."
    mc mb "Alright, lead the way."
    show melody ma

    scene bg restaurant_sushi
    with wipeleft_scene
    $ set_date(hour=17, minute=1)
    $ set_internet(True)

    _am turned casual ec md "Well, this looks about what I expected. "
    _am eb "It’s a reasonably expensive place, but there’s a decent amount of positive reviews, and I felt like trying some of the food here."
    show melody turned casual lback rback2 ef at t11
    _am ea ma "And, well... I didn’t want to go alone, so I brought along Melody."
    _am ed "She’s usually fine with this stuff, so I don’t really mind paying for her food. She doesn’t eat much, anyway." # im stuff
    show bg:
        blur 1.0 align (0.5, 1.0) zoom 1.35
    show melody ldown rdown:
        xcenter 0.58 ypos 1.0 yanchor 0.9 zoom 0.85
    camera master:
        align (0.75, 0.23) zoom 1.4
    with Dissolve(0.2)
    $ autofocus.block("melody")
    $ say_transition = True
    "A waiter strides over to us, leading us to our seats after a short introduction."
    show melody ea with say_dissolve
    "It doesn’t take us long to pick some food and place an order."
    "In the end, we’re left with quite a relaxing meal in front of us."
    mc mg "So... You come here often?"
    show melody ma ef with say_dissolve
    "She chuckles a little, looking around at the couples that frequent the surrounding tables."
    am ef mb bb "Nope, my first time."
    mc ed md "Hah, then I’ll be gentle~"
    show melody eh bb ma with say_dissolve
    "I roll my eyes. She’s obviously joking to brighten the mood, because there’s no way she would actually-"
    _am ba ed ma "Nah. This is Melody we’re talking about. She’s pretty straight, from what I’ve seen."
    _am eb md "Huh. Actually, come to think about it, I don’t know if she’s ever really been interested in anyone, outside of Sayori."
    _am ec "... Maybe she isn’t straight then?"
    _am ed ma "Not that it’s any of my business, though. Mel’s always been a little closed off, so I’d rather not pry."
    show melody ea with say_dissolve
    am eb mb "Either way, what do you think?"
    mc mg bc "It’s a lot nicer than I was gonna make for myself tonight, so..."
    mc ba mb "That’s a win in my book."
    show melody ma with say_dissolve
    am ed me "I’d hope so, at least. Considering how expensive this place is..."
    mc thinking mf "Is it that bad?"
    show melody mh with say_dissolve
    am mh "Ah, no, it’s definitely dearer than anywhere I’d go myself, though."
    mc ldown mf ef "Hm. So you felt like doing something different, right?"
    show melody mh with say_dissolve
    am ee bb mf "... Yeah, that’s about it. I dunno, sometimes I like a change of pace, of scenery."
    mc mg eg "Hm. I think I get that, but at the same time, I also wouldn’t mind being at home most of the time."
    show melody mi with say_dissolve
    am ba mb ec "That’d be the introvert speaking, Mel."
    show melody bb ma with say_dissolve
    "She chuckles a little."
    mc ea bc mb "True; I am pretty antisocial most of the time."
    show melody ma with say_dissolve
    am eb me "But hey, you’ve got this club now, right? Gonna go back next week?"
    mc ed mb ba "You bet!"
    show melody ma with say_dissolve
    am ec mb "And not just because of the cute girl there, right?"
    mc ea mh bb "..."
    "Seems I struck a nerve with my playful jab. I had a feeling it would; I don’t want to hurt her, but she’s clearly bottling something up-"
    _am md "-And I’d rather her take it out on me than keep it to herself."
    mc lback rback2 ef mg "No, not just because of her."
    mc mf eg ba "Besides, I..."
    mc ldown rdown ed mb "I made my choice years ago. I think I’d rather lie in that bed than bring those back to the surface."
    show melody ma with say_dissolve
    am eb me "... So you’re repressing your feelings?"
    mc ea bb mf "It’s not repressing them, it’s..."
    mc bi mg eg "I don’t know what it is. All I know is that I don’t feel the same way I did when I was a kid."
    show melody mh with say_dissolve
    am ec me "And you’re just interpreting those feelings as therefore not liking her anymore?"
    mc ba ef thinking "..."
    "She gives it some thought, mulling over my question."
    mc mf "Yeah. I don’t think I feel the same way, anymore. She’s not the same person, and neither am I."
    mc mh "..."
    am ed mh "Ah. I get it."
    mc bi mf "She’s not the same person."
    mc eg mg "She’s stronger, braver, and so much more than I remember."
    mc ldown ba ef mj "And I..."
    mc eg bi mb "I’ve only gone backward."
    show melody ma with say_dissolve
    am ea mb bd "... I don’t know what you were like then, but I do know that you’ve come a long, long way since we first met."
    show melody ea mh ba with say_dissolve
    am ef bb "You hardly wanted to be around me, back then. Now you’ve joined a club!"
    am eb me ba "Do you really think you could have done that back then?"
    mc mf eg "... Definitely not the Literature Club. Not if I’d known Sayori was there."
    show melody mh with say_dissolve
    am "She’s your best friend, right?"
    mc mb "Yeah. Yeah, she is."
    show melody ma ef with say_dissolve
    am ea mb "Then make sure she knows it. Make sure she knows you’re around to be her friend, not trying to get into her pants."
    mc mh "..."
    mc mf "Alright."
    show melody mh with say_dissolve
    "She looks away, gazing out of the window."
    mc mg "I wish life could just be..."
    mc eg bi mf "Different."
    mc ed ba mg "I don’t care how, I just wish that I could be strong enough to make things work, to make those I care about happy."
    show melody mh with say_dissolve
    am ee me "... A simultaneously selfish and selfless dream. Maybe one day you might get that chance."
    show melody ea ma with say_dissolve
    am ec mb "Though, you know what they say about wishes."
    mc eg mb "... Yeah. Be careful what you wish for, right?"
    show melody ma with say_dissolve
    "I nod. It makes me wonder what the future might hold for us."
    $ say_transition = False
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _am ed md "She’s wise, but lacks the ability and the motivation to develop her personability skills."
    _am eb "It makes me wonder how she’ll cope when she gets into the real world."
    _am ec "It also hurts that she gets such good grades."
    _am ee "Sure, she spends more time studying because she doesn’t have friends, but still..."
    _am ec "It’s not ideal that she has so little in the way of social skills."
    _am eb "I don’t even think she sees it, either. Maybe I’ll have to have a chat with her about it one day."
    _am ed ma "Yeah. That would be wise."

    scene bg mc_bedroom_night_closed_off:
        align (1.0, 1.0) zoom 2.0
    camera master
    with mc_pov(True)
    $ set_pov("mc")
    $ autofocus.unblock("melody")
    $ set_date(hour=21, minute=10)
    $ set_internet(True)

    _mc turned naked messy nostrands ec "Count on Amelia to know how to treat a girl, eh?"
    _mc ef mh "And I suppose a talk about our lives, too..."
    "Anyway, I find myself feeling restless now, just laying down in my bed and staring around the room."
    "That food from earlier's left me feeling pretty sleepy, yet I can't fall asleep."
    "Quite the contradiction."
    "I sigh, rolling over to my side for what must be the tenth time this past hour."
    play sound phone_notification
    "As I do, I suddenly notice a ringing noise."
    _mc ea "My phone? Who could be calling me at this time?"
    phone call "s"
    phone_s "Oh, you picked up! Goodie!"
    phone_mc "Yeah? What's up with you tonight?"
    phone_s "Shh, it's a super special secret..."
    phone_mc "Secret? Then why are you-"
    phone_s "You'll see!"
    phone_s "I'm going to message everyone in a group chat, so don't fall asleep on me!"
    phone_mc "Huh? How did you-"
    phone_s "Psychic~"
    phone_s "Okay, see you in a jiffy!"
    phone end call
    _mc ec "Well then..."
    _mc thinking ea "So she has something fun planned, I take it?"
    _mc ma "She definitely sounded pretty excited about her idea, whatever it is."
    phone discussion "lit_club":
        time auto True
        "s" "Who wants a sleepover at my place?!"
        "m" "Oh? That sounds like fun. When would it be? I would need to get permission."
        "s" "Hmmm"
        "s" "What about Saturday?"
        "n" "I think I should be able to do that."
        "y" "Oh? A sleepover? Whatever for?"
        "s" "Because we can, silly~"
        "y" "Just for fun? I don't see why not, then."
        "mc" "I dunno, I've got work that afternoon."
        "mc" "I might be able to come by after work?"
        "s" "Sure! Let's make it a 5pm start then, at my place."
        "m" "I believe I can organise that, but I'll let you know."
        "n" "Yeah, I think I can make that as well."
        "s" "Sweet! I'll see everyone there! Bring some snacks with you, and your stuff for sleeping. There's plenty of room!" # im stuff
        "mc" "Look at you, running away with the entire show. Geez, if you're gonna twist my arm, I'll be there."
        "s" "You're starting to sound like Natsuki!"
        "n" "I don't sound like that! Geez..."
        "m" "Alright, see everyone at club tomorrow! I look forward to this event!"
        "y" "Indeed."
    phone end discussion
    _mc ec mh ldown "Hm. Looks like Natsuki's still around, just not anywhere local. Good to know that she's not gotten 'hurt', as Sayori put it."
    _mc ef "I hope."
    "I sigh. Best not to worry too much about it, but I can't help the nagging feeling in the back of my mind."
    _mc ea "Just who is this girl who's inserted herself into my life?"
    _mc ec "And... Why does she act this way?"
    "A sleepover does sound fun though, honestly."
    "I've been hanging out a fair bit with Amelia lately, but it couldn't hurt."
    _mc thinking ea "Now that I think about it, why not invite Amelia too?"
    _mc ma "She's fun at parties. And it'd be a great way of introducing her to everyone else besides just Sayori."
    "..."
    _mc ec mh "Nah, on second thought, I don't think she'd be the type."
    _mc ef "That, and she's probably really busy with her job too."
    _mc ldown "I guess I could always send a message to her..."
    phone discussion "mc_am":
        time auto True
        "mc" "Hey, Meelz."
    "..."
    _mc eg "I guess she's still busy with one of her streams right about now."
    phone discussion:
        type "am" value 0.5 delay 0.2
    _mc ea "Oh, wait, she's typing now."
    phone discussion:
        "am" "Yeah? That dinner outing fill you up?"
        "mc" "It did. Thanks for the offer, Meelz."
        "am" "No problem dude."
        "mc" "That said, I had something I wanted to ask."
        "am" "No, I'm not eating pockey on stream."
        "mc" "Not that, though that'd admittedly be funny to see."
        "mc" "See, Sayori invited the Literature Club out to a sleepover at her place this upcoming Saturday. You in?"
        "am" "You sure I wouldn't be intruding?"
        "mc" "Dude, you already met Sayori, and I can give a good word in for you with everyone else."
        "am" "Thanks for the support, Mel. Sadly, I promised my audience a livestream of that one camera horror game on that same Saturday..."
        "mc" "You can't make an exception? I'll be heading to Sayori's place right off of work, so..."
        "am" "Sorry, Mel. You enjoy the sleepover in my place, okay? Be sure to invite me to the next one though!"
        "mc" "You got it, man."
    phone end discussion
    _mc ec "Well, that's disappointing."
    _mc ef ma "I guess no Meelz to crash this sleepover."
    _mc ea "Hey, at least now you can't say I didn't try, eh?"
    _mc eg mh "I really need to get to sleep now."

    $ add_calendar_description(calendar_descriptions["natsuki"][4])

    call week_2_monday_natsuki from _call_week_2_monday_natsuki
    return