label week_1_wednesday_monika:
    call act_card("act_I_m_card") from _call_act_card_1
    call calendar_transition(day=25, hour=16, minute=1, second=0) from _call_calendar_transition_2
    scene bg club_afternoon with dissolve_scene_full
    $ set_internet(True)
    play music okev

    "After our regular activities, we relax into our individual spots for some relaxation time."
    "Finding it a little difficult to focus, I look around to see what everyone else is up to."
    show expression split("bg club_afternoon", "bg club_closet_afternoon", "bg class_2_afternoon") as stuff
    show yuri turned lup e2a md b1d:
        matrixcolor TintMatrix("#f1d6bb")
        i31
    show natsuki turned e1d b1d mj:
        matrixcolor TintMatrix("#f1d6bb")
        i32
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        i33
    with NonBlockingTransition(fastfade)
    "Yuri seems to have slinked off to enjoy a book, Natsuki is glancing up at me suspiciously from behind a manga, and Sayori is writing something."
    hide yuri
    hide natsuki
    hide sayori
    show monika turned eb mc:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    hide stuff
    with NonBlockingTransition(fastfade)
    _mc turned thinking mh "Monika is.... looking rather lonely, actually."
    _mc ec "A bit out of character."
    "I decide to check on her."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    mc ea ldown mg "Hey, Monika, are you okay?"
    show monika ea with say_dissolve
    "She snaps out of her reverie."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    m md "Y- Yes... I’m quite fine."
    show monika ma 
    "Her face turns to a smile."
    _mc ec mh "A slightly fake smile."
    mc ea mb "Great."
    show monika mc
    mc mg "Because I wondered if you wanted to read or write together?" 
    m md "I... I’d like that."
    m bb eb mb "I’d.... really like that."
    show monika ba ma
    mc ed mf "So, which one?"
    m ea mb "Whichever you prefer."
    show monika ma
    _mc thinking mh ec "Hmm. Considering she showed me that work of hers from day one... I think we should write some more."
    mc mb ea "Let’s write something."
    m md rhip "Okay then. What, a poem, story?"
    show monika mc
    mc ml ldown "I think you should choose this."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc ec mh "The normally take-charge Monika is coming across as strangely passive today."
    _mc "Further reinforcing the notion that something isn’t quite right in her world."
    _mc ea "She’s usually in the hot seat all the time. Making decisions, dictating policy."
    _mc ef "A stressful role, to be sure."
    _mc ec thinking "Perhaps what she needs is a little break from that."
    hide black with NonBlockingDissolve(0.5)
    _mc ea ma "If so, I’m more than willing to take the reins and ease her load - have her not be burdened by the pressure of choice, for once."
    mc ldown mb "Okay then. We’ll write a small story."
    show monika ma ec rdown
    "Her face brightens."
    _mc ef ma "I... It feels remarkably good trying to help her a little."
    _mc ea "I should try to help her more often. It’s the least I can do."
    mc ml "So Monika, let’s start. It’ll be a short story."
    mc ed md thinking "And to put an interesting spin on things, we’ll make it a collaborative work."
    mc ea mg "Taking turns to fill in the details."
    mc mb ldown "Does that sound alright?"
    show monika ea
    "Her smile seems to grow a little."
    _mc ec ma "It feels remarkably good, being able to lift her spirits."
    _mc ea "So rewarding is her smile."
    "Determined to achieve more, I put pen to paper and kick things off."
    show monika mc
    if preferences.language is None:
        $ auto_advance_date_mult = 0.727
    mc thinking ef ml "Fallen leaves and twigs crunch underfoot as I tread my way through the verdant forest."
    _mc ea ma "A fairly innocuous opener; let’s see what Monika can do with this."

    play music2 add_playback_info(audio.okev_m, get_pos()) fadein 2.0
    stop music fadeout 2.0

    m ec bc md "Tread in the opposite direction from my home, and the tedious garden party that carouses therein."
    m eb mb "For the life of me, I can’t stand fancy-doers and their hoity-toity attendees."
    m ec bb md "It’s so stuffy. Not at all how I wish to be. And nobody would notice if I left and never came back." # im stuff
    show monika mc
    "I raise an eyebrow. Interesting tack she’s taken there, introducing a spot of drama." 
    _mc ldown ec bi "Let’s see if I can boil the pot even more."
    show monika ea ba
    mc md eh bb "Finally being able to breathe, both literally and figuratively, is so amazingly liberating."
    mc ef mb "I pause in my tracks to take in the beauty of my surroundings."
    mc ea "To be at one with the splendour of nature, so at odds with my usual dreary habitat."
    show monika ma
    mc ml ba "And then I suddenly realise that I am not alone."
    m lpoint md "A slight chatter emanates above me."
    m ldown eb bc "I spy some small rodents scurrying."
    m ba "Squirrels?"
    m mb "I see them scurrying."
    m md "They seem to be... climbing downward."
    m bc "Towards me."
    m rhip ec ba "With a mixture of curiosity and amusement, I watch them approach."
    m ea "And allow them to swarm all over me."
    m mb rdown "Engulf me in a mass of warm, furry bodies."
    m eb "And eventually, carry me away with the combined strength of their entire pack."
    show monika ma
    _mc ec ma "I am just as curious and amused as our fictional protagonist at what direction the story has taken."
    _mc ea mh "Monika is really into it, her brooding mood from earlier practically absent now."
    _mc ma "Replaced by an impassioned, almost feverish intensity as she expands upon our tale."
    "I decide to let her take over and see where this ultimately leads."
    m ec bc md "Through thickets, copses and spinneys, they scamper."
    m lpoint eb "An undulating, mobile carpet, soft and fuzzy."
    m ec md "Upon which I lie, completely abandoned to their minuscule machinations."
    m ea ba mb ldown "Feeling nothing but the most unusual euphoria."
    m md rhip "The euphoria of relinquishing control and just letting it all take me."
    m ec "At long last, we arrive at our ultimate destination."
    m eb rdown "The glade is spacious and lush; ringed by a dozen majestic trees."
    m lpoint "Their multi-hued blooms carpeting the floor in a dazzling riot of colour."
    m ea ldown "Upon a marble slab at its very centre, they place me."
    m rhip bc "And proceed, with absolute gentleness, to peel away my skin."
    m ec ba "I feel no pain whatsoever as they dehusk me, as they might do one of their acorns."
    m ea rdown lpoint "Instead emerging from what they have discarded, lighter, radiant and winged."
    m ldown mb "Like a butterfly from its pupa."
    m ec "Reborn anew."
    m eb "Gratefully petting them as I descend from the dais, I rejoice in my new form and surroundings."
    m ec md "Twirling and pirouetting amidst a rainbow of petals."
    m ea bc "Out with the old. Away with the shackles of etiquette, decorum and rules."
    m ba eb "This is my home. And I am here to stay."
    show monika mc
    "By the time Monika has brought the story to its conclusion, there is a faraway look in her eyes."
    "Peaceful, yet contemplative at the same time."
    _mc thinking ec mh "While not the peak of cheerfulness, it’s certainly a sight better than how she was earlier."
    _mc ea ma "For my part, I’m pleased that she looks improved."
    _mc bb mh eb "But what she’s written has also left me nothing short of astonished."
    mc ml nb ldown "... That’s quite the yarn."
    show monika ea
    mc bg ea mb "I can’t say I’ve ever had the privilege of reading anything quite like it."
    m bb md "... Oh no."
    m ec nb "I- I’m so sorry, MC. I didn’t give you the chance to contribute further."
    m eb mb "God, I’m no better than our protagonist, am I? Letting myself get carried away just like that."
    show monika ma
    mc eh bf md "Not to worry. I love watching a talented writer immerse herself in her craft."
    show monika ea
    mc ea ba na mb "You wrapped the whole thing up far more neatly than I ever could, so I’m hardly complaining about your taking over."
    m ec na mb "... You’re too kind. Seriously."
    show monika ea mc
    mc mf "Just being honest. Just laying it all bare."
    show monika ba
    mc ec thinking ml "Speaking of laying things bare... Mind telling me what this is all about?"
    show monika ma
    mc ea mg "It’s beautifully outlined, don’t get me wrong. Wonderful imagery and all that. But whatever meaning there is in there... it’s lost on me."
    _mc ec mh "I must confess that I’m not being entirely truthful here."
    _mc ea ldown "From what I can see, my earlier suspicion that Monika wishes to relinquish the responsibility of control every now and then, is quite likely correct."
    _mc "That her desire for this has manifested in her writing."
    _mc ec "But I guess I just want to hear some confirmation from her lips."
    _mc "Want to know that I have a handle on this girl who is just as enigmatic as she is gorgeous."
    "Monika’s smile, while no longer as artificial as it was previously, is a tad crooked nonetheless."
    m rhip md ec "It’s quite open to interpretation, I suppose."
    m mb ea "Perhaps it’s played entirely straight and should be taken entirely at face value."
    m lpoint rdown md "A fantastical account of being abducted by woodland animals and magically metamorphosed into someone or something completely different."
    m ldown ec "Or perhaps one can go a level deeper and regard it as a metaphor."
    m eb "A metaphor for emancipation, for release."
    show monika mc
    _mc ea "Not quite a slam dunk, but close enough."
    "I take that as my cue and wade in with another observation that has just come to mind."
    show monika ea
    mc mb "And maybe transcendence, too?"
    show monika md
    "Monika looks at me with pleasant surprise."
    m mb lpoint "Maybe transcendence, too, yes."
    m ldown md "Shrugging off an undesirable façade and soaring off into an elevated state of being."
    m eb bb mb "Or maybe this story just reflects the fact that I’m a nut. Ahahaha."
    show monika ma
    "I raise an eyebrow, but don’t question her."
    _mc ec ma "Perhaps she is nutty, but she is certainly just as sweet."
    show monika mc ea ba
    "I go to place my hand on her pen."
    show monika ma ec lpoint
    "And she raises a delicate finger to her lips and shushes me."
    m ldown eb mb bb "L- Let’s... Let’s just let ourselves concentrate on writing."
    show monika ma
    "I look into her eyes and see a rather mossy shade of brown reflected where they catch the light." 
    _mc mh "Just like the hazelnuts she wrote about."
    mc ea mf "Must we?"
    m ec md ba "Yes. Sorry, I know you probably wanted to spend today with Yuri or someone."
    show monika ea mc
    mc mg "I meant because I wanted to spend longer with you."
    mc mb "Because I want to."
    show monika eb nb ma
    "She blushes, a little surprised by my sudden statement."
    mc mg "I promise, I enjoy being with you."
    show monika ec bb
    "She looks somewhere between laughing, crying and pain."
    "As if incredulous but unconvinced."
    mc ml bg "Monika, do you not believe me?"
    m ea md "I, uh-"
    m eb na "I just... don’t see how you would have enjoyed this."
    show monika mc
    mc bf eh md "You’d be surprised at the wonders of good company."
    show monika ea
    _mc mh ea ba "At that, almost imperceptibly, the tide seems to turn."
    show monika ec mc ba
    "The seething emotions undoubtedly churned beneath Monika’s exterior... They appear to slowly settle."
    "Her scepticism dimming a shade or two."
    show monika md
    "Monika’s lips part, as though she is on the verge of mouthing something less self-deprecating."
    _mc ma ec "Something that might further strengthen this tenuous connection we’ve forged."
    show monika ea mc
    play sound phone_notification volume 0.5

    play music add_playback_info(audio.okev, get_pos("music2")) fadein 1.5
    stop music2 fadeout 1.5

    "Unfortunately, the abrupt interruption of a silenced cellphone’s vibratory buzz shatters the improving ambience."
    _mc ef bi pout "And just like that, the moment is frustratingly lost."
    m ec bc md "Shoot. It’s mine."
    m ea bb mb "I’m so sorry, MC. I’m going to have to take this."
    show monika ma
    mc ea ba ml "It’s not a bother."
    show monika bc mc 
    "I notice her brows knit in consternation upon producing the device and noting whomever it is that is attempting to contact her."
    show monika eb at lhide
    hide monika
    "She swiftly rises to her feet and traverses the room to its far corner as she responds to the call."
    "The immediate explanation for this behaviour that runs through my mind is that she doesn’t wish for background noise to interfere."
    show yuri turned lup b1d mh:
        matrixcolor TintMatrix("#f1d6bb")
        t31
    show sayori turned b2b lup rup mh:
        matrixcolor TintMatrix("#f1d6bb")
        t32
    show natsuki cross b3d mm nb:
        matrixcolor TintMatrix("#f1d6bb")
        t33
    "Yuri and Natsuki ARE engaged in a rather heated discussion, after all, with Sayori frantically attempting to mediate."
    "But for the briefest moment, I find myself wondering if it’s because she doesn’t want anybody to overhear."
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri 
    show monika turned eb bc:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    $ advance_date(minutes=2)
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    "Regardless of the reason, when Monika returns, I am crestfallen to note that she once again looks no better than she did when I first sat down with her."
    "All my efforts at cheering her up, undone by a single phone conversation."
    _mc thinking ec mh ba "What the hell could it have been that’s so thoroughly removed the wind from her sails once more, just like that?"
    show monika ec ba md at dip
    _mc ef ma "To her credit, she shrugs her discomfort aside and makes a courageous effort to address us as she normally does towards the end of every club session."
    show monika mb ea at t42
    show yuri turned:
        matrixcolor TintMatrix("#f1d6bb")
        t41
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        t43
    show natsuki turned e2c b1d mj:
        matrixcolor TintMatrix("#f1d6bb")
        t44
    m "It’s been great as always, everybody. Productive discussion, tantalising viewpoints, amazing artistry all around."
    show natsuki e1a b3a md
    show yuri lup mf b1b e1d
    show sayori md
    m bc ec md "Sadly, I won’t be able to partake in the rest of it; I’ve got something I need to urgently attend to."
    show sayori ma
    show yuri e1a b1a ma
    m ed ba mb lpoint "If you could do the honour of wrapping things up, Sayori, I would be most grateful."
    show monika ma ldown
    "Good old Sayori, despite being frazzled from having to keep Yuri and Natsuki at bay, immediately snaps to attention."
    show natsuki ma
    s lup rup e3d mb "Of course, Monika. You can count on me."
    show sayori ma
    m rhip ec md "You’re a champion."
    show sayori ldown rdown e1a
    m rdown ed mb "See you tomorrow, everybody. I’ll try not to let things get in the way then."
    show monika ea ma
    y mb ldown "Do take care, Monika."
    show yuri ma
    n cross mc e2c nb b3d "Yeah, don’t stress about it. You sure we can’t... you know, lend a hand?"
    show natsuki e1a me b3a
    show sayori b2a md
    show yuri md e1d
    m ed bc mb lpoint "... An arm and a leg might be more accurate, ahahah. And I wouldn’t wish that upon any of you."
    show monika eb ba ma at thide
    hide monika
    show yuri me rup at t31
    show sayori at t32
    show natsuki md b1d at t33
    "The others and myself can’t tell if she’s joking or otherwise, what with that somewhat jarring laugh." 
    show sayori e2a at thide
    "Yuri, Sayori and Natsuki eye each other with a mixture of confusion and nervousness for a moment."
    show yuri e2a md at thide
    show natsuki at thide
    hide yuri
    hide natsuki
    hide sayori
    "Then they clearly, collectively decide to leave it at that, and return to their tasks in spite of whatever doubts they harbour."
    _mc bi mh ec ldown "Not me, though."
    "I can’t shake my concern for Monika."
    show monika turned eb ba mc:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    camera master: 
        align (0.5, 0.2) zoom 1.5
    show bg class_2_afternoon:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "As she gathers up her belongings and prepares to leave, I cannot help but start after her."
    mc ea mf ba "Monika, I-"
    show monika ea with say_dissolve
    "Only to be stopped in my tracks by how strangely calm she now looks."
    "An almost eerie serenity."
    m ec md "It’s been a trying day, MC."
    m bc mb "I don’t think I’ve seen the last of its tribulations."
    m eb ba "But thank you for making things at least somewhat bearable."
    m bb ec md "I don’t know if I’ll be able to make it through in one piece, but..."
    show monika ma ea with say_dissolve
    "Her eyes turn in an almost tender look."
    m eb mb "The memory of this afternoon we’ve shared will give me a fighting chance."
    show monika ma with None
    hide monika
    camera master
    show bg club_afternoon:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("monika")
    $ say_transition = False
    "And with that, she slips out."
    "The shimmer of the ribbon around her ponytail being the last sign I see of her for the day."
    "While I’m still as bemused as ever by Monika and her air of mystery, and while I won’t deny that I’m still a little worried..."
    "... I allow myself the satisfaction of holding my head somewhat higher at her parting words."
    _mc ec ma "Perhaps it wasn’t for naught after all."

    $ add_calendar_description(calendar_descriptions["monika"][0])
    
    call week_1_thursday_monika from _call_week_1_thursday_monika
    return