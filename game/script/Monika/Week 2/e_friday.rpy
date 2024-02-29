label week_2_friday_monika:
    call calendar_transition(hour=6, minute=57) from _call_calendar_transition_10
    scene bg mc_kitchen_day with dissolve_scene_full
    play music dollaort

    "After dragging myself out of bed, sporting one hell of a hangover, I find myself walking into the kitchen, where I’m greeted by a pink-haired, spritely form."
    show natsuki turned notail noband e1d b3a mb nc at t11
    n "Heeey~ How’d you sleep?"
    n cross b1d e3c mg nb "Ugh, no, I can’t keep doing that."
    n e2a b3a mh na "Here, I made you a coffee."
    show natsuki turned lhip e1a ma at dip
    "She hands me a mug, giving me a small grin."
    show natsuki ldown me
    mc turned messy nostrands ed md "So what, you don’t want to pretend to date me?"
    n e3c mi "Nah, more trouble than it’s worth. Besides, you don’t want her to think we’re dating; you want her to notice you. If we started dating, that would..."
    show natsuki e1b md nc
    "Her face flushes crimson."
    n cross e2a mg b1a "That would..."
    n nb e2c mh "I, ah, gotta... can I use your shower?"
    show natsuki md
    mc ea mg "Yeah, sure. Take your time."
    n e2a mg b1d "Th- Thanks, yeah, I will!"
    show natsuki turned md e2c at rhide
    hide natsuki
    "She rushes past me, and out of the kitchen."
    _mc ec mh "She’s a little bit all over the place, isn’t she?"
    _mc ef ma "Ah well. Makes her unique, I suppose."
    
    scene bg school_street_day
    show natsuki turned b3a at i11
    with wipeleft_scene
    $ set_internet(False)
    $ set_date(minute=5, hour=8)

    "After leaving the house separately, we rejoin on the walk to school."
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    n mg "So, did you sleep well?"
    show natsuki e3d ma with say_dissolve
    mc turned mj eg bi "Yeah, I did, actually. Shame I had to wake up."
    n e1d b1d mb lhip rhip "Hah, the hangover got you good, eh?"
    show natsuki ma with say_dissolve
    mc ef mb ba "You could say that..."
    show natsuki e1a b1a me with say_dissolve
    mc ea mg "How about you? You spent forever in the shower. Were you massaging your head? I know that helps sometimes."
    n cross b1d e2a mc nb "Y- Yeah, that’s, ah, totally what I was doing!"
    show natsuki ma with say_dissolve
    _mc ec mh "I’m not entirely convinced. Hell, Part of me has an inkling, but I sure as hell am not going to bring it up, in case I’m wrong. Besides, wouldn’t it be weird doing that in someone else’s house?"
    show natsuki me e1a b1a with say_dissolve
    mc eg ma ba "Mhm."
    n mh b1d e1b "Seriously! The hangover hit me, and I just had to like... y’know..."
    show natsuki md e1a b1d na with say_dissolve
    mc ea mg "Yeah, I know. Though, I can’t really say I’ve been drunk too often, actually. I think that was the most I’ve ever had."
    n turned mg b3a "Really?"
    show natsuki md with say_dissolve
    mc ml ec "What, do you drink that much regularly?"
    n e2a nb mb b1a "W- Well, no, not regularly, that’d be... a little crazy..."
    show natsuki ma with say_dissolve
    "I click my tongue. I suppose I should change the topic; she seems to be a little uncomfortable whenever anyone pries into her home life."
    show natsuki e1a md na with say_dissolve
    mc ea mg "Soo... What’s your favourite manga?"
    n lhip rhip e1d b1d mh "... You were gonna fake date me, and you don’t even know that?"
    show natsuki md with say_dissolve
    mc ec ml thinking "Now, I never agreed to anything, you’re making a lot of assumptions here. Besides, how am I supposed to know if I don’t ask?"
    n cross e2a b3a mh "True. Parfait Girls. I thought you would have at least known that."
    show natsuki me e1a with say_dissolve
    mc ea mg "Hm. Never heard of it. What’s it about?"
    n turned ldown rdown mc "Oh? Well, you’re in for a treat! Oh, man, this series is great! First off, have you heard of 'slice of life'? It’s like that, but soooo much better!"
    show natsuki e3d mo b3a with say_dissolve
    "She continues to rave about this series for the rest of the walk to school."
    show natsuki b1a mc e1a with say_dissolve
    _mc ec ma "I have to say, I’m actually a little interested, after hearing her talk about it so happily. Maybe I’ll sit down and read it with her at the club today."
    
    stop music fadeout 2.0
    scene bg school_corridor_1_day
    camera master
    with longfade
    show monika turned eb mc at t11
    $ set_date(hour=15, minute=25)
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    play music daijoubu

    "As I make my way to the clubroom after school, I spy Monika in the hallway."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "Smiling, I make my way over to her. Even if she’s not interested in me, even if she knows, I still... want us to be friends."
    mc turned mb "Hey, Monika."
    show monika md ea nb  with say_dissolve
    "She practically jumps as she turns to face me."
    m mb bb eb "O- Oh, Melody! I didn’t see you there!"
    show monika ma with say_dissolve
    mc ml "M- Melody?"
    m md ea "Oh, shoot, I’m sorry, MC! I swear it was an accident!"
    show monika mc with say_dissolve
    mc ef mb bf nb "N- No, it’s... it’s okay, I just..."
    show monika na ma with say_dissolve
    mc ml bg na "It still sounds a little weird to hear, coming from someone else."
    m lpoint md ba "True. You’ve gone by MC for about as long as I’ve known you."
    show monika ma with say_dissolve
    mc thinking ec ml ba "About two years, now, I think? It..."
    show monika ldown mc with say_dissolve
    mc ea mg "I dunno. Sometimes, it sounds weird. Part of me wonders if I shouldn’t have just changed my name. It was almost Tohka, actually."
    m md "Tohka? That’s not a name-"
    show monika mc with say_dissolve
    mc ldown mb ef "... It’s a reference, don’t worry."
    _mc ma "Of course she wouldn’t get it."
    m rhip mb "Wait... Date A Live? I {i}do{/i} know that one! I’ve heard of it, at least."
    show monika ma with say_dissolve
    mc eb bb mg nb "Wait, what? You’ve seen an anime?"
    m eb md rdown "Well, no, but a couple of my friends are pretty into it, so I hear about it from them."
    show monika ma ea with say_dissolve
    mc ef mf bi na "Dang. You almost had me there..."
    m bb ed mb "Aha, sorry to disappoint..."
    m lpoint ba ea md "So, why Tohka in particular?"
    show monika ldown mc with say_dissolve
    mc ea mg ba "Well, she’s a free spirit -hah, spirit- who does what she wants, and really enjoys food and her friends."
    show monika bb with say_dissolve
    mc ef mb "I guess I just wanted to be more like her."
    m eb md "Oh, MC, that’s..."
    show monika ea ma with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She sighs, placing a hand on my shoulder."
    $ autofocus.unblock("monika")
    m mb "I wish there was something I could do to help."
    show monika ma
    mc "... Honestly, you are. Just having you around, having the club around, it means so much to me. It’s making me a stronger, more sociable person, just being around you."
    mc ea bg "I can’t tell you how much the little community you’ve created has come to mean to me, in such a short time. I’ve never connected with people quite like I have at the club, save for Sayori, who I already knew."
    m ba md "Don’t you have friends outside the club?"
    show monika ma
    mc ml ef ba "Well, I have Amelia, sure, but she’s so busy with her work that I..."
    show black with NonBlockingDissolve(0.2):
        alpha 0.75
    _mc ec mh "A bald-faced lie. I know I could spend more time with Amelia if I wanted. It’s not that I don’t want to, but more that I..."
    _mc ea "I guess I feel a little guilty. A couple weeks ago, I was more than happy being alone for as much time as possible. Now... suddenly I feel like I’m betraying her, and all her hard work to try to get me to open up."
    _mc ef "... And now, I’m spending almost less time with her than I usually do. We’ve only hung out, what, twice this week over lunch breaks?"
    _mc bi "What an awful friend I’ve been."
    show monika mc
    mc ea mg ba "Hey, actually, sorry to do this to you, but... is there any chance I could skip out on the club today?"
    m lpoint md "But the festival is-"
    show monika mc
    hide black
    with NonBlockingDissolve(0.2)
    mc mb "Next Monday, I know, but... tell you what, I’ll give you my entire Sunday after Sayori’s sleepover to help with whatever is left, okay?"
    m ldown ec md "... Alright, I’ll hold you to that."
    show monika mc ea
    mc eh md nb bg "Please do. I’m really sorry, but- there’s someone who I need to apologise to."
    show monika mc at thide
    hide monika
    "She nods, and I race off to find Amelia."
    _mc ec ba na mh "Hopefully she hasn’t left yet..."
    
    scene bg school_gate_day with wipeleft
    if preferences.language is None:
        $ auto_advance_date_mult = 0.727
    $ advance_date(minutes=3)

    _mc turned nb mf "There she is!"
    show amelia turned eb md at t11
    mc mg bb "Amelia!"
    am me "Hm? Melody?"
    show amelia md
    mc "Do you want to hang out this afternoon?"
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True 
    "As I finally catch up to her, I pause to catch my breath."
    am ec bg me "Huh? Where did that come from?"
    show amelia md ba ea with say_dissolve
    mc eg bg mg "Well... I realised I haven’t exactly been a good friend. Not for a while, now."
    am ed me bh "{size=15}Oh, so now you realise...{/size}"
    show amelia mc with say_dissolve
    mc eh bf md "Huh? I didn’t catch that, sorry, breathing is hard-"
    am ef mb bd "No, nothing. I, ah, don’t really have the time tonight. I want to start streaming a new game that’s just released."
    show amelia ma with say_dissolve
    mc ef ml bg "... I see..."
    am eb ba me "B- But, we can hang out tomorrow, after you finish work, if you want?"
    show amelia ba md with say_dissolve
    mc ea mg na ba  "Actually, I’ve been invited to a sleepover with the club..."
    am bg me ec "A sleepover...? Just how close are you all?"
    am eb ba mi "Ah, nevermind, it’s not- I’m not- Ah, forget it!"
    am ed me lup "Sunday?"
    show amelia md eb with say_dissolve
    mc ef ml "... I just promised Sunday to help out Monika with festival preparations."
    am ldown ed bd me "Oh... and I won’t have time next week, I’m streaming all week; doing a marathon."
    show amelia md with say_dissolve
    mc ea mb bg "... Sorry, Amelia..."
    am be me ee "No, it’s not your fault, I just... I wish I was more available, time-wise."
    show amelia eb bd md with say_dissolve
    mc eg "And I wish I was more available, emotional-wise..."
    show amelia ma with say_dissolve
    "She grabs my hand with both of hers, biting her lip."
    am mb "Hey, it’s not easy. You’ve no idea how happy it makes me just seeing you acknowledge it."
    show amelia ma with say_dissolve
    mc ba mf "You think?"
    am bb eb mb "I know. You’ve really opened up since joining this club; it’s doing wonders for you."
    show amelia ba ea ma rup with say_dissolve
    "She brings a hand to my head and slightly ruffles my hair. I hate it when anyone else does it, but with Amelia... I suppose I can tolerate it."
    am mb "Go to your club meeting, alright? If I don’t hear from you sooner, I’ll talk to you in a week or so, ’kay?"
    show amelia ma with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    mc mb "... Yeah. Have fun, Amelia. And if you want a guest appearance...?"
    $ autofocus.unblock("amelia")
    am ef bb mb rdown "Now you’re talking my language~ There’s a chance, at least! See ya!"
    show amelia ma at lhide
    hide amelia
    "With that, she bolts off."
    _mc ec ma"... I feel a little better, knowing that there aren’t hard feelings, but..."
    _mc mh "Still. I wish there was more I could do."
    _mc ea ma "... Best to re-join the club and help out there."

    stop music fadeout 2.0
    scene bg club_day
    show yuri turned b1d e2a md at i43
    show natsuki cross e2a b1d md at i44
    show monika turned mc at i42
    show sayori turned lup rup xd ml at i41
    with longfade
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    $ advance_date(minutes=2)
    play music playwme

    "I make my way inside, to see everyone working on some kind of curtain."
    show yuri at thide
    show sayori at thide
    show natsuki at thide
    hide natsuki
    hide sayori
    hide yuri
    show monika rhip md at t11
    m "MC? I wasn’t expecting to see you again. You said you had something to do?"
    show monika ma
    mc turned mg nb "Y- Yeah, I finished early."
    m mb rdown "Oh, that’s wonderful news for us, at least. Do you mind helping us hang this curtain?"
    m nb eb "Sayori and I aren’t quite tall enough to reach the hook..."
    show monika ma ed at thide
    mc mb na "Sure, Monika. Pass it here."
    hide monika 
    show yuri turned at t11 
    "I walk over and reach up, reasonably easily reaching the hook, with Yuri on the other end."
    show yuri at thide
    hide yuri
    show sayori turned lup rup me b1d nb e1b at t21
    show monika turned at t22
    "Sayori and Monika support it from the middle, until we can hook that in, too."
    show sayori at thide
    hide sayori
    show monika at thide
    hide monika
    show natsuki cross mm b1d e2a nb at t11
    "Natsuki... Well, she’s moral support."
    show natsuki at thide
    _mc thinking ec mh "Despite being the oldest one here, she’s... 'Not quite the tallest', is how I choose to put it. Best not to stoke the wrath of the cupcake."
    _mc ea "In contrast too, to how she came across last night, there’s definitely something there that I’d... rather not get on the wrong side of."
    hide natsuki
    show monika turned lpoint md at t11
    m "So, MC, how was your night?"
    show monika ldown mc
    mc ldown mg "Oh, mine? It was good! I just chilled, had a few drinks, it was nice."
    show sayori turned mg at t21
    show monika at t22
    s "You were drinking alone?"
    show sayori md
    mc ml nb "What? Of course not, I was with-"
    _mc mh eb bb nb "Shit."
    _mc mf ba "Monika, how could you?"
    show yuri turned lup b2b mk e2b at t33
    show monika at t32
    show sayori at t31
    y "Y- You were with someone, drinking? O-Oh..."
    show yuri shy nb eb bc md
    mc ef ml nc "N- No, it’s not what it- I, ah, it wasn’t really anything, just-"
    show yuri ea na bb mb at t43
    show sayori at t41
    show monika at t42
    show natsuki turned e1d b1d lhip rhip mi at t44
    n "Oh, for God’s sake, it was me. {i}I{/i} was with her last night, because I got trapped too far from home and didn’t want to walk that far so late, so she offered me a spare bed."
    n cross e2a nb mm "No need to make such a big deal over it."
    show natsuki e1d mj:
        xoffset -50
    camera master:
        align (1.0, 0.25) zoom 1.5 
    show bg:
        blur 2.0
    show yuri:
        alpha 0.0
    show monika:
        alpha 0.0
    with Dissolve(0.2)
    "She shoots me a glare. I’m in for it, later."
    show bg:
        blur 0.0
    show yuri: 
        alpha 1.0
    show monika:
        alpha 1.0
    camera master
    show natsuki:
        xoffset 0
    with Dissolve(0.2) 
    s lup mh "Oh, you visited? Why didn’t you tell me? We could have had a proper sleepover!"
    show sayori md
    mc ea na ba mb "Because we still have one tomorrow, remember? Save all the cool tricks and games you have planned for when everyone is there, I think."
    show natsuki e1a b1a md na
    s mg e2a b2b "... You still could have..."
    show sayori md ldown
    show yuri ba ma
    mc bg "Yeah I know, Sayori. I’m sorry."
    n turned lhip e2a mh "Yeah. It wasn’t anything planned, and by the time it happened, it was too late to reach out."
    show natsuki e1a md
    show sayori me b1a e1a
    y turned lup e1d b1a mh nc "S- So, you two... did you, well-"
    show yuri b2a e1b nd mk 
    n cross e1d b4 mb "What are you implying?"
    show natsuki ma b1d
    y shy ec md bb "N- No! I was going to ask if you two had a nice time! W- Wait, not like that, more that I-"
    show yuri ma ea
    show sayori ma
    mc mg ba "Yes, we did, Yuri, thanks for asking. We just ended up chatting for a while after I finished work."
    show natsuki b3a e3d
    y ne md "Uuuuu..."
    show yuri mb
    _mc eg ma "Ah, Yuri. If you trust anyone to accidentally say an innuendo without realising, then realise what she said before anyone else does, it’d be her."
    show yuri ea nb ma
    show natsuki e1a b1a md
    show sayori md
    m bc ec md "I see..."
    show monika mc
    _mc ec mh "I want to comment, but... I know what’s wrong, and probably have a good idea of what’s going through her head."
    _mc ef "Best to keep it to myself."
    show monika ea ba
    s rup mg "What’s wrong, Monika?"
    show sayori md
    _mc bi "Dammit."
    m md "Hm? Oh, me? Nothing, I’m just..."
    show sayori b2c rdown ma at lhide
    show yuri at thide
    m bb nb ed mb "Feeling a little faint."
    show monika ma at t21
    hide yuri
    hide sayori
    show natsuki turned ma at t22
    "Sayori moves to get her a chair, but before she can get half-way, Natsuki’s already grabbed one."
    show monika ea at thide
    n e3c mb "Here, Monika. Sit down; let’s take five."
    show natsuki ma at thide
    hide monika
    hide natsuki
    show yuri turned lup e2a mb b1d at t11
    y "O- Oh, I’ll make everyone some tea."
    show yuri ma at thide
    hide yuri
    show monika turned ec md bb at t11
    m ec md "Thank you, everyone."
    show monika ma at t22
    show sayori turned lup rup mb e3d at t21
    s "Of course, Monika, you sit down, and the rest of us will keep working. You can give us directions, if you want!"
    show sayori ma
    show monika ba ed na
    "The warm smile on Monika’s face says it all. She’s overjoyed with her little community here; even if it does happen to contain me."
    
    scene bg club_afternoon
    show monika turned eb bc mc:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with fade
    $ set_date(hour=17, minute=2)
    $ autofocus.block("monika")
    
    "After we finish, the others head home. Monika asked me to stay back a little while she finishes off some of her admin work."
    "So, here she is, toiling away at the wad of papers in front of her, while I sit down with a book."
    m md "Hmm..."
    show monika mc
    mc turned mh "Hm?"
    m ec md "Hmm..."
    show monika mc
    mc eg bi "Hm."
    m eb rhip "Hmm..."
    mc ec ba "Mm, hm."
    m ba ea md "Hmm...?"
    $ autofocus.unblock("monika")
    m rdown mb "Sorry, MC, did you say something?"
    show monika mc
    mc ea mg "No, just commenting on how you mumble when you’re focused."
    m md "Oh, do I? I never noticed."
    show monika mc
    mc mb "Yeah. It’s not very loud though, so I wouldn’t worry too much about it."
    m bb mb eb nb "Ah..."
    show monika ma
    stop music fadeout 4.0
    "She awkwardly shuffles on her seat."
    mc mg "So... What did you need me for?"
    m na ec md bc "I... feel like there’s something I need to say."
    show monika ea mc at dip
    "She collects the papers, tapping them on the desk to align them, before setting them down and walking over to me."
    "I put the book back in my bag, leaving a bookmark for my page."
    mc ml "Sure."
    show monika ec md at dip
    "Monika sighs softly, as if unsure what to say."    
    m eb bb md rhip "Are we... good?"
    show monika mc
    mc mf "What do you mean?"
    m ea mb rdown "I mean, after the last few days, I feel like a lot has happened between us, and the club."
    m md ec "I wanted to make sure that you’re okay, and that our friendship hasn’t been compromised."
    show monika ea mc
    mc ef ml "I mean, I knew what you meant, it was more that I..."
    m md bc "Wanted to avoid the topic, yes."
    m lpoint ba "But if we ignore it, will it not get worse?"
    show monika mc
    mc mh "..."
    "I click my tongue."
    show monika ma ldown
    mc eg bi mf "Probably."
    m eb md "So, all I wanted to say was that I..."
    m bb mb "I’m sorry. I hope that after everything, we can still be friends, and that you still want to be a part of the club."
    m ec "You’ve no idea how much of a difference you’ve made, and how lively this place is when you’re around! It makes it feel like a true home for all of us. I can’t begin to put to words just how-"
    show monika nb mc ea
    mc ba mb "Monika, please."
    mc ef bg "I know. I know."
    mc ml "But I..."
    m eb md na "... You aren’t planning on sticking around?"
    show monika mc
    mc mf "... I..."

    show sky_afternoon at moving_sky zorder 5
    hide monika
    with Dissolve(1.0)
    play music myconfession

    "Looking away from her, I find my gaze drifting out toward the evening sun."
    m turned eb md "I understand. For what it’s worth, MC, you..."
    m ea bb mb "You really did make a difference, here."
    m ec "Both to the club, and to me."
    m ea md "I’m sorry, I really am, that I can’t return your feelings, but I promise that I-"
    mc eg bf nb mb "Please, just- It makes it worse."
    "She stops, keeping her distance from me."
    mc ef ba na mg "I won’t tell you some sob story, or crap about why I think I should be the one. I won’t - Because it’s not true. I knew from the beginning that it was a fabrication, one I’d created for myself."
    mc eg mb "You could never love me; I understand that, now."
    mc bg mj "But even so, I couldn’t just... do nothing. I- I don’t know why I feel this way. It just seems like every time I see you, or hear your voice, I fall deeper and harder. It’s... it’s not fair."
    mc bf ef ml "I know you won’t like me because I’m strange, because I’m antisocial, because I’m so imperfect."
    mc bg mg "I’m sorry, I am, but it’s not like I chose to be this way. I want to be better, and I’m trying to be, but it takes time, and I don’t know if I’ll ever be good enough-"
    mc ml "But even if I’m not, I- I don’t want to hold you, or your club, back."
    mc ea bf  mb "I don’t want to do that to you."
    mc eg bg "I respect you too much - And that’s why I never told you how I felt because if I did, all it would do is make you..."
    "I finally look back toward her, my raving coming to a halt."
    
    hide sky_afternoon
    camera master:
        align (0.5, 0.2) zoom 1.5
    show monika ea ba mc:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    show bg:
        blur 2.0
    with Dissolve(0.7)
    $ autofocus.block("monika")
    $ say_transition = True

    mc ea mg "... Look at me differently."
    m md bb "Oh, MC, I could never-"
    show monika mc ba with say_dissolve
    mc ef bi mf "... Melody."
    mc ea mg ba "Please, call me Melody."
    "My jaw twitches as I say it, but there isn't a shred of doubt in my mind now."
    _mc eg mh "Venting has made it abundantly clear to me now - If I want to start moving forward, I need to stop running backwards."
    _mc ec "From this; from my family; from everything."
    m ec md "Alright, Melody. I... I want you to know that I’ll never look at you, or think of you, differently because of how you feel. And it’s nothing to do with you, it truly isn’t."
    m eb mb nb "Maybe there are things you can improve, and I want to support you while you do just that, but I can’t... I can’t do that as a partner."
    m ec md "It’s not about you, or me, or anything like that. I have a great deal of respect for you, Melody. That’s why I invited you to join this club."
    m ea ba rhip na "But I don’t think either of us are ready for any sort of relationship, do you?"
    show monika mc with say_dissolve
    mc ef "..."
    m rdown mb bb "You’re a wonderful person, Melody. I promise you that."
    show monika ma with say_dissolve
    mc bg mf "... I see."
    show monika mc with say_dissolve
    mc bf ea mb "But I’m not worthy, right?"
    m eb md "... It’s not that, either. I don’t think we would work out, if we tried now. We’re too different of people."
    m ea mb "Similar interests are not all it takes to make a relationship work, you know that. We need to work together as a team; trust each other. And we don’t have that kind of trust yet."
    show monika mc with say_dissolve
    mc bg ml nb ef "... So there’s a chance?"
    show monika eb with say_dissolve
    "She looks away. I know I’m being desperate, that I’m being clingy, but I need to know."
    mc bg eg mb na "If there isn’t, just say so. Please, just tell me now, so that I can wash it from my mind."
    m bc ec md "... No. There’s no chance."
    m mb ea bb nb "I’m... I’m sorry, Melody, I truly, sincerely am."
    m na ec md "But I don’t see us working out."
    show monika mc with say_dissolve
    "..."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "I slump back into my chair, defeated."
    $ autofocus.unblock("monika")
    m mb ea "But... and I know this is cruel, God help me, is it ever so, but if you’d take me as a friend? I would be honoured."
    show monika ma
    mc ec bg mh "..."
    mc eg mf "I..."
    mc ba mg "Let’s... talk about it after the festival. We should get through that, first."
    m md ba "... So, where do we stand, now?"
    show monika mc
    "..."
    "My jaw quivers."
    _mc ea bg mh "I know I should be putting distance between us. I know that’s how to move on."
    _mc ef "... But I can’t."
    mc ea mb "For now... Act as before? Friends?"
    $ autofocus.block("monika")
    m ma nb bb "..."
    "Tears start to well in her eyes."
    $ autofocus.unblock("monika")
    m mb ec "Oh, I don’t deserve you, Melody..."
    show monika ma at dip
    "She takes my hand, tentatively at first, trying to scope out how close she’s allowed to be."
    show monika ea ba md
    camera master:
        align (0.5, 0.2) zoom 1.6
    show bg:
        blur 2.3
    with Dissolve(0.2)
    "I shake my head, just a little, and pull her into a hug."
    show monika bb ec ma with say_dissolve
    mc eg "No. It’s me, who doesn’t deserve someone as caring and thoughtful as you."

    $ add_calendar_description(calendar_descriptions["monika"][8])

    call week_2_saturday_monika from _call_week_2_saturday_monika
    return