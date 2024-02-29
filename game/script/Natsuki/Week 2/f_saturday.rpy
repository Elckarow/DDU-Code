label week_2_saturday_natsuki:
    call calendar_transition(day=4, hour=15, minute=9) from _call_calendar_transition_23
    scene bg cafe_inside_day with dissolve_scene_full
    play music cafe

    "In between customers, I try to catch my breath."
    _mc turned apron casual ec nb "I’m glad I got some solid sleep last night; it made a hell of a difference."
    _mc ea "The café is packed today; I’ve got people coming out of my ears."
    _mc eg bg "Just making the coffee is running me ragged."
    show boss turned bb me at t11
    b "Yer doin’ alright there, kid?"
    show boss ma ba
    mc eh md ba "Better than ever!"
    b ed mc "Aha, that’s the spirit!"
    show boss at thide
    hide boss
    "He calls from the kitchen, as he prepares a fresh batch of muffins from the oven."
    "... In between several orders from customers."
    _mc ec mh ba "Honestly, sometimes I feel this place gets too busy for just two people on a Saturday."
    _mc ea "But you can’t just make an employee out of thin air, that would be-"
    _mc mf "Amelia?"

    #[Full Voice Acting]
    show amelia turned casual eb mb at t11
    am "Oh, hey Melody! I had a feeling you were working today."
    show amelia ma
    mc mg ea "Hi, sorry, can’t talk, I’m a little busy."
    am ea mb "I can see that, yeah. Anything I can help with?"
    show amelia ma
    mc ml ec "Not unless you want to become an employee..."
    am lup ed me "Nah, I’m too good at my day job for that."
    am eb mb "Maybe I can at least help the customers line up a little better, take their stress off?"
    am ec ldown "Besides, I’ve just the thing for it."
    show amelia ea ma
    mc bd ea mf "Huh?"
    show amelia eb at thide
    hide amelia
    show sayori turned hoodie at t11
    "As if on cue, Sayori walks into the building."
    show sayori lup rup e3d mc at hop
    s "Heyyy~"
    s rdown e1b ml nb "Woah, that’s a lot of people!"
    show sayori mk
    mc eb bg mg "And it just..."
    _mc mh "Keeps multiplying..."
    show sayori me e1a
    mc mg ba ea "Why are you all here? I appreciate the thought, but I really need to get work done."
    s ldown mb na "I’ve got this!"
    s lup mc e3d "Everyone who is waiting to order, or is waiting for their order, I have a solution!"
    show sayori ma
    "Her voice cuts through the bustle of the café, and suddenly, all is hushed."
    s ldown mb "I know it isn’t much, but please be patient. In return, I will sing you all a song."
    stop music fadeout 2.0
    show sayori ma at thide
    hide sayori
    show boss turned bb md at t11
    "Even the boss pokes his head around the corner, carrying a tray of croissants."
    b me "Hey, kid, what’s with the silence-"
    show boss ba md at thide
    hide boss
    "And suddenly, she begins to sing."
    show black with NonBlockingDissolve(1.0):
        alpha 0.6
    
    play music myfeelings
    
    _mc mh na ba ec "Sayori? I haven’t heard her sing... at least, not truly sing, since we were kids."
    _mc ma "... Ever since that one time someone said her voice was terrible."
    _mc bi eg "Hah, then I told him his nose was terrible, and broke it."
    _mc ec ba "... Worth being grounded for a month."
    _mc ea mh "It’s..."
    hide black with NonBlockingDissolve(0.7)
    _mc eg bg ma "I’m so glad that I have the chance to hear it again."
    show amelia turned casual ed mb at t11
    am "She’s like... really good. I had no idea."
    show amelia ma
    mc ba mb "Yeah, I know. She swore off singing a long, long time ago."
    mc ea mg "I’m amazed she’s built the courage back up."
    show amelia eb md
    mc ef ml "... In the time I’ve been away, so much has changed."
    am me "Wish things were different?"
    show amelia md
    mc mf "... No, not as such."
    mc ea mg "I just wish I’d made smarter choices."
    show amelia ea ma
    mc eg mb "That I’d done right by her."
    am ed me "I know the feeling. Sometimes, I wonder what life would have been like if I’d made different choices."
    show amelia ec ma at thide
    hide amelia
    show boss turned me at t11
    b "But life isn’t like that. Yer’ve not got a reset switch."
    b eb bb "All yer can do, is..."
    b ba ec mb "Keep moving forward."
    b ea lup me "It ain’t about getting no high score, but about how content yer feel at the end of it."
    show boss md
    mc ea mg "And you? How do you feel?"
    b ldown ed mc "Ohoho, I’ve still got a couple years left in me yet, kid."
    b eb mb "Though, one can never really tell."
    b ea "At the very least, this place, my baby, is in safe hands when I go."
    show boss ma with None
    show boss rup
    camera master:
        align (0.5, 0.0) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("boss")
    $ say_transition = True
    "He places a hand on my shoulder."
    b mb "And I’m proud of that fact."
    b ec "Just like I’m proud of you, Mel."
    show boss ma with say_dissolve
    mc ml ef "... Thank you."
    hide boss
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ autofocus.unblock("boss")
    $ say_transition = False
    #[End Voice Acting]
    "We return to our work, now with a renewed sense of purpose."

    stop music fadeout 2.0
    scene bg cafe_inside_afternoon with wipeleft_scene
    $ set_date(hour=16, minute=20)
    show boss turned md bb:
        matrixcolor TintMatrix("#f5e2bb")
        t11

    "After the end of my shift, the boss calls me over."
    b me "Hey, kid. That was..."
    b ba "Sayori, right?"
    show boss md 
    mc turned apron casual mg "You know her?"
    b eb me "I knew her mother."
    b bb mb "Misato was... one of the best employees I ever had."
    b ea ba "Before yer came along, of course!"
    show boss ed ma 
    "He lets out a hearty chuckle."
    b mb ea "Sayori was just a lass when I first met her."
    b me "Hardly a month old."
    b ec mb "And now, look at how much she’s grown."
    b ed mc "Though, I could say the same about yer!"
    b eb ma "..."
    b bb me "But, ah, onto more... serious matters."
    show boss md with None
    show boss ea
    camera master:
        align (0.5, 0.0) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("boss")
    $ say_transition = True
    "I sit down with him at one of the tables."
    b eb me "I, ah..."
    b ba ea "I know yer’ve got plans for after school."
    b mb "Are yer plannin’ on going and studying in Tokyo, still?"
    show boss md with say_dissolve
    mc ef ml "... Sayori and I made plans so long ago, but..."
    mc ea mb "Now that we’re re-united, I don’t see them changing."
    b eb me "Well..."
    show boss ea ma with say_dissolve
    "He smiles at me."
    b ec mb "I had a feeling that was the case."
    play music wtdgi
    b eb "Yer two are a strong pair, yer know? Her mother used to tell me all kinds of stories about yer, years ago."
    b bb me "It’s..."
    b ec bc "Hard teh believe she probably won’t be back."
    show boss md with say_dissolve
    mc mg "What do you mean?"
    b eb "..."
    b me "I, ah..."
    b ec "I probably shouldn’t be saying this, but yer deserve to know."
    b bb ea "And, more importantly, so does she."

    #[Full Voice Acting]
    b bc "... Misato’s dying, Melody."
    show boss md with say_dissolve
    _mc eb bd nb mh "Wh- What?"
    b eb bb me "It’s a... It ain’t pretty. But Sayori deserves to know."
    b ba mb "She’s a good lass."
    b ea bb me "You’ll tell her, right?"
    show boss md with say_dissolve
    mc bg ef ml "... I will."

    #[End Voice Acting]
    hide boss
    show bg:
        blur 0.0
    camera master
    show black:
        alpha 0.5
    with Dissolve(0.2)
    $ autofocus.unblock("boss")
    $ say_transition = False
    _mc ec na ba mh "I will... But I don’t know if I can do it tonight."
    _mc eg "I think it would be too much for her."
    _mc ea "For now, I’ll give it some time, and tell her in the morning. I couldn’t possibly ruin this for her."
    _mc ef "... I have to tell her tomorrow at the latest. Even if it means before the festival."
    "I don’t dare to wait any longer."
    _mc eg "... I need to bring my mood up now, or else she’ll know."
    _mc ma bg "... She’ll know anyway, won’t she?"
    stop music fadeout 2.0
    _mc ba mh "C’mon Melody. Use the mask."
    _mc ec "The mask that everyone sees."

    # goes back to script.rpy for the sleepover
    return