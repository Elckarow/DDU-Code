label week_2_sunday_monika:
    call calendar_transition(day=5, hour=11, minute=37) from _call_calendar_transition_12
    pause 0.5
    scene bg club_day with mc_pov(True)
    $ set_pov("mc")

    "After seeing everyone off this morning, I’ve come to help Monika with some last-minute preparations at school, to get the room ready."
    _mc turned ec "I’m glad she got permission to come in out-of-hours; we really need the extra time to make it perfect."
    m turned mb "Oh, can you put this over in the corner?"
    m md "And make sure the kettle is plugged in so that we can make tea for everyone who comes tomorrow."
    mc ea mb "Shall do!"
    show bg class_2_day
    show monika rhip ma eb bc at i11
    with NonBlockingDissolve(0.7)
    "She’s busily sorting out what to put on the board behind us, while I work on touching up smaller things around the room."
    _mc ma "It’s really starting to come together, actually. I can see her vision play out before my eyes."
    "... Okay, the kettle’s sorted. I’ve also got some spare water next to it, so that we can quickly refill it. I’ll also get out Yuri’s tea set and leave it on the counter next to it; that’ll help her out tomorrow, too."
    
    scene bg club_closet_day with wipeleft
    
    "Now to close the closet, and lock it up, away from any prying eyes tomorrow."
    mc turned mg "Can I borrow the keys, Monika?"
    m turned mb "Sure!"
    show white at flash(0.2)
    play sound ["<silence 0.1>", audio.slap]
    "She tosses them across the room, and I clumsily catch them, with one of the keys driving into my palm."
    mc bg eh mm "Ouch!"
    "The keys hit the floor, and I pick them up again."
    show monika mc bb at i11
    show bg club_day
    with Dissolve(0.2)
    m md "Are you alright, Melody?"
    show monika mc
    mc nb ea mb "Y- Yeah, I am, thanks..."
    show monika ba

    play music wtdgi

    mc mg bb "Also, I did want to... well, talk to you."
    m md nb "Oh, ah, I thought we were going to wait-"
    show monika mc
    mc eb "N- No, not about that, just..."
    show bg club_closet_day zorder 5 as stuff with NonBlockingDissolve(0.2)
    "I lock the closet, and turn back toward her."
    hide stuff with NonBlockingDissolve(0.2)
    mc ef mg na ba "I actually wanted to thank you for not calling me Melody last night."
    mc mb "It... I don’t know, maybe it would have caused problems."
    show monika na ma
    "She simply smiles at me."
    m ec mb "I figured that would be the case, so I played it a little safe. I’m sorry if you were worried about it."
    show monika ea ma
    mc ml bg "No, not really. It’s what I’m used to, so... honestly, being called Melody still feels a little weird. Almost... nostalgic."
    m md rhip "Do you miss it?"
    show monika mc
    mc eg ba ml "No, not as much, but... I guess I miss what it brings with it. Memories."
    m eb bb md "Ah."
    show monika rdown mc
    mc ea ml "You know, when I was a kid, I never put much thought into what people called me. Sure, it was a weird name, but no-one really made fun of me for it."
    show monika ba ea
    mc ef mg "But I guess, when it all happened, I just..."
    m md "When what happened?"
    show monika mc
    mc bi ml "... When my parents left. Abandoned me."
    m md bb "Oh, Melody, I had-"
    show monika mc
    mc bg ea mb "It’s okay, I’m... in a better place now. It took me a long time, but I’m back on my feet."
    m rhip ec mb "... I’m thankful."
    show monika ma
    mc eg ba "As am I. Without it, I would never have been able to meet you, or reconnect with Sayori."
    show monika rdown ea
    mc bg nb eh md "Hell, I’d never have connected with Amelia, either."
    mc ea ba na mb "So in a way, I think it worked out."
    _mc ec mh thinking "A lie, of course, but I don’t dare say that in front of Monika."
    _mc ef ldown "The truth is, I despise them for leaving me so helpless and unprepared."
    _mc bi "My anger never really went away; I just got better at hiding it."
    _mc eg mf "Dammit."
    m md lpoint ba "Well, we’re pretty much done here, and much earlier than I expected! Did you... I mean, if you want to, do you want to grab some lunch?"
    show monika mc
    mc ef mg ba "... Sorry, Monika, I..."
    mc bg ml "Not today."
    show monika ldown eb
    "She nods, a cloud covering her expression."
    m bb md ea "I understand. Should I... avoid asking, in the future?"
    show monika mc
    "I bite my lip."
    mc ea mb "N- No, please ask, it’s just..."
    mc ef ml "I’m not ready. Not for that."
    m md "Melody, I-"
    show monika mc
    mc eg mb "Please, Monika, I know you’re trying to help, but..."
    mc ef ml "It doesn’t."
    m ec md "I understand."
    m ea mb "I’ll... see you tomorrow, then?"
    show monika ma
    mc ea mb ba na "Mhm. I’ll see you first thing in the morning."
    "I give her a small smile before heading off."
    _mc ec mh "This is the right thing to do, Mel. Put some distance between you two."

    $ add_calendar_description(calendar_descriptions["monika"][9])

    $ persistent.monika.mark_ending(1)
    return