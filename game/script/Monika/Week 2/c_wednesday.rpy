label week_2_wednesday_monika:
    call calendar_transition(day=1, month=11, minute=30, hour=6) from _call_calendar_transition_8
    scene black with dissolve_scene_full
    $ set_internet(True)
    play sound_loop phone_alarm fadein 3.0
    pause 1.0

    "..."
    "..."
    "..."
    stop sound_loop

    play music hnt

    "I silence my alarm, again."
    _mc turned naked messy nostrands eg bi mh "I... I can’t, today."
    "Rolling over once more, I just the curtains to block out more light and squeeze shut my eyes."
    _mc mm "I can’t put to words how much I want this to stop."
    _mc bg mh "How much I want everything... to stop."
    _mc "How could I have been so stupid? I did this to myself."
    _mc "... Now Monika hates me."
    _mc "The club hates me."
    _mc bi mm "And I have no-one to blame but myself."
    _mc mh "I can’t remember the last time I was this emotional. It must be the club."
    _mc ba "... Yeah. The club got to me."
    _mc "Made me confused."
    _mc bi mm "Ugh. Pathetic."
    _mc mh "How could I let this happen? Let my guard down so much?"
    _mc ba "I was doing just fine, until Monika came along, with her charms and her wit, and her- Argh!"
    _mc bi "Fantastic. Just... fantastic."
    
    scene bg mc_kitchen_day with Dissolve(3.0, time_warp=_warper.ease)
    $ set_date(hour=16, minute=47)

    "At some stage, I must have managed to force myself out of bed - as I end up down in the kitchen, searching for a glass of water-"
    "-Only to find I’m not alone."
    show natsuki turned noband mg b3a e2a at t11
    n "You really need better security here."
    show natsuki e1a me
    mc turned naked messy nostrands bd eb nb ml "What the fuc-"
    show natsuki b1d e1b mm nb
    camera master:
        align (0.5, 0.25) zoom 1.6
    show bg:
        blur 2.3
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    "A hand covers my mouth, and Natsuki brings her finger to her lips."
    n mk "Shhh. Sayori’s only next door. You don’t want to alert the entire neighbourhood, do you?"
    show natsuki mm with say_dissolve
    mc eh mf "Mphhh!"
    n e2a mb "Okay, look, maybe you do, but hear me out!"
    n e1d na mh "At least promise to hear me out."
    show natsuki md with None
    show natsuki e3c b1a me 
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I slowly nod, and she removes her hand."
    $ autofocus.unblock("natsuki")
    n lhip e2a mh "Look, all I did was borrow Sayori’s key."
    show natsuki md b3a e1a
    mc eb mg bd "How the hell do you even know she has one?"
    n cross e1d b1d mh "... Really? She’s my best friend."
    n b3a e3c mi "I think you can put two and two together."
    n b1a e2a mh "Listen, though. There’s a problem."
    show natsuki md e1a
    mc ef bi mf "... I..."
    show natsuki e1d b1d
    mc ec na mg "I don’t want to hear it."
    n turned mg "No, I think you do."
    n mh b3a e1a "I talked with Monika, yesterday."
    show natsuki md
    mc ef ml "I know. She told me."
    n lhip rhip b1d e1d mh "... Oh. Then I’ll assume that’s why you weren’t at school?"
    show natsuki mj
    mc ba mg "No, I was just... sick."
    n rdown e2a b1a mh "Riiight. Look. Monika... She feels awful. I had a feeling she might have said something, but at the club today she almost didn’t look like she wanted to be there."
    show natsuki ldown e1a md
    mc bi ml "... Whatever happens at the club is..."
    show natsuki e1d b1d mj
    "She narrows her eyes."
    n cross mh "You’re not ditching her, right?"
    show natsuki mj
    mc mh "..."
    n e1b b3d mm "Not now, when she needs friends the most?"
    n mi "... Are you really that petty?"
    n b1d e2a mb "Actually, don’t answer that. History tells us that’s exactly what you are."
    show natsuki b3a mj e1a
    camera master at vpunch
    play sound slam
    mc eb bd mg nb "AND WHAT THE HELL WOULD YOU KNOW?"
    show natsuki turned b1d 
    "Instead of recoiling at my outburst, Natsuki stands strong."
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    n mg lhip rhip "Because you did it to my best friend."
    n e1d mi "You caught feelings, and then cried about it when they weren’t reciprocated."
    n e1a b3a mh "You don’t think I don’t know what that’s like?"
    n b1d mm e1b "You think I’m just some stupid kid who knows nothing of how people think? Well, newsflash, I’m not. I’ve seen it all. I don’t know what you take me for, but I’m not."
    "Whatever hostility I might have held has since vanished, replaced by a quiver in my lips."
    n cross mi e1b "You hurt her, more than you, or I, could possibly ever understand. And I was the one dealing with that fallout, you know? That was ME. I picked up the pieces of someone who was absolutely shattered. Shattered by you."
    n turned ldown rdown mh b3a "I did it out of respect for who I thought she cared about. Someone who, according to her, didn’t do anything wrong."
    n e1d b1d mi "But look at you. You’re a sad, lonely loser who doesn’t give a damn about anyone except herself."
    show natsuki mj with say_dissolve
    mc bi ef mh "..."
    n lhip rhip e1a mi "Take some responsibility and wear some of the blame, for once, instead of just pretending to."
    n cross e1d mh "Go face Monika, properly. If she won’t take you as a partner, you better make damn sure she’ll see you as a friend. And you better be good to her. She deserves better than what you did to Sayori."
    show natsuki mj with say_dissolve
    mc bg "..."
    n b3a e1a mh "Life isn’t about falling in love. It’s about taking the people you care about and helping them to become stronger. Love is selfish; care is selfless."
    n turned b1a mb "Show her you care."
    n b1d mh "Maybe then, {i}maybe{/i}, she might one day return those feelings, but don’t ever count on it. Help her because you want to be her friend, not because you want anything from her. She owes you nothing."
    show natsuki mj with say_dissolve
    mc na mf "... I-"
    show natsuki md b1a with say_dissolve
    mc eg mb na "I know. I know that, but I..."
    mc ef mg "How do I help her, when she thinks that I..."
    n b3a mh "When she thinks all you see her as is a love interest? You prove to her that you can be her friend."
    show natsuki ma with say_dissolve
    mc mh "..."
    mc mf "I’ll... try."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("natsuki")
    n e3c mb "Good. Because she’s waiting outside for you."
    show natsuki ma
    mc bb eb nb mg "Wh- What?"
    n lhip e3a mc "Go pay Sayori a visit. You’ll find her there."
    show natsuki ma e1a
    mc ea na mh ba "..."
    show natsuki md
    mc ef mf "I don’t know if I..."
    n lhip rhip e1d b1d mh "No more excuses."
    show natsuki mj
    "I breathe deeply."
    _mc ec bi mh "Maybe it is time to change some bad habits."
    show natsuki e1a b1a ma
    mc mf "Alright."
    mc ea ba mg "I’ll go talk to her."
    n ldown rdown mc "Good."
    show natsuki md
    mc ec bi ml "... How much of this did you plan out?"
    n cross mb e1d b1d "Hm. You think this was my idea?"
    show natsuki ma
    mc ef ba ml "... Sayori."
    n b3a e3d mo "Nail on the head."
    mc mb "I’ll have to thank her, then."
    n e1a mh "Oh, and, before you go out there?"
    n b1d e2a nc mb "Put some clothes on."
    show natsuki ma
    _mc eb bb nd mh "!!"
    _mc mj "Oh, god!"

    stop music fadeout 2.0
    scene bg s_living_room with longfade
    $ advance_date(minutes=10)

    "After clothing myself, I walk over to Sayori’s."
    _mc turned casual messy nostrands ec mh "Now..."
    _mc ea "I’m standing here, alone."
    _mc "Sayori let me in, then rushed upstairs to grab her."
    _mc bg nb eg "God, I’m nervous."
    _mc eb bf "What do I do? What do I say?"
    _mc eg ba na "... She doesn’t like me. All I need to do is try and make it seem like it was nothing, let the issue blow over."
    _mc ec "Maybe, just maybe, it’ll work out in the future, but I can’t bank on that. Like Natsuki said, I need to prove I can be a good friend. I need to win that trust back."

    play music dawn fadein 1.0
    
    show monika turned nb mb eb bb at t44
    m "Hey."
    show monika ma
    mc bf mb ea nb "H- Hey, Monika."
    mc ef mf bg "I..."
    mc ea mb "I’m sorry."
    show monika at t11
    show sayori turned at r44
    "She finishes walking down the stairs, an awkward look on her face. Sayori follows shortly afterward, standing off to the side."
    m ec mb "What for? None of this was your fault, was it?"
    show monika ma
    mc ml ef na "I mean no, not technically, but I still... feel bad about it."
    m ea mb "Yeah. It really blew up into a big thing, didn’t it?"
    show monika mc
    mc bf nb eh md "Sure did."
    m md eb "And over nothing at all, too..."
    show monika mc
    mc ef bg mb "Y- Yeah, nothing."
    show sayori b2b me
    "I look away, and Sayori frowns at me, concerned."
    m bc md na "At least I... Well, we can all move past this now, right?"
    show sayori b2c ma
    m mb ba ea "We’ve got bigger things on our mind."
    show monika mc
    mc ea ml ba "Y- Yeah, like the festival, right?"
    show sayori e3c b1a
    m rhip eb md "... If people still want to do it, I suppose so."
    show monika mc
    mc na ef mf "I mean..."
    show sayori e1a
    m ec md "MC, look... I know we haven’t known each other properly for very long, but I have to tell you that I want you to stay."
    m rdown mb ea "The club means the world to me, and giving others a chance to experience it, even if just for a moment, means so much to me too."
    show monika ma
    mc bg ea mg "... You were never doing this for you, were you?"
    m bb eb mb "... Maybe at first, it felt selfish, but the more I thought about it, the more I wanted to share this feeling with as many as would listen."
    m lpoint md ea ba "Even if no-one shows up, it would still mean so very much to me that everyone tried."
    show monika mc
    mc mb "... Then... I’ll help. At the very least, I’ll help for the festival."
    show monika ma ldown
    "She gives me a small smile."
    m bb ec md "I’m thankful you are willing to do so."
    m ba ea mb "I will gladly take your help."
    show monika ma at dip
    "She offers her hand, and I take it, resulting in a firm but warm hand-shake."
    show monika ec at thide
    hide monika
    show sayori at t11
    "Then, she takes her leave."
    show sayori b2c
    "Sayori throws me another concerned look as I make my way back home. Part of me wants to ask, but... I know that if she’s that worried, she’ll ask herself."
    _mc na ba ec mh "Besides, it’s been too long of a day. I need to sleep this nightmare off."

    $ add_calendar_description(calendar_descriptions["monika"][6])
    
    call week_2_thursday_monika from _call_week_2_thursday_monika
    return