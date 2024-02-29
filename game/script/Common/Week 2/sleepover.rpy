# this
# was a pain to code
# :YesHoney:

label sleepover:
    $ stop_channels()

    scene black with wipeleft_scene
    $ set_date(hour=16, minute=30, second=0)
    $ set_internet(False)
    play music childlikesmile

    if not branches.is_current(branches.SNARED):
        "After finishing work, I began the long trek back home."

    "I wonder as I walk-"
    _mc turned casual thinking mh "What's going to happen tonight?"
    _mc ec "See, tonight will be no ordinary night."
    _mc eg ma ldown "No, it shall be something special."
    _mc ea "Sayori's spent the week planning for a get-together for the club at her place, giving us all a chance to take a load off before the festival on Monday."
    _mc ec "I'd be lying if I said I'm not excited."
    _mc ef "After all, the whole club is going to be there."
    _mc eg ma "We'll have a chance to watch movies, play games, and just talk. It's something the club environment doesn't really allow us to do."
    
    scene bg s_house_afternoon with Dissolve(1.0)

    python:
        advance_date(minutes=25, seconds=1)

        if branches.is_current(branches.SNARED):
            advance_date_str("After finishing work, I began the long trek home.")
        
        set_internet(True)

    "I finally arrive at Sayori's front door, smiling like a goofball."
    _mc turned casual thinking mh ec "I should tone it down. I might come off looking like a psycho."
    _mc ea "Is it strange to be this excited?"
    _mc eg ldown ma "It certainly feels that way."

# SFX: Knocking
    "After a few moments, Sayori answers."
    show sayori turned casual:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    mc ea mb "Hey, Sayori, how's it going?"
    s lup mb "Great! I just finished setting up. How was work?"
    show sayori ma at thide
    "She invites me inside, and I oblige."
    hide sayori

    scene bg s_house_entrance_afternoon
    show sayori turned casual:
        matrixcolor TintMatrix("#ffdfc0")
        i11
    with wipeleft
    mc turned casual mb "It was something alright, but it was a lot of fun, so I can't complain."
    s e3d mb "That's great to hear."
    show sayori ma
    mc ml "Are the others here yet?"
    s lup e1a mh "No, Natsuki's on her way, and Monika said she was running about ten minutes late."
    show sayori md
    mc mg ef "What about Yuri?"
    s b1b e2a ldown mg "I dunno, I haven't heard anything from her, but she said she'd be here around five. So, I'm guessing that's still happening."
    show sayori md

    if branches.is_current(branches.FEELINGS):
        mc ea mf "Well..."
        $ autofocus.block("sayori")
        s ma nb b2b "..."
        show sayori b2a e1a
        "We glance at each-other."
        _mc turned ec mh "I do want to talk to her about what happened last night, but..."
        _mc ef ma "Actually, one of the first things I noticed about her is that she's replaced her pads."
        _mc ea mh "I guess that means she isn't comfortable sharing that information with the club, which doesn't surprise me."
        mc ml "Did you... get your stuff from my house?" # im stuff
        $ autofocus.unblock("sayori")
        s e2a mb b2b "Y- Yeah, I did."
        show sayori ma
        mc mb "Awesome."
        mc ef "It's been a crazy day, hasn't it?"
        s b2a e1a mb "... Yeah."
        show sayori b1a md na
        mc ml nb "Well... since everyone's late..."
        s e3d mb "Ehe~ Great minds think alike."
        show sayori lup rup b1b e3c me with None
        camera master:
            align (0.5, 0.2) zoom 1.7
        show bg:
            blur 2.5
        with Dissolve(0.2)
        $ autofocus.block("sayori")
        $ say_transition = True
        "Bringing her in, I feel her soft hair in my arms, mere moments before I feel her lips clash with mine."
        show sayori e3d b1a with say_dissolve
        "Like a battle for supremacy, we fight to prove ourselves."
        "Sayori might be skilled, but she's no match for my tenacity, and I press my advantage, lowering her onto the couch."
        show sayori b2b nc with None
        camera master:
            zoom 1.85
        with Dissolve(0.2)
        "It takes mere moments for my dominance to shine through, and for her nails to dig into my back, as-"
        camera master:
            zoom 1.4
        show bg:
            blur 1.0
        with Dissolve(0.2)
        s e2a mg "Ah, they'll be here... soon..."
        show sayori b2a nd e3d me with None
        camera master:
            zoom 1.9
        show bg:
            blur 3.0
        with Dissolve(0.2)
        "I ignore her, instead increasing my assault."
        "After all this time, I'll take any opportunity I get-"

        play sound doorbell

        camera master
        show bg:
            blur 0.0
        show sayori e1b b1a mj ldown rdown
        $ say_transition = False
        "Panicked, I pull away, glancing at my watch."
        "Exactly 5pm."
        mc bb nd eb mg "Ah, shoot, that's Yuri."
        $ autofocus.unblock("sayori")
        s mg lup e1a b2c "Ah, but I..."
        show sayori me
        "Looking at Sayori, she's a mess. Her hair's been ruffled, her clothes are only half-worn."
        s ldown e1b b1a nb ml "Wait, no, she can't-"
        show sayori mk
        mc bd nb mj "I'll stall her, go, go!"
        show sayori e2b at lhide
        hide sayori
        "Sayori quickly gathers herself and makes for the bathroom, and I head for the door."

    else:
        mc ea mb "Sweet. That's not long from now, at least."
        show sayori e1a b1a
        mc mg "Is there anything you need help with?"
        s b1b e3c me "Hmm."
        s lup mh e1a b1a "Actually, if you could set out some place-mats onto the coffee table, I can make some hot chocolate for everyone."
        show sayori ma
        mc ml "Oh, sure."
        show sayori e3d at thide
        hide sayori

        scene bg s_living_room with wipeleft
        $ advance_date(minutes=2)

        "Making my way into the living room, I grab out some of the small boards, placing them around the table. I also make sure to fluff up the pillows and dust off the couches."

        play sound doorbell
        "And, as if on cue, I hear the doorbell."
        mc turned casual mg "That'll be Yuri. I'll grab it!"
        s turned casual mi b4 "Huh?"
        "Sayori, clearly unable to hear me, calls out from the kitchen."
        mc eg bi nb "Nevermind, Sayori!"

        scene bg s_house_entrance_afternoon with wipeleft
    
    camera master:
        align (1.0, 0.55) zoom 1.5
    with Dissolve(0.2)

    "Walking over to the front door, I open it up to see Yuri standing there."
    show yuri turned casual lup md e1d:
        xcenter 0.75 ypos 1.0 yanchor 0.95 zoom 0.7
        matrixcolor TintMatrix("#ffdfc0")
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    $ renpy.set_tag_attributes("melody turned casual mb ea ba na" if not branches.is_current(branches.FEELINGS) else "melody turned casual bg eh md nb")
    mc "Hey, Yuri!"
    y mg "Oh, hello, MC." 
    y ldown e1a mb "Is Sayori here?"
    show yuri ma with say_dissolve
    if branches.is_current(branches.FEELINGS):
        mc ml ea bb "Oh, she's...uhh...making hot chocolates for everyone."
    else:
        mc mg "Oh, she's making hot chocolates for everyone."
    y e3d mb "That'll be lovely."
    show yuri ma with say_dissolve
    "Before I can utter another word, I feel Sayori's presence at my side." 
    show yuri at i22
    show sayori turned casual:
        matrixcolor TintMatrix("#ffdfc0")
        i21
    camera master
    camera above_master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("yuri")
    $ say_transition = False
    s mb "Hey Yuri!" 
    show sayori ma
    y mb e1a "Hello Sayori. How are you?"
    show yuri ma
    s lup rup e3d mb "Great, really excited to host something for the club!"
    show sayori ma
    y lup mb "I know you'll do a great job, Sayori."
    show yuri ma at thide
    s mn ldown rdown "Ah well...! Thanks, Yuri!"
    s e1a mb "Now, what're you waiting for? Come in!"
    show sayori ma at thide
    hide yuri
    hide sayori

    scene bg s_living_room with wipeleft
    show sayori turned casual md at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.3)
    $ autofocus.block("sayori")
    $ say_transition = True

    mc turned casual ml "How are those hot chocolates coming along?"
    show sayori e1d b1d lup with say_dissolve
    "Sayori pauses, processing what I asked."
    s b1a e1b mc "Oh!"
    s b2a e1a nb ml ldown "I forgot." # she sayor :skull:
    show sayori e2c mk rup at rhide
    hide sayori
    show yuri turned casual e1d mf lup at i21
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ autofocus.unblock("sayori")
    "I share a look with Yuri as Sayori disappears."
    show yuri ma at i11
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    mc ed md "So, so forgetful."
    y ldown e3d mb "She means well though."
    show yuri ma with say_dissolve
    mc ea mb "Yes, she does."
    s turned casual nb mb "Here!"
    show yuri at i21
    show bg:
        blur 0.0
    camera master
    show sayori ma lup e3d at i22
    with Dissolve(0.2)
    $ say_transition = False
    "Sayori practically throws a cup of hot chocolate at me."
    show yuri e1a
    show sayori ldown na e1a
    "I take a sip."
    show yuri b1d e3c mg
    show sayori mo e3d
    mc ed md "This is good stuff, Sayori~" # im stuff
    show sayori e1a ma
    $ autofocus.unblock("yuri")
    y e1d b1a mh "It really is, though you may want to consider thinner milk."
    show sayori me e1b
    y e1a mb "It can make a more chocolatey aroma, which helps with the taste."
    show yuri e1d md
    s e3d mb lup "Thanks Yuri!"
    show sayori e1a md
    y lup e2a b1d nb mb "My pleasure... I didn't mean to cause offence, it tastes lovely."
    show yuri ma
    s ldown e3d mo "None taken~"
    "Sayori beams a bright smile towards the both of us."
    s e1a mb "So, shall we get settled?"
    show sayori ma
    mc ba mb ea "Sure."
    y e1a b1a mb "That would be good."
    show yuri ma na ldown
    s rup mb "I'll be back in a sec!"
    show sayori me nb
    mc mg "I'll help!"
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0 xoffset -200
    hide yuri
    show sayori rdown at i11
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ autofocus.block("yuri")
    $ say_transition = True
    s mg "T- Thanks, okay."
    s ldown e2a mb na "Are you going to be okay on your own?"
    show sayori ma with None
    hide sayori
    show yuri turned casual at i11
    show bg:
        xoffset 200
    camera master:
        yalign 0.1
    with Dissolve(0.2)
    y mb "Yes, I'll be fine."
    show yuri ma with None

    hide yuri
    camera master
    hide bg
    show bg s_house_corridor_afternoon
    with Dissolve(0.4) 
    $ autofocus.unblock("sayori")
    $ autofocus.unblock("yuri")
    $ say_transition = False

    "I quickly follow Sayori out of the room."
    show sayori turned casual md:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    mc turned casual thinking ml "So, what do you need help with?"
    s lup mh "Well, there is some stuff I need bringing down from my bedroom, and we need to set up the karaoke machine. Come on up and I'll show you the ropes." # im stuff
    show sayori ma
    mc mb ldown "Sure."

    if branches.is_current(branches.FEELINGS):
        show sayori ldown b2b e2a
        "My heart beats at the mention of Sayori's bedroom, like it's some pathetic, overly excitable schoolgirl." 
        _mc ec mh ba "Which frankly, I didn't think I was."

    else:
        _mc eh bg nb ma "Who would have thought, after all this time, Sayori'd be inviting me to her bedroom once again? A- Ahaha..."
        "I shake my head to brush off the creeping insecurities."
        show sayori ldown b2b e2a
        "I start up the stairs and see Sayori biting her lip."

    mc ea bg nb ml "You okay, Sayori?"
    s b1a e3d mb "Y- Yeah, I'm fine."
    show sayori ma
    "She regains her smiles and joins me."

    scene bg s_bedroom_afternoon with wipeleft
    camera master:
        align (0.8, 1.0) zoom 2.0
    with Dissolve(0.3)

    "As I enter her bedroom, I let out a laugh as I go over to pat Mr. Cow."
    _mc turned casual ec mh "I remember this..."
    mc ea ml "Is this still..."
    s turned casual mb "Yeah! I could never replace him!"
    mc ed md "Still as adorable as ever, I see~"

    if branches.is_current(branches.FEELINGS):
        camera master:
            align (0.5, 0.2) zoom 1.65
        show bg:
            blur 2.5
        show sayori md:
            matrixcolor TintMatrix("#f1d6bb")
            i11
        with Dissolve(0.2)
        $ autofocus.block("sayori")
        $ say_transition = True
        mc mb eg "Just as you are."
        s e2a b2b mb nb "Aww, you big lug~ We- Should bring the stuff down, now, though." # im stuff
        show sayori ma with say_dissolve
        mc ed md "Sure."
        show sayori lup b1a e3d me na with say_dissolve
        "But I can't resist giving her a kiss."
        "Her strawberry scent overwhelms me."
        "Her hair brushes slightly against my face."
        "I break away."

        show sayori e1a md
        show bg:
            blur 0.0
        camera master
        with Dissolve(0.2)
        $ say_transition = False

    else:
        camera master
        show sayori md:
            matrixcolor TintMatrix("#f1d6bb")
            i11
        with Dissolve(0.2)

    mc ea mb na ba "Come on, let's get moving before someone misses us."
    $ autofocus.unblock("sayori")
    s e2a b2a mb "Yeah, ehehe..."
    show sayori ma

    scene bg s_house_entrance_afternoon
    show natsuki turned casual noband md lhip:
        matrixcolor TintMatrix("#ffdfc0")
        i21
    show yuri turned casual:
        i22
        matrixcolor TintMatrix("#ffdfc0")
    with wipeleft_scene
    $ set_date(hour=17, minute=9)

    "When we walk back downstairs, I jump a little as I see Natsuki talking calmly with Yuri."
    n ldown e1d mh b1d "We thought you'd got lost in the closet with Sayori."
    show natsuki ma
    mc turned casual ed md "Not today."
    show sayori turned casual lup rup e3d mb:
        matrixcolor TintMatrix("#ffdfc0")
        t31
    show natsuki e1a b1a at t32
    show yuri at t33
    s "And now we have a room set up."
    show sayori ma
    y mb "Great."
    show yuri ma
    n cross e3c mi b3a "I think I'll be the judge of that."
    show natsuki ma e1a
    mc ea mb "Be my guest."
    show natsuki at thide
    hide natsuki
    show yuri at t22
    show sayori at t21

    scene bg s_living_room
    show natsuki turned casual noband b3a me at i11
    with wipeleft

    "Natsuki walks into the room which we decorated and, as much as she tries to hide it, I hear her gasp."
    show natsuki md at t32
    show sayori turned casual at t31
    show yuri turned casual md lup e1d at t33
    mc turned casual ed md "Did we pass?"
    n mg "I... I uh-"
    show yuri e1a ma
    show sayori mn e3d
    extend e2a lhip b1d mh " I don't think you failed."
    show natsuki md
    _mc ec ma "I feel that's the best I'll get from her."
    mc ea mb "I'll take that."
    n e1d mg ldown "You'd better."
    show natsuki md
    show sayori ma e1a
    y ldown e1d mb "It's lovely, well done both of you."
    show yuri ma
    mc eg "Thank you, Yuri~"
    play sound doorbell
    "We hear the bell ring once more."

    scene bg s_house_entrance_afternoon with wipeleft

    "As I move to open it, I spy snow adorning a high branch on Sayori's tree. Or maybe it was a bird."
    camera master:
        align (1.0, 0.55) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "Either way, I press on, opening the door."
    show monika turned coat_casual:
        xcenter 0.75 ypos 1.0 yanchor 0.95 zoom 0.7
        matrixcolor TintMatrix("#ffdfc0")
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "Monika, waiting on the other side, beams at me."
    m mb "Hi MC, fancy seeing you here!"
    show monika ed ma with say_dissolve
    mc turned casual ed md "I know, right? What a coincidence~"
    mc ea mb "Do come in!"
    m ea mb "Thank you~"
    show monika ma with None
    camera master
    hide monika 
    show bg:   
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("monika")
    $ say_transition = False
    "Monika brushes past me."
    "Her hair runs along my chest."
    _mc turned ec mh "Somehow, I feel that was deliberate."
    s turned casual mb "Hey Mon!"
    "I hurridly follow behind her as she takes off her coat, hanging it on the rack near the door."

    stop music fadeout 1.5
    scene black with Dissolve(2.0)
    pause 1.0
    play music pillow
    pause 1.5
    scene bg s_living_room
    show monika turned casual at i41
    show yuri turned casual at i42
    show sayori turned casual at i43
    show natsuki turned casual noband at i44
    with Dissolve(1.5)
    show cg sleepover 1
    hide sayori
    hide natsuki
    hide monika
    hide yuri
    with Dissolve(0.5, time_warp=_warper.easeout_quad)
    $ persistent.sleepover.mark_cg(1)

    _mc turned casual "Ah, the club's all here."
    _mc ec mh "Right on cue..." 
    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8 
    with cg_dissolve
    s turned casual mb "So, we're all here!" 
    camera master:
        anchor (1.0, 0.325) pos (1.0, 0.4) zoom 2.1
    with cg_dissolve
    n turned casual noband b1d mb e1d "How did you work that one out?"
    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8
    with cg_dissolve
    s e2a b1d mg "Meanie..."
    camera master:
        anchor (0.0, 0.325) pos (0.0, 0.4) zoom 2.2
    with cg_dissolve
    m turned casual mb "So, Sayori, what did you have planned for this eventide?"
    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8
    with cg_dissolve
    s e1b mh "Eventide? Huh?"
    camera master:
        anchor (0.3, 0.25) pos (0.48, 0.3) zoom 1.8
    with cg_dissolve
    y turned casual mh "It is an old English word for evening time, Sayori."
    y e3d mb "And a word I most certainly enjoy hearing being spoken."
    y b2a nb e2a mk "... Ah."
    "Her face brightens a tad."
    "She obviously thinks she sounds weird."
    camera master
    with cg_dissolve
    mc ea mb "I appreciate it too. It casts an image of a great spectral moon above a silvery lake."
    camera master:
        anchor (0.3, 0.25) pos (0.48, 0.3) zoom 1.8
    with cg_dissolve
    "Yuri looks a little less flustered."
    camera master:
        anchor (1.0, 0.325) pos (1.0, 0.4) zoom 2.1
    with cg_dissolve
    "Natsuki rolls her eyes, muttering something along the lines of 'Oh my god' under her breath, but I ignore her."
    camera master:
        anchor (0.0, 0.325) pos (0.0, 0.4) zoom 2.2
    with cg_dissolve
    m md "So yeah, what have you got planned?"
    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8
    with cg_dissolve
    s b1a e3d mn "Oh, uh, not much!"
    s e1a mb "Some party games."
    camera master:
        xpos 1.0 xanchor 1.0 zoom 2.1
    with cg_dissolve
    "Natsuki seems to perk up at that."
    n nb b3a e1a mh "L- Like what?"
    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8
    with cg_dissolve
    s mb "Well, I've got a few boardgames, {i}but{/i} I thought it'd be fun to let everyone pick a game!"
    camera master:
        xpos 0.0 xanchor 0.0 zoom 2.2
    with cg_dissolve
    m mb "That sounds fun!"
    camera master:
        anchor (0.3, 0.25) pos (0.48, 0.3) zoom 1.8
    with cg_dissolve
    y na e1a mb b1a "I think that would be enjoyable."
    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8
    with cg_dissolve
    s mh "So, what are we going to do first?"
    show monika ea ba na mc at i41
    show yuri e1a b1a ma at i42
    show sayori md lup at i43
    show natsuki e1a b1a ma na at i44
    camera master:
        xpos 0.0 xanchor 0.0 zoom 2.2
    with cg_dissolve
    "Everybody turns to Monika."
    hide cg
    camera master
    with Dissolve(0.2)
    m mb bb nb "Ahah, me?"
    show monika ma
    s ldown mc e3d "Yeah! You're the president!"
    show sayori ma
    m eb bc md na "Well then..."
    show natsuki md
    m lpoint ea ba mb "Why don't we do each-others' makeup? It might give us a chance to step out of our comfort zones."
    show monika ldown ma
    s e1b mb "Oooh! That could be fun!"
    show sayori ma
    _mc thinking ea mh "I've never really bothered with makeup before, beyond the basics... It could be fun to try? I've just never really had the time or need to learn..."
    _mc ec bi ldown "Though I can't help but feel it was a slight jab aimed in my direction. "
    show sayori e1a
    y mb lup "I think this could be most enjoyable."
    y shy mc eb bb "My knowhow of makeup is scanty, but I feel it might be nice to experiment for an evening."
    n cross e2a mg "S- Same here."
    show natsuki mj
    m md "Do you have makeup, Sayori?"
    show monika ed ma
    s lup mh "I have some upstairs, I think?"
    show monika ea
    s mb e3d "I'll go get it~"
    show sayori ma at rhide zorder 1
    hide sayori
    show natsuki at t33
    show yuri turned ma at t32
    show monika rhip md at t31
    m "So, Nat, ever worn make-up?"
    show monika mc
    n turned lhip b1d mm "N- No! Idiot! My skin is too sensitive!"
    m md "Really?"
    show monika mc
    show natsuki md ldown
    m eb md rdown "So you have no experience with makeup at all?"
    show monika ea mc
    show yuri lup e1d md
    show natsuki e1b b1a mi at hop
    n "I never said that! I {i}do{/i} have experience!"
    show natsuki mm
    show monika eb bb
    "Monika looks somewhat disappointed."
    m md "Does that mean you won't be joining us? I mean, you're implying you have no-"
    show monika ea ba mc
    show yuri e1a ma
    n cross e2a b1d mh "Like I said, I {i}have{/i} used makeup before! Just not always on myself."
    n e1a b3a mb "I was with the anime club, remember? I helped the others out with their cosplays all the time."
    n turned lhip e2a b1a mh "Having sensitive skin makes me quite in the know about what cosmetics to use and not use."
    show natsuki ma
    "At this point, Natsuki's outrage peters out, replaced instead by a certain... smugness."
    _mc ec mh ba "Though, I don't think she's {i}ever{/i} mentioned being part of the anime club before..."
    _mc ea "I was under the impression she'd never been part of a club before her time on the student council; that's what made her success all the more impressive by getting elected."
    show yuri ldown e1d me
    n b3a e1a mc ldown "In fact, I daresay I could teach all of you a thing or two."
    show natsuki ma
    "All eyes upon Natsuki sit somewhere between amusement and amazement."
    "Only then does Sayori's return break the silence."
    show monika ma at t41
    show yuri ma e1a at t42
    show natsuki at t43
    show sayori turned casual mc lup rup e3d at t44
    s "Wow! We had ourselves an expert all this time and we didn't know it!"
    s rdown e1a mb "I'd love to learn from you, and I'm sure everyone else would, too! Right, guys?"
    show sayori ldown ma
    y mb "Colour me curious."
    show yuri ma
    mc mg "Likewise. Monika?"
    show monika ed
    "Monika no longer looks disappointed. She flashes Nat an encouraging grin."
    m mb "Take it away, maestra. Wow us with your guidance."
    show monika ma
    n e3c b1a mg "I think I will."
    show natsuki e2a ma
    "There seems to be a subtle note of relief in Nat's voice beneath the bravado."
    _mc ec mh "But maybe it's just me."
    show sayori at thide
    show yuri at thide
    show monika at thide
    _mc ea "It does lead me to wonder why she's so eager, but..."
    show natsuki b1d
    _mc ma "Maybe she's just eager to show off her skills."
    hide monika 
    hide sayori
    hide yuri
    show natsuki e1d mb at t11
    n "Hah, time to show you all what I'm made of. Watch and learn!"
    show natsuki e3c mj at dip
    "Taking the box with a surprising gentleness, at least compared to her voice, she pries it open."
    show natsuki e1a b3a md with None
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ autofocus.block("sayori")
    $ autofocus.block("monika")
    $ autofocus.block("yuri")
    $ say_transition = True
    $ autofocus.zorder = False
    n b1d me "Hmm. It's a little basic..."
    n b3a mb "But I can make it work." 
    show natsuki ma with None
    show sayori turned casual me zorder 1:
        i22
        yoffset 50
    show natsuki:
        i21
        yoffset -20
    camera master:
        xalign 0.63 yalign 0.22 zoom 1.4
    show bg:
        blur 1.5
    with Dissolve(0.2)
    "Natsuki sits Sayori down on the couch, and prepares some foundation."
    camera master:
        zoom 1.6
    show bg:
        blur 2.0
    show sayori e3d md
    show natsuki e1d b1d md:
        xoffset 250 yoffset -12 matrixtransform RotateMatrix(0, 0, 4)
    with Dissolve(0.2)
    "Comparing the multiple shades to Sayori's skin tone, Natsuki settles on one and brings the piece of sponge to her face."
    n mg b3a e1a "Hold still, and let me work my magic..."
    show natsuki md b1a with say_dissolve
    "After she's done, she grabs a brush, gently placing some blush on Sayori's cheeks."
    camera master:
        zoom 1.4
    show bg:
        blur 1.5
    show natsuki b3a ma:
        matrixtransform RotateMatrix(0, 0, 0) xoffset 180 yoffset -20
    with Dissolve(0.2)
    n mc "See, if you accent the cheeks without overdoing it, it highlights other parts of the face."
    n e3c mh b1a "Too much blush looks weird, and too little? You're better off not trying at all."
    show natsuki ma with None
    hide natsuki
    show sayori mn:
        xoffset 200
    camera master:
        zoom 1.5 xalign 1.0
    show bg:
        blur 2.0
    show monika turned casual mc zorder 0:
        i11
        xoffset 220 yoffset 20 matrixtransform RotateMatrix(0, 0, 4)
    show yuri turned casual e1d md lup:
        i11
        xoffset -50 matrixtransform RotateMatrix(0, 0, 12)
    with Dissolve(0.2)
    "The other girls lean in, examining Natsuki's handiwork."
    y ldown e1a mb "Remarkable."
    show yuri ma
    m mb "You look like a different woman, Sayori."
    show monika ma with None
    hide monika
    hide yuri
    show natsuki turned casual noband b3a md:   
        i21
        xoffset 180 yoffset -20
    show sayori b1b e2c md:
        xoffset 0
    camera master:
        xalign 0.63 zoom 1.4
    show bg:
        blur 1.5
    with Dissolve(0.2)
    "After letting everyone admire her handiwork, she holds up a mirror to Sayori, who looks away, rather than into it."
    show natsuki e3c mj with say_dissolve
    "Natsuki pauses, then places the mirror down."
    show natsuki e2c b3a me zorder 0:
        xoffset 370 yoffset 0 matrixtransform RotateMatrix(0, 0, 8) matrixanchor (0.5, 1.0)
    show sayori lup e2a b1a md
    with Dissolve(0.2)
    "Leaning in, she appears to whisper something to Sayori, before continuing."
    show natsuki e1a md zorder 2:
        xoffset 180 yoffset -20 matrixtransform RotateMatrix(0, 0, 0)
    show sayori ldown e1a
    with Dissolve(0.2)
    n mh "Now for the eyes."
    show natsuki md with None
    camera master:
        zoom 1.6
    show bg:
        blur 2.0
    show natsuki me:
        xoffset 270 matrixtransform RotateMatrix(0, 0, 8)
    show sayori e3d
    with Dissolve(0.2)
    n mg b1d e1d "For this, there's a couple of parts. The eyeliner, which accents the shading of eyes."
    n e1a b3a mc "And mascara, which emphasises the eyelashes."
    n mh "Working together, they place an accent on the eyes in general, drawing attention to them, and the colour of your eyes and hair."
    show natsuki e3c b1a md with say_dissolve
    "Natsuki picks up an oddly shaped brush, and gently runs it along Sayori's eyelashes. As she does, the dark colour traces along the lines of her lashes, lending them a far greater presence than they had previously held."
    show natsuki ma e1a with say_dissolve
    "Finally, she takes another piece of sponge, dabbing it under Sayori's eyes and onto her eyelids."
    show natsuki:
        xoffset 180 matrixtransform RotateMatrix(0, 0, 0)
    camera master:
        zoom 1.4
    show bg:
        blur 1.5
    with Dissolve(0.2)
    n mh "Sometimes, you can use fancy colours for the eyelids, but they aren't always necessary."
    show natsuki ma with say_dissolve
    _mc ea bb mh "Wow, the change is pretty stark."
    _mc ef ba ma "Don't get me wrong, Sayori has her own charm, but this makes her seem a lot more..."
    _mc ed mh bm thinking "Mature?"
    camera master
    show bg:
        blur 0.0
    show natsuki:
        i43
        offset (0, 0)
    show sayori:
        i44
        offset (0, 0)
    show yuri turned casual e2a b1d at i42
    show monika turned casual mc at i41
    with Dissolve(0.2)    
    $ autofocus.unblock("monika")
    $ say_transition = False
    $ autofocus.zorder = True
    m lpoint md "Wow, that's honestly pretty impressive, Natsuki."
    show monika ldown ma
    $ autofocus.unblock("yuri")
    y lup mb nb "Y- You look good, Sayori. It really suits you."
    show yuri e1a ma b1a
    show sayori ma
    mc ea ba mb ldown "Honestly, it really brings out your eyes."
    m mb "It really does."
    show sayori e1a me
    show natsuki md
    show yuri na ldown
    m rhip md "Did you want to look, Sayori?"
    show monika mc
    $ autofocus.unblock("sayori")
    s lup mg "Oh, no, I'm-"
    show sayori me
    $ autofocus.unblock("natsuki")
    n e3c b3a mi "She can admire my professional-grade handiwork in her own time."
    show natsuki md with None
    show yuri:
        alpha 0.0
    show monika:
        alpha 0.0
    show natsuki e1a b1a ma at i21
    show sayori ldown b2c ma at i22
    camera master:
        align (0.5, 0.25) zoom 1.3
    show bg:
        blur 1.0
    with Dissolve(0.2)
    "Sayori seems to give a small smile to Natsuki." 
    "She must not be used to this type of attention, as even through the makeup she looks plenty uncomfortable."
    camera master
    show bg:
        blur 0.0
    show monika ma rdown:
        alpha 1.0
    show yuri:
        alpha 1.0
    show natsuki at i43
    show sayori b1a at i44
    with Dissolve(0.2)
    show yuri lup rup b2a e1b nb mk
    m mb lpoint "I think Yuri deserves some love and care." 
    show monika ma
    y shy ne "Mmmonika..."
    m ldown ed mb "Aww, come on Yuri, you'll enjoy it."
    show monika ma
    y nc eb ma bb "F- Fine."
    show yuri ma
    n lhip rhip e3d b3a mo "Great."
    camera master:
        xalign 0.37 yalign 0.19 zoom 1.4
    show bg:
        blur 1.5
    show sayori:
        alpha 0.0
    show monika:
        alpha 0.0
    show natsuki ldown rdown e1a ma:
        i22
        yoffset -20 xoffset -180
    show yuri turned e2a b1d ma lup nb:
        i21
        yoffset 50
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ autofocus.block("yuri")
    $ say_transition = True
    $ autofocus.zorder = False
    n mh "Yuri, how do you want to look?"
    show natsuki md 
    y b2b mg e2a lup "I- I..."
    show natsuki ma 
    y e1a mb b1a "I'll take whatever you can do."
    show yuri ma na ldown with say_dissolve 
    _mc eg ma ba "Ah, Yuri. Ever demure."
    n e2a mg lhip "Let's see, eh?"
    camera master:
        zoom 1.6
    show bg:
        blur 2.0
    show yuri lup e1b b2a me:
        matrixtransform RotateMatrix(0, 0, -8) matrixanchor (0.5, 1.0)
    show natsuki b3a e1a ma ldown:
        matrixtransform RotateMatrix(0, 0, -6) xoffset -250
    with Dissolve(0.2)
    "Natsuki leans into Yuri."
    n e3c mh "Don't worry, Yuri. Where it comes to styling, I don't bite."
    n mn "... Much."
    show yuri ldown ma b1a e2a:
        matrixtransform RotateMatrix(0, 0, 0)
    show natsuki ma:
        matrixtransform RotateMatrix(0, 0, 0)
    with Dissolve(0.2)
    "Yuri smiles a little."
    show natsuki e1a b1a md with say_dissolve
    "Natsuki retrieves a little lip gloss from Sayori's bag."
    show yuri e3c
    show natsuki b3a md:
        matrixtransform RotateMatrix(0, 0, -4)
    with say_dissolve
    "She slowly runs it over Yuri's lips as she closes her eyes."
    show natsuki me e1a with say_dissolve
    "I spy a slow, muted, slightly pinky gold run across Yuri's lips."
    show yuri me
    show natsuki ma b1a:
        matrixtransform RotateMatrix(0, 0, 0) xoffset -180
    camera master:
        zoom 1.4
    show bg:
        blur 1.5
    with Dissolve(0.2)
    "Yuri opens her lips a little and lets out a slight leak of air." 
    camera master
    show monika ea:
        alpha 1.0
    show sayori:
        alpha 1.0
    show bg:
        blur 0.0
    show natsuki:
        i43
        offset (0, 0)
    show yuri md:
        i42
        offset (0, 0)
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.zorder = True
    "As Yuri pulls back slightly, I am close to whistling at her."
    "Just changing her lips makes her look almost angelic."
    show yuri e1d md lup
    m md "Wooow Yuri."
    show sayori e3c
    m mb ed "You look beautiful."
    show monika ma
    show natsuki b3a me
    $ autofocus.unblock("yuri")
    y e2a mb "Eh, thank you..."
    show yuri e1d me
    show sayori e1a
    $ autofocus.unblock("natsuki")
    n lhip mc b1a "I'm not done with you yet!"
    show natsuki ma ldown
    y ldown mk e2a b2b "A- Ah..."
    camera master:
        align (0.37, 0.19) zoom 1.6
    show bg:
        blur 2.0
    show sayori:
        alpha 0.0
    show monika:
        alpha 0.0
    show natsuki me zorder 3:
        i22
        matrixtransform RotateMatrix(0, 0, -4) xoffset -270 yoffset -20
    show yuri e2a b1d ma nb:
        i21
        yoffset 50
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ autofocus.block("yuri")
    $ say_transition = True
    $ autofocus.zorder = False
    "Natsuki starts running a sponge with concealer over Yuri's face."
    y e1d b1a mg "Thank you.."
    show yuri md
    n e1d b1d mg "Shush now." 
    show natsuki e1a b1a me
    show yuri e2a b1d na
    with say_dissolve
    "As she reaches out and slowly brushes purple eyeshadow over Yuri's eyes with a deft hand."
    show natsuki e1d b1d mn:
        matrixtransform RotateMatrix(0, 0, -6) xoffset -300 yoffset -22
    show yuri e1d me b1a
    with Dissolve(0.2)
    "Natsuki leans down and places a hand on Yuri's cheek."
    show natsuki mg e3c b1a:
        matrixtransform RotateMatrix(0, 0, -5) xoffset -305 yoffset -30
    with Dissolve(0.2)
    "She leans into Yuri's ear and whispers."
    show natsuki md
    show yuri e3c ma
    with say_dissolve
    "Yuri nods and smiles at her."
    show natsuki ma with None
    show natsuki e1a b1a md:
        matrixtransform RotateMatrix(0, 0, 0) xoffset -180 yoffset -20
    camera master:
        zoom 1.4
    show bg:
        blur 1.0
    with Dissolve(0.2)
    "I might be mistaken, but I'm pretty sure Natsuki smiles back."
    _mc ea "It's nice seeing them happy like this."
    _mc ec "Bonding."
    camera master
    show yuri e1a:
        i42
        offset (0, 0)
    show natsuki ma zorder 2:
        i43
        offset (0, 0)
    show bg:
        blur 0.0
    show sayori lup e1b me:
        alpha 1.0
    show monika ea:
        alpha 1.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.zorder = True
    "When Natsuki pulls back, I see Yuri, her face both angelic and dramatic, her lips reflecting light and her eyes hidden from it, her irises twinkling."
    s mg "Wow Yuri!"
    s ldown e3d mb "Pretty!"
    show sayori ma
    show natsuki e2a md
    $ autofocus.unblock("yuri")
    y mb "Thank you all, but... most importantly, thank you, Natsuki..."
    show yuri ma with None
    camera master:
        xalign 0.37 yalign 0.19 zoom 1.4
    show bg:
        blur 1.5
    show monika:
        alpha 0.0
    show sayori:
        alpha 0.0
    show yuri:
        i21
        yoffset 50
    show natsuki:
        i22
        xoffset -180 yoffset -20
    with Dissolve(0.2)
    $ say_transition = True
    "Yuri just looks up at Natsuki."
    n cross mh "No sweat, Yuri."
    show natsuki md with say_dissolve
    "I wait for the snarky comment."
    _mc mh "But it doesn't come."
    "A small grin slips out of me."
    camera master
    show sayori:
        alpha 1.0
    show monika:
        alpha 1.0
    show bg:
        blur 0.0
    show yuri:
        i42
        yoffset 0
    show natsuki: 
        i43
        offset (0, 0)
    with Dissolve(0.2)
    $ say_transition = False
    show yuri md e1d
    $ autofocus.unblock("natsuki")
    n b3a mh "Oh, and Yuri?"
    show natsuki md
    _mc ea mh "Here it is..."
    y lup mg "Y- Yes?"
    show yuri me
    n turned lhip mh "I'd be happy to do some more makeup... If you want it."
    n mb b1d e3c "Not that you need it."
    show natsuki ma
    show yuri ma
    "Yuri's already brightened look reaches a mighty crescendo with her wide, almost blinding smile."
    y lup e1a mb "I'd love that."
    show yuri ma
    show sayori e1a
    n e1a b3a mc ldown "Great."
    n mh "How would you feel... about me doing your nails?"
    show natsuki ma
    y mb ldown "If you're doing it, I know it'll be spectacular."
    show yuri ma
    n e3c b1a mb "Thanks."
    n e1a mh "So pass me that hand."
    show natsuki ma with None
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    hide monika
    hide sayori
    show yuri e3c zorder 3:
        i21
        xoffset 100 yoffset 30
    show natsuki e2a me:
        i22
        xoffset -70
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ autofocus.block("natsuki")
    $ autofocus.block("sayori")
    $ autofocus.block("monika")
    $ say_transition = True
    $ autofocus.zorder = False
    "Yuri moves her hand onto Natsuki's lap." 
    camera master:
        xalign 0.9 zoom 1.3
    show sayori turned casual md:
        i44
        xoffset 50
    show natsuki b3a e1a me
    with Dissolve(0.2)
    n mh "Sayori, do you have any nail paint?"
    show natsuki ma
    s e3d mc lup "Yeah! Loads!"
    s e1a mb "I'll go get them!"
    show sayori ma
    n e3c b1a mb "Thanks."
    show natsuki ma b1a
    camera master:
        xalign 0.5 zoom 1.5
    hide sayori
    with Dissolve(0.2)
    "Sayori rushes out to grab the paint."
    camera master:
        xalign 0.1 zoom 1.3
    show monika turned casual:
        i41
        xoffset -50
    show natsuki e1a
    with Dissolve(0.2)
    mc ed md "So, Mon, are you going to have anything done whilst Natsuki is on a roll?"
    m md "Ahah, yeah, I might."
    show yuri nc 
    m ed mb "Considering how good Yuri looks, I think I'd be stupid not to." 
    show monika ma
    show yuri na
    n e3d b3a mb "Thanks, Monika~"
    show natsuki ma with say_dissolve
    "Natsuki seems genuinely happy at all the compliments."
    m ea mb "You deserve it."
    show monika ma
    y lup e1a mb "You do, you've managed to make little old me look somewhat pretty."
    show yuri e1d me
    n lhip rhip e3c mi "I'd say you look more than pretty."
    show natsuki mn with say_dissolve
    "I can't tell if that is Natsuki bragging or giving a compliment to Yuri."
    show yuri ldown e1a ma with say_dissolve
    "Yuri can't seem to figure out either, but she takes it well."
    show natsuki ma ldown rdown e1a b1a
    y mb e3c "I agree."
    y e1a "At risk of sounding like a broken record, you've done a lovely job."
    show yuri ma with say_dissolve
    s turned casual e1b mb "Ah! Here!"
    camera master
    show yuri zorder 2:
        i42
        xoffset 0 yoffset 0
    show natsuki:
        i43
        xoffset 0 yoffset 0
    show monika:
        i41
        xoffset 0
    show sayori ma lup e3d at i44 
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.zorder = True
    "Sayori hurries down the stairs carrying a make-up bag."
    $ autofocus.unblock("monika")
    m bc mb "Wow Sayori! You should be a robber with all of this makeup!"
    show monika ma
    $ autofocus.unblock("sayori")
    s e1d b1d mb "Nah, if anyone's the thief here, it's Nat. She's practically stolen the show with her styling talent!"
    show sayori ma ldown
    show monika ba
    $ autofocus.unblock("natsuki")
    n cross e3d b1d mb "H- Heh. Heh heh heh."
    show natsuki ma
    "Just why Natsuki has responded to Sayori's comment with the most forced laugh I've ever heard in my life, I simply cannot fathom, but she brushes it aside before anyone can dwell upon it."
    n turned b3a e1a mh "So, I feel like black with red floral designs would work wonders."
    show natsuki ma
    s b1a e1b mh lup "Ooh!" 
    show sayori rup mc e3d at hop
    s "I can help with that!" 
    show natsuki e2a b1a
    s ldown mb e1a "I love nail art!"
    show sayori ldown ma
    n lhip mh "That'd be helpful. Nails aren't my speciality."
    show natsuki md
    m lpoint md "Yeah, I bet nails rarely ever come up in cosplay."
    show monika ma ldown
    n b1d ldown mg "Y- Yeah."
    n e1a b3a mh "So, I'll do a base layer and Sayori will do the rest, okay?"
    show natsuki ma
    show sayori e3d
    $ autofocus.unblock("yuri")
    y mb "Yes, thank you."
    show yuri ma with None
    hide monika
    hide sayori
    show yuri e3c mg b1d:
        i21
        xoffset 100 yoffset 20
    show natsuki me:
        i22
        xoffset -70
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    $ autofocus.zorder = False
    "Natsuki carefully sweeps nail varnish over Yuri's nails as I see Yuri's chest rise and fall quickly."
    show yuri me with say_dissolve
    "Her breath shallow."
    show yuri nc md with say_dissolve
    "Her cheeks crimson."
    show natsuki b1a ma with say_dissolve
    "When Natsuki finishes, she gently taps Yuri on the hand."
    show natsuki mb with say_dissolve:
        xoffset -80 yoffset 10
    n "Wakey wakey."
    show natsuki ma with None
    show natsuki md:
        i43
        offset (0, 0)
    show yuri b1a e1d me na lup:
        i42
        offset (0, 0)
    show monika turned casual at i41
    show sayori turned casual at i44
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.zorder = True
    "Yuri opens her eyes and takes a moment."
    y mg "Thank you Natsuki... I- I..." 
    y b2b e2a mb nb "It means a lot to me."
    show yuri ma
    show natsuki ma
    "Natsuki holds her gaze fondly for a moment."
    s lup mh "Should I paint your nails now, Yuri?"
    show sayori ma
    _mc ea ma "Oh Sayori."
    _mc ef nb "Ever oblivious."
    y e1a mb "I- If you would."
    show yuri ma na
    s mn ldown e3d "Sure!" 
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    hide natsuki
    hide monika
    show yuri e1a b1a md ldown:
        i21
        xoffset 100 yoffset 20
    show sayori e3c me:
        i22
        xoffset -70 
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    "Sayori grabs Yuri's arm and retrieves a crimson polish."
    show yuri e1d me
    show sayori ma e1a
    with say_dissolve
    "She slowly runs it over Yuri's nail, gently flicking it up and moving it."
    "I can see Yuri marvelling at whatever she's doing."
    camera master
    show bg:
        blur 0.0
    show monika turned casual mc at i41
    show natsuki turned casual noband md at i43 zorder 2
    show sayori e3d:
        i44
        xoffset 0
    show yuri e1d me:
        i42
        xoffset 0
    with Dissolve(0.2)
    "When Sayori steps back, I gasp audibly."
    mc eb bb mg na "Sayori, that's beautiful!"
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    hide sayori
    hide natsuki
    hide monika
    show yuri at i11
    with Dissolve(0.2)
    "Yuri is sporting jet-black nails with crimson rose adornments."
    "They match her hair and compliment her pale skin."
    _mc ec ma ba "Like Lady Macbeth."
    _mc eg "A blood-soaked bat, one might say."
    show yuri shy nc ma ee bb with say_dissolve
    "I see Yuri flush with embarassment as she gazes into the small mirror Sayori's holding up." 
    show yuri at i42
    show monika turned casual mc at i41
    show natsuki turned casual md noband at i43
    show sayori turned casual at i44
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    show yuri nd
    m md "Yuri, you are absolutely gorgeous."
    show monika ma
    y ea "T- Thank you... but I'm sure you all look far more stunning than I."
    show yuri eb
    m rhip md "Seriously Yuri."
    m mb ed "Absolutely breathtaking."
    show monika ma rdown
    show yuri mc ea ba na
    "Yuri smiles back at us all sheepishly."
    show natsuki ma
    y "Thank you all."
    n cross e2a mh "Is what I do."
    show natsuki mj
    s mh "Is Monika going to have a go?"
    show sayori md
    m rhip bb eb mb "It'd be rude for me to say no at this point, no?"
    show monika ma 
    show sayori ma
    n turned lhip e3c b1d mb "Ha, alright. Leave it to me~ By the time I'm finished, you'll be so stunning that everyone in the room will be rendered speechless." 
    show natsuki ma
    show yuri eb
    m rdown ed mb ba "Am I not already?"
    show monika ma
    show natsuki e1b b3a nc mm
    "Monika gives a small wink to Natsuki, who suddenly turns a hue of red."
    n cross b1d e1b mh nd "Ah, well, I didn't say that you weren't..."
    n na e3c b3a mi "Ah, but!"
    n b1a e1a mb "What I'm saying is that I am a genius at this stuff, so I'll make you ultra stunning. Just leave it to me~" # im stuff
    show natsuki ma
    m mb "Ultra stunning is quite the promise, but I have full faith in you, Natsuki."
    m ea lpoint "Show me what you've got."
    show monika ma with None
    camera master:
        align (0.37, 0.19) zoom 1.4 
    show bg:
        blur 1.5
    hide yuri
    hide sayori
    show monika ldown:
        i21
        yoffset 50
    show natsuki turned me b1d zorder 3:
        i22
        yoffset -20
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ autofocus.block("natsuki")
    $ say_transition = True
    $ autofocus.zorder = False
    "Natsuki steps back, and considers Monika for a second."
    n mg e1d "Hmm."
    show monika mc
    n e3c md "..."
    "Natsuki looks a little troubled."
    m md "What's wrong?"
    show monika mc
    n e1a b3a mg "Oh, ah, nothing."
    n e2c mh "I'm just trying to decide what to do."
    show natsuki md
    m md "Well, aren't you just putting makeup on me?"
    show monika mc
    n b1d mg "Well yes, but..."
    n b3a e1a mh "There comes a point where makeup doesn't do all that much. It depends on the natural beauty of the wearer."
    show natsuki mj with say_dissolve
    "Monika blinks a few times, processing what Natsuki had just said."
    n e2a b1d mg "Hmm. Perhaps-"
    show monika md
    show natsuki e2b b1a nb md
    with say_dissolve
    "Then her eyes widened."
    show monika eb bb ma
    n e1b b3a mh "Oh, ah I mean-"
    n b1d e2c mm "I didn't mean it like-"
    m ec md bc "No, I know."
    show monika ea ba ma with say_dissolve
    "Monika composes herself, gently smiling at Natsuki."
    show natsuki md
    m mb "Regardless, I would like the makeup."
    show monika ma
    n mg na "O- Of course."
    n e3c md "..."
    camera master:
        zoom 1.6
    show bg:
        blur 2.0
    show natsuki e1a:
        matrixtransform RotateMatrix(0, 0, -7) xoffset -300
    show monika mc ec
    with Dissolve(0.2)
    "It was plain to see that Natsuki was still flustered, but she did as Monika asked."
    show natsuki b1a me with say_dissolve
    "Taking the sponge to Monika's face, she places a light layer of foundation onto it."
    show natsuki md with Dissolve(0.2):
        matrixtransform RotateMatrix(0, 0, 0) xoffset -180
    n "Hmm."
    n b3a mg "Maybe..."
    show natsuki me with Dissolve(0.2):
        matrixtransform RotateMatrix(0, 0, -7) xoffset -300
    "Taking a small amount of eyeliner, she does exactly as you'd expect; lines Monika's eyes."
    "As she does, the hue of her emerald eyes shines just a little brighter."
    show natsuki ma with None
    show natsuki:
        i43
        matrixtransform RotateMatrix(0, 0, 0) xoffset 0 yoffset 0
    show monika mc:
        i41
        xoffset 0 yoffset 0
    show yuri turned casual lup rup e1d me at i42
    show sayori turned casual md at i44
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "An application of blush later, and the club is left exactly as Natsuki described."
    "Speechless."
    camera master:
        zoom 1.6 align (0.27, 0.19)
    show bg:
        blur 2.0
    hide yuri
    hide sayori
    show monika ea zorder 3:
        i21
        yoffset 60
    show natsuki me:
        i21
        yoffset -40 xoffset 200
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ autofocus.block("yuri")
    "Natsuki didn't sit around admiring her handiwork for long though, as within a few seconds she'd already started on Monika's hair."
    show natsuki b1a mh with say_dissolve
    "Taking a hairband from the case, she politely asks Monika if she could remove her ribbon."
    show natsuki ma
    m mb "Ah, I don't see why not. After all, I'd be lying if I said I wasn't curious as to what you've been planning."
    show monika ma
    n e1d b1d mn "Hehe, just you wait."
    show monika nobow md
    show natsuki ma e3c:
        yoffset -47 xoffset 150
    with Dissolve(0.2)
    "A smug grin wider than her ears is worn upon her face, as her hands find themselves running through Monika's hair."
    n b3a mh e1a "Geez Monika, your hair's so soft!"
    show monika ma
    n b1a mc "What's your secret?"
    show natsuki ma
    m mb "Aha, now that'd be telling."
    show monika ed ma
    show natsuki e3d 
    with say_dissolve
    "It's pretty clear from their expressions that they're having a blast."
    show sayori turned casual lup rup e3c me:
        i21
        xoffset -130 yoffset 80
        matrixtransform RotateMatrix(0, 0, 9) matrixanchor (0.5, 1.0)
    show monika nb
    with Dissolve(0.2)
    "So too is Sayori, who had now leaned in to feel Monika's hair."
    show sayori ma ldown rdown e3d with NonBlockingDissolve(0.2):
        matrixtransform None
    s mb "Ooo~ It totally is!"
    show sayori ma 
    show yuri turned casual b2b e2a lup nb mb onlayer above_master:
        pos (0.95, 0.05) anchor (0.5, 0.1) zoom 0.8 * 1.6
        matrixtransform RotateMatrix(0, 0, -15)
    with NonBlockingDissolve(0.2)
    y "C- Come on, now, don't swarm Monika like that..."
    show monika na ea
    show yuri ma
    with say_dissolve
    "Monika looks at Yuri and smiles."
    m mb "Normally, I'd be with you, Yuri, but for tonight, let's just relax, shall we?"
    show monika ma 
    show yuri e1d me b1a
    s mh e1a "Besides, I want to know what your hair feels like!"
    s mb "C'mon, Yuri, it must be so soft!"
    show sayori ma
    show yuri e2c ma
    n e1a mc "Hah, it might give mine a run for its money."
    hide sayori
    hide natsuki
    hide monika
    hide yuri
    camera master
    show bg:
        blur 0.0
    show natsuki turned casual noband as natsuski:
        xcenter 0.65 ypos 1.03 yanchor 1.0 zoom 0.8
    show sayori turned casual e1d b1d as susyori zorder 3:
        xcenter 0.17 ypos 1.2 yanchor 1.0 zoom 0.8
    with Dissolve(0.2)
    "As Natsuki turns to face Yuri,"
    show sayori turned casual e3d b1a mn as susyori:
        matrixanchor (0.75, 1.0) matrixtransform RotateMatrix(0, 0, 0)
        easein 1.0 yoffset 20
        "sayori turned casual e3d mn lup rup"
        0.02
        parallel:
            ease_quad 0.7 matrixtransform RotateMatrix(0, 0, 200)
        parallel:
            0.3
            ease_quad 0.4 yoffset 220
        parallel:
            0.1
            easein 0.5 xcenter 0.57
    show natsuki as natsuski:
        0.2
        "natsuki turned casual noband md"
        0.8
        "natsuki turned casual noband e1b b3a mk nb"
        0.15
        matrixanchor (0.4, 1.0) matrixtransform RotateMatrix(0, 0, 0)
        parallel:
            easein_quad 0.6 matrixtransform RotateMatrix(0, 0, 90)
        parallel:
            0.15
            easein 0.45 xoffset 500 yoffset 150
    camera master:
        align (0.0, 0.6) zoom 1.0
        easein 1.0 zoom 2.0
        0.02
        parallel:
            easein 0.6 xalign 1.0
        parallel:
            easein_quad 0.6 yalign 1.0 knot 0.4 knot 0.45 knot 0.6 knot 0.9
        0.1
        ease_quad 0.6 yalign 0.8 zoom 1.35
    show bg:
        easein 1.0 blur 2.0
        1.6
        ease 0.8 blur 1.0
    show sayori turned casual lup rup e3d:
        zoom 0.8 matrixanchor (0.6, 0.6) matrixtransform RotateMatrix(0, 0, 100) 
        xcenter 0.78 ypos 1.0 yanchor 0.0
        1.6
        ease 0.7 matrixtransform RotateMatrix(0, 0, 0) yanchor 0.87
    show natsuki turned casual xd nb b3a mk zorder 3:
        matrixanchor (0.6, 0.6) matrixtransform RotateMatrix(0, 0, 100)
        zoom 0.84 ypos 1.0 yanchor 0.0 xcenter 0.85
        1.6
        ease 0.73 yanchor 0.85 matrixtransform RotateMatrix(0, 0, 0)
    extend " Sayori leaps at the opportunity, grappling Natsuki, holding her face to the back of Natsuki's head."
    hide susyori
    hide natsuski
    s mb "Ooooh! It smells so nice too!"
    show sayori ma
    n e2b ml "Ah-"
    n e1b mi "Wait, Sayori, what are you-"
    show natsuki mk
    show sayori mn e1d b1d
    with say_dissolve
    "As Sayori continues to tighten her grip, she forms a devilish grin."
    show sayori ldown rdown
    show natsuki nc b2a me
    with say_dissolve
    "Her hands slide down to Natsuki's sides."
    n mo nb e3d b2b "Wait, Sayori, plea- AHAHAHA!"
    show sayori ma with say_dissolve
    "Sayori unleashes her ticklish fingers upon the unsuspecting Natsuki, causing her to burst into laughter."
    show natsuki xd b2a nb mk
    show sayori e3c b1a me:
        offset (20, 5)
    with Dissolve(0.2)
    "After a few seconds, Sayori's assault slows, and she leans into her ear."
    s mb "I knew you were ticklish, ehe~"
    show natsuki e2d nd mm b1d
    show sayori ma
    with say_dissolve
    "Natsuki's face turns blood red, and she attempts to hide it behind her hands."
    camera master:
        align (0.0, 0.2) zoom 1.5
    show yuri turned casual lup e1d me zorder 3:
        i42 
        xoffset -100
    hide sayori
    hide natsuki
    with Dissolve(0.2)
    camera master:
        easeout_quad 0.3 xalign 0.3 zoom 1.2
    show sayori turned casual lup rup e3d:
        xcenter 0.45 ypos 0.0 yanchor 1.0 yzoom 0.8 xzoom 0.0
        parallel:
            ease_quad 0.3 xzoom 0.8
        parallel:
            easein_quad 0.3 ypos 1.03
    show yuri:
        0.08
        "yuri turned casual e1b b2a lup md nb" with Dissolve(0.2)
    "With everyone's attention on her, though, Sayori makes a secondary attack, practically teleporting to Yuri's side."
    s mb "Ehe, surprise~"
    show sayori ma with say_dissolve
    "Yuri, who had seen her coming, but had found herself powerless to stop her, simply sits still in a combination of horror and stunned confusion."
    show yuri e2b me b2b
    show sayori ldown rdown e3c me:
        offset (-70, 90)
    with NonBlockingDissolve(0.2)
    "Seizing the moment, Sayori latches onto a small tuft of Yuri's hair."
    s e3d mb "Ooo~ It totally is suuuper soft!"
    show sayori ma
    show natsuki turned casual noband e3c me:
        i41
        offset (100, -50)
    with Dissolve(0.2)
    "Natsuki, who by now has recovered from her embarrassment, places herself next to Yuri on the couch."
    n b3a mg e1a "Oh, you're totally right!"
    n e1d b1d mb "Well, if Monika won't tell us the secret, maybe you can!"
    show natsuki md e1a b2a
    show yuri e1d b2a md
    with say_dissolve
    "Natsuki looks at Yuri, her expression shifting from one of playfulness to one of genuine pleading."
    n mh "It would be really nice of you, Yuri?"
    show natsuki me with say_dissolve
    "With the softness of her voice, I'd almost have been convinced it might not have been her talking at all."
    y e2a b2b mk nc "Oh, ah..."
    show yuri me nd 
    show sayori md e1a
    show natsuki md
    with say_dissolve
    m turned casual md nobow bc "Come on, you two, you're making her uncomfortable."
    show natsuki e3c me b1d:
        offset (0, 0)
    show yuri e1a ma
    with Dissolve(0.2)
    "Natsuki sighs, a little, before brushing her clothes down and standing back up."
    show bg:
        blur 0.0
    camera master
    hide yuri
    hide natsuki
    hide sayori
    show natsuki turned casual b1d lhip e2a md at i42
    show monika turned casual nobow ba mc at i41
    show yuri turned casual e2a b2b ma nb lup at i43
    show sayori turned casual b2a at i44
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    $ autofocus.zorder = True
    n mg "You're right, as always, Monika."
    show yuri e1a
    n ldown e3c b3a mi "That was a little sudden."
    show natsuki md
    $ autofocus.unblock("sayori")
    s lup mb b1a "Yeah, I'm sorry Yuri, we just wanted to know, because imagine if we could get super soft hair too~"
    show sayori ma
    show natsuki ma e1a
    with None
    hide sayori
    hide yuri
    show monika ma:
        i21
        yoffset 30
    show natsuki me:
        i22
        yoffset -20 xoffset -180
    show bg:
        blur 1.5
    camera master:
        align (0.37, 0.19) zoom 1.6
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ autofocus.block("natsuki")
    $ say_transition = True
    $ autofocus.zorder = False 
    "Natsuki turns her attention back toward Monika."
    n mg "Right, now to finish this."
    show natsuki me zorder 1 with NonBlockingDissolve(0.2):
        xoffset -270 yoffset -30 matrixtransform RotateMatrix(0, 0, -2) matrixanchor (0.5, 1.0)
    "Taking Monika's hair, she bunches up small parts of it, and places them into a ponytail, one on each side of Monika's head."
    show natsuki e3c md with say_dissolve
    "Then, she takes some of the hair that wasn't collected, on each side, and drapes it over Monika's shoulders."
    show natsuki b3a ma e1a with say_dissolve
    "The result is so stunning that I almost forget to breathe."
    show sayori turned casual e1b me at i44
    show natsuki cross casual noband b1a zorder 2:
        i42
        offset (0, 0) matrixtransform None
    show yuri turned casual at i43
    show monika ma zorder 2:
        i41
        offset (0, 0)
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.zorder = True
    s mg "Woah..."
    s e3d mb "No wonder you're one of the idols of the school."
    show sayori ma
    $ autofocus.unblock("natsuki")
    n mc "I know, it is pretty impressive."
    show natsuki turned ma at dip
    show monika mc
    "Natsuki stands back and reveals her handiwork, including showing Monika in a mirror."
    $ autofocus.unblock("monika")
    m md "I..."
    m mb "I really do look like a completely different person."
    show monika ma
    s mb e1a "But not, at the same time!"
    s lup mh "It's like, if Monika got dressed up by a professional."
    show sayori ma
    $ autofocus.unblock("yuri")
    y lup mb "Yeah..."
    show yuri ma
    mc ea mg "Natsuki, that's just amazing."
    show natsuki e3c b3a
    mc eh md "I know you had a great base to work with, but who'd have thought that a change in hairstyle would make such an impact?"
    n mb "And now..."
    show natsuki ma with None
    camera master:
        align (0.5, 0.25) zoom 1.3
    show bg:
        blur 1.0
    show natsuki e1d b1d ma at i11
    hide sayori
    hide monika
    hide yuri
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ autofocus.block("sayori")
    $ say_transition = True
    "Natsuki turns to face me."
    _mc eb bd mh "Oh no."
    n mb "There's one left."
    show natsuki ma with say_dissolve
    mc ec ml ba "I may be in danger."
    n b3a mg e1a "Danger?"
    n b1d e3c mb "Never, I wouldn't hurt you."
    n b1a e2a mg "Much."
    show natsuki ma with None
    show natsuki e1d b1d ma
    camera master:
        zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "I unconsciously push myself back into my seat, as far away from the slowly approaching Natsuki as I can manage."
    n mb "Now, what to do?"
    show natsuki b1a e1a md with say_dissolve
    "Then she pauses."
    n b4 e1d mh "Actually, what do you want done?"
    show natsuki cross b1d e3c md with say_dissolve
    "Placing her hand to her chin, she thinks for a moment."
    mc ea "Well, I..."
    mc ef mg "I can't say I'm a huge fan of makeup, so..."
    show natsuki e1a b1a me with say_dissolve
    s turned casual mi e1b "Oh!"
    show natsuki me at i21
    show sayori lup rup mk at i22
    camera master:
        zoom 1.2
    show bg:
        blur 1.0
    with Dissolve(0.2)
    "Sayori springs from her chair."
    s xd ml "Waitwaitwait!"
    s rdown ldown mb b1d e2a "I know exactly what to do."
    show sayori mn
    show natsuki b1d ma e2c
    with say_dissolve
    "Natsuki turns to face Sayori, and the two of them exchange a glance."
    show natsuki turned e1d
    show sayori ma e1d 
    with say_dissolve
    "Suddenly, I'm even more scared than I was before."
    s b1a e3d mb "Ehe~ Come here, Melly. Don't worry, we won't bite..."
    show sayori ma:
        easein 0.5 yoffset 100 zoom 0.65
    show natsuki mn zorder 3:
        parallel:
            easein 0.25 yoffset 570
        parallel:
            easein 0.2 xoffset 240 zoom 1.6
    camera master:
        easein 0.4 yalign 1.0 zoom 1.3
    show black zorder 10:
        alpha 0.0
        easeout 0.26 alpha 1.0
    show bg:
        align (0.5, 0.8) zoom 1.0
        easein 0.5 blur 3.0 zoom 0.8
    $ advance_date(seconds=15) # comedy
    play sound ["<silence 0.1>", audio.fall]
    "It took them exactly fifteen seconds to subdue me with their combined strength."
    show cg sleepover 2 with cg_dissolve:
        on hide:
            alpha 1.0
            ease 0.4 alpha 0.0
    hide natsuki
    hide sayori
    show bg:
        blur 0.0 zoom 1.0
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    _mc ea mh "I have to say, Natsuki is surprisingly strong for her build."
    camera master
    hide black
    with NonBlockingDissolve(0.5)
    $ persistent.sleepover.mark_cg(2)
    _mc ef "Though, that may just be because she's sitting on my stomach."
    _mc ec "I'm currently lying on the ground, on my back." 
    _mc ea "Sayori is doing..."
    _mc ec "Something."
    _mc bi "Something involving my toes, I think."
    _mc eg "With Natsuki in the way, I have no way of knowing."
    n turned casual noband mn e1d b1d "Ehe~ Gotcha."
    mc ea bd ml "Don't imitate Sayori while you're straddling me, thanks..."
    n b3a e1a mh "Oh? Would you rather her up here?"
    mc ec bi mh "..."
    mc ef mf "No comment."
    camera master:
        align (0.48, 0.1) zoom 1.3
    with Dissolve(0.2)
    "Natsuki leans forward, just a little."
    n e3c mn "Well, sadly you're gonna have to make do with me~"
    n e1d b1d mb "I may not be as experienced, but please, show me the way, Melody..."
    _mc eb bd nb mh "Nope."
    _mc ec bi "Uh-uh."
    m turned casual nobow bc md "Natsuki, that kind of behaviour is highly..."
    camera master
    with Dissolve(0.2)
    n e3d b3a mo "Ah, it's all in good fun."
    "She turns back to smile at Monika, before returning to meet my gaze."
    n e1a mh "Besides, what's the worst that could happen?"
    n b1d e2c mc "MC's already proven herself to be chill, and Sayori and I mess around like this all the time."
    mc bd ea mg "All the time?"
    s turned casual mk nb e1b "Ah-"
    s e2a b2b me "Er..."
    "Sayori says something, at least attempts to, but with Natsuki in the way, I have no idea what expression she's wearing."
    n e2c mh b3a "Sayori, you almost done over there?"
    s e1a mg b1a "Ah, almost."
    n e3d mo "Sweet."
    n e1a mc "You're lucky, you know."
    "The smirk her face had been wearing this whole time widens into a grin."
    n e1d b1d mn "Most people would kill to have someone like me on top of them."
    show natsuki turned casual noband e1a b1a ma:
        xalign 0.5 ypos 1.03 yanchor 1.0 zoom 1.6 yoffset 500
        parallel:
            easein 0.4 zoom 0.8
        parallel:
            easein 0.3 yoffset 0
        0.2
        dip
    show bg:
        align (0.5, 0.1) zoom 1.3 blur 1.0
        easein 0.4 zoom 1.0 blur 0.0
    hide cg
    "And with that, she lifts herself up, offering me a hand as she does."
    hide natsuki
    show bg:
        align (0.6, 1.0) zoom 2.0
    show sayori turned casual lup rup mj e1b b1d:
        anchor (0.5, 0.4) matrixanchor (0.5, 0.4)
        pos (0.6, 0.85) matrixtransform RotateMatrix(0, 0, -40)
        zoom 1.2
    with Dissolve(0.2)
    $ say_transition = True
    "Glancing at Sayori, who was still crouching at my feet, I noticed something different about my toes."
    "Sayori's painted them."
    s b1a e1a mh "I figured, if you're not a fan of makeup, why don't we put it somewhere easy to hide if you want?"
    show sayori ma with say_dissolve
    mc nb ml ba "... That's... Actually pretty thoughtful of you two."
    hide sayori
    show natsuki turned casual noband at i11
    show bg:
        zoom 1.0 blur 2.0
    show layer master:
        align (0.5, 0.25) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.zorder = True
    $ autofocus.unblock("sayori")
    $ autofocus.block("natsuki")
    mc bd ea mg "Apart from sitting on me, you know."
    n lhip e3a b3a mn "Ehe~"
    show natsuki ma with say_dissolve
    "I shoot Natsuki a look."
    mc bi ec mj "Are you trying to break character?"
    n ldown e1d b1d mb "No, I just know now that it's really effective at messing with you." 
    show natsuki ma
    call close_eyes(duration=0.3) from _call_close_eyes
    "Shaking my head, I look around the room."
    hide natsuki
    show cg sleepover 1
    show layer master
    show bg:
        blur 0.0
    call open_eyes(duration=0.5) from _call_open_eyes
    $ autofocus.block("monika")
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    _mc ec mh ba na "Apart from Natsuki, everyone looks really nice. Not that they didn't before the makeup, but I totally understand why it's so common to wear it."
    _mc ea "I think a part of me regrets not acquiesing, but I can't shake off the feeling that it would feel wrong on me."
    camera master:
        anchor (0.0, 0.325) pos (0.0, 0.4) zoom 2.2
    with cg_dissolve
    m turned casual nobow mb ba "Alright, who's got any other ideas of what we can do tonight?"
    camera master:
        anchor (0.3, 0.25) pos (0.48, 0.3) zoom 1.8
    with cg_dissolve
    y turned casual mb "Well, as the host and the vice-president, I believe Sayori should go next."
    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8
    with cg_dissolve
    s turned casual e1b mg "Ah?"
    s me b1b e2a "Uh..."
    "Sayori seems to think for a moment."
    "The way her lips purse when she thinks hard is adorable, honestly."
    stop music fadeout 2.0
    s e1b mc b1a "Aha!"
    s e1a mb "Let's play Charades!"
    camera master:
        anchor (0.0, 0.325) pos (0.0, 0.4) zoom 2.2
    with cg_dissolve
    m md "Charades?"
    show monika turned casual ba ma at i41
    show yuri turned casual e1d ma at i42 
    show sayori turned casual e3d ma at i43
    show natsuki turned casual mh b3a at i44
    hide cg
    camera master
    with cg_dissolve
    play music elegant_s
    n "You mean the game where one person acts out something and everyone else tries to guess what it is?"
    show natsuki md
    show sayori lup rup mb at hop
    s "Yeah!"
    show sayori ma ldown rdown
    show natsuki b1a ma
    y e1a mb "Oh, a guessing game. That might be challenging."
    show yuri ma
    show sayori e1a
    $ autofocus.unblock("monika")
    m lpoint mb "Well, I don't see why not. Should we split up into teams?"
    show natsuki me
    show yuri md
    show monika ldown ma
    n cross b1d e2a mg "Hmm - With the odd numbers that might make it a little difficult."
    show natsuki e1a b1a me
    y e1d lup mg "Perhaps we should play a free-for-all?"
    y e1a mb ldown "Ergo, the first person to correctly guess receives a point, as well as the person who acted it out. First to five wins?"
    show yuri e2a ma
    show natsuki ma
    m ed mb "That sounds brilliant."
    show yuri e1a
    m md rhip ea "So, rules shall be, no calling out, just raise your hand and the person acting will point to you."
    show monika ma
    s mb "Sounds good."
    show sayori ma
    n turned mc "Yep, works for me."
    show natsuki ma
    show monika mc
    mc thinking ml "No complaints here. But who's first?"
    m rdown lpoint mb "Well it was Sayori's idea, so why not her?"
    show monika mc
    show natsuki md
    n b3a mh "Ah, but Sayori got her makeup done first."
    show natsuki mj
    m rhip bc ec md ldown "Good point."
    m ba ea rdown "Any objections if I go first?"
    show monika ma
    show sayori e3c
    show yuri lup e3c
    show natsuki b1a ma
    with None
    hide natsuki 
    hide sayori
    hide yuri
    show monika bc ec mc at i11
    with Dissolve(0.2)
    "With everyone agreeing, Monika rises and turns to face the rest of the club."
    show monika ma
    "After thinking for a moment, she smiles."
    show monika ea ba md at dip
    "Holding her hands out, she motions her hands in front of her, as if opening a book."
    show monika ma lpoint
    "Sayori's hand shoots straight up, and Monika points to her, letting her speak."
    s turned casual mb "It's a book!"
    show monika ec ma ldown 
    "Monika nods, then moves to the next motion."
    show monika ea mc lpoint
    "She then proceeds to hold out one finger."
    y turned casual e1d mg "Ah, so one word."
    show monika ec ldown at t41
    "Standing dramatically, she motions toward something imaginary in front of her, clasping her hands together like she might be holding something inside her grip."
    show monika ea bc rhip at dip
    "She then brings her hands down in front of her, as if she were driving a blade into something lying before her."
    show monika bb md rdown
    "After that, she glances around above eye level, reaching out and clasping at air for but a few moments."
    show monika nb mc: # breaking bad reference
        0.7
        "monika turned casual nobow ec nb md bb"
        matrixanchor (0.5, 1.0) matrixtransform RotateMatrix(0, 0, 0) 
        easein_bounce 0.7 ypos 1.2
        0.08
        easeout_cubic 0.6 matrixtransform RotateMatrix(0, 0, 80)
    camera master:
        align (0.0, 0.2)
        linear 0.7 zoom 1.4
        parallel:
            easein_bounce 0.7 yalign 0.5
        parallel:
            easein_cubic 0.5 zoom 1.8
        0.08
        easeout_cubic 0.6 align (0.6, 1.0) knot (0.1, 0.6) knot (0.2, 0.675) knot (0.3, 0.75) knot (0.4, 0.875) knot (0.5, 0.95)
    show bg:
        blur 0.0
        linear 0.7 blur 1.0
        easein 0.7 blur 2.5
    "Finally, she motions as if she'd been stabbed, clutching at her heart and throat, staggering here and there, before dropping to the floor in a heap."
    _mc thinking mh "It was all very dramatic, but what does it mean?"
    show black with NonBlockingDissolve(1.0)
    _mc ec "Dramatic..."
    _mc ea bd "What do I know of the dramatic?"
    _mc ba "The first thing to leap to mind might be the Drama Club..."
    _mc ef ma ldown "The Drama Club enjoys putting on plays; twice yearly they present something to the school, and in this case a book could be a screenplay in written form."
    _mc thinking mh ea "It might be something out of Shakespeare, if Monika was going for general knowledge. I can't see her picking something obscure; chances are she'd make it straightforward for the first round."
    _mc ec bi "Let's look at what actually happened, then - It looks like the main character killed someone, and then were killed themselves."
    _mc eg "Well, that {b}definitely{/b} doesn't narrow that down."
    _mc ea ba "If I look at the most commonly referenced plays for the sake of brevity, however-"
    _mc ec "Romeo and Juliet, Hamlet, A Midsummer Night's Dream, Much Ado about Nothing, I and II Henry IV, Macbeth-"
    _mc bb ma ea ldown "-Wait, that's it!"
    _mc ec bi "She specified a single word - It has to be."
    show monika ea ma ba na lpoint
    hide black
    with Dissolve(0.2)
    "Raising my hand, Monika points to me."
    show monika ed ldown with say_dissolve
    mc ea mb ba "It's Macbeth, isn't it?" 
    show monika mb ea rhip:
        parallel:
            easein 0.5 ypos 1.4
        parallel: # fix "offset" due to the focus
            warp autofocus.WARPER autofocus.DURATION xoffset -30
        0.1
        xcenter 0.5 ypos 2.0 xoffset 0
        matrixanchor (0.5, 0.75) matrixtransform RotateMatrix(0, 0, 50)
        ease 0.4 ypos 1.3
        0.08
        ease_quad 0.4 matrixtransform RotateMatrix(0, 0, 0) ypos 1.03
    show bg:
        0.5 + 0.1
        easeout 0.4 blur 0.0
    camera master:
        0.5 + 0.1
        easeout 0.4 zoom 1.0
    m "Ah, yes!"
    m ed rdown "Well done, MC. That was quite fast, especially considering my hints weren't exactly the most straightforward."
    show monika ma at thide
    mc mg "Well, once I'd nailed it down to the works of Shakespeare, it was a simple application of Occam's Razor."
    hide monika
    show sayori turned casual lup mh at t33
    show natsuki turned casual noband md at t32
    show yuri turned casual ma at t31
    s "So, now Melody can go, right?"
    show sayori ldown ma
    mc mb "Sure, I don't see why not."
    call close_eyes(duration=0.3) from _call_close_eyes_1
    "Replacing Monika in the centre of the room, I have a think."
    show natsuki me at i44
    show sayori at i43
    show yuri md at i42
    show monika turned nobow casual mc at i41
    _mc thinking eg mh "It'll have to be something that everyone at least has a chance of knowing."
    _mc bb eb "Oh!"
    call open_eyes(duration=0.25) from _call_open_eyes_1
    "Holding out my hand, I rotate it around an imaginary projector, as if to turn the wheel."
    show yuri e1d me lup
    "Yuri raises her hand, and I gently point toward her, giving her the chance to speak."
    y mg "A movie?"
    show sayori md e1d b1d
    show yuri ma e1a ldown
    "Nodding, I continue by holding up two fingers."
    show sayori me e1a b1a 
    n cross mc "Ah, so two words for this one!"
    show natsuki me with None
    camera master:
        align (1.0, 0.25) zoom 1.5
    show bg:
        blur 2.0
    show sayori:
        alpha 0.0
    show yuri:
        alpha 0.0
    show monika:
        alpha 0.0
    with Dissolve(0.2)
    "I give Natsuki a bit of a dirty look, then glance toward the others."
    camera master
    show bg:
        blur 0.0
    show natsuki at i44
    show sayori e2c md:
        alpha 1.0
    show monika mc:
        alpha 1.0
    show yuri e1d md:
        alpha 1.0
    with Dissolve(0.2)
    s lup mg "Natsuki, you have to hold out your hand, remember?"
    show sayori ma b2a ldown
    n turned e2a b2a mk nb "Oh! Sorry, everyone..."
    show natsuki md
    "As she looks downcast, I frown."
    _mc ea bg mh ldown "I didn't mean to upset her with that, only remind her of the rules without speaking."
    _mc ec bi mh "And as much as I would want to comfort her, she just got a little too into the game, I can't break character."
    "I decide to get it done quickly so I can cheer her up, unless Sayori notices and beats me to it."
    show sayori e1a b1a md
    show natsuki e1a b3a me 
    "Pulling my hands to my sides, I angle myself upward, as if in flight."
    show natsuki md na b1a
    "Then I land, pulling a sword from my hip."
    camera master:
        matrixcolor BrightnessMatrix(0.0)
        easeout 0.14 matrixcolor BrightnessMatrix(0.3)
        easein 0.14 matrixcolor BrightnessMatrix(0.0)
        0.4
        easeout 0.14 matrixcolor BrightnessMatrix(0.3)
        easein 0.14 matrixcolor BrightnessMatrix(0.0)
        0.1
        easeout 0.12 matrixcolor BrightnessMatrix(0.3)
        easein 0.12 matrixcolor BrightnessMatrix(0.0)
    "Swishing it around, I move forward and backward, I look back toward the others, who don't seem to have any idea yet."
    _mc bm ea "Hmm, this is harder than it looks."
    "I then take my hand and form it into a pinch, sprinkling it onto the air in front of me."
    "I then make the flight motion again."
    _mc ec ba "Still nothing."
    show sayori e1d b1d
    _mc ea "I must be doing something wrong."
    "I switch up my style, making an effort to change character, and waving my fist at the ceiling."
    show sayori e1a b1a me
    "As I do, I form my hand into the shape of a hook."
    show yuri lup rup e1b mk b2a nb
    show sayori ml lup rup e1b nb at hop
    "The moment I do, I see Sayori's hand shoot straight into the air."
    show yuri e2a ma na b2b rdown
    "Pointing to her, as she looks like she's ready to burst if I don't, she practically shouts."
    s b1a mh rdown na "Oooo!"
    show yuri ldown e1d me b1a
    s ldown e1a mb "It's Peter Pan!"
    show sayori e3d ma
    show monika md
    show yuri b1d e2a ma
    show natsuki b3a me
    "And a realisation washes over the others' faces."
    y mb na "Oh, it was flying you were simulating."
    show yuri ma
    n cross e3c b1d mm "And the sprinkling was pixie dust, of course!"
    show natsuki md
    m mb "Aha, well done, MC. It was just challenging enough to keep us all on our toes."
    stop music fadeout 2.0
    show monika ma

    scene bg s_living_room
    show monika turned casual at i21
    show yuri casual turned at i22
    with wipeleft_scene
    $ advance_date(minutes=12)

    "We continue our charades for a while, with Monika just beating Yuri, who takes it extremely well."
    y mb "Good game Monika. That was close."
    show yuri ma
    m mb "Quite. I look forward to playing again."
    show monika rhip md at t41
    show yuri e1d md at t42
    show sayori turned casual at t43
    show natsuki turned casual noband at t44
    m "So Yuri, it's your choice now."
    m mb "What are we going to do?"
    show monika rdown ma
    show yuri b2b e2a ma
    "A shy smile creeps around Yuri's lips."
    y mb "I-I don't know how easily you will all agree to this but..."
    show natsuki me
    show monika mc
    show sayori md
    
    play music ahog

    y e1d b1a mg "What about Never Have I Ever?"
    show yuri ma
    _mc turned casual ec mh "That's... alcohol, right?"
    s mh "That could be fun..."
    show sayori ma
    show natsuki e2a b1d mm
    "Natsuki curses under her breath, but makes no objections."
    n mg "Oh, boy..."
    show natsuki md e1a b1a
    show sayori md
    show yuri lup me
    m bb mb nb "Err... sorry for sounding stupid, ahaha, but what is it?"
    show monika ma
    "Everybody looks at Monika."
    _mc ma "Apparently {i}Yuri{/i} is less sheltered than Monika."
    show monika ba na mc
    y e2a mb "It's where somebody states something they have never done, and anybody who has done that... uhh... takes a shot."
    show monika md
    show yuri ma ldown
    "Monika's mouth takes one out of Sayori's book."
    _mc ea "A perfect circle."
    m eb "Oh."
    show monika mc
    s mb "Yeah, it's a fun drinking game where you learn all sorts of stuff about people." # im stuff
    show sayori me
    n e1d b1d mb "Yeah, but you can also use it to mess with people."
    show natsuki ma
    "Sayori glances around the room, clearly thinking."
    show natsuki md e1a b1a
    show yuri e1a 
    show monika ea
    s mg "But we won't do that."
    s lup mb "We're better than that, right everyone?"
    show natsuki ma
    s rup e3d "Besides, it's all in good fun."
    show sayori e1a ldown rdown ma
    show natsuki e2c md
    mc mb "I agree, it'll be a chance to learn things that we otherwise wouldn't."
    y lup mb "Y-yeah. It'll be fun, Monika."
    show yuri ma
    $ autofocus.block("monika")
    m "..."
    $ autofocus.unblock("monika")
    m ec md "If everyone else says so, I suppose it can't be all that bad."
    show monika ea ma
    s e3d mn "Yay!"
    "Across the room, I notice only one person still seems to have doubts:"
    extend " Natsuki."

    if not branches.is_current(branches.SNARED):
        _mc mh thinking "I wonder why? Maybe she's not a big drinker."
    else:
        $ advance_date_str("I wonder why? Maybe she's not a big drinker.")
    
    s e1a mb "Ooo~ I have just the thing. Wait here, everyone!"
    show sayori ma at thide
    hide sayori
    show natsuki e1a at t33
    show yuri ldown at t32
    show monika at t31
    "Sayori scurries away, a gleeful expression written on her face."
    "I'd be lying if I said I wasn't at least a little concerned, but this is Sayori, so what's the worst that could happen?"
    show natsuki at t44
    show yuri at t42
    show monika at t41
    show sayori turned casual lup e3d at t43
    "Sayori marches back in, carrying a bottle of..."
    mc mf "Is that rum?"
    s rup mn "Yep!"
    s rdown e1a mb "It's really good!"
    show sayori ldown ma at dip
    "While I have my doubts, as to the other club members, at a quick glance, I shrug."
    _mc ldown mh "Honestly, I was expecting worse."
    _mc ec "At least it wasn't vodquila."
    show natsuki ma
    y mg e1d "S- So, who wants to go first?"
    show yuri ma
    mc mb ea "Sure, I can go first."
    show yuri e1a
    show sayori md
    show natsuki md
    "Everyone glances in my direction."
    mc ml "Ah..."
    "On second thought, maybe I shouldn't have run my mouth."
    "Considering how intently they're looking at me, it makes me a little nervous."
    mc ef bi mf "How about..."
    show monika mc
    mc ea mg ba "Never have I ever cheated on a test."
    show sayori lup ma
    show natsuki b3a me
    show yuri md
    "Looking around the room, I see a glass raised."
    mc bb eb mg "Sayori!"
    show sayori e3d mn
    mc ea bd "What the hell? When?"
    show yuri ma
    show natsuki md
    s ldown mb "Ehe~ It was back in middle school. Remember that test that we worked really hard on?"
    show sayori ma
    mc mb ba ea "Oh, that maths one? I do. We had a challenge, and the winner would buy the other lunch for a week."
    mc ec bi mf "Wait..."
    mc ea bd ml "You didn't."
    show sayori mn e3d
    hide natsuki
    hide monika
    hide yuri
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    show sayori at i11
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("sayori")
    mc mg eb nb "Sayori, I failed that test!"
    mc ba ea na ml "And you're telling me that you got the second best score in the class because you cheated?"
    mc mg bd "I bought you food for two weeks because I was so impressed!"
    s e3a mb "Surprise!"
    s mg lup e2a "Technically, I did pass the test though."
    show sayori ldown e3d ma with say_dissolve
    mc ec bi mh "..."
    "My eyebrow twitches, just a little."
    "Then I sigh."
    camera master
    show bg:
        blur 0.0
    show monika turned casual ec rhip md at i41
    show sayori at i43
    show natsuki turned casual noband at i44
    show yuri turned casual at i42
    with Dissolve(0.2)
    $ say_transition = False
    show monika eb mc
    mc mj eg "Fiiine. Well played."
    show monika rdown 
    $ autofocus.unblock("sayori")
    s mb "I know. I got free food from you for two whole weeks. All that saving let me buy the fancy outfit I wore to the dance that year."
    show sayori ma
    mc ea ml ba "Wait, you saved up to buy that?"
    show sayori e1a
    mc eg mb "Man, that red dress was great! It really suited you."
    s e3d mn "And all the boys in our grade knew it, ehe~"
    show yuri md
    show natsuki me
    show monika ea
    s lup b1d e1d mb "But I think we've got bigger fish to fry, here."
    show sayori ma
    show natsuki md
    "Both Yuri and Natsuki look at her, confused."
    s ldown b4 e1a mh "Did all three of you miss it?"
    show sayori md with None
    hide sayori
    hide natsuki 
    hide yuri
    show monika md nb
    camera master:
        align (0.0, 0.2) zoom 1.6
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ autofocus.block("monika")
    $ say_transition = True
    "I glance toward Monika, who's eyes have opened wide."
    $ autofocus.block("sayori")
    show monika mc at i21
    show sayori turned casual e1d b1d at i22
    camera master:
        zoom 1.37 xalign 0.5
    show bg:
        blur 1.5
    with Dissolve(0.2)
    s mb "Someone else was drinking."
    show sayori ma
    m rhip eb mb "I... don't know what you're talking about, Sayori."
    show monika ma na
    s e3d mn b1a "Oh don't play dumb with me~ I saw you drink while everyone else was watching me."
    show monika mc
    s e3a mb "Clever, but not clever enough."
    show sayori ma e1a
    m ec md bc "I... just wanted to taste it, you know?"
    show monika ea ba mc rdown with say_dissolve
    n turned casual noband b1d e3c mb "Hah, a likely story."
    show natsuki cross casual noband b1a e1a ma:
        i33
        xoffset -50 
    show sayori at i32
    show monika:
        i31
        xoffset 50 
    camera master:
        zoom 1.2
    show bg:
        blur 1.2
    with Dissolve(0.2)
    "Natsuki joins in on the interrogation."
    n turned e3c mh b1d "Look, I don't want my partner here to get rough..."
    show natsuki lhip b1a e2a ma
    show sayori lup rup b1d e3d
    with say_dissolve
    "She motions to Sayori, who makes a big show of looking tough."
    n ldown b3a mc e1a "But I think you'll find me a lot easier to deal with."
    show sayori me b1a e1a
    show natsuki me
    m ea md bc "Or, we can just drop it and change the subject?"
    show sayori ldown rdown e2c md
    show natsuki e2a
    show monika mc
    with say_dissolve
    "The hint of forcefulness causes the playful act between Natsuki and Sayori to drop, as they look at each-other."
    show sayori e2a 
    n rhip e2c mg "It's not like we need explanations of why you drink anyway, so..."
    show natsuki md with None
    camera master
    show bg:
        blur 0.0
    show natsuki rdown e1a b1a md:
        i44
        xoffset 0
    show sayori e1a at i43
    show yuri turned casual md at i42
    show monika eb ba:
        i41
        xoffset 0
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    n mh "Who's next?"
    show natsuki md
    y mb "I- I'd like a go."
    show natsuki me
    show monika ea
    y mh e1d lup "Never have I ever been someplace where I wasn't supposed to be."
    show yuri ma e1a
    _mc ef bg ma na "Ah, crap."
    hide yuri
    hide monika
    hide natsuki
    camera master:
        align (0.5, 0.2) zoom 1.7
    show bg:
        blur 2.5
    show sayori lup e3d mg at i11
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    $ autofocus.zorder = False
    "I glance toward Sayori, and the two of us raise the shot glasses to our mouths, downing them."
    show natsuki turned casual lhip noband e3c b1d me at i22
    show sayori e1a md ldown at i21 zorder 3
    camera master:
        zoom 1.37
    show bg:
        blur 1.5
    with Dissolve(0.2)
    "What surprises me more, however, was that Natsuki did the same."
    show natsuki e1a b1a md ldown
    s lup mg "Hey, Natsuki, why did you drink?"
    show sayori md
    n e2c mg "I-"
    n b1d e1d lhip rhip mh "I could ask you the same question."
    show natsuki md
    s mg "Well, Melody and I climbed a lot of trees as kids."
    show natsuki e1a b1a
    s ldown mb "I'm guessing you did the same?"
    show sayori ma
    n rdown e2a mg "Ah, yeah. Basically."
    show natsuki md with say_dissolve
    "I'm not convinced, but as Natsuki had mentioned, in defence of Monika, it's best not to pry too much when someone's uncomfortable. The game's supposed to be fun, after all."
    camera master
    show bg:
        blur 0.0
    show natsuki e1a ldown at i44
    show sayori at i43 zorder 2
    show yuri turned casual at i42
    show monika turned casual at i41
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.zorder = True
    show yuri me e1d
    show natsuki b1d me e1b
    $ autofocus.unblock("monika")
    m mb lpoint "Never have I ever stolen something worth more than ten bucks."
    show monika ma ldown
    $ autofocus.unblock("natsuki")
    n mk "Wha- when did your go start?"
    show natsuki e1a mm
    show yuri e1a ma
    m ed mb "Just now. So?"
    show monika ea ma
    show natsuki md nb 
    show yuri md
    "Natsuki's eyes darted from Monika to her shot glass."
    show natsuki me e3c me at dip
    show monika mc
    show sayori me
    "After a few seconds, she downs the shot."
    show natsuki md
    "I don't think anyone could have missed Natsuki's movement."
    show natsuki nc mm e2a
    "In fact, Natsuki looks pretty self-conscious about it."
    n e1a mg na "What?"
    n mm e1b nd b3d "Why is everyone judging me?"
    show natsuki mj
    m md nb "Natsuki, are you al-"
    show monika mc
    n cross nb e3c mh b1d "I'm fine, alright?"
    n e2a b1a mg "Please, can we just move on?"
    show natsuki md na
    "Her bubbly attitude evaporated in an instant."
    _mc ec ba mh "It's a shame too, so far it looked like she'd been having a blast."
    show yuri ma
    n mg "I think I'll go next."
    show natsuki md
    show sayori ma
    show monika na
    "Brushing aside her sombre attitude, she pipes up again."
    m md "Alright, have at it, Natsuki."
    show monika ma
    n turned b3a e3c mi "Never have I ever..."
    show monika mc
    show sayori md
    show yuri md e1d
    n lhip b1d e2a mg "Kissed someone."
    show natsuki md
    m md "What, you're saying you've never kissed anyone?"
    show monika mc
    show natsuki nc e1b ldown me
    y mg "Honestly, that doesn't surprise me."
    show yuri md
    n mk nd "Wh-"
    n nb lhip b1a e2a mg "Well, I just haven't found the right person yet, alright?"
    show natsuki md with None
    hide natsuki
    hide yuri
    hide monika
    camera master:
        align (0.75, 0.2) zoom 1.7
    show bg:
        blur 2.5
    with Dissolve(0.2)
    "Meanwhile, Sayori and I steal a quick, inconspicuous glance at each-other."

    if branches.is_current(branches.FEELINGS):
        _mc ec mh ba "Well, what do we do?"
        _mc eb bd nb "We were literally making out hours ago before everyone arrived."
        _mc eg mm bi "Hell, after everyone arrived, in her room!"
        _mc eb bd "Not to mention we've slept together!"
        show sayori ma with say_dissolve
        "I motion to Sayori."
        _mc ec ba na mh "Looks like we don't have a choice, so we'll do it separately, and hope that it's enough to distract them."
        camera master
        show natsuki turned casual noband me e1b b1d at i44
        show yuri turned casual lup me e1d at i42
        show monika turned casual md at i41
        show bg:
            blur 0.0
        with Dissolve(0.2)
        "Biting the bullet, I bring the shot to my mouth and down it."
        "As I do, I see the mouths of most of the club members drop open."
        m mb "No, really?"
        show monika ma
        n mg "Who was it?"
        n e1a mh "Was it good?"
        show natsuki b1a md
        y lup b2a e2a mb "Now, we shouldn't bombard her with questions."
        show yuri ma with None
        camera master:
            align (0.05, 0.15) zoom 1.7
        show sayori lup mg e3c:
            blur 2.0
        hide monika
        hide yuri
        hide natsuki
        with Dissolve(0.2)
        "As they speak, I see Sayori out of the corner of my eye bringing her own shot to her mouth."
        show natsuki turned casual noband b1d md at i44
        show sayori:
            i11
            blur 0.0
        show bg:
            blur 2.0
        camera master:
            align (1.0, 0.25) zoom 1.6
        with Dissolve(0.2)
        "Natsuki, who's been sitting next to her, pauses."
        show natsuki e2a with say_dissolve
        "She looks at Sayori."
        show natsuki e1a me with say_dissolve
        "Then at me."
        show natsuki b1a mg with say_dissolve
        "She opens her mouth, and as she does, I shoot her a pleading glance."
        show natsuki me
        show sayori md ldown
        with say_dissolve
        "Then pauses again."
        show natsuki ma
        show sayori e1a md at i43
        show monika turned casual at i41
        show yuri turned casual at i42
        camera master
        show bg:
            blur 0.0
        with Dissolve(0.2)
        n mb e1d b1d "Wow, look at you, all popular."
        n cross e3c b3a mi "I'll bet they were really lucky, whoever they were."
        show natsuki e3a ma
        "She then subtly winks at me."
        show natsuki e1a
        show sayori ma
        _mc ma "Ha, I knew I could count on her."

    else:
        _mc ea ba mh "What do we do?"
        _mc ec "It's not like we can just pretend it didn't happen, right?"
        show sayori md e2a with say_dissolve
        "I glance at Sayori again, who's now looking away."
        "She seems to have no intention of drinking."
        _mc ea mf "Wait, don't tell me..."
        _mc bg mh "Don't tell me she doesn't consider what we had to be a kiss?"
        _mc eb mf "No way."
        hide sayori
        camera master
        show bg:
            blur 0.0
        show black
        with Dissolve(0.2)
        "Glancing at the floor, I almost kick myself."
        _mc eg bi ma nb "Ha, of course she doesn't think that."
        _mc bg ef "I mean, it was in middle school. Who counts that?"
        _mc mh "And it was with her best friend."
        _mc eg bi ma "Of course it doesn't count."
        "..."
        "I honestly can't help but feel disappointed."
        camera master
        show monika turned casual at i41
        show yuri turned casual at i42
        show natsuki turned casual at i44
        show sayori turned casual at i43
        hide black
        with Dissolve(0.2)

    "After a few seconds, I speak up."
    show natsuki turned b1a
    mc ea ba na mb "I think that means it's Sayori's turn?"
    $ autofocus.unblock("sayori")
    s mb "Ooo~ It is too!"
    s b1d mj e3c "Hmmmm."
    s e1b lup mb b1a "Oh! I've got it!"
    show sayori e1a ma ldown
    _mc ma "That was awfully quick."
    show yuri md
    s mb "Never have I ever had any pets!"
    show sayori ma
    _mc ec "Huh. That's both exactly what I expected and completely opposite to what I expected."
    _mc ea mh "As... expected? Of Sayori?"
    show natsuki lhip me e3c at dip
    show yuri me lup e2a b1d
    "Glancing around the room, I see Natsuki take another shot, and I see Yuri clam up a little."
    show natsuki ldown e1a md
    y e3c mg "Uuuu~"
    show yuri ldown b1a e3d me at dip
    "Bringing the shot to her mouth, she pours it in, throwing her head back."
    show yuri e3c b1d md
    "She shakes her head, probably in an effort to keep it down, then looks back to everyone."
    show yuri e1d b1a
    mc mf "Huh."
    y b4 mg "What is it?"
    show yuri b1a me
    mc ml thinking "Oh, nothing, I just realised that you almost went an entire round without drinking."
    y b2b mb e2a "I'm sorry that I'm boring..."
    show yuri e1a b1a md
    n b3a mh "Not at all!"
    n lhip b1d e2a mb "Hell, I drank almost every round. That doesn't mean my life is interesting."
    n ldown b3a e3c mi "It just means that we live different lives to one another."
    show natsuki e1a ma
    y e2a nb b1d mg "Yes. R- Right."
    show yuri md
    "A moment passes."
    show yuri na e3c
    "Then, just as we're about to move on..."
    show natsuki md
    show monika mc
    show sayori md
    y me lup "It was a raven."
    show yuri md
    "..."
    n b1d mg "Say what."
    show natsuki mj b1a
    y e2a b1a mg "He came to me one dreary winter's day, tapping upon my room's windowpane while I sat by it, curled up with a book and a cup of chamomile."
    y e1d mh "And I could not help but let the poor thing in; it was freezing outside."
    y e2a mg "Black as the ace of spades, he was, but for a splash of white upon the nape of his neck and his back."
    y mb e3c "He gratefully ate every crumb I had to offer, and offer him I did aplenty, for days and weeks after that."
    y mh ldown e1d "And would you believe how he showed his gratitude? He brought me gifts, that's how."
    show natsuki md
    y e1a mb "Shiny buttons, insect wings, feathers, a loose coin or two, even little seashells."
    show sayori ma
    y e3d "I still have them all tucked away in a little box. Happy memories of the bond I shared with such a beguiling creature."
    show yuri ma
    "All this while, we have been listening to Yuri's narrative in dumbfounded silence."
    "Then Monika breaks it."
    show yuri e1d md
    m md "What happened to him, Yuri?"
    show monika mc
    show yuri ma e2a b1d
    "Yuri smiles wistfully."
    y mb "As unexceptional as it sounds... one grey dawn, his visits just stopped. And I haven't seen him since."
    y e3c b1a mg "I'm not sad that it's over, though. I'm grateful that it happened."
    y e1a mb "Grateful that I was granted the opportunity to touch what seemed to be the edge of a magical world."
    y e1d mh "They say the souls of poets, artists and dreamers sometimes return as ravens. Perhaps that was just what he was - a dark muse, come soaring out of the chill air to inspire and enrich me."
    y e3d mb "Goodness knows I penned many a poem and a story based on what happened."
    show yuri ma
    "Silence reigns once again. An almost awed silence."
    show natsuki e2a
    "Until a sotto voce comment emanates from a corner of the room."
    show yuri e1a
    n cross mh "He'll be with you always, Yuri."
    show yuri e1d me
    n e1a mb "Or should I say... evermore."
    show natsuki ma
    show monika ma
    "Yuri's expression is a mix of surprised, happy and touched."
    y b1d e2a mb "I can never get your limits, Natsuki." 
    show yuri ma
    n e3c b1d mb "Heh. Who's to say I have any?"
    show natsuki e3d b3a ma
    show sayori e3d
    show yuri e3d b1a 
    show monika ed
    "We all laugh, and the moment passes."
    show natsuki turned e1a
    show monika ea
    show yuri e1d
    s e1a mb "Shall we try and get in two more rounds before we change the game?"
    show sayori ma
    m mb "Sounds like a plan."
    show monika ma
    _mc ec mh ldown "Hmm."
    _mc ea "I feel we should try and give Yuri some..."
    _mc eg ma "Or... no. I'll give her an easy one. Natsuki's up next, she is sure to give Yuri one. I'll give a 'blank'. No way anyone has done this, and if they have, it'll be all the more surprising."
    show yuri md
    mc ea mb "Never have I ever... rapped."
    "I glance around at all of us."
    hide monika
    hide sayori
    hide natsuki
    show bg:
        blur 2.5
    camera master:
        align (0.25, 0.1) zoom 1.7
    show yuri e2a b1d me lup
    with Dissolve(0.2)
    "And spy Yuri attempting to subtly down her shot."
    _mc bd nb eb mh "Yuri?!"
    camera master:
        align (1.0, 0.2) zoom 1.4
    show natsuki turned casual noband b3a me at i44
    show bg:
        blur 1.5
    with Dissolve(0.2)
    "Natsuki sees her as well."
    camera master
    show yuri at i42
    show monika turned casual at i41
    show sayori turned casual at i43
    show bg:
        blur 0.0
    with Dissolve(0.2)
    show yuri md e2b b1a nb
    show sayori md
    show monika mc
    n mg "What? Yuri?"
    show yuri e1b me ldown
    show natsuki md
    "She puts her shot glass down."
    y e1d b4 mg "W-What?"
    show yuri na me
    "Everybody looks at her incredulously."
    n b1d mg "W- When?"
    show yuri md
    show natsuki md
    y lup nb mb e2b b1a "W- Well that raven I talked of? Legrand? Well, rapping and high pitched whistling would get it to sleep. For my own personal sanity, I opted for the former."
    show sayori ma
    y e3c b1d na mh "Not to mention all the stray cats and dogs whistling attracted..."
    show yuri mj
    n mg b1a "S- Stray cats?"
    n mh b1d "Were any of them ginger with green eyes?"
    show natsuki md
    y ldown e1a mb b1a "Yes, actually, why?"
    show yuri md
    n e2a mg "N- No reason..." 
    show natsuki md
    show yuri b4 e1d
    "Yuri throws her a questioning look but doesn't push it further."
    show monika ma
    y b1a e1a mb "So yes, I had to learn to rap."
    y e1d mh "It's more poetic than you'd think."
    show yuri me
    m ed mb "Well I think that means we need to get Yuri up for karaoke later."
    show monika ma
    show yuri e2a nc ma
    "Yuri looks flustered but I see her mouth curl slightly."
    _mc ec ba na ma "She must be very happy."
    show monika ea
    show natsuki e1a b1a me
    y e1a mh na "I uh, I believe it's Natsuki's turn now?"
    show yuri ma
    n lhip e2a mh "Never have I ever... had a crush on a fictional character."
    show natsuki mj
    show sayori lup e3c me at dip
    show yuri lup e3c me at dip
    show monika md ec rhip bc at dip
    "Everyone very quickly takes a shot, except Natsuki."
    show monika mc rdown ea ba
    show yuri e1a md ldown
    show natsuki e1a ldown md
    show sayori e1a ma ldown
    "We all look at each other sheepishly." 
    $ advance_date(minutes=1)
    show natsuki ma
    "Nobody says anything for a good minute as Natsuki smirks."
    n e1d b1d mb "Anybody gonna share their crush? After all, don't you looooove them?"
    show natsuki ma
    show monika ma
    y mb "I'd be happy to share my fictional crush if you share your non-fiction love interest." 
    show yuri ma
    show natsuki mm e1b nd b1a
    "Natsuki blushes bright red, and if she'd be speaking I'm sure she'd be stammering."
    show natsuki mj b1d e2c nc
    "I take a mental note that she hasn't denied the existence of such a crush; after all..."
    _mc "Who knows when such information might become invaluable?"
    stop music fadeout 2.5
    s mh "So, you guys want to change activities?"
    show sayori ma
    n e3c na mg "Y- Yeah."
    n e1a b3a mh "I think it's my choice now?"
    show natsuki md
    y mb "It is, yes."
    show yuri ma
    n cross me e3c b1d "Hmm."
    show natsuki md
    "Natsuki brings her hand to her face thoughtfully."
    show natsuki e1a b1a with None
    hide yuri
    hide monika
    show sayori md at i11
    show natsuki ma
    camera master:
        align (1.0, 0.23) zoom 1.4
    show bg:
        blur 1.5
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ autofocus.block("natsuki")
    $ say_transition = True
    "After glancing at each of the club members, she then turns to Sayori."
    n turned mc "I've got it."
    n b1d e1d mb "We need the stuff." # im stuff
    show natsuki ma
    s mg b4 "The stuff?" # im stuff
    show sayori md with say_dissolve
    "Sayori, for a moment, looks confused."
    show sayori mb e1b b1a
    show natsuki e1a b1a
    with say_dissolve   
    "Then her eyes widen in realisation, and a smile breaks across her face."
    show natsuki e3d b3a 
    s e3d mc lup rup "Yeah, the stuff!" # im stuff
    s ldown rdown mn "Natsuki, you're a genius!"
    show natsuki at rhide
    show sayori at rhide
    hide sayori
    hide natsuki
    camera master
    show bg:
        blur 0.0
    show monika turned casual mc at i41
    show yuri turned casual lup md at i42
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    "And the two of them scurry off, leaving the remaining three of us to wonder."
    show monika md bc at t21
    show yuri at t22
    m "Uhhh."
    m mb bb "Should we be worried?"
    show monika ma
    mc thinking ea mg bm "I... don't think so?"
    y b1d e2a mg "I wonder what they mean by 'stuff'." # im stuff
    show yuri md
    m eb ba md "Well, I think I have a vague idea..."
    show monika ea mc
    show yuri e1d me b1a
    mc ml ba "Yeah, me too, but it's not..."
    y mg ldown "Not what?"
    show yuri md
    mc ef ldown mf "Ah..."
    _mc bi mh "Do I tell her my suspicions?"
    _mc eg ma "No way, this is Sayori we're talking about."
    _mc ea bd mh "Though now that I think about it, Sayori drinking is a relatively new concept to me."
    _mc ef ma ba "Who knows what else she gets up to?"
    "Just then, Natsuki makes her return known."
    show natsuki turned casual lhip rhip mn e3d b3a noband at t33
    show yuri at t32
    show monika at t31
    n "Ta-da~"
    show natsuki ma ldown rdown at dip
    "Placing a large sack onto the table, it falls open to reveal..."
    _mc bi ec mh "Are those toy guns?"
    show natsuki e1d b1d mn
    "I look at her in confusion, but her smug look is enough to blow that confusion away."
    n mb "So here we are, everyone~"
    n e1a b3a mh "Everyone pick a gun, and then take fifteen of the foam darts."
    n cross b1a mb "That's all you get, mind you. No picking them up off the floor."
    show natsuki ma
    m md "Why fifteen?"
    show monika mc
    n e3c b3a mi "Otherwise we'd be here all night for one round."
    show natsuki turned e1a ma
    mc ef ml ba "Makes sense, yeah."
    hide yuri
    hide natsuki
    show monika at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "With that, Monika leans in, grabbing one of the guns from the sack."
    "It's a large one, and from memory, it has an automatic function."
    "As well as a shield on top."
    show monika ma with say_dissolve
    "A small grin crosses her face as she holds it up."
    m mb "Perfect."
    show monika ma with say_dissolve
    n turned casual b3a mh noband "Oh, actually, everyone take two. Best to have a sidearm."
    show monika at i41
    show yuri turned casual at i42
    show sayori turned casual e3d at i43
    show natsuki b1a ma at i44
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "As she speaks, Sayori re-enters the room, carrying a crate of darts."
    s e1a mb "Alright, let's get started, shall we?"
    show sayori ma with None
    hide sayori
    hide monika
    hide natsuki
    show yuri md e1d at i11
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.unblock("monika")
    $ autofocus.block("yuri")
    $ say_transition = True
    "I see Yuri reach into the bag, upon being told to take two, and pulls out two revolvers."
    y mb e1a "This'll do nicely."
    show yuri ma with None
    show yuri lup e2a b1d ma
    camera master:
        zoom 1.2
    show bg:
        blur 1.3
    with Dissolve(0.2)
    "Standing up, her hair flows down her shoulders, as she assumes a pose."
    _mc ma ea ba na "Man, she looks badass!"
    show monika turned casual at i41
    show yuri e1a b1a at i42
    show sayori turned casual at i43
    show natsuki turned casual noband at i44
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    mc mg "Oh, actually, I've got one at home. Can I go grab that?"
    s mb "Yeah sure, just be quick, or we'll start without you~"
    show sayori ma
    mc eg mb "Sure sure."
    _mc ec ma "There's no way they'd be mean enough to play without me. Besides, it won't be long."
    
    scene bg s_house_entrance_night with wipeleft
    $ autofocus.unblock("yuri")
    
    "I race out the front door, into the frigid night."

    scene black with wipeleft

    _mc turned casual bf mm "Geez, it's cold out here."
    "I make it to my front door, unlock and open it, and fly through."

    scene bg mc_bedroom_night_closed_on with fastfade

    mc turned casual ec bi mf "Now where did I put it..."
    camera master:
        align (0.48, 0.7) zoom 1.6
    with Dissolve(0.2)
    "After considering for a moment, I race to the closet."
    "Prying it open, I see exactly what I was looking for."
    mc mb ea ba "Ha! Perfect."
    camera master:
        yalign 1.0 zoom 1.8
    with Dissolve(0.2)
    "Kneeling down, I pick up the belt and start loading it."
    "After placing thirteen shots in the belt, I place one in my sidearm and the last one in my pocket."
    mc ed md "That should do nicely."
    camera master
    with Dissolve(0.2)
    "I'll have to keep count, as the belt goes for 25 rounds, so I'll have no idea when I run out unless I do."
    "And with that, I make my way back to Sayori's."

    scene bg s_house_night_on with wipeleft_scene

    "I gently open the door..."

    show black zorder 20 with NonBlockingDissolve(0.5)
    play music wtdgi 

    "And I see something that truly shocks me to my core, sending vibrations along the shocklines of my skin and digging deeper into my brain."
    mc turned casual ea nb mf "S- Sayori?"
    show bg s_living_room
    show cg sleepover 3
    "Lying on the ground in the living room..."
    "Is Sayori."
    "She isn't moving."
    "Hell, from this far away I can't even tell if she's breathing!"
    "I slowly approach her, dropping the gun as I do."
    "After a few steps, I break out into a run."
    mc mg bf eb "Sayori!"
    hide black with NonBlockingDissolve(0.5)
    $ persistent.sleepover.mark_cg(3)
    "Sliding across the ground on my knees, I come to a stop next to her head."
    mc bg mj ea "Sayori, can you hear me?"
    camera master:
        align (0.7, 1.0) zoom 1.2
    with Dissolve(0.3)
    "Leaning in, my eyes are drawn to her chest."
    "She isn't..."
    "She's not breathing."
    _mc eb bf mh "Oh god..."
    _mc bg ea "What do I do?"
    _mc ef mf "Uh, I know CPR, but aren't there steps I need to take first?"
    _mc ea bf mh "Uh... Wait, I need to check her pulse."
    camera master:
        align (0.95, 1.0) zoom 1.7
    with Dissolve(0.3)
    "Grabbing her wrist, I can feel that it's still warm."
    _mc eb bg mh "I was only gone for a few seconds!"
    _mc bf mf "What the hell happened?"
    camera master:
        align (0.4, 0.5) zoom 1.8
    with Dissolve(0.3)
    "Placing my fingers on her neck, I search for her pulse."
    "Frantically, I search for the pulse."
    _mc mh ea "It's there, right?"
    _mc eb "And where did everyone else go?"
    _mc "Why aren't they helping?!"
    "Wait, there it is!"
    "There's her pulse!"
    "And then, after finding her pulse, I feel a soft movement."
    _mc eg ma "Oh god, she's breathing."
    "Thank goodness."
    "And she moves, avoiding my finger."
    "She might almost be conscious. Maybe this isn't as bad as I..."
    stop music fadeout 0.1
    show cg mb with cg_dissolve
    s turned casual e3d mn "... Ehehe~"
    camera master
    with Dissolve(0.2)
    "I straighten up."
    _mc ec ba mh "No way."
    _mc bi "She's not serious, is she?"
    _mc eb bd "She did {b}not{/b} just pull that sort of prank on me."
    show cg eb ma with cg_dissolve
    s mg e3b "Shhhhh."
    show cg ea with cg_dissolve
    s mh e3d "I'm supposed to be dead, Melly!"
    show cg mb with cg_dissolve
    s mn "You can't talk to dead people!"
    show cg ma with cg_dissolve
    "Her playful whisper reminds me of something, as I come to terms with what was going on."
    "Sayori's own words."
    show bg s_living_room as stuff onlayer above_master
    show monika turned casual at i41 onlayer above_master
    show yuri turned casual e1a b1a at i42 onlayer above_master
    show sayori turned casual mb at i43 onlayer above_master
    show natsuki turned casual noband at i44 onlayer above_master
    show white_flashback onlayer above_master
    camera above_master at flash
    "'We'll start without you'."

    play music dday_2 fadein 1.0

    $ clear_layers("above_master")
    show cinematic_bar_top    at cinematic_bar(True, 0.5, 0.0)  onlayer above_master zorder 10
    show cinematic_bar_bottom at cinematic_bar(False, 0.5, 0.0) onlayer above_master zorder 10
    show black zorder 10 with {"master": Dissolve(0.5)}:
        alpha 0.5 
    "And at that moment, I reach for the sidearm in my pocket."
    # can someone please shoot me with a real gun?
    # this is hell to code
    # should've hired q fr fr
    hide cg
    hide black
    play sound nerf_shot_2
    show bg:
        align (0.4, 1.0) zoom 2.0
        easein_back 0.3 zoom 1.1 align (0.5, 0.5)
    with Dissolve(0.2)
    "Out of the corner of my eye, I see a dart whiz past my face."
    mc ea mg "Woah! Hey, no fair!"
    $ autofocus.block("yuri")
    $ autofocus.block("monika")
    $ autofocus.block("sayori")
    $ autofocus.block("natsuki")
    $ autofocus.zorder = False
    show bg:
        matrixtransform RotateMatrix(0, 0, 0)
        ease_back 0.5 xalign 0.8 yalign 0.1 zoom 1.5 matrixtransform RotateMatrix(0, 0, -10)
    show yuri turned casual lup b1d onlayer above_master:
        xanchor 0.0 xpos 1.0 yalign 1.0 yoffset 120 zoom 0.8
        matrixanchor (0.5, 1.0) matrixtransform RotateMatrix(0, 0, 0)
        ease_back 0.4 xpos 0.6 zoom 0.9 matrixtransform RotateMatrix(0, 0, -10)
    "My assailant - none other than Yuri with her dual revolvers - has begun charging me."
    show yuri mb rup with {"above_master": Dissolve(0.1)}
    y "Surprise."
    show yuri ma
    show white onlayer above_master at flash(0.2)
    show bg:
        0.2
        easein_back 0.4 matrixtransform RotateMatrix(0, 0, 4) align (0.0, 1.0) zoom 1.7
    show yuri b1a me e1d:
        0.2
        alpha 0.0
    play sound nerf_shot_1
    "Firing off a shot at her, I roll sideways, toward my larger gun."
    hide white
    hide yuri
    mc mb na "I was sure outplayed there."
    y turned casual e1d mh "Well, I wasn't going to shoot you when you were genuinely worried about your friend."
    mc ec bi md "Oh, how considerate of you!"
    show bg:
        easein_back 0.4 matrixtransform RotateMatrix(0, 0, 0) xalign 0.5 zoom 1.75
    "The sarcasm dripping from my voice, I finally reach my gun."
    show bg:
        easein_back 0.5 yalign 0.0 zoom 1.6
    show yuri turned casual ma b1d e1a:
        xalign 0.5 ypos 1.03 yanchor 1.0 
        zoom 1.2 alpha 0.0 yoffset 0.0
        easein_back 0.5 alpha 1.0 zoom 1.0 yoffset 200.0
    "Yuri's now practically on top of me, both guns bearing down within only a few metres of me."
    show bg:
        easein_back 0.3 zoom 1.35 yoffset 30
    show yuri me e1d b1a:
        easein_back 0.3 zoom 0.8 yoffset 70
    "I grab the heavy gun, turn it on, and aim it in her direction, firing off a volley."
    play sound [audio.nerf_shot_1, audio.nerf_shot_1]
    show yuri b1d ma e1a:
        parallel:
            0.2 + 0.2 + 0.21 + 0.1
            alpha 0.0
        parallel:
            matrixtransform RotateMatrix(0, 0, 0)
            parallel:
                easein 0.15 matrixtransform RotateMatrix(0, 0, 10) yoffset 120
                easeout 0.25 matrixtransform RotateMatrix(0, 0, 0) yoffset 90
            parallel:
                easeout_quad 0.4 xoffset 150
            "yuri turned casual e3d me lup rup"
            easein 0.1 yoffset 30
            easeout 0.2 yoffset 90
    show bg:
        easeout 0.2 align (0.9, 0.9) yoffset -50
        0.2
        ease 0.21 yoffset 0
        0.1 
        xalign 0.65 zoom 1.9 yoffset 30
    show white zorder 5:
        flash(0.2)
        0.21
        flash(0.1)
    "The rapid fire causes Yuri to leap backward, flipping behind the couch."
    hide white
    _mc eb ma ba "Man, not only does she look badass with the guns, but she acts it too!"
    _mc ec bi "Looks and style can only get you so far in a fight, though. At the end of the day, fire kills."
    hide yuri
    show bg:
        yoffset 0 zoom 1.1 xoffset 0
    hide cinematic_bar_top
    hide cinematic_bar_bottom
    with Dissolve(0.2)
    "With that in mind, I break cover, intent on pressing my advantage."
    show bg:
        easein_back 0.4 zoom 1.9 yoffset 30 xoffset -200
    show cinematic_bar_top    at cinematic_bar(True, 0.2, 0.3)  onlayer above_master zorder 10
    show cinematic_bar_bottom at cinematic_bar(False, 0.2, 0.3) onlayer above_master zorder 10
    "Mounting the couch like the Marines cresting Suribachi, I purposefully raise my gun over the parapet of its back-"
    show expression Gradient("#7e3f28", "#894227") as stuff
    show yuri turned me b2a nb e1b casual:
        xalign 0.5 ypos 1.0 yanchor 0.6 zoom 1.4
    with NonBlockingDissolve(1.0)
    "-The sights triumphantly settling on a huddled mass of purple."
    mc md "Say goodnight, Gracie."
    "And I squeeze the trigger..."
    show yuri e1d b1a md with say_dissolve
    play sound nerf_trigger
    "... only to have nothing exit the weapon but the pathetic whirring noise of a stoppage."
    mc mj nb "Of all the stinking-"
    show yuri ma e1a b1d na with say_dissolve
    "Yuri's look of apprehensive resignation transforms into a sly grin."
    show yuri mb with say_dissolve
    y "Goodnight, Gracie."
    show yuri ma lup rup with say_dissolve
    "She brings her six-shooter to bear."
    "Just as I'm about to stare down the barrel of her weapon and look destiny in the face-"
    n turned b3a mc notail noband casual "Two birds with one stone!"
    play sound nerf_shot_2
    hide stuff
    hide yuri
    show bg:
        easein_back 0.3 yoffset 0.0 zoom 1.1 xoffset 0
    with {"master": Dissolve(0.3)}
    hide cinematic_bar_top
    hide cinematic_bar_bottom
    "-A volley of darts whizz though the gap between Yuri and I, causing both of us to startle and dodge aside."
    mc md na "Praise the tsun."
    show bg:
        easein_back 0.5 zoom 2.3 yoffset 30 xoffset -100
    show cinematic_bar_top    at cinematic_bar(True, 0.25, 0.0)  onlayer above_master zorder 10
    show cinematic_bar_bottom at cinematic_bar(False, 0.25, 0.0) onlayer above_master zorder 10
    "I scramble for safety behind the armchair, frantically doing what I can to clear the jam."
    show expression Gradient("#7e3f28", "#894227", xsize=0.5) as stuff:
        xalign 0.0
    show yuri turned e2a b1d md casual: 
        xcenter 0.25 ypos 1.0 yanchor 0.6 zoom 1.2
    show expression Gradient("#1e1b29", "#242030", xsize=0.5) as stuff2:
        xanchor 1.0
    show natsuki turned ma b1d notail casual noband:
        xcenter -0.25 ypos 1.0 yanchor 0.7 zoom 1.2
    hide cinematic_bar_top
    hide cinematic_bar_bottom
    with NonBlockingTransition(Wipe(0.25, theta=180))
    "Yuri, evidently dismissing me and my disabled weapon as a threat, focuses on tackling the clear and present danger."
    show yuri e1a ma lup rup
    camera master:
        xanchor 0.5 xpos 0.5
        ease 0.5 xpos 1.0
    show white onlayer above_master:
        alpha 0.0
        matrixcolor OpacityMatrix(0.4) # tone it down because holy shit flashbang
        0.5
        block:
            choice:
                flash(0.1)
                0.2
            choice:
                flash(0.1)
                0.1
            choice:
                flash(0.2)
                0.2
            choice:
                flash(0.2)
                0.1
            choice:
                flash(0.1)
                0.08
                flash(0.1)
                0.3
            choice:
                flash(0.1)
                0.3
            repeat
    "A rampaging candyfloss commando, hellbent on maximum carnage."
    "The battle spills out of the living room in short order."
    "Against all reason, I stop and gawk in awe at the sight of them going at it amidst the battleground of the living room."
    "Weaving and bobbing, adroitly taking advantage of cover as they close the distance."
    "Loosing potshots at one another every opportunity that presents."
    "Sixty seconds of old school John Woo."
    hide stuff 
    hide stuff2
    hide white
    hide yuri
    hide natsuki
    camera master
    show bg:
        align (0.2, 1.0) zoom 2.1 yoffset -50
    show sayori turned casual rup e3a me:
        matrixtransform RotateMatrix(0, 0, -76)
        xalign 0.5 yanchor 0.63 ypos 1.0 zoom 1.1   
    show cinematic_bar_top    at cinematic_bar(True, 0.0, 0.5)  onlayer above_master zorder 10
    show cinematic_bar_bottom at cinematic_bar(False, 0.0, 0.5) onlayer above_master zorder 12
    with NonBlockingDissolve(0.2)
    "Even Sayori can't help but pull a Lazarus and take a peek, so incredible is the sight."
    hide sayori
    show bg:
        offset (0, 0) zoom 1.0
    with fastfade
    $ advance_date(minutes=1)
    "It's a close-run thing, but the issue is decided at long last."
    show bg:
        align (0.0, 1.0)
        easein 0.4 zoom 1.7
    show yuri turned casual lup e2a mk b2b:
        xanchor 0.5 xpos 0.3 yalign 1.0 yoffset 200
        zoom 1.04 alpha 0.0
        easein 0.4 alpha 1.0 zoom 1.0
    "Yuri blunders, hiding behind a rack of shelves that isn't big enough to shield her..." 
    show bg:
        matrixtransform RotateMatrix(0, 0, 0)
        easein_back 0.4 xalign 0.8 yalign 0.1 zoom 1.5 matrixtransform RotateMatrix(0, 0, -10)
    show natsuki turned casual notail noband mb e1d lhip:
        xanchor 0.0 xpos 1.0 yalign 1.0 yoffset 120 zoom 0.8
        matrixanchor (0.5, 1.0) matrixtransform RotateMatrix(0, 0, 0)
        easein_back 0.4 xpos 0.6 zoom 0.9 matrixtransform RotateMatrix(0, 0, -10)
    show yuri:
        matrixtransform OffsetMatrix(0, 0, 0) * RotateMatrix(0, 0, 0) matrixanchor (0.5, 1.0)
        easein_quad 0.2 matrixtransform OffsetMatrix(-250, 230, 0) * RotateMatrix(0, 0, -27)
        alpha 0.0
    n "That rack isn't going to help you any, Yuri!"
    hide natsuki
    show yuri mm e3a b2a nb rup:
        alpha 1.0 zoom 1.3 matrixtransform None
        0.08 + 0.08 + 0.12 + 0.08 + 0.08 + 0.17 + 0.11
        matrixtransform OffsetMatrix(0, 400, 0)
    show bg:
        align (0.0, 1.0) zoom 2.3 matrixtransform None
        0.08 + 0.08 + 0.12 + 0.08 + 0.08 + 0.17 + 0.11
        yoffset 400
    show white:
        flash(0.08)
        0.12
        flash(0.08)
        0.16
        flash(0.1)
    play audio audio.nerf_shot_1
    play audio ["<silence 0.3>", audio.nerf_shot_1]
    play audio ["<silence 0.67>", audio.nerf_shot_2]
    "... from a perfectly executed Mozambique drill from Natsuki."
    show yuri mi e3c b1d ldown rdown with say_dissolve
    y "Agh! Dash it all."
    show yuri mj:
        show_cancels_hide False
        on hide:
            easein_cubic 0.6 xanchor 0.0 xpos 1.0
    hide yuri
    with None
    hide bg
    show bg s_kitchen_day:
        align (0.0, 0.5) zoom 1.1
        easein_back 0.5 xalign 0.5
    show yuri turned casual e3c mj b1d:
        xanchor 1.0 xpos 0.0 yanchor 1.0 yalign 1.0 yoffset 150 zoom 1.0
        easein_back 0.5 xanchor 0.5 xpos 0.5
    with Dissolve(0.5)
    show yuri ketchup
    camera master:
        yoffset 30
        align (0.5, 1.0) zoom 1.3
        ease 5.0 yalign 0.0
    with Dissolve(0.5)
    "Much to Natsuki's and my disbelief and amusement, Yuri pauses to smear herself with ketchup before dropping her gun and clutching her chest." 
    show yuri lup rup me b2b e3d nb with say_dissolve
    "Gasping out some famous last words as she does so."
    show yuri mh with say_dissolve
    y "Now... ends... the mystery."
    camera master:
        easein_back 0.5 yalign 1.0 yoffset -100
    show bg:
        matrixtransform RotateMatrix(0, 0, 0)
        easein_back 0.5 zoom 1.5 align (0.6, 1.0) matrixtransform RotateMatrix(0, 0, 3) yoffset 15
    show yuri me e3c:
        matrixtransform RotateMatrix(0, 0, 0)
        easein 0.3 matrixtransform RotateMatrix(0, 0, 81) yanchor 0.5 ypos 1.05 yoffset 0 zoom 0.8
    "And with that, she dramatically collapses to the floor like a dying swan, then lies still."
    camera master:
        easein 0.25 zoom 1.4 yoffset -120
    show natsuki turned casual notail noband rhip b3a e3c me onlayer above_master zorder 11:
        xoffset -500 yalign 1.0 zoom 1.5 alpha 0.0 matrixtransform RotateMatrix(0, 0, 8) yoffset 550
        easein 0.25 alpha 1.0 xoffset -450
    "Natsuki sidles over to her fallen opponent, blowing imaginary smoke from the muzzle of her gun."
    show natsuki mc e1a with say_dissolve
    n "You were good, kid. Real good. But at the end of the day, you'll always be second best, see?"
    show natsuki mb e1d b1d with say_dissolve
    n "Because nobody, absolutely nobody beats me in the kitchen."
    show natsuki ma
    camera master:
        blur 3.0
    show black:
        alpha 0.3
    with say_dissolve
    "Those gimlet eyes of passion pink then snap around to fix me with a look of savage appetite."
    show natsuki e3c mb with say_dissolve
    n "That's the hors d'oeuvres done."
    show natsuki e1d mo with say_dissolve
    n "Now for the main course."
    show natsuki ma with say_dissolve
    "And I belatedly remember that I was supposed to be clearing the stoppage."
    show bg s_living_room:
        align (0.5, 1.0) zoom 1.0 offset (0, 0) matrixtransform None
    camera master
    hide natsuki
    hide yuri
    hide black
    with fastfade
    _mc eg ma ba na "That's the stoppage cleared, thank god."
    show natsuki turned notail casual noband:
        xcenter 0.25 yalign 1.0 yoffset 100 zoom 0.85
    show expression split("bg s_kitchen_day", "bg s_living_room") as bg
    hide cinematic_bar_top
    hide cinematic_bar_bottom
    show expression "#000" as stuff:
        FadingBorders((20, 0, 0, 0))
        xanchor 20 xpos 0.5
    with {"master": wiperight}
    mc ea mb "Careful what you wish for, Captain Cupcake."
    show natsuki e1d b1d with say_dissolve
    mc ec bi md "You might just find yourself biting off more than you can chew."
    hide natsuki
    hide stuff
    show bg s_kitchen_day:
        align (0.0, 0.0) zoom 2.0
    show black onlayer above_master
    show cinematic_bar_top    at cinematic_bar(True, 0.0, 0.0)  onlayer above_master zorder 10
    show cinematic_bar_bottom at cinematic_bar(False, 0.0, 0.0) onlayer above_master zorder 10
    with Dissolve(0.2)
    "The danse macabre begins anew."
    hide black
    show white:
        alpha 0.0
        matrixcolor OpacityMatrix(0.4)
        0.4
        block:
            choice:
                flash(0.1)
                0.2
            choice:
                flash(0.1)
                0.1
            choice:
                flash(0.2)
                0.2
            choice:
                flash(0.2)
                0.1
            choice:
                flash(0.1)
                0.08
                flash(0.1)
                0.3
            choice:
                flash(0.1)
                0.3
            repeat
    with {"above_master": Dissolve(0.3, time_warp=_warper.easein)}
    show bg:
        matrixtransform RotateMatrix(0, 0, -2)
        easein_back 0.45 xalign 0.9 yalign 1.0 zoom 1.7 matrixtransform RotateMatrix(0, 0, 3)
    show natsuki turned casual noband e1d b1d:
        matrixtransform RotateMatrix(0, 0, 13) xpos 0.0 xanchor 0.8 yoffset 0 yanchor 1.0 ypos 1.5 zoom 1.2
        easein 0.3 xpos 1.0 xanchor 0.0 yoffset 20
    "Fancy footwork. Dips and pirouettes."
    show bg:    
        easein_back 0.4 xalign 0.2 yoffset -120 zoom 1.8 matrixtransform RotateMatrix(0, 0, -4)
    show natsuki mn e3c:
        matrixtransform RotateMatrix(0, 0, -40) yoffset 0.0 xoffset 20
        parallel:
            easein_quad 0.25 matrixtransform RotateMatrix(0, 0, -80) xoffset -1200
        parallel:
            easeout_quad 0.3 yoffset 330
    "I've never had a worthier partner, nor a more frustrating foe."
    show bg:
        easein_back 0.6 matrixtransform RotateMatrix(0, 0, 0) zoom 1.6 xalign 0.7 yoffset 300 knot 180 knot 220 knot 250 
    hide natsuki
    show natsuki turned casual notail lhip rhip noband e3d me:
        around (0.75, 1.0) anchor (0.5, 0.5)
        matrixtransform RotateMatrix(0, 0, 100)
        radius 1400 angle -80
        easein 0.45 matrixtransform RotateMatrix(0, 0, 250) angle 70 radius 1100 knot -100 clockwise
    "Quick of reflex and small of silhouette, she makes a difficult target."
    _mc ba mh "It's like trying to hit a dragonfly with a twelve gauge."
    _mc eg ma "But at the end of the day, you know what they say: 'A good big 'un will always beat a good little 'un'."
    _mc ef mh "Or so I think."
    hide bg
    show bg s_kitchen_day:
        align (0.53, 1.0) zoom 1.1
    hide white
    hide natsuki
    hide cinematic_bar_top
    hide cinematic_bar_bottom
    with fastfade
    "For now, I've got her at bay."
    show bg:
        easein 0.5 zoom 2.0
    show expression "#000" at FadingBorders((0, 0, 30, 0)) as stuff:
        xanchor 1.0 xpos 0.0
        easein 0.5 xpos 0.3
    show expression "#000" at FadingBorders((30, 0, 0, 0)) as stuff2:
        xanchor 0.0 xpos 1.0
        easein 0.5 xpos 0.65
    "She's holed up near the far end of the dining table, crouched low, just out of sight."
    "I scribble the word {b}{i}{color=#482414}SURRENDER{/color}{/i}{/b} in chocolate sauce on one of the many wandering pieces of paper, fold it into an aeroplane and waft it her way."
    show bg:
        zoom 1.1 offset (0, 0)
    hide stuff2
    hide stuff
    with fastfade
    "Back comes the aeroplane several seconds later, a reply scrawled on its fuselage in mustard."
    "{b}{i}{color=#f1dd3f}NUTS{/color}{/i}{/b}"
    _mc ec bi ma "Okay, smartass. You asked for it."
    show white:
        flash(0.1)
        0.08
        flash(0.1)
    show bg:
        easein_back 0.4 yoffset -20 zoom 2.0
    show cinematic_bar_top    at cinematic_bar(True, 0.2, 0.0)  onlayer above_master zorder 10
    show cinematic_bar_bottom at cinematic_bar(False, 0.2, 0.0) onlayer above_master zorder 12
    play audio nerf_shot_2 
    play audio ["<silence 0.2>", audio.nerf_shot_2]
    "One climactic burst of suppressing fire and I'm finally on her."
    show natsuki turned casual notail noband mj onlayer above_master zorder 11:
        xcenter 0.45 yalign 1.0 yoffset 400 zoom 1.3
    show bg:
        blur 3.0
    with Dissolve(0.2)
    "Caught in the midst of reloading, she looks up at me, her expression deadpan."
    "I take a moment to gloat."
    mc ea mg ba "I know what you're thinking. 'Did she fire fifteen shots total, or just fourteen?'"
    mc ec bi md "Truth is, I sort of lost count in all this excitement." 
    show natsuki ma with say_dissolve
    mc ea mb ba "But being that this is the most powerful weapon of its class, and would blow your-" 
    show natsuki e3c b1d mb with say_dissolve
    n "No kidding on losing count, schmuck."
    show natsuki ma with say_dissolve
    mc ml bd "Come again?"
    _mc ec ba mh "... She's right."
    _mc nb "There's nothing left on the belt."
    show natsuki rhip b3a with say_dissolve
    play sound nerf_reload
    "Natsuki's finished reloading - And she's looking more bloodthirsty than ever."
    show natsuki e1a mc with say_dissolve
    n "It just isn't your day, is it, Inspector?"
    show natsuki ma with say_dissolve
    _mc eg bi ma "No shit."
    mc mb "Run, little miss MC; run."
    hide bg
    hide natsuki
    show black
    hide white
    with NonBlockingTransition(wipeleft)
    "-And run I do, tearing up the stairs, like all the devils in the world are at my heels."
    "Heart pounding, lungs bursting, I make a beeline for the likeliest port in this storm."
    hide cinematic_bar_top
    hide cinematic_bar_bottom
    with None
    hide black
    show bg s_spare_bedroom:
        align (0.5, 1.0)
    with NonBlockingDissolve(0.3)
    "The spare bedroom with its spacious walk-in closet, where she and I used to play at interdimensional travel as kids."
    show bg:
        align (0.5, 1.0) zoom 1.0
        parallel:
            (0.6 * 0.91)
            blur 1.0 matrixcolor BrightnessMatrix(0.2)
            zoom 2.0 yoffset 100
        parallel:
            easein 0.4 zoom 1.5
    show black zorder 1:
        FadingBorders((20, 0, 0, 0))
        xsize 1.5 xpos 1.0 xanchor 0 ysize 1.5 yalign 0.5
        easein_bounce 0.6 xpos 0.0 xanchor 20
        easein 0.08 xanchor 4
    play music2 add_playback_info(dday_1, 50) fadein 2.0
    stop music fadeout 2.0
    "Dashing straight into the wardrobe, I slam the door behind me and sink to the floor in a sweaty heap, catching my breath."
    show monika turned casual ed:
        alpha 0.0 xcenter 0.9 yalign 1.0 yoffset 400 zoom 1.2
        easein 0.9 alpha 0.25
    camera master:
        xpos 0.5 xanchor 0.5 zoom 1.0 yalign 0.2
        0.7
        easein_back 0.5 xanchor 0.9 zoom 1.05
    $ say_transition = True
    "Only to discover, as my vision adjusts to the extremely dim light streaming in through the door louvres, that I'm not alone."
    m mb "Desperation loves company, it would seem. Or is it great minds thinking alike? Either way, you're a sight for sore eyes."
    show monika ma with say_dissolve
    mc mg bg ea "M- Monika? What are you doing in here?"
    show monika ec bc mc rhip with say_dissolve
    "She hangs her head ruefully."
    m md "Dropped my primary during the initial havoc. Didn't take long for me to empty my secondary, as well."
    m eb bb mb "Clearly I'm no expert at this."
    m ba ec md "And now here I am, completely defenceless, with nothing but this closet for shelter."
    show cinematic_bar_top    at cinematic_bar(True, 0.2, 0.3)  onlayer above_master zorder 10
    show cinematic_bar_bottom at cinematic_bar(False, 0.2, 0.3) onlayer above_master zorder 10
    show monika rdown ea mc:
        easein_back 0.45 xoffset -500
    "Outside, I can hear the ominous pad of purposeful footsteps."
    show monika rhip bc md:
        xoffset 0
    with NonBlockingTransition(fastfade)
    m "This closet, in which I'm going to meet my end."
    show monika mc ea ba rdown
    camera master:
        zoom 1.3
    with say_dissolve
    "I clasp my hand over Monika's shoulder reassuringly."
    mc mb ba na "Don't put yourself down. You made it this far, and that's amazing for a neophyte."
    mc eg bi mg "The end may be nigh, but rest assured you won't have to face it alone."
    show monika bb ma with say_dissolve
    "Monika gazes gratefully at me, flashing me a bittersweet smile."
    show monika md ba with say_dissolve
    "Just as she's about to open her mouth and reply..."
    show monika:
        linear 1.5 xoffset 100 
    n "{cps=30}Heeeeeereee's{/cps}{nw}"
    show monika mc:
        blur 0.0
        easein 0.35 blur 3.0 alpha 0.0
    camera master:
        easein_back 0.32 xpos 0.12 xanchor 0.12 yoffset 200 zoom 2.0 yalign 0.2 xoffset 100
    show black:
        easein_back 0.32 xoffset 150
    show bg:
        easein_back 0.32 matrixcolor BrightnessMatrix(0.3)
    show natsuki turned notail casual noband mask e1c mo b3a zorder 0:
        matrixanchor (0.5, 1.0) matrixtransform RotateMatrix(0, 0, -25) zoom 0.8 xcenter 0.26
        yoffset -200 xoffset 400 matrixcolor BrightnessMatrix(-0.2)
        easein_back 0.32 xoffset 0 
    hide cinematic_bar_top
    hide cinematic_bar_bottom
    play music add_playback_info(audio.dday_2, get_pos("music2") + 69.857) fadein 1.0
    stop music2 fadeout 1.0
    extend "{cps=187} Natsuki!{/cps}"
    show expression "#000" onlayer above_master as stuff
    hide monika
    with NonBlockingDissolve(0.3)
    "What happens next is a blur."
    show black:
        on hide:
            easeout_quad 0.42 xoffset 0 xpos 1.0
    hide black
    show natsuki ma lhip rhip:
        easein_back 0.4 matrixtransform RotateMatrix(0, 0, 0) xcenter 0.35 yoffset -80 zoom 1.2 matrixcolor BrightnessMatrix(0.0)
    show bg:
        parallel:
            # X_back warpers cause blur to be negative, which is an error
            easein 0.2 blur 0.0
        parallel:
            easein_back 0.4 align (0.2, 1.0) matrixcolor BrightnessMatrix(0.0) zoom 1.15
        parallel:
            matrixtransform RotateMatrix(0, 0, -10)
            easein 0.3 matrixtransform RotateMatrix(0, 0, 0)
    camera master:
        easein 0.2 align (0.5, 0.0) offset (0, 0) zoom 1.0
    show cinematic_bar_top    at cinematic_bar(True, 0.0, 0.5)  onlayer above_master zorder 10
    show cinematic_bar_bottom at cinematic_bar(False, 0.0, 0.5) onlayer above_master zorder 10
    with None
    hide stuff with {"above_master": Dissolve(0.15, time_warp=_warper.easein_quad)}
    "The doors of the closet fly open."
    camera master:
        align (0.25, 0.4) zoom 1.5
    show natsuki zorder 1
    with Dissolve(0.2)
    "From where we're crouching on the floor, what stands in the frame looks like a giant. A gun-toting, pastel-hued giant clad in what appears to be Sayori's old hockey mask."
    show black zorder 0:
        alpha 0.5
    show bg:
        blur 2.0
    with NonBlockingDissolve(0.3)
    "Her eyes blazing with unholy light."
    hide natsuki
    hide black
    show bg:
        blur 0.0
    camera master
    show bg:
        align (0.9, 1.0) zoom 2.0 yoffset -130
    show monika turned casual nb md bb:
        xcenter 0.8 yalign 1.0 yoffset 600 zoom 1.5
    with NonBlockingTransition(fastfade)
    "Monika screams, the piteous noise arousing all my protective instincts."
    camera master:
        align (0.9, 0.85)
        easein_back 0.3 zoom 1.5
    show monika:
        parallel:
            easein_quint 0.3 xoffset 500 alpha 0.0 yoffset 650
        parallel:
            blur 0.0
            easein_cubic 0.3 blur 2.0
    "Without a second thought, I hurled myself between her and our executioner... with predictable results."
    show black:
        alpha 0.0
        0.2 + 0.05
        alpha 1.0
    show white:
        alpha 0.0
        easein_quad 0.2 alpha 1.0
        0.1
        ease 1.0 alpha 0.0
    play sound ["<silence 0.07>", audio.nerf_shot_2]
    "Down I go, a suction cup dart stuck to the middle of my forehead."
    hide monika
    camera master
    show bg:
        offset (0, 0) zoom 1.0
    n turned casual noband notail mask e3c mb b1d "Pffft. Such heroic nonsense."
    "Far less predictable, though, is how it all ends."
    window hide None
    stop music
    play sound nerf_shot_2
    pause 2.5
    window auto show Dissolve(0.5)
    n e1a mg "The heck?"
    show natsuki me:
        xcenter 0.3 yalign 1.0 zoom 1.4 yoffset (500 - 100)
        ease 4.0 yoffset 500
    show bg:
        align (0.0, 0.5) zoom 1.4 yoffset -30
        ease 4.0 yoffset 30
    hide white
    hide black
    with NonBlockingDissolve(0.3)
    "Natsuki suddenly finds herself sporting precisely the same head accessory as I do."
    "A suction cup dart, landed smack dab above her right eyebrow."
    "A suction cup dart, fired from none other than..."
    show bg:
        easein_back 0.4 xalign 0.8 yalign 0.1 zoom 1.5 yoffset 0 matrixtransform RotateMatrix(0, 0, -8)
    show monika turned casual:
        xanchor 0.0 xpos 1.0 yalign 1.0 yoffset 200 zoom 0.9
        matrixanchor (0.5, 1.0) matrixtransform RotateMatrix(0, 0, 0)
        easein_back 0.4 xpos 0.55 matrixtransform RotateMatrix(0, 0, -8)
    show natsuki:
        matrixanchor (0.5, 1.0) matrixtransform RotateMatrix(0, 0, 0)
        easein_back 0.4 matrixtransform RotateMatrix(0, 0, -15) xoffset -500
    mc ml ba ea nb "You-"
    mc mm eb bd "You told me you were out."
    hide natsuki
    mc ea mg na "Helpless."
    mc ef bi ml "Defenceless."
    mc ea mg bd "I took that shot Natsuki meant for you, based on that faulty knowledge."
    show monika ed lpoint with say_dissolve
    "Monika smiles coyly, twirling her pistol around her trigger finger before holstering it in her waistband."
    m eb mb "Sorry, MC. But sometimes, a girl's gotta do what a girl's gotta do."
    m ea bc "Outplay, outwit and outlast."
    m md ba ec "I won't deny it, though. It's nice, seeing that chivalry's not dead." 
    m ldown ea mb "So here's a little something for your trouble."
    show monika ma with say_dissolve
    "She's got me there."
    "There's nothing in the rules prohibiting her from doing that."
    "But it isn't so much her explanation that stifles my further protests..."
    show monika ec md rhip:
        zoom 1.9
        yoffset 800 xoffset -400
    show bg:
        zoom 1.7 yalign 0.4 xalign 0.9
    with NonBlockingTransition(fastfade) 
    "... than it is the contact of her lips against my still-stinging forehead."
    show black
    hide monika
    camera master
    show bg:
        zoom 1.0 offset (0, 0) matrixtransform None
    with NonBlockingDissolve(0.3)
    "Imparting a soothing effect that completely outweighs the fleetingness of their touch."
    "All my indignation, dispelled just like that."
    hide black 
    show natsuki turned mask casual noband notail b1d e3c me nb:
        xcenter 384 yalign 1.0 zoom 1.4 yoffset 500
    show bg:
        align (0.0, 0.5) zoom 1.4 yoffset 30
    with NonBlockingDissolve(0.3)
    "Part of Natsuki clearly wants to laugh her head off at how I've been hoodwinked."
    show bg:
        easein 0.5 zoom 1.0 offset (0, 0) xalign 0.5
    show natsuki md na:
        easein_quad 0.5 xcenter 640 zoom 0.8 yoffset 0 ypos 1.03 yanchor 1.0
    hide cinematic_bar_top
    hide cinematic_bar_bottom
    $ autofocus.unblock("monika")
    $ autofocus.unblock("yuri")
    $ autofocus.unblock("sayori")
    $ autofocus.zorder = True
    $ say_transition = False
    "But she can't sufficiently get over something else in order to do so."
    $ autofocus.unblock("natsuki")
    n mc "All that skill. All that know-how. All that firepower. All that positional advantage."
    n e2a b3a mb lhip "Everything under my belt I had going for me."
    show monika turned casual at t22
    show natsuki cross mh e1d b1d at t21
    n "And I lose to someone cowering in a closet with a dinky sidearm, and their human shield?!"
    show natsuki mj
    m lpoint md "That's just how the cookie crumbles, Natsuki."
    m mb ldown bc "All's fair in love and war."
    show monika ma
    n e2a mm "Damn it!"
    show monika ba ed
    show natsuki md
    with None
    hide natsuki
    hide monika
    show black zorder 0
    with NonBlockingDissolve(1.0)
    "As we reluctantly crown Monika the winner, descend the stairs and call for Yuri and Sayori to join us..."
    "... I can't help but boggle at how we've underestimated our President."
    "How strategically she's outmanoeuvred us."
    "She may not have been the strongest player, but she used what she had to her advantage."
    "All done so cunningly that you could stick a tail on her plan and call it a fox."
    "It was a battle for the ages, the likes of which the world might never see again."
    "And at the end of it all, when the dust settles, who's left standing?"
    show monika turned casual:
        i11
        flash
    _mc ec mh ba "Just Monika."
    _mc eg ma "{i}That{/i} Mon."
    "With her maddening smile and even more maddening charm."
    "Continuing to surprise me at each and every turn."

    if branches.is_current(branches.FATE):
        scene bg s_kitchen_day:
            zoom 1.5 align (0.4, 1.0)
        show yuri turned casual ketchup e3c md lup:
            xycenter (0.5, 1.05) zoom 0.8
            matrixtransform RotateMatrix(0, 0, 81)
        with wipeleft_scene

        "Moving back into the kitchen, I spy Yuri, still lying there in a puddle of her own... ketchup."
        show yuri e3a me with say_dissolve
        "She sneaks a peek at me with one eye through her hair,"
        show yuri e3c md with say_dissolve
        extend " then shuts it and goes rigid again."
        _mc turned casual ec "Waiting to be revived, I think."
        _mc eg "She's loving the hell out of this."
        camera master:
            align (0.4, 1.0) zoom 2.0
        with Dissolve(0.2)
        "I kneel down beside her and touch her upper leg."
        show yuri ma with say_dissolve
        "Though her eyes remain closed, I see the corners of her mouth twitch into a smile."
        mc bg ml nb "Oh, Yuri."
        mc bf mg "It's... It's just so tragic..."
        mc ef bf ml na "You youthful flower, cut down in your prime."
        mc eg bg mg "Leaving me all alone in the world."
        mc mm nb "Wherever will I go? Whatever will I do?"
        camera master:
            ease_quad 1.0 zoom 2.1
            0.2
            ease 3.0 zoom 1.0
        with Dissolve(0.2)
        "I keel over, the side of my head resting on her chest, and start keening away."
        "I've never put on a more convincing show of it."
        "So convincing, that I even end up shedding a few real tears."
        mc tears_a bf mg  "I must lay you to your eternal slumber."
        mc ml bg "Burial at sea is as good an option as any, I suppose..."

        scene bg s_house_corridor_day with wipeleft

        "Hoisting her on to my shoulders, I convey her up the stairs, caterwauling all the way."

        scene bg s_bathroom_night_on with wipeleft

        "Into the master bathroom we go, where I gently set her down into the tub."
        mc turned casual eg bg ml "Now to consign you to the deep."
        "I lean over to turn on the tub's faucets, and she finally springs to life, squealing and giggling as she reaches out to stop me."
        y turned casual ketchup mo e3d "Alright, alright! Enough already~"
        show yuri ma at i11 with fastfade
        mc ed md ba "Oh, don't tell me you aren't keen on my performance."
        y e1d mb lup rup "Of course I am. It was the icing on the cake. This whole evening has been chock-full of fun."
        y rdown mh e2a b1d "Don't stop entirely, though."
        show yuri md
        mc mf ea "Mmm?"
        y b1a mg "As in, well- Um-"
        show yuri ma nb b2b
        "Yuri trips over herself as she tries to figure out what she meant to say."
        y e3c b1a mh na ldown "Okay, that sounds a bit wrong, but what I meant was this."
        show yuri mj at dip 
        "She gestures over herself, the ketchup splattered across her torso."
        "It takes a second for me to realise what she means before I speak up."
        mc ml "Ah, true..."
        y e2a mh b1a "Admittedly, I wished to give off the most convincing act, like you did, but in hindsight..."
        show yuri me e3c at dip
        "Yuri lets out a light sigh."
        show yuri e1a md
        mc mb "Well, I'll let you handle yourself, but may I at least clean your arms off?"
        y mg e2a b1d "Of course..."
        show yuri md with None
        camera master:
            align (0.45, 0.52) zoom 2.0
        show yuri b1a e1a lup
        show bg:
            blur 3.0
        with Dissolve(0.2)
        "Soaking a flannel with warm water, I lean closer to Yuri, gently dabbing at her hands and forearms."
        show yuri ldown
        camera master:
            easein 0.2 xalign 0.5
        "Washing her left arm up and down, I then proceed to lift the sleeve of her right arm, when-"
        show yuri rbandages
        camera master:
            easein 0.2 xalign 0.55
        pause 1.4
        _mc bd mh "I'm just imagining things, right...? Just being paranoid?"
        camera master:
            easein 0.2 yalign 0.1 xalign 0.5 zoom 1.7
        show bg:
            easein 0.2 blur 2.5
        "I look up from her arm to meet Yuri's eyes."
        show yuri ma b2a nb with say_dissolve
        "... The look she gives me in return only confirms my fears."

        play music pensive

        mc ml bf "Yuri..."
        $ autofocus.block("yuri")
        $ say_transition = True
        y mk b2b e2a "..."
        camera master
        show bg:
            blur 0.0
        show yuri me
        with Dissolve(0.2)
        "Yuri looks away, grimacing."
        mc mg bg nb "Yuri...!"
        $ autofocus.unblock("yuri")
        $ say_transition = False
        y b1d e1a na mh "What?"
        show yuri md
        "Yuri practically spits fire with that one word, causing me to pause."
        "Thinking on how best to respond, I speak up."
        mc mb "Err, what we discussed... don't you remember?"
        "..."
        $ autofocus.block("yuri")
        y rdown "..."
        "Yuri doesn't respond to my inquiry."
        show black
        hide yuri
        with NonBlockingDissolve(0.5)
        _mc mf "Why, Yuri...?"
        _mc ef mh "Do you not trust me?"
        y turned casual ketchup mg e3c "Melody."
        show yuri md e1a at i11
        hide black
        with NonBlockingDissolve(0.2)
        "Yuri's voice brings me back out of my thoughts."
        $ autofocus.unblock("yuri")
        y e3c mh "I understand your frustration."
        y b2b mb "... But please, don't attack me."
        y e2a mg "Things like this- Coping mechanisms-"
        show yuri ma rup at dip
        "She gestures to her bandaged arm."
        y b1a mg rdown "-I need them to get through the day."
        show yuri md
        "She keeps her gaze squarely away from me."
        show yuri mj
        mc bg ml "But-"
        y e3c mg "Please."
        show yuri md
        "..."
        _mc ef mh "I want to trust her."
        _mc eg "I really do, but..."
        mc ba mf "I... guess I should've expected this."
        $ autofocus.block("yuri")
        y e1a md b1d "..."
        "Yuri stares at me, with what I can only imagine to be... disdain."
        show black with NonBlockingDissolve(0.5):
            alpha 0.5
        _mc bf nb mf ea "But why...?"
        _mc ef bg mh "I just wanted to help her..."
        _mc ea ba thinking na "Am I being too overbearing...?"
        _mc ec "The Boss said not to do that, but..."
        "..."
        hide black with NonBlockingDissolve(0.5)
        mc ldown eg mj bi "Nevermind."
        mc ef ba ml "You're right; this is a delicate process."
        mc eg bi mg "I can't just expect you to change things around right away."
        mc ef mh "..."
        mc ea bg mb "You don't {b}have{/b} to rely on me, or let me know when you do this sort of thing, but..."
        "..."
        mc ef ml "I'd feel better if you did."
        mc eg mb "That's all."
        "..."
        y "..."
        "..."
        mc ea bf mh "..."
        "An uncomfortable silence overlays us."
        "..."
        mc ef ml nb bg "A- Anyway, um..."
        mc ea mg ba "Need me to find you some new clothes? I don't think you'll be getting those stains out anytime soon."
        "I point to her shirt and skirt."
        y e2a md "..."
        $ autofocus.unblock("yuri")
        y e3c mg "No, I've a spare outfit - If you could retrieve my bag...?"
        show yuri mj at thide
        hide yuri
        "I nod, turn around, and walk {nw}"
        show bg s_house_corridor_day with NonBlockingTransition(wipeleft)
        extend "out of the bathroom to fetch the clothes."
        y turned casual e1d mh "Oh, and... MC?"
        mc ml "Yeah?"
        y me e2a "..."
        y b1d e3c mb "I'm sorry for worrying you. For what it's worth, thank you."
        "I give her another nod in return, then exit the bathroom."

        scene bg s_bathroom_night_on with fade
        $ advance_date(minutes=6)

        "After some time, I return to the bathroom with a new set of clothes - I almost frown at the sight."
        _mc turned casual thinking mh "Her fashion sense... Why does she have three of the same outfit? Not that I'm one to talk, but these are all... She'd be right at home in the sixties, I think. Perhaps they were all hand-me-downs?"
        show yuri turned casual ketchup e1d md at t11
        "Yuri looks up at me after noticing my return."
        y mg "Ah, thank you."
        y e2a mh "I had been getting... uncomfortable in these stained clothes."
        show yuri md
        mc eg mb ldown "I don't blame you, that {i}can{/i} be pretty uncomfortable."
        "I place the clothes onto the side of the faucet."
        show yuri e1a
        mc ea "I'll let you get changed now. Come out when you're ready, yeah?"
        show yuri ma
        "Yuri gives me a quick nod, before I turn around and shut the door behind me."

        scene bg s_living_room with wipeleft
        show sayori turned casual at t11

        s mb "Hey Melly!"
        show sayori ma 
        mc turned casual ml nb "Oh! Uh..."
        show sayori md
        mc mb "Hey, Sayori."
        s mh lup "You okay? I noticed you carrying Yuri up here earlier."
        show sayori mk e1b
        "Sayori gasps."
        s ldown e1a b2a ml nb "Yuri didn't break her leg, did she?!"
        show sayori mj
        mc bb eb mg "No! No, of course not!"
        show sayori md b1a na
        mc bg eh md "We were just, well... Acting, really."
        mc ba mg ea na "But she kind of got into a mess during her acting, so she wanted a new set of clothes."
        mc ml "I let her use your shower, I hope you don't mind."
        s e3d mb "Nope! All's well that ends well, after all~!"
        show sayori ma
        stop music fadeout 2.0

    scene bg s_living_room
    show monika turned casual at i41
    show yuri turned casual at i42
    show sayori turned casual at i43
    show natsuki turned casual notail noband at i44

    if branches.is_current(branches.FATE):
        with wipeleft_scene
    else:
        with longfade

    $ set_date(minute=30, hour=19)

    "After the shootout ends, we all return back to the living room in one piece."

    if not branches.is_current(branches.FATE):
        "Yuri's now returned from the bathroom, it seems, while the rest of us waited patiently."
    
    hide yuri
    hide natsuki 
    hide monika
    hide sayori
    show cg sleepover 1
    camera master:
        anchor (0.3, 0.25) pos (0.48, 0.3) zoom 1.8
    with cg_dissolve
    play music pillow

    y turned casual mb "I never thought I'd enjoy myself so much."
    camera master:
        anchor (0.0, 0.325) pos (0.0, 0.4) zoom 2.2
    with cg_dissolve
    m turned casual mb ed "Same. It's definitely the most fun I've had in ages."
    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8 
    with cg_dissolve
    s turned casual e3d mb "So glad you're having a great time. I'm sure it'll get even better now that it's Melody's turn to choose an event!"
    camera master
    with cg_dissolve
    mc turned casual ed md "Ah. Ball's in my court now, hey?"
    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8 
    with cg_dissolve
    s mb e1a "Sure is."
    camera master:
        anchor (1.0, 0.325) pos (1.0, 0.4) zoom 2.1
    with cg_dissolve
    n turned casual notail noband b1d e3d mo "Better pick something good. My selection is going to be a tough act to follow."
    camera master
    with cg_dissolve
    mc thinking mg ea "Alright, then. What about.... Truth or Dare?"
    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8 
    with cg_dissolve
    s e1b mb "Ooh, spicy!"
    camera master:
        anchor (1.0, 0.325) pos (1.0, 0.4) zoom 2.1
    with cg_dissolve
    "Natsuki's bravado disappears like water down a drain."
    n mg nb e2c b1d "I... Errr..."
    camera master:
        anchor (0.3, 0.25) pos (0.48, 0.3) zoom 1.8
    with cg_dissolve
    y mb "Don't worry, Natsuki. I'm sure everyone's going to be tactful."
    y e1d mh lup "I think this could be an interesting exercise, as long as we all respect boundaries."
    camera master:
        anchor (1.0, 0.325) pos (1.0, 0.4) zoom 2.1
    with cg_dissolve
    "Natsuki doesn't look entirely convinced, but she doesn't protest either."
    camera master:
        anchor (0.0, 0.325) pos (0.0, 0.4) zoom 2.2
    with cg_dissolve
    m md ea "But of course, Yuri. Boundaries are always important."
    camera master:
        anchor (0.0, 0.325) pos (0.0, 0.4) zoom 2.2
    with cg_dissolve
    m mb eb "Shall we make ourselves comfortable?"
    camera master
    with cg_dissolve
    "Is it just me, or does Monika look a little pensive in spite of her going with the flow?"
    "Probably just me; everyone else is concurring with her and settling around the coffee table."
    "Well... everyone except Natsuki, who seems bent on making herself as inconspicuous as possible."
    show monika mb ea lpoint at i41
    show yuri ma at i42
    show sayori ma e1a at i43
    show natsuki md b1a na at i44
    hide cg
    with cg_dissolve
    m "I think it's only fair that MC begins."
    show monika ma ldown
    mc mb ldown "Sure."
    show natsuki e1a
    s mh "Move clockwise in a circle?"
    show sayori ma
    y mb ldown e1a "Sounds perfectly amenable."
    show yuri ma
    show monika mc
    mc thinking md ed "So... truth or dare, Monika?"
    show monika at i11
    hide yuri
    hide natsuki
    hide sayori
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "Monika hesitates."
    show monika eb bc with say_dissolve
    "Nope, I wasn't wrong after all. There's that pensive look, and it's intensifying."
    "When I'm on the verge of asking her if everything is okay, her mouth sets in a determined line and she makes her choice."
    m ea md "Truth."
    show monika mc ba with say_dissolve
    _mc ea mh "... not sure I was expecting that, but okay."
    mc mb ldown "Alright, then."
    mc mg "What's one thing you wish others knew about you?"
    m ec md bc "That being the popular girl at school, the scion of a wealthy family, isn't all that it's cracked up to be."
    show monika mc with None
    show monika at i41
    show yuri turned casual rup e1d me at i42
    show sayori turned casual md at i43
    show natsuki turned casual notail noband md at i44
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Silence reigns."
    _mc eg bi ma "I was expecting her to say something like 'I wish people would stop putting love confessions in my locker' or something..."
    _mc ec mh ba "Now it just feels like we're holding an intervention or something."
    show monika ec md
    "Monika takes a long breath as if she's about to say more, but more doesn't come."
    show monika ma ba
    "She seems to be a little better than before, though. Like this has been the first step to relieving herself of a considerable burden."
    "And I think that's absolutely worthy of praise."
    show monika ea
    mc ml nb ea "That... took courage."
    y mg "I absolutely agree."
    y e1a mb rdown "You do so much for everybody - meeting deadlines, targets, expectations. I don't think you get half the credit you deserve."
    show monika eb bb
    show yuri ma
    mc eh md na "We'll be sure to make up that deficit, won't we?"
    s mb "Totally. We love you, Monika. And if you're in difficulty of any kind, just know you can always come to any of us, just like how we can always rely on you!"
    show sayori ma
    show natsuki b3a ma at dip
    "Natsuki doesn't say anything, but holds Monika's hand and pats it reassuringly."
    show monika mb nb at dip
    "Monika lets out an almost awkward-sounding chuckle."
    $ autofocus.unblock("monika")
    m na ea ba "You're the best, you know that. All of you are. What would I ever do without you..."
    show monika ma
    mc mb ea "Hey, no sweat, Monika. We've got you."
    "The stagnant air steadily clears."
    show monika bc ec md at dip
    "And Monika does the same for her throat."
    m ea ba mb "So! Moving on..."
    show yuri md
    m md rhip "... Truth or dare, Yuri?"
    show monika mc with None
    hide natsuki
    hide sayori
    show monika at i21
    show yuri e1d me at i22
    camera master:
        align (0.5, 0.15) zoom 1.5
    show bg: 
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ autofocus.block("yuri")
    $ say_transition = True
    "She bats her eyelashes at Yuri as she does so. I can't help but chuckle - That winsome charm of hers is back."
    y b2b e2a mk "Um. D- Dare."
    show yuri ma with say_dissolve
    "She shuffles apprehensively in her seat."
    show yuri e1a
    m ec mb rdown "It's okay. Like I said, I won't push boundaries, so if this is too much, tell me, okay?"
    show yuri b1a
    show monika ma
    with say_dissolve
    "That seems to do the trick, as Yuri's tensed hands relax a touch."
    m ea mb lpoint "So, why don't you show us your secret talent, Yuri?"
    show monika ma
    show yuri e1b me nb
    with say_dissolve
    "Yuri goes a little pale."
    show monika ldown
    y e2b mb "S- Sure."
    show yuri ma with None
    camera master
    show bg:
        blur 0.0
    show monika mc at i41
    show yuri e3c md na b1d at i42
    show sayori turned casual at i43
    show natsuki turned casual notail noband md at i44
    with Dissolve(0.2)
    $ say_transition = False
    "Yuri fetches her bag from beside her, rummaging through it."
    show yuri e1a b1a
    "Out of it she draws an elegant box, which she opens like a dark tome of arcane mysteries to reveal..."
    show sayori me
    mc ml thinking "Tarot cards?"
    $ autofocus.unblock("yuri")
    y lup nb e2a mh "Y- Yes. I, uh, do readings. Mostly for myself, to help guide me through... particularly difficult situations."
    y e1d mb na "You'll be surprised, what power these seventy-eight sigils hold." 
    y rup e3c mh "How much they can reveal about a person or a circumstance."
    show yuri ma
    show monika ma
    "All of us marvel at the beautifully illustrated cards."
    "At their eldritch imagery - all vampires, werewolves, Gothic architecture and benighted dreamscapes." 
    "So full of hidden meaning and sinister symbolism."
    mc eg mb ldown "Truly are you a lady of talent and taste, Yuri."
    show sayori ma
    y shy "You're too kind..."
    y turned lup e1a mb "I'm no expert diviner, mind you. But I know enough to interpret what the cards symbolise and apply the meanings to the matter at hand."
    show yuri e1d md
    $ autofocus.unblock("monika")
    m mb "How about you surprise us, then, Yuri? Let's see what your deck has to say about each of us in turn."
    show monika mc
    show natsuki e2a
    y mg nb "A- Are you absolutely sure? Its truths can be hard to swallow sometimes. I don't want to embarrass anybody."
    show yuri me
    s b2c mb "Aw, we're among friends, aren't we? We won't judge each other, right?"
    show sayori md
    m bc md "Last thing I'd ever do to those I care about."
    show monika mc
    show yuri e1a ma na
    mc ea "Indubitably."
    show monika ea ma ba
    show sayori b1a
    mc mg "Not going to lie - I'm very curious to see what the cards say about me."
    s mn e3d "Same! You know, they might just end up cutting straight to the truths and help all of us avoid performing stupid dares."
    show sayori ma
    m bb eb mb "Ahahaha. That's one way of looking at it."
    show natsuki e1a
    m rhip ea md "You okay there, Nat? You've been pretty quiet thus far."
    show monika mc
    show natsuki ma
    "Natsuki attempts a smirk, although it's not as jaunty or confident a smirk as what she normally pulls off."
    n b1d e1d mn "Eh, no harm trying. No skin off my nose. Like a stack of cardboard's going to be able to read my mind."
    show natsuki ma
    y ldown mg e3c "A- Alright then. Here goes."
    show yuri ma with None
    hide natsuki
    hide sayori
    hide monika
    show yuri at i11
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "Yuri's hands deftly flutter, shuffling the cards with the expertise of a professional croupier."
    "Once, twice, thrice she does this."
    show yuri e1a with say_dissolve
    "Before spreading them out in a near-perfect semicircle."
    y mb "Pick a card. Any card." # forsenCD PICK A CARD ✨ forsenCD ANY CARD ✨ forsenCD THE 2 OF WIVES? ✨ forsenCD EXCELLENT CHOICE ✨ https://www.youtube.com/watch?v=Al5uGPXSZ4s
    show yuri ma with None
    camera master
    show bg:
        blur 0.0
    show yuri at i42
    show monika turned casual at i41
    show sayori turned casual at i43
    show natsuki turned casual notail b2a e1b mn noband at i44
    with Dissolve(0.2)
    $ say_transition = False
    "I reach forward, draw one from the spread and flip it over."
    mc ml bd "... What?"
    show sayori md
    show yuri e1d b4 md
    show natsuki b2b mo e3d nb at hop
    n "Pfffffftttt. Hahahahah!"
    n e3b b2a mc "I think I might have been wrong about this Tarot business, after all."
    show yuri b1a
    n cross b2b mo e3d na "Because that card definitely suits Melody. Hee hee hee!"
    s e1d b1d mh "Aw, c'mon, Nat. Don't be a meanie."
    show sayori md
    show natsuki e3a b2a mn
    $ autofocus.unblock("yuri") # TODO fool
    y mb "Appearances can be deceptive, MC. The Fool is actually one of the Tarot's most positive cards."
    show natsuki b3a ma e1a
    show sayori e1a b1a
    y e1d mh "It symbolises a carefree, spontaneous spirit, a mind that is both open and curious."
    y mb "Somebody on the brink of a momentous journey that promises much opportunity and potential."
    show yuri ma
    mc ba nb "If you put it that way, I suppose it sort of does apply to me."
    show natsuki md 
    mc ef mg na "I took a leap of faith and joined this Club pretty much on a whim, keeping an open mind."
    mc ea mb "And look where that's gotten me now. It's been quite the ride, full of amazing discoveries."
    m mb "We're all the better for your membership, MC."
    show monika ma
    s mb "Totally."
    show sayori ma
    n turned lhip mi e3c "Hmph. I prefer the on-the-face-of-it interpretation, but whatever."
    show natsuki ldown e1a b1a ma
    s mb e3d "My turn! My turn!"
    show sayori ma with None
    hide natsuki
    hide monika
    show yuri e1a md at i21
    show sayori e1a md at i22
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ autofocus.block("yuri")
    $ say_transition = True
    "Sayori reaches over and draws..."
    s mg "Hmm. What's this mean?"
    show yuri ma
    show sayori md
    with say_dissolve
    "Yuri smiles."
    y mb "The Six of Cups indicates a strong connection with your inner child."
    y e3c mh "You love revisiting happy memories from the past, reconnecting with old friends and reminiscing about fun times you shared."
    show sayori ma
    y e1d mb "And you always give people the benefit of the doubt, rarely if ever expecting anything in return."
    show yuri ma
    s mb e3d "Ehe~ That sounds exactly like me!"
    show sayori ma with None
    show yuri e1a at i42
    show sayori at i43
    show monika turned casual at i41
    show natsuki turned casual notail noband at i44
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    m mb "Down to a tee."
    show monika ma
    show sayori e1a
    mc ed md "You know, the bit about reconnecting with old friends is especially relevant since I joined the Club."
    $ autofocus.unblock("sayori")
    s mb "It is, isn't it? And I don't want what we share to ever end, Melody."
    show sayori b2b ma
    mc eg mb "It won't. Not by a long shot."
    "We relish the fond moment for a bit, before letting Monika have her turn."
    hide natsuki
    hide sayori
    show yuri at i22
    show monika mc at i21
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    m md "What do we have here...?"
    show monika ma
    y lup rup e3d mb "Aha. Wouldn't have expected anything less."
    y rdown e1d mh "The Queen of Wands - a social butterfly, passionate and enthusiastic, a mover and shaker."
    y e1a mb ldown"Someone who is determined to make a difference, a natural born, inspirational leader, full of energy and charm."
    show yuri ma with None
    show yuri at i42
    show sayori turned casual e3d at i43
    show monika at i41
    show natsuki turned casual notail noband at i44
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    s mn "Ha. That's our Monika!"
    show sayori ma
    show monika bb eb nb
    "Monika blushes."
    $ autofocus.unblock("monika")
    m mb ea na ba "These cards sure know how to flatter a girl."
    show monika ma
    $ autofocus.unblock("yuri")
    y mb "No flattery; only truth."
    show yuri md b1d
    "Yuri abruptly becomes very serious."
    show natsuki md
    show sayori e1a md
    show monika mc
    y mg e3c "There is one aspect of the Queen of Wands that often goes overlooked, mind you."
    y e1d mh lup b1a "While bold and outgoing, she is also in touch with her inner self - the lesser known aspects of her being that people aren't aware about."
    y e1a mb "Don't be afraid to show this 'shadow side' of yourself, Monika. Doing so is healthy; it will help you connect with others on a deeper level."
    show yuri ma
    "This hearkens back to the 'truth' Monika told earlier during her turn. Along with whatever else might have gone unsaid."
    show monika eb
    "Once again, she looks a tad reflective. But only for a few seconds."
    show sayori ma
    m ec md "I'll definitely keep that in mind, Yuri. Thank you for your advice."
    show monika ea ma
    show yuri e2a
    "With that, Yuri segues back into her usual demure self."
    y mb ldown "Not a worry. I'm always glad to be of help."
    show yuri ma
    mc ea mg "Three for three. I'm impressed."
    show yuri e1a md
    show monika bc
    "Everyone turns to look at Natsuki."
    m mb "Can we make it four for four?"
    show monika ma
    show natsuki e3c b1d mn
    "Natsuki snorts derisively."
    n b3a e3c mi "You're not going to make a statistic out of me, much less a believer."
    n e1a mc "I'll bite, if only to prove that these cards aren't the hands of fate."
    show natsuki md with None
    hide sayori
    hide monika
    show natsuki b1a at i22
    show yuri ma at i21
    camera master:
        align (0.5, 0.23) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ autofocus.block("yuri")
    $ say_transition = True
    "She reaches forward and draws..."
    stop music fadeout 3.0
    y lup e2a mg b1d "Um."
    show yuri md
    n b4 mg "What?"
    show natsuki md
    y mb b2b "A- Are you sure you want to hear this, Natsuki?"
    show yuri md
    n mm e1d b1d "Don't keep me in suspense, Yuri."
    n cross b3a e3c mi "Just get it over with already so we can return to the main game. We're getting more than a little sidetracked."
    show natsuki b1a mj e1a
    show yuri b1a me e3c ldown
    with say_dissolve
    "Yuri sucks in her breath."
    y b1d e1a mg "The Seven of Swords. The card of secrets, deception, trickery."
    y lup e2a mh b1a "Of trying to get away with something behind other people's backs."
    y mg e3c b1d "A high stakes game with immense risk of discovery."
    show yuri md with say_dissolve
    "I can practically hear more than a few eyebrows raising."
    "Mine sure did."
    show yuri e1a with say_dissolve
    "Yuri is dead serious once again."
    y mg "Whatever's going on, Natsuki, tread carefully."
    y ldown b1a mh "The effort at covering things up will not be worth it."
    show yuri md with None
    show yuri at i42
    show natsuki at i44
    show sayori turned casual md at i43
    show monika turned casual mc at i41
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Natsuki says nothing for several seconds."
    $ advance_date(seconds=16)
    show natsuki ma
    "When she finally speaks again, it is through a thin, tight smile."
    show sayori ma
    $ autofocus.unblock("natsuki")
    n turned mb e1d b1d "Three for four. Close, Madame Zorra, but no cigar."
    n e1a b3a mh "Can we get back to Truth or Dare now?"
    show natsuki ma
    show monika ma
    "And that we do, if only to make the atmosphere less tense."
    "You could practically cut through that tension with a knife."
    show sayori md
    $ autofocus.unblock("yuri")
    y e2a mg b1d "So, Sayori..."

    play music elegant_s

    show sayori ma
    y e1a b1a mb "Truth or dare?"
    show yuri ma
    s e1b mg "Ooh!"
    s e3c mj "Hmm."
    s e1a mb "Truth!"
    show sayori ma
    y e2a mg "Okay, hmm."
    show sayori md
    y e1a mb "What's the most trouble you've been in?"
    show yuri ma
    s mh "Hmm... I think Melody knows this one."
    show sayori ma
    "I wince."
    "I have a feeling I know what she's talking about."
    n cross b1a mc "Oh, is this the time that you disappeared for an entire day?"
    show natsuki ma
    s lup e2a b2b mb nb "Y- Yeah. Ehe~"
    show sayori ma
    "Well that sounded just a little forced."
    s e1a b1a na mh "So I was climbing a tree just before school, and I..."
    s e2b b2c mb "Kinda got stuck up there. For basically the whole day."
    show sayori ma
    n turned b3a mh "Yeah, I was wondering where you'd gone, because I saw you at school, but then not in class."
    show natsuki ma
    s ldown b1a e2a mh "Well, that."
    show sayori b2b ma with None
    if preferences.language is None:
        $ auto_advance_date_mult = 0.0
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    "She seems to grimace a little. It must not be a very fond memory."
    _mc ec mh "Hell, I remember it pretty clearly."
    _mc eg "Not too long after we stopped talking, she just went and disappeared. Of course I was concerned; there were rumours."
    _mc bi "Rumours that she'd been kidnapped or something."
    _mc ef "I'd..."
    _mc ba "I'd be lying if I said I wasn't scared."
    _mc eg ma "And then someone found her in a tree."
    _mc ea "Hell, they almost called the fire department to help get her down."
    _mc mh "But that didn't make it any less shocking. I didn't even find out she'd come back until the following day."
    _mc ef bg "... It really did shake me back then."
    _mc eg bi "I remember seeing her the following morning, and I had to resist the urge to race over and hug her."
    _mc ec ba "Even now, I still remember that moment of relief, seeing her alive and well, intertwined with the feeling of pain."
    _mc ef "The pain of knowing I can do nothing."
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    hide black with NonBlockingDissolve(0.2)
    mc ed md "Alright. We're into Round Two, and I think it's only fair that we up the intensity."
    show sayori e1a b1a ma with None
    hide sayori
    hide natsuki
    hide yuri
    show monika at i11
    camera master:
        align (0.5,0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("monika")
    mc ea mb "I believe it's your turn once again, Monika."
    mc ml "Truth or dare?"
    m mb "I'll dare to 'dare,' methinks."
    show monika ma with say_dissolve
    mc ed md "Alright then."
    show monika mc with say_dissolve
    mc ea mb "Pick one of the others and embrace them."
    hide monika
    show sayori turned casual mn e3d at i43
    camera master:
        xalign 0.75 zoom 2.0
    show bg:
        blur 3.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("monika")
    "Sayori squeals amusedly."
    hide sayori
    show natsuki turned casual notail noband b1d e3c mb at i44
    camera master:
        align (1.0, 0.25)
    with Dissolve(0.2)
    "Natsuki slowly shakes her head, but her mouth is hanging open, somewhere between a laugh and a stunned mullet."
    show yuri casual shy ne at i42 
    camera master:
        align (0.25, 0.1)
    with Dissolve(0.2)
    "Yuri flushes pink and gazes down into her lap."
    show natsuki turned casual notail noband ma e2a at i44
    show bg:
        blur 0.0
    camera master
    show sayori turned casual e3d at i43
    show monika turned casual nb mc at i41
    show yuri casual shy ne at i42
    with Dissolve(0.2)
    "As for Monika herself, she stammers..."
    m nb mb bb "Em- Embrace, you say."
    show monika mc
    mc md ed "Well, I did say we'd be upping the intensity."
    mc ea ml "But if this is too far, if it's making you uncomfortable, you can always forfeit."
    show monika eb ma
    "Monika smiles awkwardly - such a different sort of smile from what I normally see from her."
    m rhip ec bc md "I'm not... Ah, fine, I might be a little."
    m ea mb ba na "But, I'll do it."
    show monika ma rdown with None
    show monika:
        i21
        xzoom -1
    show yuri at i22
    camera master:
        align (0.5, 0.15) zoom 1.5
    show bg:
        blur 2.0
    hide natsuki
    hide sayori
    with Dissolve(0.2)
    $ say_transition = True
    "She turns to face Yuri."
    $ autofocus.block("yuri")
    $ autofocus.block("monika")
    $ autofocus.zorder = False
    m md "May I hug you, Yuri?"
    show monika ma zorder 3
    show yuri turned lup b2b e3c ma nd
    with say_dissolve
    "Yuri's face reddens further, but she slowly returns Monika's smile and nods."
    y e2b mh "O- Okay."
    show yuri e2a md:
        easein 0.8 xoffset -200
    camera master:
        easein 0.8 xalign 0.35 zoom 1.7
    show bg:
        easein 0.8 blur 2.5
    "She slowly sidles up next to Monika."
    show monika lpoint with say_dissolve
    "Monika tentatively hovers her hand above Yuri's shoulder."
    stop music fadeout 3.0
    m md eb "I'll start with... rubbing your shoulders."
    show monika ma ec ldown
    y e2b mg ldown "Y- Yes. I'll... lean into you."
    show monika zorder 2:
        matrixtransform RotateMatrix(0, 0, 6) matrixanchor (0.5, 0.75) yoffset 0
    show yuri ma nb rup zorder 3:
        matrixtransform RotateMatrix(0, 0, -17) matrixanchor (0.5, 1.0) yoffset 25 xoffset -300
    with Dissolve(0.2)
    "She gently rests her head on Monika's neck."
    show monika eb with say_dissolve
    "Monika places her hands on both of Yuri's shoulders."
    "There is something motherly and loving in Monika's eyes."
    show yuri e3c b1a
    show monika ec
    with say_dissolve

    play music stars

    "Yuri closes her eyes and I see a serene smile play on her lips."
    "I thought this might range anywhere from awkward to titillating, but no." 
    "The end result is nothing less than sweet."
    "Yuri's happy expression and Monika's parental nurturing."
    "Monika's fingers then run along Yuri's hair, their conjoined fibres..."

    scene black
    camera master
    with yuri_pov()
    $ set_pov("y")
    $ autofocus.zorder = True
    $ autofocus.unblock("yuri")

    "... intermingling strands of midnight and sunlight, wrapping around me like a cocoon."
    "I feel her stroke our conjoined tresses and I feel a great sense of protected satisfaction."
    "Her shielding me from everything that harms."
    "I can't help but feel safe."
    "I rest my hands around her waist."
    "My eyelids start to fall closed, pulled down by reassuring intimacy." 
    "Swept over by a feather of golden dust and joyous parental nurturing."
    "Something I love dearly."
    "I feel sleep pull at me."
    "Monika can surely see my eyelids closing, the dark pull of Hypnos taking hold of my lashes."
    "I expect her to berate me for this."
    "But she neither lashes out at me nor resists it, instead continuing to stroke my hair and murmuring softly."
    "I just hover there, feeling appreciated and loved."
    "Monika leans down and whispers softly into my ear, her warm breath on my cheek."
    m turned casual mb ec "Fall right asleep if you want, Yuri. It's perfectly okay."
    y turned casual mb e3c b2b nb "You're so good to me, Monika. Thank you."
    m md "Anytime, Yuri. Anytime."
    "The soft strains of Clair De Lune play in my ears and I slip out of consciousness."

    scene bg s_living_room
    show monika turned casual:
        i41
        xzoom -1 matrixtransform RotateMatrix(0, 0, 6) matrixanchor (0.5, 1.0) yoffset 100
    show yuri turned casual e3c rup zorder 4:
        i42
        matrixtransform RotateMatrix(0, 0, -12) matrixanchor (0.5, 1.0) yoffset 80 xoffset -140
    show sayori turned casual e2a at i43
    show natsuki turned casual notail noband e2c md at i44
    with mc_pov(True)
    $ set_pov("mc")

    "After watching Yuri's eyes close and her breathing slow, I quietly assume she's fallen asleep."
    show sayori:
        alpha 0.0
    show natsuki:
        alpha 0.0
    camera master:
        align (0.0, 0.2) zoom 1.7
    show bg:
        blur 2.5
    with Dissolve(0.2)
    "I watch Monika, stroking the slumbering Yuri with such gentleness, and I can't help but smile."
    show monika:
        alpha 0.0
    show yuri:
        alpha 0.0
    show sayori:
        alpha 1.0
    show natsuki:
        alpha 1.0
    camera master:
        align (1.0, 0.23) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ autofocus.block("natsuki")
    "Sayori, and I sit there in silence, marvelling at Monika's tender affections, while Natsuki still flusters in the corner."
    show sayori e1a md with say_dissolve
    "Eventually, Sayori pipes up in a low whisper."
    show natsuki e1a me with say_dissolve
    s lup mg "Shall we step to the side so we don't wake her?"
    show sayori ma with say_dissolve
    n mc "Yeah! I mean..."
    extend e2a b1d mb " Yeah."
    show natsuki ma nb with say_dissolve
    "Natsuki quickly checks herself after initially forgetting to lower her voice."
    mc turned casual ml "What about Monika?"
    show monika ea:
        alpha 1.0
    show yuri:
        alpha 1.0
    show sayori:
        alpha 0.0
    show natsuki:
        alpha 0.0
    camera master:
        align (0.0, 0.2) zoom 1.7
    show bg:
        blur 2.5
    with Dissolve(0.2)
    "Monika looks up at us slowly, and mouths at us."
    m ed mb "Go on, don't worry about me. I'll just stay here with Yuri. You go ahead."
    show monika ma with None
    show sayori:
        alpha 1.0
    show natsuki:
        alpha 1.0
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    s mb e2a "Okay~ Thanks Monika!"
    show sayori ma at thide
    hide sayori
    show natsuki at thide
    hide natsuki

    scene bg s_kitchen_day
    show sayori turned casual at i22
    show natsuki turned casual notail noband at i21
    with wipeleft
    show sayori md
    window auto show
    $ autofocus.unblock("Monika")

    show sayori mg rup at t55
    show natsuki md
    s "Oh, but-"
    show sayori me
    "She pauses for a moment."
    s mb "I'll be back."
    show sayori e2c rdown ma at rhide
    hide sayori
    show natsuki e2c at t11
    "I shrug as Natsuki raises an eyebrow, but neither of us say anything as Sayori bounds out of the room."
    "..."
    show natsuki e1a
    camera master:  
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    n cross b3a mh "So... Seen any good movies lately?"
    show natsuki mj with say_dissolve
    mc turned casual mj ec bi "Was that really the best one up there?"
    n e2a mg b1a "... Yeah..."
    show natsuki md with say_dissolve
    mc ef ml ba "That's sad."
    n turned e1d b1d mg "I don't see you doing any better."
    show natsuki me with say_dissolve
    mc ec bi mg "I didn't try."
    n e1a b3a mb "Exactly."
    show natsuki ma with say_dissolve
    mc thinking ea ba "So who's worse, the one who's terrible at small talk when they try, or the one who doesn't bother?"
    n cross b4 e1d mh "The one who doesn't bother? Obviously?"
    n b1a mg "You're not gonna improve if you don't-"
    n turned e1d b1d mm "You know what? We're talking about this later."
    n e1a mh "We're gonna fix..."
    n rhip lhip e1b b3d mg "This."
    show natsuki md with say_dissolve
    mc ec ml ldown ba "You just gestured to all of me."
    n ldown rdown e1a b3a mc "Yes."
    show natsuki ma with say_dissolve
    "I chuckle."
    _mc ea ma "Her heart's in the right place, I guess?"
    show natsuki b1a md at i21
    show sayori turned casual mn e1d b1d at i22
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "At that point, Sayori re-enters the room, grinning ear to ear."
    mc ec ml "Should we be concerned?"
    s mb "Always~!"
    show sayori e3d ma b1a
    "I have half a mind to step back out into the living room, but decide against it."
    s e3d mb "Alright, back behind the trigger."
    show sayori lup rup e1d b1d ma
    "Sayori rubs her hands gleefully."
    s mh b1a e1a ldown rdown "So, Nat, truth or-"
    show sayori md
    $ autofocus.unblock("natsuki")
    n e2a lhip mh "Dare."
    show natsuki ma
    s mg b2b nb "Aw, what? Again? You're no fun."
    show sayori md
    _mc mh "There she goes again. Opting for a dare almost immediately."
    "My mind can't help but wander back to Yuri's tarot reading."
    _mc ea thinking "What could Natsuki be so desperate to avoid exposing?"
    show sayori ma na b1a
    n mb e1d b1d ldown "Pipe down already. Everyone knows dares are more fun to watch than truths."
    show natsuki ma
    "She arguably has a point."
    n e1a mc b3a "So go on, then. Have your fun."
    show natsuki ma with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("natsuki")    
    $ autofocus.block("sayori")
    n b1d e1d mb "I can take anything you can throw at me."
    show natsuki e1a b1a ma
    s mo b1d e1d "Alright then."
    show natsuki md
    show sayori e3c b1b md:
        yoffset 80
    camera master:
        align (0.7, 0.7) zoom 1.6
    with Dissolve(0.2)
    pause 0.4
    show natsuki b3a me
    show sayori lup e1d b1d ma:
        matrixanchor (0.5, 1.0) matrixtransform RotateMatrix(0, 0, -10)
        xoffset -160
    camera master:
        zoom 1.7 align (0.35, 0.5)
    show bg:
        blur 2.5
    with Dissolve(0.15)
    pause 0.1
    show sayori ldown e3d ma b1a:
        matrixtransform None offset (0, 0)
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.15)
    $ say_transition = False
    "Reaching into a nearby jam jar, Sayori smears a dollop of the stuff onto Natsuki's elbow, smirking to herself gleefully." # im stuff
    $ autofocus.unblock("sayori")
    s mb "Bet you can't lick that off~"
    show sayori e1a b1a me
    show natsuki rhip ma
    with None
    hide sayori
    show black
    with NonBlockingDissolve(0.5)
    "Wordlessly, Natsuki lifts her elbow to the level of her mouth."
    "She tilts it inward."
    "There's an audible pop, followed by another, and..."
    s turned casual nb mg "No way."
    show sayori me at i22
    show natsuki rdown b1a
    hide black with NonBlockingDissolve(0.5)
    mc ml nb "Did you really just...?"
    $ autofocus.unblock("natsuki")
    n cross b3a mo e3d "Should have taken you up on that bet."
    show natsuki ma
    "Sayori and I can scarcely believe what we've just seen, but it is what it is."
    "Natsuki just dislocated both her shoulder and elbow to lick the jam off."
    s mh b1d rup "How the heck did you-"
    show sayori me
    $ autofocus.force_focus("natsuki")
    n turned b1a mb e2c "I was born pretty flexible. Can pop my joints just by flexing the tendons. It's come in handy on more than one occasion."
    window hide None
    pause 0.9
    show natsuki b2a e2d nb me
    pause 0.07
    show sayori rdown b1a md
    pause 0.04
    $ autofocus.restore_focus("natsuki")
    show natsuki e2a b1d md
    pause 0.95
    show natsuki ma
    window auto show None
    "She laughs nervously."
    n mn na e1d b1d "But... Enough about me already, hey? Time to put MC through her paces!"
    n mc b3a e1a "And Sayori, was that some awesome jam or what? I'll have to note down that brand so I can put some in my pastries!"
    show sayori me b4 
    show natsuki ma 
    with None
    show natsuki:
        alpha 0.0
    show bg:
        blur 3.0
    camera master:
        align (0.75, 0.2) zoom 2.0
    with Dissolve(0.2)
    "Sayori and I glance quizzically at each other, but decide to play along."
    show sayori:
        alpha 0.0
    show natsuki b1d:
        alpha 1.0
    show bg:
        blur 2.0
    camera master:
        zoom 1.5 align (0.25, 0.25)
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("natsuki")
    "Natsuki composes herself and turns to face me."
    n e1a mh b1a "So what's it gonna be?"
    show natsuki ma with say_dissolve
    "With the memory of my previous ordeal still fresh in my mind, the answer is obvious."
    mc mb na ldown "I'll opt to tell the truth this time."
    n cross mb e1d b1d "Ho? Maybe I'll be able to prove myself wrong about dares being more fun to watch."
    show natsuki ma with say_dissolve
    mc ec mj "Joy."
    n turned mc b3a e1a "Alright, MC. What's your guiltiest pleasure?"
    show natsuki ma with say_dissolve
    "Now it's my turn to smile."
    show natsuki me with say_dissolve
    mc ed md "Parfait Girls, hands down."
    camera master
    show bg:
        blur 0.0
    show sayori e1b mn b1a:
        alpha 1.0
    show natsuki b1d e1b
    with Dissolve(0.2)
    $ say_transition = False
    show sayori xd b2b mb nb at dip
    "Sayori lets out a guffaw that she frantically turns into a cough upon seeing Natsuki's expression."
    show sayori mo
    $ autofocus.unblock("natsuki")
    n cross mb e1d b1d "In a fighting mood, are we?"
    show natsuki mj
    mc mg bd ea "I said guiltiest PLEASURE, okay? Which implies that it's pleasurable. So don't take it so hard."
    n e2a md "Ugh."

    scene black
    show layer master:
        align (0.5, 0.2) zoom 2.0
    show bg s_living_room:
        blur 3.0
    with yuri_pov(True)
    $ set_pov("y")
    $ autofocus.block("monika")
    $ say_transition = True

    call close_eyes(0.0) from _call_close_eyes_2
    
    "As my eyes drift open, I realise I'm... being held."
    "Hands softly hold me and support my body."
    "Whose fingers rest upon me?"
    m turned casual mb ec "Wakey wakey, Yuri."
    show monika ma at i11
    hide black
    call open_eyes(1.0) from _call_open_eyes_2
    y turned casual nb mg e1d "M- Monika?"
    m ed mb "Yes Yuri, it's me."
    show monika ma with say_dissolve
    "Slowly memories of earlier trickle into my consciousness."
    y e1b mi "I- I fell asleep on you?"
    y e3c mk b2b "I'm so sorry Monika... Really, I..."
    m mb ea "Hush, Yuri. Everything is fine. It was nice actually. You slept very peacefully."
    show monika ec ma with say_dissolve
    "Monika's tone only just registers."
    "Maternal and soft. Like cotton candy upon my ears and feathers upon my body, keeping me supported."
    show monika mc ea with say_dissolve
    "And I notice what is {i}actually{/i} supporting my head."
    show monika ed ma with say_dissolve
    "Monika lets out a slight chuckle."
    m mb "Don't worry about it, Yuri. Seriously though, it's nice that you felt comfortable enough to sleep on me."
    show monika ma with say_dissolve
    y e2a mb nd "And I do feel truly comfortable, Monika."
    m mb "Lovely."
    m ea md "What do you want to do now, Yuri?"
    show monika mc with say_dissolve
    y mg e1d nb b1a "W- Well, where are the others?"
    m mb "They moved to the kitchen in order to keep the noise down for you, Yuri."
    m eb md "But it's your choice. If you're tired... you can sleep for a little longer."
    show monika ea mc with say_dissolve
    y e3c mb b2b "N- No... It's okay."
    y b1a na mg "We shouldn't be keeping them..."
    y e1a mb "But thank you. I mean it."
    m ec mb "My pleasure."
    show monika ma with say_dissolve
    "She softly strokes the hair out of my eyes."
    "Her hair brushes my skin as she gently lifts me to a sitting position."
    show monika ea mc rhip with say_dissolve
    "She places her hand on my knee."
    m md "Come along, Yuri."
    show monika ma with say_dissolve
    y e2a b2b mb "Y- Yes, let's."
    show layer master
    show monika rdown
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She takes my hand and helps me sit up."
    show monika at t44
    show melody turned casual eg at t43
    show natsuki turned casual notail noband b1d e2a at t42
    show sayori turned casual e2a at t41 
    "Hearing the commotion, I watch the girls make their way back to their seats."
    "For some reason, they seem to be holding in chuckles. I assume whatever conversation they'd just had was quite something."
    show melody ea
    show sayori e1a
    n cross e1d b1d mb "Well, look what the cat dragged in."
    n b3a mc e1a "How are the doting lovebirds?"
    show natsuki ma
    $ autofocus.unblock("monika")
    m nb mb eb "A- Ah... Well enough. In any case, I believe we're about ready to rejoin the game."
    show monika ma
    "My cheeks burn."
    _y shy ne "L-Lovebirds? I- I shouldn't have fallen asleep... if Monika suspects anything-"
    show monika ea na
    "-But Monika simply beams at me."
    m md bc "Also, we aren't lovebirds."
    m lpoint ba mb "I was just giving Yuri a hug - She just happened to be tired."
    m md "Right?"
    show monika ma ldown
    y turned e3c nb b1a "Oh... Yes. I was tired, and Monika made me feel comfortable and warm."
    show sayori md
    n turned lhip e2a mh "Riiight."
    show natsuki ma
    s lup mh "It's called harmless cuddling, Nat. You should try it yourself sometime."
    show sayori ma
    show natsuki b1d e3c ldown me at dip
    show monika bb
    "Natsuki sighs."
    show natsuki md
    "I can't help but feel a little better."
    "And a whole lot happier."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _y b2a e2a ma nc "I... I never knew Monika cared that much about me."

    if branches.is_current(branches.FATE):
        _y e3c b2b "That anyone cared about me, aside from Melody."
    else:
        _y e3c b2b na md "That anyone cared about me."

    _y e1a ma b1a na "But... It's lovely nonetheless."

    scene bg s_living_room:
        blur 2.5
    camera master:
        align (0.25, 0.1) zoom 1.7
    show yuri turned e2a casual at i42
    with mc_pov(True)
    $ set_pov("mc")

    "After seeing Sayori's handiwork, it's all I can do to keep myself from giggling."
    _mc turned casual eg "I can't believe I didn't think of it myself..."
    m turned casual mb ldown "Tell me, MC, what is your happiest memory?"
    show monika mc ldown at i41
    camera master
    show bg:
        blur 0.0
    show natsuki turned casual notail noband at i44
    show sayori turned casual at i43
    show yuri e1a
    with Dissolve(0.2)
    "Monika opens the floor to return to the game, giving me a chance to drag my eyes away from Yuri."
    mc ml ea "Oh. That was very much not what I was expecting."
    show monika ma
    "The grin returns to Monika's face."
    m bc mb "True, but what's life without a little subversion?"
    show monika ma ba ed
    mc ef ml bi "True. Well, if I had to pick a single moment..."
    mc ea mg ba "I think it would be the time my family threw a barbecue."
    m md ea "Oh?"
    show monika mc
    mc eh md "Yeah. It was great. We invited all the neighbours over, I got some friends to hang out, and we had all the food we could possibly want."
    mc ea mb "Oddly enough, because it was so long ago, I don't remember all of it, but it's still the first thing to come to mind when I think of happy memories."
    mc thinking ef bi ml "I would have been... what, five?"
    mc ea mg bb "But honestly, it does stick out to me."
    show sayori md
    mc mb ldown ba "Hey, Sayori, do you remember that?"
    show yuri md:
        alpha 0.0
    show natsuki md:
        alpha 0.0
    show monika:
        alpha 0.0
    camera master:
        align (0.75, 0.2) zoom 1.7
    show bg:    
        blur 2.5
    show sayori b2b ma
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("sayori")
    "I glance her way, but all she does is give me a half-smile."
    s e2a mb lup "I... don't think so, no."
    s e1a b1a mg "It might have been something before we met."
    show sayori ma ldown with say_dissolve
    mc ml "... Maybe it was."
    camera master
    show bg:
        blur 0.0
    show yuri md:
        alpha 1.0
    show natsuki md:
        alpha 1.0
    show monika:
        alpha 1.0
    with Dissolve(0.2)
    $ say_transition = False
    mc ef mg "Well, there you have it."
    m md "So, you haven't had any happy memories since?"
    show monika ma
    show natsuki ma
    mc mb ea "Oh, I most certainly have. I have memories with all of you, of course."
    show yuri ma
    mc eh md "And I'm sure that tonight will be one to remember as well."
    y mb "Yes, I'm sure it will be."
    y e1d mh lup "So, would it be my turn?"
    show yuri md
    $ autofocus.unblock("sayori")
    s mg "Yeah, I think it is."
    show sayori ma
    y e2a b1d mb "Ah, so, who to ask?"
    show yuri ma
    mc ed md "Ha, well the point is to spring it on them, not just ask them politely."
    y mg "That is true. In that case..."
    y ldown e1a mb b1a "Sayori. Truth or dare."
    show yuri ma
    s e1b b2b mk "Ah- Me?"
    show sayori me
    y mg e1d "I did say your name."
    _mc ec ma "Geez, Sayori, way to be caught off guard."
    s e2a mb "Oh, ah..."
    show sayori me
    "Her expression melts into confusion, and a little concern."
    show yuri me
    s mb b2c "I think... I'll have to go with dare."
    show sayori e1a b1a ma
    y mg lup e2c "Oh, I see."
    y mb b1d e2a "I don't have anything for this one - That's unfortunate."
    show yuri e1a md
    "She glances around the room, and locks eyes with me."
    _mc mh "I know what I have to do."
    _mc eg bi "I don't know if I had the strength to do it, but it needs to be done."
    _mc eb bd mh "Alright me, for the sake of the party!"
    show sayori:
        alpha 0.0
    show natsuki:
        alpha 0.0
    show monika:
        alpha 0.0
    camera master:
        align (0.25, 0.1) zoom 2.0
    show bg:    
        blur 3.0
    show yuri ldown e1d b1a md
    with Dissolve(0.2)
    "Leaning over to her, I whisper something in her ear."
    show sayori:
        alpha 1.0
    show natsuki:
        alpha 1.0
    show monika:
        alpha 1.0
    camera master
    show bg:    
        blur 0.0
    show yuri b2b nc e1b lup me
    with Dissolve(0.2)
    "As I pull away, I see Yuri flush crimson."
    y mg "I-"
    extend mk e2a " Ah-" 
    extend mg e2c b2a " Bu-"
    show yuri me
    window hide None
    pause 1.0
    show yuri md ldown nb e3c b1d
    window auto show None
    "After a moment, her embarrassment fades, and she turns to face Sayori."
    y e1d mg b1a "So..."
    y mh na "Actually, I've been wondering about this for a while, but..."
    show natsuki me b1d nb
    show sayori md
    y mb e1a "How close {i}are{/i} you and Natsuki?"
    show yuri md
    s lup b1d mh "Hey, that's not a dare!"
    show sayori md
    y mg e1d nb "N- No, it wasn't intended to be."
    show natsuki e1b nc md
    show sayori b1a ldown
    y mh e1d b1d na "But the dare is this: Prove how close you two are."
    show yuri ma with None

    scene bg s_living_room 
    show sayori turned casual nc e2a at i44
    show yuri turned casual at i43
    show monika turned casual mc at i42
    show melody turned casual mh at i41
    with natsuki_pov()
    $ set_pov("n")

    _n turned casual notail noband b3d nb e1b me "Wha-"
    _n md "She did not just say that."
    _n b1d mj e3c "She didn't, did she?"
    _n md e1b "What does she think is going on?"
    show yuri:
        alpha 0.0
    hide melody
    show monika:
        alpha 0.0
    show layer master:
        align (1.0, 0.2) zoom 1.7
    show bg:    
        blur 2.5
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("sayori")
    "Glancing at Sayori, it becomes clear to see her cheeks are flushed - Though whether it's from embarrassment or..."
    s mb "Ah, how close we are?"
    s mi e1a nb lup "I mean, we're pretty close."
    show sayori ma na with say_dissolve
    n b3a e1a mh "Yeah, of course we are."
    n e2a b1d me "Like..."
    n b3a mi e1b "Ah, it's not like I wanted you to like me or anything!"
    n e1b b3d mh "It just sorta... happened!"
    show sayori e3d ldown with say_dissolve
    "The room erupts into chuckles, though I don't dare to look at any of them. My eyes are fixed."
    "I find myself suppressing the urge to pout. It wouldn't do me any good."
    show sayori e1a with say_dissolve
    mc turned casual mg "You know, Natsuki, I've been wondering the same thing."
    mc mb "You two have been together since the start of high school, right?"
    n mg b1d e1a "Ah, yeah, but what does that-"
    show sayori e2a md with say_dissolve
    mc ml thinking "So, you two have been together through all of your biggest ups and downs, right?"
    n mm b3d e1b "!!"
    n e2b b1d mg "I-"
    show sayori e1a with say_dissolve
    n na e1d mh "... I still don't see how this is a dare."
    s mg lup "I think..."
    s mb "I think they want us to prove how close we are."
    show sayori ma ldown with say_dissolve
    n mi "Okay, so what, you want to snuggle like Monika and Yuri just did?"
    s b1b e2a mg "Well..."
    s mh e1a b1a "I don't think we have that kind of relationship, do we?"
    show sayori md with say_dissolve
    n b1a mg e1a na "I-"
    extend e2a me " ..."
    n b1d e1d mh "What are you saying, Sayori?"
    s e3d mn "Well, I'm saying we need to fulfil the dare."
    s mb lup "There isn't anyone out there like us, you know?"
    show sayori ma with say_dissolve
    n nb md e1a b1d "..."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _n e3c mj na "... She's right."
    _n e1a b1a ma "We've done everything together."
    _n me "But..."
    _n e3c b1d mm "This is exactly what I wanted to avoid tonight!"
    _n e2a md "I didn't want to be put in a corner like this, it makes me..."
    _n e3c mm "Ah, whatever."
    _n md nb "It's Sayori."
    _n ma b3a na "It's not like we're strangers, not even close."
    _n b2a e2a "She always says that she thinks the world of me."
    show sayori e3a with say_dissolve
    _n me "But..."
    show sayori e1a md ldown with say_dissolve
    _n b4 e1a "Doesn't she love Melody?"
    _n e1d mj b1d "She always used to talk about her."
    hide black
    s mb b2b "Hey, Natsuki, it's just a dare."
    s b1a mh "If you don't want to, you don't have to."
    show sayori md with say_dissolve
    n mm e3c b1d nb "Ah, to hell with it."
    show layer master:
        align (1.0, 0.2) zoom 2.0
    show bg:
        blur 3.0
    show sayori me 
    with Dissolve(0.2)
    "As I reach toward her, the world around me seems to slow."
    "I feel her sudden surprise."
    "I don't even see it, I just know."
    "And with it, I feel the anticipation well inside of me."
    "Man, if I was ever prepared for a moment, it'd be this one."
    show sayori ma
    show layer master:
        align (1.0, 0.2) zoom 2.2
    with Dissolve(0.2)
    "Placing my hands gently on her face, I bring her in close."
    "As I do, I prepare my heart."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _n b1d md nc "Man, I'm so nervous."
    _n e2a me "My heart is beating so fast I can barely breathe."
    _n e1a b3a "What am I doing?"
    _n e1b b1d md nb "Is this legal?"
    "..."
    _n e1d mj na "Yes."
    _n e3c me "No time for hesitation."
    hide black with NonBlockingDissolve(0.2)
    "I clear my mind, and lean in."
    call close_eyes(0.4, wait=True) from _call_close_eyes_3
    "All at once, my senses explode."
    _n b1a e1a nb "Is this...?"
    show bg:   
        blur 0.0
    "I've never felt anything like it."
    _n e2a b2a md "Sayori..."
    _n e3c ma b1d "Honestly, I'd almost have taken anyone, at this stage, but..."
    _n me e1a b1a "She..."
    _n ma b2a e2a "She really cares about me."
    _n e3c "She honestly believes in me."
    _n e1a "What else could I ever ask for?"
    "The sensation causes my body to tremble, shuddering."
    _n mj na b1a "The anticipation had been killing me, but now?"
    _n e3c ma "Now it just seeks escape."
    $ autofocus.unblock("sayori")
    $ say_transition = True
    "I feel all of my doubts evaporate, and just let myself be."
    "To feel her warmth."
    _n b2a mj "To think..."
    _n e2a ma "That it was this nice to feel loved."
    "I make sure to savour the moment for as long as I possibly can."
    show bg:
        blur 3.0
    show sayori e2c nc ma b1a lup
    call open_eyes(1.0) from _call_open_eyes_3
    "And when I finally do pull away, it leaves me hollow. Lonely."
    "A feeling that I can't quite describe."
    "But..."
    "I was happy."
    "And even now, I still am."
    show layer master
    show bg:
        blur 0.0
    show monika eb nb:
        alpha 1.0
    show yuri e2a ma nc:
        alpha 1.0
    show melody ldown ef mh at i41
    with fade
    "As I look away from Sayori's embarrassed smile, I see the others."
    "It's then that it occurs to me that we were being watched."
    n me nb e1a b1a "Ah- Well!"
    _n md b1d e1b "What do I do?"
    _n me "They just-!"
    _n mm e3c "I don't know what do think, it just happened so quickly that I-"
    _n b3a me e1a na "No, wait. This was their idea."
    _n ma "Just ride it out, Natsuki."
    _n b1a "You've got this."
    show sayori:
        alpha 0.0
    camera master:
        align (0.2, 0.17) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "Looking at their faces, they're all a shade of pink too."
    _n mk b2a e1b "Nononononono!"
    _n mj e3c b1d "Nope, nope, nope that's it."
    _n mm "Can't do it, nope."
    _n mj e1b "You don't got this, Natsuki!"

    scene bg s_living_room
    camera master
    show sayori turned casual e2a at i43
    show natsuki turned casual notail e3c mj b1d nd at i44
    show yuri turned casual nc e2a at i42
    show monika turned casual eb at i41
    with mc_pov()
    $ set_pov("mc")
    
    if branches.is_current(branches.BLOOD):
        _mc turned casual ec "Finally made your choice, did you? I'm proud of you, Sayori."
    else:
        _mc turned casual mh "I wasn't expecting that, to be completely honest."
        _mc ec "But..."

    camera master:
        align (1.0, 0.25) zoom 1.7
    show bg:
        blur 2.5
    show sayori:
        alpha 0.0
    show monika:
        alpha 0.0
    show yuri:
        alpha 0.0
    show natsuki ma e2a b1d nc
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    _mc ef ma "It really looked like Natsuki needed that."
    stop music fadeout 3.0
    "She just looks so much more at peace now."
    "Despite the flustered look she's wearing, aha~"
    mc ed md "So, next up would be you, Natsuki."
    n ml e1b b3a "Uwa-"
    n cross nb e2a mb b1d "Oh, ah, yeah, sure!"
    n mg "Um..."
    show natsuki me with None
    camera master
    show bg:
        blur 0.0
    show sayori e1a na:
        alpha 1.0
    show monika ea mc:
        alpha 1.0
    show yuri e1a na:
        alpha 1.0
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    n e1a mi b3a "Monika."
    show natsuki me
    m md ec rhip "Dare."
    show monika mc
    n mg b1d e1b "But I didn't even-"
    n turned mm e3c na "Ah, forget it."
    show monika rdown ba ea
    n e2a mg "I dare you..."

    play music elegant_s

    show yuri lup md e1d
    show sayori md nb
    show monika ma
    n e1a mb "To make MC really uncomfortable!"
    n cross b3a e3d mo "Yeah, wipe that stupid grin off of her face!"
    mc ea bd mg "Hey, don't bring me into this!"
    n mi e1d b1d "You were making fun of me!"
    show sayori na ma
    show natsuki mj
    mc nb "No I wasn't!"
    _mc ec mh ba "At least, not out loud..."
    show natsuki e1a b1a ma
    m mb bc "Well, how shall I go about that, I wonder."
    show monika ma at t11
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    camera master:
        align (0.5, 0.2) zoom 1.0
        easein 15.0 zoom 1.5
    show bg:
        blur 0.0
        easein 15.0 blur 2.0
    $ say_transition = True
    "Monika stands up, and slowly starts to move toward me."
    show monika ed ba
    "Accenting her hips as she walks, I can't help but feel a little concerned."
    show monika ea
    $ autofocus.block("monika")
    "Just what is she planning?"
    show monika bc
    "As she gets closer, she slows her movements."
    show monika ed rhip ba
    "In fact, she seems to exaggerate more and more her movements."
    show monika ea ba
    "This..."
    _mc nb "This might be bad."
    m mb bc "Ho? You're in for quite the surprise..."
    show monika ma with say_dissolve
    _mc eg bi ma "Oh, I don't doubt that."
    "She's now mere inches from my face, and I can't help but flinch a little."
    "What's she planning?"
    "The grin on her face really gives me shivers."
    "She's not doing what I think she is, right?"
    "There's no way."
    m md ba "Prepared, MC?"
    show monika ma with say_dissolve
    mc mb bg ea "N- No?"
    m mb ed "Perfect~"
    show monika ma with None
    camera master:
        zoom 2.0
    show bg:
        blur 3.0
    show monika rdown ea
    with Dissolve(0.2)
    "She leans in, and I pull back, but my seat refuses to give me any more room."
    "Ohh, not good."
    "I'm in a spot of bother."
    "There's no doubt in my mind now. The smirk on her face, mere centimetres from my face, is definitely making me uncomfortable."
    show monika:
        easein 0.3 xoffset -150 blur 2.0
    show bg:
        easein 0.3 blur 0.0 xoffset -50
    show natsuki turned casual notail noband e1b mg b1d zorder 1:
        xcenter 0.65 yanchor 1.0 ypos 0.7 zoom 0.4
        alpha 0.0 xoffset 0.0 blur 2.0
        easein 0.3 alpha 1.0 xoffset -40 blur 0.0
    camera master:
        easein 0.3 zoom 1.9 xoffset 20
    "Glancing past Monika for a moment, I can see Natsuki's face in a state of shock. I don't blame her, I don't think any of us were expecting..." 
    "This."
    hide natsuki
    show black
    show monika:
        blur 0.0 xoffset 0.0
    show bg:
        xoffset 0.0
    with Dissolve(0.2)
    "Resigning to my fate, I turn my head slightly to the side, and squeeze my eyes shut."
    "Agonising moments pass, with no end in sight."
    _mc bi mh eg nb "How long was she planning on tormenting me?"
    _mc "Maybe she isn't even there anymore, and this in itself is the torture?"
    _mc "Should I open my eyes?"
    _mc "Or is that what she's waiting for?"
    _mc mm "Ah, screw it. I'd rather know what's going on."
    play sound ["<silence 0.1>", audio.slap]
    hide black
    camera master:
        zoom 2.0 xoffset 0
    show bg:
        blur 3.0
    show monika lpoint ba ed
    with Fade(0.12, 0.0, 0.15, color="#fff")
    "Opening my eyes, I instantly recoil in pain."
    mc mj bg eh "Ough! My nose!"
    m mb "Ahahaha, I can't believe you fell for that!"
    show monika ma with say_dissolve
    "Monika, holding her fingers as if she'd just flicked me, provides me with a grin."
    _mc mh ec bi "She got me, alright."
    show yuri turned casual e2a lup at i42
    show sayori turned casual md at i43
    show natsuki cross casual noband e2a md nb at i44
    show monika ldown ea at i41
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    y mb b1d "O- Okay, so who's next? Sayori?"
    show yuri ma nb
    show monika ec
    "I think everyone's a little shaken after that, all except Monika herself, who looks abundantly proud of herself."
    show monika ea
    s mb "Oh, ah, yeah, my turn."
    show sayori ma with None
    show sayori rup
    show yuri:
        alpha 0.0
    show monika:
        alpha 0.0
    camera master:
        align (1.0, 0.2) zoom 1.7
    show bg:
        blur 2.5
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    "She turns to Natsuki."
    $ autofocus.block("sayori")
    s mb "Tr-"
    show sayori md
    n b1d na mm "Dare. Absolutely dare."
    show natsuki md 
    show sayori b4 rdown
    with say_dissolve
    "Sayori gives her a puzzled look, as do the rest of us."
    s e2a mg b1b "Okay then... How about..."
    show natsuki b2a nb e1b me
    s e3d mc lup rup b1a "Eating a whole tub of ice-cream!"
    show sayori mo with say_dissolve
    _mc ea bg mh nb "This girl frightens me sometimes."
    _mc ec bi "I mean... just think about that for a second."
    _mc eb bd "That borders on torture, depending on how large the tub is."
    n b1a mg e1a "Uhh..."
    n turned e2c rhip mh "That's..."
    show natsuki me
    s mn "Well, you're lucky I didn't go with my first thought, ehe~"
    show natsuki b1d md rdown with say_dissolve
    "Natsuki doesn't look super happy. I think I'm sensing a trend."
    n mg "I..."
    n cross mm b1d e1d "Y- You better not pull anything stupid!"
    show natsuki md
    s mb e1d b1b "Who, me? Never!"
    show sayori ma with say_dissolve
    "Alright, now I'm just scared for Natsuki."
    show monika mc:
        alpha 1.0
    show yuri lup e1d md b1a na:
        alpha 1.0
    show sayori e3d b1a at rhide zorder 0
    hide sayori
    camera master:
        zoom 1.0
    show bg:
        blur 0.0
    show natsuki turned b2a e1b me 
    with Dissolve(0.2)
    "Sayori gets up, and walks toward the kitchen."
    camera master:
        zoom 1.7 yalign 0.25
    show monika:
        alpha 0.0
    show yuri:
        alpha 0.0
    show bg:
        blur 2.5
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    "Natsuki throws me a terrified look. We both know exactly what that girl is capable of."
    show natsuki:
        alpha 0.0
    camera master:
        xalign 0.0 yalign 0.15
    show yuri:
        alpha 1.0
    show monika zorder 3:
        alpha 1.0
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    "Monika has an eyebrow raised, and Yuri's no less confused."
    m nb mb bb "How is eating ice-cream hard?"
    show monika mc
    mc mg ef ba na "It's not the ice-cream."
    mc ml ec bi "... Sayori's crafty. We'll have to wait to see what she comes up with."
    camera master
    show bg:
        blur 0.0
    show sayori turned lup e3d casual at r43 zorder 0
    show monika ba na
    show natsuki me b3a na e1a:
        alpha 1.0
    with Dissolve(0.2)
    $ say_transition = False
    "And as if on cue, she re-enters the room, holding a small tub of ice-cream."
    s mc "Ta-da!"
    show sayori ma with None
    show natsuki b2a me e1b nb
    show bg:
        blur 2.0
    camera master:
        align (1.0, 0.2) zoom 1.5
    hide monika
    hide yuri
    with Dissolve(0.2)
    $ autofocus.zorder = False
    $ autofocus.block("natsuki")
    $ say_transition = True
    "I watch the colour drain from Natsuki's face as she locks eyes with Sayori."
    $ autofocus.block("sayori")
    show natsuki e2a b1d mb:
        xoffset 60
    camera master:
        zoom 1.7
    show bg:
        blur 2.5
    with say_dissolve
    n "N- No... Sayori, wait, let's talk about-"
    show natsuki b2a e1b mk
    s mb e1d b1d ldown "Nope, no negotiations. Only suffering."
    show sayori ma with say_dissolve
    "For what may be the first time in my life, I am truly glad that I am me, and not Natsuki."
    "And considering how specific that is, it may not happen again."
    show natsuki e1a me
    show sayori e3d b1a:
        xoffset 70
    camera master:
        xalign 1.0 zoom 1.9
    show bg:
        blur 3.0
    with Dissolve(0.2)
    "Sayori places herself next to the pink ball of fear, and it leaves the rest of us wondering just how bad this really is."
    "Looking at the ice-cream itself, it appears to be about a 1 litre container, and is very, very strawberry flavoured."
    _mc ea ba thinking mh "I thought Natsuki liked strawberry though?"
    n mg "Sayori, please, anything else. C'mon, please-"
    show natsuki me e1b
    show sayori mo e1d b1d
    with say_dissolve
    "Sayori cuts her off, and slowly, a truly devilish grin widens across her features."
    s mb "Better get started~"
    show natsuki e3c nb mm b1d
    s mh b1a e1a lup "There will be penalties if it melts, you know~?"
    show sayori ma ldown
    show natsuki md
    with say_dissolve
    "Natsuki says no more. She simply takes the container."
    show natsuki e1a na mj with say_dissolve
    "As she opens it, I can't help but stand to get a better look."
    "The labels don't lie, for once."
    show natsuki e1d md with say_dissolve
    "It looks like basically frozen strawberries mixed with cream."
    "But that isn't the thing that stands out."
    show natsuki b2a e1b me with say_dissolve
    "No, it's so much worse than that."
    "This ice-cream is something different. It looks like it was formed in the last ice-age."
    n mk "N- Not like this..."
    n e3c mb "I... I can't believe you've done this, Sayori."
    show sayori e3d
    show natsuki ma
    with say_dissolve
    "Sayori simply smiles as if it's the happiest day of her life."
    n b1d mg e1a "It is, isn't it?"
    show natsuki me
    s mb "It is exactly what you think it is."
    show sayori mn
    n e1b mh "This ice-cream is two years old, Sayori. It's been sitting in your freezer for all that time?"
    show natsuki md
    s mb "Well I sure wasn't going to eat it~"
    show sayori ma
    n e3c mb "God, you're a monster."
    show natsuki ma
    s e3c mi lup "I had to save it."
    show natsuki e2b b2a
    extend e3d mn " For a rainy day."
    s e1b mb "And oh! It is pouring."
    show sayori ldown ma
    show natsuki mk e1b
    with say_dissolve
    "I think I see the light fade from Natsuki's eyes."
    "But she isn't wrong. Who plans a party like this just to make their best friend eat two-year-old ice-cream that you didn't want to eat yourself?"
    show natsuki e3c b1d mm with say_dissolve
    "That's plain diabolical."
    show sayori e1a
    show natsuki b2a me lhip
    with say_dissolve
    "Natsuki brings the first spoonful to her mouth."
    n mg e1b b1d "Nope, I remember this stuff!" # im stuff
    show natsuki me
    s mb e1d b1b lup "C'mon, it's your favourite flavour~!"
    show sayori ma
    n cross e1a mi "No, it's a ridiculously rich version of my favourite flavour! We had this discussion when we opened it, remember!?"
    show natsuki me
    s e3c b1d mi "And how do you expect me to remember that? It was over two years ago!"
    show sayori md with None
    show natsuki:
        alpha 0.0
    camera master:
        xalign 0.8 zoom 2.0
    show sayori ldown e3a b1a ma
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    "Sayori turns to me and winks."
    "All I can return is a look of horror."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc ldown eb bg nb mh "Sayori..."
    _mc "She's a demon."
    hide black
    show sayori e1a
    camera master:
        zoom 1.9 xalign 1.0
    show natsuki turned b2a e1b me nb:
        alpha 1.0
    with Dissolve(0.2)
    s mh lup e3c "Eat up now, Natsuki. Otherwise, if any small amount melts, we'll have a punishment game!"
    show sayori ma
    show natsuki md e3c b1d
    with say_dissolve
    "And with that, Natsuki's fear overtakes her suffering from the block of frozen flavouring."
    scene black 
    camera master
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ autofocus.zorder = True
    $ say_transition = False
    $ autofocus.unblock("monika")
    "It took mere minutes for the entire thing to be devoured."
    _mc turned casual bi ec mh nb "Just what the hell sort of punishment games does Sayori play?"
    "It was today that I discovered my best friend's sadistic streak."

    stop music fadeout 2.0
    scene cg sleepover 1 with longfade
    pause 0.1

    camera master:
        anchor (0.65, 0.325) pos (0.53, 0.4) zoom 1.8 
    with cg_dissolve
    s turned casual mb "I can think of a great way to end this night with a bang."
    camera master
    with cg_dissolve

    play music arcade

    mc turned casual eh md "Mmm-hmm. Bring on the karaoke!"
    show bg s_living_room
    show monika turned casual ed at i41
    show yuri turned casual at i42
    show sayori ma at i43
    show natsuki turned casual notail noband at i44
    hide cg
    camera master
    with cg_dissolve
    play sound phone_notification
    "Right as I pump myself up, my phone starts to hum its annoying little tune."
    "I pull it out of my pocket and stare at the screen."
    show sayori md
    "I feel a twinge in my lip as the screen burns into my eyes."
    show natsuki md
    s mg "Mel?"
    show sayori md
    show monika ea
    n cross e1d b1d mb "What, you got a booty call?"
    show natsuki ma with None
    show sayori b1d rup:
        subpixel True
        easein 0.17 xoffset 40
        easeout 0.17 xoffset 0
    show natsuki:
        subpixel True
        pause 0.16
        "natsuki cross casual noband e2a b1d ma"
        easein 0.14 xoffset 20
        easeout 0.14 xoffset 0
    with None
    show black
    hide natsuki
    hide monika
    hide sayori
    hide yuri
    show bg s_house_entrance_night
    with NonBlockingDissolve(0.6)

    play music2 add_playback_info(audio.arcade_muffled, get_pos()) fadein 2.0
    stop music fadeout 2.0

    "Out of the corner of my eye, I see Sayori elbow her. I can almost feel the impact."
    "After that, I think Monika says something, but I can’t quite catch it."
    "Something mumbles and trips out of my mouth as I stand and move toward the door."
    s turned casual mh "Hey, what is it? What's going on?"
    mc eg bi mj "Just... just a call."
    s e2a b2b mg "It doesn't look like just a call..."
    hide black
    show sayori md at i11
    with NonBlockingDissolve(0.3)
    "I look back at Sayori. I think I want to glare at her, but my face is frozen."
    s b2a e1a mg "Mel...?"
    show sayori me
    mc ea ba mg "You guys start the karaoke without me, okay?"
    mc ef bi ml "I'll be right back."
    "Nothing else leaves my mouth as I step out into the frigid night."

    scene bg s_house_night_on with fade

    "I close the door and look at the screen again."
    "It's still ringing."
    "..."
    "I pick up."

    stop music2 fadeout 2.0
    play ambient ext_night fadein 3.0
    if preferences.language is None:
        $ auto_advance_date_mult = 2.0
    phone call "dadmc"

    phone_mc "Hello?"
    phone_dadmc "Hey, Melody."
    phone_mc "Oh lovely."
    phone_mc "May I ask what possessed you to call me right now?"
    phone_dadmc "... I wanted to check on how you were doing."
    phone_mc "Send a text. It's been doing {i}wonders{/i} for the past three years."
    phone_dadmc "How are you doing?"
    phone_mc "..."
    phone_mc "I'm fine."
    phone_dadmc "What does fine mean?"
    phone_mc "What do you think it means?"
    phone_mc "I'm doing okay, I am alive and I am well, I continue to {i}breathe{/i}, much like to your - and I’m sure my mother’s - chagrin."
    phone_mc "What more do you want?"
    phone_dadmc "I'd like to hear some more details. Is school going well for you?"
    phone_mc "You have access to my grades if you so wish."
    phone_mc "You can just check yourself."
    phone_dadmc "I have checked. Almost straight fives."
    phone_dadmc "I- I know you're doing well. I'm very proud."
    phone_mc "..."
    phone_dadmc "I was just trying to make conversation."
    phone_mc "Well, if you’d started five years ago, maybe this conversation would have gone somewhere."
    phone_mc "Anyway, you caught me in the middle of something, so I'll be going back to that now."
    phone_mc "Good day."
    phone_dadmc "Wait, wait!"
    phone_mc "..."
    phone_dadmc "..."
    phone_mc "..."
    phone_dadmc "Are you there?"
    phone_mc "Did you hear me hang up?"
    phone_dadmc "You know, it is a little shameful to have your father chase after you like this."
    phone_mc "Let's not start on what's shameful - I think we both know one of us will have a bad time."
    phone_dadmc "..."
    phone_dadmc "So what's the something I interrupted?"
    phone_mc "Lord almighty, get to the point!"
    phone_dadmc "This is the point, Melody."
    phone_mc "Stop- Stop calling me that!"
    "I'm tempted to throw my phone face-first into the cement and just end the call that way."
    "It'll cost me a phone, but it was my money anyway."
    "I can just get another one."
    phone_dadmc "This something..."
    phone_mc "If you must know, I have friends over and I much prefer their company to yours!"
    phone_dadmc "That's nice. I'm happy you're taking the steps to get out of your shell."
    phone_dadmc "A lot of people would value you, you know."
    phone_mc "..."
    phone_dadmc "So, do you have any other plans lined up in the next couple weeks?"
    phone_mc "There's a festival in two days, but otherwise it's just the normal day-to-day."
    phone_dadmc "The Culture Festival that Misato and Karin used to talk about?"
    "He pauses, as if not sure what to say."
    phone_dadmc "I’m sure you’ll have a wonderful time."
    phone_mc "I'm sure it'll be a lot better than this."
    phone_dadmc "Speaking of Karin..."
    phone_dadmc "Have you spoken to your mother recently?"
    phone_mc "What do you think?"
    phone_mc "Considering you apparently care and you're still a massive deadbeat, how do you think that {i}witch{/i} is managing?"
    phone_dadmc "Nothing, is it?"
    phone_mc "Nothing at all."
    phone_dadmc "..."
    phone_dadmc "Expected, but disappointing."
    phone_mc "What?"
    phone_mc "Is there something up with her?"
    phone_mc "Don't tell me she went out in the rain again. You know how witches are with water."
    "He stifles a chuckle."
    phone_dadmc "No, not last I heard."
    phone_dadmc "... Misato’s still been in regular contact, so it’s been difficult to avoid."
    phone_mc "Aunt Misato?"
    "He says nothing for a moment."
    phone_dadmc "They’ve been staying with me over here recently."
    "Now it’s my turn to pause."
    
    if not branches.is_current(branches.BLOOD):
        "Part of me is curious, part concerned, but I decide to not press the issue."
    else:
        "A sinking feeling wells within my gut - I still need to tell Sayori."
        "I just... Don’t know where to begin."

    phone_dadmc "It’s been nice, having them back in the country. We went fishing a little while back."
    phone_dadmc "Have you learned?"
    phone_mc "Did you teach me?"
    phone_dadmc "To be honest, it's not worth teaching."
    phone_dadmc "It's mostly for the serenity and the conversation."
    phone_mc "Did you teach me that, either?"
    phone_dadmc "..."
    phone_dadmc "I thought your mother would have done at least that much."
    phone_mc "Sayori didn't tell me Aunt Misato was with you."
    phone_dadmc "Right."
    phone_mc "..."
    
    if not branches.is_current(branches.BLOOD):
        phone_mc "Right what?"
        phone_mc "Does she not know?"
        phone_dadmc "..."
        phone_mc "She doesn't? I expect it from you, but not from her!"

    else:
        phone_mc "Wait, what's happening?"

    phone_dadmc "Things are... complicated."
    "My eyes narrow."
    "It doesn’t take a genius to recognise the sudden lack of bluster in his tone."
    phone_mc "What's going on?"
    phone_dadmc "..."
    phone_mc "Come on. This has to be the reason you called instead of just shooting me a text, right?"
    phone_mc "What is it?"
    phone_mc "Oh God, I swear if you pulled a {i}Karin{/i}-"
    phone_dadmc "No, purge the thought from your mind."
    phone_mc "Okay..."
    phone_mc "Then what is it?"
    phone_dadmc "Just... don’t be surprised if you see your mother sooner than you might expect."
    "He seems to let out a sigh on the other end, but I only feel the tension grow."
    phone_mc "If she shows up, I won’t open the door."
    phone_dadmc "I’m not asking you to do anything."
    phone_mc "If that damned rotting hag even looks in my direction-!"
    phone_dadmc "And you are in your right."
    phone_dadmc "I just didn't want you to be surprised when the time comes."
    phone_mc "... Well thanks."
    phone_mc "You ruined my night."
    phone_dadmc "Glad to be of service."
    phone_dadmc "There’s... one other thing."
    phone_dadmc "Bills here are... Expensive."
    phone_dadmc "A house in Japan that isn’t an investment is only compounding on those expenses."
    "I feel my teeth grit."
    phone_mc "Fine."
    phone_mc "I didn’t want your handouts anyway."
    phone_dadmc "I... I’ll try and give you until graduation, but-"
    phone_dadmc "There’s a chance Sayori might be in a similar boat. Perhaps you two could work something out?"
    "My grip on the phone tightens, and the urge to peg it is palpable."
    phone_mc "I..."
    phone_mc "Will sort something out."
    phone_dadmc "If you don’t, you both do have dual citizenship, so-"
    "He seems to cut himself off, not sure if he should finish his own thought."
    phone_mc "I’ll work it out. On my own."
    "I can hear him nod from the way his beard brushes against the microphone."
    phone_mc "Any other Earth-shattering news today?"
    phone_dadmc "... No."
    phone_mc "Good. I’m going back inside."
    phone_dadmc "Alright. It was..."
    phone_dadmc "..."
    phone_dadmc "It was nice talking to you, Melody."
    phone_dadmc "And I know you don't feel the same way, so you don't have to throw a snide remark."
    phone_dadmc "I understand."
    phone_dadmc "I'll..."
    phone_dadmc "See you at another time."
    phone_mc "..."
    "The phone shakes by my ear."
    "And then, before I can even register..."
    "My lips start to move and the words spill out."
    phone_mc "Wh- What about you?"
    phone_dadmc "Hm?"
    phone_mc "How... are things?"
    phone_dadmc "Oh...!"
    phone_dadmc "Um..."
    phone_dadmc "They're alright."
    phone_dadmc "It's hard work, but I make do with what little time you have."
    phone_mc "What do you do in that little time?"
    phone_mc "I remember you used to read those big, thick books you had lying around the house..."
    phone_mc "Do you still do that?"
    phone_dadmc "Ah..."
    phone_dadmc "I wish. I don't have {i}that{/i} kind of time."
    phone_dadmc "Outside of helping with..."
    phone_dadmc "With Misato, I..."
    phone_dadmc "Mostly just eat, watch garbage television, and..."
    phone_dadmc "Think about you."
    phone_mc "..."
    phone_mc "Yeah?"
    phone_dadmc "Yeah."
    phone_mc "I umm..."
    phone_mc "I..."
    phone_mc "..."
    phone_dadmc "I hope you're not thinking of me, though."
    phone_dadmc "You have better things to do than fret over an old man who isn't even around."
    phone_mc "You'd be surprised."
    phone_dadmc "It's no use getting bogged down by things that don't matter."
    phone_mc "..."
    phone_dadmc "Those friends you have to get back to..."
    phone_mc "Yeah? What about them?"
    phone_dadmc "Do you like them?"
    phone_mc "Well, I sure hope so, they know where I live!"
    phone_dadmc "Hm, yes, let's hope you're a better judge of character than I am."
    phone_mc "That is a very low bar to clear."
    phone_dadmc "Indeed, so make sure you do."
    phone_mc "I will try my best."
    phone_dadmc "Do, or do not."
    phone_dadmc "Not try."
    phone_mc "Okay, sure."
    phone_mc "I'll..."
    phone_mc "I'll catch you later, Dad."
    phone_dadmc "... Yeah. Have a good night."
    phone_mc "And you, a good afternoon."
    phone_dadmc "Of course."
    phone_dadmc "Bye."
    phone_mc "Bye."

    phone end call
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    stop ambient fadeout 3.0

    play sound ["<silence 0.9>", audio.fall]
    camera master:
        xoffset 0.0 align (0.4, 0.7)
        easeout 0.3 xoffset -14
        easein 0.12 xoffset 14
        easein 0.12 xoffset -14
        easein 0.12 xoffset 14
        ease 0.15 xoffset 0
        easein_back 0.3 zoom 2.5
    "As the phone drops to my side, my legs wobble beneath me. I have to lean on the door to keep myself on my feet."
    _mc turned casual eg bi mm "Fuck..."
    camera master:
        align (0.5, 0.2) zoom 2.0
    show bg:
        blur 3.0
    show sayori turned casual md:
        matrixcolor TintMatrix("#6065b1")
        i11
    with Dissolve(0.2)
    "The door opens behind me, almost toppling me backward - At least, until Sayori catches me."
    camera master
    show sayori ma
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "She steps outside with me, helping me back to a rightward position."
    s mb lup b2b "Hey, Melly."
    s e2a b2b mg "I heard a thud, so..."
    show sayori md ldown
    mc ef ml "I’m good."
    mc eg mg "... They’re selling the houses."
    show sayori me e3c b1b
    "Sayori clicks her tongue."
    s mh e1a b1a "Well, looks like we might need to find somewhere else to stay."
    show sayori md
    mc ef mg ba "Not for a while yet, it was just some forewarning."
    show sayori me b2b e3c at dip
    "She lets out a sigh of relief."
    s mg "Oh, good."
    s e1a b1a mb lup "Well, you want to join us inside?"
    s mh "Or is there something you want to talk about?"
    show sayori ldown md 
    call close_eyes(0.4) from _call_close_eyes_4
    "I close my eyes, considering what to say."

    if not branches.is_current(branches.BLOOD):
        _mc eg ba mh "Best not to subject her to conjecture."

    mc eg ml "No, I think I’m okay."
    mc mb bg "Thank you, though."
    "I muster up a warm smile as we step back inside."

    scene bg s_living_room
    camera master
    show monika turned ed casual at i41
    show yuri turned casual e1d nb lup at i42
    show natsuki turned casual notail noband at i44
    with wipeleft
    show sayori turned casual e3d at r43 zorder 1
    play music stars

    "The warm air rushes over me, accompanied by smiles of the same ilk."
    m mb "Come, sit with us."
    show monika ma
    n cross b3a mh "Ya missed out! We just finished packing up!"
    show natsuki ma
    mc turned casual mj eg bi "Aww, crap..."
    mc ea bg mg "Really?"
    s e2a mb "Yeah... Ehe~"
    show sayori ma with None
    hide sayori
    hide monika
    hide yuri
    hide natsuki
    show cg sleepover 1
    with cg_dissolve
    "I take my seat once more, sighing."
    mc ml ba ea "Did you rap, Yuri?"
    camera master:
        anchor (0.3, 0.25) pos (0.48, 0.3) zoom 1.8
    with cg_dissolve
    y turned casual e2a mb b1d "I did..."
    camera master
    with cg_dissolve
    mc ef bi mj "Daughter of a bastard..."
    camera master:
        anchor (0.3, 0.25) pos (0.48, 0.3) zoom 1.8
    with cg_dissolve
    y e1d mh nb b1a "M- Maybe next time?"
    camera master:
        anchor (0.0, 0.325) pos (0.0, 0.4) zoom 2.2
    with cg_dissolve
    m turned casual ec mb "I’ll say, it was exceptionally impressive." 
    camera master:
        anchor (0.3, 0.25) pos (0.48, 0.3) zoom 1.8
    with cg_dissolve
    "Yuri looks at Monika, who giggles."
    camera master:
        anchor (0.0, 0.325) pos (0.0, 0.4) zoom 2.2
    with cg_dissolve
    m bc ea "What? I’m not allowed to copy your mannerisms~?"
    camera master:
        anchor (1.0, 0.325) pos (1.0, 0.4) zoom 2.1
    with cg_dissolve
    n turned casual notail mm e3c b1d noband "Please, I think we’ve had enough flirting in this room for one night - Get a room."
    camera master:
        anchor (0.3, 0.25) pos (0.48, 0.3) zoom 1.8
    with cg_dissolve
    y b1d e2a mb "Y- Yes, I do agree, though it wouldn’t be myself responsible for the most overt of such actions..."
    show monika eb ba ma nb at i41
    show yuri lup ma na at i42
    show natsuki cross e2a md nc at i44
    show sayori turned casual e3d at i43
    hide cg
    camera master
    with cg_dissolve
    "Natsuki flushes crimson, jumping to her feet."
    n e3c mm "Fuck off..."
    show natsuki turned lhip mj:
        easein 0.17 xoffset -40
        easeout 0.17 xoffset 0
    show sayori e1b mn b2b:
        pause 0.16
        "sayori turned casual b1a e3d mn"
        easein 0.14 xoffset -20
        easeout 0.14 xoffset 0       
    "Sayori starts to let out a restrained giggle, until Natsuki punches her in the arm."
    show sayori b2c xd mo at hop
    show monika ed ba na
    show yuri b1a e1a ldown
    show natsuki cross e2c md nb
    "Then Sayori just laughs."
    show monika ea
    mc ml ba ea thinking "As the... I wanna say fifth wheel here? I think I’m gonna go wash up."
    show natsuki e1a b1a 
    show sayori mn b2b e3a nb
    m mb "I agree. It's getting a little late."
    m md lpoint "Should we be heading to bed?"
    show monika mc
    show yuri md
    n b3d na mi "What? No."
    show sayori e1a b1a na ma
    n b1d mg "It's way too early."
    show natsuki me
    show monika ea ldown
    y mg b1d "We have preparation we need to do for the festival still tomorrow, Natsuki. It would be irresponsible to stay up late."
    show yuri ma b1a
    show natsuki md e2a
    mc mb ldown "I agree with you both, I won't stay up too much later."
    mc thinking mg "Maybe half an hour?"
    show yuri e2a
    m rhip ec md "Okay, but I'll be going to bed now."
    show monika mc
    y lup nb e1d mb "S- Same."
    show yuri ma
    show monika rdown ea ma
    mc ml "Sayori, what will you be doing?"
    s mb lup "I'll stay up!"
    show sayori ma
    m mb "Okay then, come Yuri - We'll head to bed."
    show monika ma
    y e3c mg "O- Okay."
    y e1a ldown e1a b1a na mb "Thank you all for being so nice to me and making it such an enjoyable night."
    show yuri ma
    show sayori rup e3d mc at hop
    s "No problem! Glad it was fun!"
    show sayori ma
    m mb ed "Our pleasure, Yuri."
    show monika ma
    show sayori ldown rdown e1a
    n turned e3c b3a mi "Well, I'm glad."
    show natsuki ma e1a
    mc ldown mb "Yeah, it's good you enjoyed it. I certainly did."
    show yuri e3c
    show monika ec at dip
    "Monika takes Yuri's hand."
    m mb ea "Thank you all! See you in the morning!"
    show monika ma at thide
    hide monika
    show yuri e2a at thide
    hide yuri
    show sayori at t21
    show natsuki at t22
    mc "Night!"
    s mb "Bye!"
    show sayori ma with None
    show natsuki:
        alpha 0.0
    show bg:
        blur 2.5
    camera master:
        align (0.25, 0.2) zoom 1.7
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("natsuki")
    "Watching Monika and Yuri leave, I turn to Sayori."
    $ autofocus.block("sayori")
    mc mg "So, what did you have in mind, if you wanted to stay up?"
    s mb "Well, I figure we can just chat, you know?"
    show sayori ma with None
    show natsuki:
        alpha 1.0
    hide sayori
    camera master:
        align (0.75, 0.25)
    with Dissolve(0.2)
    n lhip mh "Yeah, we've been playing so many games that we..."
    show natsuki me
    extend e2a b1d mg " haven't really had the chance to just..."
    show natsuki me with say_dissolve
    s turned casual mb "Hang out."
    n b3a mb ldown e1a "Yeah! Exactly."
    show natsuki ma with None
    show sayori ma at i21
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    mc ec mj "So, what did you want to talk about?"
    mc ml ea "Our crushes?"
    show black with NonBlockingDissolve(0.3):
        alpha 0.5
    _mc ec mh "That's typical girl talk, right?"
    show natsuki:
        alpha 0.0
    camera master:
        align (0.25, 0.2) zoom 1.7
    show bg:
        blur 2.5
    show sayori e2c me nb
    hide black
    with Dissolve(0.2)
    "Though my assumption is quickly shot down."
    show natsuki e2b b1d me nb:
        alpha 1.0
    show sayori:
        alpha 0.0
    camera master:
        align (0.75, 0.25)
    with Dissolve(0.2)
    "With the look that both of the girls shoot each-other, then me, I decide that for whatever reason, it probably isn't wise."
    n cross e1b mm "!!"
    show natsuki e2b:
        alpha 0.0
    show sayori:
        alpha 1.0
    camera master:
        align (0.25, 0.2)
    with Dissolve(0.2)
    s e1a lup mh "Ah, I don't think..."
    show sayori me with None
    show sayori ldown e2a ma b2b na
    show natsuki e2d md:
        alpha 1.0
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    mc eh bg mb nb "Oh, I was joking, don't worry."
    mc ef mg bi "Besides, even if you told me, it's not like I'd tell them or anything."
    mc eh md bg "I'd keep it to myself, like a good friend, you know?"
    $ autofocus.unblock("natsuki")
    n e3c mb "Y- Yeah, no, I know you would."
    show natsuki ma
    $ autofocus.unblock("sayori")
    s mh lup e1a b1a "Yeah, but, probably not a topic for now, you know?"
    show sayori e2a ldown md
    _mc ec mh nb bi "Wow, way to kill the mood, me."
    show natsuki na e1a b1a md
    show sayori e1a ma
    mc mg ea na ba "So, how has life been lately?"
    _mc eg bi mh "... Really."
    _mc eb bd "That's the best you can come up with?"
    _mc eg ma bi "Genius right here."
    n turned lhip e2a mh "Ah, same old, same old. Just school and work."
    show sayori md
    n mg ldown e1d b1d "Though I do wish you'd lengthen your wit a little."
    show natsuki mj
    s mg b1d "Now that's a little mean, Natsuki."
    show sayori md
    n mh e1a b3a "I'm just saying, she could afford to be a little more active in her language."
    show natsuki md
    s mi lup "What, you're saying that Melody isn't perfect as she is?"

    if branches.is_current(branches.FEELINGS):
        s e3c mh b1a ldown "I think she's quite the cunning linguist, if you ask me."
        show sayori ma nc

    else:
        s mb b1a "I think she's just great, even if her brain isn't all that large sometimes."
        show sayori ma ldown
        _mc bi mh "... I don't know if that hurt me more than Natsuki's remark."
        _mc ba ea "She knows I'm ranked fourth, right?"
    
    n lhip rhip e1d b1d mh "Regardless, I think someone needs to work on her conversational skills."
    show sayori na e1a
    show natsuki md
    "I shrug, more to myself than to either of the girls."
    mc eg mj ba na "I can't really argue with that..."
    show sayori md
    n mc b3a ldown rdown e1a "So, let's do that."
    show natsuki md
    show sayori mg lup b1d
    $ autofocus.force_focus("sayori")
    "S & MC" "Huh?"
    $ autofocus.restore_focus("sayori")
    show sayori me
    n mg "Do I really need to explain it?"
    n cross e3c mh b1d "This is exactly what I'm talking about."
    show natsuki mj
    show sayori md b1a
    _mc ec mh nb ba "... As much as I hate to admit it, she might have a point."
    _mc ef na "I haven't really had many friends since Sayori and I stopped talking."
    show natsuki b3a e3a md
    s e3d mn ldown "My social skills are great, so I think I'll take lead, ehe~"
    show sayori md e1a
    n mi b3a e3c "Not so fast."
    show natsuki turned md e1a b1a
    show sayori e2c b4 me
    "Sayori shoots a glance at Natsuki, something that seems to convey more than a little confusion."
    n lhip rhip e2a mg "That's exactly what I mean."
    show sayori md b1b
    n b3a mb ldown rdown "You've got a good mind for conversation, but that's not exactly what you need."
    show sayori e2a b1a
    n cross b1d mh "You lack confidence in tense situations, but you're good around people you don't know."
    show sayori e1a
    n e1a b3a mb "MC is much the same. You get self-conscious around people you know, though you still don't have a problem with people you don't. That would be because of your work experience, I'd bet."
    n turned mh b1a "So, because you're used to people who aren't your peers, and Sayori is, I don't think the two of you interacting would be very helpful."
    show sayori e2a ma nb
    n e1d b1d mg "Especially considering the two of you are uncomfortably close already."
    show natsuki e1a b1a ma
    _mc ec bi mh "... What's that supposed to mean?"
    show sayori e1a na at thide
    hide sayori
    show natsuki e1d b1d mh at t11
    n "So, you're going to talk to me."
    show natsuki md with None
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    "With her facing me dead on, I can't help but start to feel a little uncomfortable with the intensity of those eyes."
    $ autofocus.block("natsuki")
    _mc ec ba mh "Actually, that's exactly what she was talking about, isn't it?"
    show sayori turned casual b2b md at i21
    show natsuki:
        alpha 0.0
    camera master:
        align (0.25, 0.2)
    with Dissolve(0.2)
    "Though, the look on Sayori's face gives me pause."
    camera master:
        align (0.5, 0.25) zoom 1.7
    show bg:
        blur 2.5
    show natsuki e1a b1a ma:
        alpha 1.0
    hide sayori
    with Dissolve(0.2)
    n b3a mc "So - Tell me about yourself."
    show natsuki ma with say_dissolve
    mc ef mj bg nb "Oh, ah-"
    n e3c mi "Aaaand you fail!"
    n cross mg e1d b1d "Introductions are paramount."
    n e1a b1a mh "A good introduction will set up that relationship for life. It's almost impossible to fix that initial impression later on, so get it right."
    n e2a mg "Hesitation is akin to letting yourself be intimidated. The other party will walk all over you for as long as you know them."
    n turned e1a b1d mh "Don't fall into that trap. Become confident."
    show natsuki mj with say_dissolve
    mc eb nb ml bd "You didn't give me a chance to prepare, how was I supposed to react properly?"
    n mh "By being better."
    n cross e2a b1a mg "Not my fault you can't keep up."
    n b3a e1a mb "But that is exactly what I'm going to fix."
    n turned b1a e1a mh "By learning to react to situations, you will be able to make better impressions and save yourselves from ridicule."
    show natsuki e2a md with say_dissolve
    s turned casual b1d mg "But you missed the point. If you don't have time to process the question, how are you supposed to react?"
    n cross b1d mh "By being smart. By predicting what they're going to say."
    n e1a b1a mg "By having a list of responses for common questions."
    n turned b3a mi e3c "If you can't at least do that, are you really ready to step into the outside world?"
    show natsuki mj with say_dissolve
    mc mg na ea "Hey now, I've been living in the adult world for three years. I don't think you have any place to lecture me on being an adult."
    n e1d b1d mm "Oh really?"
    show natsuki mj at i22
    camera master
    show bg:
        blur 0.0
    show sayori b2b me at i21
    with Dissolve(0.2)
    $ say_transition = False
    show natsuki e3c md at dip
    "She moves to stand, but pauses, replacing herself on the couch."
    n e2c me "..."
    show natsuki md
    "Her voice is hushed, almost a whisper, but the hint of a threat still lingers."
    $ autofocus.unblock("natsuki")
    n mg e3c rhip "Will you take my advice or not?"
    show natsuki md
    show sayori e2c
    "I don't think I've ever seen Natsuki like this."
    show natsuki:
        alpha 0.0
    camera master:
        align (0.25, 0.2) zoom 1.7
    show bg:
        blur 2.5
    with Dissolve(0.2)
    "In fact, from the look on Sayori's face, I don't think she has either."
    camera master
    show bg:
        blur 0.0
    show natsuki rdown e2c:
        alpha 1.0
    show sayori e1a md
    with Dissolve(0.2)
    mc eg bi mg "I'm listening, but I don't think you should be lecturing someone your own age like you've got life experience on them."
    n me "... Fine."
    show natsuki mj
    show sayori b1a
    "Her voice loses the hostility, but hasn't regained any volume."
    n b3a mh e1a "Next, what to say in that introduction."
    n lhip b1a e2a mg "Both politeness and assertiveness are imperative."
    n cross mh "If you are rude, that will damage the other party's image of you. Same if you are too passive."
    n mg b1d e1a "Be smart about what you say. If you are talking to an employer, tell them what they want to hear."
    n turned mh b1a "When making friends, tell them what makes you worth knowing."
    show natsuki md
    "Her quiet tone is really starting to be unsettling, considering how loud she usually is."
    s lup mg "So how does that apply to complete strangers off the street?"
    show sayori md
    n mh "That's easy. Tell them as little as you can, while still being polite, as you work out what stance to take with them."
    show sayori ldown
    n cross b1d mg "Answer questions directly, and never answer a question with a question."
    n e2a mh "That's a classic example of back-chat, and is disrespectful."
    n e1a b1a mb "Be direct, but not aggressive. Answer questions with sincerity, and don't overthink it."
    n e3c mh "Falter, especially at the first question, and you may as well give up."
    show natsuki ma
    mc ml thinking ba ea "What if you're just having a casual conversation?"
    n turned lhip b3a mc e1a "I'm glad you asked. There's good news: You'll never have to worry about that."
    n mh ldown "A first conversation is never purely casual. Both sides will be scoping each-other out."
    n b1d mg "That's how we learn about each-other."
    n mb b1a "So, nothing changes."
    n cross mh "Even at a party, if you let yourself get 'caught up in the mood', you'll be the subject of all the jokes for weeks. Do you want that?"
    show natsuki me
    mc bi ldown ec ml "Well what if you don't care what others think about you?"
    $ autofocus.block("natsuki")
    n "..."
    $ autofocus.unblock("natsuki")
    show sayori b2b
    n turned b1d e3c mb "Are you an idiot? Do you want to die alone?"
    n mh e1a "Ignoring masses can serve you well, but never, ever ignore individuals."
    n cross e1d mg "Individuals will cause you hell. Individuals start rumours."
    n e1a b3a mb "Children will ruin your reputation. After all, who doesn't trust a small, adorable face?"
    show sayori nb mj
    n mh e1d b1d "And most importantly, never, ever, underestimate anyone."
    n mm "If you do, you're digging your own grave."
    n turned lhip b3a e1a mh "Navigating through social situations comes easy to some. For those it doesn't, you need to fight for it. Fight for respect."
    n mg ldown b1d e1d "If you don't, you'll be left by the wayside."
    show natsuki md
    s lup b2a mb "I think you're being a little too cynical though. People aren't all out to get you. Sometimes, you can just make a good friend."
    show sayori ma with None
    show natsuki:
        alpha 0.0
    show sayori na
    camera master:
        align (0.25, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "She shoots a glance my way, and it warms my heart."
    show sayori ldown e2a b2b md with say_dissolve
    "And straight after, a glint of sadness."
    "And I'm immediately reminded of what I did to her."
    _mc ef bg mh "I can't believe she forgave me so easily."
    camera master:
        align (0.75, 0.25)
    show natsuki e1a b1a:
        alpha 1.0
    show sayori b1a:
        alpha 0.0
    with Dissolve(0.2)
    _mc ec bi "More than that, I can't believe Natsuki, who had obviously been told all the stories, is even willing to talk to me."
    camera master
    show bg:
        blur 0.0
    show sayori:
        alpha 1.0
    with Dissolve(0.2)
    _mc ea ba "Surely she knows?"
    n mg "What?"
    show sayori e1a
    n cross mh "Too close to home?"
    show natsuki mj
    mc ef nb mf "N- No..."
    show sayori rup e3c
    "Sayori steps in."
    show natsuki e2a me
    s mh e2a "Ah, while I do appreciate the advice, I think that's enough for the night."
    show sayori ma e1a
    show natsuki turned e1a md b1d nb
    "Natsuki turns to her, then back to me."
    "Seems she's realised something. Big talk for someone who was just lecturing us on social interaction."
    n mg e2a "I see."
    show natsuki turned e2c me at t55
    show sayori me
    "Standing up, she starts to walk toward the stairs."
    n lhip e2a b1a mg "I'm going to bed."
    show natsuki md
    s b2b mh rdown "No, Natsuki, don't leave just yet-"
    show sayori md
    n b3a e3c mi ldown "I'm not stupid. I know when I've overstayed my welcome."
    n mh e2c b1d "Thanks for listening to my useless advice."
    show natsuki md at thide
    hide natsuki
    show sayori rdown e2a mj at t11
    "She practically spits the last two words, as she disappears up the stairs, without another word."
    mc bd ea ml "What..."
    s mh e3c "It's... a long story."
    show sayori md with None
    show sayori e1a
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    mc ef mg ba na "Well, we have time."
    $ autofocus.block("sayori")
    s b1d mg e1d "You really aren't good with social cues, are you?"
    show sayori md with say_dissolve
    mc ea "I am, but I prefer to know things than not know."
    s b1b e2a "..."
    s mg b1a "Natsuki doesn't have the most fun home life, as far as I know. She's never dated anyone. Not even gotten close."
    s e3c mh "What happened earlier today... I think that was the first time she's been embraced like that."
    s mg e1a "That was her first kiss."
    show sayori md with say_dissolve
    mc mh "..."
    mc bd ml "So what does that make you to her?"
    show sayori b2c e2a nb mj with say_dissolve
    "She shuffles uncomfortably on her seat."
    s mh "I'm her best friend. Her... only real friend."
    s b2b e3c mb na "She believes I'm the only one that will ever understand her."
    s e1a b1a mh lup "So... do me a favour."
    s e2a mg "Be her friend. Be there for her, so that if..."
    show sayori me with None
    show black with NonBlockingDissolve(0.3)
    "It seems to now be my turn to look away, my eyes filled with uncertainty."
    _mc ef bi mh "I've no idea where I'm going to end up. Making a promise like that..."
    _mc ec ba "She does seem to mean well, and I've nothing really against her, but I've only very recently starting talking with {b}anyone{/b}, let alone so many people."
    mc ef ml "I can't make that kind of promise, I'm sorry."
    show sayori md b2b nb
    hide black
    with NonBlockingDissolve(0.2)
    "From the corner of my eye, I see Sayori grow melancholy."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("sayori")
    s lup mg "I just don't know... what she'd do if I wasn't around anymore."
    show sayori md
    mc bd ea "What do you mean, 'If you weren't around?'"
    s e3c na b1a mh ldown "Don't read too much into it. I just wish she'd try to make more friends."
    show sayori md
    mc ef mg ba "I'll do my best."
    show sayori ma e1a
    "At last, her smile returns."
    s mb b2a "Thank you."
    show sayori ma na

    if branches.is_current(branches.FEELINGS):
        with None
        show sayori b1a e3c
        camera master:
            align (0.5, 0.2) zoom 1.5
        show bg:
            blur 2.0
        with Dissolve(0.2)
        $ say_transition = True
        "We relax for a moment, leaning back into the couch."
        $ autofocus.block("sayori")
        "Sayori leans into me, her breathing softening as she pulls me ever closer."
        mc bi ml ef "Well... You know..."
        show sayori e1a md
        window hide None
        stop music
        pause 1.6
        window auto show None
        s e1d b4 mg "Really? After all that?"
        show sayori md with say_dissolve
        mc ea mg ba "What? We're alone. We can duck over to my place."
        s e2a mg b1a "Then we'd have to come straight back to our separate beds here. Do you really want that?"
        show sayori md with say_dissolve
        mc bg "Why? Would it be such a bad thing if they knew?"
        show sayori b1d e1d mj with say_dissolve
        "Her incredulous look shuts me down in an instant."
        s mi e1a lup "Yes! Obviously it would be a problem!"
        show sayori md with say_dissolve
        mc ef bi ml "... Alright. Fine, it's a bad idea."
        mc eg mg ba "Sorry, I'll just head to bed."
        s mb e1d b1b "Oh no you don't." # jesus fuck she horni
        show sayori ma with None
        camera master:
            zoom 2.0
        show bg:
            blur 3.0
        with Dissolve(0.2)
        "Grabbing my shirt, she pulls me in."
        s mb "You aren't going anywhere just yet..."
        show sayori ma 

        scene black
        camera master
        with Dissolve(0.5)
        $ say_transition = False
        $ autofocus.unblock("sayori")

        "She drags me up to her room, practically by the mouth."
        "The night didn't stop for us until the sun slowly began its rise."

    else:
        mc eg mg ba "No, thank you, Sayori."
        show sayori b1a
        mc ea mb "I feel like I understand her a lot better."
        mc ml "We should get some sleep now though."
        s mb "I'll see you in the morning, Melody."
        show sayori ma

        scene bg s_house_corridor_day with longfade

        "As I reach to top of the stairs, I hear sounds coming from the master bedroom; Yuri and Monika are evidently still awake, quietly conversing."
        camera master:
            align (0.55, 0.52) zoom 1.7
        with Dissolve(0.2)
        y turned casual mb b2b "Thank you for making me feel at ease this evening, Monika... You- You've always been a sister to me."
        m turned casual ed mb "The pleasure has been all mine, Yuri. I've always wanted a younger sister, you know~"
        m ea md "After everything... I think it would be nice to simply have that chance - For both of us."
        "While I'm not exactly standing in the doorway, my gait has certainly paused as I lean on the bannister of the top step, not quite in view, but also well within earshot."
        "A small smile crosses my face as I chuckle to myself softly."
        _mc turned casual nb eg "God, how is everyone in this club so cute? How do they keep it up all the time?"
        y e3c "Thank you, Monika."
        "A long pause ensues, and I step back in the silence to move toward my own assigned room, before Yuri continues."
        y e2a mg b1a na "I- I need to prepare for sleep. Brush teeth and the like..."
        m mb "Of course, don't let me stop you."
        y e1d mb "M- May I cuddle with you when I return?"
        _mc bd eb nc mh "P- Pardon? They're that close?"
        m eb nb mb "Ah... I suppose you could... Attend to your before-bed needs first, though."
        "I can hear Yuri giggle as she rolls out of the bed and walks into the adjoining ensuite."
        show monika ma na ea at i11
        camera master:
            zoom 1.0
        with Dissolve(0.2)
        "Monika, on the other hand, steps outside of the room, her eyes locking onto mine without a hint of surprise at my presence."
        mc ed md ba na "That was rather sweet of you, Monika."
        m mb bc eb "Ah, please don't flatter me..."
        m md ea ba "Yuri's a sweet girl, and one of my best friends. I can see myself being a sister figure for her."
        show monika ma
        mc eg mb "So could I. You're very alike."
    
        if branches.is_current(branches.SNARED):
            m mb "So, what were you and the others doing?"
            show monika ma
            mc ea "Ah, you know, just chatting. Not much really, so I decided to come up."
            m mb lpoint "Good. We don't want you too tired for tomorrow, now do we?"
            show monika ma ldown
            mc ml "What does that mean?"
            m mb rhip "It means you are helping me with the festival prep."
            show monika ma
            mc mg "Oh, er, sure."
            mc ef mb "That'd be great."
            m mb ed "Lovely."
            show monika ma
            mc ea ml "So, I'll leave you two be, okay?"
            m mb "Alright then, I'll see you in the morning~"
            show monika ea ma
            mc eg mg "Sure."
    
        else:
            mc ml ea "Should I leave you two be?"
            m md eb "Well, we are pretty much just going to be sleeping..."
            m bc mb ea "Unless you are some pervert that likes watching her gal pals sleep~"
            show monika mc
            mc bd mf nb "I, uh..."
            m mb ea ba "Just joshing you. Sleep well."
            show monika ma
            mc mb bg nb ea "Y- Yeah... You too."
    
        show monika at thide
        hide monika
        "Monika steps back inside, clearly in time for Yuri to exit the bathroom."
        camera master:
            zoom 1.7
        with Dissolve(0.2)
        "I raise an eyebrow, though, at what she says at that point."
        y e1a mb na b1a "How about that huggle then, Madame Rein?"
        m turned casual eb nb mb "A- Ah, of course... Of course. Let me just, um... do one thing first."
        y e3c "Please do."
        camera master:
            0.2
            zoom 1.0
        show white at flash(0.2)
        play sound ["<silence 0.2>", audio.slap]
        "I watch as a piece of paper bounces off the wall, hitting me square in the noggin."
        $ show_poem(monika_poem_2, music=False)
        _mc eb bd nb mh "H- How did she- Ah."
        _mc ec bi "I'll just go."

        stop music fadeout 2.0
        scene black with Dissolve(0.5)

        "I tuck myself into the spare bedroom, and the fatigue hits me like a freight train. I fall asleep without even finishing changing."

    scene black
    pause 0.5
    scene black with monika_pov(True)
    $ set_pov("m")
    $ set_date(day=5, hour=3, minute=14)

    "As I awaken, deep into the night, I find Yuri's hands clasped over mine."
    "Her head on the pillow next to me."
    _m turned casual mc nobow "I'm..."
    _m eb nb "Not sure how I should be acting around Yuri. We're just supposed to be friends, after all - And I've been working so hard to put that little bit of distance between us so she doesn't get ideas, but..."
    _m bc na "The idea she gave me, us being siblings? Maybe, if I can nurture that a little, she might move past this silent infatuation."
    play sound fall
    window auto hide
    pause 0.6
    "As I roll over to get more comfortable..."
    play sound grumble
    "I hear her stomach rumble softly."
    _m ec ma "I guess she's hungry?"
    _m eb ba mc "We didn't even eat dinner... Of course she is."
    _m ea "I don't believe Sayori would mind if I grab a snack - She'd at the very least understand why I did."
    "I carefully slip my hands out from under hers and scoot myself off of the bed on the side opposite of her."
    "I then put on a dressing gown and slip downstairs, making my way to the kitchen."

    scene bg s_kitchen_day with dissolve

    _m turned casual mc ec nobow bc "Now, hm."
    _m ea ba "What would Yuri like?"
    _m ma ec "Her classic tea is something she's taught me to brew, but she'd expect that, no?"
    "I ponder the question to myself for a brief moment, glancing through the pantry, when-"
    _m ea mc "Cookies."
    _m ec bc ma "Sayori will kill us if she finds out we ate her cookies."
    _m ed ba "So~, I'd best be nice and quie-"
    show white at flash
    play sound ["<silence 0.1>", audio.thud]
    "I cringe as the jar makes contact with my foot, haphazardly shoved in between it and the ground. Luckily, a metal jar won't shatter, but..."
    _m ec nb bc "I suppose it's still better than the alternative outcome, no?"
    "I take some cookies, laying them out in a circular shape upon a plate-"
    "-Then take a glass out from the cupboard."
    _m mc na ba "Better not risk making that tea, lest I wake anyone."
    _m ea "No, milk is far safer."

    scene bg s_kitchen_day with fade

    "I look over my offering."
    "Part of me still can't believe I'm waking up to give Yuri cookies and milk in the middle of the night."
    "But... I can't help but think that she would appreciate this. A gesture of our friendship, no?"
    "I just... The more I think about it, the more I hope that's what she sees it as, and nothing more."

    scene black with wipeleft

    "I carry it up the stairs and settle down next to her."

    play music ahog

    m turned casual mb ed nobow "Yuri~?"
    y turned casual e1a b2b mg "M- Mon... ika?"
    m mb "Yes, it's me, Yuri."
    m ea md "I heard your stomach rumbling, so..."
    m mb "I brought you some cookies."
    "Yuri's face of surprised happiness and touched gratefulness makes me smile so very widely."
    m ed "So, sister, ever had a midnight feast?"
    y e2a b1a mh "N- No, I haven't."
    m ea "Well, then this will be a first for both of us."
    "I deftly close the door and lie down next to her."
    "Then turn on my lamp."
    window auto hide None
    hide black
    show cg sleepover 4
    with Fade(0.06, 1.0, 1.5, color="#fff")
    pause 0.05
    $ persistent.sleepover.mark_cg(4)
    "Yuri's face lights up."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m ec "Thought you might like them."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y b1d e2a mb "I- I do..."
    y b1a e3c "Thank you, dearest sister."
    camera master
    with cg_dissolve
    "I shouldn't be this happy about having a sister, since I already have one, but..."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    _m ec ba ma "... With Yuri, it just feels right. The sister I should have had."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m mb "My deepest pleasure."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    "Yuri takes a cookie and slowly bites down on it."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m ea md "Is it nice, Yuri?"
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y e3d "Delectable."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m mb ed "Excellent."
    camera master
    with cg_dissolve
    "Her way with words always brings a smile to my face; one of her laundry list of wonderful traits."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m ea md "Mind if I have one?"
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y e1d mh "Oh, please do Monika. Here."
    "Yuri holds one up."
    camera master
    with cg_dissolve
    "I bend down and take it in my hand."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    "She giggles."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    "I then finish my cookie before speaking again."
    m ec md "Shush, sis..."
    m ea mb "We don't want to wake the others."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y e1a mb "Okay then. But, that was nice..."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    "I smile, taking another cookie into my hand, then to my mouth."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    "She moves her hand to my hair and softly plays with it, twirling it between her fingers."
    y e1d "You have such beautiful hair, Monika."
    camera master
    with cg_dissolve
    "I swallow my cookie."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m ea mb "Of course... Your midnight hue is equally as beautiful though. You take really good care of it."
    camera master
    with cg_dissolve
    "We sit there in silence..."
    "Just staring into each other's eyes, basking in the moment."
    "Her eyes, a hazy purple, and her genuine smile."
    scene black with Dissolve(0.3)
    _m turned casual ec "I'm happy to be her big sister."
    # they are so fucking gay vceuajzevujhFGJH

    scene cg sleepover 4 with Fade(0.0, 1.0, 1.0)

    "After some time, I decide to finally break the silence."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m turned casual md nobow "... Do you think you could tell me a poem, Yuri?"
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y turned casual e1d nb mg "Y- You want to hear my poetry?"
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m mb "Of course, Yuri. You're very talented."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y e2a b1d mb "So are you, Monika."
    y b1a na e3c "You're the type of girl I aspire to."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    "I giggle in response. I can tell she's still a little under the influence, so..."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    "She clears her throat and begins speaking."
    y mh "I gaze into that deceptive water."
    y e2a mb "Crystal-clear and yet impossible to scry in. A murky haunter."
    y mg b1a "I lean ever closer, hoping to touch my restorer."
    y mh b1d "But as I lean in, place my hand on it, an offer."
    show black zorder 10 with NonBlockingDissolve(6.0)
    y e3c "It sucks me in, a captor, a great mirror of horror."
    y b1a "As I move through its depths, it gets stronger..."
    y mg b1d "As I watch unspeakable slaughter..."
    y mh e1d b1a "I burst back out."
    y e1a mg "I splash out."
    y e3c mh "All of the longing for oxygen I had felt is magnified and is directed towards the lake."
    y mb "My want to submerge myself in it."
    y mg "So I cover my eyes."
    y b1d "And lose myself again."
    "Waiting, I held my breath. When Yuri stopped speaking and looked at me, I realised she was done reciting her poem."
    hide black
    camera master:
        align (0.0, 0.23) zoom 2.0
    with NonBlockingDissolve(0.2)
    m md nb "D- Did you just come up with that on the spot Yuri?"
    "I'm stunned."
    _m ma "It was beautiful."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y e2a mb nb "Y- Yes..."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m ec md na "Oh, Yuri. You marvel."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y e1d mb b1a "Thank you... I- I'm curious to see if you can guess what it's about."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    _m ea bc na mc "Hmm-"
    _m ba "Maybe..."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    _m ec "She went into the water."
    _m eb "And came up."
    _m ea bc "And was hungry to go back under?"
    _m ba ma "OH!"
    _m ed "I know!"
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m ea md "Is it..."
    m mb "The feeling of getting absorbed in a book and then finishing it?"
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    "Yuri's smile is obscenely wide."
    y e3d mc na "Exactly."
    y e1d mb "Did you catch the rhyme scheme trick?"
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m md "I believe I did."
    m ec mb "The idea is that the rhyme scheme breaks when she stops reading the book."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y mh "Exactly."
    y e3c mb "I'm glad you caught that."
    y b2b "I'm glad you took the time to listen."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m ec mb "I'm glad we are bonding."
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y e2a "I'm glad you are being kind to me."
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m ea md "Yuri, I... I have a question for you - I know this is a little off-topic, but-"
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y b1a mb e1a na "Please, what is it?"
    camera master:
        align (0.0, 0.23) zoom 2.0
    with cg_dissolve
    m "Did you get... picked on before you met me?"
    m "Like, bullied?"
    camera master:
        align (0.77, 0.25) zoom 2.0
    with cg_dissolve
    y mg e1d "I..."
    "I spy a tear forming in her eye."
    _m bb mc "O- Oh... Maybe that was the wrong thing to ask...?"
    y e2a mh tears_a "P- People don't care about me... They..."
    show black
    camera master
    with cg_dissolve
    "I place a hand on her head, rubbing it softly."
    m ec mb "I care about you, Yuri. You're a wonderful girl, my best friend, and my sister."
    m ba "Don't let anyone ever tell you otherwise."

    scene black with Dissolve(1.5)
    pause 0.6
    scene sky_night at moving_sky
    show sky_stars
    with Dissolve(1.5)
    pause 1.0
    stop music fadeout 2.5
    hide sky_stars
    show sky_afternoon at moving_sky:
        alpha 0.3
    with Dissolve(1.5)
    pause 0.3
    scene bg s_spare_bedroom
    show expression "#000" as stuff1:
        FadingBorders((0, 0, 160, 0))
        xsize 760 xalign 0.0
    show expression "#000" as stuff2:
        FadingBorders((160, 0, 0, 0))
        xsize 350 xpos 1.0 xanchor 260
    with natsuki_pov()
    $ set_date(hour=6, minute=33)
    $ set_pov("n")

    play music a_sunshine

    "The door swings open in front of me as I shake my head."
    _n turned casual notail noband mj e1d b1d "The least she could have done is gotten up herself..."
    "MC lies on top of the sheets, seemingly rolling over after mumbling something along the lines of 'enter' when I knocked."
    n mb b3a e1a "MC, breakfast is ready. Sayori sent me to wake you."
    mc turned casual messy nostrands nohairclip mh eg bi "Mh- hmm..."
    "She rolls onto her stomach, seemingly hand-waving me off."
    n mi e1d b1d "C'mon dude, don't make me enter the room..."
    _n e1a md "I know Sayori told me to 'do whatever it takes', but this still..."
    "Her sprawled form upon the bed seems oddly... Human."
    _n me b1a "You're so odd, MC. With a name like that, you've always been a grand story to me. Something larger than life who worked in strange and mysterious ways."
    _n b1d md "But here you are. And now..."
    _n e2a ma "It's hard to think of you as anything but another one of my weirdo friends."
    _n e3c "... Maybe I'm getting a bit ahead of myself."
    "She turns again, her oversized shirt riding up her legs."
    n nb mm "Dude, seriously, get up. I don't wanna see one of my friends disrobe themselves."
    camera master:
        align (0.95, 0.9) zoom 2.0
    hide stuff1
    hide stuff2
    with Dissolve(0.2)
    "I grab a corner of the sheet and pull it over her."
    n mh e1a b1a na "Now will you get up?"
    mc mf "Mmmm..."
    "I roll my eyes, allowing a small hint of a chuckle to form on my lips."
    _n e2a b1d ma"That's about what I expected..."
    n mb e1d "If you don't get up now, I'm going to drag you downstairs."
    "..."
    n mi e1a b3d "Okay, I'll throw water on you!"
    "..."
    n b4 mh "I'll... tickle you? I dunno, the fuck do you want from me?"
    "..."
    "Still nothing."
    n e1d b1d mm "You know what? Fine, keep the bloody thing."
    play sound fall
    camera master
    with Dissolve(0.2)
    "I take the edges of the sheet and roll them around her, wrapping her up before hoisting her over my shoulder like an oversized sleeping bag."
    n mh e3c "I'll let Sayori deal with this..."
    mc ba ml "Mm... hm?"
    "She seems to stir as I walk out of the room."
    mc mj "Meelz, it's not time yet..."
    "This time, I properly chuckle."
    _n ma "Is that what's on your mind, eh?"
    "Shaking my head, I make for the stairs."
    "Who knew this girl I'd heard so much about could be so cute?"

    $ add_calendar_description(calendar_descriptions["sleepover"], day=4)
    return
