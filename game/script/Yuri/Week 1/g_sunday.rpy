label week_1_sunday_yuri:
    call calendar_transition(day=29, hour=10, minute=0) from _call_calendar_transition_40
    scene black with dissolve_scene_full
    $ phone_available = False

    _mc turned naked messy nostrands bi mh eg "Zzzzz..."
    _mc "Zzzzzzz..."
    _mc "Zzzzzzzzzz..."
    play sound phone_notification
    phone register "lit_club":
        time hour 10 minute 0
        "m" "Hey everyone! The culture festival is soon upon us, and for that, we need supplies for preparation. Who would like to go shopping with me? I was thinking sometime around 4 pm?" 
    pause 0.5
    mc ec mf "Huh...?"
    mc eg ba ma "No... Let me sleep some more..."
    "Completely ignoring whatever may be in the notification, I drift off to sleep again."
    phone register "lit_club":
        "s" "I'm in!"

    scene black with Pause(1.7)
    $ advance_date(hours=3, minutes=12)

    "It isn't until hours later..."
    
    scene bg mc_bedroom_day_closed with Dissolve(1.0)

    mc turned messy naked nostrands eh bg mg "Yaaaawn..."
    "I get dressed as usual, and look outside."
    show bg mc_bedroom_day_open with NonBlockingDissolve(0.5)
    play ambient ext_day fadein 1.0
    mc ec bi mf "Why is it so bright out...?"
    "One glance at my phone shows the time."
    mc mg eb bd nb "One?! In the PM?!"
    _mc ec bi ma "Geez, seems I {b}really{/b} needed that sleep..."
    mc na ba ea mf "Wait."
    "I grab my phone, and see a text."
    phone discussion "lit_club":
        pause
    $ phone_available = True
    _mc ec bi mh "So that's what was buzzing earlier today..."
    _mc ea ba "Didn't imagine Monika to be the type to spontaneously plan things on the same day..."
    mc ec thinking "Hmm..."
    mc ea ml "Well, I have nothing else to do today, so..."
    phone discussion:
        time auto True
        "mc" "Sure!"
    phone end discussion
    _mc ef bi ma ldown "I'm sure glad I didn't wake up at 3..."
    
    stop ambient fadeout 1.0
    scene bg mc_kitchen_day with wipeleft
    $ advance_date(minutes=23)

    "While I quickly fix and eat some breakfast, I wonder about something:"
    _mc turned casual ec bi mh "The festival..."
    _mc ea ba "What is that about?"
    _mc eg ma "I guess I'll find out eventually."
    
    scene bg mc_living_room with fade
    $ set_date(hour=15, minute=20)

    "As 4 pm nears, I head over to the mall."
    
    scene bg mall_int_2_afternoon with wipeleft_scene
    $ set_date(minute=55)
    $ set_internet(True)
    play music school

    _mc turned casual mh "It's quite busy today."
    _mc ec "Well, it is a Sunday, but still."
    camera master:
        align (0.0, 0.4) zoom 1.7
    with Dissolve(0.2)
    "I look around, and see tons of shops."
    "Tons of things to buy."
    camera master:
        align (1.0, 0.5) zoom 2.0
    with Dissolve(0.2)
    "... And things not to buy."
    _mc ma "Malls seem to have everything, huh...?"
    camera master
    with Dissolve(0.2)
    _mc ea mh thinking "I wonder why I never go to malls?"
    _mc ec "The last time I stepped foot in here was..."
    "..."
    _mc eg ldown "... Let's not approach that today."
    "As I take another step, I look inside the stores."
    _mc eb bg "Busyness to the max in the clothing stores..."
    _mc ec bi "The supermarkets could be described as health hazards..."
    _mc ea ba "Oh, and the restaurants never have clean tables."
    _mc ef ma "I remember why I never go to malls now..."
    m turned casual mb nb"MC! Glad you made it!"
    show monika ma ed nb:
        matrixcolor TintMatrix("#ffecdb")
        t11
    mc mb ea "Monika!"
    "Monika rushes to catch up with me."
    _mc ec ma "I must've been speed-walking while observing my surroundings..."
    mc ea mb "Glad to see you too."
    m ea md "Seen Sayori yet?"
    show monika mc na
    mc md ed "Nuh-uh."
    mc ea mb "But, she'll be here soon."
    show monika ma
    mc eg "She's never one to come {i}too{/i} late."
    camera master:
        align (0.5, 0.5) zoom 1.5
    show monika ea mc:
        yoffset 160 zoom 0.9 xoffset 0 blur 0.0
    show bg:
        blur 1.5 xoffset -35 yoffset -20
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("monika")
    m eb mb "... I think you're right."
    m ea lpoint md "Let's go sit on that bench while we wait."
    show monika turned casual lpoint:
        ease 0.5 blur 2.0 xoffset 150
    show bg:
        ease 0.5 blur 0.0 xoffset -15
    "She points to a nearby bench, luckily having no one else sitting there."
    camera master
    show bg:
        offset (0, 0) blur 1.5 align (0.47, 0.57) zoom 3.0
    show monika turned mc eb ldown:
        xcenter 0.3 blur 0.0 xoffset 0 yoffset 300 zoom 1.2
    with Dissolve(0.2)
    "We sit and both glance in multiple directions."
    show monika ea with say_dissolve
    mc ea "So what are your plans for this dangerous shopping trip, madame president?"
    m rhip bc ed mb "Ohoho, we'll be going into the deepest depths of the malls."
    m ea ba "To get the best decorations it can offer."
    show monika ma with say_dissolve
    mc ef mg "Look, I know I'm {i}supposed{/i} to know this, but I've never cared enough to ask before this year - What is the culture festival, anyway?"
    m mb "I'm glad you asked!"
    show monika ma rdown with say_dissolve
    "Monika smiles, her hands on her lap."
    m md "It's a day when we'll introduce the Literature Club to everyone."
    show monika mc with say_dissolve
    mc ml bg nb ea "E- Everyone?"
    m bc eb mb "Everyone interested, that is."
    m ba ea lpoint md "We'll show them what we usually do in the club and get them interested!"
    show monika mc with say_dissolve
    mc mg na ba ef "That sounds difficult."
    show monika ec ldown with say_dissolve
    "Monika nods in agreement."
    m mb ea "And that's why we need to prepare for it."
    m md rhip ec "And what better way to start..."
    m ed mb "... Than with decorations?"
    show monika ma with say_dissolve
    $ autofocus.block("sayori")
    "Before we realise it, a wild Sayori appears!"
    show monika:
        ease 0.3 xoffset -120
    show bg:
        ease 0.3 xoffset -20
    camera master:
        blur 0.0
        ease 0.3 blur 2.0
    show sayori turned lup rup casual mc e3d onlayer above_master:
        matrixcolor TintMatrix("#ffecdb")
        ycenter 0.7 xcenter 1.6 blur 2.0 zoom 2.3 rotate -70
        ease 0.3 xpos 1.04 blur 0.0
    s "Heyo!"
    show sayori ma onlayer above_master with say_dissolve
    mc  mj bg eb nb "W- Woah!"
    mc ec bi mg "Where did you come from?"
    show sayori mn onlayer above_master with say_dissolve
    "Sayori smirks."
    hide sayori onlayer above_master
    show sayori turned casual lup rup e3d mn:
        matrixcolor TintMatrix("#ffecdb")
        i22
    hide monika
    show monika turned casual:
        i21
        matrixcolor TintMatrix("#ffecdb")
    camera master
    show bg:
        blur 0.0 offset (0, 0) zoom 1.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("sayori")
    s rdown e1a mh "Some call me the master of sneaking."
    s ldown e1d b1d mb "But in truth, I can {i}teleport.{/i}"
    show sayori ma
    mc eg mb na ba "I'm sure you can, Sayori."
    $ autofocus.unblock("monika")
    m mb ed "Glad you made it, Sayori."
    m ea md "Now that we're all here..."
    m mb "How about we go?"
    show monika ma
    show sayori lup e3d b1a mb at hop
    $ autofocus.force_focus("sayori")
    "MC & S" "Yeah!"
    $ autofocus.restore_focus("sayori")
    show sayori ma with None
    hide sayori
    show monika at i11
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("monika")
    "We stand up and follow Monika."
    m md lpoint "First stop, decorations."
    show monika mc with say_dissolve
    mc thinking mg ea "What about that shop there?"
    show bg mall_int_2_afternoon as stuff onlayer above_master with NonBlockingDissolve(0.5):
        align (0.6, 0.5) zoom 4.0
    "I point to a little shop with a small number of customers, yet what seems to be a huge amount of banners and little trinkets."
    show monika ldown mb with None
    hide stuff with NonBlockingDissolve(0.5)
    m "Sure, lead the way, MC!"
    show monika ma with None
    show bg:
        align (0.6, 0.5) zoom 4.0 blur 0.0
    hide monika
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("monika")
    "We stop by the glass window, eyeing the many decorations displayed."
    mc ml "What are you specifically looking for, Monika?"
    show monika turned casual mb lpoint:
        matrixcolor TintMatrix("#ffecdb")
        t11
    m "I was thinking of something that fits the theme."
    m eb md "Things that display books, writing..."
    show monika ldown ea mc at t21
    show sayori turned casual lup b1d e1b me:
        matrixcolor TintMatrix("#ffecdb")
        t22 
    "Sayori perks up."
    show monika ma
    s b1a mh "Oooh... How cool would it be if we found something from our favourite writers?"
    show sayori e1a md
    mc mg ldown "Like from who?"
    s ldown mb "Seeing something from Anne McCaffrey would be amazing."
    show sayori ma
    mc mb "Oh, you mean the Dragonriders of Pern series?"
    s mc "Yep!"
    show sayori ma
    _mc ef ma "Goddamn, that takes me right the hell back..."
    m rhip md "I'm not sure if I have a favourite... But what about from Henry James?"
    m eb bb mb "Alas, I don't think this is that kind of shop."
    show monika ma
    "Suddenly, something grabs my attention."
    show sayori md
    show monika ea ba mc
    mc ea mg thinking "Hey, how about this?"
    "I point to a cheery looking banner, saying 'Writers unite!'"
    mc ec ml "I wonder what this could've been used for in the past..."
    s mb "I like it! What about you, Monika?"
    show sayori ma
    show monika bc ec at dip
    m "Hmm..."
    show monika rdown ea ba ma
    "She nods in approval."
    m mb "Good choice!"
    show monika ma
    "We begin rummaging through the store, attempting to find only the best and most exquisitely awesome decorations related to reading, time speeding on by all the while."
    
    scene bg mall_int_2_night
    show monika turned casual at i21
    show sayori turned casual b2b e3c mj nb at i22
    with longfade
    $ advance_date(hours=2, minutes=13)

    "As the sun slowly sets, our energy levels slowly but surely decline with it."
    show monika mc
    s mg "Uwaaaa..."
    s b2c xd mk "I am sooooo tired..."
    s e1a lup mh b2a "Could we take a break from carrying all these decorations...?"
    show sayori e3c b2b ldown mj
    "Sayori, not being used to carrying a bag filled with decorations, pretends to have befallen some sort of weakness."
    m lpoint md "Alright... But, there's still some decoration to go."
    show monika mc
    "As I stare at my bag, and Monika's bag..."
    show monika ldown
    mc turned casual nb ml "W- Wait, Monika, how many decorations are we planning to have?"
    m rhip ed mb "Enough to cover the whole school, of course!"
    show monika ma
    show sayori me b2a e1b 
    mc bd eb mf "Wha-"
    show sayori b2b md e1a
    m mb rdown "Just kidding~"
    m ea md "Although, we do need to decorate the outside of our classroom too."
    m bb ed mb "So, sorry if this seems a bit overboard."
    show monika ma
    s na e3c mh lup rup "Tell that to my arms!"
    show sayori mj
    m bb md ea "Oh, I am sorry, Sayori's arms~"
    show monika ed ma ba at t11
    show sayori rdown e2a b1d md at thide
    hide sayori
    "Monika and I giggle slightly, with Sayori pouting behind us, before we all sit on another nearby bench."
    show monika ea mc
    mc mg na ea ba "Say... Monika, how come you sent the text for us to go to the mall together so late?"
    m rhip md "Late?"
    show monika mc
    mc ef ml "I mean, I was uh..."
    mc eh bg teehee "Still sleeping, and if I didn't wake up at 1 pm I probably wouldn't have seen it in time."
    m bb rdown md "Oh my, what made you so tired?"
    show monika mc
    mc ef mf ba "Um..."
    _mc bi mh "Do I tell her about Yuri...?"
    show monika ba
    mc ea ba ml "Work."
    mc bg eg mg "Yeah, yesterday was a tiring day at work."
    m ec md "That's understandable."
    show monika mc ea at t21
    show sayori turned casual mh at t22
    s e1d b1d mb "What made it tiring, Melly?~"
    s b1a e1a mh "Annoying customers?"
    s e1d b1d mg "Or!"
    show sayori lup rup mi e1b b1a nb
    "She gasps audibly."
    s ldown rdown b2b e1a ml "The ice cream machine broke!"
    show sayori mj
    mc ec bi mh "..."
    show sayori b1a na md
    mc ea ba mg "Sayori, we don't have an ice cream machine."
    s lup b2b e2a mb "It was worth a try..."
    show sayori ma
    "I sigh."
    "Then... I remember what the boss said to me."

    show white_flashback onlayer above_master
    show bg cafe_kitchen_day onlayer above_master
    show boss turned noapron noblink at i11 onlayer above_master
    with Dissolve(0.25)
    $ autofocus.block("boss")
    $ say_transition = True
    b mb "However much yer try, there's just so much yer don't know yet."
    b eb "So much you won't ever know."
    b me ea bb "And there's only one solution for that:"
    show boss ec md with Dissolve(0.2) 
    pause 0.15
    b me ea "Getting closer."
    b mb ba "Getting to know them better."
    b ed mc "Spend time with them."
    $ renpy.scene("above_master")
    show sayori ldown
    with Dissolve(0.25)
    $ autofocus.unblock("boss")
    $ say_transition = False
    _mc ec mh "Getting closer..."

    stop music fadeout 3.0

    show sayori e1a b1a md
    mc ea ml "Monika, Sayori?"
    show monika md
    show sayori mg lup
    $ autofocus.force_focus("monika")
    $ autofocus.force_focus("sayori")
    "M & S" "Yeah?"
    $ autofocus.restore_focus("monika")
    $ autofocus.restore_focus("sayori")
    show sayori md
    show monika mc
    mc mg bg "Can I ask you two... What really happened last Friday?"
    show sayori ldown
    mc ba ml "With Yuri and Natsuki?"
    $ autofocus.block("monika")
    m "..."
    "Monika darts her eyes left and right."
    $ autofocus.unblock("monika")
    m rhip bc ec md "She was just stressed, that's all."
    show monika mc

    play music pensive

    s e2a mg "Yuri hasn't had it easy lately."
    show monika ea ba
    s e1a mh "We don't know why, but..."
    show sayori md
    m bc md rdown "Sayori..."
    show monika mc
    s b1d mh "Melody is one of us now, she is allowed to know."
    show sayori mj
    mc mf bd "Huh?"
    show monika eb ba
    s lup b1a mh "Whatever is happening with Yuri, she doesn't want to talk about it with us."
    s e2a mg "But..."
    s e1a mb "You seem to be getting close to her, right?"
    show sayori ma
    mc ec bi "Um..."
    s mb b2c "If you can, support her."
    show sayori ma
    _mc mh eb bb "The same thing boss said!"
    s lup mb "She needs someone to rely on."
    show monika ea
    s b2b e2a mh "I mean, she's never been good with change..."
    show monika bc
    show sayori ldown b1a me
    "Sayori opens her mouth once more, but before anything comes out, Monika rushes into the conversation like her life is at stake."
    show sayori md
    m md "But,"
    show monika rhip ec 
    extend " don't do things blindly."
    show monika mc
    mc bd ea mf "Monika? What do you mean?"
    m rdown ea md "You took her out of the clubroom a few days ago."
    show monika mc
    _mc eb bg mh "!!"
    m ba lpoint md "But failed to inform us."
    m mb "Usually, I don't mind but..."
    m ldown eb md "Natsuki does."
    show sayori e2a
    m ea bc "And Natsuki is {i}not{/i} afraid to confront people."
    _mc eg bi mm "Ugh... I knew it was a bad idea."
    _mc ec mh "..."
    _mc ef "So that's why..."
    _mc eg "She was angry at me."
    show monika mc
    show sayori e1a
    with None
    $ renpy.scene("above_master")
    with NonBlockingDissolve(0.5)
    mc ef bg ml "I... I'm sorry."
    m eb ba md "Don't feel bad, just..."
    m ea bb mb "Please keep us in the loop whenever you try to do things that might concern the Literature Club."
    show monika ma ba
    mc eg mf "I understand..."
    show monika ba
    m eb bc md "And, when you can..."
    m ea mb ba "Apologize to Natsuki. She'll appreciate it."
    show monika ma
    "Monika gives me a smile."
    show black:
        alpha 0.5
    show sayori e1a
    with NonBlockingDissolve(0.5)
    _mc ec mh ba "I don't really like Natsuki."
    _mc ef "I understand I've angered her..."
    _mc eg bi "She just always seemed angry in my eyes."
    _mc ea bd "At me, at everyone."
    _mc bb thinking "And Monika?"
    _mc ef ba "She's clearly concerned about Yuri. but-"
    _mc bi "Her reluctancy to talk about her..."
    _mc ec "Is she hiding something from me?"
    "..."
    hide black with NonBlockingDissolve(0.5)
    _mc ldown eg "No, I shouldn't think badly of Monika like that."
    _mc ec ba "I am sure she has her reasons."
    show sayori b1a
    m ba md lpoint "Now, how about we continue on?"
    m ed mb "There's much still to buy~!"
    show monika ma
    s lup rup mn e3d "Okay!"
    mc ea mb "Let's go."
    
    scene black with Dissolve(0.5)
    $ advance_date(minutes=12)

    "The day continues, and as we buy everything reading related..."
    "I can't help but find it fun."
    _mc turned casual mh "I don't think I've ever been this close to people my age."
    _mc ef ma "With the exception of Sayori, of course..."
    _mc eg "But that was a lifetime ago."
    s turned casual e1d b1d mh "Hey! Melly!"
    s e1a b1a mb "Stop daydreaming!"
    mc ed md "Okay~ Okay~"
    "With a smile, we continue on."
    
    stop music fadeout 2.0
    scene bg mall_int_1_night
    show monika turned casual at i21
    show sayori turned casual at i22
    with Dissolve(1.5)
    $ advance_date(minutes=30)
    play ambient int_night fadein 1.0

    "Holding heavy bags full with supplies, the day slowly comes to an end."
    mc turned casual mb nb "That was fun, thank you both~"
    m mb "Likewise!"
    m rhip md "Now, will we see each-other again tomorrow?"
    show monika ma
    mc eh md bb na "Of course!"
    s e3d mn "Yep!~"
    show sayori e1a ma
    m rdown md "Oh, and... if you two don't mind?"
    show monika mc at dip
    show sayori md
    m md "Could you take the supplies home with you, and then bring it to the club tomorrow?"
    m mb bb eb "Holding that many bags is kind of difficult for one person, aha~"
    show monika ma
    mc mb ba ea "Will do!" 
    s mg e1b lup "Oh my, seems like Monika has to go to the gym."
    show sayori me
    m ea bc mb "You're the one who was feeling weak just a while ago~"
    show monika ma
    s ldown b2c xd mk "Mmm..."
    show sayori md
    m mb ba "Enjoy your evening, you two!"
    show monika ma at thide
    hide monika
    show sayori b1a ma e1a lup at t11
    "We wave at Monika as she heads on home."
    show sayori ldown
    mc mg ef "Well, seems like it's time for me to go too-"
    s mg "Before you go..."
    show sayori me with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show sayori lup ma b2a
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("sayori")
    "Sayori taps me on my shoulder."
    s mh "Don't feel bad about Yuri, okay?"
    s b1a mb "Spend time with her."
    s mh "And, we'll be by your side to help if you need it."
    s mb "Okay?"
    s mg e2a "I gotta go this way and grab something extra, so..."
    extend mb e1a " Toodles~"
    show sayori ma with say_dissolve
    mc eg mb "Thanks Sayori. I won't forget it."
    mc ea "See you tomorrow, okay?"
    s e3d mn "Byee~!"
    hide sayori
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("sayori")
    "We both head on home, using all our strength to drag the bags home."
    
    scene bg mc_house_entrance_night with wipeleft_scene
    $ advance_date(minutes=32)

    mc turned casual eg mj bi "Phew.. Finally."
    "As I shut the door behind me, I put the bags near the door so as to not damage or forget them tomorrow."
    _mc ec ba ma "Tomorrow will be quite the day."
    _mc ea "Seeing Yuri again and all..."
    _mc mh ef "And the menacing Natsuki..."
    _mc eg bi ma "Correction: menacing {b}protective{/b} Natsuki, I guess."
    _mc ec ba mh "I hope everything will go fine."
    _mc ef "Well, I have some alone time now."
    _mc ea ma "Time to relax."

    stop ambient fadeout 3.0
    scene bg mc_bedroom_night_closed_off with wipeleft
    $ set_date(hour=20, minute=26)

    "I cooked up some dinner for myself and watched some TV, and now..."
    _mc turned naked nostrands messy eg "Well, now is about time I fall asleep."
    
    scene black with Dissolve(1.5)
    pause 2.0
    $ phone_available = False
    $ advance_date(minutes=10)
    show bg mc_bedroom_night_closed_off
    hide black

    window auto show None
    play ambient add_playback_info(audio.int_night, 3.0)
    _mc turned naked nostrands messy bi ec mh "I said, now is time I fall-"
    play sound phone_notification
    phone register "lit_club":
        time auto True
        "s" "Who wants a sleepover at my place?!"
    pause 0.3
    _mc ba mf ea "Huh?"
    _mc ec bi mh "Is someone messaging me? At this hour?"
    phone discussion "lit_club":
        "m" "Oh? That sounds like fun. When would it be? I would need to get permission."
        "s" "Hmmm"
        "s" "What about Saturday?"
        "n" "I think I should be able to do that."
        "y" "Oh? A sleepover? Whatever for?"
        "s" "Because we can, silly~"
        "y" "Just for fun? I don't see why not, then."
    _mc mh ba ea thinking "A sleepover? Sayori sounds pretty excited about it."
    _mc ldown "I suppose I'm up for it, though it would pose a conflict with my work schedule..."
    phone discussion:
        "mc" "I dunno, I've got work that afternoon."
        "mc" "I might be able to come by after work?"
        "s" "Sure! Let's make it a 5pm start then, at my place."
    _mc ma "That works."
    _mc mh "Let's see what everyone else says."
    phone discussion:
        "m" "I believe I can organise that, but I'll let you know."
        "n" "Yeah, I think I can make that as well."
        "s" "Sweet! I'll see everyone there! Bring some snacks with you, and your stuff for sleeping. There's plenty of room!" # im stuff
        "mc" "Look at you, running away with the entire show. Geez, if you're gonna twist my arm, I'll be there."
        "s" "You're starting to sound like Natsuki!"
        "n" "I don't sound like that! Geez..."
        "m" "Alright, see everyone at club tomorrow! I look forward to this event!"
        "y" "Indeed."
    phone end discussion
    $ phone_available = True
    _mc ec ma "I guess the sleepover is a go then."
    _mc eg "I should probably get to sleep now though. I have those decorations to haul in the morning."

    $ add_calendar_description(calendar_descriptions["yuri"][4])
    
    call week_2_monday_yuri from _call_week_2_monday_yuri
    return