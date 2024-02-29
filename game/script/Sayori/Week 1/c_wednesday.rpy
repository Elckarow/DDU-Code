label week_1_wednesday_sayori:
    call act_card("act_I_s_card") from _call_act_card_3
    call calendar_transition(day=25, hour=6, minute=0, second=0) from _call_calendar_transition_25
    stop music fadeout 2.0
    scene black
    show bg mc_bedroom_day_open
    with Dissolve(1.5)
    play sound_loop phone_alarm fadein 2.0
    pause 1.5

    _mc turned messy naked nostrands ec mh "Is it time already?"
    "..."
    _mc eg bi mm "Ugh, fine."
    stop sound_loop
    _mc bd ec mj "Time to get up."

    hide black with Dissolve(0.3)
    play music a_sunshine

    "Pulling myself from slumber, I draw the curtains, and prepare my routine."
    _mc bc eg mg "School today, as usual."
    _mc ec ba mh "Well, as usual as it gets, I suppose."
    _mc eb bf "I'll admit, the thought of graduating in just over six months terrifies me."
    _mc ea mh ba "The boss has been helping me come up with a plan, but..."
    _mc ef "I know I want to go to university."
    _mc eg bi "What I'm going to do? Hell if I know."
    _mc ba "But I know it will be something."
    _mc ma "Something good."
    _mc ec "Something worth doing."
    _mc eg bi mm "Ugh, imagine getting sentimental this early in the morning."
    _mc ma "Couldn't be me."
    "With my... morning pep talk? over with, I set off for my shower. Gotta be prepared for today."
    "I'm not sure why, but it feels like it's gonna be a big day."

    scene bg residential_day with wipeleft_scene
    $ set_date(hour=7, minute=50)
    $ set_internet(False)

    "As I leave, something stops me."
    show bg s_house_day with Dissolve(0.4)
    _mc turned tail nostrands ec mh "Sayori's place is just there."
    _mc ea thinking mf bb "Maybe I should ask her to walk to school with me?"
    _mc ed mh ba "I mean, it would be polite, considering she lives right next to me."
    _mc bd ec "Or would it? We haven't really talked in years."
    _mc bi ldown eg mm "Argh, I really don't want to think about that right now."
    _mc ef ba mh "I might leave it for the day."
    _mc ec "Best to head off for school, in case I'm late."
    _mc ea bb "Maybe I'll ask her at the club today?"
    _mc ec ma "Yeah, that sounds like a good idea."
    _mc eg "Be smarter than just knocking on the door, at least."
    _mc ea mf "Alright, let's do that. It would be better for her, wouldn't it? Than just barging into her house, I mean."
    _mc ec mh "Hell, I haven't been inside her house in years, but what I do remember is how similar it is to mine."
    _mc ef ma "Not perfectly identical, of course. Her family had a different taste in furniture and decor than mine ever did."
    _mc mh "Though, I've packed away or sold most of that old garbage anyway."
    _mc eg bi "Yeah, let's hide that demon away again. That's what, twice this morning? Seeing Sayori again must have awakened it."
    show bg residential_day with Dissolve(0.4)
    _mc ba ef "... I don't know how I feel about that, if I'm honest."
    _mc mf "Maybe catching up with Sayori isn't such a good idea."
    _mc thinking eg bi mm "Ah, what am I thinking? She was my best friend! How could I even consider backing out now?"
    _mc ef bf ma "Sayori was once my entire world. It brings back memories just being in the same room as her."
    _mc ldown "She was a good friend."
    _mc mh bg "The greatest of friends."
    _mc bi eg "And that's why I can't just back off."
    _mc ea nc mh ba "Even if those days are dead, perhaps there's a chance..."
    _mc eb mf nb bb "N- No, stop, bad me."
    _mc eg mm bi "Those thoughts need to be killed off if I'm going to hang out with Sayori again."
    _mc ef ba mh na "That was a long time ago."
    play sound beep
    "I feel my watch beep, indicating the alarm set for school."
    _mc eb bb "Geez, what am I thinking? Gotta get to school before I'm late!"
    show bg school_street_day with NonBlockingDissolve(0.4)
    "I rush off down the road, though I could have sworn I noticed Sayori's curtain move."
    "Nah. Must have been my imagination."

    stop music fadeout 2.0
    scene bg club_day with longfade
    $ set_date(hour=15, minute=18)
    play music playwme

    "Well, here I am again."
    "I didn't really have to convince myself to come back - The girls here are all really cool."
    show natsuki turned:
        i11
        flash
    _mc turned tail nostrands thinking mh "Natsuki's got some charm, with her brash and outlandish personality." 
    _mc ef "She strikes me as someone who is actually pretty introverted though." 
    _mc ldown ma "Maybe the club brings out another side to her?"
    hide natsuki
    show yuri turned lup:
        i11
        flash
    _mc ea mh "Yuri, on the other hand, is pretty introverted, even inside the clubroom. Though, something tells me she's kinda happy that way."
    show monika turned:
        i11
        flash
    _mc eg "And then there's Monika."
    _mc ma "Where do I begin?" 
    hide yuri
    _mc ef "We talked a bit while we were in class last year, but we never really sat down and became friends."
    _mc ec mh thinking "That just makes it all the more confusing as to why she would ask me to join her."
    hide monika
    _mc ea mf bb "Hey, I'm not complaining. She's been really welcoming. Maybe something I said last year struck a chord with her."
    _mc ldown ba ma eg "Either way, she's been really good to me so far. I don't want to mess that up."
    _mc ec mh "Which means working out how to talk to Sayori."
    show bg club_afternoon as stuff onlayer above_master:
        blur 2.0
    show sayori turned b2a e2b lup onlayer above_master:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    show white_flashback onlayer above_master
    camera above_master:
        align (0.5, 0.2) zoom 1.5
        flash(0.4)
    _mc ea "Properly. I mean, we barely talked yesterday. Just read together."
    _mc eb nc bb "Oh."
    $ clear_layers("above_master")
    with None
    show cg sayori 1
    show white_flashback
    with NonBlockingDissolve(1.0)
    "I feel my cheeks flush as I remember how close we got."
    _mc mf "I mean, we almost..."
    _mc eg bg nb mi "Man, that was close. I don't know what I would have done if I'd been put in that situation again."
    _mc ef bf na ma "Probably something stupid."
    hide cg
    hide white_flashback
    with NonBlockingDissolve(0.4)
    _mc mh "Yeah. Like last time."    
    show natsuki turned lhip e2a mg at t11
    n "You alright?"
    show natsuki 
    n ldown e1a b3a mh "You were staring. It's gonna make Sayori uncomfortable."
    show natsuki md with None
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    show natsuki cross b1a
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    "A small figure sits down next to me, pulling up a chair."
    show natsuki e3c with say_dissolve
    "She's almost uncomfortably close, considering she wasn't all that much of a fan of me yesterday."
    n e2a b1d mg "You're..."
    n b1a e1a mh "You're actually Melody, right?"
    n turned e2a b1d mc "I know that's a stupid thing to ask, but..."
    show natsuki ma with say_dissolve
    mc ea mb ba "Yeah, that's me."
    mc ml "I'm guessing Sayori's told you a bit about me, by now."
    mc ef mg "Well, whatever she's said..."
    n e1b b3a mi nb "N- No, all good things, I swear!"
    n e1a mh "Actually, she holds you in really high regard."
    n na mb b1a "It's kinda crazy, really."
    n cross b3a e3c mi "Like, she really respects you, which strikes me as weird."
    show natsuki mj with say_dissolve
    mc bm ea ml "How so?"
    n e1d b1d mg "Well, look at it this way."
    n turned e1a b3a mb "Imagine you have a friend." # not relatable
    n lhip e2a b1a mh "And this friend is really into gardening."
    n ldown b3a e3c mi "They say they used to garden a lot as a kid, and then just stopped one day, despite not having a reason to." 
    n e1a mh "Their garden still existed, they still walked past it every day, but..."
    n e1d b1d mg lhip rhip "They just didn't tend to it. And they still claim to be into gardening."
    show natsuki md with say_dissolve
    mc thinking ba ec ml "Hmm. You're right, that is a little strange."
    n cross mh "That's what it's like for me, seeing her talk about you. Because believe me, she's done it a lot."
    n e1a b3a mg "She's really a fan of you, you know."
    show natsuki md with say_dissolve
    mc ef mf ldown "I thought she wanted nothing to do with me."
    n mg "What gave you that impression?"
    show natsuki md with say_dissolve
    mc mg eg "I mean, she hasn't reached out to me in five years. That's a big one."
    n turned lhip mh "And did you try to talk to her?"
    show natsuki mj with say_dissolve
    mc bi ef mf "No..."
    n mb b1a "I rest my case."
    n cross e3c b3a mi "Now, go make yourself useful and talk to her, will you?"
    show natsuki e1a ma with say_dissolve
    mc bi mh "..."
    mc ba ea ml "What do I say?"
    n mg b1d e1d "Oh, don't be so stupid."
    n turned mh b3a e1a "Just be yourself. That's the reason you were such good friends in the first place."
    show natsuki ma with say_dissolve
    mc eb mf "..."
    show natsuki md with say_dissolve
    mc ec bi ml "How do you know all this?"
    show natsuki mb e1d
    n lhip b1a e2a mh "I'm her best friend. She tells me everything."
    show natsuki md with None
    hide natsuki
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    "Frowning, I stand up."
    _mc thinking ea bd mh "Something about this whole situation feels..."
    _mc ec mf bi "Off. But I can't quite put my finger on it as to why."
    _mc ldown ea ba mh "Maybe Sayori will have some answers."
    show bg:
        align (1.0, 0.6) zoom 1.8
    show sayori turned e2c me b1b at i44
    with Dissolve(0.2)
    "Standing up, I make my way over to the girl. She's staring out the window, looking a little lonely."
    _mc ec "No, lonely isn't the word."
    _mc ef "Lost."
    _mc eg "Yeah. That's it."
    show sayori me b2b 
    camera master:
        align (1.0, 0.2) zoom 1.4
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc ea mg "Hey, Sayori."
    mc mb "Do you mind if I sit down?"
    s e1a b1a md "..."
    camera master:
        zoom 1.0
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    mc ml "Alright, I'll come back when you're feeling-"
    $ autofocus.unblock("sayori")
    s ml b2a rup e1b lup "N- No wait, come back!"
    show sayori me b2b with None
    camera master:
        zoom 1.4
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    "Frantically, she flails her arms at me."
    $ autofocus.block("sayori")
    mc mg "But you look like you're thinking pretty hard about something, so I-"
    s mk rdown e2b b2c nb "Nonono, Iwasjustthinkingabooutyou-"
    s me "I,"
    extend e2c b2b mg " ah,"
    extend mb e2a b2a na ldown " mean..."
    s b1a e1b rup lup mc "Food!"
    s mb e3d ldown rdown "Yeah!"
    s e1a mb "I was thinking about what I was gonna have for dinner tonight!"
    show sayori ma with say_dissolve
    mc ml "Oh, right."
    mc mg bb "I mean, it doesn't take that much thought, does it?"
    s lup e2a b2a mb "N- No, not really..."
    show sayori ma with say_dissolve
    mc mb ba "But hey, if that's what makes you happy."
    show sayori e3d mn b1a with say_dissolve 
    _mc ec ma "Geez, she's as jumpy as ever."
    _mc ef "Better to not push her on what I know she said. I'll ask another time, perhaps."
    _mc nc "Honestly, if she's thinking about me, that makes me a little happy."
    mc ea mb na "Well, if you're that hungry, do you want a snack?"
    s mh e1a "I,"
    extend ldown e2a mg " ah..."
    show sayori me with say_dissolve
    "She seems to mull it over for a moment."
    s e1a mb "Sure, I would!"
    show sayori ma with say_dissolve
    mc md ed "Well, I'll run to the vending machine then."
    show sayori md with say_dissolve
    mc ea mg "Oh, actually, better idea."
    mc "Do ya wanna come with?"
    s lup mf lup rup e1b "Ooooo~"
    show sayori mb 
    s e3d ldown rdown mn "Yes please!"
    show sayori ma rup:
        i44
        easein 0.25 xoffset -1500
    camera master
    show bg:
        zoom 1.0 blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She stands and practically bounds toward the door."
    $ autofocus.unblock("sayori")
    show bg class_2_day
    hide sayori
    show monika turned rhip bc eb at i42
    with NonBlockingDissolve(0.4)
    "She waves to Monika as she does so, who smiles while rolling her eyes."
    m ba rdown mb ea"If you're going, grab me a coffee, would you please?"
    show monika ma 
    s turned e3d mb "Sure!"
    hide monika
    show natsuki turned b3a md at i43
    show bg club_closet_day
    with Dissolve(0.2) 
    n mh "Oh, and I'll take a protein bar!"
    show natsuki ma with None
    hide natsuki
    show yuri shy nb at i42
    show bg club_day:
        align (0.0, 0.8) zoom 1.9 
    with Dissolve(0.2)
    y bb eb "Uuuu..."
    "Yuri sinks deeper into her book."
    show yuri mc
    s e1a "I'll grab you a green tea, Yuri!"
    y ba ea "... Th- Thanks..."
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    show yuri na
    with Dissolve(0.2)
    $ say_transition = True
    "As I walk past, I flash Yuri a smile."
    $ autofocus.block("yuri")
    mc "Don't worry, it's on us."
    show yuri turned ldown e3c b1a ma with say_dissolve
    "She simply nods and buries herself into the novel."
    show yuri e2a b1d md with say_dissolve
    _mc thinking mh ec "Hmm. Odd book she's got, actually."
    _mc ma ea "It looks like a Poe story, but..."
    _mc ec mh "No, actually, it's not. It's far more recent."
    show yuri ma nb with say_dissolve
    _mc ea ma "The Turn of the Screw. That's a Henry James novel."
    _mc eh "A really good one, too, from memory."
    _mc ldown ea "I might have to ask her to borrow it when she's done."
    s mh "You coming?"
    mc mg "Oh, yeah!"
    show yuri e1a b1a na with say_dissolve
    mc md bf eh nb "Sorry for staring, Yuri, I was just looking at the book you've got."
    y e2c mh "Ooh, it's... alright, I was just..."
    show yuri md with say_dissolve
    mc na ml ea ba "If you don't mind, could I borrow it when you're done?"
    y lup rup e1b ml nb "Y- Yes! I- I mean..."
    show yuri na e3c 
    y e2b b2b rdown mb "Sure, I don't mind..."
    show yuri ma with None
    hide yuri
    show bg:
        blur 0.0 zoom 1.0
    camera master
    with Dissolve(0.2) 
    $ autofocus.unblock("yuri")
    $ say_transition = False
    "I wave as I make my exit."
    _mc ef ma "She seems really nice, though a little shy."
    _mc ea mh "I wonder what she's like when you get her to open up?"
    show sayori e1b b1d mj at t31
    _mc ec ma "No use thinking about it now - Sayori looks like she's about to explode."
    mc md ed "I'm coming, hold your horses~"
    show sayori rup at t11
    "She grabs me by the wrist before I even make it to the door, dragging me along behind her."
    show black with NonBlockingDissolve(0.5)
    "For the next few moments, I don't think I could wipe the grin from my face if I tried."

    scene bg school_vending_machine_day
    show sayori turned e2a b1b md at i11 
    with wipeleft
    
    s me "Oooooo, what to get?"
    show sayori md 
    mc turned tail nostrands thinking ec bi ml "Good question."
    show sayori b1a e1a
    mc ea ba mg "What do you feel like?"
    s mb lup "Hmm. Best to start with what the others want, then decide."
    show sayori ma 
    mc mb ldown "That's a good idea, so we have time to think about it."
    hide sayori 
    show bg:
        align (0.97, 0.42) zoom 3.3
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "Pressing the buttons, I pick a can of green tea."
    mc ml ec "Hmm. What coffee would Monika like?"
    show bg:
        align (0.9, 0.41) zoom 2.5
    show sayori turned rup e3d:
        xcenter 0.61 ypos 1.0 yanchor 0.8
        matrixanchor (0.5, 0.4) matrixtransform RotateMatrix(0, 0, 5) yoffset -6
    with Dissolve(0.2)
    "Musing to myself, I watch Sayori gleefully press another button, as a very specific bar falls into her waiting hand."
    show sayori:
        xoffset 30 matrixtransform None
    show bg:
        blur 1.0 xoffset 10
    s rdown mn "Ehe!"
    show sayori ma with say_dissolve
    mc ea mg "Oh, now that's interesting. I wouldn't have guessed Natsuki to be a fan of the yogurt bars. I thought she would have wanted chocolate or strawberry."
    s e1a mh "Oh, she does."
    show sayori ma with say_dissolve
    mc eb mf "Then why-"
    s e1d b1d mb "Ehe~ You'll see."
    show sayori ma with None
    show sayori rup e3c:
        xoffset 0 xcenter 0.67 matrixtransform RotateMatrix(0, 0, 5)
    show bg:
        blur 0.0 xoffset 0
    with Dissolve(0.2)
    "She then presses another button, and a chocolate protein bar falls."
    "No, she wouldn't."
    "Oh, that devilish smile gives it all away."
    show bg:
        blur 1.0 xoffset 10
    show sayori rdown:
        xoffset 30 matrixtransform None
    with say_dissolve
    mc bd ed md "That's mean, Sayori."
    s mn b1a e3d "I know~"
    hide sayori
    show sayori turned e3d at i11
    hide bg
    show bg school_corridor_3_day
    with Dissolve(0.2)
    $ say_transition = False
    "Smugly, she starts walking back."
    mc ea mg ba "Wait, what about Monika's coffee?"
    $ autofocus.unblock("sayori")
    s mb "Pick something! She might like it regardless!"
    show sayori ma 
    mc bi mm eg "Argh, Sayori..."
    hide sayori
    show bg school_vending_machine_day
    with wipeleft
    "Turning back to the machine, I consider my options."
    show bg:
        align (0.97, 0.42) zoom 3.3
    with Dissolve(0.2)
    _mc ec ba mh "I could get one with milk. That would be sensible."
    _mc ea "But then again..."
    _mc mf eb bb "Oh, this must be a test, to see how well I know Monika."
    "..."
    _mc ec ba mh "Wait, I think I have it."
    _mc ea ma "Yeah. It's a bit of a gamble, but..."
    show bg:
        zoom 1.0
    with Dissolve(0.2)
    _mc eh "This should be right."
    "Can in hand, I make my way back."
    
    scene black with wipeleft
    pause 0.5
    show bg school_corridor_3_day
    hide black
    window auto show None

    _mc turned tail nostrands mg nb eb bb "Wait, I didn't get something for me!"
    _mc ba eg ml "... Ah, it's fine. I've got food at home to eat later."
    _mc ma ec "It saves me a little money, anyway."
   
    scene bg class_2_day
    show monika turned mc bc at i11
    with wipeleft_scene
    $ autofocus.block("monika")

    m "..."
    $ autofocus.unblock("monika")
    m rhip ec "Hmm."
    mc turned tail nostrands ml nb "S- Sorry, I-"
    show monika ea md
    m "Sayori."
    show monika mc at t21
    show sayori turned lup mh at t22 
    s "Huh?"
    show sayori md
    m rdown ba md "Did you tell her to get this one?"
    show monika mc
    s ldown mg "No, I didn't."
    show sayori me
    $ autofocus.block("monika")
    m "..."
    $ autofocus.unblock("monika")
    m eb md "I see."
    show sayori md at thide zorder 1
    hide sayori
    show monika ea mb at t11
    m "It seems you do remember."
    show monika mc
    mc ml "Remember what?"
    show monika bc
    "She shoots me a narrow look."
    m md "So, you just guessed that I would like straight, black coffee?"
    show monika mc
    mc eb mg bb "Well, n- no, it was an educated-"
    show monika eb at thide
    hide monika
    "She clicks her tongue, then sits back down."
    _mc mf ba na "Did I do something wrong here? I got what she wanted, right?"
    _mc ec mh thinking "I get the feeling she wants me to be more confident around her, but I'm not sure why."
    _mc ea ma "Ah, it's fine for now. She seems happy, considering she's already downed half of it."
    _mc ec mh "Now to-"
    stop music fadeout 3.0
    n turned b1d mi "Sayori. What the hell is this?"
    
    scene bg club_day with wipeleft:
        align (1.0, 0.5) zoom 1.0
        easeout_quad 4.0 zoom 2.0
    pause 0.1
    scene bg club_closet_day
    show sayori turned md rup at i21
    show natsuki cross e1d mm at i22
    with Dissolve(0.4)

    s mb "It's a protein bar, like you asked."
    show sayori ma
    n mi e1b b1a "It's one of those gross yogurt ones, you numpty!"
    show natsuki mm
    s e1a mb b2a "Yeah, but it's-"
    show sayori md b2b
    n e2a mg b1d "Ugh, it's fine."
    n turned b3a mi e3c "I'm sorry, I didn't mean to raise my voice."
    show natsuki md
    s mb b1a "N- no, it's alright, I actually-"
    show sayori md rdown
    show natsuki lhip e3d me at hop
    "Before Sayori can finish her explanation of her small prank, Natsuki's already opened the bar, and taken a bite out of it."
    show natsuki e2a b1a md
    s e2a mk b2b "... Uuuu..."
    show sayori md
    n b4 e1a mg "What?"
    show natsuki md
    s me "I'm sorry, it was..."
    show sayori md e1a
    n mh b3a ldown "It's not a big deal, I just overreacted."
    show sayori mj e1b
    n b2a mg "I'm sorry; don't get upset, okay?"
    show natsuki md
    s b2b me lup "N- No, you..."
    show sayori ml xd rup b2c nb at hop
    show natsuki me b1a
    s "You ruined my joke!"
    show sayori mk
    n mg "Your-"
    show sayori md
    n me "..."
    "Natsuki stares blankly at the girl for a moment."
    n mg b1d "You..."

    play music daijoubu

    n lhip rhip mh e1d "What do you mean, joke?"
    show natsuki mj
    s e1a mg na b1a rdown ldown "I..."
    show sayori ma e2a b2a lup
    show natsuki md b1a e1a
    "She pulls from her pocket, another bar."
    "This one is coated in chocolate."
    $ autofocus.block("natsuki")
    n me "..."
    $ autofocus.unblock("natsuki")
    n ldown rdown mb b1d e3c "I should have known."
    n mi b3a "Here I was trying to be nice to you..."
    n lhip b1a mb e2a "Ah, it's alright. I've already started this one. You can have the chocolate one."
    show natsuki ma
    s mg e1a tears_a "B- But I don't deserve it, now..."
    show sayori md e3c b2b
    show natsuki e1a md
    "Sayori sniffles a little."
    "Clearly this whole thing didn't go her way."
    n b3a mh ldown "No, it's fine. If you don't want it, Melody can have it."
    show sayori ldown
    show natsuki ma b1a at dip
    "She takes the bar from Sayori, placing it into my hand."
    _mc turned tail nostrands ec "I guess I'll just ignore the fact that she called me Melody, shall I?"
    n cross mb e2a b1d "See? No need to cry, geez."
    show natsuki ma 
    $ autofocus.block("sayori")
    s e2a "..."
    show natsuki md e1a b1a
    $ autofocus.unblock("sayori")
    s me "B- But I'm still hungry..."
    show sayori md
    n turned e3c b3a mi "Oh, my god, fine."
    show natsuki e2a md b1a at dip
    show sayori rup e1a b1a me
    "She takes her bar, breaks it in half, and gives the untouched side to Sayori."
    n e1a mb "Here you go."
    show natsuki ma
    s mb e2a b2a "Th- Thank you..."
    show sayori e3d notears lup me b1a
    "Sayori wipes her eyes with her free hand."
    s b2c e1a mb ldown "I'm sorry, I didn't mean to..."
    show sayori mj
    n b3a mh "Hey, no need to get all emotional, you know?"
    n cross e2a b1d mb "I'm sorry for not playing along, honestly."
    show natsuki ma
    show sayori b1a me
    mc ea mb "Hey, Sayori, here."
    "I break open my bar, and hand her half."
    _mc ef ma "There's no way she'd accept the full bar, so this might be enough."
    s e2a b2b mg "Mmm... Thanks..."
    show sayori md ldown 
    "She eats the bar, and keeps her gaze firmly planted at her feet."
    mc ea mb "C'mon, let's do some reading. That should cheer you up, yeah?"
    show natsuki ma b1a
    s mg e3c "... Yeah."
    show sayori me
    
    scene bg club_day with wipeleft
    show bg:
        blur 2.0 align (1.0, 0.6) zoom 1.8
    camera master:
        align (1.0, 0.2) zoom 1.4
    show sayori turned lup b2c me at i44
    with Dissolve(0.2)

    "I lead her over to her spot, and sit down, pulling her seat out as I do."
    show sayori md
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    s ldown e2a mb "A- Actually, I... I gotta..."
    s e1a b1a mh "I'm gonna go to the bathroom first."
    show sayori ma
    "Her mood seems to clean up pretty quickly, but something tells me it's not so genuine."
    show sayori md
    show natsuki turned mg at t43
    n "I'll come with you-"
    show natsuki md
    s mh "No, it's fine."
    s e2a lup mb "It's only down the hall."
    show sayori ma ldown at lhide zorder 1
    hide sayori
    "She leaves pretty quickly after that."
    show natsuki e2a at thide
    hide natsuki
    _mc turned tail nostrands thinking ec mh "Huh. Weird."
    _mc ea "I thought I was gonna read today, but..."
    _mc ef ma "This just gets stranger. Must be Sayori's influence, every day was strange and fun with her around."
    _mc eg ldown "I'm sure it'll get better though, as I get more used to it."
    _mc ec "It's Sayori. She can't have changed all that much, right?"

    scene bg residential_afternoon 
    show sayori turned lup e1b b1d:
        matrixcolor TintMatrix("#ffeede")
        i11
    with fade
    $ set_date(hour=16, minute=52)

    s ldown mi "And then, when the big guy came over, Natsuki stood up and was like, 'If you don't leave us alone, I'm gonna make you wish you had!'" 
    s mk b2b "With one of those really dark and gruff voices. It was like nothing I'd ever seen before."
    s e1a b1a mh "And then, the craziest thing happened. He did."
    s lup e1b mi "He was like, three... No four times her size, and he just up and walked away!"
    s ldown e2a mb b2a "I dunno, but sometimes, she might be a little scary like that."
    show sayori ma
    mc turned tail nostrands ed md "No bet."
    mc ea mg "She strikes me as having a lot more going on, right?"
    s e1a mh b1a "Oh, she does. She sometimes leaves for days on end, and re-appears like nothing was any different."
    s e2a b1d lup mb "Sometimes, I wonder if she isn't secretly a spy."
    s mh e1a b1a "Or a super-soldier."
    show sayori rup mb e1b at hop
    s "Or a robot."
    show sayori md e1a
    mc ec ml "Alright, alright, that's no way to talk about your friend."
    s ldown rdown mn e3d "But she's not just my friend, she's my beeest friend! I gotta-"
    s e2a mb "..."
    show sayori b2a e1a ma
    "She glances my way."
    s mb "I, I mean, like, she's good, but-"
    show sayori mj
    mc bf ef mb nb "No, I get it."
    mc bg ml na "I totally do. It's been so long since we've hung out, that..."
    s e2a b2b mg "Yeah, but I don't want you to-"
    show sayori md
    mc eg mb "No, trust me, it's alright."
    show sayori e1a b2a ma
    mc ba ef ml "It'll take some getting used to again, I reckon."
    show sayori b1a me
    mc ea mb "Which is why, I would like to propose."
    s mg b2b "Propose?"
    s b2a e1b lup nb mh "What, to me?"
    show sayori me
    mc ml "Yes."
    s ldown e2a mb nd "O- Oh..."
    show sayori me
    "Hyping myself up for the big moment, it takes me a second to realise I stopped mid-explanation."
    mc eb mf "Wait, that..."
    show sayori e1b b2c nb mk at hop
    mc nb bb mg nb "That came out wrong!"
    s b1a lup mh e1a "D- Did it?"
    show sayori me
    "Sayori jumps back a little from my sudden outburst."
    mc mg ea ba "Y- Yeah, I didn't mean propose, like, marriage or anything! Like, I had an idea!"
    s ldown b1a e2a mb "O- Ohh, I get it..."
    s e1a mh na "So..."
    show sayori md 
    _mc ef bd mh "Man, it's weird, but I feel a little disappointed."
    show sayori b1a
    mc eb mg na bb "Ah, right! My idea!"
    show sayori ma
    mc ea mb ba "How about the two of us start walking to school again?"
    s mg lup "What, together?"
    show sayori md
    mc ml "Yeah, obviously."
    s b2a e2a mb "But then..."
    s mg ldown "If we did, wouldn't people start to get the impression that you..."
    show sayori b1a mb e1a
    extend " proposed... the idea?"
    show sayori e3d mn b1d
    mc ed md "Oh, shut up..."
    "I wave her off, feeling myself flush with crimson."
    mc mb eg "Sure sure, have your fun."
    s b1a mb "I will. And there's plenty more where that came from."
    show sayori ma
    mc ed md "I'll bet."
    s e1d b1d rup mb "Just you wait, I'm gonna rock your socks off."
    show sayori lup e3d b1a mc at hop
    s "I'll pull the most crazy prank before the end of the week, just you wait!"
    show sayori ma 
    mc ed md "Not if I get you first!"
    show black
    hide sayori
    with NonBlockingDissolve(1.0)
    "We keep walking, bantering to each-other, describing possible prank ideas, and just chatting."
    _mc ef ma "It's..."
    _mc bg "Been so long since we've had a chance to do this sort of thing."
    "God, I've missed it."
    s turned mg "What? You went quiet all of a sudden."
    hide black
    show sayori turned md:
        i11
        matrixcolor TintMatrix("#ffeede")
    with NonBlockingDissolve(0.3)
    mc ea bf mb "Yeah."
    s mg "Oh, I get it."
    s b2a mb "I've missed you too."
    show sayori ma with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "I look at her, a small smile on my face."
    s mb b1a "I can still read your mind, you know."
    show sayori ma with say_dissolve
    mc ed ba md "Hah, that wouldn't surprise me."
    mc ea ml "Alright, what am I thinking of... right now?"
    s e3c mj b1d "Hmm..."
    show sayori rup with say_dissolve
    "She holds her pointer fingers to her temples and looks at me, staring into my soul."
    "At least, that's what it looks like she's doing."
    s b3d mm nb "Hgggggggggg..."
    s rdown e1b b1a mb na "Alright!"
    show sayori ma with say_dissolve
    "I can practically see the light-bulb above her head."
    s mb "You're thinking..."
    s e1d b1d mh "About how to not get me to discover that you don't have any food at home, and was gonna get pizza!"
    s lup e1b b2b mg "Wait, don't do that!"
    s mb e1a b1a "I'll cook something for you!"
    show sayori ldown ma with say_dissolve
    mc ec bi ml "Wait, rewind though. How the hell could you have known that?"
    s mb "I just told you, I'm psychic!"
    show sayori md with say_dissolve
    mc eg ba mg "... You win. I'll be sensible and make myself something."
    s mg "You sure you don't want me to cook?"
    show sayori md with say_dissolve
    mc ea ml "Nah, wouldn't want to trouble you."
    s lup mb "It's no trouble! I'll bring something around a little later, alright?"
    show sayori md with say_dissolve
    mc eb bb mg "No, really, it's fine. I can cook for myself."
    s ldown "..."
    s b2a e2a mh "Alright then."
    show sayori me with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "The shift in her mood causes me to pause."
    mc bf mg ea "Hey, no, if you really want to cook-"
    $ autofocus.unblock("sayori")
    s e1a mb "No, I don't want to be a bother..."
    show sayori mj
    mc ef ml bg "No, it isn't like that. I just don't want you to go out of your way for me, is all."
    s b2a e1a mg "But sometimes..."
    show sayori md
    mc mb "... Yeah."
    mc ea mg ba "Alright, tell you what."
    show sayori b1a
    mc mb "Let's go out to the park on our way home, and decide what we want to eat."
    s mh b1a "Really?"
    show sayori ma
    mc ed md "Yeah, like old times."
    s mb e3d rup lup "Ooo, except we get to do the cooking!"
    show sayori ma
    mc ed md "And we don't have to list off fifteen things before we get to one that one of our parents willing to cook!"
    s mc "Yeah!"
    show sayori ma
    "Grinning ear to ear, the two of us bound off to the park."

    scene bg park_afternoon
    show sayori turned me:
        matrixcolor TintMatrix("#ffeede")
        i11
    with wipeleft_scene
    camera master:
        align (0.5, 0.2) zoom 1.5
    show sayori e1b
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ advance_date(minutes=20)
    $ autofocus.block("sayori")
    $ say_transition = True

    s mh "Woah, this place has changed!"
    show sayori me with None
    show sayori:
        alpha 0.0
    show bg:
        blur 0.0
    camera master:
        align (0.0, 0.57) zoom 2.6
    with Dissolve(0.2)
    mc turned tail nostrands mg "Yeah, that entire structure is new."
    show sayori e1a md
    mc ed md "I wonder if they tore down the old one after you broke it."
    show bg:
        blur 2.0
    show sayori tap bc ea ma:
        alpha 1.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    s md "Hey, I didn't break it, I simply bent it!"
    show sayori ma with say_dissolve
    mc eg mg bb "Sure sure, but the hinge looked pretty broken to me."
    mc ba ed md "That's what you get for planking on it."
    s mb eb bb nb "Ehe~"
    s turned lup e2a mb b2a "Not my smartest moment, but..."
    show sayori ma with say_dissolve
    mc mb eg "It sure was fun."
    s e3d b1a na ldown "Yeah!"
    show sayori ma e1a with say_dissolve
    mc ea mg "So, what's our plan?"
    s e1d b1d mb "Oh, I think you know exactly what our plan is."
    show sayori ma lup rup with Dissolve(0.05)
    show sayori ldown rdown:
        yoffset 50
    camera master:
        zoom 1.4
    show bg:
        blur 1.7
    with Dissolve(0.2)
    "Without missing a beat, she claps her hands together, then slams them both on the ground in front of her."
    camera master
    show bg:
        blur 0.0
    show sayori:
        yoffset 0
    with Dissolve(0.16)
    $ say_transition = False
    "Acting on impulse alone, I leap backward."
    $ autofocus.unblock("sayori")
    s lup b1a e1a mb "See, you still got it!"
    show sayori mn e1d b1d
    mc ed md "Oh, you've seen nothing yet!"
    "I clap my own hands, this time touching my arm."
    mc ec "Take..."
    show sayori ldown
    extend eb mb " this!"
    camera master:
        align (0.5, 0.3) zoom 1.8
    show sayori b1a nb ml e1b
    show bg:
        blur 2.5
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "And charge her, arm raised like a sword."
    s lup rup xd b2a mk "Ooof!"
    play sound ["<silence 0.1>", audio.fall]
    camera master
    hide sayori
    show bg:
        blur 0.0 align (0.4, 1.0) zoom 4.0
    with Wipe(0.2, theta=0)
    $ say_transition = False
    "Sayori drops to her hands and knees, with me following suit shortly afterwards."
    mc bg eh md "Man, we haven't done that in years!"
    s turned e1b b1a nb mc lup rup "I know! That was crazy! It was like we knew each-other's moves before we even made them!"
    mc mb eg ba "Evenly matched, as always."
    mc ea ml "I guess we'll never know."
    show bg:
        align (0.1, 0.9) zoom 2.0
    show sayori ldown rdown ma na e1a:
        matrixcolor TintMatrix("#ffeede")
        zoom 2.0 ypos 1.0 yanchor 1.0 xcenter 0.5
    with Dissolve(0.2)
    "Smiling, I look back at her."
    show black with NonBlockingDissolve(0.2)
    _mc mf bb "Oh."
    _mc bi mh ec "Wait, hold on-"
    _mc ea mf ba "I can..."
    $ autofocus.unblock("sayori")
    _mc bb eb nb "I can see down her shirt."
    _mc mf "This angle..."
    _mc bi eg mm "No! Nononono, stop that!"
    show sayori rup at i11
    show bg:
        zoom 1.0
    hide black
    with Dissolve(0.2)
    "Shaking my head, I push those impure thoughts from my mind, and stand back up, offering Sayori a hand."
    s rdown mb "That was pretty great, right?"
    show sayori ma
    mc ea mb na ba "Yeah, it sure was."
    s mh "So, where to next?"
    show sayori md
    mc mg "I mean, we don't have to leave yet."
    s e1b mh "Oho, you wanna try the slide?"
    show sayori md
    mc ed md "Nah, we'd just get stuck, I reckon."
    show sayori e1a 
    mc ea mg "But we could always try the see-saw?"
    s e1d b1b lup mh "Do you really want to try that again, after last time?"
    show sayori md 
    mc mf "Oh, wait, no..."
    show sayori e1a b1a ma
    mc ef mb "On second thought, let's not."
    s mb e2a ldown "Hehe, thought so."
    show sayori ma 
    "I wince a little as I feel the pain in my butt like it was only yesterday."
    "She bounced so hard it caused some major bruising for weeks."
    _mc ma "All part of her prank, I'm sure."
    _mc eg bg "Unfortunately, I couldn't sit down for a week afterward. Sleeping was almost impossible."
    _mc mh "Right before our exams, too."
    _mc ea ba "She did feel really bad, though."
    _mc ec "She tried nursing me as best she could."
    _mc eb mf "It was, ah..."
    show sayori e1a md
    _mc ma nb ef "A little weird having her hovering around my..."
    _mc eb bb mh "Woah, bad!"
    show sayori nb
    _mc eg bi "Stop with those thoughts! We just talked about this!"
    s mh "You're..."
    s na e1d b1d mi "Thinking something... inappropriate, aren't you?"
    show sayori mj
    mc eb mg bb "N- No, not at all!"
    _mc mh "Oh, shoot, this is bad."
    _mc ec bi "Gotta change the subject."
    mc ea mf "I was thinking about..."
    show sayori e1a b1a md
    mc na bc mb eb "Oh! About how good the weather is!"
    mc eh ba ma "Yeah, it's really nice!"
    $ autofocus.block("sayori")
    s "..."
    $ autofocus.unblock("sayori")
    s mg e2a "Right."
    s mh e1a "I mean, it isn't bad. Just... not fantastic, either."
    show sayori md
    mc ea mb "At least it isn't raining, right?"
    s mg "Uh-huh."
    s mh "Look, there's-"
    show sayori me
    mc mg "Oh, look at that cloud!"
    show sayori e1b md
    mc mb "It's shaped like a face!"
    show sayori lup b1d mh:
        xzoom -1
        0.18
        xzoom 1
        0.18
        repeat
    s "Oh? Where?"
    play sound ["<silence 0.4>", audio.fall]
    play sound2 ["<silence 0.75>", audio.fall]
    show sky_afternoon at moving_sky zorder 5
    show sayori ldown e1a ma b1a:
        xzoom 1.0
    with NonBlockingTransition(fade)
    "Before I know it, the two of us have fallen backward into the sand, and are gazing up at the sky."
    hide sayori
    $ autofocus.block("sayori")
    s turned lup mc e1b "And that one looks like an apple!"
    mc ed md "Hah, I would have said a ball, but sure. Are you that hungry?"
    s e3d mn ldown "Ehe~"
    mc mg ea "The big long streak from those jets is always cool to see, too. It really stands out."
    s e1a mh "Especially when you can see them move behind the clouds."
    mc ml "True, it sort of looks like the cloud is making them."
    mc mb "Like they're being propelled far across the sky, on jets of their own."
    s mg "But, I mean they kinda are."
    s mb "In the sky, they're moved by the high winds, and clouds are always moving pretty fast. They're just so far away that it looks slow. Like how in a car, things that are further away take longer to move."
    mc ml "I mean, yeah, but-"
    s e2a mh "Or when you're looking down from a plane, you can see the ground before you pass the clouds." 
    s e1a mb "And how it moves slowly, despite how quickly the plane is moving. It's really cool to see."
    mc ec ml "Have you been in a plane recently?"
    s nb mg e2a bags b1b "Y- Yeah, I was..."
    s mh na b1a nobags "I went to America a few months ago. It wasn't for very long though."
    mc ea mg "Oh? I don't remember you taking time off of school."
    s md "..."
    s mg "No, I didn't."
    s e1a mh "It was during the break."
    mc thinking ml ec "Oh, between the school year? That was a while ago, right?"
    s e3c b1b me "Mm."
    mc ldown mg ea "Did you do much sight-seeing? It's a long way to go for not much time."
    s e2a mg "No, I didn't... really get the chance."
    mc ec ml "Ah, that's a shame."
    mc ea mb "Maybe we can go back there after we graduate?"
    s mb b2a "Y- Yeah, that would be... nice."
    mc mf "Hey, Sayori..."
    mc bf ml "I don't mean to pry, but is something wrong?"
    s e2c b1b me "No, not... not really, I just don't feel super well."
    show sayori turned md rup b1a e1a:
        i11
        matrixcolor TintMatrix("#ffeede")
    hide sky_afternoon
    with Dissolve(0.2)
    "She moves to sit up, and I gently clasp her hand."
    mc mb "Hey, you don't have to tell me, it's fine."
    show sayori b2b
    mc bg ml "I'm sorry for asking."
    mc mb ba "But if you do need anything, I'm here, alright?"
    $ autofocus.unblock("sayori")
    s nb mb e3d "Yeah."
    show sayori e1a ma 
    "She looks back down at me, a weak smile on her face."
    s mh na e3c "Thank you."
    s mg e2a b2c "It's not... I don't wanna ruin the mood with my problems, you know?"
    show sayori ma 
    mc bf ed ml "Hey, it's cool."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("sayori")
    "I sit up to join her."
    show sayori me e1a b2a with say_dissolve
    mc mg ba ea "We have time now, if you wanna talk about it."
    s b1b e2a mg "I mean, not really..."
    show sayori b1a md e1a with say_dissolve
    mc ml "Cool. In that case, let's change the subject."
    mc mb "Did you wanna go grab a bite to eat? It'll start getting dark soon."
    s mb "Ah, yeah. That'd be nice."
    show sayori ma with None
    show sayori e3d
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "We stand, and it occurs to me that she's still holding my hand."
    $ autofocus.unblock("sayori")
    s e2a b2a mb "I do really appreciate it. You... just being here. And knowing."
    show sayori ma
    mc ed md "Well, I know you better than anyone, right?"
    show sayori b1d e1d md
    mc eh bb mb "I don't think there's a single thing you could do to surprise me."
    s mb "Hah, I suppose that's a challenge?"
    show sayori mn
    mc ba ed md "It sure is."
    show sayori e3d ma
    "Finally, she starts smiling again."
    show black with NonBlockingDissolve(0.4)
    "The two of us make our way down the street, with Sayori reluctantly letting go of my hand as we leave the park."
    _mc ef ma "A part of me wants to grab it again, but..."
    _mc mh bg eg "She needs time to sort out whatever's bothering her. I don't want to..."
    _mc ef "Add more pressure."
    "Instead, we walk in peaceful silence toward the centre of town."

    stop music fadeout 2.0
    scene bg mc_kitchen_day with longfade
    $ set_internet(True)
    $ set_date(hour=19, minute=27)

    _mc turned tail nostrands bg eg mj "Home at last."
    _mc bb mg "Man, that was a long day."
    _mc ea ma "Oh, but it was a good one."
    _mc ec ba "I haven't had the chance to hang with Sayori like that for years. It was..."
    _mc ef "Just pure bliss."
    _mc md eg bi "I still can't wipe this stupid grin off of my face."
    "Now I'm just throwing something together for dinner, at least, before I do some study."
    _mc ec ma ba "It'll be a lot of fun going to school tomorrow."
    show bg residential_day as stuff at flash
    _mc ea mf "School..."
    _mc mg bb nb eb "Oh, shoot! I totally forgot to ask if she wanted to walk with me!"
    _mc mh ba "I better do that now, before I forget again."

    play ambient ext_night fadein 2.0
    scene bg s_house_night_on with Dissolve(0.5)
    $ advance_date(minutes=3)
    play sound door_knock

    s turned mi "Coming!"
    pause 0.7
    show sayori ma:
        matrixcolor TintMatrix("#6065b1")
        t11
    pause 0.2
    s mb "Oh, I had a feeling it was you. I was meaning to ask the same thing."
    show sayori ma
    mc turned tail nostrands eb mf "Huh? You were?"
    s mb b1a "Yeah!"
    s mh e3c "Sure, I'll walk to school with you tomorrow." 
    s mb e2a b2a "I was planning on asking myself, honestly, but we just got so distracted by everything that it was hard to find the time."
    show sayori ma
    mc ml ea "Oh, yeah."
    mc eb mg "Wait, you-"
    s lup mb e3a b1a "Ehe~ Trade secret! You'll never know."
    show sayori ma
    mc md ed "Alright then, keep your secrets. One day I'll find out how you read my mind."
    s mn e3d ldown "No, you won't~"
    show sayori at thide
    hide sayori

    "She grins at me, closing the door behind her."
    "That girl, I might never understand her. But in the same way, I feel like I know everything."

    scene sky_night at moving_sky
    show sky_stars
    with Dissolve(2.5)
    pause 1.5

    mc turned tail nostrands eb bb nb mg "Oh, shoot, my pasta!"

    $ add_calendar_description(calendar_descriptions["sayori"][0])
    
    call week_1_thursday_sayori from _call_week_1_thursday_sayori
    return