label week_2_wednesday_sayori:
    call calendar_transition(month=11, day=1, hour=8, minute=17) from _call_calendar_transition_31
    scene bg mc_bedroom_day_closed
    camera master:
        align (1.0, 1.0) zoom 2.0
    with dissolve_scene_full
    play music pensive

    "Unsurprisingly, sleep did not find me."
    "Instead, I spent the night staring at my roof."
    play sound phone_notification
    camera master
    with Dissolve(0.2)
    "Now, more tired than ever, I force myself out of bed to the sound of my phone ringing."
    "I glance over, noticing it's from Sayori."
    phone call "s"
    phone_s "If you're going to keep me waiting, at least let me in."
    phone_mc turned naked nostrands messy ec bi mf "... Huh?"
    "I glance at the time on my phone."
    _mc ba mh "Huh. That's different. It's pretty late. I'm usually half-way to school by now."
    _mc eb bb mf "Wai-"
    phone end call
    # 5mins 10secs
    $ phone.data["mc"]["call_history"][-1].duration = 310
    $ phone.data["s"]["call_history"][-1].duration = 310
    show bg residential_day with NonBlockingTransition(wipeleft)
    $ advance_date(minutes=5)
    "Five minutes and one awkward phone call later, I barge out of the front door, screeching down the street."
    _mc uniform tail nostrands ec mh ba "It's going to be a long, long day."

    scene bg class_1_day with fade
    $ set_date(hour=12, minute=0)

    _mc turned tail nostrands eg bi mm "Ugh, I'm too tired for this."
    play sound school_bell
    "The bell rings for lunch, and I realise just how little I've managed to pay attention in class today."
    "Normally, that would be cause for concern, but today, I just can't even muster up that much energy."
    "Sayori ended up leaving without me, so I had to sprint to make it to school on time, but that may well have drained all of the energy I had left."
    "Not to mention the puddle of sweat I was standing in by the time I got to school."
    "I had been meaning to talk to her about what happened last night, but..."
    "I can't believe that I managed to stare at my roof for nine hours, just questioning every life choice I've ever made."
    _mc ba mh ec "Sayori..."
    "If I get some sleep now, maybe I'll be awake enough to pay attention in class later."
    _mc eg ma "Yeah, that'll do it."
    call close_eyes(1.0) from _call_close_eyes_16
    "I lay my head on my arms, squarely on my desk, and close my eyes."
    
    $ renpy.music.set_volume(0.3, 2.2)
    scene black
    show bg class_3_day
    camera master
    pause 2.0

    "As I start drifting off, I feel a presence above me."
    _mc turned uniform tail nostrands eg ba mh "'Wake up', I can hear them say."
    _mc "'Only losers sleep in class', they say."
    _mc bi "Man, is someone trying to bully me for being tired?"
    _mc ba "Ah, I'll just ignore them and deal with them later."
    _mc ma "When I'm more awake."
    play sound smack
    call blink(color="#fff", duration=0.4) from _call_blink_17
    _mc eb bb nb mf "... Ouch!"
    "A sharp pain to my cheek."
    $ renpy.music.set_volume(1.0, 2.0)
    hide black with NonBlockingDissolve(0.2)
    "I raise my head. ready to sock someone for disturbing me."
    show aika turned at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("aika")
    $ say_transition = True
    a mf nb "Woah, calm down there."
    show aika ma na with say_dissolve
    mc ec bi mf na "Aika?"
    mc ea bd ml "What are you doing in my classroom?"
    a lpoint mb "I was looking for you."
    show aika ma with say_dissolve
    _mc ec bi mh "I'm not sure I like where this is going, knowing everything I know about this girl so far."
    mc ea bd thinking ml "... Why?"
    a ldown ec md "Well, if I'm honest, a little bird told me something."
    mc ldown mg "What? What did they tell you?"
    a smug mb "I think you know exactly what I know."
    show aika ma with say_dissolve
    "A sly smile crosses her face."
    _mc eb bd mm "Natsuki! I'm gonna kill her!"
    _mc "She promised!"
    a turned rhip mf ea "Oh, now that's a new look. Don't keep it; it doesn't suit you."
    a smug mb "I much prefer when you're embarrassed."
    show aika ma with say_dissolve
    mc ec bi ml "Sorry, I have some business to attend to."
    show bg:
        blur 1.0
    camera master:
        zoom 1.3
    show aika turned me
    with Dissolve(0.2) 
    "I rise from my seat. I can't believe she would do that, after all of her talk of support."
    _mc eg ma "Ha, I should have known."
    a mf "Oi, are you listening to me?"
    $ say_transition = False
    show aika bc nb
    camera master
    show bg:
        blur 0.0
    with None
    camera master at vpunch
    play sound slam
    stop music 
    mc eb bd mm nb "WHAT?"
    $ autofocus.unblock("aika")
    a mg eb "I just... wanted to congratulate you... on your club getting a feature in the news club bulletin..."
    show aika me
    mc ea ml "Wh-"
    play music myconfession
    show bg class_1_day as stuff zorder 5 with NonBlockingDissolve(0.3) 
    "As I look around, I see the entire classroom looking at us."
    show bg class_1_day as stuff:
        align (1.0, 0.6) zoom 2.0
    show yuri turned b2b me lup nb zorder 6:
        i43
        zoom 0.78
    with Dissolve(0.2)
    "Including Yuri."
    hide stuff
    show aika na ea
    hide yuri
    with Dissolve(0.2)
    "Aika's face is something I've never seen before. Her smug atmosphere is replaced by fear."
    "Fear... of me."
    mc bf ml "Aika, I'm so sorry, I didn't mean to shout."
    show aika mf nb at t21
    "I reach out to apologise, but she pulls even further away."
    mc "Aika, please, I didn't mean that. I'm just exhausted."
    mc bg eg "And I know, that gives me no right to shout at my friend."
    mc ea be "Please, let me make it up to you."
    "Aika remains backed away."
    show aika ed
    "I feel like she's about to run for the door, and if she does, I'll lose her forever."
    "I've never seen anyone this scared before; not of me."
    "I can't begin to imagine what might be running through her head right now."
    show aika eb me na
    "She looks from me to the ground."
    show aika ea bd
    "Then back to me."
    a rhip mh "We need to talk."
    show aika me
    "An almost defiant look appears on her face. I dare not disobey her."

    scene bg class_1_day with wipeleft:
        xzoom -1
    show aika turned bd me at t11
    play sound slap
    camera master at vpunch

    "Aika drags me to an unused classroom, where she unlocks it, walks inside, and places me down on a chair."
    a mh eb "Alright, you have six seconds to explain yourself."
    show aika ea me
    "I don't think I could mistake the look on her face if I tried."
    mc turned tail nostrands ml bf nb ed "Ok, I'm going to tell you something, but you need to keep it a secret. From absolutely everybody."
    show aika eb mh at dip
    "Aika leans onto the wall next to me, her face now morphing into frustration."
    a mf "I will make no such promises after what you just pulled."
    a mh ea "Do you know how much that could damage both of our reputations?"
    a mg "Do you even think before you do things?"
    a eb mf ba rhip "Or do you just assume that everything will work out, like one of those happy little stories you club members like to read?"
    a ea mh bd "Well, surprise, no. Your actions have consequences."
    a mg "I didn't want to have to drag you here. I'm not supposed to be using this room for anything."
    a ea mh "And yet, here we are, because you don't know how to keep your panties on."
    show aika me
    mc ea mg "Wait, that's-"
    a rdown eb mf "I'm not finished."
    a ea mh "Do you understand what you're doing to Sayori?"
    a mf "She's hurting because of you."
    a mh "Act like an adult and make a decision for yourself for once, if you dare."
    show aika me
    mc ec bi ml na "Wait, what do you know?"
    "Did Natsuki tell her after all?"
    a rhip eb mg "Oh please, I see the way you two look at each-other."
    a mf ea ba "I hate getting involved, so I'm only going to say this once."
    a mh bd rdown "Make a decision. I don't care what decision you make, but make it."
    show aika me
    mc ba ea "So, how much do you know?"
    a mf "I know more than you realise."
    show aika me
    mc ef bi mf "I see."
    show aika ba eb
    show bg:
        blur 1.0
    camera master:
        align (0.5, 0.2) zoom 1.3
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("aika")
    "Aika's frustrated look melts away, and she approaches me, pulling up a chair."
    a ed bd mg "I'm sorry that was so blunt. But we both know that you couldn't make a decision without it."
    a ea ba mf "Sayori's your best friend. It must be hell for you to try and work out where you stand."
    show aika me with None
    camera master:
        zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    a eb mf "Tell you what."
    a ea mb "If the festival goes well, make your decision then."
    show aika ma with None
    camera master:
        zoom 2.0
    show bg:
        blur 3.0
    with Dissolve(0.2)
    a mf "No need to force yourself, yeah?"
    show aika ma with say_dissolve
    "Aika's face is close to mine. Dangerously close. And the now sweet smile makes me return one in kind."
    a eb mb "Again, I'm sorry for being so blunt. To be honest, part of it was saving face in a public environment."
    a ed mf "The other part is, well, I care about you guys."
    a ea mb "I just want you to be happy, you know?"
    show aika ma with say_dissolve
    mc ed ml ba "Yeah. But, you should be too."
    mc ea mb be "I'm sorry to have made you go through that."
    show aika me with say_dissolve
    "Aika's expression shifts to one of confusion."
    camera master:
        zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    a mb "Sorry?"
    show aika me with say_dissolve
    mc bf "I want you to be happy as well, you know?"
    a nb mb bb ed "Me? Why would you worry about me?"
    show aika ma with say_dissolve
    mc "Because you're my friend, and I care about you too."
    a mb bd eb na "Hah, go figure."
    show aika ma with None
    show aika lpoint ea ba
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She stands, and motions toward the door."
    $ autofocus.unblock("aika")
    a mf ldown "We... probably shouldn't be in an empty classroom alone for much longer. It might make lives difficult for us."
    show aika me
    mc ef bg nb "Yeah, you're right."
    show aika ma
    "We leave the room, and after sharing a smile, return to our classrooms for the next period."

    stop music fadeout 2.0
    scene bg school_corridor_1_day with longfade
    $ set_date(hour=15, minute=20)

    "After the end of classes, I make my way to the clubroom."
    "Even considering all that, I still can't focus on class."
    _mc turned tail nostrands eg bi mh thinking "Hell, if anything, I was more distracted."
    show bg class_1_day as stuff onlayer above_master:
        xzoom -1
    show white_flashback onlayer above_master
    show aika turned bd mh at i11 onlayer above_master
    camera above_master at flash(0.5)
    "Aika told me to make a choice. I know what she means, and I get that. I really do."
    "I just don't know what choice I should make."
    $ clear_layers("above_master")
    _mc ec ba "Why wait until after the festival?"
    _mc "Wouldn't it be smarter to choose beforehand?"
    _mc ea "Hell, why didn't she make me pick then and there?"
    "..."
    _mc ec "Because she knows."
    _mc "She understands that I can't."
    _mc ef ldown "It's not a choice I can make. Even if it was..."
    _mc eg "I already know my answer."
    _mc bi "I had that answer within me years ago. That hasn't changed."
    _mc ec ba "But, I'll wait until after the festival. There's less than a week, so we really should be focusing on that."
    show natsuki cross e1d b1d mh at t11
    n "Oi, are you coming in, or just planning on standing there the whole day?"
    show natsuki mj
    "I'm still standing outside the clubroom, and Natsuki appears to have come out to chastise me."
    n b1a e2a mg "I don't know what you did, but..."
    n turned e1a mb "I do have to thank you."
    n b3a mh "Sayori's in a better mood now. At least she seems to be."
    n mb "So, thank you. Now come on, we have prepwork to do."
    show natsuki ma e2a at thide
    hide natsuki

    mc ed mb ba "Hah, yeah we do, don't we?"

    scene bg club_day with wipeleft
    play music okev
    pause 0.03
    show bg:
        align (1.0, 0.6) zoom 1.8
    show sayori turned lup b1d e1d md at i44
    with Dissolve(0.2)
    "Stepping inside, I see Sayori working hard at making decorations."
    show bg:
        align (0.0, 0.8) zoom 1.9
    hide sayori
    show yuri turned md lup e2a b1d at i42
    with Dissolve(0.2)
    "Yuri's in the corner, hard at work writing."
    show bg class_2_day:
        zoom 1.0
    hide yuri
    show monika turned eb mc bc rhip at i11
    with Dissolve(0.2)
    "Monika seems to be doing some paperwork."
    show natsuki turned me b1d at i43
    show bg club_closet_day
    hide monika
    with Dissolve(0.2)    
    "Natsuki seems to be sewing something. It looks like a curtain?"
    "Huh. She never struck me as someone interested in sewing."
    hide natsuki
    show bg club_day
    with Dissolve(0.2)
    "Regardless, after looking around the room, I wonder what I can help with."
    show natsuki turned md e1d lhip rhip b1d at i43
    show bg club_closet_day
    with Dissolve(0.2)  
    "I glance toward Natsuki, who is making some rather obvious gestures toward me."
    show natsuki b1a mm e1b ldown rdown at hop
    "She's pointing at Sayori."
    show bg club_day:
        align (1.0, 0.6) zoom 1.8
    hide natsuki
    show sayori turned lup b1d e2a mj at i44
    with Dissolve(0.2)
    "I give her a smile and squat down next to Sayori."
    camera master:
        align (1.0, 0.2) zoom 1.4
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc turned tail nostrands mb "Hey, Sayori."
    mc mg "Want a hand?"
    show sayori b1a md with say_dissolve
    "Sayori pauses, holding the scissors in a loose grip."
    show sayori e1a with say_dissolve
    "She turns toward me."
    show sayori ma with say_dissolve
    "Sayori beams."
    s e3d mn "Yeah, I'd love one, ehe~"
    show sayori ma 
    show black 
    with NonBlockingDissolve(1.0)
    $ advance_date(minutes=12)
    "Sayori and I work on some decorations in silence."
    "We exchanged greetings, then just started working."
    "Most of them are being made out of paper, but there's also some fabric that she's been working with."
    "I suppose I shouldn't complain, it isn't an uncomfortable silence."
    show sayori e2a ma ldown
    hide black
    with NonBlockingDissolve(0.5)
    "I'm more happy to just exist next to her."
    show sayori md lup with say_dissolve
    "Her hands soar over the paper like a glider in the wind, gently, yet deliberately."
    show sayori ma rup with say_dissolve
    "Selecting the right colour paper to match the one she already holds, she glues them together, forming a simple, yet gorgeous flower design."
    show sayori ldown rdown e3c with say_dissolve
    "My skills are not as pronounced, but with the extra time I take for each, they still look alright."
    show sayori rup md e2c with say_dissolve
    "Every time she moves, my eyes are drawn back to her."
    show sayori lup rdown e2a me with say_dissolve
    "Her dexterous fingers caress the paper and fold it in such a way that I simply couldn't look away if I tried."
    show sayori ma  with say_dissolve
    "The small smile on her face, the determination in her eyes..."
    show sayori md b1d with say_dissolve
    "It reminds me of what happened last night."
    show sayori b1a me with say_dissolve
    "It isn't the same face, but it doesn't matter."
    show sayori e1a md with say_dissolve
    "She's still Sayori."
    show sayori ma ldown with say_dissolve
    "Noticing my stare, she turns toward me."
    s mb e2a "Ehe... Did you want it?"
    show sayori ma with say_dissolve
    mc ml bf "Want... what?"
    "I see the way she moves her lips as she speaks."
    "I... I was attached to them, less than a day ago."
    "I kissed her."
    "To be honest, I'm still floating a little from it."
    s e1d mb "You know..."
    show sayori ma with say_dissolve
    "Oooh, those eyes."
    "The smile she gives me is like nothing I've ever seen."
    "It's both playful, and..."
    "Something else."
    mc ef mb "Well, I would never say no, that's for sure..."
    show sayori mo e3d with say_dissolve
    "Sayori smiles at this."
    show sayori e1d ma at i43
    camera master:
        zoom 1.7 xalign 0.65
    show bg:
        zoom 1.65 blur 2.5
    with Dissolve(0.2)
    "A smug, cheeky grin, as she leans closer toward me."
    "I prepare myself."
    show black with NonBlockingDissolve(0.5)
    play music_poem add_playback_info(audio.okev_s, get_pos()) fadein 2.0
    stop music fadeout 2.0
    "Closing my eyes, I start to tense up from anticipation."
    "And then..."
    "I feel Sayori's hands."
    "They're next to my ear."
    _mc eb bb mf nd "Huh?"
    "She's doing something above my ear?"
    show sayori e1b mf lup at i44
    hide black
    show bg:
        blur 2.0 zoom 1.8
    camera master:
        zoom 1.4 xalign 1.0
    with Dissolve(0.2)
    play music add_playback_info(audio.okev, get_pos("music_poem")) fadein 2.0
    stop music_poem fadeout 2.0
    "Opening my eyes, I see her lean back, appreciating her handiwork."
    mc bd mg "Wha-"
    s e1a mb "Ehe, there you are. All yours!"
    show sayori ma ldown with say_dissolve
    "Confused, I reach up to my ear."
    "She's placed the paper flower there, seated above my ear."
    _mc mf ba ea na "Did she..."
    _mc ec bi mh "No, there's no way that was deliberate."
    "In a way, though, this means more to me than if something else had happened."
    "It proves that she still enjoys my company."
    "It means that, through it all..."
    _mc eg ba ma "We can still be friends."
    
    scene bg club_afternoon
    camera master
    with Fade(0.6, 0.0, 0.5)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    $ set_date(hour=16, minute=34)
    stop music fadeout 3.0

    "As we finish packing up, I notice an uneasiness wash over the room."
    "Like a chill breeze, what had been the sound of bustle was now as silent and empty as a tomb."
    show sayori turned b1b e2c md:
        matrixcolor TintMatrix("#f1d6bb")
        i44
    show bg:
        align (1.0, 0.6) zoom 1.8
    with NonBlockingTransition(wiperight)
    "Glancing toward Sayori, I see her expression has soured."
    show monika turned bc ec mc:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    hide sayori
    show bg class_2_afternoon:
        zoom 1.0
    with NonBlockingTransition(wipeleft)
    "Monika's, too."
    hide monika
    show bg club_afternoon:
        align (0.0, 0.8) zoom 1.9 xoffset -150
    show bg club_closet_afternoon as stuff zorder 2:
        crop (absolute((config.screen_width / 2.0) - 150), 0.0, absolute((config.screen_width / 2.0)), 1.0) xalign 1.0
    show natsuki turned e2c rhip mj:
        matrixcolor TintMatrix("#f1d6bb")
        i43
        xoffset 150
    show yuri turned e2a b1d md:
        matrixcolor TintMatrix("#f1d6bb")
        i42
        xoffset -150
    with NonBlockingDissolve(0.3)
    "In fact, everyone would appear to be locked deep in thought."
    "Maybe I haven't been around long enough to get it."
    hide natsuki
    hide yuri
    hide stuff
    show bg:
        zoom 1.0 xoffset 0
    with Dissolve(0.2)
    "As I contemplate what it might be about, I feel a tug at my sleeve."
    show sayori turned me b1b rup:
        matrixcolor TintMatrix("#f1d6bb")
        i44
    show bg:
        align (1.0, 0.6) zoom 1.8 blur 2.0
    camera master:
        align (1.0, 0.2) zoom 1.4
    with Dissolve(0.2)
    "Sayori is holding it, looking up at me."
    "Her expression of loneliness is unlike anything I've seen before."
    "It suddenly occurs to me that I've seen a lot of Sayori lately; sides of her I never knew existed."
    "Knowing someone needs to break the atmosphere, I open my mouth."
    "What follows cuts the air like a knife."
    play music myfeelings
    m turned eb bc md "Do you guys really want to perform for the festival?"
    show natsuki turned e2a md:
        matrixcolor TintMatrix("#f1d6bb")
        i43
    show yuri turned lup md:
        matrixcolor TintMatrix("#f1d6bb")
        i41
    show sayori turned rup md:
        matrixcolor TintMatrix("#f1d6bb")
        i44
    show monika mc:
        matrixcolor TintMatrix("#f1d6bb")
        i42
    show bg:
        blur 0.0 zoom 1.0
    camera master
    with Dissolve(0.2)
    "Every head in the room turns to face her."
    m md rhip "I know we've done a fair bit of prep work already, and the paperwork's already done, but..."
    m mb ea bb "I don't want to force you guys, if you really don't want to. There'll be other chances to get members, and we aren't exactly an experienced club."
    show monika ma
    show yuri e2a ldown
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    "My eyes darts around the room. The three girls are considering Monika's offer. Weighing up their options."
    show natsuki b1d
    "I'm sure at least a couple of them think it's a trap."
    "That Monika's trying to trip them up for some reason."
    "But..."
    "I don't think so."
    "I don't claim to know Monika all that well, but I think there's something else going on here."
    _mc turned tail nostrands mf "Why would she want to shut down something she's worked so hard for?"
    hide black with NonBlockingDissolve(0.4)
    _mc ec bi mh "Something's going on."
    m rdown mb ba "You don't have to say anything right now. All I'm saying is, if only a couple of people want to read poems, then we shouldn't all feel obligated to."
    m eb bc md "And if I'm the only one..."
    m ec mb "Then there's no point in forcing everyone to participate."
    show monika ma
    "..."
    "The club continues to maintain silence."
    show sayori rdown e1a b1a
    "That is, until I feel Sayori let go of my sleeve."
    show yuri e1d
    show natsuki b1a e1a
    show monika ba ea mc
    s mg "Monika."
    s mh "We all agreed to this."
    s mb "No matter the reason, it's bad form to back down now, right?"
    s lup e3c "At least, that's what you taught me."
    s b1d mh e1a "And I, for one, won't back down."
    s ldown e2a mg b1a "It might not be just you having reservations, Monika, but I know us."
    s e1a mb "Even if we're scared, we will still get there in the end. How else are we supposed to grow without that initial leap?"
    show sayori ma with None
    show sayori b2a
    show natsuki:
        alpha 0.0
    show monika:
        alpha 0.0
    camera master:
        align (1.0, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "She turns back to me."
    "The smile she now wears is a torn one."
    "The smile of a burned friend."
    s mb "There are no redos. No second chances."
    show sayori ma with None
    show monika:
        alpha 1.0
    show natsuki:
        alpha 1.0
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    "She turns back toward Monika."
    $ autofocus.unblock("sayori")
    $ say_transition = False
    s b2b e3c mb "So, let us have this. Let us learn from our mistakes. And to do that, we need to make them in the first place."
    show sayori ma
    "I'm..."
    "I'm in awe."
    _mc ea mh ba "Who is she, and what has she done with Sayori?"
    show sayori e1a
    m rhip bc ec md "No, you're right."
    m mb "You're absolutely right."
    show monika ma eb
    "Her expression darkens."
    m mb "I'm sorry for putting everyone through that."
    m ba md rdown ec "We should probably break for the day. I'll see everyone tomorrow."
    show monika mc with None
    hide monika
    hide natsuki
    hide sayori
    hide yuri
    with Dissolve(1.5, time_warp=_warper.ease)
    show natsuki turned lhip e2a md:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    "As everyone files out of the room silently, Natsuki approaches me."
    n ldown e1a b3a mh "She's not just talking about Monika, you know?"
    show natsuki md at thide
    hide natsuki
    "And with that, the clubroom is empty."

    scene bg mc_living_room with wipeleft_scene
    $ set_date(hour=19, minute=10)
    $ set_internet(True)

    "After a long sigh, I spread out over the couch."
    _mc turned tail nostrands mj bi eg "This day was long, but..."
    _mc ea ma ba "I'm not unhappy. Far from it, actually."
    _mc ef "I spent some quality time with Sayori, we walked home together..."
    _mc mh "But something's still on my mind."
    show bg class_1_day as stuff onlayer above_master:
        xzoom -1
    show white_flashback onlayer above_master
    show aika turned bd mh at i11 onlayer above_master
    camera above_master at flash
    _mc bi "The conversation with Aika."
    _mc ec ba "To an extent, I know exactly what she means."
    _mc bi "No, that's a lie."
    $ clear_layers("above_master")
    _mc eg "I know exactly what she means."
    _mc ec ba "I just can't, or rather, don't want to face it."
    _mc "As soon as I do, I hurt Sayori. No matter what I pick."
    _mc "She's my best friend."
    _mc ef "She's..."
    _mc bg "The most important person in the world to me."
    _mc "But if I hurt her, by dragging her into something she doesn't want to do, then I would be the worst possible person to have ever lived."
    _mc "I can't do that to her."
    _mc "I know that she's always been one to tag along whenever we did things as kids. She'd always just agree and go along with it."
    _mc eg "But I can't get that look out of my head."
    _mc "It's haunted me for all these years."
    call close_eyes(1.5) from _call_close_eyes_17
    _mc bi mm "The kiss, the kiss I never should have attempted. The one I gave her before all the hell, the misery, of the past few years."
    _mc bg ec mh "That was the day I lost Sayori."
    _mc "That was the day I swore to never hurt her like that again."
    _mc ef "But it was more than that."
    _mc "That was the day..."
    _mc eg "The worst day of my life."
    _mc "And at that point, it had only just begun."
    _mc "Losing my best friend... was just the beginning of the nightmare."
    _mc "The nightmare that I still traipse through today."
    _mc "I couldn't drag her into that hell."
    _mc ef "I'd rather die."
    mc bf ml "Sayori... what have I done?"
    play sound door_knock
    stop music fadeout 2.5
    pause 0.5
    _mc eb ba nb mf "Huh?"
    call open_eyes(0.4) from _call_open_eyes_10
    _mc "Who's at the door?"
    show bg mc_house_entrance_night with NonBlockingTransition(wipeleft)
    "Getting up, I drag my sorry corpse over to the front door, slowly dragging it open."
    show sayori turned at t11
    
    play music dollaort

    mc turned tail nostrands eb mg "... Sayori?"
    s mb e3d "Surprise!"
    show sayori ma
    mc ed bd ml "I thought you said you had stuff you had to do at home?" # im stuff
    s mb e1a "Yeah, all finished, so I decided to head on over!"
    show sayori ma
    _mc bi ec mh na "I'm struggling to see the logic, but..."
    _mc ma ea ba "I certainly wouldn't complain."
    _mc "We should probably have a chat anyway, in all honesty."
    show sayori lup
    "I wonder what she's got in her bag, at least. She never brings a bag over, considering she lives next door."
    show sayori md
    _mc thinking ec mh "What is she planning?"
    s b2a e2a mb "Are you going to invite me in, ehe?"
    show sayori ma at thide
    mc ea mg "Oh, of course."
    hide sayori
    "I let her enter the door, and we head toward the living room."
    
    scene bg mc_living_room
    show sayori turned at i11
    with wipeleft

    mc turned tail nostrands ml "So, what brings you over?"
    s lup mb e3a "Well, that's a surprise!"
    show sayori ma e3d
    mc ec mf "... Alrighty."
    show sayori at thide
    hide sayori
    "I'm fairly certain the confusion on my face has been picked up by my best friend, but she proceeds to ignore it."
    _mc ma "Alright, keep your secrets."
    "Shrugging, I follow her toward the kitchen."

    scene bg mc_kitchen_day
    show sayori turned mj b1d at i11
    with wipeleft

    s e2a lup mb "Now, where are they? Ehe~"
    show sayori ma
    mc turned tail nostrands ml "What are you after, Sayori?"
    s e1a b1a mh "Oh, nothing. Nothing in particular, anyway."
    s ldown mb "Just go sit on the couch, I'll be out in a minute."
    show sayori ma e2a b1d
    "If that isn't the most suspicious smile I've ever seen from her, I don't know what is."
    "Regardless, it would be uncouth of me to disobey. Best to let her have her fun."
    "Besides, I'd be lying through my teeth if I said I wasn't curious."

    scene bg mc_living_room with wipeleft

    "Placing myself on the couch, I shrug nonchalantly."
    "It's far from the first time she's done this type of thing."
    "If she needs any help, she'll ask."
    
    scene bg mc_living_room with fade
    $ advance_date(minutes=5)

    "After about five minutes, I hear a sound from behind me."
    s turned lup rup mb e3d "It's reeeaaaaadyyyy~"
    show sayori mn at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "I start to turn around to face her, but by the time I do, she's already placed herself squarely on the couch, right next to me."
    s mo "Tada!"
    "In her hands, she holds two..."
    "Wait, are those the witch's old wine glasses?"
    "And what's that inside? It's bubbling away merrily."
    _mc turned tail nostrands bi ec "Oh, she didn't, did she?"
    show sayori ma e1a with say_dissolve
    "I smirk, if just a little."
    s mb b1d e1d "Surprise! Ehe~"
    show sayori ma with say_dissolve
    "Ah, that's right. I never told her about what happened with my mother."
    "It happened right after we stopped talking."
    show sayori e1a b1a with say_dissolve
    "I mean, it's alright. Honestly, I haven't seen that witch of a woman in years." 
    "To hell with it. She doesn't want them, so I may as well make use of them."
    show sayori me rdown with say_dissolve
    "Handing me the glass, she motions toward her mouth with her own."
    "She wants me to drink with her."
    "Something about this, despite having never drank with Sayori before, feels nostalgic."
    "It reminds me of how we used to hang out, dreaming of being adults."
    show sayori ma with say_dissolve
    play sound wine_glass
    "We gently connect the glasses, and a hollow ring calls out through the room."
    show sayori e3c b1b mg with say_dissolve
    "Placing the glasses to our lips, I feel the cool liquid rush down my throat."
    show black with NonBlockingDissolve(1.0)
    "The sweetness, mixed with the alcohol, warms me. Calms me."
    "It reminds me of drinking with my father on my birthday. It was the first time I'd seen the bastard since I was in middle school."
    "He'd come back to celebrate with me, even cut a business meeting short to do so."
    "It was the nicest thing he'd done for me in a long time, and the first birthday I'd had where I hadn't been essentially alone since my mother left."
    hide black 
    show sayori e1a ma b1a
    with NonBlockingDissolve(0.5)
    "Before I knew it, the glass was empty in my hand."
    s mb e1a "Ehe, you too? I'll go grab some more."
    show sayori ma with say_dissolve
    mc ea ml ba "Ah, we should-"
    s e3c mg "Shh."
    show sayori ma with say_dissolve
    "Sayori places a finger to my lips."
    s mb "No talking. Just relax. Can you do that for me?"
    show sayori ma with say_dissolve
    mc ec mh "..."
    show sayori mo e3d with say_dissolve
    "I nod wordlessly and she grins."
    hide sayori
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    "Leaning back I watch out of the corner of my eye as Sayori wanders back into the kitchen."
    show sayori turned rup at l11 
    "A few seconds later, she returns with the bottle in hand."
    s e2c mh "Saves having to get up and grab it each time, y'know?"
    show sayori ma
    mc ml ea "Well, yes, but I think that defeats the pur-"
    s b1d e1a mh "Ah, what did I just say?"
    s mi e3c "Can't you just have an evening where you don't stress over something?"
    show sayori md 
    show black with NonBlockingDissolve(0.3)
    "I look away from her concerned face."
    "I see why she's doing this now."
    "She's been worried about me."
    "Ah hell, I've been worried about her too. Worried about making her uncomfortable." 
    "Worried about projecting an image of her that doesn't exist, onto her."
    "For lack of a better term, I've been worried sick."
    "Sayori is the most important person in my whole world."
    "The last thing I would ever want is to hurt her."
    show sayori e1a b1a
    hide black
    with NonBlockingDissolve(0.4)
    mc mb "You're right. But the same goes for you. Let's just kick back, shall we?"
    mc ed "It'll do us both some good."
    s e2a mb "Yeah, that's true, in a way."
    s e1a mg "Well, if we both want to relax..."
    s mb "Why don't we play a game?"
    show sayori ma with None
    show sayori e3d mn rdown
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "The cheeky grin Sayori now wears, as she places herself down next to me, newly filled glass in hand, would normally fill me with a little apprehension."
    "But not today."
    "I trust Sayori. I think I've finally come to terms with that."
    mc ea "Yeah, sure. What did you have in mind?"
    s lup e2a mg b1b "Well, to start off with..."
    s b1a e1a mb "How about two truths and a lie?"
    show sayori ma ldown with say_dissolve
    mc mg thinking "Oh, so we each tell three facts about ourselves, and the other person needs to guess which is the lie?"
    s mb e1d b1d "Yeah! And if you get it wrong, you need to drink."
    show sayori ma with say_dissolve
    mc ml "I mean, that would be fun, but don't we know each-other too well for that sort of thing?"
    s lup b1b e1d mb "Well... There's a lot you don't know about me, I'm sure."
    show sayori ma with say_dissolve
    "I have to force myself to not double-take. Is she... flirting with me?"
    mc ef ldown mb "Ah, then quite likely the same goes for me."
    s ldown e1a b1a mh "Since it was my idea, I'll go first."
    show sayori md e2a with say_dissolve
    "I do wonder what she'll pull out to confuse me."
    "She must have been planning this, so it'll be a good one."
    s tap ma eb bc "So, three things about me..."
    s turned mc lup e1b "Ah! I actually get the best grades in my class."
    s mb e1a "I'm more comfortable jumping onto solid ground than diving into water."
    s mh "And... I prefer bubble gum to chewing gum."
    show sayori ma ldown with say_dissolve
    "Heh. Typical Sayori, starting it off easy."
    mc ed md "Well, Monika's in your class, so..."
    s tap ma ea bc "Hey!"
    show sayori eb with say_dissolve
    "She pouts."
    s ea md "That's mean, Melly..."
    show sayori eb ma with say_dissolve
    mc eh "Well, you're the one who brought it upon yourself."
    mc mb ea bb "So, you have to drink, because I got it right, right?"
    s ea "..."
    s mb "Hehe."
    show sayori turned lup e3d mn with say_dissolve
    "My smug smile evaporates in an instant."
    s ldown mo "Hahaha, I can't believe you fell for that!"
    show sayori ma with say_dissolve
    mc bd ea ml "What?"
    s e3a mb "Ha! I win!"
    show sayori ma e1a with say_dissolve
    mc eb "But, Monika's in your class, right?"
    s mn "Well yeah, but I got slightly better grades than her in the last test!"
    show sayori e3d lup rup with say_dissolve
    "She's cackling, practically rolling on the couch."
    mc ef "But that doesn't make any se-"
    _mc mh "I've always known that Sayori was smart, far more so than she lets on, but beating Monika?"
    _mc ec bi "There's something amiss here."
    mc thinking "Hmm." 
    mc ml "You say you beat Monika."
    mc ea ba mg "But in what subject?"
    show sayori e1b ldown rdown md nb with say_dissolve
    "Sayori freezes."
    s b1d e2a me "..."
    show sayori mj with say_dissolve
    "She mumbles under her breath."
    mc ldown ml "I didn't quite catch that, you know?"
    s e3c mi na "Okay, fine."
    show sayori tap eb bc ma with say_dissolve
    "Her pout returns."
    s ea "Art."
    mc bd "The way you worded that made it sound like it was overall."
    s mb bb "I know, I know."
    mc md "So, for deliberately misleading me, I think you should drink, fair?"
    show sayori turned lup mb e3d with say_dissolve
    "Sayori's grin returns, as she brings the glass to her lips once more, downing a sizable portion of it."
    s mn e3a "Hehe, but it still caught you off guard, didn't it?"
    show sayori e1a ma ldown with say_dissolve
    mc ea ba ml "I can't argue with that. I was wondering what scheme you were cooking up."
    s mb "Well, your go now! Hit me, I know I'll get it right!"
    show sayori ma with say_dissolve
    mc ed mb "Hah, we'll see."
    "Now, to think of what to say."
    "I do want to pay her back for that stunt, but I can't lie like she did."
    show sayori md with say_dissolve
    "Perhaps..."
    mc ea mg "I've always wanted to learn an instrument."
    mc ef mb "As a kid, I once made an entire dish before realising the eggs were bad, then had to run to the store to get new ones before my parents got home, and recreate the entire dish before they realised."
    show sayori ma e1b with say_dissolve
    mc bi ml "And... I've..."
    s mb "Well, you've already given one of those away."
    show sayori ma with say_dissolve
    mc eb bb nb ml "Huh?"
    s lup b4 e1a mh "I was there that day, remember?"
    show sayori md with say_dissolve
    mc ea bd na "Wait, were you?"
    s b1d e1d ldown mi "I was the one who remembered we needed money to get eggs, so we had to run all the way back to my place to get some."
    show sayori md with say_dissolve
    mc mg ba "Ha, oh yeah!"
    mc bd eb nc ml "Wait, ah, that's..."
    show sayori ma with say_dissolve
    "Bad for me."
    s mh e1a b1a "C'mon, what's your next one?"
    show sayori ma with say_dissolve
    mc bi ef pout nb "I'm thinking!"
    s b1d e1d mh "Well, think harder! It's not that hard to come up with a truth or a lie!"
    show sayori md with say_dissolve
    mc ed bd ml na "Yeah, well you try!?"
    "By now, we've placed the glasses down and are practically wrestling on the couch."
    s mb "I just did, dummy, now it's your turn, ehe~"
    show sayori ma e1a b1a with say_dissolve
    mc bg mj ef "Uh, I, ugh..."
    "I can't think of anything."
    "Nothing, except the girl in front of me."
    show sayori md with say_dissolve
    stop music fadeout 4.0
    mc ea ba nb mg "I've, uh, only ever had a thing for one person!"
    s "..."
    "Suddenly, we both stop."
    s e2a "..."
    s e2c "..."
    _mc mf "Oh."
    _mc ef bg nb "Now I've done it."
    s e1a lup mg "That one. That's the lie."
    show sayori md with say_dissolve
    _mc eb bd nb mh "How... How do I play this?"
    _mc "What does she expect me to do?"
    _mc ef bi "If I say that it's a lie, that might cause further prying."
    _mc eg mm "If I say it's the truth, then..."
    _mc eb bd mf "That's the same as a confession, right?"
    _mc eg bi mm "Argh, why do I do this to myself?"
    _mc ec mh "I've only got one option here."
    "I reach for my cup, and take a sip."
    show sayori ldown b1b e3c md with say_dissolve
    "Sayori slumps back into the couch."
    s mg "I see."
    show sayori md with say_dissolve
    mc ef ml na ba "It, ah, was a long time ago."
    s mh b1a "I've known you, our whole lives."
    s mi e1a "Why wouldn't you tell me?"
    s mh e2a b2a "We could have..."
    s mg b2b "I... would have helped you."
    show sayori md with say_dissolve
    mc ea bg mb "I know. Trust me, I know. It was never going to happen."

    play music rgb

    s b1a e1a mh lup "It was Monika, wasn't it?"
    show sayori md with say_dissolve
    mc bd ml "Huh?"
    s b4 mh e1d "I've seen the way you look at her sometimes. Even last year, when you two were in the same class."
    s ldown b1a e3c mg "I get it."
    show sayori md with say_dissolve
    mc ed bm ml "What's that supposed to mean?"
    s e1a mh "You still do, don't you?"
    show sayori md with say_dissolve
    mc ef ba "Ah, no."
    "Alright, this is a bigger hole that I've dug for myself than even I expected."
    s e2a mg "Good. She will never reciprocate. You know that, right?"
    show sayori md with say_dissolve
    mc ea bg mb "Of course. It was a long time ago, so don't worry."
    _mc eb bd mh "How the hell do I change the subject"
    _mc bf eh mm "Someone, please, please give me an out!"
    mc ea mg ba "But we don't have to worry about that. Not at all. I mean, we're trying to relax, aren't we?"
    s e2c mb nb "Yeah..."
    show sayori ma with say_dissolve
    "I can see that she's uncomfortable. I don't blame her in the slightest."
    mc mb "Hey, how about another game?"
    show sayori e1a na b1b bags with say_dissolve
    "Sayori looks at me. Her face is smiling, eager to begin another game, a dramatic shift from a few seconds ago, but her eyes..."
    "Her eyes betray her."
    "The hurt hiding there cannot be undone."
    "I... did this."
    "I hurt her."
    mc ml "Why... Why don't we play Would You Rather?"
    s lup rup nobags e1b mg b1a "Oooo~ Sounds fun! You can go first, this time!"
    show sayori ma ldown rdown e1a with say_dissolve
    mc ef ml "Alright, how about..."
    "Gotta change the subject as much as possible."
    mc ed mb "Would you rather carry ten cats, or ten dogs, if your arms were large enough?"
    s e1b mh "Oooo, good one!"
    s mj e3c b1d "Mmmm..."
    "She thinks long and hard about her answer."
    s e1a mh b1a "So, just for clarity, I can't have both?"
    show sayori me with say_dissolve
    mc ml "Nope, one or the other."
    s mj e3c b1d "..."
    s e2a b1a mg "I might have to go with..."
    s e1a mb "Dogs, because that many cats wouldn't want to be that close together."
    show sayori ma with say_dissolve
    mc thinking mg ea "Well, that's true, but neither would the dogs, would they?"
    s mb e2a b2a "Ehe~"
    show sayori ma with say_dissolve
    "That seems to have worked. Sweet."
    s e1b rup mb b1a "Alrighty, my turn!"
    s mh e1a "How about..."
    show sayori ma with say_dissolve
    "What follows, chills me to the bone."
    "I could have sworn I heard..."
    s rdown mh "Would you rather me or Monika?"
    show sayori md with say_dissolve
    $ _history_list[-1].what = _("Would you rather a glass of tea or a shot of vodka?")
    mc eb bg mf "What?"
    s "..."
    s mg "You need me to repeat it?"
    s mi "Would. You. Rather. A. Glass. Of. Tea. Or. A. Shot. Of. Vodka?"
    show sayori md with say_dissolve
    mc eg bg mb ldown "Vodka. So much vodka right now, you have no idea."
    _mc bd eb mh "Oh man, something must be wrong with me."
    s e3c mb "Well, I don't have any. So more wine will have to do!"
    s lup mg e1a "Speaking of which, we didn't decide when we would drink for this one."
    s mb e3d "Let's just drink now, ehe!"
    show sayori mg with say_dissolve
    "Without a word, I bring the glass to my lips."
    show sayori e1a ma with say_dissolve
    "I drain the entire glass dry."
    s mh ldown "Woah, you're really going hard, y'know?"
    s mg e1d b1d "Did you want the vodka that badly?"
    show sayori md e1a b1a with say_dissolve
    mc bb ea mg "Ah, no, it's uh..."
    mc ef bg mb "It's fine, don't worry about me."
    s me "..."
    s mi e1d b4 "You do realise that's the most suspicious thing you can possibly say, right?"
    show sayori md with say_dissolve
    mc ea ba mg "No, for real. I'm alright. I just..."
    show sayori e1a b1b
    "Holding the glass in my hand, I look at it with a tinge of sadness."
    s e2a b1a mh "Ooooh. These were your mother's, right?"
    show sayori md with say_dissolve
    mc ef ml "Oh, yeah, they were."
    s mb b2a e1a lup "I'm sorry about what happened."
    show sayori ma with say_dissolve
    mc ea mf "Huh?"
    s e2a b2b mg ldown "Yeah, your dad told me before he left."
    show sayori md with say_dissolve
    mc mg bd "He told you? Why?"
    s b1d e1d mh "He told me to take care of you, duh~"
    show sayori me with None
    show sayori ma b2a e1a rup:
        zoom 1.0 yoffset 145
    camera master:
        zoom 1.6
    with Dissolve(0.2)
    "She leans in, placing a hand on mine. It's only then that I realize that I'm shaking."
    s e3c mb "I'll be here for you. Always."
    show sayori ma with say_dissolve
    mc ed bg mb "Thank you. Really, thank you, Sayori. I've always been able to count on you."
    s mb "Yeah, and I on you."
    show sayori ma with say_dissolve

    scene black
    camera master
    with wipeleft
    $ say_transition = False
    $ autofocus.unblock("sayori")
    $ advance_date(minutes=17)

    "Some time passes, and we simply remain in each-other's company."
    "We continue drinking, and playing the odd game here or there."
    "Until..."
    show bg mc_living_room
    show sayori turned at i11
    hide black
    with Dissolve(0.2)
    s e2a mh "Never have I ever..."
    s mb e1d "Kissed someone other than you."
    show sayori ma
    mc turned tail nostrands ec mh "..."
    "I don't place down my finger."
    show sayori lup rup mo e3d at hop
    s "Aha! I knew it!"
    show sayori ma
    mc bm ed mg "Knew what?"
    s e1a mb "I knew you hadn't kissed anyone!"
    show sayori ma ldown rdown
    mc ea ba ml "What makes you say that?"
    s e3c b1d mi "Because it was sloppy! You had no idea what you were doing!"
    show sayori mj
    mc bd "Uh, and you do?"
    s e1a b1a mg "I-"
    s e2c md "..."
    s e1a mb "I have the right to remain silent."
    show sayori ma
    mc ed md ba "Sure, sure."
    mc ea ba mg "But you made the statement, so that means it's true, right?"
    s mh "Yeah, of course."
    show sayori md
    mc ec bi ml "So how would you know?"
    s e2a mg "I, uh..."
    show sayori md
    "Under her breath, I hear..."
    $ autofocus.block("sayori")
    s me e3c b1d "{size=-6}I may have practised on Mr Cow... once or twice...{/size}"
    show sayori md
    mc bm thinking ml ea "So how does that make me bad?"
    $ autofocus.unblock("sayori")
    s e1a b1a mb "Well, you need practice, that's all!"
    show sayori md
    mc mg "Is that so?"
    s mb "Yeah!"
    s e1d "So, you should get some!"
    show sayori ma
    mc ldown bi ec ml "And where, pray tell, do you propose I do that?"
    show sayori b1d mj
    "Her expression changes from cheeky to a hint of frustration."
    s mm e3c "Argh! Do I have to spell it out for you?"
    show bg:   
        blur 0.0
        easein 0.5 blur 2.5
    camera master:
        align (0.5, 0.2) zoom 1.0
        easein 0.5 zoom 2.0
    with None
    show black with NonBlockingDissolve(0.2)
    stop music fadeout 1.0
    play sound ["<silence 0.2>", audio.heartbeat]
    "My addled mind suddenly awakes, and small alarm bells start ringing in the back of my mind, but by then, it was far too late."
    show sayori lup rup b2b e3c mg nb
    show mc_roof zorder 1 
    hide black
    with NonBlockingDissolve(2.0)
    play music myfeelings
    $ autofocus.block("sayori")
    $ say_transition = True
    "We're already connected."
    "Her lips are nothing like they were last night."
    "No, the slow, soft feeling has been replaced."
    "There's a hunger here, like she's trying to drain my very soul out through my lips."
    _mc ea nc ma ba "In a way, it's... satisfying."
    "I return fire with just as much of the same."
    "As I do, I hear a sound. A muffled sound from Sayori."
    s e3d me nc "Mmmhh!"
    "I can't describe what it does to me, but that was all it took."
    show sayori b2a mg:
        zoom 1.02 yoffset 130
    camera master:
        zoom 2.2
    with Dissolve(0.2)
    "I take her in my arms, pulling her closer."
    "I can feel her chest against mine, and our breathing, all through our nose at this point, brushes against our cheeks, increasing in speed and reps."
    show sayori me with say_dissolve
    "I feel her grasp my shirt, pulling me in even closer."
    s "Mmmmm..."
    show sayori b1a e1d ma nc ldown rdown at i11
    camera master
    show bg:
        blur 0.0
    show mc_roof:
        alpha 0.0
    with Dissolve(0.2)
    "She breaks away, and her eyes, glazed over, leer with a hunger for more."
    $ autofocus.unblock("sayori")
    $ say_transition = False
    s mb "Now, was that practice enough?"
    show sayori ma with None
    camera master:
        align (0.5, 0.2) zoom 1.6
    show bg:
        blur 1.7
    show mc_roof:
        alpha 1.0
    show sayori na e3c rup
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "Sayori gently places her hand onto mine, turning it over, and slipping her fingers in between my own."
    s mb e1d "It isn't enough..."
    s mg "Melody..."
    show sayori me with say_dissolve
    mc ed ml nc "Sayori..."
    show sayori b2a mg e3c:
        zoom 1.02 yoffset 130
    camera master:
        zoom 2.0
    with NonBlockingTransition(fastfade)
    "Again, an explosion from within me, as our lips lock yet again. I feel her lips open, and the soft prodding at my own lips." 
    "Opening my mouth, I feel something well within me, unlike anything I'd ever felt before."
    show sayori lup mh with say_dissolve
    "Sayori places her hand behind my head, pushing it ever harder against her own."
    s me nb "Mmmm..."
    "Grasping at her shirt, I noticed her hips. Smooth, soft, and ever so close to my own."
    camera master:
        zoom 2.1
    with Dissolve(0.2)
    "I pull them even closer."
    s e3d nc "Mmm-!"
    "Her voice is like the sweetest of caramel, caressing my ears."
    "I feel her breath gently warm my cheek, and her hand, the one interlocked with mine, clenches harder, her nails digging into my skin."
    s mn e1d b1b "Ooo~"
    show sayori ma nd
    camera master:
        zoom 1.5
    with Dissolve(0.2)
    "Sayori pauses for a split second, cooing."
    s mb "That..."
    show sayori ma with None
    show black with NonBlockingDissolve(0.2)
    "At a loss for words, she leans in once again."
    hide mc_roof
    show bg:
        align (0.5, 1.0) zoom 1.3 blur 2.0
    show sayori mg b2a e3d na
    hide black
    with NonBlockingDissolve(0.5)
    "This time, instead of lying on my back, where Sayori had initially pushed me, I gently wrap my arms around her, placing her onto her own back."
    "The angle might be a little more awkward, but we pay it little mind."
    show sayori ldown b2a nc ma e1a with fastfade
    $ advance_date(minutes=5)
    "After another round, I noticed Sayori reaching for the tie on her shirt. She's already undone three of the buttons."
    "The smile she's giving me..."
    "I..."
    mc ea bb nd mg "No, wait, Sayori."
    camera master:
        zoom 1.4
    show sayori mj nb at i11
    show bg:
        zoom 1.0
    with Dissolve(0.2)
    "I sit back up."
    mc ef nb bg ml "We... can't."
    show sayori e2a md with say_dissolve
    mc ea mb bf "It's not you, or me, or anything like that."
    camera master
    show sayori  b2b rdown
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Sayori sits up, her face clouded."
    mc "We've had too much to drink."
    mc ef bg ml "Neither of us would be in this position if we weren't drinking."
    $ autofocus.unblock("sayori")
    s mg na "I know..."
    show sayori me
    "Sayori mumbles something, but I pay it no mind. As long as she understands, that's all that really matters."
    s e1a mg "But..."
    s e2a mb b2a "We can still..."
    show sayori rup ma e1a
    "She grasps my shirt."
    s mb "Stay like this, right?"
    show sayori ma with None
    show black with NonBlockingDissolve(0.8)
    "She pulls me down toward her, and with her other hand, activates the foldout part of the couch."
    "Pulling me in, she wraps her arms around me."
    "Another kiss, this one far more gentle."
    "And, as the fatigue hits me, that's how we remain."

    $ add_calendar_description(calendar_descriptions["sayori"][6])

    call week_2_thursday_sayori from _call_week_2_thursday_sayori
    return