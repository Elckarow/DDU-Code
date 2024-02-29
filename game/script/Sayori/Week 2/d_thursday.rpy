label week_2_thursday_sayori:
    call calendar_transition(day=2, hour=8, minute=44) from _call_calendar_transition_32
    scene black
    show bg mc_living_room:
        blur 2.5
    show sayori turned md e3c b1b:
        i11
        zoom 1.2
    with Dissolve(1.5)
    $ autofocus.block("sayori")
    $ say_transition = True
    play music a_sunshine

    "As I wake, I feel something soft against my face."
    camera master:
        align (0.5, 0.2) zoom 1.6
    show black with NonBlockingDissolve(2.5, time_warp=_warper.easeout):
        alpha 0.95
    "Upon opening my eyes, for a moment, all I can see is darkness."
    "Pulling my head back, I see two large mounds where my eyes were."
    _mc turned messy mh "Ah, that's..."
    mc eb nb "Wait, that's-!"
    hide black
    show sayori e1d at i11
    camera master:
        zoom 1.5
    show bg:
        blur 2.0
    with Fade(0.2, 0.0, 0.3)
    "Sayori stirs as I move."
    s b1d "Mmm... ?"
    s b1a e1a mg "Oh, morning?"
    show sayori mu e3d lup rup with say_dissolve
    mc ea na ml "Yeah, it is, but..."
    s e1a mh "Melody?"
    s rdown ldown b1d mi "What are you doing in my bed?"
    show sayori md with say_dissolve
    mc mj ef "Ah, no, actually..."
    show sayori b1a e2a with say_dissolve
    "Sayori opens her eyes fully, glancing around."
    show sayori e2c with say_dissolve
    "We're still on the recliner."
    s mg "Wait, we..."
    s me b1d e3c "Huh, would you look at that..."
    show sayori b1b ma with say_dissolve
    mc ec bi mg "Uh, Earth to Sayori?"
    "Sayori's still in a daze."
    s b1a e3d mn "Hehehe..."
    s e1a mg "You know..."
    s mb "If either of our parents had still been around..."
    show sayori e2a ma with say_dissolve
    _mc eb nc bb mh "Oh. OH!"
    _mc ea nb ba "Wait, we..."
    _mc "Did we..."
    show bg:
        blur 0.0
    show sayori e1a me
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    "Checking myself, as I stand up, I see that we're both still fully clothed in our school uniforms."
    show sayori b1d e1b nb
    "Those must have been uncomfortable to sleep in."
    $ autofocus.unblock("sayori")
    s mm b2b e3b "Guh, that hurts..."
    show sayori e3c mj at dip
    "Sayori slowly brings herself to a seating position."
    mc bg na mg "What hurts? Do you need ice or something?"
    s e1a b1a mg "Oh, ah, no, it's..."
    show sayori md lup
    "She sheepishly motions to her chest."
    s e2b mg "I..."
    s e1a mb nc "Melly, if there's any chance... Could you turn around for a sec?"
    show sayori md 
    mc ba ml "Oh, sure."
    hide sayori with NonBlockingTransition(wipeleft)
    play sound ["<silence 0.25>", audio.fall]
    "I do so, and hear some rustling of clothing behind me."
    "Sayori breathes an audible sigh of relief."
    s turned nb mh"You can... turn back around now."
    show sayori ma na e3c at i11 with NonBlockingTransition(wiperight)
    "Nothing appears to have changed. Maybe she was just rearranging herself?"
    "Speaking of which, my blazer is crumpled and wrinkled. I'll need to iron both of our uniforms."
    s e1a mh "Is there... any chance I could use your shower?"
    show sayori ma
    mc ef mj "Oh, uh..."
    _mc ec mh "She wants to use mine?"
    mc ml bb ea "Don't you have one at your place?"
    s e2a mb "Oh, yeah, I do, but..."
    show sayori ma
    mc ba mg "Oh, it'd be pretty embarrassing to walk out of the house with your crumpled uniform, y'know?"
    mc ed mb "Here, I'll iron it for you while you take a shower."
    s lup mg e1a "Oh, yeah that's it..."
    show sayori md
    mc ea ml "Oh, is there something else?"
    s e2a b1b mg "Well..."
    s b2a mb nb "If I walk back home looking like this, this time of morning..."
    s b1a e3d ldown mn "I think the neighbours would have some words to say."
    show sayori ma
    mc eb mh "!!"
    _mc ef mh "Ah, shoot. She's totally right."
    _mc "That would be incredibly incriminating."
    show sayori e1a na
    mc ea mb "Yeah, go use my shower, alright?"
    s mh "Yeah. I'll leave the clothes out the front for you."
    show sayori ma
    mc "I'll grab some spares out of my stuff and leave it in the same spot." # im stuff
    s mb "Thanks."
    show sayori ma at rhide
    hide sayori
    stop music fadeout 4.0
    play sound_loop static fadein 10.0 volume 0.5
    "Sayori shuffles away, and I exhale the breath I'd been holding."
    call close_eyes(1.5) from _call_close_eyes_18
    _mc eb bd mh nb "What..."
    _mc "What the hell...?"
    _mc "How did it come to this?"
    _mc "I thought I was going to put a little distance back between us?"
    _mc nc "How did that turn into sleeping together?"
    camera master
    "I look at my hand."
    "I could still feel the soft, fluffy feeling of her hair."
    "It was like patting a cloud of rainbows."
    "But more than that..."
    "An image was burned into my mind."
    camera above_master:
        align (0.5, 0.2) zoom 1.5
        flash(2.0)
    show mc_roof onlayer above_master
    show sayori turned lup rup e3d b2b nc me at i11 onlayer above_master
    "The face Sayori had made last night."
    "And a sound."
    "Her moans."
    "And a feeling."
    "Her soft, gentle figure, wrapped in my arms."
    "And above all, her words."
    show sayori rdown na mb b1a e1d
    camera above_master:
        flash(0.7)
    "'It isn't enough'."
    _mc eg bg mh nb "I just..."
    _mc ea "What... have I done?"

    stop sound_loop fadeout 3.0
    scene bg mc_living_room
    $ clear_layers("above_master")
    camera master:
        blur 3.0 matrixcolor BrightnessMatrix(-0.1)
        ease 6.0 blur 0.7 matrixcolor BrightnessMatrix(0.0)
    with longfade
    play sound_loop tinnitus fadein 10.0

    "After bringing some spare clothes to Sayori to put on, while I clean her uniform, I set up the iron and let it heat up."
    mc turned messy bg eg mm "Ugh, my head..."
    "I'm sporting a splitting hangover, but I can't let it bother me."
    show layer master:
        align (0.35, 1.0) zoom 2.4
    with Dissolve(0.2)
    "As I look at the coffee table, I notice that the wine glasses are still there, but..."
    "There's three empty bottles of wine, and a fourth half empty."
    _mc eb bd nb mh "How much did we drink!?"
    camera master:
        align (0.35, 1.0) zoom 2.4
        easein 0.2 blur 3.0 matrixcolor BrightnessMatrix(1.0)
        zoom 1.0
        ease 3.5 blur 0.0 matrixcolor BrightnessMatrix(0.0)
    show layer master
    "Clutching my head, I feel the pain surge forth, now vindicated in its own presence."
    "I stagger toward the kitchen, and toward my salvation; water and coffee."
    
    scene bg mc_kitchen_day
    camera master
    with wipeleft
    stop sound_loop fadeout 4.0
    pause 0.05
    scene bg mc_living_room with Fade(0.6, 0.0, 0.25)
    $ advance_date(minutes=6)

    "After taking the time to make some coffee, I set two cups down."
    "I take a sip from my cup, then begin ironing the blazers."
    show sayori turned pyjama2 at i11 with fastfade
    $ advance_date(minutes=10)

    play music tswstd

    "Not long after I finish, I hear Sayori walk down the stairs."
    mc turned messy ed md "There's some coffee here for you. I made a mocha - I know you aren't a fan of normal coffee."
    s mb lup "Ah, thanks, Melly~"
    show sayori ldown e3c ma at dip
    "Sitting down next to me on the couch, she takes the drink, as well as the glass of water I had set out for her, and rests her head on my shoulder."
    "The smell of her damp hair is..."
    "Intoxicating."
    "The sight of her wearing my clothes..."
    "Thrilling."
    "And the knowledge that we spent the night in each-other's arms..."
    "Priceless."
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.7
    show sayori e1a me
    with Dissolve(0.2)
    "As I lean back into her, I look upon her figure." 
    "Her phantasmal eyes glisten aquamarine in the morning light, ghosts of last night dance in them like candles burning bright..." 
    "Her sapphire irises shimmering as if imbued by the sea itself, azure and perfect."
    show sayori ma with say_dissolve
    "Honestly, I don't know what to think anymore."
    "But I'm not going to ruin this moment. Not if it kills me."
    show sayori lup e2a 
    camera master:
        zoom 2.0
    show bg:
        blur 2.5
    with Dissolve(0.2)
    "Her hand upon mine sends warming shocks up my arm, making me huddle closer, desperate for warmth and love only she can give."
    "Her soft fingers slowly interlock with my own, and we simply cease to exist, a single, perfected entity."
    "Her scent of flowering buds and ripe strawberries ceaselessly penetrates my nostrils, and I inhale deeply of her incomparable smell." # :SNIFFA:
    "Like breathing life itself upon my senses, and delicious drops of joy upon my parched tongue."
    "However."
    "I intend to never go thirsty for her goodness again."
    "I fear I could never resist the urge, the passion."
    "For it would ruin me, leave me wasting among the fallen."
    "Despite the burning desire in my soul, it simply cannot be."
    "Her fire burns too brightly, too harshly, for me to approach."
    "The intoxicating rush of adrenaline coursing through me, even now, threatens to consume my very essence."
    show sayori e1a me
    camera master:
        zoom 2.2
    show bg:
        blur 3.0
    with Dissolve(0.2)
    "Turning my head, I reposition Sayori's own, and our lips meet once more."

    scene black
    camera master
    with Dissolve(1.0)
    $ advance_date(hours=4)
    pause 0.2

    "I don't know how much time has passed. I simply can't fathom it. For all I know, it could have been years, or seconds, or anything in between."
    "But none of it matters."
    "Nothing else matters, but Sayori."
    "Feeling her. Having her in my embrace."
    "I wish this feeling would never go away."
    "I want to remain connected to her like this, for the rest of my waking hours."
    show bg mc_living_room
    show sayori turned pyjama2 e2a b2a nd:  
        i11
        hop
    hide black
    with NonBlockingDissolve(0.5) 
    "Sayori finally parts from me, her breathing laboured."
    s mb e3c b2b "Hah... Hah..."
    s mo rup e3a b2a nc "You're... improving, you know that?"
    show sayori ma
    mc turned messy ed md nc "Well, I've had a fine teacher."
    s nb mb b2c e2a "Mmm. But then again..."
    show sayori e2c ma
    "Her eyes shift ever so slightly."
    s rdown e1d b1b mb "I think we both..."
    show sayori mg b2b e3c at dip
    "Taking another breath, as her panting was interfering with her ability to speak."
    s mb nd e1d b1a "Could use some more... practice."
    show sayori ma
    "Her face is practically begging me to come at her."
    "Though I knew I shouldn't..."
    "That contains its own type of thrill, doesn't it?"
    show sayori lup e1a
    camera master:
        align (0.5, 0.2) zoom 2.0
    show bg:
        blur 3.0
    with Dissolve(0.2)
    "Placing my hand onto her soft, smooth cheek, I pull her in, and we resume once more in earnest."
    
    scene sky_day at moving_sky
    camera master
    with Dissolve(4.0)
    pause 2.0
    camera master:
        align (0.5, 0.2) zoom 2.2
    show bg mc_living_room:
        blur 3.0
    show sayori turned pyjama2 lup b2c mg e3c nc at i11
    with Dissolve(1.0)
    $ set_date(hour=15, minute=34)

    "Having given up on going to school long ago, the two of us simply remain together, attached at the lips, pausing only to grab the occasional drink."
    "Our lust shows no signs of slowing, as it only deepens as the day grows late."
    show sayori b1a e1b me with None
    camera master
    show bg:
        blur 0.0
    show sayori b2a e1a nd mj ldown 
    with NonBlockingTransition(Fade(0.2, 0.0, 0.2, color="#fff"))
    play sound phone_notification
    stop music fadeout 5.0
    play ambient int_day fadein 5.0
    "Now in a state of minor dishevelment, Sayori jumps at the ringing of her phone, biting my tongue."
    mc turned messy mm eh bg nd "Agh!"
    "Wincing in pain, I jump back, clutching at my mouth."
    show sayori b2c rup ma at dip
    "Sayori places a hand on my shoulder in consolation, as she's already answered the phone."
    show sayori mk e1b 
    "Mouthing the word 'Sorry', she replies to the caller."
    s lup rdown nb e2a b1a mh "Ah, no, I'm not at school today."
    s mg na "Yes, she's here too."
    s mb e3c "I know, thank you."
    show sayori e1b nc mj
    "Sayori suddenly turns red."
    s mk e2b b2a "Ah! No, no no no! It's... Ah, a fever."
    s mh e2a b1a nb "Very funny! I've ah, gotta go."
    s md e2b nd "!!"
    s na e3c mg "... Mmm. Alright. Have fun."
    s me b1b "..."
    show sayori ldown md 
    "Sayori hangs up the phone."
    mc ea mg nb "Who was that?"
    s e1a b1a mh "Ah, it was Natsuki. She was wondering where we were."
    show sayori md
    mc ba ml na "So what did you tell her?"
    s e3c mi "The truth. No point lying to her."
    show sayori ma e1a
    mc bf eb mg "Wha- You told her how much!?"
    s e2a mh "Just that we're home. I mentioned that you had a fever, but..."
    show sayori md
    mc ec bi ml "She didn't buy it, did she?"
    s mg "... No, she didn't."
    show sayori md
    mc ea mg ba "Well, what do you suggest we do?"
    $ autofocus.block("sayori")
    s e1a "..."
    $ autofocus.unblock("sayori")
    s lup mh b4 "Panic?"
    show sayori b1a ma
    _mc ec ma "Yeah, sounds about right."
    _mc thinking ea mh "I don't think Natsuki would tell anyone, but we did skip a day of school together, so there's a chance someone else might..."
    mc ml "Should we..."
    show sayori ldown md
    mc ldown ec "Should we just own up to it?"
    s e2a me "I..."
    show sayori md
    _mc mh "I see where she's coming from. I sure as hell don't want to do that."
    camera master:
        align (0.5, 0.75) zoom 1.0
        ease 6.0 zoom 1.7
    show bg:
        blur 0.0
        ease 6.0 blur 2.5
    show black:
        alpha 0.0
        ease 6.0 alpha 0.7
    play sound_loop heartbeat fadein 6.0
    "Unfortunately, my eyes, as well as my thoughts, are wandering."
    "Specifically to her clothes."
    "Well, my clothes, but they look sooo much better... on her."
    "Makes me wonder..."
    "How they would look..."
    "On my floor."
    "The fact that she's hardly wearing them anymore is not helping."
    show bg:
        blur 0.0
    camera master
    hide black
    stop sound_loop
    _mc eg bi mm nc "Ah, no, stop it, me!"
    _mc "You can't think of her that way!"
    show black with NonBlockingDissolve(2.0)
    _mc "That's really hypocritical."
    _mc mh nb "I know it is."
    _mc ef ba "I just..."
    _mc bg "I can't shake it."
    _mc ea bf "I loved her, once."
    _mc ec bg "And now..."
    _mc bi eg mm "Now I'm falling for her all over again."
    _mc mh "When I swore to myself I would never, ever, let it happen."
    _mc "I couldn't."
    _mc "It wasn't fair to her."
    _mc "It wasn't fair to me."
    _mc ea ba "And yet..."
    hide black
    camera master:
        align (0.5, 0.3) zoom 3.0
    show bg:
        blur 3.0
    with Dissolve(0.2)
    "The nape of her neck looks so inviting..."
    camera master:
        yalign 0.1 zoom 3.5
    with Dissolve(0.2)
    "Her hair ripe to stroke."
    camera master:
        yalign 0.2 zoom 1.7
    with Dissolve(0.2)
    "And her embrace, pure and comforting."
    camera master
    show bg:
        blur 0.0
    show sayori md b2b nb
    with Dissolve(0.2)
    "Shaking my head, I return to the mortal coil, fantasies pushed to the wayside."
    "Sayori doesn't look well. Not at all."
    "She's stressed."
    "I should help her."
    mc bg mb ea "Hey, Sayori, it'll be alright."
    s mg "How do you know th-"
    stop ambient fadeout 3.0
    show sayori me e1b b2c with None
    show sayori e3d mg
    camera master:
        align (0.5, 0.2) zoom 2.0
    show bg:
        blur 3.0
    with Dissolve(0.2)
    $ say_transition = True
    "Embracing her once again, my lips find their way to hers, and all of my worries drift away once again."
    $ autofocus.block("sayori")
    s lup rup me nc "Mm!"
    "Sayori's voice leaks into my ears, stoking my fire further."
    "Wrapping my arms around her tightly, we lock ourselves in an embrace, not unlike what had been our entire day so far."
    "My hands slowly drift upward, target locked."
    "As they travel, they gently grip a section of fabric, taking it with them."
    show sayori nd mg with say_dissolve
    "In tandem, Sayori's breathing grows hotter, and pulls me deeper."
    "My hands, invigorated, move quickly to place themselves under the fabric."
    "As they do, they find their mark."
    show sayori e1b b2a me with say_dissolve
    "-And as a small 'click' sounds out, I feel a sudden change in Sayori."
    camera master
    show bg:
        blur 0.0
    show sayori ldown rdown md b2c e1a
    with Dissolve(0.2)
    $ say_transition = False
    "Pulling back, her eyes remain the same, but something in her face holds great pain."
    $ autofocus.unblock("sayori")
    s mg "I'm sorry..."
    s me e2a b2b "I'm just..."
    show sayori mj
    mc nb bf mb "No, I was out of line, I should be the one apologising."
    s e1a mb b2a "No, a moment ago, I was happy, but..."
    show sayori md
    mc bg ef ml "I'm sorry. I'll give you some time."
    s e3c mg b2b "... Thank you, Melody."
    s mb e1a lup "I really do appreciate it."
    show sayori ma at thide
    hide sayori
    "Getting up, I make my way to the kitchen, with much more speed than I normally would."

    scene bg mc_kitchen_day with wipeleft
    show black with NonBlockingDissolve(0.3):
        alpha 0.7

    _mc turned messy eb bg mh "It's official. I'm a monster."
    _mc "I'm, objectively, a monster."
    _mc "I just made a move on my best friend."
    _mc "I just made her uncomfortable."
    _mc eg "I did this."
    _mc "It's happening all over again."
    _mc "I'm doing it again."
    _mc "This can't be happening."
    _mc eb "I swear, this cannot be happening."
    _mc "This is why I had to distance myself from her."
    _mc bd "This is EXACTLY why."
    _mc eg bi "I can't do it."
    _mc bg "I'm only hurting her."
    _mc ec "{cps=12}{i}{b}...I will only ever hurt her........{/b}{/i}{/cps}{nw}"
    
    window auto hide None
    show black:
        alpha 1.0
    camera master:
        align (1.0, 1.0) zoom 2.7
    pause 4.0
    play sound fall
    show black with NonBlockingDissolve(5.0):
        alpha 0.8
    play ambient int_day fadein 2.0

    "Slumping down the wall, I curl my arms around my face."
    "It's more than I deserve."
    "I shouldn't have arms, not after what they've done."
    "Nor should I have lips."
    _mc turned messy eg bg mh "{cps=12}What have I done...?{/cps}"

    stop ambient fadeout 3.0
    scene bg mc_kitchen_day
    camera master
    with Fade(1.3, 0.3, 1.0)
    $ advance_date(minutes=48)
    phone register "mc_s":
        time auto True
        "s" "Sorry, I had to go home to sort something out."
        "s" "If you want, I can come back later tonight though."
        "s" "If not, I'll see you in the morning, alright?"
    $ advance_date(hours=3)
    play ambient int_night fadein 2.0

    "By the time I finally have the courage to open my eyes, Sayori is gone."
    "All I was left with was a text."
    phone discussion "mc_s":
        pause
    "I don't think I could bear to look her in the eye right now."
    "Hell, I don't know if I'll ever be able to again."
    _mc turned messy ec mh "Maybe it would be best to just..."
    _mc eg "Not."
    phone end discussion
    _mc "Yeah."
    _mc "It would be for the best."

    scene black with wipeleft_scene
    $ set_date(hour=23, minute=47)

    "The rest of my night passes me by."
    "I never did respond to that text."

    $ add_calendar_description(calendar_descriptions["sayori"][7])

    call week_2_friday_sayori from _call_week_2_friday_sayori
    return