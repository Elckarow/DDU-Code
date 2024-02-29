label week_2_wednesday_natsuki:
    call calendar_transition(day=1, month=11, hour=4, minute=10, second=35) from _call_calendar_transition_20
    scene black
    camera master
    with dissolve_scene_full
    $ autofocus.unblock("sayori")
    play sound_loop phone_alarm fadein 2.0

    "I wake up to the sound of my alarm."
    _mc turned messy naked nostrands ec mh bi "Strange, I’m always up before that goes off; it’s only insurance."
    _mc ea ba "Still, better get up, or I’ll be late."

    stop sound_loop
    scene bg mc_bedroom_night_open with Dissolve(0.2)
    play ambient ext_night fadein 1.0

    _mc turned bd messy naked nostrands mh "... Wait, why is it still dark out?"
    _mc ba "Hm?"
    $ advance_date(seconds=4)
    "The clock clearly tells me the time is 4:11 AM."
    _mc ec bi "... Sayori."
    _mc eg ma "I’ve been pranked, haven’t I?"
    _mc mh "God. Dammit."
    _mc ec "That’s the last time I ever offer her my phone."
    _mc ea ba "I guess I’ll get up, and grab some water."
    _mc eg ma "Not like I’ll sleep properly again, like this."

    stop ambient fadeout 1.0
    scene bg mc_living_room with wipeleft

    _mc turned messy naked nostrands mh "Why is the light in the kitchen on? Did I forget to turn it off?"
    _mc ec "No, I always do; it’s habitual at this point."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    play sound heartbeat
    _mc bi "... Someone’s in my house."
    show black with NonBlockingDissolve(1.5):
        alpha 1.0
    "I race back upstairs as quietly as I can, grabbing the heaviest thing I can find."
    _mc "Well, if it’s the best I’ve got..."
    pause 1.0
    play sound_loop heartbeat fadein 2.0 volume 0.7
    pause 2.0
    "In my hands, I hold a microphone stand."
    _mc ea ba "Amelia wanted me to stream with her, so bought me some of the stuff I might need to do so. It’s a shame it’ll be wrecked in this way, but I’ll pay it back in the morning if I have to." # im stuff
    _mc ec "... If I live long enough to see that through."
    _mc eg bi mm "No, no, no. Just go. Do, or do not."
    _mc mh ec "And I can’t afford to 'do not', here."

    scene bg mc_kitchen_day with wipeleft
    stop sound_loop fadeout 2.0
    stop music fadeout 1.0
    pause 0.2 
    play sound thud
    pause 0.9

    _mc turned messy nostrands naked mf nb bd eb "... What."
    _mc mh "The ever-loving shit."
    show natsuki turned casual notail b3a mg nb at t11
    n "Oh, ah, Mel?"
    n lhip rhip e2a b1a nd mb "G- Good morning!~..."
    show natsuki ma
    "The implement I had planned on using in my defence has fallen to the ground."
    "Instead, I stare, slack-jawed, at the sight in my kitchen."
    n b3a e1a mh "L- Look, I can explain-"
    show natsuki b1d mm e2a
    mc bi ec mj na "Uh- huh."
    n ldown rdown e1b ml nc b1a "It’s not what it looks like, I swear!"
    show natsuki mm
    mc bd ea mg "Really? Because it looks like you’re making lunch, with my ingredients!"
    n e2a lhip b1d mh "W- Well, then, it’s exactly what it looks like, I suppose..."
    show natsuki md
    mc mm eb "In my house! At 4AM!"
    n e1b ml ldown "Well, you don’t need to shout, it’s 4am!"
    n cross e1d mh na "Do you want to wake Sayori?"
    show natsuki mj
    mc ea mg "I’m saying, what are you doing {i}here{/i}?"
    n e2a mg b1a "Nothing. Nothing at all."
    show natsuki turned e1a ma:
        ease 3.0 zoom 1.4 yoffset atl_utils.yoffset(z=1.5, r=1.1)
    show bg:
        blur 0.0 align (0.5, 0.2)
        ease 3.0 blur 5.0 zoom 1.2
    $ autofocus.block("natsuki")
    $ say_transition = True
    "She walks over to me, her feet barely moving as she seems to hover across the ground."
    _mc ec ba mh "What is she, some spectre?"
    n e3c mg "Now, back to sleep with you. You’ll awaken after this, and everything will be normal."
    show natsuki b3a ma e1a with say_dissolve
    mc ml ea bd "Sleep? How could I possibly sleep after-"
    call blink(color="#fff", duration=0.4) from _call_blink_7
    play sound slap
    camera master:
        matrixcolor BrightnessMatrix(0.0) blur 0.0
        linear 10.0 matrixcolor BrightnessMatrix(-0.4) blur 5.0
    mc ml ba "That..."

    window auto hide
    pause 0.7
    call blink(base_blur=10) from _call_blink_8
    pause 2.0
    call blink(base_blur=10) from _call_blink_9
    pause 0.5
    call blink(base_blur=10) from _call_blink_10
    pause 1.0
    scene black
    camera master
    with Dissolve(0.3, time_warp=_warper.easein)
    play sound fall
    pause 5.0
    scene bg mc_bedroom_day_closed
    camera master:
        blur 10.0
    with dissolve_scene_full
    camera master:
        ease 5.0 blur 2.0
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    $ set_date(hour=7, minute=50)

    _mc turned messy naked nostrands mf eg "Hm?"
    _mc bi mm "Ouch, my head..."
    _mc ec mh "What a messed up dream, dude."
    _mc ea ba "... Hm?"
    _mc mj bb eb nb "Oh, shoot! I’m gonna be late for school if this keeps up!"

    scene bg residential_day
    camera master
    with wipeleft_scene
    $ set_date(hour=8, minute=10)
    $ set_internet(False)

    "As I make my way quickly down the road, I can’t shake the feeling that something weird is going on."
    _mc turned bun nostrands ec mh thinking "Sure, maybe it felt like a dream; I mean, I woke up in my own bed, but-"
    _mc ea "It definitely didn’t seem like a dream."
    _mc mb ldown "But do I just ask, 'hey Natsuki, did you break into my house last night to do some cooking?'"
    _mc eb bd mh "Imagine if I was wrong!"
    _mc eg bi "I can’t do that. Not that directly. I just have to find another way."
    _mc ea ma bb "Oh, I’ve got it!"
    _mc ba "Just have to catch up with Sayori sometime today."

    scene bg class_2_day with fade
    $ set_date(hour=10, minute=10)
    play music school

    _mc turned bun nostrands ec mh "Boy, is it hard to concentrate today."
    show bg:
        blur 2.0
    show natsuki turned e2a md:
        zoom 0.57 xcenter 0.78 yalign 1.0
    camera master:
        align (0.8, 0.8) zoom 1.5
    with Dissolve(0.2)
    _mc eg "Not in the least because Natsuki is sitting {b}right there{/b}."
    _mc ec "What do I do? Pretend that nothing’s changed?"
    _mc ea ma "Yeah. Let’s do that, for now."

    scene bg school_corridor_2_day
    camera master
    with wipeleft_scene
    $ set_date(hour=12, minute=1)

    "I make my way outside, ready to find Sayori, before something catches my arm."
    show bg:
        blur 2.2 xzoom -1.0
    show natsuki turned b2a md nb at i11
    camera master:
        align (0.5, 0.25) zoom 1.5
    with Dissolve(0.15)
    $ autofocus.block("natsuki")
    $ say_transition = True
    n mg lhip "H- Hey, where are you going? You promised... t- to have lunch with me, remember?"
    show natsuki md with say_dissolve
    mc turned bun nostrands ml "Oh, yeah, I did, didn’t I..."
    n b1a na mh ldown "Are you saying you don’t want to have lunch with me?"
    show natsuki mj with say_dissolve
    mc bd ml "No, that’s not what I-"
    n b3a na mo e3d "Good! So come this way! We don’t have long."
    hide natsuki
    camera master
    show bg school_rooftop_access_day:
        blur 0 xzoom 1.0
    with Dissolve(0.3)
    $ say_transition = False
    "She drags me by the arm toward the rooftop access."
    $ autofocus.unblock("natsuki")
    _mc ec mh ba "... She seems exactly the same as she was yesterday, if you ask me; really weird."
    _mc ea "Still... Maybe that means I’m the crazy one. Best to see how this plays out."

    scene bg school_rooftop_day
    show natsuki turned b3a at i11
    with wipeleft

    "..."
    n mc "Well?"
    show natsuki ma e3d
    mc turned bun nostrands ml "It’s, ah, good?"
    "Truthfully, it’s about average. She’s put work into it, that much is plain to see, but she’s missing some of the finesse."
    show natsuki e1a b1a with None
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    "The blends of flavours that really make something pop."
    "If yesterday’s had too much flavouring, tonight’s has too little."
    _mc ec mh "It’s fascinating, almost like she’s never cooked in her life. But that can’t be right; is there anyone who’s ever not cooked before?"
    show natsuki md
    _mc ea "How could you go eighteen years without cooking?"
    _mc eg bi ma "... Don’t answer that, me."
    hide black with NonBlockingDissolve(0.5)
    _mc ec mh ba "Some things are better left for the imagination."
    n b2a mh "Well?"
    n e2a b1a mc nb "It’s clearly not good! Look at your face!"
    show natsuki ma
    mc ea ml "N- No, I was just thinking-"
    n e1d b1d na mh lhip rhip "And not concentrating?"
    show natsuki mj
    mc mg "Well, by proxy, you could technically argue that a portion of my brain power is always focused on other tasks, so can we ever really concentrate 100\% of our brain-"
    show natsuki b3a mo e3d ldown rdown at hop
    n "NEEEERRRRRDDD!"
    "I mutter under my breath."
    mc ef bi mf "{size=-5}... Have you seen your grades?{/size}"
    n b3a mc e1a "So!"
    n b1a rhip mh "Tell me! Good? Or not?"
    show natsuki md
    mc ea mg ba "It could use more flavour."
    mc mb "If you adjust the amount of curry and test it as you add it, you’ll be able to make something with more precision."
    $ autofocus.block("natsuki")
    n rdown "..."
    "She listens, surprisingly attentively."
    $ autofocus.unblock("natsuki")
    n e2a b3a mh "Alright!"
    show natsuki e1a ma at dip
    "As soon as the last bite leaves the container, she snatches it away from me."
    n mc "Good! Now I’ll make one for you tomorrow!"
    show natsuki ma
    mc ml bg nb "W- Wait, that’s my-"
    n mc lhip "Free food!"
    show natsuki me
    mc bd na mg "Look, maybe I want to cook something for myself!"
    $ autofocus.block("natsuki")
    n mg b1a "..."
    "She pauses, jaw agape."
    show natsuki ldown e2a mj b1d
    "Then, after a moment, she looks away."
    $ autofocus.unblock("natsuki")
    n cross mh "... It really was that bad, wasn’t it?"
    show natsuki mj
    mc ba ml "No, it wasn’t-"
    n e1a mi b3d "But it was, wasn’t it?"
    n turned b3a e3c mh "It’s alright, I understand."
    show natsuki b2a e1a ma nb at dip
    "She hands me the lunchbox back."
    mc bg mg "Natsuki, it’s not like that, it’s just-"
    n b2b mb e2a "I get it! My food is terrible! You don’t have to force yourself to eat it!"
    show natsuki e1b b3a nd md at hop
    mc eb bd "No!"
    show natsuki e1a nb
    mc ml ec bi "Give me yours."
    n b1a na mg "Eh?"
    show natsuki mj b3a
    mc ea ba "Your lunchbox."
    mc mb "I’ll make something tomorrow."
    mc mg "It’s not fair that you’ve been making food."
    $ autofocus.block("natsuki")
    n me "..."
    show natsuki b1a e3c mj at dip
    "After a moment, she wipes the stunned mullet expression from her face, and wordlessly hands me her box."
    show natsuki e1a md
    mc ed md "Besides, perhaps I can show you what I mean, rather than just telling you."
    n e2a b1d "..."
    hide natsuki
    show bg:
        align (0.4, 0.5) zoom 2.7 
    with Dissolve(0.2)
    "I swear I see her lip quiver as she turns on her heel and rushes from the rooftop."
    $ autofocus.unblock("natsuki")
    _mc eb bd mh "What... the hell is this day?"

    scene bg school_corridor_1_day with wipeleft_scene
    $ set_date(hour=15, minute=12)

    "As I make my way to the clubroom, pushing through all the hordes of people, I find myself stopped, dragged in the opposite direction down a separate hallway."
    show bg:
        xzoom -1.0 blur 2.2
    show amelia turned ponytail rup bb md at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    am me "Where were you?"
    show amelia md with say_dissolve
    mc turned bun nostrands ml "Huh?"
    am rdown ec me "Lunch. Where were you?"
    show amelia md with say_dissolve
    mc bm ed mg thinking "The rooftop?"
    show amelia bf ea mg with say_dissolve
    "She blinks a couple times, probably out of sheer bewilderment."
    am bg me "The rooftop? Why?"
    show amelia ba eb md with say_dissolve
    mc ea "I was having lunch?"
    am ec bh mb "So you made your own lunch, did you?"
    show amelia mc with say_dissolve
    _mc ea mh ba "Wait-"
    _mc ec "She said something about wanting to pack the stuff she made yesterday into a lunch for me, right?" # im stuff
    _mc eb bd "I just palmed it off as her trying to be polite! I never once thought she’d do it!"
    mc eg ldown mg ba "Okay, there appears to be a misunderstanding here."
    am ea bf me "And that would be?"
    show amelia md with say_dissolve
    mc mg ea "You made me lunch, right?"
    am ba ed me lup "I said I would."
    show amelia md with say_dissolve
    mc mb "Yeah, exactly-"
    mc ec ml "That’s just it. I didn’t actually expect you to."
    show amelia bh mc with say_dissolve
    "She almost looks offended."
    am ec me "You think I’d go back on my word?"
    show amelia md ldown with say_dissolve
    mc ea mg "No, I thought you were just being polite."
    am ed mc "..."
    "She bites her lip, clicking her tongue."
    am ba me "So that’s how you took it..."
    am ee mf "I probably shouldn’t even bother with this now, but here."
    show amelia mg with say_dissolve
    "She pushed the box into my hands."
    am ed me "Take it for dinner, then. It’ll save you a little this week on expenses, and means you don’t have to go to all that effort to cook something up."
    show amelia md with say_dissolve
    mc ml "Amelia, I-"
    am eb me "No, we’re both at fault here. Best to just cut our losses."
    am ee mf "Take the food, and like it, alright?"
    am ea bd mb "Geez, last time I do anything nice for you..."
    show amelia ma with None
    hide amelia
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ autofocus.unblock("amelia")
    $ say_transition = False
    "She gives me a small smile as she waves me off, heading back to her infamous 'Going Home Club'."
    _mc ec ma "I’ll have to do something nice for her, someday, to make up for all the crap she puts up with."
    _mc ea "For now, though, I’d better get to my own club."

    scene black onlayer above_master
    hide bg
    show bg club_day
    with wipeleft
    $ advance_date(minutes=10)

    "As I carefully mark down and collate notes from class through my incessant, building headache, my attention is dragged away again and again by the sound of raised voices."
    "With each sound my ears split just a little more, like a nail driven into the side of my head with every word."
    $ autofocus.force_focus("yuri")
    show yuri turned mb lup at i21
    show natsuki cross e1d b4 mj at i22
    hide black with {"above_master": Dissolve(5.0)}
    stop music fadeout 15.0
    _mc turned bun mh eg bi "God... Just shut up, please..."
    $ autofocus.force_focus("natsuki")
    $ autofocus.restore_focus("yuri")
    show natsuki b3a e1a mb
    show yuri md 
    "The girls are arguing over something - I'm in too much pain to pay attention to what. Besides, this study {i}needs{/i} doing."
    show natsuki turned mi b1d lhip rhip
    "I can't afford to be waste any more time with exams in a few weeks."
    $ autofocus.force_focus("sayori")
    $ autofocus.restore_focus("natsuki")
    show natsuki mj at t33
    show sayori turned lup rup xd b2c nb ml at t32 
    show yuri at t31
    "Sayori's voice cuts through the noise, and it feels as though the argument might subside for a moment, but-"
    show yuri mh b1d ldown at t21
    show sayori mk at thide
    hide sayori
    show natsuki b3a e1b mm at t22
    $ autofocus.force_focus("natsuki")
    $ autofocus.force_focus("yuri")
    $ autofocus.restore_focus("sayori")
    "-Only a moment later, it resumes in earnest."
    show black onlayer above_master with {"above_master": Dissolve(3.0)}
    show natsuki cross mm b1d
    show yuri md
    $ autofocus.restore_focus("yuri")
    "My hands now clutch at my ears and head, the aching echoing through the rest of my body."
    show natsuki mj
    show yuri mg e2a
    $ autofocus.force_focus("yuri")
    $ autofocus.restore_focus("natsuki")
    "My work remains untouched in front of me, and it occurs to me that I've no idea how long it's been since I last wrote a line, depsite my best efforts."
    show yuri e1a mh
    _mc mf "They're still shouting...!"
    show natsuki turned lhip rhip mm b3a e1b
    show yuri md
    $ autofocus.force_focus("natsuki")
    $ autofocus.restore_focus("yuri")
    "Something about manga now."
    show natsuki b1d e1a mh ldown rdown
    "As much as I tried to avoid it, it seems they've changed from their previous argument, which is probably why they're still able to continue..."
    $ autofocus.restore_focus("natsuki")
    show natsuki md
    "Monika's voice now joins the pandemonium, only further contributing to my misery, though it would seem no-one's noticed."
    "Like stabbing needles, every consonant drives deeper into my skull, taxing me more and more effort just to stay still."
    
    play sound ["<silence 0.2>", audio.chairmoving]
    play music poempanic

    hide natsuki
    hide yuri
    show yuri turned mj b1d rup:
        xcenter 0.34 zoom 0.8 ypos 1.03 yanchor 1.0
    show natsuki turned e1b b3a mm lhip rhip:
        xcenter 0.66 zoom 0.8 ypos 1.03 yanchor 1.0
    show bg:
        blur 1.5
    camera master:
        align (0.5, 0.1) zoom 1.4
    hide black
    with NonBlockingDissolve(0.2)
    "After one too many comments from someone, my legs force me to my feet, sending the chair screeching across the floor."
    mc bd nb eb mg "For the love of god, guys!"
    show yuri shy bc eb md nc:
        easein 0.3 xcenter 0.25
    show natsuki cross e2c b3d mj nd:
        easein 0.3 xcenter 0.75
    show bg:
        easein 0.3 blur 0.4
    camera master:
        easein 0.3 zoom 1.1
    "I receive two sharp glares, which quickly shift to looks of shame."
    mc ea "I know you guys have differing opinions, but c’mon, let’s settle something, right here, right now."
    show bg:
        blur 0.0
    camera master
    show natsuki at i22
    show yuri ma at i21
    with Dissolve(0.2)
    "I stand up, placing my revision book to the side, and walk over to the front of the room."
    _mc ba ma na "Sure, when I walked in, it was nice and peaceful."
    _mc ec mh "That was, of course, until these two got into an argument."
    _mc ea bd "{b}Again.{/b}"
    mc mg "Tea is good, so is hot chocolate, and so is coffee."
    show yuri mb na
    mc eg bi "Manga is a form of written expression involving words, therefore by definition making it literature."
    mc ea ml ba "And finally, someone having an opinion different to you does not make them less than you, it makes them experienced in a different way, and learning from those experiences are what make you stronger and wiser."
    show yuri nb ba
    mc bd mg "Do I make myself clear?"
    show natsuki e1a b1d md 
    show yuri ma 
    "A couple of blank stares bounce across the room."
    mc ml "Good."
    mc bi eg mg "Now, can I focus on my revision, please? I wasted pretty much all of yesterday, so I need to make up for it."
    hide yuri
    hide natsuki
    show bg class_2_day:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    show sayori turned md at i11
    with Dissolve(0.2)    
    $ autofocus.block("sayori")
    $ say_transition = True
    s mh lup "... When did you get so studious?"
    show sayori md with say_dissolve
    mc ec mh "..."
    show sayori ldown with say_dissolve
    mc ef ml "When I lost the rest of what meant anything to me."
    show sayori e2c with None
    hide sayori
    show bg club_day:
        blur 0.0
    camera master:
        align (0.0, 1.0) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    stop music fadeout 4.0
    "I return to my seat with a cryptic statement."
    _mc mh "Sayori knows. I know she knows."
    _mc bg "... I shouldn’t have said that. It’ll just make them worried."
    _mc eg "Hell, I shouldn’t have blown up like that at all. It’s not really in my nature to get so worked up."
    _mc ec "Everything’s just gotten... so stressful lately."
    _mc ea ba "Dealing with people?"
    _mc ec bi "It’s a mess."
    _mc eg "Makes me tired."
    call close_eyes(1.0) from _call_close_eyes_10
    _mc "So..."
    _mc ba "Tired..."

    stop music
    scene black
    pause 1.0
    camera master:
        zoom 1.0
        blur 5.0
    with None
    scene bg school_infirmary_night
    with dissolve_scene_full
    camera master:
        linear 5.0 blur 5.0
    pause 1.4
    call blink(base_blur=5) from _call_blink_11
    pause 1.0
    call blink(base_blur=0) from _call_blink_12
    pause 1.7
    $ set_date(hour=19, minute=9)

    _mc turned bun nostrands ec mh "This... isn’t the clubroom."
    _mc ea "Where...?"
    mc mf bd "Huh?"
    camera master
    show cg natsuki 2 ec at Flatten with cg_dissolve
    $ persistent.natsuki.mark_cg(2)
    $ say_transition = True
    play music ["<silence 0.4>", audio.anewday]
    "I’m lying in a small hospital-style bed. Looks like the school’s infirmary."
    "I look to my side, and see the figure of Natsuki, curled up and grasping my left hand."
    "She’s sleeping soundly on my thigh."
    _mc ec ma ba "... Must be comfy, eh?"
    show cg eb bb with cg_dissolve
    n turned e1d b1c me "Ng- hmmph..."
    "She stirs, but doesn’t wake."
    "She must have been here a while, and judging by the fact that it’s getting pretty dark outside, I think it’s safe to say the others have gone home."
    _mc mh "Though, why she’s here in particular..."
    _mc eg ma "Best not to think about it."
    _mc ea "She was probably worried about me."
    show cg ba with say_dissolve
    n b1a "Hmm...?"
    show cg ea bc with say_dissolve
    n b3a mg "Oh, you’re..."
    show cg ec ba with cg_dissolve
    "She yawns, cutting herself off."
    show cg eb bb with cg_dissolve
    n b1c me "Awake..."
    "But does not move her head from its spot."
    show cg mb with cg_dissolve
    n mo b1a "That’s nice..."
    mc ed md "Sure is, yeah."
    show cg ec bb ma with cg_dissolve
    n b1d mg e3c "The doc said something about... stress..."
    n me "Gotta keep your stress levels down..."
    show cg ba ea with cg_dissolve
    n b3a e1a mg "So she wanted me to ensure that you got home safe..."
    mc ea mg "Wait, she’s not here anymore?"
    n "No, she went home..."
    show cg eb bb with cg_dissolve
    n e1d b1c "She left me the keys to lock up though..."
    mc ml "With you?"
    show cg ba ea with cg_dissolve
    n b3a e1a "Why wouldn't she leave them with me...? I'm a member of the Student Council, a prefect, and Chiaki's vice-president, and I've got a perfect record..."
    mc bd mg "You’re kidding. I mean, I knew you were a prefect - The armband is a dead giveaway, and you’re obviously a prefect if you’re also a member of the Student Council, but..."
    show cg bb ec with cg_dissolve
    n e3c b1a mh "Because it happened like last year, dude... That’s just what happens..."
    _mc eg bi mh "Mel, you idiot! How did it slip your mind that she’s the same person you saw running for President last year?"
    _mc ea bd "Not that I pay attention to the politics or anything that goes on around here, but still...!"
    show cg eb bc with cg_dissolve
    n e1d b1c "So I’m in charge of locking up and getting you home..."
    show cg ec bb with cg_dissolve
    n mg e3c "But it’s soooo comfortable here..."
    "She closes her eyes once more, nuzzling deeper into my thigh, and moving her head longitudinally toward my more..."
    "Sensitive areas."
    mc mj "Do you mind?"
    show cg mb bc with cg_dissolve
    n mo b1a "Mind? No, I’m Moses, watch me part the seas-"
    "She reaches up with her arms, gently pushing my thighs apart-"
    hide cg with cg_dissolve
    $ say_transition = False
    mc ba eg mg na "Aaand we’re done here."
    "I pick her up, and she seems to snap out of whatever stupor she was in."
    show natsuki e1d b1d mg:
        matrixcolor TintMatrix("#5d9be0")
        t11()
    n "Eh? Where am I-"
    n b3a e1b mi "Oh, Mel! You’re finally awake! I was afraid you were gonna sleep all day!"
    n e2a mh b1d "Though, to be fair, you just about did..."
    show natsuki ma
    mc ec mj ba "Yeah, don’t you play dumb with me."
    n b4 e1a mc "Me? Dumb? I’m the smartest in my class!"
    show natsuki b3a ma e3d
    "I frown. Either she’s playing me for a fool, or she genuinely has no idea what she just tried to do."
    _mc ea mh "Either way, that was... very forward."
    _mc ef nb "I, well... don’t know how I feel about it."
    _mc "I’d had a feeling something like this was going on, but-"
    _mc ea "How do I even begin to broach such a topic? She’s the best friend of someone I..."
    _mc ef "Someone I once held dear."
    _mc bi "Besides, so far all I’ve seen of her is..."
    _mc ec na "Not exactly flattering."
    show natsuki e1a
    _mc ea ba "I don’t know what to think, now."
    show natsuki b3a e3d me at hop
    "My thoughts are interrupted by her yawning and standing up."
    n e1a b1a mc "C’mon, let’s get you home."
    show natsuki ma at thide
    "I stand up, following her lead, and make my way out of the infirmary."
    hide natsuki

    scene bg school_corridor_3_night 
    show natsuki turned:
        matrixcolor TintMatrix("#181b3b") * ContrastMatrix(1.1)
        i11()
    with wipeleft

    "Natsuki locks the door behind her, and then walks by my side toward the front of the building."
    mc turned bun mg nostrands "So... You’re a member of the Student Council, huh?"
    n lhip e2a b3a mh "Sure am. Handover’s in... February, I think? So I’ve only got a couple months left. It actually keeps me busier than you’d think."
    show natsuki mj
    mc mb "What made you want to sign up?"
    $ autofocus.block("natsuki")
    n md b1d "Hmm..."
    "She pauses to think for a moment."
    $ autofocus.unblock("natsuki")
    n e1a b3a mh "I dunno. I think I was just inspired by Sayori."
    show natsuki ldown ma
    mc thinking ml "Sayori’s not part of the Student Council, though?"
    n b1a e2a mh "No, of course not, though I almost convinced her to run with me, last year."
    n e3c mb "I think it was more that I wanted to do a little more for people, like she did for me."
    show natsuki e1a ma
    mc ldown ef mb "Ah, I see. She has that effect on people, huh? You just want to do better when she’s around."
    n b3a mc "Exactly!"
    show natsuki ma
    "She tugs my sleeve and grins ear to ear."
    n mc e1a "That’s exactly it! Every time she’s around, it’s like all of your problems melt away!"
    n e3c mb b1a "All that’s left is to make everything around you better in some way!"
    show natsuki e1a ma
    mc ea "She really is like that! I can’t tell you how many times an entire room has been quelled from an argument just because she walked in. Even as a kid, it was crazy how often it happened."
    mc ml eg "I don’t know if it was people being polite to protect her innocence, or if it was something else, but every time."
    show natsuki e3c b3a
    mc mb "She just has that calming effect on people."
    n rhip e1a mh b1a "She motivates me to do better, to {i}be{/i} better, every day. How could I {i}not{/i} share that?"
    show natsuki ma
    mc ef mg "I know what you mean. When I lost her... I felt like my motivation left me too."
    show natsuki e2a md rdown
    mc ea bg mb "B- But hey, it actually worked out. She met you, who’s been driven to be better because of her, so I’m actually pretty stoked about that."
    n cross b3a mi "True... But honestly, rather than getting hung up on what did happen, I think it’s better to look forward. Big things are happening in this world; things you and I could hardly imagine."
    n turned b1d mh e1a "And I dunno about you, but I want to be a part of it."
    show natsuki md
    mc mg ba "What, are you gonna go into politics?"
    n e2a me "Hm."
    "She bites her lip, thinking to herself."
    n mh b1a "I hadn’t really considered it, but that’s not a bad idea."
    n mi "I was actually considering... I dunno, something simpler."
    n mb b3a e3c lhip "It’d be nice to just be able to relax, and see what opportunities come my way, you know?"
    n e1a mh "Not be completely lax, of course, but like..."
    show natsuki md
    mc ml thinking "You want to see what direction the universe pulls you?"
    n ldown mg "... Yeah."
    show natsuki ma
    mc mg ef "I don’t know if I could ever be like that. I’ve always been so driven and stubborn, it would be hard to just be dragged toward something."
    mc ea mb ldown "I think I’d miss the signals."
    n b1a e2a mc "Hah, probably."
    n e3c b3a mi lhip rhip "But hey, at least you’ll have someone by your side who can point you in the right direction."
    show natsuki mj
    mc mf "You mean Sayori?"
    n e1d b1d mh "I mean {i}me{/i}, dumbass. If you’re stuck with Sayori, you’re stuck with me."
    show natsuki ldown mn at dip
    "She gives me a friendly elbow as we reach the end of the building."
    show natsuki at thide
    hide natsuki

    scene bg school_gate_night
    with wipeleft
    show natsuki turned:
        matrixcolor TintMatrix("#4b739d")
        t11()

    "She turns around and locks it behind her, placing the keys into her pocket."
    mc turned bun nostrands mb "Hah, I could see that. You strike me as someone who would really enjoy a quieter life. Something I think Sayori’s been pining for, for as long as either of us can remember."
    n b3a e3c mh "You have no idea. I don’t know if I’d ever have the stamina to keep up with you, but..."
    n b1d e1a mb "I’ll give it a go, I reckon."
    show natsuki b1a ma at thide
    mc ef mg "You’re more than welcome to try, at least. I don’t know if I’d survive losing Sayori again, to be honest, even if it meant slowing down."
    mc mh "..."
    "Finally, we turn back toward the road and head off, continuing our conversation."
    hide natsuki

    scene bg school_street_night_on
    show natsuki turned:
        i11()
        matrixcolor TintMatrix("#9fbcdd")
    with wipeleft

    mc turned bun nostrands mg"To be honest, though, I’m still deciding what I’m going to be doing after school."
    mc mb "The old guy who runs the cafe I work at is wanting to retire soon, and I’m pretty sure he’s planning on leaving it to me."
    n b3a mh "Oh, that’ll set you up reasonably well, won’t it?"
    show natsuki ma
    mc ef ml "Yeah, but it’s also..."
    show natsuki e1a mj
    mc ea mg "A very quiet life for someone like me."
    n lhip mh "You mean you want to do more?"
    show natsuki mj
    mc mg "I want to see more, yeah."
    mc eg mb "To feel more, to know as many of the things there are to know."
    n e2a mg "Hah, well..."
    n b3a e3c mi "Some things are better off just as dreams. Don’t throw away the things you have for something elusive."
    show natsuki e1a ma ldown
    "I nod, thinking to myself for a moment."
    mc mg "Yeah, I think you might be right."
    mc ea mb "Still, I’d like to travel, at least a little. Even if it isn’t out of the country, just to see a new beach, or a new town."
    show natsuki b3a md
    mc ef ml "... I haven’t had a holiday since I was twelve."
    n b1d mh "That’s a long time to keep working for. Not even breaks from work?"
    show natsuki b1a mj
    mc ea mg "I’ve taken one or two sick days a year, but that’s been the extent of it. Other than that, I’ve worked basically non-stop."
    show natsuki b2a me
    mc ef ml "Don’t get me wrong, I enjoy what I do, but without parents to give me any guidance I-"
    "I cut myself off. I don’t want to drag her into my problems."
    n b2b mg "... You don’t have parents?"
    show natsuki mj b2a
    mc mg "... I do, but they’re divorced. I haven’t seen either of them since I was..."
    mc ea mb "About twelve or thirteen, yeah."
    n nc mb "... I’m sorry, I didn’t mean to bring up painful memories."
    n e2c b2b mh nb rhip "If it helps, I lost my mother when I was... maybe five or six?"
    n b2a e3d mb na "I don’t even think I was that old."
    show natsuki e1a rdown ma
    mc bg ml "I’m sorry, that must have been hard."
    n cross b2b mb "No, not hard, just... I was too young to really understand, you know? All I can remember now is the face she had when she tucked me in at night."
    n b2a e2a mh "... Even now, it..."
    show natsuki me nc
    "She looks away, and I can’t tell what sort of expression she wears, but I can guess it."
    n b1a mg nb "... I don’t think I even remember her face, anymore."
    n e1a mh b2a "Promise to not make fun of me?"
    show natsuki ma
    mc mg "How could I?"
    n turned e3c mh b2b "... Sometimes, when I’m cold and alone, I don’t even think it’s her face anymore."
    n nc e2a mb "... It’s Sayori’s."
    show natsuki md
    mc ml "I... I’m so, so sorry, Natsuki."
    "I reach out to touch her shoulder to comfort her, but she recoils as I do."
    show natsuki mm nc e1b b1d at hop
    n "N- NO!"
    n e1a b2a mh "W- Wait, I mean-"
    show natsuki me
    "I back away quickly, not wanting to cause any more distress, but the damage was done."
    n mg "I..."
    n cross e2a mh nb b1d "I’m sorry you had to see me like this."
    n mb b2a "I know it might sound stupid, especially after that, but it’s not your fault."
    n turned nc mh "I promise, it’s not-"
    show natsuki me b2b
    mc ef mg "I know. You don’t have to talk about it."
    n b2a e3c na mb "... Thank you."
    n e1a mh "And... don’t tell Sayori, please. I don’t want to worry her."
    show natsuki mj
    mc ba ea ml "... Is that wise?"
    n cross b2b mh e2a "She’ll understand. Besides, she-"
    extend e1a " She knows, better than most."
    n turned b2a mb nd "I don’t want to be a burden, Mel."
    show natsuki md
    mc bg mb "You’ve been nothing of the sort, I promise."
    mc ba mg "We all have struggles, and the more we share the burden, the lighter the load becomes."
    mc ef ml "... But I understand the desire to carry it alone."
    mc mg "Even Amelia doesn’t know what I’ve been through, and she..."
    mc ea bg mb "She means the world to me."
    show natsuki ma rhip
    "Natsuki gives me a small smile."
    n na b3a mh "Well, keep her close then, won’t you?"
    show natsuki me
    mc bb mg nb "Oh, wait, no, not like that, I-"
    n b1a mb rdown "Pff- Hah, I know. She’s your best friend, right?"
    show natsuki ma
    mc ef bg mb "Yeah. I have a weird way of showing it, though..."
    n rhip e3c b3a mg "Well, maybe you should change that."
    n e1a mh "Be more of a friend to her. Give her some of the respect she deserves."
    n rdown b1a mc "Hell, go have lunch with her tomorrow. I know you’ve been blowing her off to hang out with me."
    show natsuki ma
    mc ea mf ba na "How did you-"
    n lhip rhip mo e3d b3a "Student Council. I have my connections."
    mc ec mh "..."
    mc ef ml "Alright. I’ll do just that."
    show natsuki e1a b1d ma ldown at dip
    "She elbows me, giving me a warm smile this time."
    n rdown mc b1a "Take care, alright? It’s late."
    show natsuki ma
    mc eg mb "Nah, I’m not too far from here, don’t worry."
    n b4 mh "You live close to Sayori’s house?"
    show natsuki b3a md
    mc bm mg ed "Yeah? We’re neighbours."
    $ autofocus.block("natsuki")
    n "..."
    $ autofocus.unblock("natsuki")
    n e2a b3d mb nb "Y- Yeah, I, ah, right..."
    show natsuki ma
    mc ed md ba "You knew that, right?"
    n cross b1d e3d mc "Y- Yes, I definitely knew that..."
    show natsuki ma
    "I awkwardly chuckle along with her."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc ec ma "Something tells me, from her reaction, she hadn’t the faintest idea, which means..."
    _mc ea mh "My dream last night?"
    _mc eg ma "It must have been just that."
    _mc ec "Hah."
    hide black with NonBlockingDissolve(0.5)
    "With that weight off of my shoulders, I set off back home."

    $ add_calendar_description(calendar_descriptions["natsuki"][7])

    call week_2_thursday_natsuki from _call_week_2_thursday_natsuki
    return