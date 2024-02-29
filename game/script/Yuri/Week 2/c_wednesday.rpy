label week_2_wednesday_yuri:
    call calendar_transition(day=1, month=11, hour=4, minute=10, second=35) from _call_calendar_transition_43
    scene black with Dissolve(1.0)
    scene black with mc_pov(True)
    $ set_pov("mc")
    $ set_internet(True)
    
    mc turned messy naked nostrands eg bi mj "Uugh..."
    mc ec mh "Rise and shine..."
    
    play ambient int_day fadein 3.0
    scene bg mc_bedroom_day_closed with Dissolve(0.5)

    _mc turned messy naked nostrands mh "Should I even go to school today...?"
    _mc ec "Not like I would learn anything new about Yuri."
    _mc eg bi "..."
    _mc ec "No, skipping school is bad."
    _mc ef ba "I'll go."
    _mc bi "But..."
    _mc ea ba thinking "... Maybe I'll skip the Literature Club..."
    "I sigh softly to myself."
    _mc ldown mj eg "... I'll see."
    
    stop ambient fadeout 2.0
    scene bg school_gate_day with wipeleft_scene
    $ set_date(hour=8, minute=3)
    $ set_internet(False)
    play music hnt

    "As I look around, seeing a million couples and people smiling, I can't help but think..."
    _mc turned messy ec mh "... I want to go home, I need more time."
    _mc ef bi ma "I don't think anyone missed me, particularly."
    _mc ea ba mh "But... grades determine my future. If nothing else, I need to think of my grades."
    "Getting close to the entrance, I hear none other than Amelia, nearly screaming into my ear."
    show amelia turned ponytail lup eb mf at t11
    am "{size=+3}Melody? What's with your face?{/size}"
    show amelia ma
    mc bg ec mg nb "What...?"
    am mh ec ldown "I'll repeat. Your face."
    show amelia md
    mc ml bd na ea "There's nothing wrong with my face. I checked this morning."
    am bd eb me "You look so... bummed?"
    am ba mb "What's up?"
    show amelia md ea
    mc ef mg bi "I don't want to talk about it."
    mc ec ml "What are you even doing here, hanging by the entrance?"
    $ autofocus.block("amelia")
    am ed "..."
    $ autofocus.unblock("amelia")
    am mb "No reason."
    show amelia ma bd
    mc ec ba mh "...?"
    camera master:
        align (0.5, 0.2) zoom 1.7
    show bg:
        blur 2.5
    with Dissolve(0.2)
    "I look at Amelia's face carefully."
    _mc ea "A slight twinge of nervousness?"
    _mc ec "What is she nervous about?"
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    mc mj bi "There's something with your face, too."
    am bh ec mb lup "Nuh-uh."
    am bb ef "Nothing wrong there."
    show amelia ma
    mc ef mg "I know you're lying."
    mc ea ba ml "Normally, you're inside by now, doing whatever you do."
    show amelia ldown ec md ba
    mc ec mg "Spill the tea."
    am bg me "Are you trying to be that professor with a top hat, or that attorney with his blue suit?"
    show amelia md
    mc ml bd ea "Pardon?"
    show amelia mh ee ba at dip
    "Amelia sighs."
    am ed me "You should really play more games."
    am mf ee "-But, yeah. You got me. I am..."
    am lup bd mb ea "-Concerned about you."
    am eb ldown ba me "Where were you yesterday? I was searching for you."
    show amelia mg ea
    mc ba nb "Oh... Yeah..."
    mc ef mg na "Was everyone alright in my absence...?"
    am ec mi "How would I know? I don't go to your club."
    show amelia md
    mc mf bi "Right..."
    am mf ee bb "You are so out of it, Mel."
    show amelia md ba eb
    mc ef ml ba "I was... sick."
    am eb me ba "Is it about Literature Club stuff?" # im stuff
    am ef mb "You know, I figured people who joined a Literature Club would be more theatrical, but things took an even quicker turn than I thought!"
    show amelia ma
    mc ec bi mj "... Are you saying I'm being dramatic?"
    am ed mb "Maybe a little bit."
    show amelia ma
    mc ef mf ba "Haha..."
    hide amelia
    camera master:
        align (1.0, 0.9) zoom 2.6
    with Dissolve(0.2)
    "I nod, looking away from Amelia."
    am turned ponytail rup mb ec bd "Hey..."
    "She puts her hand on my shoulder."
    am ba ed me "I might be... zealous sometimes, but..."
    am eb mb "I don't mind sitting down with you sometime to talk things out."
    am bd "To support you."
    show amelia ma at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    "I look back at Amelia, a little touched, but also surprised, by her statement."
    mc mb bg ea "Is that why you made that mod for me?"
    mc mg ba "So I could... vent in a way?"
    am ec mi ba "No, I just wanted to beat the shit out of Kaito."
    show amelia ma with say_dissolve
    mc ec mj "That's... very fair."
    show amelia eb with say_dissolve
    mc eg mb "That was fun, you know."
    mc ea bg "Thanks for that."
    am ee mb "Always, Melody."
    show amelia ma with say_dissolve
    mc ef mh "..."
    mc bi mf "For now..."
    show amelia ea with say_dissolve
    mc ba mg "I think... I just need some time."
    am mb "I gotcha."
    show amelia ma with say_dissolve
    mc ea mb "... I need to go now, class is starting soon."
    am mb eb "Alright. Stay safe, kay?"
    show amelia ma with say_dissolve
    mc eg "I will. Catch you some other time, Amelia."
    camera master
    hide amelia
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("amelia")
    $ say_transition = False
    "I half heartedly smile at her, and head off to class."

    stop music fadeout 2.0
    scene black with Dissolve(1.5)
    pause 1.5
    hide black
    show bg class_1_day
    call close_eyes(0.0) from _call_close_eyes_25
    play sound school_bell
    play ambient students fadein 5.0
    $ set_date(hour=15, minute=10)

    t "Class dismissed! Don't forget to submit your homework this Friday!"
    call open_eyes(1.0) from _call_open_eyes_17
    _mc turned messy eg bi mh "Finally..."
    _mc ec "Can't say I was looking forward to any of this."
    _mc ef ba "... Can't say I'm looking forward to my friends either."
    _mc bi "I can't talk with them properly..."
    _mc "..."
    _mc eg mm "I need to think."

    stop ambient fadeout 1.5
    scene bg school_bathroom with fade
    $ advance_date(minutes=5)
    $ autofocus.block("melody")
    play sound_loop static fadein 6.0

    "As I head to the bathroom with a head filled with thoughts..."
    show bg:
        align (1.0, 0.35) zoom 2.0 blur 2.0
    show black zorder 1:
        alpha 0.35
    show expression AlphaMask("bg school_bathroom", mask="mod_assets/BG/montages/masks/school_bathroom_mirror_mask.png") zorder 2:
        align (1.0, 0.35) zoom 2.0
    show melody turned messy ec mh onlayer above_master:
        xcenter 0.61 yalign 1.0 zoom 0.79
        yoffset 120
    camera above_master at Transform(perspective=True, matrixtransform=Matrix.rotate(0, -25, 0)), renpy.partial(AlphaMask, mask=Transform("mod_assets/BG/montages/masks/school_bathroom_mirror_mask.png", align=(1.0, 0.35), zoom=2.0))
    with Dissolve(0.3)
    "I pass by the mirror and look at myself."
    show melody thinking bg eg with say_dissolve
    _mc "What do I even want at this point..."
    show melody ef bf mf with say_dissolve
    _mc "The girl I am interested in seems... troubled."
    show melody bi mh with say_dissolve
    _mc "Yet... I can't talk to her."
    show melody ba with say_dissolve
    _mc "..."
    show melody ldown mh bi eg with say_dissolve
    _mc "I should just give up."
    show melody ba ef with say_dissolve
    _mc "I asked everyone what's going on... yet..."
    show melody bb eg mg with say_dissolve
    _mc "They can't tell me a single thing other than 'she's having a hard time.'"
    show melody eb bd mf with say_dissolve
    _mc "Then they ask me to support her?"
    show melody eg mm bi with say_dissolve
    _mc "How the hell do I even start with that if I don't know what's going on?"
    show melody bd ea mh with say_dissolve
    _mc "Screw it."
    show melody ea_b noblink 
    stop sound_loop fadeout 0.05
    _mc "I'm leaving the club."
    show melody bi eg
    _mc "At this point, it's more trouble than it's worth."
    show melody bd ea_b 
    _mc "If every club meeting is going to end with a dramatic walk out, might as well make it permanent."
    
    scene bg school_corridor_1_day
    $ clear_layers("above_master")
    with fade
    $ advance_date(minutes=2)
    $ autofocus.unblock("melody")

    "I walk towards the hallway, slowly approaching the Literature Club."
    _mc turned messy ec bi mh "I know they won't like this, but I can't."
    _mc ef "I can't-"
    show yuri turned e1d mh lup at t11
    y "MC?"
    show yuri ma
    mc nb mf ea bg "H- Huh?"
    "Before me stands Yuri, and she's..."
    "Slightly smiling at me?"

    play music playwme

    y ldown mb e1a "Should we go read something together?"
    show yuri ma
    _mc mh "What is this, a dream?"
    mc ml bf "Um... Alright."
    show yuri lup at dip
    "She tenderly takes my hand before I can even think to protest, and we head inside."
    show yuri at thide
    hide yuri

    scene bg club_day:
        align (0.0, 0.8) zoom 1.9 blur 1.5
    show yuri turned at i42
    camera master:
        align (0.5, 0.1) zoom 1.5
    with wipeleft
    $ autofocus.block("yuri")
    $ say_transition = True
    y mg e1d "Are you... feeling better?"
    show yuri ma with say_dissolve
    mc turned messy ef bg mb "Y... Yeah."
    show yuri e3c 
    show expression split("bg class_2_day", "bg club_day", "bg club_closet_day") as stuff onlayer above_master
    show natsuki cross e2c md at i55 onlayer above_master
    show monika turned rhip ec bc mc at i51 onlayer above_master
    show sayori turned e2a at i11 onlayer above_master
    with Dissolve(0.2)
    "As we sit down, I see that the rest of the club seems to largely pretend I don't exist..."
    hide monika
    hide sayori 
    show natsuki at i44
    camera above_master:
        align (1.0, 0.25) zoom 1.5
    show bg club_closet_day onlayer above_master as stuff:
        blur 2.0
    with Dissolve(0.2)
    "Even Natsuki, who's cut is still visible, doesn't seem to be interested."
    _mc bd eb nb mh "What's going on here?"
    $ clear_layers("above_master")
    show yuri e1a
    with Dissolve(0.2)
    y mb "What do you want to read?"
    show yuri ma with say_dissolve
    mc mg bb ea "Well... What choices do we have?"
    y lup e1d mh "Why don't we continue where we left off? We never did finish {i}Something Wicked This Way Comes{/i}."
    show yuri ma with say_dissolve
    mc ef mb ba "... Actually, that sounds fine to me."
    show yuri ldown e3c with say_dissolve
    "Yuri wastes no time grabbing the book, and putting it on the table."
    show yuri e1a with say_dissolve
    "She gives a slight smile to me, and we open it to where we left off previously."
    "My mind, however, can't help itself from wandering."
    show bg club_closet_day as stuff onlayer above_master
    show natsuki cross mj e2a at i55 onlayer above_master
    with Dissolve(0.2)    
    _mc ec mh na "That cut..."
    _mc ea thinking "What's the full story behind it?"
    $ clear_layers("above_master")
    show yuri e2a md
    with Dissolve(0.2)
    _mc ea "Was she involved?"
    _mc ec "Seems highly likely..."
    stop music fadeout 3.0
    show black with NonBlockingDissolve(2.0)
    _mc ea bd "But why on Earth would she do that to Natsuki?"
    _mc ba "And what happened yesterday? Did they plan something...?"
    _mc bd eb "What is this interconnected web of insanity that I've found myself in?!"
    _mc ldown eg bi "I should leave! I should. Why am I even doing this to myself?"
    _mc ea bd "My self preservation kicked in and it hasn't failed me before!"
    _mc ba "So, why am I not listening to my better judgement?"
    show yuri b1d nb
    hide black 
    with NonBlockingDissolve(0.5)
    "I look at Yuri who seems a bit restless in her seat."
    "One glimpse of her and my heart sinks in my chest like it's being dragged into a whirlpool, leaving my arms numb and flailing for sensation."
    "Yet the feeling..."
    "Even though it's terrifying..."
    "It's also exhilirating."
    show yuri e1d me b1a na with Dissolve(0.2)
    pause 0.6
    show yuri e1a ma with Dissolve(0.5)
    pause 1.0
    _mc ec bi "I think I'm going to see this through."

    play music pensive

    show yuri e1d me with say_dissolve
    _mc ef "Maybe..."
    _mc ea ba "Maybe I should-"
    y e3c b2b mb "I'm sorry..."
    show yuri mj with say_dissolve 
    _mc bd mf "Huh?"
    y mh e2a b2a "I know I haven't... talked much with you."
    y mk b2b nb lup "P- Please don't think I dislike you or anything-"
    y mg e3c "-It's just that... I feel so nervous all the time."
    y mh "I hope that..."
    y e1a mb "I didn't hurt you in any way."
    show yuri ma ldown with say_dissolve
    mc ml nb ba "Y- Yuri?"
    mc ef "I..."
    mc mf bf "Um..."
    mc na ea bg mb "Thank you..."
    show yuri e3c me na with say_dissolve
    "Yuri closes her eyes, seemingly attempting to say something."
    y mh "{size=-7}Do you want to...{/size}"
    y rup lup mg "{size=-9}Do you want to walk...{/size}"  
    y me e2a "{size=-15}Do you want to walk home with me?{/size}"
    show yuri md with say_dissolve
    mc ml nb ba "Sorry, I didn't quite catch that..."
    show yuri e3c b1d me with say_dissolve
    "Yuri sighs."
    y ml e1b b2a nb "Do you want to walk home with me after school?"
    show yuri me with say_dissolve
    mc mh bb "..."
    y e2a ma b2b "..."
    show yuri e1a me with say_dissolve
    "I think deeply about my decision. Yuri being this straightforward is odd."
    "Not to forget, the rest of the club is dead silent..."
    "Like this is some sort of play."
    _mc eg bi ma "Ugh, I am starting to sound like Amelia..."
    "I take a deep breath to prepare my response."
    mc ml nb ba ea "Y- Yeah."
    show yuri rdown ldown b1a e1b ma nd with say_dissolve
    "Yuri attempts to smile widely."
    mc mf na "Yuri..."
    "Yet, things still ache at the back of my mind."
    show yuri e1d nb md with say_dissolve
    mc ef bg ml "It's just... I'm confused."
    mc ea bf mb "I want know you better, you know?"
    mc bi mf ef "It's difficult when I feel so... shut out."
    show yuri e2a b1d with say_dissolve
    mc mg ba "Do you feel like talking about-"
    show yuri e1a na with say_dissolve
    "Before I finish my sentence, I get interrupted by a confident looking Yuri."
    y e3c mh "No..."
    y b2b mg "Rather not..."
    show yuri me with say_dissolve
    "Her face shifts from confidence to nervousness as I raise my eyebrows."
    _mc ec bi mh "She's not helping me get rid of my confusion huh..."
    show yuri ma with say_dissolve
    mc ba ml ea "Well... "
    mc mb "Alright. I am sure you'll tell me later, right?"
    y mg "U- Um..."
    y e1a mb b2a "M- Maybe...?"
    show yuri md b1a ldown rdown with say_dissolve
    _mc mh eg bi "Yuri..."
    "I sigh out of frustration."
    mc ef ba ml "I... Alright then."
    _mc ea mh "Yuri's always been the mysterious one in my eyes..."
    _mc ec "And this mystery of hers just seems impossible to solve..."
    y e2a mb b1d lup "Do you... read much?"
    show yuri ma nb with say_dissolve
    _mc "..."
    _mc eg bi ma "It makes me feel better knowing I am not the only socially awkward one at least..."
    mc ea mb ba "Yeah, that's why I chose the club, remember?"
    y e1d b1a mg "O- Oh."
    y na mh "It wasn't because of Sayori...?"
    show yuri md with say_dissolve
    _mc mf bg "Aww geez, Sayori. Having seen her so little these past few days, I'd almost forgotten she was even here..."
    "I shake my head."
    mc ef mb ba "Sayori and I were good friends, but... I hadn't spoken to her for a while until I joined the club two weeks ago..."
    mc ea mg thinking "How about you? Why did you join the club?"
    y b1d e2c mg "That's... a long story."
    show yuri md
    show bg class_2_day as stuff onlayer above_master
    show monika turned rhip eb mc at i42 onlayer above_master
    with NonBlockingDissolve(0.2)
    "She glances at Monika for a second or two."
    _mc mh "Monika, huh?"
    _mc eg ma "I shouldn't be so surprised."
    $ renpy.scene("above_master")
    with NonBlockingDissolve(0.2)
    mc ea mg ldown "Because of Monika?"
    y lup e1d b1a mh "Yeah... She's just- nice... you know?"
    y nb e1b b2b mk "A- Ah! Forget I said that..."
    show yuri mj e2a ldown with say_dissolve
    mc eh bg md "Hehe, don't worry~"
    mc ea mb ba "I am sure she feels the same way. You two are good friends, after all."
    mc bg "There's no need to be ashamed of that, y'know?"
    y mb "Y- Yeah."
    show yuri ma with say_dissolve
    "I gesture to the book between our desks."
    show yuri e1a b1a na md with say_dissolve
    mc ml ba "Let's continue this book?"
    y ma e2a "M- Mhm."
    hide yuri
    show monika turned at i42
    show bg class_2_day:
        blur 0.0 zoom 1.0
    camera master
    with NonBlockingDissolve(0.5)
    $ say_transition = False
    "As we read, I can't help but notice Monika smile."
    _mc ec ba ma "So it {i}was{/i} your plan..."
    _mc eg mh "Huh."
    _mc ef "I guess I should say it."
    _mc ea mf "Thanks...?"
    $ autofocus.unblock("yuri")

    stop music fadeout 2.0
    scene bg school_street_afternoon
    show yuri turned:
        matrixcolor TintMatrix("#ffeede")
        t11
    with longfade
    $ set_date(hour=16, minute=34)
    play music anewday

    "After a little time walking down the street, silently keeping to ourselves, Yuri turns to me." 
    mc turned messy mb "Hey Yuri, where do you live?"
    y e2a mg "Well..."
    y e1a mb lup "Not too far from school."
    y e1d mh "You?"
    show yuri md
    mc thinking ml "About a thirty minute walk, actually."
    y e1a mb ldown "Do you think it's fate...?"
    show yuri ma
    mc ldown bd mf "Huh?"
    y e2a mg "Having a home so close to our school..."
    y e1d mh "Then eventually going to said school..."
    y shy ma eb "Meeting us, and being reunited with your childhood friend..."
    show yuri mc
    mc ef ba mf "...Maybe."
    mc ea mg "But to be entirely honest, that seems to imply that fate is in my favor, which..."
    mc eg bi mb  "Well, I know better than that."
    y "That seems pessimistic."
    mc ea mg ba "It's realistic."
    mc ml thinking "What do you think?"
    show yuri bb ee ma
    "She nods, and as a character from a book, she stares into the distance."
    y ea "I never told you, but..."
    y ba mc "Not only do I like gothic things..."
    y turned e1d mb "I like pondering on abstract concepts."
    y lup e2a b1d mg "Like..."
    show yuri md
    "Yuri briefly falls silent, before turning back to me."
    y e1d mh "Who are we, really?"
    show yuri md
    mc ec mh "Hmm?"
    mc ea mg "That's a very broad question."
    mc ldown ml "You mean like-"
    y ldown mh b1a "Like, what are we in the grand scheme of things?"
    show yuri md
    _mc ec mh "... Huh..."
    mc ef ml "I don't think about those sorts of things."
    mc ea mg "Because... why should it matter who we are to everyone else?"
    mc eg ml "It's not like we actually do."
    mc ea mg thinking "Shouldn't you live for yourself?"
    $ autofocus.block("yuri")
    y "..."
    y e2a b1d "..."
    $ autofocus.unblock("yuri")
    y mb lup "Yes."
    y mg "I suppose."
    y e3c me "It's just..."
    y b1a e1d mh "It's comforting to think we're meant something more."
    y me "..."
    y b1d ldown mg e2a "For someone more."
    show yuri md
    $ renpy.music.set_volume(0.2, 0.4)
    play sound heartbeat
    show black:
        on show:
            alpha 0.0
            ease 0.4 alpha 0.6
        on hide:
            ease 0.4 alpha 0.0
    "My heart stops."
    _mc eb mh ldown "Does she know-"
    hide black
    $ renpy.music.set_volume(1.0, 0.4)
    y b1a mg "I hope I am right on who I think I may be for."
    show yuri md
    mc ea nb "..."
    show yuri e1d me
    mc mf bf "W- Who's that...?"
    y mg lup "M-"
    stop music
    $ autofocus.force_focus("yuri")
    window hide None 
    pause 1.0
    window auto show None
    $ autofocus.restore_focus("yuri")
    y me "..."
    y e1b nb b2b "!"
    y mk "A- Ah!"
    y e2b b2b mb rup "S- Sorry!"
    y mg "I... I don't-"
    show yuri mj
    mc bf mg nb "N- No no no, it's okay!"
    show yuri e2a md
    mc ef bi mf "M- Maybe we should um.."
    mc eb mb bb "Oh! W- What are your hobbies!?"
    "My question to her echoes throughout the street we are standing in."
    _mc eg mj "Crap... I said that a bit too loud."
    _mc ba mh "But damn... What was Yuri about to say?"
    _mc eb bd "M...? Melody...?"
    _mc eg bi na "Wait... She wouldn't just say that straight up... right?"
    y b1a na mg "I... like-"
    show yuri e1d me na ldown rdown
    play sound widenekoflap
    wnf "Meow!"
    "As we both turn our heads to look at the source of this cute noise..."
    "We see a-"

    play music rgb

    y mg "Cats?"
    show yuri ma
    "A small black cat greets us as it's sitting near a home in my neighbourhood."
    play sound widenekoflap
    wnf "Meooow!"
    mc ml ba na ea "I... didn't know I had a cat in the neighbourhood."
    show widenekoflap:
        align (0.8, 1.0) zoom 0.5
    show bg:
        align (0.88, 0.7) zoom 3.0
    show yuri e2a:
        xzoom -1.2 yzoom 1.2
        ypos 1.0 yanchor 0.79 xcenter 0.35
        matrixtransform RotateMatrix(0, 0, 1)
    with Dissolve(0.3)
    $ autofocus.block("yuri")
    $ say_transition = True
    "Yuri slowly approaches the cat."
    show yuri lup with say_dissolve
    "Reaching out to it."
    y mb "Cute kitty..."
    show yuri ma e3c with say_dissolve
    "Reaching the cat, she pets it."
    show widenekoflap mb
    y e2a mb "Who's a cute kitty?"
    show yuri ma with say_dissolve
    _mc ec ma "Yuri's a cat person huh..."
    mc ea mg "Do you have a cat yourself?"
    y e1d mh "No, but... I would love to."
    y mb e1a "... What about you...?"
    show yuri ma with say_dissolve
    mc eg ml "No pets."
    y md "Hmm..."
    y e1d mh "But would you like one?"
    show yuri me with say_dissolve
    mc ea mg "I don't really know."
    mc ec ml "It might be a lot of responsi-"
    y e1a mb "Could you come here, MC?"
    show yuri ma with say_dissolve
    mc ea mf "Huh? Um... okay."
    show yuri e2a rup ldown
    camera master:
        align (1.0, 0.65) zoom 1.2
    with Dissolve(0.2)
    "As I come closer, Yuri grabs my hand."
    mc bf nb mf "Y- Yuri?"
    show yuri e1a with say_dissolve
    "She guides my hand to the cat, while looking into my eyes."
    y mb "Pet the cat."
    show yuri ma with say_dissolve
    mc ba mh na "..."
    y rdown e3c "..."
    show widenekoflap mc with say_dissolve
    "As I slowly pet the cat, I can't help but feel a sense of peace and tranquillity."
    y "..."
    y e1d mh "Do you think it's fate that we met this cat, MC?"
    show yuri md with say_dissolve
    mc bd ml ea nb "Are--Are you trying to be funny?"
    y e1a mb "Is it working?"  
    show yuri ma with say_dissolve
    "I giggle." 
    mc eh md bb na "I'd say so."
    show yuri e1d md with say_dissolve
    mc ea mb "And honestly, Yuri..."
    mc mg ba "You like pondering on destiny, fate and all that, but..."
    mc eg mb "Do we really need more of a reason to appreciate a cute cat?"
    y e2c mg "... No."
    y e3c mh "We don't."
    y mb "It can just be a nice moment."
    y ma "..."
    show sky_afternoon at moving_sky onlayer above_master
    with NonBlockingDissolve(1.0)
    "As we look at the sky... "
    show sky_night as stuff at moving_sky onlayer above_master with NonBlockingDissolve(0.7):
        alpha 0.6 matrixcolor SaturationMatrix(0.5)
    "A dark cloud slowly approaches."
    $ renpy.scene("above_master")
    with NonBlockingDissolve(0.5)
    mc ba ml ea "I think it's best we go home before the rain starts."
    mc mg bf "Is... that fine with you...?"
    y e2c mg "... Yeah."
    camera master
    hide yuri
    hide widenekoflap
    show yuri turned md:
        i11
        matrixcolor TintMatrix("#ffeede")
    show bg:
        zoom 1.0
    with Dissolve(0.3)
    $ say_transition = False
    "We both stand up, and look at one another."
    $ autofocus.unblock("yuri")
    y b2b mb "T- Thanks... MC."
    y mh b1a e1d "It was fun."
    y shy eb mc "S... Same thing tomorrow?"
    mc mg ba "Y- Yes!"
    mc mb "I'd love that. Thank you as well, Yuri."
    y ea ma "Then... I think I'll be going."
    y turned lup mh e1d "Be sure to give this kitty your attention once she asks for it... okay?"
    show yuri ma
    mc eg mb "I'll certainly try."
    show yuri e1a ldown
    "As a smile appears on her face once more..."
    y mb "See you, MC... and kitty."
    show yuri ma at thide
    mc ea "See you, Yuri!"
    hide yuri
    "She turns around, and heads home."
    _mc ma "Yeah..."
    _mc ec "Same thing tomorrow."
    show widenekoflap mc:
        align (0.8, 1.0) zoom 0.5
    show bg:
        align (0.88, 0.7) zoom 3.0
    camera master:
        align (1.0, 0.65) zoom 1.2
    with Dissolve(0.2)
    "I pet the kitty one last time..."
    "And head on home."

    $ add_calendar_description(calendar_descriptions["yuri"][7])

    call week_2_thursday_yuri from _call_week_2_thursday_yuri
    return