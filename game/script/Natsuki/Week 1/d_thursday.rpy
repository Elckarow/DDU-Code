label week_1_thursday_natsuki:
    call calendar_transition(day=26, hour=12, minute=0) from _call_calendar_transition_14
    scene bg class_1_day
    with dissolve_scene_full
    play sound school_bell
    play music ["<silence 0.3>", audio.playwme]

    _mc turned "Alright, there it is. Time to have lunch."
    _mc ef mh "Not that class wasn’t interesting, it wasn’t bad; just not quite as fun as I would have hoped, today."
    _mc ec "Revisiting trigonometry for the third time sure wears down on you. To be fair, it’s only in preparation for our next actual piece of work, which expands on the topic, so we should only have two or three lessons on it as revision."
    _mc ea ma "Still, I’m more than ready for lunch."
    _mc eh "Time to break it out. I made myself something nice, today, if I do say so myself-"
    show natsuki turned mh e1d b1d rhip at t11
    n "You. With me. Now."
    show natsuki mj at thide
    _mc ef pout bi "God. Dammit."
    hide natsuki

    stop ambient fadeout 1.0
    scene bg school_rooftop_day
    show natsuki turned mj e2a at i11
    with wipeleft
    $ advance_date(minutes=5)

    show natsuki e1a
    mc turned ed mj bm "... Why are we here?"
    n e1d b4 mh "Because it’s quiet? And free from prying eyes?"
    show natsuki mj b1d
    mc eg ba mg "Alright, how about I rephrase my question."
    show natsuki e1a b1a
    mc ea bd ml "Why am {i}I{/i} here?"
    n lhip e2a mh "Because I wanted company, and Sayori is busy today."
    show natsuki md
    mc ed bm mg "So... Why me? When I could be inside, in the warmth?"
    n mb e1a "Because you were stupid enough to follow me?"
    show natsuki ldown e1b nc mk with None
    hide natsuki
    camera master:
        align (0.4, 0.5) zoom 2.7
    with NonBlockingDissolve(0.3)
    mc eg bb mg "Alright, that’s it; I’m going back inside."
    n turned e1b b2a mh nb "N- No, w- wait, it was a joke-"
    "She grabs my sleeve, and when I turn back toward her,"
    show natsuki b2a md nc e2a at i11
    camera master
    with NonBlockingDissolve(0.3)
    extend " she’s pulling a face that I could only call 'positively adorable'."
    "It’s like when your pet knows they’ve done something wrong and is trying to make up for it by looking and acting as cute as possible."
    "... And it appears to be working."
    n e1a mh b2b "I... Please don’t leave."
    show natsuki md
    mc ef bi ml "... Give me one good reason why not."
    n mh "Because I’ll be lonely?"
    show natsuki md
    mc mf "I don’t see how that’s my-"
    show natsuki na b1a ma
    extend eg mg " Argh, fine, you win!"
    show natsuki e3d mo b1a at hop
    n "Yaay!"
    mc ef ml "I swear to god, copying Sayori’s mannerisms is cheating."
    n e1a mc "But it worked, did it not?"
    show natsuki b1c mg
    stop music fadeout 1.5
    mc ea ba mg "I will still leave."
    n b2a mh nc "N- No, please don’t!"

    play music myfeelings

    show natsuki mj
    _mc bi ec mh "I hate how she can do that."
    _mc ef "It’s almost uncanny how effortless it is for her. How long has she spent with the girl?"
    show natsuki na md b1a
    _mc bg "... Longer than I have, in a very long time."
    n b2b mh "Hey, what is it? You’ve gone all... cloudy."
    show natsuki mj
    mc mb eg "... It’s nothing, don’t worry about it."
    _mc ec ba mh "I can’t have myself getting emotional so easily. These past couple days have been a ride, but it’s nothing I can’t handle."
    _mc ea "It’ll do no-one good to crack already."
    n b1a mh "Was it Sayori?"
    show natsuki mj
    mc mf nb "What-"
    n e2a mb b3d nc "Because I imitated her? I thought it would be funny, not..."
    n cross e2a b2a mh "Not painful."
    show natsuki md
    mc mg "No, it’s fine, I just-"
    mc ef mb bg "I wasn’t ready for it."
    show natsuki e1a ma b2b
    "She gives me a small, half-smile."
    n e2a mb b2a "I know you two were close, but... She never really told me much about what happened."
    show natsuki ma
    mc na ba ml "It’s... not something I really want to be talking about."
    show natsuki turned na e3c b1a at dip
    "Natsuki nods, and returns to unpacking her food."
    show natsuki e1a
    mc ea mb ba "Oh hey, that’s cool. I have that exact pair of chopsticks at home."
    n mc "Oh? No way, that’s crazy."
    show natsuki ma e2a
    mc eh md "Yeah! I use them with dinner, more often than not. They were a gift from my grandmother; they mean a lot to me."
    n mb nc b3d "That sounds lovely, yeah..."
    show natsuki ma
    "She shuffles, a little awkwardly. Maybe she doesn’t have a good relationship with her family?"
    _mc ec mh ba "I’ll change the topic for her."
    mc ea mg "So, Natsuki, do you-"
    play sound heartbeat
    stop music fadeout 0.05
    n mh b1a e1a na "Do you like Sayori?"
    show natsuki mj
    mc mj eb bb nb "Wha- wait, what?"
    n lhip mi "I said, do you like Sayori?"
    show natsuki mj
    mc mg ba ea "Y- Yes? She’s a good friend?"
    n rhip e1d b1d mh "No, you know what I mean."
    show natsuki mj
    mc bd na "Look, Natsuki, I don’t know what you take me for, but I’ve reconnected with her for less than a day. There’s no way I would fall for someone that quickly-"
    n cross e2a b1a mg "... You’re right, that would be stupid. But you haven’t only known her for a day."
    n e1a b1d mh "You’ve both known each other for your entire lives."
    show natsuki b1a me
    mc ec bi ml "Maybe so, but that question was a little out of left field, would you not agree?"
    n turned e2a mg "... Even if it is."
    show natsuki md
    mc bd ea mg "What do you want from me? This is clearly the reason you brought me up here, so what, if you’re asking for my permission or something, it’s not mine to give-"
    mc ba mf "... No, you’re not..."
    mc ef bi ml "I see."
    _mc mh "She’s not asking permission at all."
    _mc ec "It’s a declaration of war."
    show natsuki e1a
    mc ba mg ea "... No. I don’t have feelings for Sayori."
    n b1d mh e2a "... I see."
    show natsuki md
    mc ml eg "Now, was that all? Because I would like to eat my dinner in peace."
    n e1b b3a mk nd "W- Wait, it’s- it’s not what you think, I swear."
    n b3d e2a mb "You’re thinking that, maybe I, but that’s not it. Sayori’s my best friend, and I don’t want just {i}anyone{/i} taking her."
    n cross nb b2a e1a mh "She’s... She means the world to me, and I don’t want someone who isn’t worthy of taking her."
    show natsuki mj
    mc thinking ea ml "So it was a test?"
    n turned e2a mh lhip b1a "... Maybe."
    show natsuki mj
    "Where I expect a joke, she instead looks away, clearly conflicted."
    _mc ec ma ldown "This girl wears her heart on her sleeve; so incredibly open and direct."
    _mc ea "It makes me wonder what the rest of her family must be like to have raised her like this."
    show natsuki ldown
    mc mb "Hey, look. Sayori’s pretty incredible, isn’t she? There’s a reason she was my best friend."
    mc ef "If she’s got someone like you protecting her, then..."
    mc ea mg "She’s in good hands, isn’t she?"
    show natsuki b2a e1a me
    "Natsuki looks toward me, her eyes filling with what I could only describe as an unimaginable relief."
    n b2b mh "You... You mean it? You’re not gonna fight for her to be your best friend again instead?"
    show natsuki b1a me na
    mc bd ml "W- Wait, that’s what this was about?"
    n b4 nb mg "Y- Yeah? What else would it have been-"
    show natsuki e1b b3a nc md
    "Her face flushes crimson, and she rapidly packs up her things."
    n b1d e2b mm "I- I- I didn’t say anything! This conversation didn’t happen, right?!"
    mc ed md ba na "Sure, sure. Whatever you say~"
    hide natsuki
    camera master:
        align (0.4, 0.5) zoom 2.7 
    with Dissolve(0.2)
    "After haphazardly grabbing what she can, she bolts away, having never touched her lunch."
    _mc ma ec "... What an incredibly high-strung young woman."

    scene bg club_afternoon
    camera master
    with longfade
    play music okev
    $ set_date(hour=16, minute=3)

    m turned mb "Alright everyone, let’s all gather together and share what we’ve been reading!"
    show yuri turned:
        matrixcolor TintMatrix("#f1d6bb")
        t41
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        t43
    show monika ma:
        matrixcolor TintMatrix("#f1d6bb")
        t42
    show natsuki turned:
        matrixcolor TintMatrix("#f1d6bb")
        t44
    "We oblige, making our way over to the front of the room. We’d been given copies of the same book, a book none of us have read, and been given a random chapter assigned to us."
    "Our goal is to combine what we’ve read to try and piece together the story."
    _mc turned mh "To be honest, the chapter I got was somewhat near the end, so it made it a little difficult to make sense of it all."
    _mc eg bi "Well, no, it made it almost impossible. Something about a boy running with a bunch of people while avoiding a bunch of monsters? Talk about confusing!"
    _mc ea ba "I’m sure everyone else had at least a little easier time with it. Let’s find out!"
    m rhip md "So, who would like to go first?"
    show monika mc
    y mb "Should we go in chapter order?"
    show monika rdown ma
    show yuri ma
    s e1b lup rup mh "Oooh, how about we go in reverse chapter order! Won’t that make it even harder to put together, and more fun to try?"
    show monika md
    show sayori rdown e1a b1a ma
    m mb lpoint "That sounds like a wonderful idea! So, who had the latest chapter?"
    show monika ldown ma
    mc thinking mf "That would be me, I think..."
    show sayori ldown
    m mb "Well, let’s hear it, then! Everyone take a seat, and listen along!"
    show monika ma
    show natsuki md
    mc ef ml "Well, if I had to start somewhere, I guess it would be... They were running."
    n mh "Who was running?"
    show natsuki md
    show sayori md
    mc ec mj ldown "Uh... The people."
    s lup mg "Which people?"
    show sayori me
    show monika md
    mc ea ml "Yes."
    show monika rhip ec bc mc
    show yuri e3c
    show natsuki e1d mj
    show sayori e3d ma at dip
    "Sayori chuckles, while Monika shakes her head a little."
    show natsuki e1a b1a ma
    show sayori e1a
    show yuri e1a
    m eb ba nb md "Maybe starting in reverse order was a bad idea..."
    show monika ea mc na rdown
    n mh "No no, I’m sure we can piece something together, so long as we don’t use what we know from our chapters to add to it until it comes time."
    show natsuki ma
    y lup mb "I agree, with our combined intellect, this should be straightforward."
    show yuri ma
    m eb mb "Alright... Please, continue, MC."
    show monika ea ma
    show natsuki md
    mc mg thinking "Well, they were running from a bunch of things called... grievers? It was really unclear what they were, some kind of spider?"
    show natsuki ma
    mc ml ec "And it was through a maze, I worked out that much. They eventually reached the end of the maze, though, I think? That was the end of the chapter."
    s rup e3d mc "Oh, they found the exit? Nice!"
    show sayori e1a ma
    y mb "Are you next, Sayori?"
    show yuri ma
    s rdown mh "Umm... I think so? Was anyone else moderately close to the end?"
    show sayori md
    n e2a mh "Nah, not me."
    show natsuki md e1a
    m md "I got quite close to the beginning, actually."
    show monika ma
    y mh e1d b1c "Mine was somewhere around the middle?"
    show yuri ma ldown b1a
    show sayori ma
    n mc "Alright, then go for it, Sayori."
    show natsuki ma
    show yuri e1a
    s mh "Right. Well, what I read was, there were these monsters attacking some kind of village, stabbing people and killing them, or dragging them off. They got a few people including someone who seemed important?"
    s lup e2a b2a mb "It wasn’t exactly clear, though. I suppose knowing who these characters are would be a boon..."
    show sayori ma
    mc ldown mb ea "Well, that’s why we’re doing this, so that we can find out together."
    m ec mb "Indeed, it’s certainly interesting."
    show sayori e1a b1a me ldown
    m ea md "Though part of me is starting to wonder if it might damage our opinions and therefore enjoyment of the story if we ever choose to go back and read it in full..."
    show monika mc
    show yuri e1d
    mc mg "I wouldn’t worry too much about that; if anything, it should make us more intrigued. Considering there are sequel stories, it doesn’t exactly spoil the entire plot, after all."
    show monika ma
    show sayori ma
    y lup e2a b1b mb nb "An excellent point. So, if I might surmise what I believe to be going on..."
    show yuri e3c ma b1d
    s mc "Ooo, yes! Please do!"
    show sayori ma
    y na e1d mb b1a "It would appear that there is a colony of people that have either created barricades to keep something out, or keep something in, which also involves some sort of maze."
    y e2a mh "Given that the story involves them running through said maze, the assumption would be that they were trapped inside this maze, in some sort of safe zone, but the containment was breached."
    y e1d mg "Therefore, they were forced to make a break for an exit?"
    show yuri e1a ma
    mc ml thinking "That certainly seems to be the case, but why were they there?"
    n cross mh "Something tells me we won’t find out by reading toward the beginning of the story; it feels like that’s part of the mystery we would have found out by reading the end."
    show natsuki ma
    s lup mh "So is it really worth reading further backward, then?"
    show sayori md
    show monika ec
    y mb "Perhaps not, but we might still learn something."
    show monika ea
    show yuri ma
    show sayori ldown ma
    mc ldown mb "Agreed."
    "We continue discussing what we’ve read for the rest of the club time, though Yuri was right: it was difficult to really determine what the story was about, from the small pieces of information we’d been given."
    "Still though, we agreed that the idea was definitely interesting enough to pursue again in the future, if we chose to."

    scene bg club_afternoon with fade
    $ set_date(minute=25)
    if preferences.language is None:
        $ auto_advance_date_mult = 0.66

    "All too quickly, the club meeting comes to an end."
    show monika turned:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    show bg class_2_afternoon
    with NonBlockingDissolve(0.5)
    "It seems Monika has more to say though, as she claps her hands to bring us together."
    m mb "Okay everyone~"
    m md rhip "Before everyone heads off, I wanted to ask something that's been on my mind."
    m rdown bb mb "I'm sorry, MC, I know you've only been in the club for a few days so I'll try and explain as best I can."
    show monika ma with None
    hide monika
    show sayori turned md:
        matrixcolor TintMatrix("#f1d6bb")
        i44
    show bg club_afternoon:
        align (1.0, 0.6) zoom 1.8
    camera master:
        align (1.0, 0.2) zoom 1.2
    with Dissolve(0.2)
    "I share a glance with Sayori, who looks just as surprised as I am."
    show sayori ma with say_dissolve
    _mc turned ec "It can't be that bad though, if she's smiling."
    camera master
    show bg:
        zoom 1.0
    show monika turned:
        i42
        matrixcolor TintMatrix("#f1d6bb")
    show yuri turned:
        i41
        matrixcolor TintMatrix("#f1d6bb")
    show natsuki turned md:
        i43
        matrixcolor TintMatrix("#f1d6bb")
    with fastfade
    "I finish gathering my things and move to the front of the room as Monika begins anew."
    m mb "The Culture Festival is the week after next, and I-"
    show monika md
    s e1b lup rup mh "Oh! Are we doing something~?"
    show sayori e1a me
    show monika rhip mc ec bc
    "Monika clears her throat, and it seems to occur to Sayori that she might have interrupted her."
    s b2b e2a mg rdown "Sorry..."
    show sayori mj ldown
    m eb mb "I'm happy you're excited, honestly."
    show sayori e1a md b1a
    m rdown lpoint ea ba md "-But yes, that was my hope. I've been debating with myself over what to do, but I think I've finally found an idea that we can get behind."
    show monika ma ldown
    show natsuki e1d b1d
    y lup e1d mh "Is it to sit down and read in peace?"
    show yuri md
    n b4 mg lhip "Yuri, how is that any different from what we already do?"
    show monika mc
    n cross b1a e1a mh "Plus what reason would we have for doing that at the festival?"
    show natsuki mj
    y e2a mg "Well, I mean we could just have it as a safe space for people to come away from the noise...?"
    show yuri rup me b2a e1a
    n mm e2a b1d "That's stupid."
    show natsuki mj
    m eb bc md "Both of you, please, that's..."
    show monika ea mc
    show natsuki me e1a b1a
    show yuri b2b md
    "Natsuki looks poised to continue, but then glances at Monika."
    show natsuki b1d md e2c
    "Something in her expression must get to the girl, because not only does she cease her verbal tirade upon Yuri, but she also looks away."
    show monika ea ba
    show sayori me
    show yuri b1a e1d
    n turned ldown rhip b1a mg "... Sorry, Monika. Please continue."
    show natsuki md
    "The girls seem somewhat taken aback by the muted reaction."
    show natsuki e1a
    _mc mh "I'm not familiar enough with most of the girls here to really know, but it seems they were expecting more."
    n rdown e1b b1d mm "... What? Don't... Don't look at me like that."
    mc ea ml "Like what?"
    n cross e2a mh "... Like I've done something weird."
    show natsuki md
    s lup mh "But you {i}did{/i} do something weird."
    show sayori md
    _mc ef ma "Well, I guess that answers my previous question."
    s ldown mh e2a "I thought you'd want to assert yourself more, but you backed off."
    show sayori md
    y rdown e2a b1d mg "I'll admit, I was expecting more..."
    show yuri ldown md
    n e1b mh nb "What- You don't have to make such a big deal out of it, okay? I just don't want to fight today!"
    n mm e3c "God!"
    show natsuki turned md at rhide zorder 1
    hide natsuki
    show sayori e1a at t33
    show monika at t32
    show yuri at t31
    "She steps over to the window, leaning on the small sill."
    show sayori e2c
    camera master:
        align (1.0, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show monika:
        alpha 0.0
    show yuri:
        alpha 0.0
    with Dissolve(0.2)
    "I glance toward Sayori, looking for any sign of answers, but she shrugs at me, just as lost."
    show monika:
        alpha 1.0
    show bg:
        blur 0.0
    camera master
    show yuri ldown e1a b1a:
        alpha 1.0
    with Dissolve(0.2) 
    m eb md "... I'll go talk to her."
    show monika mc at rhide zorder 1
    hide monika
    show yuri at t21
    show sayori e1a at t22
    "Monika sighs, following the girl to the window."
    show monika turned mc:
        i43
        matrixcolor TintMatrix("#f1d6bb")
    show natsuki turned e2a mi lhip:
        i44
        matrixcolor TintMatrix("#f1d6bb")
    show bg:
        align (1.0, 0.6) zoom 1.8
    hide sayori
    hide yuri
    camera master:
        align (1.0, 0.25) zoom 1.2
    with NonBlockingDissolve(0.5)
    "The three of us left simply wait for a moment, letting them speak without being overheard."
    show natsuki b3a ldown me e1a with say_dissolve
    "Whatever conversation they have doesn't appear to be long - Natsuki mostly motions to her armband, then to the door."
    show natsuki ma with None
    show natsuki e2a md 
    show monika ec
    show sayori turned ma:
        i42
        matrixcolor TintMatrix("#f1d6bb")
    show yuri turned md:
        matrixcolor TintMatrix("#f1d6bb")
        i41
    camera master
    show bg:
        zoom 1.0
    with Dissolve(0.2)
    "It doesn't appear that there's any misunderstanding or hard feelings, as the pair return pretty quickly."
    m rhip md ea "... Okay everyone, I think it's probably best if we leave it there for now. We'll return to this conversation next week?"
    show monika mc
    mc ea mg "But if it's for the festival, isn't that a little urgent?"
    show monika bc
    "Monika looks to Natsuki, then to the rest of the club members."
    m ba mb rdown "Not so urgent that I'll pull her away from her duties."
    show natsuki cross b1d md e3c
    show monika ma
    "Natsuki nods, her expression grim."
    n b3a mi "Duty calls, but that doesn't mean I won't make time."
    show sayori md
    n e2a b1a mh "Give me... maybe until Wednesday or so to get all my paperwork sorted, then I'll have time to help out."
    n b1d mb "... This is gonna be a {i}lot{/i} of early mornings, isn't it?"
    show natsuki ma
    s mh "Do you want some help?"
    show sayori ma
    show yuri e2a
    n b1a e1a mh "No, it's fine."
    n turned mb b1d e3c "I can't ask any of you to carry this burden."
    show natsuki ma
    mc bg ml "Is everything alright?"
    n b1a e1a mg "Hm?"
    show natsuki me
    "She looks at me quizzically."
    show yuri e1a
    n rhip b4 mh "Yeah? Why wouldn't it be?"
    show natsuki md
    mc bm ed mf thinking "... Okay?"
    show natsuki e2a b1a rdown
    "I feel like I'm missing something, but no-one else seems too bothered by it, so I brush it off."
    _mc mh ec ba "Maybe she's just a member of another club she's got commitments to?"
    _mc ea "Or perhaps it's to do with the band itself? It means she's a prefect, so she might have some Student Council or House duties?"
    _mc ma ldown "Yeah, that feels about right, actually, preparing for a Culture Festival."
    y lup e1d mh "So... we'll return to this conversation sometime next week?"
    show yuri ma
    s mb e3d "Looks like it~"
    s mh e1a "And- If there is anything I can do, just let me know."
    show sayori me
    mc mb "Me too."
    show yuri me
    show natsuki e1a
    "A couple of surprised looks are thrown my way, but I brush them aside."
    mc mg "If it means we can participate in the festival together, I'd be happy to pitch in."
    m bc mb "Well - Look at you, fitting right in~"
    show monika ma
    show sayori ma
    y mh "That's very... generous of you, offering to help her."
    show monika ba
    show yuri md ldown
    mc mg "Well, why not? It's the least I can do."
    show yuri e2a
    n mh "I really appreciate your offers, but I kinda have to do this stuff on my own." # im stuff
    n e2a b1d mg "Besides, I... don't really want to distract you from more important things."
    show natsuki md
    m mb "Natsuki, you're a valued member of our club and our friend. If anything, helping you is the more important thing here."
    show monika ma
    show natsuki nb ma
    "Natsuki attempts to hide her face, but the pink on her ears gives her away."
    n mm e3c nc "You guys... and right after I almost started another argument..."
    y e1a mb "But the key word there is 'almost'. You pulled yourself back, no?"
    show yuri ma
    $ autofocus.block("natsuki")
    n md nb "..."
    show sayori lup rup mb e3d
    s "Exactly! You did well~!"
    show sayori ma
    $ autofocus.unblock("natsuki")
    n b1a e1b mh "Alright, alright, no need to lay it on {i}that{/i} thick..."
    n lhip e2a b1d mg "I get you. I'll ask for help if I need it."
    show natsuki mj
    m mb ed "That's all we ask~"
    show monika ma at thide
    hide monika
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    "With that, it seems that club time truly does wrap up for the day."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show sayori turned:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    with Dissolve(0.2)
    $ say_transition = True
    "Sayori latches herself onto my arm before I can comment further."
    $ autofocus.block("sayori")
    s mb "Walk home?"
    show sayori ma with say_dissolve
    "I almost recoil at her sudden movement, momentarily stunned"
    _mc eb bb mh na "It's almost as if..."
    _mc ef nb ba "N- No. She's trying to act like she used to, isn't she?"
    _mc ma na "I see. To make it feel like nothing's changed. She's aware I'm still off-kilter."
    _mc ec mh "If she's going to this much effort then..."
    _mc ea ma "How could I say no?"

    play music2 add_playback_info(audio.okev_s, get_pos()) fadein 2.5
    stop music fadeout 2.5
    scene bg school_corridor_3_afternoon
    show sayori turned e3d:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    camera master
    with wipeleft_scene
    $ advance_date(minutes=2)
    $ say_transition = False

    "After we wrap up, Sayori and I gather our things and head off toward the front of the school."
    "She's in a bubbly mood, almost skipping while she hums to herself."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True 
    mc turned ml "What's gotten you in such a good mood, Sayori?"
    s mn "I have some cookies at home~"
    mc ed md "I see~"
    mc mg ea "What kind?"
    s e1b mb "Triple-chocolate-chip!"
    show sayori ma with say_dissolve
    mc mb "That's a lot of chocolate. Be careful to not eat it all at once."
    show sayori lup e2a b1d with say_dissolve
    "She pouts a little, but she's still smiling."
    s mb "Alright, {i}Mother{/i}~"
    show sayori ma with say_dissolve
    mc ed md "Someone's gotta be~"
    show bg:
        blur 0.0
    camera master
    show sayori e3d b1a ldown
    with Dissolve(0.2)
    $ say_transition = False
    "She doesn't stop grinning as we practically skip down the hall. I can hardly remember the last time she was in such a good mood over something so trivial."
    mc ml ea "Did you... wanna go get something to go with the cookies?"
    $ autofocus.unblock("sayori")
    s tap ea "Boo, you just want me to share~!"
    show sayori turned rup e3d at dip
    "She leans into me with her shoulder, slightly pushing me to the side."
    mc mb "I'll bring something to go with it!"
    show sayori rdown at hop
    "Now I'm grinning ear to ear as I push her back."
    s e3c b1d mh "Fiiiine, but only if you give me the chocolate milk you have at home."
    show sayori md
    mc ml "Hey now, how did you even-"
    s lup e1d b1b mb "You've always had chocolate milk in the house~"
    show sayori ma
    mc ef mf "Got me there..."
    show sayori ldown b1a e3d at hop
    "I push her again for good measure to try and reclaim some of my lost honour, and she chuckles."
    s e1a mh "We should-"
    extend mb " Oh, hi Kaito."
    show kaito turned lup mb ec:
        matrixcolor TintMatrix("#f1d6bb")
        t21
    show sayori ma at t22

    play music add_playback_info(audio.okev, get_pos("music2")) fadein 2.0
    stop music2 fadeout 2.0

    k "Boo~"
    k ea me bb "I see you two are having fun."
    k mf ldown ba ec "Didn't I warn you?"
    show kaito md
    show sayori me
    mc ed bm mg "You did, and I put it with the rest of your advice."
    "Any trace of my smile has long since vanished, replaced by a dark scowl and a glare."
    "Even Sayori's surprised by the expression on my face."
    s mg lup b2c "H- Hey now, there's no need to get-"
    show sayori md b1a
    k mf ee "No, don't mind her, she's just salty."
    k ea mc lup "How are you, Miss Katsuragi?"
    show kaito ma
    s ldown mb "Good! We just finished at the club!"
    show sayori ma
    k bb ldown me "As did I - the Debate Club wrapped up a little early today."
    k mf ba ee "Aika wanted us to go home and write a short analysis on the debate we watched."
    show kaito ma
    "He half rolls his eyes."
    show kaito ea
    s e1d b1d mh lup "Kaitoooo, you have to do your homework! Otherwise you won't learn!"
    show sayori md
    k lup mc ef "Hah, that so? I never would have guessed."
    show kaito ma
    s ldown e3d b1a mn "See? This is why you need to study, otherwise you don't learn~!"
    mc bi eg mj "Sayori - He's just being a twat."
    show kaito ea md
    s e1a b1d mh "Melly, that's rude!"
    show sayori md
    "She scolds me, her face somewhere between a pout and a genuine frown."
    k ldown ec mc "I agree. What have {i}I{/i} done to deserve such mistreatment~?"
    show kaito ma
    mc ml bi ec "Existed?"
    show sayori mh at hop
    s "Mel!"
    show sayori mj
    show kaito ea md
    mc bb mg eg "Fine! I get it, let's just go..."
    stop music fadeout 5.0
    show sayori b1a md
    k me bb "Go? It's cute that you two are walking home together after so long apart."
    show sayori b1b e2a 
    k ec ba mc "Almost as if there was never any hard feelings to begin with~"
    "His words cut me like ice."
    camera master:
        align (0.75, 0.2) zoom 2.0
    show bg:
        blur 2.5
    show kaito:
        blur 1.0
    with Dissolve(0.2)
    _mc ec mh ba "No hard feelings? We're pretending, both of us. I can see it in her eyes that she hasn't truly forgiven me. I'm just doing my best to ignore it."
    show black
    hide bg
    hide kaito
    camera master
    with Dissolve(0.2)
    play sound fall
    "I push past him, shoving him with my shoulder as hard as I can."
    "He staggers a little, but allows me to pass."
    k turned mf bg ea "Up to you, really. Just think about what position you're in, Miss Nakamura. Time waits for no-one."
    mc bd eb mg nb "Just shut up already!"
    "Leaving him behind, I can feel Sayori hesitate, but she inevitably follows behind, probably after apologising."
    _mc ef bi mh "It's better than he deserves."

    scene bg school_gate_afternoon
    show amelia turned ed lup mg:
        matrixcolor TintMatrix("#f5d5b6")
        i11
    with wipeleft_scene
    play music ohayou
    $ advance_date(minutes=2)
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0

    _mc turned "Ah, there’s Amelia. Waiting for me, as she said she would."
    show amelia eb bb md at t21
    show sayori turned me:
        matrixcolor TintMatrix("#f1d6bb")
        t22
    mc mb "Hey, Amelia. Mind if Sayori walks with us?"
    show sayori md
    show amelia ec ba
    "She blinks, not looking at me, but at the girl next to me. We’d gotten talking after the meeting, and I figured it wouldn’t hurt having her walk back home with us."
    _mc ec mh "... That’s what I tell myself, at least. I’m honestly just trying to not freak out around her, anymore."
    _mc ef ma "If we can spend some time being just friends in a social environment, that should do us... me, a world of good."
    show amelia ea ldown
    s e2a b2b mb lup nb "Ehe, I hope you don’t mind, but I live next door anyway, so if it’s not too much trouble-"
    show sayori e1a b1a md
    am eb bb mb "The more the merrier! Not like this is an exclusive party!"
    show sayori me ldown na
    am me "Actually, if you want, you can come over! I’ve got something planned that might actually be better with multiple people!"
    show amelia ea ba ma
    show sayori lup rup e1b mf
    "She beams, excited to be included."
    show sayori ldown rdown e3d ma
    mc eh md "Sweet! Sounds like a party!"
    s mh e1a "Oh, ah, wait though, I should check with Natsuki, just in case she had something she wanted to do tonight."
    show sayori lup ma e3c
    "She pulls out her phone, dialling the number of her best friend."
    show sayori e1a
    "It rings a couple of times, then Sayori starts speaking."
    s mb "Hey, Nats, I was wondering if you wanted to hang out tonight? Melody and her friend are planning a little get-together."
    show amelia ed lup md
    s ma "..."
    s md e2a b2b "..."
    s mb nb b2a "Oh, I see. That’s... too bad. I’ll text you later then, okay?"
    s e3d ma na b1a "Mhm! See ya!"
    show amelia ldown ea ma
    s ldown mh e1a "She said she’s busy with work tonight, but appreciates the offer."
    show sayori me
    mc mg ea "I mean, we didn’t exactly have the chance to offer-"
    s e2c b2a mk rup nc "O- Oh! Sorry, I didn’t even think, just sorta..."
    show sayori mj
    am bb ef mb "Not that we would have complained though! Seriously, the more the merrier!"
    show amelia ma
    show sayori e1a b2c ma
    "Sayori gives us a small smile; I know she appreciates that. Sure, she sometimes does things on impulse, but it’s fine."
    _mc ec ma "It makes her spontaneous, and it’s why we got along so well as kids. She was always dragging me into situations I would never dream of finding myself in otherwise."
    show amelia eb
    mc ea mb "So, shall we?"
    show sayori na
    am ea mb "Yes, let’s."
    show amelia ma

    scene bg school_street_afternoon
    show sayori turned e3c:
        matrixcolor TintMatrix("#ffeede")
        i44
    show amelia turned:
        matrixcolor TintMatrix("#ffecdb")
        i21
    with wipeleft_scene
    $ advance_date(minutes=10)

    "After a bit of walking, Amelia leans over toward me, and whispers in my ear, while Sayori wanders along, off in her own world, humming to herself."
    show amelia eb bb md:
        yoffset 150
    camera master:
        xalign 0.25 yalign 0.6 zoom 2.2
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("amelia")
    $ autofocus.block("sayori")
    am me "That’s the girl, right? The one you..."
    show amelia md 
    hide amelia
    show bg:
        blur 1.0
    camera master:
        xalign 1.0 yalign 0.2 zoom 2.0
    with Dissolve(0.2)
    mc turned ef ml "Yeah, that’s her."
    show amelia turned ed bh mc:
        i21
        yoffset 150 matrixcolor TintMatrix("#ffecdb")
    camera master:
        xalign 0.25 yalign 0.6 zoom 2.2
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "She clicks her tongue, more in amazement than anything else."
    am me "She’s... almost as pretty as you are."
    show sayori e2c
    show amelia md bi
    with say_dissolve
    mc eb bd nb mj  "Wha-"
    am bb eb mh "Oh, I mean-"
    show sayori me e1a
    extend ed bd mb " She’s really pretty, don’t get me wrong, I just, ah-"
    show amelia bb eb mh with say_dissolve
    s "Hm? What’d I miss?"
    show sayori lup md at i22
    show amelia ed bb ma lup at i21
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    mc eh bg md "N- Nothing! We were just talking!"
    $ say_transition = False
    $ autofocus.unblock("sayori")
    s tap ma "And you didn’t include me? Meanie..."
    show amelia ba md
    mc ea ba mg "It’s not like we didn’t want to include you, the conversation was just-"
    s turned e3c mh "Nah, it’s cool. I was doing my own thing anyway."
    show sayori e2c me at t33
    show amelia eb bb
    "She shrugs and returns to humming, as she walks alongside us."
    "My gut wrenches as I let out a frustrated sigh. I absolutely could have handled that better; most people would think that she just moves on quickly, but not me."
    show amelia ldown ea ba me
    _mc ec na mh ba "I know her better than anyone, which means I know how she thinks."
    show sayori e3c md
    _mc ef "... At least, I used to."
    show amelia bd md
    camera master:
        align (0.25, 0.25) zoom 2.2
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "Amelia gives me a light tap and a concerned look, noticing my souring demeanour."
    "I give her a small smile back, trying to tell her that I’m okay."
    show amelia ma with say_dissolve
    _mc ea ma bg "Yeah. I’m okay."
    "I chuckle to myself as I shake my head. It’s funny how I find myself talking in my own head, sometimes, as if I have something important to say."
    show amelia ba
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.3)
    "Shrugging, I turn my attention back toward the road. Best to keep my chin up, yeah? I should just be thankful for what I’ve been given."
    _mc ef "Thankful she would even look my way anymore."
    mc ea mg ba "Hey, Sayori?"
    show sayori e1a me at t22
    s "Hm?"
    show sayori ma
    "She pauses her skip and turns her head to face me."
    show sayori md
    mc mb "Thanks."
    s mg "What for?"
    show sayori ma e3c
    show amelia ed
    mc eg "For being you."
    s lup mb e1a "Ehe~ That’s what I’m best at!"
    show sayori ma
    mc ed md "Sure is."
    "A smile now worn properly across my face, I can’t help but notice the smug look Amelia’s wearing beside me."
    "I have half a mind to tell her to come off it, but can’t be bothered."
    _mc ef ma "Let her have her fun; I wouldn’t ruin this moment for the life of me."

    scene bg mc_living_room
    show amelia turned eb bb at i21
    show sayori turned at i22
    with wipeleft_scene
    $ advance_date(minutes=17)
    $ set_internet(True)

    "After getting settled, the three of us huddle around the coffee table."
    camera master:
        xalign 0.14 yalign 0.17 zoom 1.9
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc turned mg "So, what’s this game that had us skipping out on the arcade for?"
    am lup ed ba me "Well... Would it surprise you if I told you it was a card game?"
    show amelia ma with say_dissolve
    mc ec thinking ml "Not really?"
    camera master:
        xalign 0.9
    with Dissolve(0.2)
    s mh "Oh, what game?"
    show sayori md with None
    camera master:
        xalign 0.14
    with Dissolve(0.2)
    am eb bb me "It’s an old one, but... I can’t tell you the rules."
    show amelia md ldown with say_dissolve
    mc ea bd "Wait, don’t you know them?"
    camera master:
        xalign 0.9
    with Dissolve(0.2)
    s lup mc e1b "Aha!"
    show amelia ea ba ma
    s mb e1a ldown "She does know them, but she isn’t allowed to say them."
    show sayori ma with say_dissolve
    "Confused, I shrug. Surely someone will explain it eventually."
    camera master
    show bg:
        blur 0.0
    show sayori lup rup e3d
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    s mb "I haven’t played this game in so long! I wish Natsuki was here; she’s amazing at this one."
    show sayori e1a ma rdown ldown
    $ autofocus.unblock("amelia")
    am eb me "Alright, everyone okay if I deal first?"
    show amelia ma
    s mb "Sure!"
    show sayori ma
    mc ldown ed bm mg "I guess?"
    am ef mb bb "Don’t worry, you’ll get there."
    show amelia ma
    "I figure it’s best to just roll with it. Let’s see how it goes, huh?"

    scene bg mc_living_room
    show amelia turned ef bb at i21
    show sayori turned at i22
    with fade
    $ set_date(hour=18, minute=11)

    _mc turned eg bi mm  "That... was the most infuriating thing I have ever been party to."
    _mc ea mh ba "A game where you aren’t allowed to ask about the rules, and have to use the power of deduction? That, I can handle."
    _mc ec bi mh "A game where learning about the rules is entirely luck-based? That’s just awful."
    am eb mb "Hey, don’t feel too bad. You picked it up by the third round, didn’t you?"
    show amelia ma
    mc ba "..."
    show sayori mj
    show amelia md
    mc ef bi mb "Sayori. We’re subjecting the club to this tomorrow."
    s e2a b2a mb "H- Huh? That seems out of character for a literature club-"
    show sayori e1a b1a md
    mc ec md "That was not a suggestion."
    show sayori e2a b2b ma
    "She frowns, then shrugs, while a small smile starts to cross her features."
    show amelia bc ea
    s lup mb "I suppose seeing the looks on their faces would be worth it..."
    show sayori ma
    am ed be mb "... You’re both sadistic."
    show amelia ma
    mc ea ba mg "Hey, you said it, not me."
    s e1a ldown mb b1a "Yep, wasn’t me."
    show amelia bb ef
    show sayori e3d ma
    "We chuckle a little, before relaxing into some dinner."

    scene bg mc_living_room
    show amelia turned eb at i21
    with wipeleft_scene
    $ set_date(hour=19, minute=3)

    "After the pizza arrives, we settle into the sofa, putting on an old show that Sayori and I used to watch together as kids."
    "Amelia had apparently never seen it, somehow, so it worked well that she was with us to experience it."
    _mc turned mh "Considering how large a part of our lives this show had been, for so long, it only made sense."
    show amelia ea
    "Sayori excused herself after eating to visit the bathroom; it’s a little odd, honestly."
    _mc ec "Even when she eats in the clubroom, she often races off. I don’t remember her having such a small bladder as a kid..."
    "..."
    stop music fadeout 3.0
    _mc eb bd mf "... Wait."
    show amelia md eb bb
    mc bi eg mj "Oh, god damnit."
    _mc mh "This has nothing to do with her bladder."
    _mc eb bd "The pizza. I can’t believe I didn’t see it before; how could I have been so blind?"
    am me "Huh?"
    show amelia md
    mc ef bi mf "I..."
    mc ea ba mg "I’ll be back."
    show amelia be ea 

    scene black with wipeleft

    "I make my way to the top of the stairs, where the bathroom is. The lights are off up here, making it pretty dark."
    _mc turned ec mh "Still, both of us know this place like the back of our hands."
    mc ea mg "Sayori? I know you’re in there."
    mc ef bg ml "I, ah, won’t pry too deeply, but... I think I understand. I’m sorry I never noticed before."
    mc mb "You’d think I’d be a little more aware about things when it comes to my best friend, right?"
    mc eg mg "Point is, I’m sorry. I didn’t think too deeply into it, but... I guess it’s a little hard to ignore when I’m supposed to know so much about you."
    mc ea bf mb "If there’s anything I can do to help, I-"
    s turned e2a b1b mg "No, there isn’t."
    s me "It’s..."
    mc eg ml bg "Sayori, I’m sorry."
    "I place a hand on her shoulder."
    _mc ea ma "Even in the darkness, I know where she is."
    mc ml "I know, I understand, that this is because of me."
    mc eg mb "Maybe that’s arrogant, maybe there’s more to it than that, but I-"
    s e3c md "Mm."
    _mc ef mh "The last thing I wanted to hear."
    mc ml "I wish I could have seen it sooner, or known better, or done something, {i}anything{/i} to help, but I..."
    mc ea bf mb "I was blind, wasn’t I?"
    s e2a mg "... Blind as a bat."
    mc ba mg "But a bat’s vision is around as good as a human’s-"

    play music myconfession

    "I cut myself off, as I feel arms wrap around me."
    "..."
    "Gone are the days when she was taller than me. Now, we stand at a similar height; perfect for me to run my hands through her hair."
    s e1a b2b mb "It’s okay, Melody. I promise you."
    s e3c "I’ll be okay."
    mc ef mf "But I-"
    s b1b e2a mg"I know. You wanted to help me, but we..."
    "I fight the welling tears building within me, not daring to allow the dam to burst."
    _mc eg mh tears_a "It’s so much more than I thought it was. Everything is."
    _mc ma ea bf "I’ve missed her more than words could possibly convey."
    mc ml notears "Sayori, I-"
    "She hushes me, before I can speak."
    _mc eg ba ma "Her hugs are warm, such that they don't feel like the ones I remember."
    s b1a mb e3c "I know, Melody. I’ve always known."
    mc mf bg "B- But I-"

    #[Full Voice Acting]
    s me "Shh. Take a breath. You’re going to be okay."
    _mc ef ma "Ah. That's what they remind me of. Her hugs are just like Aunt Katsuragi's, the way she leans down to place her forehead upon the top of my head."
    _mc eg "That's why they feel so nostalgic."
    s mb "{i}We’re{/i} going to be okay."
    s mg "Now..."
    "She places a hand upon the side of my face, and her forehead to mine."
    "S & MC" "Swish, swish, swish, swish. Call away the bad thoughts."
    "S & MC" "Let them sing, call to me, tell me all their candid wroughts."
    "S & MC" "I will hold you, safe and tight;"
    "S & MC" "I will hold you, through the night."

    #[End Voice Acting]
    "A small poem that Sayori wrote when we were much younger, and we’ve used it to comfort each-other ever since."
    _mc mh ef "... Hell, sometimes, at night, I’d whisper it to myself, when it all became too much."
    mc mf "... Why?"
    mc bf ea mg "Why is it that whenever I try to comfort someone, I end up a bigger mess?"
    "She takes my hand, interlacing her fingers with mine."
    s mb "Because you feel for them. It’s... your superpower, taking on the burdens of others, so that they can be free."
    "Sayori taps my nose, and through the darkness I can see her smile."
    s e2a "You don’t see it, but you’re so, so selfless, Melody. Even when you shut yourself off, you can’t help but reach out to those in need."
    s e1a b2b "There’s a reason we were so close. We complemented each-other. You hate the world, but can’t help trying to fix it."
    "I chuckly dryly, despite myself."
    _mc bg ma ef "God, that's cheesy. It's also wrong, but - if she sees something in me that I don't, maybe that means there's hope."
    _mc "I'm not selfless, and I think she understands that. Then again..."
    mc bf mb ea "And you love the world, but lack the ability in your own two hands."
    s e3c b1a "But together, it all just..."
    mc ml ba "Happens."
    mc eh bg md "One hell of a team, eh?"
    s e2a mg "Even now, when we have new friends..."
    mc mb ea ba "We still know what the other is thinking."
    "She nods."
    _mc ec ma ba "Confirmation, then, I take it. Even if it isn't true, she knows it could be - This is her way of letting me understand that."
    s e1a mh "The girl down there, Amelia? Take care of her. She’s lovely."
    mc ml ea "Your friend, Natsuki, seems the same way, despite her..."
    s e3d mn "Hehe, she’s like that. But on the inside, she’s like a jelly bean."
    mc ed md "Hah, I don’t doubt that for a second."
    s e1a mb "So... Please try to get along with her?"
    mc ea mb "Of course. I’d be happy to, if she’s good enough for you."
    "Sayori shuffles, a little awkwardly."
    mc mg "Even if you don’t think you’re good enough for someone, I know better. That’s why you’ve got us, right?"
    s e1d b1d "You always know how to steer me right, huh?"
    mc ed md "Always."
    "I ruffle her hair a little."
    mc mb ea "Also? I love the new hair. It suits you."
    s e3d mn b1a "Ehe~ I’m glad."
    _mc ec ma "What a day."

    $ add_calendar_description(calendar_descriptions["natsuki"][1])

    call week_1_friday_natsuki from _call_week_1_friday_natsuki
    return