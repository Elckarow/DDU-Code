label week_2_sunday_sayori:
    call calendar_transition(day=5, hour=11, minute=43) from _call_calendar_transition_35
    pause 0.5
    scene bg s_living_room
    show sayori turned casual e2a b1b md at i11
    with mc_pov(True)
    $ set_pov("mc")
    play ambient int_day fadein 1.0

    "Long after the others had left, Sayori and I spend some time cleaning up."
    "Most of has been in silence, but a comfortable one."
    "Despite not having been here for years, I still know exactly where everything belongs."
    "There hasn't been a need for words, really."
    "It takes me some time to re-arrange the living room back to a normal state, but once I finish, I sit myself on the couch."
    mc turned casual mg "Hey, Sayori, did you have fun?"
    s e1a b1a mg "Huh?"
    show sayori ma
    mc ef ml "Last night, I mean."
    mc ea bg mb "You put a lot of work into it, so it would be really sad if you didn't enjoy it."
    s mb "I did, yeah."
    show sayori ma
    "That wasn't the most convincing thing I've heard all day."
    mc mf "Sayori."
    s mh "No, I did have fun. We did so much last night, and I really enjoyed it."
    show sayori md
    mc bb ml "Then what's up?"
    s mh e2a b2b "... It isn't the party, don't worry."
    show sayori md
    "..."
    s me "I just..."
    s mg e1a b2a "It's the festival."
    show sayori md
    mc eb nb mg "Ah, shoot, that's tomorrow!"
    mc bg eg mj "We still have so much preparation to do!"
    stop ambient fadeout 5.0
    s nb e3c mb "Ah, no, I did all that while you were at work yesterday."
    show sayori md
    mc ea mf "But..."
    s b1a e2a mg na "I know, we were going to do it together."
    show sayori md
    mc ef ml "Yeah..."
    s lup b2a e1a mb "I just had nothing to do, so I wanted to make your life easier."
    show sayori md

    play music myconfession

    mc ea bd mg "But I wanted to do it with you."
    show sayori ldown e2a b2b
    "Sayori's already melancholic look deepens."
    s mg "I know that. I just..."
    s b2a e1a mb "I couldn't help myself."
    s e2a mk b2b "I thought-"
    show sayori e2b md
    mc ec bi ml "Did you?"
    mc ea ba mg na "You knew that I was looking forward to that today. I even made sure to take the day off."
    s b2c e1b mg nd lup "But..."
    show sayori me at thide
    mc ef bi ml "I really wanted to spend time with you today. That's all."
    hide sayori
    "I stand up."
    s turned casual nb e1b b2c mk "Ah-"
    show black with NonBlockingDissolve(0.3)
    "I grit my teeth, turning away."
    _mc ef bi mh "That was unfair to Sayori."
    _mc ec ba "But..."
    s e1a ml "Wait, don't leave."
    s e2a b2b mg "Please..."
    show sayori me lup e1a tears_a at i11
    hide black
    camera master:  
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.4)
    $ autofocus.block("sayori")
    $ say_transition = True
    "Turning to face her again, I realise her eyes are starting to tear up."
    s e3c mk "Don't leave me again..."
    show sayori mj with say_dissolve
    "So soft are her words that I can scarcely hear them."
    "But even if I'd have missed it, I would have never missed the feeling behind it."
    camera master:
        zoom 1.8
    show sayori ldown
    with Dissolve(0.2)
    "I embrace her, pulling her in tight."
    "Her soft hair in my hand, I feel my shoulder slowly grow damp, and I wouldn't dream of moving."
    mc eg bg mg "I'm sorry. I never intended on leaving you."
    mc ml "I could never."
    s mg "B- but you did."
    s e1a b2a "You hung me out to dry..."
    s mk e3c tears_b b2b nc "I was so lost..."
    show sayori mk with say_dissolve
    "She isn't talking about now. She hasn't been since the start."
    mc "I'm sorry."
    mc ea bf mg "I really am."
    mc eg bg "I won't tell you I did it for any good reason, or for your own good, or any crap like that."
    mc ea ml "But I am sorry."
    s mg "I don't..."
    s b2b tears_a nb "I don't understand..."
    show sayori md lup with say_dissolve
    "She struggles to form the words through the sniffles."
    s b2a e1a mh "Why..."
    s e3c mg "Why did you..."
    show sayori md with say_dissolve
    mc ef ml bg "I had to. I couldn't force you to go through what I was going through."
    camera master
    show bg:
        blur 0.0
    show sayori e1a
    with Dissolve(0.2)
    $ say_transition = False
    "Sayori pulls away."
    "Her tear-stained eyes cause me pain just to see."
    $ autofocus.unblock("sayori")
    s ldown mi notears "Look around you, Melody. I know exactly what you went through."
    show sayori rup e3c b2b mj
    "She wipes her tears, and looks me in the eye."
    camera master:  
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show sayori e1a md rdown na
    with Dissolve(0.4)
    $ autofocus.block("sayori")
    $ say_transition = True
    s e1a tears_a lup mh b2a "I made a promise, and you made me break it."
    show sayori md with None
    camera master
    show bg:
        blur 0.0
    show sayori e2a notears
    with Dissolve(0.2)
    $ say_transition = False
    "She turns away from me."
    $ autofocus.unblock("sayori")
    s mg b2b "Why..."
    show sayori md ldown e3c at rhide
    hide sayori
    "And she disappears into the kitchen."
    "All I'm left with is the question."
    _mc thinking ea mh "What promise did she make?"
    _mc ec "I don't think it was to me."
    _mc ef "At least, it's nothing that I remember."
    _mc bi eg mm ldown "But honestly, I could care less."
    _mc ea mh ba "Sayori."
    _mc ec "That's what I care about."
    "I start walking over to the kitchen, but..."
    show black with NonBlockingDissolve(2.0)
    "As I get close, I pause."
    mc ea bg mg "Sayori, I'm sorry."
    mc ef "More sorry than I've ever been."
    mc ml "What I did to you..."
    _mc mh "It was unfair."
    _mc ec "I hurt her."
    _mc "I left her alone, and now..."
    _mc ea "She really is, isn't she?"
    _mc ef "But what can I do?"
    _mc eg "What should I do?"
    _mc bi "Apologies are meaningless."
    mc ef bg ml "It was heartless, Sayori."
    mc ea mg bf "I know that now."
    mc ef ml "I won't ask for your forgiveness."
    mc eg bi mb "I probably don't deserve it."
    mc ea bf mg "But, if you do, I will do what I can to make it up to you."
    mc mf bg "You're..."
    mc ef mg bg "You're my best friend, Sayori, and I don't want to lose that."
    mc ml "If you need me, you know where I'll be."
    "And with that, I let out a sigh."
    _mc ec ba mh "No use being here anymore, if it's just going to hurt her."
    _mc ef "Best to give her space."

    scene bg mc_bedroom_night_closed_off with longfade:
        align (1.0, 1.0) zoom 2.0
    $ set_date(hour=23, minute=23)
    play sound phone_notification

    "It's not until that evening that I finally hear back from Sayori."
    "I'm just crawling into bed, when my phone goes off."
    "Grabbing it, I find myself convinced it should be from her."
    "And as the screen lights up, I see..."
    phone register "mc_n":
        time auto True
        "n" "Hey, did you say anything to Sayori?"
    phone discussion "mc_n":
        pause
    _mc turned casual ea mh "Well, that's a little disappointing."
    _mc ec "But moreso, it's concerning. She went to Natsuki before me."
    _mc bi "Well, of course she did."
    _mc ef ma "Natsuki hasn't hurt her lately."
    phone discussion:
        "mc" "I had a chat with her this morning, after everyone left, why?"
    phone end discussion
    "I then put the phone down."
    "I don't want to get too caught up waiting for a response."
    "As much as I want to know she's alright, I know she is."
    "Sayori's stronger than I am."
    "But, against my better judgement, as soon as my phone goes off again, it's already in my hands, and I'm already reading the message."
    phone register "mc_n":
        "n" "Well..."
    phone discussion "mc_n":
        "n" "You should probably go check on her."
        "n" "Like, now."
    play ambient int_night fadein 3.0
    stop music fadeout 3.0
    phone end discussion
    "I freeze."
    _mc eb bd mh "Why would I need to check on her now?"
    _mc "It's after eleven at night."
    _mc "It would be insane to walk outside this late."
    show bg s_house_night_off with NonBlockingTransition(wipeleft):
        zoom 1.0
    "But even as I question it, my feet have already carried me out the door."

    stop ambient fadeout 3.0
    scene black with wipeleft
    phone register "mc_s":
        time auto True
        "mc" "Sayori, I'm just checking up on you, as Natsuki was worried about you. I'm heading over now, okay?"

    "I don't bother knocking. I know there's no chance of her responding to it."
    "Stepping inside, I see it dark."
    _mc turned casual ec mh "I'm glad she gave me a spare key, at least. Makes my life a little easier."
    _mc ea "Her bedroom light wasn't on, so I'm not sure if I should be here, but-"
    _mc ec "-Even so, I need to do something."
    _mc ea "If Natsuki says something is up, it's definitely worth worrying about."
    _mc "She wouldn't text me over just anything."
    play sound door_knock
    "I make my way up the stairs, and knock on the door."
    "I'd already sent her a text, so if she's up she will have read it."
    "... I think."
    mc mg "Sayori, you in there?"
    mc ef bg ml "Natsuki was worried about you, so I came to check on you."
    "..."
    "No response."
    _mc ec ba mh "I don't like the look of this."
    # play sound door_open
    "I reach for the doorknob and gently push open the door."
    "The room is covered in darkness."
    "My hand reaches for the lightswitch, and when it flicks on-"
    play music wtdgi fadein 1.0
    window auto hide None
    scene white 
    show cg sayori 3 zorder 1
    with None
    pause 3.5
    hide white with Dissolve(3.3, time_warp=_warper.easeout)
    $ say_transition = True
    $ persistent.sayori.mark_cg(3)
    mc turned casual ml bg "Sayori..."
    "Sayori, holding the covers of her bed over her head like a cowl."
    "She's facing away from me, and she seems aware of my presence, yet..."
    "She doesn't respond."
    mc mg "Sayori, are you alright?"
    mc ml "Natsuki was worried about you."
    "..."
    "Still nothing."
    mc mf "I'm..."
    mc ef ml "Worried about you."
    "..."
    mc mg "I know that I haven't been the best friend you deserve."
    mc "I've done some stupid things, I'll admit that."
    mc ml "I know that we've had some rough patches, too."
    mc ea bf mg "But that doesn't mean I don't care about you."
    mc ml "I do."
    mc mb "I really, really do."
    mc ef bg mg "More than you realise."
    mc ml "Sayori... I-"
    s turned casual bags e2a b1b mg "That's all, isn't it."
    mc ea bf ml "Huh?"
    show cg eb with cg_dissolve
    s e1a mh "That's all you see me as, isn't it? I'm not even..."
    "She shakes her head, seemingly driving away her thoughts."
    s e3c mg "... I know."
    s e2a mh "I know that I'm not smart like Monika, or cute like Yuri, or wise like Natsuki."
    s b2a mb "Hell, even the president of the Debate club, Aika, has more charm than I do."
    s b1b mh "I know, I saw you talking to her the other day."
    s mg "But..."
    s e3c "That's all I am, isn't it?"
    s e1a mh "The one you could manipulate the easiest."
    s "The one you could bond with, then have your way with."
    s e2a mg "That's why, isn't it?"
    mc mf nb "What...?"
    _mc eb bd mh "What is she talking about?"
    mc ml ea "I never used you."
    mc mg "I never once considered it."
    mc bg mb "You're my best friend, Sayori, just listen-"
    s e1c b1d mi nb "{i}No!{/i}"
    "I pause at her outburst."
    s mj e1a "..."
    s e2a mg "No."
    s e3c mm "Stop {i}saying{/i} that."
    s e1a b1b mh na "If you aren't here to fix what you've done, {b}{i}leave{/i}{/b}."
    _mc na ec ba mh "What I've done..."
    _mc thinking ef "That could be a lot of things."
    _mc eg bi "Hell, what in particular is she referring to?"
    _mc ec ba "It must have been something I've done just then..."
    _mc "But I can think of nothing."
    _mc ldown ea "I know for a fact that I've done something wrong, but I have no serious idea exactly {b}what{/b}."
    mc ml bg "Sayori, I'm not-"
    show cg ea with cg_dissolve
    s e3c mg "I know."
    s e2a "That's the problem."
    s e1a mh "You don't, do you?"
    s e2a me "I..."
    s e3c mh "{cps=20}{b}{i}I don't want to see you anymore.{/b}{/i}{/cps}"
    s e1a mg "I think you should leave, before you make it worse."
    mc mh "..."
    mc ef ml "Sayori..."
    mc ec bi "I need to tell you something."
    mc ba mf ea "I-"
    s e1c "{i}Don't.{/i}"
    s mh "Don't you {i}dare.{/i}"

    scene black with Dissolve(0.5)
    $ say_transition = False

    "And with that, I leave."
    "Not another word."

    scene bg mc_bedroom_night_closed_off with longfade:
        align (1.0, 1.0) zoom 2.0
    $ advance_date(minutes=10)
    play sound phone_notification

    "After crawling back into bed, for the second time tonight, I received another text."
    "This time, from Sayori herself."
    phone register "mc_s":
        time auto True
        "s" "I won't say anything to anyone else."
    phone discussion "mc_s":
        "s" "We have the festival tomorrow, so I'll just..."
        "s" "Pretend like nothing happened."
    _mc turned casual ec bg mh "She really meant that, didn't she?"
    phone end discussion
    "I consider responding, but instead put my phone back on to charge."
    _mc ef ba "There's no point in talking about it."
    _mc eg "As she said, we should just get through the festival."
    _mc "After that..."
    _mc bi ma "Well, after that, I'll try and work out if there's even a friendship left to save."

    $ persistent.sayori.mark_ending(1)
    return