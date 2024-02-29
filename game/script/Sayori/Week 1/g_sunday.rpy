label week_1_sunday_sayori:
    call calendar_transition(day=29, hour=14, minute=25) from _call_calendar_transition_28
    scene bg mc_living_room
    camera master:
        align (0.35, 0.2) zoom 1.7
    with dissolve_scene_full
    pause 0.02
    camera master
    with Dissolve(0.2)
    play music dollaort

    "As the credits roll for the upteenth time today, I stand up and stretch." 
    _mc turned casual bb eg mg "Man, I really needed that breather. It's a bit disappointing that I'm not working today, but it's not like I'll miss the money today." 
    "The anime I'd just finished gave me a bit to consider, but I'd rather do some cooking. It was getting toward lunch time, and I had a plan for the day." 
    "I'd made up my mind." 
    "I'm going to invite Sayori over for dinner." 
    "I've already planned a three-course meal, done the shopping, and prepared the dining table." 
    "All I had left was to invite her." 
    "Something I really, definitely, should have done first." 
    _mc bi eg mm "Dammit." 
    "Taking a deep breath, I march toward my front door." 
    
    scene bg mc_house_entrance_day with wipeleft

    _mc turned casual ef mh "Better late than never, right?" 
    _mc bb ma "Besides, the food won't spoil that quickly, we could give tomorrow a go, right?" 
    _mc ec ba mh "Unless she isn't free either day." 
    _mc bi "This... may have been a mistake." 
    "I take some time to compose myself, walking out the front door."

    scene bg s_house_day with wipeleft
    $ advance_date(minutes=2)

    "My nerves racking up, I quickly rap on Sayori's door." 
    _mc turned casual bi eg mm "C'mon, me. Sayori was my best friend for years. What the hell is wrong with you? Just... act normal." 
    show sayori turned casual md at t11
    "The door swings open, and before I can muster any more words to berate myself with, Sayori is standing in front of me." 
    s mb lup "Hey, Melly! What's up?"
    show sayori ma
    mc ef nb ba mf "Oh, uh..." 
    _mc mh "Remember, cool!" 
    show sayori ldown
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "Leaning into the doorframe, I give her the biggest smile I can muster." 
    mc ed md ba na"Oh, hey Sayori. Didn't see you there." 
    show sayori md nb with say_dissolve
    _mc eb be mh "What... the hell was that?" 
    _mc "Are you trying to make a fool of yourself?" 
    _mc eg bi "Ah, forget it. Just ask her to dinner already." 
    _mc eb be "Wait, dinner?"
    _mc bf "Wouldn't that make this a date?" 
    mc ml bi eg "No no, It's just dinner." 
    s mh "Oh, there's food?" 
    s mb na "Were you inviting me over?" 
    show sayori ma with say_dissolve
    _mc eb ba mf nb "No- Wait- yes. This could work." 
    _mc ec bi mh "Just... don't screw this up." 
    mc ea ml na ba "Oh, yeah, I was. If you're free or anything. If you're not, that's cool." 
    _mc ec bi mh "Geez, now you sound like an unconfident jerk? Are you trying to screw up that archetype too?" 
    s mh "Yeah, sure, I'd be happy to. What time did you have in mind?" 
    show sayori md with say_dissolve
    mc ef mf "I- uh-" 
    mc ea ba mg "I was thinking six, does that work?" 
    mc mb "I've got a movie to watch afterward as well, if you wanted." 
    s mb "Oh, yeah for sure! I'll need to get ready, so I'll see you then!" 
    show sayori ma with None
    camera master
    show sayori me lup
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Sayori moves to close the door, then pauses, re-opening it."
    $ autofocus.unblock("sayori")
    s mh "Did you need me to bring anything?" 
    show sayori ma
    mc "Ah, no, just yourself, that's plenty." 
    s ldown e3d mb "Cool, see you in a few hours then!" 
    show sayori ma at thide
    hide sayori
    "The door softly closes in my face." 
    _mc eg bi mh "Alright. Looks like I need to have a very clear chat with myself, while I make dinner." 
    _mc ec "Addressing... whatever the hell that was." 

    scene bg mc_kitchen_day with fastfade
    $ set_date(hour=17, minute=40)

    _mc turned casual "Alright. It won't be long before Sayori arrives. Gotta make sure everything is done."
    show bg mc_living_room with NonBlockingTransition(wiperight)
    $ advance_date(minutes=2)
    "I race around, meticulously scanning every corner of the house."
    show bg mc_bedroom_afternoon_open with NonBlockingTransition(wiperight)
    $ advance_date(minutes=2)
    "I find myself standing in my bedroom."
    _mc bb eb nb mf "Wait, what am I doing here?"
    _mc nc "It's not like she'll come up here for... any... reason..."
    show black with Dissolve(0.2)
    "My thoughts start to drift to a dangerous place."
    "It's become harder and harder to control over this past week. I don't know what's wrong with me."
    _mc bi eg mh "It's worse than it ever was in middle school, that's for sure."
    _mc ec nb "Regardless, she can't come in here. No way, that's off-limits." 
    hide black with NonBlockingDissolve(0.2)
    "Turning my back, I walk out and close the door."

    scene bg mc_kitchen_day with wipeleft

    "Racing back down the stairs, I check the table, then the oven, turning it down to the lowest setting,"
    show bg mc_living_room with NonBlockingTransition(wiperight)
    $ advance_date(minutes=3)
    extend " then the living room, to make sure the movie is all set." 
    show bg mc_kitchen_day with NonBlockingTransition(wipeleft)
    $ advance_date(minutes=3)
    "Then I readjust the placemats, the cutlery, the jug of water, and the plates." 
    camera master:
        align (0.0, 1.0) zoom 1.7
    with Dissolve(0.2)
    "I grab the entree, consisting of hand-made spring rolls, some prawn crackers, pumpkin soup and some bread rolls, all carefully made fresh this afternoon."
    "Placing them, very gently, in the centre of the table, I take a deep breath." 
    mc turned casual thinking ml "Okay. I think that's everything." 
    mc ec mf "But, just in case..." 
    show black
    show bg mc_living_room
    camera master
    with NonBlockingDissolve(0.2)
    $ advance_date(minutes=4)
    play sound doorbell

    "I make another full round of the house, and again, and again, before the doorbell rings." 
    "The shock almost makes me drop the bottle of water I was drinking from."
    hide black
    mc eb mg ldown "Crap, that's her!"
    "I make my way over to the door, as quickly as my feet would carry me, and trip over my own legs in the process." 
    mc mj bb nb "Ah-"
    show black:
        alpha 0.0
        easein 0.15 alpha 1.0
    camera master at vpunch
    play sound fall2
    "As I hit the floor, my wrist lands at an angle, and I hear a small crunch." 
    "My face contorts from the pain, as I try desperately to return to my feet." 
    "Unfortunately, that same wrist is used to try to pull me up, leading to an even larger spike of pain, coursing through my entire arm, causing me to cry out." 
    mc bg eg mm "Gh- Why? Why now?"
    show bg mc_house_entrance_afternoon
    hide black
    camera master:
        align (0.0, 0.55) zoom 1.5
    with Dissolve(0.3)
    $ say_transition = True
    $ autofocus.block("sayori")
    $ advance_date(minutes=4)
    "Staggering to my feet, this time making use of my off-hand, I finally reach the door." 
    show sayori turned casual md:
        matrixcolor TintMatrix("#ffdfc0")
        xcenter 0.25 ypos 1.0 yanchor 0.95 zoom 0.7
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "Swinging it open, I see a familiar face waiting for me."
    s b4 mh rup "Took your time, huh? Do you want me to come back later?" 
    show sayori md with say_dissolve
    mc md eh "N- No, it's all good, don't worry." 
    show sayori b1b rdown with say_dissolve
    "I avoid clutching my hand, out of a fear she might notice something off."
    mc ea mb ba "A- Anyway, come in. Everything's all set up." 
    s mn e3d b1a "Ok~"
    show sayori ma with None
    hide sayori
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "Sayori steps into the house, making her way toward the kitchen." 
    camera master
    with Dissolve(0.2)
    "I close the door behind me, as I feel the heat rise to my face."

    scene bg mc_kitchen_day
    show sayori turned casual e2a at i11
    with wipeleft

    "I follow her, acutely aware of her features from behind."
    camera master:
        align (0.5, 0.7) zoom 3.0
    show black zorder 1
    with Dissolve(0.2)
    _mc turned casual ec mh "Her figure has definitely shapened since middle school, that much is a given."
    camera master:
        yalign 0.15 zoom 3.2
    with Dissolve(0.2)
    _mc ea "She might have cut her hair right back after we stopped hanging out, but...."
    camera master:
        yalign 0.2 zoom 1.5 
    with Dissolve(0.2)
    _mc ma nc "She's still the same Sayori I once-"
    hide black
    camera master
    _mc eb nb mh "Ah, no. Stop that thought. We're just friends. Just hanging out for the evening. Nothing more to it."
    show sayori e1a at t41
    "Sayori sits down in the same old spot."
    show bg:
        align (0.0, 1.0) zoom 1.7 blur 2.0
    show sayori:
        zoom 1.2 ypos 1.0 
        xoffset 100 yanchor 0.72
    with Dissolve(0.2)
    "I take my place on my own, next to her." 
    show sayori md with say_dissolve
    mc ea na mg "The, uh, entree is ready when you are." 
    s rup b4 e1d mb "Entree? Well, aren't you fancy today?" 
    show sayori e1a b1a md with say_dissolve
    mc eh be md "Ah, yeah, I just felt like cooking." 
    show sayori me b2b rdown with say_dissolve
    "Sayori shoots me a glance, a hint of concern crossing her face." 
    s e2a mg "... Sure..."
    show sayori md with say_dissolve
    "Trying to quell the awkward mood before it starts to grasp us, I take the soup ladle and pour some into my bowl. " 
    mc ea ba mb "You should try it, it's really good."
    s e1a b1a mb "Yeah, I will."
    s mg "How... How much food did you prepare?" 
    show sayori md with say_dissolve
    _mc ma "Oh, she's that hungry?" 
    mc ed md "Heaps, of course. Have as much as you'd like."
    show sayori nb e2a b1b with say_dissolve
    "Something about Sayori's expression shifts." 
    _mc ea mh "Maybe she wasn't hungry?"

    window auto hide
    show sayori na ma e1a b1a with wipeleft_scene
    $ advance_date(minutes=7)
    
    "Most of the entree passes in silence. I wouldn't really call it an awkward silence, though it definitely is, but it's still something soothing." 
    show sayori nb with say_dissolve
    "It's been a while since Sayori and I have just... enjoyed each-other's company like this." 
    show sayori e2a with say_dissolve
    "Though..." 
    show sayori md with say_dissolve
    "With every glance, Sayori seems more and more uncomfortable." 
    show sayori e1a with say_dissolve
    mc turned casual mf "Hey, Sayori..." 
    show sayori b1a with say_dissolve
    mc mg "Is everything alright?"
    s na mb "Yeah, of course. Don't mind me." 
    show sayori ma with say_dissolve
    mc ml bf "Don't mind you? If you're not having fun, we can leave dinner for a little while."
    s lup mg "No, it's fine." 
    show sayori md with say_dissolve
    mc be mb "Sayori, I'm here for you, you know that, right?" 
    show sayori ldown nb with say_dissolve
    mc ba "That's why I did this. Made you dinner, prepared a movie, even made some lunch for us to eat tomorrow. It's all for you." 
    s e2a mg na "I didn't ask you to-" 
    s me "..." 
    "Sayori looks at me, her expression changing." 
    "It was then that I realised what I just said." 
    "That's not something a friend would say." 
    "That's something... a partner would say..." 
    show sayori md e1a with say_dissolve
    "My cheeks flush."
    stop music fadeout 3.0
    s b1b mg e3c "I think... I've had enough." 
    show sayori md with say_dissolve
    _mc eb bg mf nb "... What?" 
    _mc "Is she leaving? Did I really screw up that badly?" 
    mc ea ba ml "Oh, alright."
    show sayori e1a b1a:
        xoffset 0
        i41
    show bg:
        blur 0.0 zoom 1.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("sayori")
    s mh lup "Did... Did you want some help with the plates?" 
    show sayori md
    mc mb na "N- No, I've got it." 
    show bg:
        align (0.24, 0.6) zoom 2.0
    hide sayori
    with Dissolve(0.2)
    play sound_loop tap_water_loop fadein 1.0
    "I grab the used utensils and quickly make my way to the sink."
    _mc ef bg mh "Is she really leaving? What did I do?" 
    _mc "Was the food really that bad?" 
    _mc "What do I do? Can I salvage this?" 
    "My thoughts are cut like a knife." 
    show bg:
        zoom 1.0
    show sayori turned casual lup nb me at i11
    with Dissolve(0.2)
    s mg "Are you sure you're ok?"
    show sayori ldown md
    mc ea ml ba "Y- Yeah, just tryna..." 
    s na b4 e1d mh "Well, I'm assuming that the main course is in the oven, and you're nowhere near it, so..." 
    show sayori md
    _mc eb mf "The main course?" 
    "I look at her, confusion worn on my face." 
    mc bd ea ml "What do you mean?" 
    s e1a mh "Aren't you getting the main course out, now that we've finished with our entree?"
    show sayori b1a md
    mc ba mh "..." 
    stop sound_loop fadeout 5.0
    _mc mf "There's... no way." 
    _mc eb mh "Did I really just misinterpret what she said?"
    "I could kick myself."
    mc mb ea "Yeah, don't worry about it, I'll bring it out in a minute."
    mc md eh be "Feel free to go sit down, alright?"
    s b1b e2a mg "Okay... If you're sure."
    show sayori md at thide
    hide sayori
    "Scrambling to get the remainder of the main prepared, I quickly set out the roast, including 
    the salad, roast vegetables, and Hasselbeck potatoes, something I know used to be Sayori's favourite."
    "I also grab a second jug, this one containing orange juice, and attempt to carry it out to the table." 
    "Unfortunately, as I have been doing so all night so far, I've made a miscalculation."
    camera master:
        xoffset 0.0 align (0.6, 1.0) zoom 1.0
        easeout 0.3 xoffset -14
        easein 0.12 xoffset 14
        easein 0.12 xoffset -14
        easein 0.12 xoffset 14
        easein_back 0.3 zoom 2.5
    play sound ["<silence 0.69>", audio.fall]
    mc eb bb nb mg "Shit!"
    "Holding the tray of food in my off-hand, and the juice in my main, I proceed to wince, dropping the plastic jug." 
    "My hand buckles and limply droops as I attempt to recatch the jug, and it clatters upon the floor."
    show sayori turned casual b2b me nb at t11
    "For a moment, the pain is all I can process, before I realise Sayori is standing in front of me, holding the tray of food." 
    camera master
    with Dissolve(0.2)
    s lup mg "Melody, what happened? The juice went everywhere! Are you okay?"
    show sayori ldown b1b e2a md na
    "Clutching my wrist, I glance up at Sayori. She's placed the tray on the bench beside us, and she's crouching in front of me." 
    s e1a b1a mh "I'll get you some ice, but you have to tell me what happened, alright?"
    show sayori md

    scene bg mc_living_room:
        blur 2.0
    show layer master:
        align (0.5, 0.2) zoom 1.5
    show sayori turned casual e2a md b1b at i11
    with wipeleft_scene
    play music myfeelings
    $ autofocus.block("sayori")
    $ say_transition = True
    $ advance_date(minutes=4)

    "A few minutes later, I find myself sitting on the couch, Sayori next to me." 
    "She's gently holding the ice to my hand, resting in her lap, while the movie plays."
    s mh b1a "You really should be more careful. I don't know why you've been pushing yourself that hard, but, for my sake..." 
    s mg b2b e1a "Don't." 
    s mb e3c "I'm not worth the effort, alright?" 
    show sayori e1a ma with say_dissolve
    mc turned casual eb mg bb "No. No, you're wrong." 
    show sayori md with say_dissolve
    mc ea ba ml "To me, you're worth..." 
    show sayori mj e2a with say_dissolve
    mc mf ef "All the effort."
    "My tired brain wants to complain about how embarrassing what I just said was, but I don't think I could cope."
    "I've been so exhausted, running all over the house, out to the mall for shopping, and back, making food, and, most draining of all... simply worrying, that I haven't been able to slow down at all."
    "My hand still aches, though the ice is helping. With any luck, it'll be back to normal by tomorrow."
    "The movie is most of the way through, but I don't think I can stay awake for it."
    "Should I send Sayori home?"
    call blink(duration=0.4) from _call_blink_14
    "Nah, I'm sure she can..."
    call blink(duration=0.8) from _call_blink_15
    "Let..."
    call blink(duration=1.0) from _call_blink_16
    "Herself..."
    extend " Out..."
    call close_eyes(duration=2.0, wait=True) from _call_close_eyes_15
    pause 2.0
    $ say_transition = False

    scene bg mc_living_room
    camera master
    show mc_roof zorder 5
    with Dissolve(1.5)
    $ set_date(hour=20, minute=32)
    $ phone_available = False

    "I don't think I've slept that well in a long time."
    "Wait, why am I on the couch?"
    "And what is this angle-"
    hide mc_roof
    show sayori turned casual e3c me b1b:
        i11
        block:
            linear 2.02 yoffset -3
            easein_cubic 0.9 yoffset 2
            repeat
    show layer master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    s "... Zzz..."
    "Sayori?"
    "She's sleeping on my shoulder."
    "She looks so peaceful."
    "Her soft hair rests gently, like a blanket, over my shoulder."
    "Her soft breathing, and the rise and fall of her chest, create a rhythm that I can't help but close my eyes and soak in."
    "The soft smell of her hair wafts into my nose, further dulling my senses."
    _mc casual turned ec "I could remain here forever..."
    "It would be a shame to disturb her now, so maybe, I'll just go back to sleep."
    _mc ea mh bb "That's alright, isn't it?"
    _mc ec bi "Wait..."
    "Looking over at the table, I notice my phone."
    "Some sort of missed notification. I really must've slept like a log."
    _mc ea ba "... Can I get the phone and check it, while not disturbing Sayori?"
    show layer master:
        offset (100, -50) align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    "Carefully, I manuever myself around the couch, very slowly and delicately, reaching my arm out."
    _mc eb mf "Just a little more, and..."
    phone register "lit_club":
        time hour 19 minute 23 day True year True month True 
        "s" "Who wants a sleepover at my place?!"
        "m" "Oh? That sounds like fun. When would it be? I would need to get permission."
        "s" "Hmmm"
        "s" "What about Saturday?"
        "n" "I think I should be able to do that."
        "y" "Oh? A sleepover? Whatever for?"
        "s" "Because we can, silly~"
        "y" "Just for fun? I don't see why not, then."
        "s" "Let's do it in the afternoon, at my place."
        "s" "Maybe straight after classes?"
        "m" "I believe I can organise that, but I'll let you know."
        "n" "Yeah, I think I can make that as well."
        "s" "Sweet! I'll see everyone there! Bring some snacks with you, and your stuff for sleeping. There's plenty of room!" # im stuff
        "m" "Alright, see everyone at club tomorrow! I look forward to this event!"
        "y" "Indeed."
    _mc ma "There!"
    play sound fall
    show layer master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    "Clutching my phone in my hand, I nudge myself back into place before I accidentally fall off the couch itself."
    "I open up my messaging app and see..."
    phone discussion "lit_club"
    $ phone_available = True
    _mc bi ec "... Geez, Sayori planning things without me, huh?"
    _mc ea thinking ba mh "I should probably say something here before I forget."
    phone discussion:
        time auto True
        "mc" "I dunno, I've got work that afternoon."
        "mc" "I might be able to come by after work. Can it be around 5pm?"
    phone end discussion
    _mc eg ma ldown "Hopefully they see that before the sleepover actually happens."
    _mc ef mh "Then again, that's not until next Saturday, right?"
    _mc ma "Yeah, that should be plenty of time."
    _mc eg "Now I should get back to sleep."
    _mc "Good night, Sayori..."

    $ add_calendar_description(calendar_descriptions["sayori"][3])
    
    call week_2_monday_sayori from _call_week_2_monday_sayori
    return