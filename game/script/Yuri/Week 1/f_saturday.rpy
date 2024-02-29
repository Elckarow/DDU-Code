label week_1_saturday_yuri:
    call calendar_transition(day=28, hour=6, minute=0, second=5) from _call_calendar_transition_39
    scene black with Dissolve(1.0)
    show bg mc_bedroom_day_open with mc_pov(True)
    $ set_internet(True)
    $ set_pov("mc")
    play sound_loop phone_alarm fadein 1.0

    "With some annoyance, I press the snooze button and turn off my alarm."
    stop sound_loop
    play ambient ext_day fadein 3.0
    mc turned naked messy nostrands bg mg eh "Huaaaaaaaaaaaaaaaaaaaaaa!"
    mc ml ec ba "Work time..."
    "I look at the alarm clock."
    _mc ea mh "6 o'clock, huh..."
    _mc eg ma "Just ten more minutes..."
    _mc bi mh "No, bad Melody."
    hide black with NonBlockingDissolve(1.0, time_warp=_warper.ease_quad)
    "I throw myself out of bed, trying to avoid the disaster that is falling asleep again."
    "I sigh."
    _mc ec ba "I definitely need some more sleep..."
    _mc ef "This week has been so far from ordinary."

    stop ambient fadeout 1.0
    scene bg mc_living_room with fade
    play music cafe fadein 1.0
    $ set_date(hour=6, minute=30)

    "I get dressed in my usual barista uniform and head on downstairs."
    _mc turned casual "At least I'll be able to see the boss today."
    _mc mh thinking "Maybe he knows what I should do."
    extend ef ".. in regards to knowing Yuri better, I mean."
    "I take a glance at the clock hanging in my living room."
    _mc nb bd eb ldown "6- 6:31?! I need to hurry up!"
    "Rushing my breakfast, brushing my teeth, and tidying up my hair, I rush out the door."

    scene bg cafe_outside_day with wipeleft_scene
    $ set_date(hour=7, minute=15)
    $ set_internet(False)

    "Looking at the clock, it appears to be 7:15."
    _mc turned casual nb mf "Phew... just in time."

    scene bg cafe_inside_day with wipeleft
    
    "As I enter from the back, the place already seems quite busy, and all at once my feet seem to find themselves unsteadily wobbling beneath me."
    "Standing there, I suddenly feel a hand on my shoulder."
    mc turned casual mj eb bg nb "E- Eh?!"
    "I whirl around quickly."
    camera master:
        align (0.5, 0.0) zoom 1.5
    show boss turned at i11
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ persistent.boss_seen = True
    $ autofocus.block("boss")
    $ say_transition = True
    b ed mc "Relax, kiddo! It's just me."
    b me ea bc "You alright?"
    show boss md with say_dissolve
    mc mb ef "A- Ah. Sorry about that."
    mc eh bf md "... Yeah, I'm alright, just a bit tired, that's all."
    b me bb "Tired? Yer usually come here with a smile on yer face."
    b ba mb "Yer certain nothing's wrong, kid?"
    b ed mc "You know you can tell me."
    show boss ma with say_dissolve
    mc ma ba ef "..."
    _mc bi mh "Why do I feel nervous all of a sudden?"
    _mc ea ba "The boss is the kindest person I've met, having helped me with things my parents should've helped me with."
    _mc ef "Like taxes. And..."
    _mc ma "So on..."
    show boss ea md with say_dissolve
    mc eg mb "It's.. nothing to worry about right now."
    show boss bb with say_dissolve
    "The boss looks me in the eyes, clearly suspicious."
    b me "You know, kid..."
    show boss md with say_dissolve
    mc ea mf na ba "Huh?"
    b me ec bc "I've been your age too."
    b ea rup bb "So, I know when someone like yer is feeling under the weather."
    show boss md with say_dissolve
    mc ef mh "..."
    b rdown ba mb "How 'bout we talk about it after work?"
    show boss ma with say_dissolve
    mc mb "Y- Yeah. Thanks, boss."
    b mc ba ed "Alright, now give today your best, kiddo. Holler if yer need me!"
    mc eh md "Will do!"
    camera master
    hide boss
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("boss")
    $ say_transition = False
    "The boss walks on ahead past me."
    call close_eyes(duration=0.5) from _call_close_eyes_22
    "As I head off to my own post, I keep thinking..."
    _mc ef mh "Why do I feel afraid to tell him?"
    _mc ec "I think..."
    "..."
    $ set_date(hour=8, minute=4)
    _mc eg ma "In the long run, this kind of feels dramatic, doesn't it?"
    _mc ea thinking "Maybe the boss doesn't like drama..."
    cu "Hello, can I get a coffee please?"
    call open_eyes(duration=0.15) from _call_open_eyes_14
    mc mg nb eb bb "A- Ah, right, coming right up!"
    _mc ea ba mh "A customer already? I've only just clocked on..."
    "While preparing the coffee, I look at the time."
    _mc bd eb "Wait, it's 8 o'clock already?!"
    _mc ec bi "Geez... stop daydreaming, Mel..."
    "Deciding to bury my thoughts, I shake off the mental cobwebs and pour myself into my daily duties."

    scene bg cafe_inside_day with wipeleft_scene
    $ set_date(hour=15, minute=7)

    "Time passes me by quickly, as it often does around here."
    "As customers leave and the number of new customers replacing them slowly wanes..."
    show boss turned at t11
    b mb rup lup "Alright, kid. It's 3 o'clock. Time to wrap it up."
    b ed mc "Let's clean this place for tomorrow, yeah?"
    "He waves at the girl standing behind the counter, who gives him a nod and steps back into the kitchen."
    show boss at thide
    _mc turned casual apron mb "Gotcha, boss."
    hide boss
    "As I prepare to grab some cleaning equipment myself-"
    camera master:
        align (0.5, 0.0) zoom 1.5
    show bg:
        blur 2.0
    show boss turned bb md at i11
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("boss")
    stop music fadeout 3.0
    b me "Except you, you deserve a break. Remember what I told yer earlier?"
    show boss md with say_dissolve
    mc bb nb mf "O- Oh, yeah."
    _mc ef bi mh "What's with me stuttering so much today?"
    _mc eb bd "I'm not subconsciously becoming Yuri, am I?"
    show bg cafe_kitchen_day:
        blur 0.0
    camera master
    hide boss
    show boss turned noapron ec bc md lup at i11
    with Dissolve(0.5)
    if preferences.language is None:
        $ auto_advance_date_mult = 2.67
    $ say_transition = False
    "As the boss leads me into the kitchen, he takes off his apron and points to a nearby table and chairs."
    "The same ones we use for our lunch breaks, huh."
    $ autofocus.unblock("boss")
    b me ea ba "Take a seat, kiddo."
    show boss md ldown with None
    camera master:
        align (0.5, 0.0) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("boss")
    $ say_transition = True
    "I close the door behind us and take my seat."
    b eb bb "..."

    play music pensive

    # [Full Voice Acting]
    b me ba ea "So... what's going on?"
    b ed mc "Only if yer feel comfortable telling me, of course."
    "..."
    show boss ea md with say_dissolve
    mc noapron mf ba na ef "Alright..."
    show bg school_library_afternoon onlayer above_master 
    show white_flashback onlayer above_master
    show monika turned noblink lpoint mb onlayer above_master:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with NonBlockingDissolve(0.5)
    mc ea mg "Monika, a friend of mine, introduced me to her school club."
    mc ml "The Literature Club."
    camera above_master:
        alpha 0.0
    show boss mb
    with NonBlockingDissolve(0.5)
    b "Ah, I remember that one."
    b me "What do yer guys do? It still the same as I remember from those stories Misato and {i}Karin{/i} used to tell me, back when it was their spin through senior year?"
    show boss md with say_dissolve
    "I internally wince at that name, but brush it aside. I need to get used to hearing it, and that's obviously why he didn't dance around it."
    mc ef mb "Well, so far, we read a lot."
    mc ea "Read and make poems."
    mc mg "Then we show them to each other and try to interpret their meanings."
    mc mb "The first few days went really well."
    camera above_master:
        alpha 1.0
    show bg club_day onlayer above_master:
        align (0.0, 0.8) zoom 1.9 blur 0.0
    hide monika onlayer above_master
    show yuri turned noblink e2a md b1d at i42 onlayer above_master
    hide boss
    with NonBlockingDissolve(0.4)
    mc ef ml "Due to some unforeseen force, Yuri and I got paired together."
    $ say_transition = False
    mc ea mg "Oh, right. Yuri, she's one of the Literature Club members."
    b turned noapron mb "Sounds like a fun place, I reckon."
    mc mb "Yeah, the Literature Club {i}is{/i} fun!"
    mc mf "It's just..."
    extend ef bi ml " I think..."
    camera above_master:
        align (0.5, 0.1) zoom 1.3
    show bg class_1_day onlayer above_master:
        blur 2.0 zoom 1.0
    show yuri e1d ma b1a at i11 onlayer above_master 
    with NonBlockingDissolve(0.4)
    mc ba mg "I'm starting to feel something for Yuri..."
    show boss md at i11
    camera above_master:
        alpha 0.0
    with NonBlockingDissolve(0.3)
    "The boss looks at me with mild surprise, but he doesn't speak."
    show boss ec mf lup with say_dissolve
    "He only gestures for me to continue speaking, so I do."
    mc ea "So, this last Thursday..."
    show boss ea md ldown
    show cg yuri 2 turn onlayer above_master
    hide yuri onlayer above_master
    camera above_master
    hide bg onlayer above_master
    with NonBlockingDissolve(0.5)
    mc mb "I tried to get her to know better, and to do that, we..."
    extend ef ml " went to the courtyard."
    mc bi mg "I {i}was{/i} going to bring her out to the park, but that would be too far away."
    mc eg mb "And before you say anything, yes. I am well aware that the park would not have been the right spot for introductions."
    mc ea ba mg "... At least, I don't think so. Neither was the courtyard really, but it was the closest alternative."
    camera above_master:
        alpha 0.0
    with NonBlockingDissolve(0.5)
    "The boss doesn't respond, just giving me his full attention."
    mc ml "Since, you know... parks are supposed to be romantic, right?"
    mc ef mg "Or just... taking a stroll together, side by side, all out of the blue?"
    mc ea ml "It really could've given Yuri the wrong impression."
    show boss ec with say_dissolve
    mc ef mf "At least, initially..."
    mc mb ea "Making such a move that early is just not a good idea, you know?"
    $ clear_layers("above_master")
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ autofocus.unblock("boss")
    b ea lup me "Ask yourself, why did you choose the courtyard?"
    show boss md
    _mc ea mh "..."
    show boss ldown
    mc ef mf "I... uh..."
    mc ea mg "It made sense at the time."
    mc eg mb "It was one of the most calming places on the school grounds."
    mc ef ml "Meaning that we wouldn't be disturbed..."
    b me "And those factors turned out to be true, didn't they?"
    show boss md
    mc mh "..."
    show boss ma
    mc ml bm thinking ed "Yeah...?"
    b mb "Then, it was the right place to be in. It all worked in yer favor."
    show boss ma
    mc ec ba mh "Mmm..."
    show boss md
    mc mg ea ldown "But, that's not all that bothers me."

    show white_flashback onlayer above_master
    show bg club_day onlayer above_master
    show yuri turned noblink lup e1d md b1a at i21 onlayer above_master
    show natsuki turned rhip noblink e2a mg b1d at i22 onlayer above_master
    with NonBlockingDissolve(0.5)

    mc ml "Yesterday..."
    mc ef bg mg "She was very nervous yesterday."
    mc bi ml "I kind of ignored the signs, considering Yuri almost always seems stressed."
    mc ea mg ba "Yet, when Natsuki, another Literature Club member, took her outside the clubroom..."
    hide natsuki onlayer above_master
    hide yuri onlayer above_master
    hide boss
    show natsuki turned noblink lhip e2a md at i11 onlayer above_master
    with NonBlockingDissolve(0.4)
    mc ml bg "... Yuri hid in the restrooms and wouldn't come back out until much later."
    b turned noapron me "Because of Natsuki?"
    mc ef bi ml "I think so. But, not just her."
    mc mh "..."
    mc eg mg "I feel like I am at fault, too."
    hide natsuki onlayer above_master
    show monika turned noblink md eb onlayer above_master:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    camera above_master:
        align (0.5, 0.2) zoom 1.5
    show bg club_afternoon onlayer above_master:
        blur 2.0
    with NonBlockingDissolve(0.4)
    mc ea ba "Monika told me Yuri's been quite stressed lately."
    mc ml bf "And, considering all these wrong moves I've been making the last few days..."
    mc ef bg "Just staring at her... dragging her out to the courtyard... flattering her poems..."
    mc mg "I feel like I've been... insensitive, maybe."
    mc eg bi mb "Only thinking about myself."
    $ clear_layers("above_master")
    show boss md at i11
    with NonBlockingDissolve(0.5)
    $ autofocus.block("boss")
    "..."
    b ec bc "..."
    "..."
    $ autofocus.unblock("boss")
    b ea ba me "Kid. From what I am hearing, you aren't doing anything wrong."
    show boss md
    _mc ea bd mh na "Huh?"
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    b me lup "You didn't know she was stressed, did you?"
    show boss md
    mc ml "No, I didn't..."
    b mb ldown "Then how could you have possibly foreseen this?"
    show boss ma
    mc ea ba mh "..."
    mc ef mf "I feel like..."
    show boss md
    mc bi ml "... Like it's my fault."
    mc eg mg "If I left her alone, maybe she wouldn't have such a hard time."
    mc ea bd ml "And then I-"
    show boss lup bc ec mf
    "The boss cuts me off."
    b ldown eb bb me "Oh, kiddo..."
    show boss md
    mc ea ba mh "Mm...?"
    b ec bc me "I know this kinda thing is common for people yer age, but..."
    b ea ba "Nothing in life will go perfect."
    b mb "However much yer try, there's just so much yer don't know yet."
    b eb "So much you won't ever know."
    show boss md
    "The boss takes a glance, then returns his gaze to me."
    b ea me "Even I have that issue."
    b lup bb ec "I do something, and it only seems to make things worse."
    b ea "Because I lack information."
    b ldown mb ba "{b}But{/b}, that doesn't mean it was wrong."
    b ed mc "Like fixing someone a cake, only to find out they don't like cake."
    mc bg mf "But-"
    b ea me bb "Wait a second there, I know exactly what you wanna say:"
    b eb "'That means you don't know them well enough'."
    b ec "'If you knew them well enough, you'd know not to make them cake', right?"
    show boss md
    mc ef mb "Y... Yeah..."
    b me ea "You're right, kiddo. And there's only one solution for that:"
    show boss ec md
    "He takes a deep sigh."
    b me ea "Getting closer."
    b mb ba "Getting to know them better."
    b ed mc "Spend time with them."
    "..."
    b lup eb bb me "Yes, sometimes that brings up hardships, both new 'n old..."
    b ea mb ba "But, I've known yer for a lifetime, Melody."
    b ldown ed mc "I'm sure you'll withstand it all."
    b ea mb "It'll turn out fine in the end, kiddo."
    show boss ma
    mc mf "I..."
    "..."
    b me "My advice? Support that girl, Yuri."
    show boss md
    "I find myself flustering a little, but I try to maintain my composure."
    mc nc bi eg mh "..."
    "I take a deep breath."
    mc ml ef ba nb "I'm not sure..."
    show boss bb
    $ advance_date(seconds=45)
    "He looks at the time."
    b ba mb "3:30, huh? Seems it's time to go on home."
    b me "I want you to think about it."
    b mb ec "Sit down somewhere calm and think back."
    show boss ma
    "I silently nod, as boss gives a smile."
    b mc ed "Well, enough blabbering from me, let's enjoy some free time."
    b me ea "Unless, you want more off yer chest?"
    show boss md
    mc mg na "No, I... I think I said everything I wanted to."
    mc eg mb "Thank you, boss."
    "I give him a warm smile to show my appreciation."
    show boss ma
    "He returns that smile."
    # [End Voice Acting]

    stop music fadeout 2.0
    scene bg residential_afternoon with longfade
    $ advance_date(minutes=30)
    $ set_internet(True)

    _mc turned casual ec ma "Saturdays always have this strange melancholy."
    _mc ea "Rarely having any contacts with friends, getting unshaken support from the boss..."
    _mc eg "Let's just enjoy some TV, alright?"
    "As I go to open the door, I hear some strange noises before getting tackled from behind."
    play sound fall
    camera master:
        align (0.6, 0.8) zoom 1.0
        easein_back 0.4 zoom 2.0
    mc mg bb nb eb "Ah!"
    mc mm ea bd "Get off of me!"
    am turned hairdown casual ec mb "Never~"
    show amelia ef ma rup lup:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.8
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    play music friendly_endeavours
    "As I turn my head, I see a certain blonde."
    mc mj ec bi na "Meelz?"
    am eb me "Yes, Mel?"
    show amelia md with say_dissolve
    mc ea ba mg "Get off me, please."
    am ed mb "Okay~"
    camera master
    show amelia ma rdown ldown
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    "Amelia hops down and takes a few steps back, allowing me to recover from this backbreaking blow."
    mc mb "Why message me if you plan to surprise me anyways?"
    $ autofocus.unblock("amelia")
    am ed mb "Why not?"
    show amelia ma
    "I take a deep sigh."
    mc mj eg bi "What did you want to show me?"
    am mb ec "Let's mozey on over to the living room first; it's not for the faint of heart!~"
    show amelia ma
    mc bb mg "Yeah, yeah..."

    scene bg mc_living_room with wipeleft
    show amelia turned casual hairdown at t11

    "Tired, I walk into the room and plop down onto the couch."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    "Amelia does much of the same, sitting down in the spot next to me."
    show amelia:
        xoffset 0 blur 0.0
        ease 0.3 xoffset 50 blur 2.0
    show bg:
        xoffset 0
        ease 0.3 xoffset 20 blur 0.0
    "The TV stares at me. Knowing I just want to... Relax."
    show amelia:
        easein 0.35 xoffset 0 blur 0.0
    show bg:
        easein 0.35 xoffset 0 blur 2.0
    _mc turned casual eg bi "Please just keep it quick Amelia..."
    am me "Remember Monday?"
    show amelia md with say_dissolve
    mc ml ec "... No?"
    am mb ee rpocket lpocket "Okay, Melody 'The Goldfish' Nakamura, I'll give you a hint."
    am ed me bh ".... Kaito."
    show amelia mc with say_dissolve
    mc ea bb thinking ml "Kaito...?"
    show amelia ec md ba with say_dissolve
    "I click my tongue."
    mc eg bi mg "Please don't remind me of his existence."
    am ef mb bb "Keep your friends close, but your enemies closer!"
    am ed mh ba rup "That's what some say."
    am ldown ea me "It's stupid, but I have an idea."
    show amelia md rdown with say_dissolve
    mc ldown bd ed md "Hold on. Are you going on a conquest against Kaito?"
    am mh bh ec "No-"
    show amelia ed mi bd with say_dissolve
    extend " I mean-"
    show amelia me ba ea with say_dissolve
    extend " Sort of."
    am eb mb "You know how I mod games sometimes?"
    show amelia md with say_dissolve
    mc ea ml ba "Yeah...?"
    am ba me "I had this brilliant idea."
    am ec mb "You wanted to punch Kaito back there, right?"
    show amelia ma with say_dissolve
    mc ef mg "... I always want to punch him, but continue."
    am mh ed rpocket "Touché."
    am me bb eb rup "Well - Take a look at this."
    show amelia ma rdown with say_dissolve
    "Out of her pocket she retrieves a game console."
    "She opens it, revealing that it has two screens."
    am me ed ba "Just lemme boot it up real quick..."
    show amelia md with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    mc mb ea "In the meanwhile, I'll grab some tea. Do you want some too?"
    $ autofocus.unblock("amelia")
    am mb ba ee "Nah, no need."
    show amelia ma

    scene bg mc_kitchen_day with wipeleft

    _mc turned casual m eg bi "Aaaaaaahh, I just wanted to relax today...."
    _mc ec mh "What's gotten into her, coming here to show off... whatever she will be showing off?"
    play sound_loop kettle1
    _mc ma ba "At least I've got some tea to help me."
    "As the tea pot boils, I sit down on a chair to wait it out."
    $ renpy.music.set_volume(0.3, 3.0)
    if preferences.language is None:
        $ auto_advance_date_mult = 5.714
    call close_eyes(0.6) from _call_close_eyes_23
    "I close my eyes."
    show yuri turned onlayer above_master:
        i11
        flash
    "Thinking of Yuri."
    show bg club_day onlayer above_master at flash
    "Of the Literature Club."
    hide yuri onlayer above_master
    _mc ea thinking mh "What really happened yesterday...?"
    hide bg onlayer above_master
    _mc ec "There's something I am unable to discern."
    _mc ea "Is it... about me?"
    _mc mf "Maybe Yuri-"
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    am turned casual hairdown eb mb "Hey, hey! Are you still coming, Mel?"
    call open_eyes(1.0) from _call_open_eyes_15
    $ renpy.music.set_volume(1.0, 0.5)
    _mc ldown ec bi mh "Stop calling me Melody, dammit..."
    _mc ef "What's with everyone's obsession with that lately?"
    stop sound_loop fadeout 3.0
    "I sigh, pouring my tea, and heading back to face Amelia."

    scene bg mc_living_room
    show amelia turned casual hairdown rup lup mc at i11
    with wipeleft
    pause 0.02
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("amelia")

    "Sitting next to the girl, I glance over at her console."
    mc turned casual mg "So what did you want to show me so badly?"
    am mb ldown ec "Look at this."
    show amelia ma with say_dissolve
    "She shows the screen, showing a fighting game."
    _mc mf "Wait..."
    extend eb bd mh " is that... Kaito?"
    "In the character roster, there is one character that has the face of Kaito, and one with my face."
    "Poorly modelled at that, but if you squint, you can almost be convinced that they are official characters."
    am ef mb "Here! Beat him up!"
    show amelia ma with say_dissolve
    mc mf ea "Pardon? What?"
    show amelia rdown ea with say_dissolve
    "Amelia shoves the console into my hands."
    mc ml "I've never pl-"
    am ee mb "I'm sure you'll get the hang of it!"
    show amelia ma with say_dissolve
    mc mf bi ec "Okay..."
    "I pick myself as my character, and Kaito as my opponent and start playing."
    show amelia mc ea with say_dissolve
    mc ea mg ba "Isn't this illegal?"
    am me bg "Playing games?"
    show amelia md with say_dissolve
    mc ed bm mj "No, I meant our likenesses in the game!"
    mc ea bd mg "Where did you even find this image of mine?"
    am ed mc ba "..."
    am ea me "You see... I've stolen Kaito's from his social media, and yours I had lying around somewhere."
    am ef bd rup lup mb "It's not illegal though, I promise!"
    am ldown ed me ba "{size=-7}Unless we release it to the public...{/size}"
    show amelia md with say_dissolve
    mc ml "Would you care to repeat that?"
    am mb ef rdown "Oh uh, nothing, don't worry!"
    show amelia ma with say_dissolve

    scene bg mc_living_room
    show amelia turned casual hairdown rpocket ed at i11
    camera master
    with fade
    $ say_transition = False
    $ set_date(hour=22, minute=36)

    "After I beat up Kaito some more - in game - losing and winning several times, I look at the time."
    _mc turned casual eb bd nb mh "-It's half-past ten?!"
    "On the verge of yawning, I pause the game and look at Amelia."
    show amelia eb md
    mc mg ea na "Amelia, I think it's about time I get some sleep."
    $ autofocus.unblock("amelia")
    am me ea bg "Really? Don't you like all nighters?"
    show amelia md 
    mc mj ec bi "... Got some screws loose in that dome of yours?"
    am ba ef mb "Maybe~"
    am ed me lup "But, if you say so. I think I'll go home then."
    show amelia ea ma ba ldown at dip
    "I give her the console back."
    mc ed md ba "That was strangely fun. Thanks dude."
    am eb me "Want me to mod others into it next time?"
    show amelia md
    mc mg nb ea bb "Wha- That sounds like far too much effort for what it's worth!"
    am ec mh lpocket "This is easier than you think, but okay."
    am ed mb "You sure are a tough crowd to please~"
    show amelia md ea
    mc mb ba "You too need sleep, you know."
    mc eg mg bb "It's proven that adults need at least 7 hours of-"
    am mf ee lup bb "Yeah yeah, {i}mother{/i}... I'll sleep on time."
    am ba mb ef ldown rdown "... But only today~"
    show amelia ma at rhide
    hide amelia
    "As Amelia grabs her stuff, she opens the door and leaves." # im stuff
    "..."
    _mc ec bi mh "Wait."

    scene bg residential_night:
        blur 1.0 align (0.1, 0.0) zoom 1.2
    show amelia turned hairdown casual ed md:
        ypos 1.03 yanchor 1.0 xcenter 220 zoom 0.57 
        matrixcolor TintMatrix("#4b598f") * BrightnessMatrix(-0.2)
    camera master:
        align (0.0, 1.0) zoom 1.3
    with wipeleft_scene
    $ say_transition = True
    $ autofocus.block("amelia")

    mc turned casual mg "Wait, Amelia!"
    show amelia ea with say_dissolve
    "She stops halfway down the walkway, turning back to look at me."
    am eb mf lup "{size=-9}Yeah?{/size}"
    show amelia md with say_dissolve
    mc bb "Isn't it late out?"
    am mf "{size=-8}I can manage!{/size}"
    show amelia md with say_dissolve
    _mc ba ec mh "... I can barely hear her."
    mc mg bc ea "{size=+5}Come back here so we can talk!{/size}"
    am ldown bh ee mh "{size=-12}Fine...{/size}"
    show amelia md with say_dissolve

    scene bg mc_house_entrance_night
    show amelia casual hairdown turned lpocket rpocket mc ec bg at i11
    camera master
    with wipeleft
    $ say_transition = False

    "Amelia walks back over to me, a mix of confusion and mild irritation on her face."
    $ autofocus.unblock("amelia")
    am me "So what was the issue?"
    show amelia md
    mc turned casual bd ml "You can't just walk out this late on your own, you know? Your house isn't next door!"
    am ea ba me "Yeah? Then what do you propose?"
    show amelia md eb
    mc thinking mg ba "... Maybe, you can stay at my place for the night? I have a spare bed and-"
    am rup mb ed bd "I'll pass on that. No hard feelings or anything, but my sister would be dead worried about me if I didn't get home tonight."
    show amelia ma rpocket
    _mc ec mh "Then, uh..."
    mc ea mb ldown "What about a taxi? I could hail one over for-"
    am be eb mi lup rup "No! Don't do that!"
    am lpocket rpocket ed me "... Er, I mean, don't."
    am ea mb bc "I can pay for the taxi myself, okay?"
    show amelia ma
    "I let out a sigh."
    mc ml ec "You sure?"
    am ef ba mb rup "Absolutely positively."
    show amelia ma
    mc ef "... Alright."
    mc ea mb "At least stay here until the taxi comes by?"
    show amelia ed mc bh ldown rdown
    "Amelia rolls her eyes."
    am mi "Alright, {i}mom.{/i}"
    show amelia mc

    scene bg mc_house_entrance_night
    show amelia casual hairdown turned md ed at i33
    with wipeleft_scene

    "After a few minutes, the taxi arrives."
    show amelia ee at dip
    "Amelia grabs her stuff," # im stuff
    show amelia ea ma rup at t31
    extend " turns around to wave at me,"
    show amelia rpocket lpocket at thide
    hide amelia
    extend " then walks out the door."
    "I wave at her as she enters the taxi, driving off into the distance, then close the door behind me."
    
    stop music fadeout 2.0
    scene bg mc_bedroom_night_closed_off with fade
    play ambient int_night fadein 2.0

    "I dress into some comfortable clothes, head into bed, and think back on this whole day."
    _mc turned casual eg mj "So tired... Thanks for that, Amelia."
    show white_flashback onlayer above_master
    show bg cafe_kitchen_day onlayer above_master
    show boss turned noapron noblink mb at i11 onlayer above_master
    with NonBlockingDissolve(0.5)
    "I think back to my conversation with the boss."
    _mc ea mh "Never did I expect him to be so understanding..."
    _mc ec thinking "Is it true that I should just..."
    _mc ea ma "Worry less, and get to know Yuri better...?"
    _mc mh "..."
    $ renpy.scene("above_master")
    with NonBlockingDissolve(0.5)
    _mc ec ma ldown "Yeah."
    _mc eg "I'll try my best."

    $ add_calendar_description(calendar_descriptions["yuri"][3])

    call week_1_sunday_yuri from _call_week_1_sunday_yuri
    return