label week_1_thursday_sayori:
    call calendar_transition(day=26, hour=7, minute=50) from _call_calendar_transition_26
    scene black with Dissolve(1.0)
    play ambient int_day fadein 5.0
    play sound_loop phone_alarm fadein 3.0
    pause 5.0

    _mc turned naked messy nostrands eg bi mm "Ugh, fine! I get it, I'm up!"

    stop sound_loop
    scene bg mc_bedroom_day_closed with Dissolve(0.4)

    _mc turned naked nostrands messy ec bi mh "Geez, that gets old real quick."
    _mc ea ba mf "Man, it's almost like I slept-"
    "..."
    extend " In..."
    "Ah."
    "Glancing at my clock, it reveals to me that, in fact, I have."
    "..."
    _mc mf "Well then."
    _mc ef "That is.."
    extend mh " unfortunate."
    _mc ec "For me."
    _mc ea "And Sayori, who was going to walk to-"
    _mc ml "Oh yeah."
    _mc mh eb bb nb "Oh, shoot!"
    _mc mg "Gotta get ready!"

    stop ambient fadeout 1.5
    scene bg s_house_day with wipeleft_scene
    $ advance_date(minutes=15)
    $ set_internet(False)
    play music school

    _mc turned nb mh "Man, that might be approaching the fastest time it's taken me to be ready, in..."
    _mc ef ma na "Well, ever, I suppose."
    _mc thinking ea mh "Maybe I did better as a kid, but..."
    _mc ma "Who knows, at this stage."
    show sayori turned lup b4 e1d mh at t11
    s "Geez, and I thought I was a late riser!"
    s e1a mb b1a "I was gonna start using you as my alarm clock, but it would seem that you're worse than I am!"
    show sayori ma ldown
    mc ldown mf "Oh, no, that was just..."
    mc ef ml "A freak accident."
    s e3c mi "Sure sure."
    s e2a b2a mb "We gotta run though, or we'll be late!"
    show sayori ma at lhide
    hide sayori
    mc ed md "You betcha!"
    "Before I even finish speaking, she's started bolting down the street."
    show bg school_street_day with NonBlockingDissolve(0.3)
    "Chasing after her, I make a mad dash for school."
    "Better to not be late, no matter what day."

    scene bg class_1_day
    camera master:
        align (0.5, 0.5) zoom 2.0
    with wipeleft_scene
    $ set_date(hour=11, minute=55)

    "My eyes are focused squarely on the board, occasionally darting to the teacher while she speaks."
    "Dancing across the page is my pen, guided effortlessly by my hand, almost as if by a force divine in nature."
    "I hardly have to spare a glance at it to know it is exactly where I expect it to be."
    "I wordlessly grin to myself, knowing that things are right with the world, at least for a brief moment."
    play sound school_bell
    camera master
    with Dissolve(0.2)
    $ set_date(hour=12, minute=5)
    "With the tolling of the bell, I get to my feet and pack my things."
    show yuri turned at t11
    "I give Yuri a wave as she shuffles out of the room, no doubt headed for the music room to meet Monika."
    show yuri e3c at dip
    "She smiles warmly in response, returning my smile, before bowing politely."
    show yuri at thide
    hide yuri
    _mc turned "She's wound tight, but over the past week, she's been talking with me in class, asking questions, opening up."
    "It's almost an unfamiliar feeling, having classmates and friends."
    _mc eg bi "God, that sounds even sadder than I thought it would."
    "Picking up my bag, I sigh to myself."
    _mc ec ba mh "Guess I'll go find somewhere to eat lunch."

    scene bg school_corridor_3_day
    camera master:
        align (0.5, 0.5) zoom 1.5
    with wipeleft

    _mc turned ec mh "Agony."
    "Walking the halls, that's how I'd describe the general mood among the other third-years."
    "Our mid-semester results are back - Looks like most people didn't fare as well as they expected."
    _mc bi ma "Sucks to be them. Should have studied better."
    "Another sigh escapes my lips. I don't really believe that, and I know it."
    "Part of me wishes I could help some of them, though I can't for the life of me imagine why."
    "I hardly have the time to keep myself in fourth, let alone help someone else."
    camera master
    with Dissolve(0.2)
    "My feet come to a halt."
    _mc eb nb mh ba "Wait- When did I start caring? Is this Amelia's doing?"
    _mc ec bi "... Or Sayori's?"

    scene bg school_corridor_2_day with wipeleft
    $ advance_date(minutes=3)
    show aika turned ed me at t11

    "While wandering the second floor, I spy a rather disoriented Debate Club President."
    mc turned mb "Lost?"
    a mb "Me? Never..."
    show aika me
    "She hardly acknowledges me, her face still turned to the side."
    a mf "Have you seen -"
    show aika rhip eb
    extend mb " No, nevermind."
    a ed "She's a big girl."
    show aika me
    mc thinking ml "What, a little sister or something?"
    a ea mf rdown "... You could say that. What brings you down the the second-year classrooms?"
    show aika me
    mc ef mb ldown "Honestly, just going for a walk."
    a mb ba "Got a destination in mind?"
    show aika ma
    mc ea ml "The garden, if I make it that far."
    a smug mb "Company?"
    show aika ma
    mc ed md "Not opposed."
    show aika turned ec ma
    "She grins, her previously apprehensive look finally completely shaken from her face."
    show aika ea
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("aika")
    $ say_transition = True
    "Seemingly content with our broken, almost offensively lacking-in-context conversation, something one might call an affront to language, she tags along by my side."
    mc ef mg "You don't have to. I'm not exactly all that interesting."
    a mb eb "That's exactly what the most interesting people say~"
    show aika ma with say_dissolve
    mc bd mb "Touché."
    "I grin to myself, not unpleased by this turn of events."
    _mc eg bi ma "I mean, don't punch a gift horse, right?"

    scene bg school_courtyard_day
    camera master
    show aika turned at i11
    with wipeleft_scene
    $ advance_date(minutes=3)
    pause 0.02
    show bg:
        blur 2.0 offset (-150, -100)
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)

    "We settle onto a bench, and as I relax, I notice her shuffle a little closer to me."
    a eb mb "So... I heard a rumour that this club of yours was a touch more than you signed up for~"
    show aika ma ea with say_dissolve
    mc turned eb mg nb "I- I suppose that's one way to put it?"
    a smug mb "Been accosted by so many new people, I'll bet you hardly know which one to pursue~?"
    show aika ma with say_dissolve
    mc bf ef mb nc "I- I have no idea what you mean by that."
    show aika turned ec ma with say_dissolve
    "She grins widely."
    a mb "Of course you don't~"
    a mc ea rhip lpoint "Fear not, of course - I'm here to help."
    a md ec "I'm known for my... shall we say, sway with the masses?"
    show aika ldown ea ma with say_dissolve
    mc ec bi na ml "Yeah, now you've lost me. Is that just a euphemism for 'sleeping with people'?"
    show aika me rdown with say_dissolve
    "Aika looks almost offended at my statement."
    a ed bc mb lpoint "M- Me? No, never! Well - Not {i}never{/i}, I just- I haven't found the right person yet!"
    show aika ma with say_dissolve
    mc ea bd ml "... So what the hell were you alluding to?!"
    a ldown ea bb mf "Th- That I can get people to talk to you? H- How did you even get that idea?"
    a rhip mb "Is your mind perpetually in the gutter or something?"
    show aika ma with say_dissolve
    mc ba mh ec "..." 
    _mc ef bf ma "Got me there..."
    mc mg ea bb "I- In any case, how about- Your lunch! How is it?"
    show aika ba eb me rdown with say_dissolve
    "Aika readjusts herself, seemingly patting herself down and picking up the lunchbox she'd set to the side."
    a ea mf "Yes, indeed. It's nothing dramatic - Something my father put together for me this morning as I was late getting up."
    show aika me with say_dissolve
    mc ml ec ba "Oh, you live with- Of course you do- Never mind..."
    show aika bb with say_dissolve
    "She throws me a look, but thankfully doesn't pursue her train of thought vocally."
    a ba mf "... How's life?"
    show aika me with say_dissolve
    mc mb eg bi "Damn, and I thought I was terrible at small talk."
    a rhip eb mf "In my defence, in debate, all there is is 'big' talk. I don't get all that much practice."
    show aika me ea with say_dissolve
    mc ef mb ba "Well, that makes two of us."
    a smug mb "What, are you the leader of a Debate Club too, all of a sudden~?"
    show aika ma with say_dissolve
    mc ed md "Hah, I wish."
    show aika turned me with say_dissolve
    mc ea mg bb "No, just... I dunno, small talk's not really my thing. If I'm talking, it tends to be about the big things."
    a turned mf "That so?"
    show aika me with say_dissolve
    mc ba ef ml "I guess. Never been one for wasted breath."
    show aika ec ma with say_dissolve
    "She chuckles a little."
    a ed mb "{size=-7}Boy, do I know...{/size}"
    show aika ma with say_dissolve
    mc ea mg "So have you been up to much today?"
    a ea rhip mf "Nah, not me. Unless you count endless paperwork for this club..."
    show aika me with say_dissolve
    mc ed md "Hey, whatever floats your boat~"
    a ed mf "One day, it might just sink it - You won't know until you put that last barrel on when you'll start taking on water."
    show aika me with say_dissolve
    mc thinking mg ea "Interesting way to put it. Are you stressed?"
    show aika ea me rdown with say_dissolve
    "She seems to consider my question for a moment."
    a mf "I wouldn't call it 'stressed'? More that I think I've bitten off a little more than I'd typically be interested in chewing."
    show aika me with say_dissolve
    mc ldown mb eg "Hah, don't worry, I absolutely know that feeling."
    show aika ma 
    camera master
    show bg:
        offset (0, 0) blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She shares my grin, getting to her feet as she glances toward the garden."
    mc mb ea "Shall we?"
    $ autofocus.unblock("aika")
    a ec mb "Lead the way~!"
    show aika ma with None

    stop music fadeout 2.5
    scene sky_day at moving_sky with sayori_pov(True)
    pause 0.4
    scene bg school_rooftop_day with Dissolve(1.5)
    $ set_pov("s")
    $ set_date(minute=14)
    play music rgb

    "I swing the door to the roof open, listening to the loud screech it makes."
    _s turned e3d "Never gets old, ehe~"
    show natsuki turned e1b b3a mh nb at t11
    n "There you are! I was..."
    show natsuki me b1d
    s e1d b1d mb "Starting to get worried?"
    n cross e2a mm "N- No! Why would I be worried?"
    show natsuki md with None
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.25) zoom 1.5
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("natsuki")
    "Sitting at our regular spot, my best friend pouts as I approach her."
    s mn b1a e3d "Because you looooove me~?"
    n b1a nc mb "A- As if!"
    show natsuki ma with None
    show natsuki na 
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    "I giggle as I take my seat next to her."
    $ autofocus.unblock("natsuki")
    n turned lhip b3a mh "... Here."
    show natsuki ldown mj at dip
    "She pushes a lunchbox into my hands before turning away from me."
    s b1d e1d mb "Someone's in a mood today~"
    n e2a b1d mm "I- You-"
    n e3c md "Hmph."
    show natsuki e1a b1a mj
    "I buff her shoulder, and she turns back around."
    n turned lhip e2a mh "I didn't make it for you, or anything..."
    show natsuki mj
    s mk e3c b2a "Didn't you? Aww..."
    n b1d mg "N- No, I mean, I did, but-"
    show natsuki md
    s mn b1a e3d "Hehe~"
    show natsuki e1a b1a ldown
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("natsuki")
    "I wiggle my butt into a more comfortable position, before cracking open the lunchbox."
    s e1b mu "Ooooh~ Is that fried chicken? Where'd you get all this?"
    n b3a mg "It's..."
    n e2a b1d mh "I don't wanna talk about it."
    show natsuki mj with say_dissolve
    "I frown, putting the box to the side."
    s e1a mh b1d "We talked about this, Nat."
    show natsuki md with say_dissolve
    s mg b1a "No secrets."
    n e3c mm "I... It's not that simple. Besides, can't you just be happy that I made something for you?"
    s mb "I can."
    show natsuki e2a md with say_dissolve
    "She bites her lip."
    n e1a b3a mb "I saw it on sale yesterday, and it reminded me of you."
    show natsuki mj with say_dissolve
    s mh "Where'd you get the money for it?"
    n e2a b1d md "..."
    "She glances away, but it tells me all I need to hear."
    s e2a b1b mh "You can't keep pulling money from that little pile of savings every time you want to do something nice for me, Natsuki."
    n mg e1a b1a "Why not?"
    show natsuki mj with say_dissolve
    s e1a b1a "Because we both know that pile isn't going to last forever."
    n e2a b1d "..."
    n mg "But I want to."
    show natsuki md b1a with say_dissolve 
    s b1b e2a me "I..."
    stop music fadeout 3.0
    camera master
    hide natsuki
    show bg:
        blur 0.0
    show sky_day at moving_sky
    with NonBlockingDissolve(2.0)
    "I furrow my brow as I glance over the edge of the roof."
    "The view of the ocean from here is pristine, so much so that you can almost hear it from here."

    play music myconfession

    n turned b1d mg "Is that so wrong?"
    s mg "... I don't know why you try so hard."
    $ say_transition = False
    $ autofocus.unblock("natsuki")
    n mh b2a "Because I know that if I don't, you won't eat."
    n e1d b1d mg "... And I know that even when you do, I have to make you keep it down."
    n mh b1a e2a "You can't keep putting off that appointment, Sayori."
    s md "..."
    s mg "I'd just be..."
    n e1d b1d mm "Don't you {i}dare{/i} say it."
    hide sky_day
    show natsuki turned mj e1a b1a at i11
    with NonBlockingDissolve(0.5)
    "Natsuki grabs my sleeve."
    n mb b2a "I'll go with you, just - Please go, this time."
    show natsuki mj
    s mg b1a "... I'll consider it."
    n lhip rhip e1d b1d mi "No, just 'do'. You've been 'considering it' for two years."
    show natsuki b1a me e1a
    s e3c b1b mh "Well, maybe - Maybe I don't want to go. Maybe-"
    show natsuki b2a ldown rdown
    "She doesn't say anything, but her eyes tell me all I need to hear."
    n cross mg "Sayori... Do you trust me?"
    show natsuki md 
    s mg b2c e1a "... I do."
    n e2a mh "Then why does it feel like, every single time, you're doing your hardest to push me away?"
    show natsuki mj
    s mb b2a "... Because that's what I'm best at."
    s e2a b2c "It's the only thing I'm good at."
    show layer master:
        align (0.0, 0.5) zoom 2.2
    hide natsuki
    with Dissolve(0.2)
    "I can't look her in the eye."
    n turned mb e2a b2a "Everything I've done... I've done because I wanted to help you the way you helped me."
    s e1a nb "And I appreciate-"
    n mm e1d b1d "No, I don't think you do."
    s mj b2b "..."
    n e2a mg "... I'm sorry, that was uncalled for."
    s mh e3c "No... You're right. I do just brush you off. But- It's not because I don't trust you."
    s b1b e2a na mg "It's because..."
    call close_eyes(0.5) from _call_close_eyes_12
    "For a moment, I close my eyes, trying to find the words she wants to hear."
    "The words that she might find acceptable."
    "But they don't come."
    show layer master
    show natsuki turned e2a b2a md at i11
    call open_eyes(1.0) from _call_open_eyes_8
    "Instead I'm left with unceasing questions."
    n b2a mh "I just... It hurts when I see you hurting."
    n e1a mb "I don't want you to feel like that."
    show natsuki mj
    s mh e1a "Then why do you deflect the way you do?"
    $ autofocus.block("natsuki")
    n cross b1d e2a md nb "..."
    "She turns away from me once more."
    s b1a "You talk about helping others all the time, but when was the last time you stopped to let someone else help you?"
    show natsuki mj
    s b2b mb "When was the last time you stopped to help yourself?"
    $ autofocus.unblock("natsuki")
    n e3c mm "... I don't need help. I don't {i}deserve{/i} it."
    show natsuki mj
    s e2a b1b mg "... That's exactly how it feels."
    show natsuki turned e1a na b1a md
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("natsuki") 
    "She turns back and looks me in the eye."
    n b2a mb "It doesn't have to be much. Just... I make these for you to enjoy. You don't... You don't have to eat them."
    show natsuki ma with say_dissolve
    s e3c mh "I know."
    s b1a mi "You're just making sure that I've always got something."
    s e1a b2a mb "... Thank you."
    n b1d nb e2a mb "D- Don't mention it..."
    show natsuki nc ma lhip with say_dissolve
    "She flushes a little, scratching her cheek."
    n b1a mh na ldown "I, ah... Should probably eat my own now..."
    show natsuki md e1a with say_dissolve
    s b1a mh "It's all gonna be cold. Do you wanna go for a walk and reheat them?"
    show natsuki b3a with say_dissolve
    "Her eyes light up, if just a little."
    n mc "Y- Yeah!"
    extend cross e2a b1d mh " I- I mean, sure, if that's what you want..."
    show natsuki ma with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I chuckle as I stand up, offering her a hand."
    s e3d mb "See? Not so bad when the shoe's on the other foot, no?"
    $ autofocus.unblock("natsuki")
    n turned e1d b1d mh "That sounds like something Yuri would say..."
    show natsuki md
    s mn "Ehe~!"
    s e1a mb "I've been practicing!"
    show natsuki b3a e3c ma at dip
    "She takes my hand, and after getting to her feet, seems to linger holding onto it for just a touch longer than I think she intended to."
    _s md "... One of these days we're going to have to talk about it, but..."
    _s e2a ma "Not today."
    _s e3c "Not right now."
    n e1a mb "Ready to go?"
    show natsuki ma 
    s e3d mb "Yep!"
    show natsuki e3c at thide
    hide natsuki
    "Our presence is punctuated the same way we arrived - The creak of the door."

    stop music fadeout 1.5
    scene bg club_day with mc_pov(True)
    $ set_pov("mc")
    $ set_date(hour=15, minute=20)
    play music ohayou

    _mc turned mh bb eg "What a day."
    call close_eyes(1.0) from _call_close_eyes_13
    _mc mi "Instead of afternoon classes, we were all brought to the lecture hall to discuss careers and university."
    _mc bi ma "Makes me almost wish I'd skipped it and went back to bed."
    _mc ec ba mh "No, that's not strictly true."
    _mc eg ma "Nah, not in the slightest."
    _mc "I got to sit next to Sayori."
    _mc bb "We were refreshing our old hand signal code, and telling each-other funny, stupid stories the entire time."
    _mc md "Hah. It was the best."
    _mc ma bg "God, I've missed this."
    _mc mh "I've missed her."
    _mc "I just wonder if she's felt the same way, the past few days."
    _mc ba ma "Maybe she has. But honestly, no matter what, I'm happy."
    _mc bb "Being around her, being here at the club, has brought me more joy than I've had the past three years of high school."
    _mc "The past couple of days have been..."
    _mc ba "Like a dream."
    call open_eyes(0.24) from _call_open_eyes_9
    _mc bb eb mf nb "Oh, right, I was supposed to be reading."
    _mc ec thinking bi mh "Let's see... Where was I?"
    pause 0.5
    _mc ea ba mf na "Hmm?"
    "Something out of the corner of my eye catches my attention."
    show bg:
        align (1.0, 0.6) zoom 1.8
    show sayori turned lup md b1b at i44
    with Dissolve(0.2)
    "When I look over, I see Sayori moving her hand beside her desk."
    _mc ma ldown "Oh, it's the code."
    show sayori ldown with say_dissolve
    _mc ec mf "'Come..." (what_underline=True)
    show sayori b1a lup with say_dissolve
    extend ea mh " here.'" (what_underline=True)
    _mc md bi eg "Oh, if that's all she wanted, she could have just asked."
    show sayori rup e1b b2a with say_dissolve
    _mc ea mf ba "'Wait.'" (what_underline=True)
    show sayori ldown rdown e1a b2b with say_dissolve
    _mc ec "'Not now.'" (what_underline=True)
    show sayori e2a me with say_dissolve
    _mc bd mh "'In...'" (what_underline=True)
    show sayori lup e1a b2a ma with say_dissolve
    _mc ea ba "'Two minutes.'" (what_underline=True)
    show sayori ldown with say_dissolve
    _mc ef "Huh. I wonder why."
    _mc eg ma "I suppose it's fine though."
    show sayori rup e2a mc with say_dissolve
    _mc ec mh "'Let..." (what_underline=True)
    show sayori tap eb with say_dissolve
    extend ed " me..." (what_underline=True)
    show sayori turned lup mb e1a b2b with say_dissolve
    extend " finish the chapter.'" (what_underline=True)
    show sayori ma ldown with say_dissolve
    _mc ea mf "Really?"
    _mc ec ma "Alright, sure... I'll play along."
    show sayori e1a b1a with say_dissolve
    _mc ea mh "Gotta respond myself."
    _mc ma "'Sure.'" (what_underline=True)
    show sayori rup e3c with say_dissolve
    "She gives me one last movement, acknowledging my confirmation."
    _mc eg "I suppose I'll find out what she's after in two minutes."
    
    scene bg club_day with wipeleft_scene
    $ advance_date(minutes=2)

    _mc turned mh "Alright, surely that's enough time, right?"
    show bg:
        align (1.0, 0.6) zoom 1.8
    show sayori turned md b1b at i44
    with Dissolve(0.2)
    "I motion to her, only for her to respond with-"
    show sayori tap ma ea bc with say_dissolve
    _mc ec "'Not yet. Two more minutes.'" (what_underline=True)
    show sayori eb with say_dissolve
    _mc me eg bi "Ah, geez. This is going to be my whole afternoon, isn't it?"
    
    scene bg school_street_afternoon
    show sayori turned:
        i11
        matrixcolor TintMatrix("#ffeede")
    with fade
    $ set_date(hour=16, minute=47)

    mc turned mj ec bi "I hope you're happy."
    s mb b1d "C'mon, it was good!"
    show sayori ma
    mc eb bd ml "Twelve times."
    s tap eb ma bc "It's not my fault! I thought you'd give up by like the third!"
    show sayori ea
    mc bj mg "You made it seem important!"
    s turned mb e1a lup b1a "If it was important, I would have told you!"
    show sayori ma
    mc ml ec bi "So why use the signal?"
    s ldown mn e3d "Because it's fun!"
    show sayori ma with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "She beams at me, rolling her head onto my shoulder as we walk."
    s mb e1d b1d "Because I knew you'd pick up on it, and I did originally want you to come over~"
    s mh e2a b1a "It was just that, when it came time for you to come over, I'd already finished the chapter and was half-way through the next one."
    show sayori md with say_dissolve
    pause 0.3
    show sayori e1a with say_dissolve
    pause 1.0
    s mi b1d e1d lup "Oh, c'mon, don't give me that look! It's a good book!"
    show sayori mj with say_dissolve
    mc ml ef bi "You had me worried!"
    s e3d mb b1a ldown "Oh, you're always worried. Lighten up, take a joke~"
    show sayori ma with say_dissolve
    mc ml ec "I will, when you learn to tell them properly."
    hide sayori
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    "At this, Sayori unclings herself from me."
    s turned e2a b2a mg"What, you don't like them?"
    mc ea ba mg nb "N- No, it's not that I don't like them, just..."
    show sayori lup:
        matrixcolor TintMatrix("#ffeede")
        i11
    camera master
    with Dissolve(0.2)
    "I turn around and face her, and she seems a little down."
    "Staring at the ground, hiding her face in her fringe."
    mc ea bf na mg "C'mon, I didn't mean it like that. Your jokes are great."
    s mb e3a b1a "Ehe~ They sure are!"
    show sayori ma e1a ldown
    _mc mf ba "Did she just-"
    _mc bd eb nb mh "She just guilt-tripped me!"
    _mc mf ea na "That's..."
    show sayori md
    _mc ec bi mh "Rude."
    _mc ef "I don't know how I feel about that. Has Sayori always been..."
    _mc ea ba "No, she can't have. She's better than that."
    _mc bg "Right?"
    s e1d b1d mb "Oh, don't be so sour. I won, just admit it~"
    show sayori ma
    mc ba ml "That's not..."
    _mc thinking mh "Does she not realise she did it?"
    _mc ec "Maybe I should tell her, just in case."
    mc ml ldown "Hey, Sayori, just before-"
    s mb e1a b1a "Yeah? What's up?"
    show sayori md
    mc ea bg "You know, that was a kinda underhanded thing to do, right?"
    s rup mh b4 "What'd I do?"
    show sayori md
    mc ef mg "I- I mean, you kinda..."
    _mc bi mh "Something about it feels... wrong. Like I'm ruining her innocence."
    _mc "..."
    extend nb " Innocence..."
    show sayori rdown b1a 
    _mc nc eg mm "Nonono! Come on, stop!"
    _mc eb nb bd mh "What is wrong with me?!"
    mc eb ba mg "N- Never mind, I, ah..."
    mc md ba eh na "Yeah. Never mind."
    s mb "Okay!"
    s e3d mn "If you say it's fine, it must be!"
    show sayori ma lup rup b2b
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "She nonchalantly wraps herself around my arm, dragging me further down the road."
    s e3c mh "C'mon, don't sweat the small stuff." # im stuff
    s b1a e1a mb "Walk with me!"
    show sayori ma with say_dissolve
    "Hah, look at her, so confident."
    "Almost like she's enjoying this."
    s mh "Yeah, of course I'm having fun."
    s e3c mb "I'm with you."
    show sayori ma nc with say_dissolve
    stop music fadeout 3.0
    "Huh?"
    show sayori nc
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "My whole body just... stops."
    "Sayori..."
    extend " she's blushing."
    $ autofocus.unblock("sayori")
    s mg "You make everything more fun, you know."
    s nb b2c e1a mb "It was... hard. When you left."
    show sayori mj
    mc ef bg ml "Yeah. It was hard on me, too."
    s b2b e2a mg na "Th- Then, why did-"
    s me "..."
    show sayori ldown rdown md

    play music myconfession

    "She lets go of my arm."
    s e1b b1a mk nb "Sorry, I didn't mean to..."
    show sayori e1a md
    mc eb bf mg "No, it's alright. It's..."
    show sayori e1a tears_a me b2b
    mc eg bg ml "I'm sorry."
    mc mb "I'm... really, really sorry."
    mc ef ml "For everything."
    s mg e3c "... Yeah. Me too."
    s mb e2a b2a notears "I guess... We both..."
    show sayori e1a tears_a mj b2c
    mc bi mg "No, it was my fault."
    mc ea bf ml "I did this."
    s e3c tears_a mg b2b "Yeah, but..."
    s mk tears_b b2a "You... You came back."
    show sayori mm lup rup
    camera master:
        align (0.5, 0.2) zoom 1.8
    show bg:
        blur 2.5
    with Dissolve(0.5)
    $ autofocus.block("sayori")
    $ say_transition = True
    "Tears start to well in her eyes, and she wraps her arms around me."
    s mb e1a b2c nc "You came back, and that's all that matters."
    show sayori ma with say_dissolve
    mc ef bg mf "... Yeah."
    _mc bi mh "I don't think I could ever tell her that I didn't know she was there in the first place."
    _mc eg "That it was Monika who made me join, and the thought of getting closer to her."
    _mc mm "Nope, that's going to the grave with me."
    show sayori e3c ma b2b with say_dissolve
    pause 1.5
    _mc ec mh "Man, she..."
    "Her hair has a hint of strawberries today. And... coconut?"
    "Either way, it's heavenly."
    show black with NonBlockingDissolve(0.4):
        alpha 0.5
    _mc mh bg eg "I don't want to let her go..."
    _mc ma "I don't think I could, if I tried."
    _mc ea mf bf "Here we are, just embracing on the sidewalk."
    hide black
    s me e1a tears_a "You..."
    s mg "You really mean it?"
    show sayori mj with say_dissolve
    mc bg eg ml "I'm... so sorry. I don't want to lose you again."
    s nd mg e3c notears "You... You won't. I promise."
    s e3d b1a mb "We'll be together forever, right?"
    show sayori ma with say_dissolve
    mc bf ea mb "Yeah. Best friends, forever."
    s md b2b e1a "..."
    s me e2c "Yeah."
    show sayori md with say_dissolve

    scene bg mc_living_room 
    camera master
    with fade
    $ set_date(hour=20, minute=2)
    $ autofocus.unblock("sayori")
    $ say_transition = False

    "A sigh escapes my lips as I relax into the sofa, dinner in hand."
    _mc turned eg mh "Today has been long."
    _mc bg "Too long"
    "The television flashes with pictures of images that I hardly notice."
    "Even my plate of food sits mostly untouched."
    "My hands instead find themselves occupied with my phone, thumbing through old text messages."
    phone discussion "mc_dadmc"
    "Messages from the bastard who ran from me..."
    phone discussion "mc_momc"
    "Messages from the witch who abandoned me..."
    phone discussion "mc_s"
    "And messages from the girl who I'd dreamed of spending the rest of my life with."
    "My gut tears at me as I finally open the messages left on read for five years."
    _mc ec ba "Read. I left her on read."
    _mc bb eb mm "... What the fuck is wrong with me?"
    _mc bf mj "Look at this... She was trying to check up on me, trying to help."
    _mc mm bi eg "And all I could do was ignore her."
    phone end discussion
    $ phone_available = True
    "Standing up, I pocket my phone, picking up the meal and walking back to the kitchen."
    "If I'm not going to eat it, I can at least turn it into lunch for tomorrow."
    "..."
    _mc ec mf "Coward."

    stop music fadeout 2.0
    scene black with Dissolve(1.5)
    pause 1.0
    hide black
    show bg mc_bedroom_night_open
    with NonBlockingDissolve(5.0, time_warp=_warper.ease)
    $ set_date(hour=22, minute=22)
    play ambient ext_night fadein 5.0

    "The day and its labours may be over and done with..."
    "... But I'm still far from my own point of closure, let alone sleep's grasp." 
    camera master:
        align (1.0, 1.0) zoom 2.0
    with Dissolve(0.2)
    "Even as I lie here in my comfortable bed, in my darkened room."
    "The moon's gentle glow providing sole illumination."
    "The wind whispering conspiratorially through the leaves of the trees outside my window."
    "Conditions that usually spell a surefire recipe for instant slumber."
    "Not this time, however."
    "My mind is wide awake, firing on all cylinders."
    "The cinema of my memory playing and replaying that special moment Sayori and I shared on the sidewalk."
    "With special emphasis on the warmth of her embrace."
    show white_flashback onlayer above_master
    show sayori turned e3d onlayer above_master:
        matrixcolor TintMatrix("#ffeede")
        i11
    show bg school_street_afternoon as stuff onlayer above_master:
        blur 2.0
    camera above_master:
        align (0.5, 0.2) zoom 1.5 
        flash
    "The feel of her skin against mine."
    show sayori rup lup e3c tears_b b2b nc
    show bg school_street_afternoon as stuff:
        blur 2.0
    camera above_master:
        zoom 1.8
        flash
    "That startling, intoxicating new fragrance of her hair."
    _mc turned casual messy nostrands bi eg mh "I can't. I shouldn't."
    _mc "Especially not after previously contemplating the innocence and wholesomeness of my childhood friend." 
    show sayori e1a md b4 notears na ldown
    show bg school_street_afternoon as stuff:
        blur 0.0
    camera above_master:
        zoom 1.0
        flash
    _mc "Not to mention the potential of it being irrevocably sullied."
    _mc ba "But the evocation is so very strong..."
    _mc ef "... And my flesh is all too weak."
    $ clear_layers("above_master")
    "I grit my teeth and pass one hand wearily over my face."
    _mc eg bi mm "Dear Lord. I'm so pathetic."
    $ renpy.music.set_volume(0.2, 6.0, "ambient")
    show black with NonBlockingDissolve(6.0):
        alpha 0.8
    "The conflicting emotions within me build to an intense pitch."
    "Their friction giving rise to a feverish heat."
    "Spreading within my chest."
    "Spreading outwards... and below."
    "Heavenly reminiscings now giving way to hellfire."
    $ renpy.music.set_volume(1.0, 0.5, "ambient")
    camera master
    hide black
    with Dissolve(0.2)
    mc ea ml ba "... Gotta crank the A/C."
    "Which, in the event, does absolute jack-all."
    "Nor does me doffing my pyjama top, or tossing and turning restlessly in a desperate bid to cool off."
    "Perhaps an extinguisher?"
    show expression "#06020e" zorder 1 as stuff
    show bg:
        align (1.0, 1.0) zoom 2.0
    with NonBlockingDissolve(0.6)
    stop ambient fadeout 1.0
    "I pull one of my pillows over my head, attempting to block the scandalous thoughts that are flowing unbidden."
    "Then all of a sudden, that incomparable odour of strawberry and coconut intensifies."
    "To a level far stronger than a mere recollection could grant my senses."
    play sound heartbeat
    mc naked eb bd ml "Sayori? How the devil-?"
    show sayori turned e3c md b1b pyjama2 noblink:
        i11
        matrixcolor TintMatrix("#4c508d")
    with NonBlockingDissolve(1.0)
    play sound_loop static fadein 40
    "My words trail off into stupefied silence as I behold her emerging from under the covers, as if by magic."
    "Or rather, witchcraft."
    play sound heartbeat
    camera master:
        align (0.5, 0.15) zoom 3.9
    with NonBlockingTransition(fastfade)
    "That scented auburn bob teasingly tousled."
    play sound heartbeat
    camera master:
        yalign 0.22 zoom 3.1
    with NonBlockingTransition(fastfade)
    "Eyes heavily lidded."
    play sound heartbeat
    camera master:
        yalign 0.31
    with NonBlockingTransition(fastfade)
    "Lips pouting tremulously."
    play sound heartbeat
    camera master:
        align (0.55, 0.45) zoom 4.5
    with NonBlockingTransition(fastfade)
    "Her all-too-familiar nightdress, harkening back to more carefree times between us, slipping past her shoulders."
    play sound heartbeat
    camera master:
        align (0.525, 1.0) zoom 5.0
    with NonBlockingTransition(fastfade)
    "Revealing endowments far more ample than anything I could have envisioned or expected."
    play sound heartbeat
    camera master:
        align (0.55, 0.45) zoom 4.5
    with NonBlockingTransition(fastfade)
    "Rising and falling hypnotically, like a creamy tide beneath the moonbeams."
    play sound heartbeat
    camera master
    with NonBlockingTransition(fastfade)
    "Questioning where she has come from and why, is longer foremost in my mind."
    play sound heartbeat
    camera master:
        align (0.55, 0.45) zoom 4.5
    with NonBlockingTransition(fastfade)
    "Not while she lies here before me, so irresistibly presented."
    play sound heartbeat
    show sayori e1a b1a
    camera master:
        align (0.5, 0.2) zoom 3.0
    with NonBlockingTransition(fastfade)
    "Before I knew it, I had narrowed the distance between us to mere inches."
    play sound heartbeat
    show sayori lup rup mg e3d
    with NonBlockingTransition(fastfade)
    "And then I am kissing her, long and full, square upon that pretty little mouth."
    play sound heartbeat
    show sayori me nb
    camera master:
        yalign 0.34 zoom 4.0
    with NonBlockingTransition(fastfade)
    "Then onward, in a wet trail that leads past her chin..."
    play sound heartbeat
    show sayori b2a nc 
    camera master:
        align (0.55, 0.407) zoom 4.5
    with NonBlockingTransition(fastfade)
    "... Down her collarbone, and perhaps further still."
    play sound heartbeat
    show sayori ldown rdown md e3c b1b na
    camera master:
        align (0.5, 0.2) zoom 3.0
    with NonBlockingTransition(fastfade)
    "She goes limp in my arms as they land home." 
    play sound heartbeat
    "Hard enough to leave marks upon her previously flawless skin."
    play sound heartbeat
    "Flags of conquest upon terra incognita."
    play sound heartbeat
    camera master:
        yalign 0.4 zoom 4.0
    show sayori me e3d
    with NonBlockingTransition(fastfade)
    "Instinct takes over now, as my hands, my mouth, all of it bows to the lust I'd once chained so strongly."
    show black with NonBlockingDissolve(2.0)
    "When at long last, we descend from that hallowed light above the cloudline, I continue to hold her in near total silence."
    "Floating, trancelike, in that blissful, post-climactic state, my contentment manifests into words."
    show sayori e1a md b1a
    hide black
    camera master
    with NonBlockingDissolve(2.0)
    "Which spill freely from me, as my passion did but minutes earlier."
    mc nd ec ml ba "This is all I've ever wanted."
    mc ea md "You're all I've ever wanted."
    mc ec mb "You're mine, Sayori."
    mc eb "And always will be."
    show sayori e2a with NonBlockingDissolve(0.4)
    "..."
    "No response to my desirous declaration is forthcoming."
    camera master:
        align (0.5, 0.2) zoom 2.2
    with NonBlockingDissolve(0.3)
    "Giving me pause, for her face is abashed."
    "Not necessarily surprising, given how vigorously we exerted ourselves."
    "But astonished I still am, regardless."
    hide sayori
    stop sound_loop
    "My eyes meet nothing but rumpled bedding."
    camera master
    "My words echo through an empty room."
    "And what I am enclasping against me, like all the gold in the world..."
    mc nb eb mf bb "No way."
    hide stuff
    play ambient add_playback_info(audio.ext_night, 5.0)
    "... is naught but my saliva-stained pillow."
    show bg:
        easein 0.2 zoom 1.0
    "I sit bolt upright, casting frantically about me."
    "Staring disbelievingly."
    "Jaw slack."
    "Beholding no evidence whatsoever that I was anything but alone."
    "No evidence apart from..." 
    mc nd ml "Hold the phone."
    mc nb bc mg "Hold on a goddamn minute."
    "Surely my nose doesn't deceive me."
    "Surely that's the faint, lingering smell of fruit?"
    "But even as I think I discern it, it too, is gone." 
    "Like dust in the breeze."
    show sky_night at moving_sky 
    show sky_stars
    show bg mc_bedroom_night_open
    with NonBlockingDissolve(1.0)
    play sound train volume 0.03
    "Outside, morning stars are faintly visible in the east, the Milky Way is moving to the west..." 
    "... Distant thunder is rumbling, and the clickety-clack of a train barreling down the railroad tracks rises above its bass in a metallic staccato."
    camera master:
        zoom 2.0 align (1.0, 1.0)
    hide sky_night
    hide sky_stars
    with NonBlockingDissolve(1.0)
    "Sinking back down onto my bed in utter confusion, I ask myself..."
    mc eb bf mg "What in the blue blazes just happened?"
    _mc mh bg "No..."
    _mc mf "There's no way."
    _mc ef "I couldn't have."
    _mc eb mh "That's... heinous"
    _mc eg mj "Abominable."
    _mc bi mm eg "Oh, God, what have I done?"
    _mc ea mf bg "It was just a dream, yet..."
    "Gazing down at my hands, I see them shaking."
    _mc eb bf ml "No..."
    _mc eg bg mf "How could I?"
    _mc mh "Sayori..."
    show black zorder 1 with NonBlockingDissolve(0.2)
    "I close my eyes, blinking rapidly, desperate to remove the images flashing through my mind."
    show expression "#06020e" zorder 1 onlayer above_master
    show sayori turned pyjama2 md onlayer above_master:
        i11
        matrixcolor TintMatrix("#4c508d")
    camera above_master:
        align (0.5, 0.2) zoom 3.0
        flash
    _mc eg na bi mm "Monstrum."
    show sayori lup rup mg e3d
    camera above_master:
        flash
    _mc mg "Crudelis es."
    show sayori me nb
    camera above_master:
        yalign 0.34 zoom 4.0
        flash
    _mc ml "Non es fidelis."
    show sayori b2a nc 
    camera above_master:
        align (0.55, 0.407) zoom 4.5
        flash
    _mc mm "Filius mali."
    show sayori ldown rdown md e3c b1b na
    camera above_master:
        align (0.5, 0.2) zoom 3.0
        flash
    _mc "Exitiale vitium."
    show sayori me e3d
    camera above_master:
        yalign 0.4 zoom 4.0
        flash
    _mc ml "Cor tuum est fur."
    $ clear_layers("above_master")
    camera master
    with None
    show melody turned braid strands uniform ec mh ba at i11 with Dissolve(1.7, time_warp=_warper.ease)
    pause 0.4
    hide melody with Dissolve(1.7, time_warp=_warper.ease)
    stop ambient fadeout 1.0
    _mc turned naked messy nostrands bi ec mg "Melody. You monster."

    $ add_calendar_description(calendar_descriptions["sayori"][1])

    call week_1_friday_sayori from _call_week_1_friday_sayori
    return