label week_2_saturday_yuri:
    call calendar_transition(day=4, hour=5, minute=39, second=0) from _call_calendar_transition_46
    scene bg mc_bedroom_day_closed
    call close_eyes(0.0) from _call_close_eyes_30
    with Dissolve(1.5)
    $ set_internet(True)
    play music anewday

    "A yawn escapes my lips as I stretch, my eyes slowly preparing to open and welcome the new day."
    mc turned naked messy nostrands ec bi mf "Hm... Mm...?"
    call open_eyes(2.0) from _call_open_eyes_21
    "I check the time."
    _mc mh "5:39..."
    _mc ef ba "Too early to have the alarm wake me, but"
    extend eg " too late to go back to bed."
    _mc bi ma "Geez, thanks circadian rhythm."
    "I prepare myself, get dressed and head off to eat some delicious breakfast."
    
    stop ambient fadeout 2.0
    scene bg mc_kitchen_day
    camera master
    with wipeleft
    $ advance_date(minutes=40)

    _mc turned casual eg mj "Hah... Last week I was pretty stressed about all kinds of things."
    _mc ec mh "But.. Now I feel pretty good."
    _mc ea "The festival..."
    _mc thinking "Will it really bring new members?"
    _mc ef "Well, Monika would love that, for sure."
    _mc bi "It will get a bit busy if there's going to be 7 people, but..."
    _mc eg ma ldown "Oh well."

    scene black with wipeleft
    $ advance_date(minutes=23)

    "Having eaten a delicious breakfast, and having a large amount of time left till I have to be at work..."
    show bg school_street_day
    hide black with NonBlockingDissolve(0.5)
    "I decide to head off early."
    camera master:
        align (1.0, 0.65) zoom 3.0
    with Dissolve(0.2)
    "I stop walking near a certain now-recognisable house."
    _mc turned casual "Hey... That's where Yuri and I found that cat."
    _mc ec mh "I wonder where it is now."
    _mc ea "... Should I take a cat as a pet?"
    _mc ec "Hmm..."
    _mc ma "That's food for thought."
    camera master
    with Dissolve(0.2)
    "I continue on, eventually reaching the cafe."
    
    stop music fadeout 2.0
    scene bg cafe_inside_day with longfade
    $ set_date(hour=7, minute=8)
    $ advance_date(seconds=20 + 32)
    play music cafe

    "Walking in, I see that the place isn't as busy as I expected it to be this time of morning."
    show boss turned me at t11
    b "Hey, kid!"
    show boss ma
    mc turned casual mb "Oh! Hey, boss!"
    b mb "Yer're quite early."
    b bb me "Everything alright?"
    show boss ba ma
    mc ml "Yeah. Thanks for asking."
    mc ef mg "Where's everyone? I thought I was just that little bit extra early, not like massively early."
    b mb "Yer'd would be amazed at how many people simply order coffee ten minutes before work begins, then rush their whole morning..."
    b mc ed "Haha, not like I blame 'em!"
    "I look at the clock."
    _mc ec mh "7:10..."
    mc ea mg "Anything... special on your end?"
    b ea mb "I don't think so. This cafe rarely has hardships."
    b me "Yer know why?"
    show boss md
    mc ec mh thinking "Hmm..."
    mc ea mb "Because of your great leadership?"
    b ec mb bb "Ohoho, don't flatter me!"
    b ba lup mb ea "It's because of people like yerself."
    b ldown mc ed "People who care about what they do, and do their utmost best."
    mc mf "Oh... Well."
    show boss ea ma
    mc mb ldown "You know why we do that?"
    b bb me "Hmm?"
    show boss md
    mc eh md "Because you actually care about them."
    b ed mc ba "Ah... Heh, that's true."
    "The boss gives a bright grin, before glancing around."
    b eb bb me "By the way..."
    b ea ba mb "How are you and that Yuri lass?"
    b me "The whole Literature Club shenanigans?"
    show boss md
    mc mb ea "Everything's well, we're actually having a sleepover tonight."
    b mb "Really? I used loved those when I was younger - A lot younger than yer are now, mind you, haha~!"
    b ec "Make sure you enjoy it, alright kiddo?"
    show boss ma
    "As other workers slowly enter the building and go to their posts, it becomes clear it's time to work."
    mc ml "I will, and, boss?"
    show boss bb md ea
    "He looks at me, curiosity in his eyes."
    mc ef bi mg "I normally try not to be chummy with you, but..."
    mc ea bg mb "Thanks. Thanks for being there and giving me advice."
    $ autofocus.block("boss")
    b "..."
    "The boss looks at me, deciding on his response."
    $ autofocus.unblock("boss")
    b ec mb "Always, kid."
    b ed mc ba "If something ever happens, yer can always come to me."
    b ea mb "Be sure to keep me up to date, eh?"
    show boss ma
    mc ba "Will do!"
    b mb "Now, good luck on the job, kid. We got work ahead of us."
    show boss ma at thide
    mc eh md "See you!"
    hide boss
    "As we walk to our posts, I can't help but feel happy."
    _mc ec ma ba "At this time..."
    _mc ea "Things seem to be going perfectly."
    _mc eg "No drama with me and the Literature Club..."
    _mc nc "Yuri trusting me..."
    _mc ea na "And, even a sleepover."
    _mc ec "I can't begin to ask for more."

    scene bg cafe_inside_afternoon with wipeleft_scene
    $ set_date(hour=16, minute=21)
    
    mc turned casual apron mb "Thanks for coming!"
    _mc ec ma "Another satisfied customer."
    stop music fadeout 3.0
    "Slowly, but surely, as time goes on, people leave as the cafe nears closing time."
    "As I clean up my post and put everything back in place, I return to the back."
    show boss turned mb:
        matrixcolor TintMatrix("#f5e2bb")
        t11
    b "Great job again, kid."
    show boss ma
    mc ea mb "Thanks!"
    b me "Make sure you enjoy that sleepover of yours, eh?"
    show boss ma
    mc ed md "Yeah, that's the plan~"
    b mb "Good! Then, I'll see yer next week?"
    show boss md
    mc eh bb ma "Mhm!"
    show boss ec bb
    "The boss scratches his chin."
    b eb me "Also..."
    b ba ea "I know this probably yer first time in a long time having a sleepover, so..."
    b mb "Don't be afraid to give me a call or text if you need anything, kiddo."
    b mc ed "I'll be around."
    "I muster up a smile."
    mc eg mb ba "Thank you, boss."
    mc ea "Enjoy your weekend, too."
    b mb ea "Will do, kid."
    show boss ma

    # goes back to script.rpy for the sleepover
    return