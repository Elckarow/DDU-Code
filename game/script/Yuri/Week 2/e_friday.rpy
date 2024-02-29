label week_2_friday_yuri:
    call calendar_transition(day=3, hour=7, minute=20) from _call_calendar_transition_45
    scene black with Dissolve(1.5)
    $ set_internet(True)
    play sound_loop phone_alarm fadein 3.0

    "..."
    "..."
    mc turned naked messy nostrands eg bi mj "Ugh..."
    play sound smack
    stop sound_loop
    show bg mc_bedroom_day_closed
    hide black 
    with NonBlockingDissolve(1.0)
    play ambient int_day fadein 1.0
    "I hit the snooze button like it's a mosquito and roll out of bed."
    _mc ec ba mh "It's Friday already."
    _mc eg bi "God, where's my week gone...?"
    _mc ef ba "Worse yet... there's so many mysteries."
    _mc ea bf "I'm not even just concerned for Yuri, now I'm just... worried."
    _mc eg bg "When will she tell me what's going on?"
    _mc bi ma "I definitely sound like a broken record saying that-"
    _mc ef ba mh "-But it's the only question on my mind."
    _mc ec bi "... Do I really need to get the answer from Monika instead?"
    _mc ef "Not even the festival feels important in comparison."
    _mc ec "The only thing that matters is Yuri."
    "I shrug the blanket off of me, sighing to myself."
    _mc eg ba "I need to hurry up if I don't want to be late to school."

    stop ambient fadeout 2.0
    scene black with wipeleft
    $ set_internet(False)
    $ set_date(hour=15, minute=10)

    "... Later, after classes..."
    
    scene bg club_day with Dissolve(1.0)
    show monika turned at t11
    $ advance_date(minutes=4)
    play music playwme

    "As I take a single step inside the Literature Club, Monika seems to appear out of nowhere."
    m mb "Great! Everyone's here!"
    show monika ma
    mc turned ml "Oh, hi Monika-"
    m mb "Hey, MC!"
    m md "While I hate putting people to work straight away..."
    m rhip mb "Today has to be an exception."
    m rdown lpoint md "Does everyone remember the shopping from last Sunday?"
    show monika mc at thide
    hide monika
    show natsuki turned me at t22
    show yuri turned e1d md at t21
    "She looks at Yuri and Natsuki."
    show yuri at t32
    show natsuki at t33
    show monika turned mb at t31
    m "I know you two weren't there, but it's important to mention it."
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    show monika md at t11
    m "Sayori, MC and I did a lot of shopping for decorations and such..."
    m mb "And those decorations have to be put in the right spots."
    show monika ma at lhide
    hide monika
    "Monika goes to the storage room, opens it, and grabs the three bags of decorations."
    m turned md "We have all kinds of decorations..."
    show monika turned mb at t11
    m "Like this banner here!"
    show monika ed ma with None 
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "She holds up an old looking banner, reading..."
    "Oh wait! That's what Sayori bought!"
    "'Writers unite...'"
    s turned mb "I'll hang that one up somewhere~"
    show sayori lup rup:
        r22
        "sayori turned lup rup md"
    show monika:
        0.15
        "monika turned mc"
        easein 0.2 xoffset -200
    camera master:
        0.15
        easein 0.2 zoom 1.0
    show bg:
        0.15
        easein 0.2 blur 0.0
    "As Sayori walks up to attempt to grab the banner, Monika quickly moves it away."
    m rhip ec md "Now now, Sayori... There's more I have to explain."
    show monika ea ma
    s ldown rdown e3d mi "Okaaaay."
    show sayori ma at thide
    hide sayori
    show monika rdown:
        easein 0.2 xoffset 0
    "Sayori returns to her seat, seemingly eager to start decorating."
    m md lpoint "I want you all to close your eyes..."
    show monika mc
    call close_eyes(0.3) from _call_close_eyes_27
    "We do as Monika says, then continue to listen."
    hide monika
    m turned md "Imagine you're not in this club-"
    m mb "Following along, imagine you, on the day of the festival, looking for a club to join."
    m md lpoint "What would you be looking for?"
    m "Which halls would you traverse...?"
    m "What would make you curious as to checking out the Literature Club...?"
    m mb "That's how you're supposed to think today."
    call open_eyes(0.4) from _call_open_eyes_19
    "We open our eyes back up."
    show natsuki turned b3a me at t11
    "Out of nowhere, Natsuki puts up her hand."
    n mc "You know, I'd be near the cafeteria first, taking a coffee before I go look around. Are we-"
    show natsuki b1d me at t21
    show sayori turned lup rup e1b mc at t22
    s "Oooh, same! But hot chocolate for me!"
    show sayori e1a md 
    show natsuki mj e1d lhip rhip
    "Natsuki looks over at Sayori, a little irritated."
    _mc mh "Either Natsuki doesn't like hot chocolate, or prefers to not be interrupted..."
    _mc ec "... Or she's just irritated as always."
    s e2a b2b mb nb "S- Sorry, continue..."
    show sayori ma at thide
    hide sayori
    show natsuki rdown ldown e3c md at t11
    "Natsuki regains her posture and resumes speaking."
    n b1a e1a mh "Are we allowed to put decorations there?"
    show natsuki md at t22
    show monika md ldown at t21
    m "Sadly not."
    show monika ma
    s turned e3c b2b mi "Awww..."
    show natsuki b3a me at thide
    m mb lpoint "And that's why I want to reveal a secret!"
    show monika ec mc at t11
    hide natsuki
    "Catching everyone's interest, Monika grabs her bag from under the desk."
    show monika eb bc ldown
    "She then begins rummaging through it, and grabbing..."
    m ea mb ba "Posters!"
    m md rhip "Five posters, each having a little description of our club."
    m ed mb "And, of course, where they can find our classroom."
    show monika rdown ma at t21
    show sayori b1a e1b mh at t22
    s "Monika... That's... great!"
    show sayori e3d ma at thide
    mc mb ea "Oooh... great idea, Monika!"
    hide sayori
    show natsuki turned mh b3a at t22
    n "We're allowed to put those ones on the wall?"
    show natsuki md
    m mb ea "Correct, as long as they don't cover up other things."
    show monika ma
    show natsuki ma
    mc thinking mf "Decorations and posters..."
    mc ldown eg mb "Sounds like we have quite the task ahead of us."
    show natsuki me
    m md "Indeed, so I thought of a little plan..."
    show monika mc
    n cross mg b1a "Hm?"
    show natsuki md
    show monika lpoint ma at thide
    "Monika points at the bag with Sayori's banner."
    hide monika
    show natsuki at t21
    show sayori turned md at t22
    m "Sayori and Natsuki, you two both work together to decorate using this bag."
    show natsuki at thide
    show sayori at thide
    hide natsuki
    hide sayori
    show monika turned lpoint md at t22
    show yuri turned lup e1d md at t21
    m "MC and Yuri, you two do this bag."
    show monika mc
    "She points at... What I think is my bag?"
    mc ea mg "Alright."
    y e2a mh "O- Okay..."
    show yuri md at thide
    hide yuri
    show monika ldown mb at t11
    m "And lastly, I'll do this one."
    show monika ec mc at dip
    "Monika grabs the last bag remaining."
    m mb ea "We'll do the posters later, one for each of us!"
    m md "Does this sound good?"
    show monika ma
    mc eh ma bb "Mhm!"
    show monika at t21
    show sayori turned e3d mn at t22
    s "Yeah!"
    show sayori ma at t33
    show monika at t32
    show yuri shy at t31
    "Yuri silently nods."
    show natsuki cross e2a mi at t44
    show sayori at t43
    show monika at t42
    show yuri at t41
    n "I have no objections."
    show natsuki mj at thide
    show sayori at thide
    show yuri at thide
    hide yuri
    hide sayori
    hide natsuki
    show monika ed rhip mb at t11
    m "Then, let's go!"
    m md ea "Oh, and before I forget..."
    m mb rdown "Take it slow and don't stress!"
    m md lpoint "If you don't know what to do with a decoration, you can always ask me or the others."
    m ed mb "Good luck, everyone!"
    show monika ma at thide
    mc ea ba mb "You too, Monika!"
    hide monika
    "And at that, Monika disappears to decorate."
    _mc ec mh "It's difficult to find a good time to approach Monika..."
    _mc ea thinking "Maybe after decorating?"
    show yuri shy eb at i11
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("yuri")
    "I grab our bag and head towards Yuri."
    mc mg ef ldown "Hey... Yuri."
    y ea "Hey..."
    mc ea bg ml "Are you alright?"
    y bb "I'm...  better now..."
    y eb mc "D- Don't worry about me."
    show yuri ma with say_dissolve
    mc mg "Yuri... Don't say that."
    mc ef ba mg "I- I mean, something like yesterday is worth worrying about."
    y ea mb "..."
    "..."
    y ee ma "..."
    y turned e2a lup b1d mh "Yeah... I guess so."
    y e3c mg "Should we..."
    y ldown e1d mh b1a "Start?"
    show yuri ma with say_dissolve
    mc ea ml "Yeah. Let's start."
    show yuri e1a md with say_dissolve
    "Yuri and I take a look into the bag."
    _mc ec ma "Yep, this is my bag."
    y e1d mg "What's this...?"
    show yuri lup me rup with say_dissolve
    "Yuri grabs a decorative garland, filled with patterns resembling popular fiction characters."
    "Still looking at the garland, like in a trance, Yuri speaks again."
    y mg "This'll bring in people... For sure..."
    show yuri me with say_dissolve
    mc eh mb "I'm most proud of finding that one."
    show yuri ldown rdown e1b md with say_dissolve
    "Yuri turns to me, snapped out of her stupor."
    y mg lup "Huh? You found this one?"
    show yuri e1d md with say_dissolve
    mc ea "Yep! Monika said this was my bag."
    mc ef ml "And it's not that difficult to tell these decorations were my idea when you know Sayori's tastes."
    y mg "Huh... I see."
    y e2a b1d mb ldown "Well..."
    show yuri ma with say_dissolve
    "Yuri glances around."
    y b1a mg "Where to put it...?"
    show yuri e1d me with say_dissolve
    mc mg thinking ea "Well, how about somewhere close to the entrance?"
    mc mb ldown "There, maybe?"
    hide yuri
    camera master
    show bg:
        blur 0.0 align (0.6, 0.4) zoom 3.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("yuri")
    "I point somewhere near the door, visible enough so you'd instantly see it once you come close."
    _mc ec ma "It's the perfect spot if you want to grab someone's atten-"
    show sayori turned lup e3d at t11
    "But before I know it, Sayori's hanging her 'Writers Unite' banner in that exact spot..."
    mc ea bd ml nb "S- Sayori!"
    s e3a mh "Hmm? Yeah?"
    show sayori md e1a
    mc mg ba na "Don't you think we should save that spot for things that will draw in people?"
    s e1b ml "W- Wha?"
    s lup b1d e1a mh "You're saying this {i}doesn't{/i} draw in people?"
    show sayori md
    mc bg ml "That's not what I'm sa-"
    show sayori at t21
    show natsuki cross e1d b4 mh at t22
    n "That's exactly what you're saying, MC."
    show natsuki mj b1d at t32
    show yuri turned lup e2a b1d md at t33
    show sayori ldown b1a me at t31
    "Yuri nervously interjects."
    y mg b1a "We wanted to..."
    show yuri e1d ma ldown at dip
    "Yuri holds up our banner."
    show yuri e2c mk b2b
    s e3c mi b1d "Well, we got this spot first!"
    show sayori mj
    show yuri rup mj
    "Yuri flinches, averting her eyes."
    show sayori e1a b1a md
    mc bi ec ml "Sayori..."
    s e2a b2b mg "Sorry... That was mean."
    s e1a b1a lup mh "But, where else should we place this?"
    s mb "Writers would be absolutely pulled in by this!"
    show sayori ma 
    _mc ef mh "Darn, she has a point."
    hide natsuki
    hide sayori
    hide yuri
    show bg:
        zoom 1.0
    with NonBlockingDissolve(1.0)
    "I look around, attempting to find another spot to put this banner."
    "Yet, I fail to find a spot that would make as much of an impact as the already occupied spot."
    show yuri turned e1d md lup at i11
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    mc ea ba mg "Yuri, do you see any nice spots?"
    y mg e2a b1d "Umm..."
    show yuri md with say_dissolve
    camera master
    show bg:
        blur 0.0
    show yuri at i31
    with Dissolve(0.2)
    $ say_transition = False
    "She walks around a little."
    $ autofocus.unblock("yuri")
    y b1a mh "How about..."
    show yuri e1d ldown mb at hop
    y "There?"
    show yuri ma with None
    show bg class_2_day as stuff zorder 5 with NonBlockingDissolve(0.5):
        align (0.2, 0.55) zoom 3.0
    "She points at the desk in front of the classroom."
    hide stuff with NonBlockingDissolve(0.5)
    y e1a mb "People won't see it from outside but... it {i}is{/i} the second place where people would look."
    show yuri ma
    mc mf "Huh..."
    mc ec ml "That could work."
    mc mb ea "Thanks, Yuri."
    
    scene bg class_2_day with wipeleft
    show bg:
        align (0.2, 0.55) zoom 3.0
    show yuri turned at i11
    with Dissolve(0.2)

    "As we place the banner, we look through the same bag."
    $ autofocus.block("yuri")
    y e1d md "..."
    mc turned mg bf "So much stuff..." # im stuff
    $ autofocus.unblock("yuri")
    y lup b4 mh "Do you think we'd have enough space for this...?"
    show yuri b1a md
    mc ef bg ml "Not sure..."
    "Just then, Monika comes closer and interjects, having heard our conversation."
    show yuri ldown at t22
    show monika turned lpoint md at t21
    m "Hey, you two!"
    m mb ldown "If you're worrying about space, you know you can decorate the floor and the more obscure parts, okay?"
    m md "Just don't overdo it, of course."
    show monika ma
    y mg lup "The floor...?"
    show yuri md
    m mb rhip "Yeah!"
    show monika md rdown ec bc at dip
    m "For example..."
    show monika ba ea ma
    "Monika looks through our bag, and finds an assortion of styled letters that can be placed on a mat."
    mc ml ea ba "I totally forgot I found those..."
    y mh "So.. We can use that to spell something?"
    y e1a mg ldown "Like what?"
    show yuri md
    m mb lpoint "How about... something from your poems?~"
    show monika ma ed
    show yuri me e1b lup rup
    "Yuri's eyes brighten."
    $ autofocus.block("yuri")
    y e1d md "..."
    $ autofocus.unblock("yuri")
    y ldown rdown e2a b1d mb "I- I'll think about it."
    show yuri ma
    m ldown ea md "Remember, if either of you need me..."
    m mb "Don't be afraid to ask~"
    show monika at thide
    mc mb "We'll keep it in mind, thanks Monika."
    hide monika
    show yuri e1a md b1a at t11
    "As she returns to her spot, we grab the letters and look at them."
    "..."
    $ autofocus.block("yuri")
    y "..."
    mc mh "..."
    mc ef mf "Well..."
    mc ea mb "Any clue what to spell, Yuri?"
    show yuri lup rup e1b mk nb b2a at hop
    "Yuri jolts in place."
    $ autofocus.unblock("yuri")
    y b2b e2a mb "W- Why me?"
    show yuri ma
    mc ml bf "S- Sorry, I didn't mean it that way."
    mc ef bg mb "... I know by now that you don't like to share your poems, so you don't have to if you don't want to."
    y e3c mb "Thanks..."
    show yuri ma e2a ldown rdown na
    mc ec bi mf "Then..."
    call close_eyes(0.4) from _call_close_eyes_28
    "A memory shoots into my mind."
    _mc ec mh thinking ba "What's something I associate with Yuri... that has to do with reading, and that I've also seen around a few times lately?"
    "..."
    "...!"
    show bg school_street_afternoon onlayer above_master:
        align (0.88, 0.7) zoom 3.0
    show widenekoflap onlayer above_master:
        align (0.8, 1.0) zoom 0.5
    show white_flashback onlayer above_master
    camera above_master:
        align (1.0, 0.65) zoom 1.2
        flash
    _mc ea ldown ma "A black cat."
    show yuri e1a md b1a
    call open_eyes(0.3) from _call_open_eyes_20
    mc mb "Yuri?"
    $ clear_layers("above_master")
    mc mg thinking "Do you know any interesting quotes from that first book I brought in?"
    mc mb "You know, The Black Cat?"
    y e1d mg "O- Oh, hmm..."
    y mh lup "Something to grab people's attention?"
    show yuri md
    mc ml "I was thinking more so... something that you'd like."
    mc md eh ldown "Whatever it may be, I'm sure you'll pick a good one!"
    y e2a b1d mg "Then... How about..."
    y e3c b1a mh "'Yet mad I am not... and very surely do I not dream'..."
    show yuri e1a ma
    _mc ec mh "Huh..."
    mc ea mb "... I think that's a great quote!"
    mc ml "Let's do it?"
    y e1d mg nb "Oh..."
    show yuri md
    "She thinks about it for a second, and then nods."
    y mb ldown "L- Let's do it!"
    show yuri ma e1a na
    call close_eyes(0.4) from _call_close_eyes_29
    "Having a wonderful sentence to put near the windowsill, we make sure it looks special."
    "We look at each other at times, wondering what the other is thinking."
    "Being close..."
    "Working together... "
    "And helping each other put up the different decorations..."
    _mc nc ef ma "It makes me feel..."
    "..."
    _mc eg na "Yeah..."
    _mc "... Yuri."
    _mc ec bg "If only you knew how I felt."

    scene bg club_afternoon
    camera master
    with wipeleft
    $ set_date(hour=16, minute=25)

    "We finally manage to empty our bag, having the whole classroom covered from the bottom to the top."
    show monika turned mc rhip:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    show bg class_2_afternoon
    with Dissolve(0.3)
    "Monika looks over the room in its completed state."
    m md "... Woah..."
    m mb "I definitely do not regret that shopping trip from Sunday."
    show monika ma
    "I can second that."
    "All of our decorations, beautifully placed and complementing each other..."
    hide monika
    show sayori turned nb:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    show bg club_afternoon
    with Dissolve(0.2)
    "As I look back, Sayori stands there, exhausted but proud."
    show bg club_closet_afternoon
    show natsuki cross b1d e2a:
        i44 
        matrixcolor TintMatrix("#f1d6bb")
    hide sayori
    with Dissolve(0.2)
    "Natsuki, calm and collected..."
    _mc turned ec "Huh. She seems to even have a little smile."
    show monika turned rhip:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    show bg class_2_afternoon
    hide natsuki
    with Dissolve(0.2)
    "Monika... satisfied with our group effort and smiling across the room."
    hide monika
    show bg club_afternoon:
        blur 2.0
    show yuri turned e1d:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    camera master:
        align (0.5, 0.1) zoom 1.5
    with Dissolve(0.2)
    "Then... Yuri."
    "Yuri looks at me."
    "Her nervousness seems absent."
    _mc ef nc "... And I know that means a lot."
    hide yuri
    camera master
    show bg class_2_afternoon:
        blur 0.0
    show monika turned:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    with Dissolve(0.2)
    m mb "Now comes the part that needs the most creativity of all."
    show monika ec bc mc at dip
    "She puts the same posters as this morning on her desk."
    m lpoint ea ba mb "I want you to do the same thing as earlier."
    m md "Close your eyes, and imagine where... a student without a club would go and look."
    m ldown mb "Everyone got that? If so, grab a poster and let's go!"
    m md "..."
    m eb bb mb "... That was not meant to rhyme, but hey, perfect timing!"
    show monika ma at thide
    hide monika
    "All of us grab a poster."
    show bg school_cafeteria_afternoon
    show natsuki turned me:
        matrixcolor TintMatrix("#f1d6bb")
        i21
    with NonBlockingDissolve(0.3)
    "Natsuki seems to be going to the cafeteria..."
    show bg school_corridor_2_afternoon:
        align (1.0, 0.55) zoom 3.0
    hide natsuki
    show sayori turned e2c:
        matrixcolor TintMatrix("#f1d6bb")
        i33
    with NonBlockingDissolve(0.3)
    "Sayori to the area around the restrooms..."
    hide sayori
    show bg school_corridor_3_afternoon:
        zoom 1.0
    show monika turned rhip mc bc ec:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with NonBlockingDissolve(0.3)
    "Monika near the ceremony hall..."
    hide monika
    show bg school_corridor_1_afternoon
    with NonBlockingDissolve(0.3)
    "And Yuri..."
    stop music fadeout 3.0
    _mc mh ea na "... Yuri?"
    _mc ec "Hmm. Can't see her anywhere."
    _mc ea thinking "Maybe she took a different rout-"
    play sound chairmoving
    "I hear the sound of a chair being moved behind me."

    scene bg club_afternoon:
        align (0.0, 0.8) zoom 1.9
    show yuri turned e2a md:
        matrixcolor TintMatrix("#f1d6bb")
        i42
    with wipeleft

    "As I turn around, I see Yuri sitting back in her ordinary spot."
    _mc turned mf "Huh...?"
    _mc mh bd "What is she doing?"
    $ autofocus.block("yuri")
    y b1d e2a me "..."
    $ autofocus.unblock("yuri")
    y e1d b1a lup mh "... Melody?"
    y mg "May I..."
    y e2a b1d "Talk with you?"
    show yuri md
    _mc ec bi "'Melody'... I wasn't expecting her to use that name."
    _mc eg ba ma "... I suppose I can pardon it just this once."
    mc ea ml "O- Oh, yeah. Of course."
    show yuri b1a
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "I take a seat next to her."

    play music wtdgi

    "..."
    mc mh "..."
    show yuri e1d me with say_dissolve
    "Yuri looks at me, a mix of expectancy and nervousness."
    "I give her my best smile in an attempt to reassure her."
    mc mb bg "... I'm listening, take your time..."
    y md "..."
    y e2a mk b2b "I..."
    y rup e3c "I'm..."
    show yuri mj e1a tears_a b2a with say_dissolve
    "Tears start forming in her eyes, as she looks into mine."
    y nb e3c notears b2b mh "I am so... so sorry!"
    y e2a b2a mb "I know I haven't been... honest and straightforward with you..."
    y ldown rdown mk "It's just... been so difficult."
    show yuri mm with say_dissolve
    mc mh "..."
    show yuri mj with say_dissolve
    mc ba ml "... Sayori did say you might be having a hard time."
    mc ef bi mg "Monika seemed to hint at something as well, but she never told me much..."
    y e2a "..."
    y me e3c "... Yes..."
    y b2a na e1a mg lup "I... well..."
    show yuri e3c b1d me with say_dissolve
    "Yuri sighs."
    y e2a b1a mh "... I... As you've no doubt noticed, I suffer from... panic attacks."
    y b1d mg "... I..."
    show yuri e1a b1a md with say_dissolve
    "Noticing Yuri's struggles, I can't help but think that pushing her will start one of those panic attacks."
    mc ea bf mb nb "Take it slow, deep breaths. Okay?"
    mc ml bg "You don't have to tell me everything all at once, if you're uncomfortable, you know...?"
    y e1d mi b3d ldown "I do want to!"
    show yuri e2d nb md b1a with say_dissolve
    "Yuri stops, making sure no one heard her."
    y b1d mg rup e3c "... Please allow me to elaborate, even just a little bit."
    show yuri md with say_dissolve
    mc mf ef na "... Okay..."
    show yuri b1a me na with say_dissolve
    "She takes in deep breaths, then looks back at me."
    y rdown mh e1d "... I... have a troubled family."
    y mg e2a "... That's where my panic attacks stem from..."
    show yuri md with say_dissolve
    "..."
    y "..."
    mc ea mf nb ba "I... see..."
    _mc ec mh "A bit short, but-"
    y b1d mg "And..."
    show yuri e1a md with say_dissolve
    "Yuri looks me dead in the eyes."
    y mg "The blood on Natsuki's cheek, on Monday."
    y rup e3c me "... That was me."
    show yuri md with say_dissolve
    "..."
    _mc bd ea "Wait... What? Huh?"
    y b1a e2c mg "I... cut myself."
    y b1d mh tears_a "It's a... It's how I... I cope when I have a panic attack..."
    y mk nb b2b "When it's just too much to bear..."
    show yuri mm tears_b with say_dissolve
    "Yuri grimaces, the tears still flowing."
    y b2a e1a mh tears_a "Natsuki tried to help me, but..."
    y e2a rdown b1d notears mg "She... Likes to push too much."
    y mh b1a e2b tears_a "She came closer and closer, trying to grab my knife as I s-screamed."
    y e1b mi tears_b rup "And..."
    show yuri e3c tears_a b1d me with say_dissolve
    "Yuri takes a deep breath."
    y rdown b2b e2a mk "I- I accidentally hurt her instead..."
    _mc ea bg "That explains a lot..."
    y mm nb e3c "I wanted to tell you, but..."
    y tears_b mk "... I just couldn't. I was too scared..."
    y lup rup e2a notears b2b mh "... Stressed, anxious, still overwhelmed after everything that happened..."
    y b2b e3c tears_a mg "... I just left."
    show yuri mj with say_dissolve
    "..."
    mc ef na "..."
    y me e3c na "..."
    y rdown b1d e2a mg "I tried to pretend nothing happened..."
    y b1a mb notears "That I was fine, I didn't have any panic attacks at all..."
    y b2b e2b mg tears_a "... But in that moment, when I was nearly hit by that car..."
    show yuri me with say_dissolve
    mc bf ea ml "... The stress and panic came back in full force?"
    y e3c mg "... Yes."
    y ldown e2c nb mk "... I had to go home. Where it was safe..."
    y mg e1a tears_a lup rup "... Please forgive me, MC..."
    show yuri md with say_dissolve
    mc bg mf "... Yuri..."
    show yuri me with say_dissolve
    mc eg ml "I... I can't imagine what it's like."
    show yuri e1a md na with say_dissolve
    mc ef bf mg "... To have all that anxiety, to lose control of yourself like that..."
    mc ml bg "I just... want to understand, Yuri."
    mc ea mb "I want to know you more than I do."
    y me b1a "..."
    y mg e1d ldown rdown "Even after everything I told you?"
    show yuri me with say_dissolve
    mc eh md nb bf "We all have skeletons, right?"
    show yuri md notears with say_dissolve
    mc ef ma "..."
    mc bi mf "... And, one more thing?"
    mc ea mg na ba "You're brave."
    show yuri e1b b1a nb me with say_dissolve
    "Yuri pauses, taken aback."
    y e1d b4 mg lup "H- Huh?"
    show yuri me with say_dissolve
    mc ef bi ml "Telling me this..."
    mc ba mg "I have a feeling it probably isn't the full story yet, but just by doing that..."
    show yuri b1a with say_dissolve
    mc eg mb "Well, you're already a lot braver than me, I can say that for sure."
    show yuri md with say_dissolve
    "Yuri looks at me, her tears past dried."
    mc ef bg ml "So... I just want to say..."
    show yuri me with say_dissolve
    mc bf ea mb "It's okay, Yuri."
    mc eg bg "If you want to cry..."
    show yuri mj e1a b2b tears_a with say_dissolve
    mc ea "Please. You've earned it."
    show yuri ldown md:
        xoffset 100 
    camera master:
        zoom 1.6
    with Dissolve(0.2)
    "Yuri slowly leans into me, her tears flowing once more."
    y e3c mk "... T- Thank you. Thank you f- for... u- understanding..."
    show yuri mm tears_b with say_dissolve
    "Yuri hicks as she begins to sob."
    y e1a mg "... Melody...?"
    show yuri md with say_dissolve
    mc eg "... Just this once, Melody."
    camera master:
        zoom 1.7
    show yuri e3c ml lup rup nb
    with Dissolve(0.2)
    "Yuri wraps her arms around me, giving me a light hug."
    show black with NonBlockingDissolve(0.3)
    "Her tears flow into my chest as I return the hug, rubbing her back."
    hide yuri
    y turned lup rup b2b e3c nb tears_b mk "... Thank you, Melody..."
    y ml "... Thank you..."
    mc md "... Of course..."
    "I spend the next few minutes rubbing her back to comfort her as she gets the rest of her tears out of her system..."

    scene black
    show yuri turned mj b2b e3c nb:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    show bg club_afternoon 
    camera master
    $ autofocus.unblock("yuri")
    $ say_transition = False
    pause 2.0
    hide black with Dissolve(1.0)

    "... Afterwards..."
    show yuri:
        "yuri turned b1a lup me e3d nb"
        0.4
        xzoom -1
        0.4
        "yuri turned ldown b1a e1d me"
        xzoom 1
    "Yuri wipes her tears as she gives herself some space."
    y lup mg "B- Before we forget..."
    show yuri me
    mc turned mh "Hmm?"
    y ldown e2a b1d mb "We should do the flyers..."
    show yuri ma
    mc bb eb nb mg "Oh, you're right! Completely crossed my mind!"
    mc ml ba ea "You... want to walk together?"
    show yuri e1d me b1a
    "Yuri can't help but be surprised once more."
    y mg "R- Really?"
    show yuri md lup
    mc md eh "Yeah!"
    y e2a b1d mg "T- Then..."
    show yuri e1a ldown ma b1a
    "She gives a bright smile."
    y mb "Let's go...!"
    show yuri ma at thide
    "I can't help but think how much she's trying."
    "Trying to be more than she is."
    _mc thinking na mh ea ba "With her panic attacks... If I was in her place, I wouldn't let anybody know."
    _mc ec "Someone knowing something like that about me would make me want to tear my own heart out."
    _mc eg ma "But she told me anyways."
    _mc nc "Which is probably what makes her too good for me."
    _mc na ea mh "Is this the start of her opening up?"
    _mc bg "Will she... Tell me about her family? About what Natsuki said to her?"
    _mc ldown bi eg "I hope so... It'll probably just take time."
    _mc ef ba "She probably needs that time..."
    _mc ma "... Yeah."
    hide yuri

    scene bg school_corridor_3_afternoon
    show yuri turned e2a:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with wipeleft

    "We both walk downstairs, looking for a place to hang up our posters."
    mc turned ec mh thinking "Hmm..."
    show yuri e1d md
    mc bi mf "I can't find anywhere to put this..."
    mc mg ba ea ldown "You really picked a good one at the library, you know?"
    y lup b1d e2a mb "T- Thanks..."
    show yuri ma with None
    hide yuri
    show bg class_1_afternoon
    with NonBlockingDissolve(0.4)
    "Looking around, an empty, yet nostalgic classroom grabs my attention."
    "As I slowly approach it, I notice how silent it truly is."
    mc mf "Nobody around here..."
    mc ec ml "Yet, it is technically the most important classroom in the school."
    mc eg bi mb "... At least, according to teachers..."
    show yuri turned lup e1d md:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    "Yuri looks over in my direction."
    y mg "MC... are you sure?"
    y e2a b1d mb ldown "I don't know how many people will go here."
    show yuri ma 
    mc ea ba mf "I..."
    mc eg mb "I'm sure, Yuri."
    show yuri e1a b1a
    "I put the poster near the door."
    mc md ed "The Form classroom deserves it."

    scene bg school_corridor_1_afternoon
    show yuri turned:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with fade
    $ advance_date(minutes=6)
    pause 0.02
    show bg:
        xzoom -1
    show natsuki turned e2a md:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    hide yuri
    with Dissolve(0.2)

    "As we walk back, I see Natsuki walking behind us."
    _mc turned mh bg "Poor Natsuki..."
    _mc ba "Maybe I should..."
    hide natsuki
    show yuri turned e1d md:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    show bg:
        xzoom 1
    with Dissolve(0.2)
    mc mb "Yuri, give me a moment, okay?"
    mc eh md "I'll meet you back in the Literature Club."
    y e2a mb b1d "S- Sure."
    show yuri ma with None
    hide yuri
    show natsuki turned e1b me:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    show bg:
        blur 2.0 xzoom -1
    camera master:
        align (0.5, 0.25) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    "I approach Natsuki, who looks at me in surprise."
    n b1d mm "!!"
    n e2a mh nb "What is it...?"
    show natsuki md with say_dissolve
    mc ml ea "Natsuki..."
    mc mb bf "Sorry for never checking up on you."
    show natsuki na with say_dissolve
    mc bg ef ml "After that... thing on Monday."
    n lhip mg "..."
    n b1a e1a mh "I assume you two talked about it?"
    show natsuki mj with say_dissolve
    mc ea bf mb "Yeah. We did."
    n cross b1d e2a mm "{i}This{/i}, is why I keep an eye on Yuri."
    n b1a mg "While she simply seems shy..."
    n turned ldown b3a mh e1a "She's seen a lot of things."
    n mg e2a b1d "Been hurt."
    n cross mh b2a "And I don't want that to ever happen again."
    show natsuki mj with say_dissolve
    mc ba ml "I get that, but..."
    show natsuki md with say_dissolve
    mc bd mg "She's not a child, Natsuki. You don't have to agonize over her like she is one."
    mc ef bi mf "She's..."
    show natsuki b1a with say_dissolve
    mc ba eg mg "She's so much stronger than you think."
    show natsuki turned e3c b1d me with say_dissolve
    "Natsuki then lets out a sigh."
    n e2a lhip mh b3a "Well, being strong is hard. It's a little bit easier if you have someone watching your back."
    n e1a mb "And she has all of us."
    n e2a b1d mh "She's {i}important{/i} to all of us."
    n e1a b1a mb "So... be a good friend to her."
    show natsuki ldown ma with say_dissolve
    "She flicks a finger against my chest."
    n cross mh "Don't take that responsibility lightly!"
    n b1d e1d mg "We all bear it."
    show natsuki mj with say_dissolve
    mc ef mh "..."
    _mc bi "Responsibility..."
    show natsuki e1a b1a ma with say_dissolve
    "I stare into Natsuki's eyes, taking a deep breath."
    mc bd ea ml "I promise."
    n turned b3a mc "Good."
    n b1a mh "Well then, let's go back?"
    show natsuki ma with say_dissolve
    "I give her a steady nod."
    mc eg mb ba "Agreed."
    
    stop music fadeout 2.0
    scene bg club_afternoon
    camera master
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        i21
    show monika turned:
        matrixcolor TintMatrix("#f1d6bb")
        i22
    with longfade
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    play music daijoubu

    "As we walk in, Sayori and Monika seem to already be waiting for us."
    show monika mb at t44
    show sayori at t43
    show yuri turned:
        matrixcolor TintMatrix("#f1d6bb")
        t42
    show natsuki turned:
        matrixcolor TintMatrix("#f1d6bb")
        t41
    m "Welcome back, everyone!"
    m md "Satisfied with your placements?"
    show monika mc
    show yuri lup at dip
    show natsuki e3c at dip
    show sayori e3d at dip
    "We all nod in agreement."
    show natsuki e1a
    show sayori e1a
    m md lpoint "Then... I will conclude the day."
    m ldown mb "Thank you all."
    show monika ma at thide
    hide monika
    show yuri at t32
    show natsuki at t31
    show sayori at t33
    show bg class_2_afternoon as stuff onlayer above_master with {"above_master": Dissolve(0.5)}
    "Monika gives a small curtsy, before walking behind the teacher's podium."
    show sayori md with None
    hide stuff with NonBlockingDissolve(0.2)
    "I walk over to Monika, standing next to her."
    mc turned mg "No, I have to thank you all."
    show sayori ma
    mc mb "It was fun."
    s mb "... Know what's gonna be more fun, though?"
    show sayori ma
    mc ml thinking "... What?"
    show sayori lup rup e3d mc at hop
    s "Sleepover at my place!"
    show sayori ma
    n e1d b4 mb "I bet Mel forgot about it~"
    show natsuki ma
    mc ldown ed md "Did not~!"
    _mc eh bg teehee nb "... I might have done."

    camera master:
        align (0.5, 0.1) zoom 1.4
    show bg:
        blur 1.7
    show natsuki e1a b1a:
        alpha 0.0
    show sayori e1a ma:
        alpha 0.0
    show yuri ldown at thide
    with Dissolve(0.2)
    "I look at Yuri and give her a smile."
    "And as I do... She smiles back."
    camera master
    show bg:
        blur 0.0
    show natsuki:
        alpha 1.0
    show sayori ldown rdown:
        alpha 1.0
    with Dissolve(0.2)
    n cross e3c mi b3a "We'll be there, as long as you don't forget to make your house tidy!"
    show natsuki e1a ma at thide
    s lup e3d mn "Looking foooorward to it!~"
    show sayori ldown ma at thide
    hide sayori
    hide natsuki
    hide yuri
    show monika turned rhip ec:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    "Monika gives a nod in agreement."
    show monika at thide
    hide monika
    show yuri turned e2a:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    "As we pack our bags, I decide to go to Yuri."
    show yuri e1a
    mc na ea ba mb "Hey, Yuri..."
    show yuri md
    mc ml "I know it's late, but... want to head home together?"
    y e1d mg "R- Really?"
    y b2b lup e2a mb "I... I wouldn't mind."
    show yuri ma with None
    show yuri e1d b1a me lup
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "I grab her hand, prompting her to look at me."
    "She stares at me. Deep into my eyes."
    _mc ec ma "I can sense it."
    _mc eg "A sense of relief."
    _mc ec "Both of our thoughts aligned."
    show yuri e1a ma with say_dissolve
    _mc ea "I think she understands."
    _mc ef "And..."
    _mc eg "I can't be any more grateful for that."

    $ add_calendar_description(calendar_descriptions["yuri"][9])

    call week_2_saturday_yuri from _call_week_2_saturday_yuri
    return