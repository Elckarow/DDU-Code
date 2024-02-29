label week_2_thursday_natsuki:
    call calendar_transition(day=2, hour=2, minute=4) from _call_calendar_transition_21
    scene black with Dissolve(1.5)
    scene bg am_bedroom_night_on_closed
    camera master:
        align (0.3, 0.5) zoom 1.7
    with amelia_pov(True)
    play music dollaort
    $ set_pov("am")

    am turned casual ponytail ee md "Mmmmh..."
    camera master
    with Dissolve(0.2)
    "I stretch my arms to the sky, slumping back into my chair."
    _am ec ma "God, that feels good..."
    "My stream for the night over, I take a moment to breathe."
    _am md bh "The latest game is no joke..."
    _am ee "That boss had me on the ropes literally the entire fight."
    _am bb ef ma "Still though, victory for Amelia~"
    "My shoulders are wound up tight - must be the gamer concentration pose getting to me."
    "Maybe I'll get something to eat. Sure, it might be... "
    _am ec md ba "Christ, 2am? I am gonna have the worst time at school tomorrow... Well, today, I guess."
    
    scene bg am_kitchen_night_off with wipeleft

    "The kitchen light is off - Best to leave it that way, lest I wake someone up."
    "My gamer eyes have long prepared me for this day, of course, so naturally I can see perfectly-"
    play sound fall
    show layer master:
        align (0.1, 1.0) zoom 1.0
        easein_back 0.2 zoom 2.0
    call close_eyes(0.2) from _call_close_eyes_11
    stop music
    pause 0.6
    "I fall flat on my face, tripped by some unknown object."
    am turned ponytail casual ec bh mh "Who the hell is putting random-"
    am ea me ba "Ellen?"
    $ autofocus.block("ellen")
    e turned ed md bc ponytail "..."
    _am ec md "Ellen tripped me?"
    $ say_transition = True
    _am ea bh "Wait, rewind, what's she doing sleeping on the floor?!"
    show layer master:
        align (0.1, 1.0) zoom 2.0
    show bg:
        blur 2.0
    show ellen:
        matrixcolor TintMatrix("#221f49")
        i21
        yoffset 270
        block:
            linear 2.02 yoffset 270 - 3
            easein_cubic 0.9 yoffset 270 + 2
            repeat
    call open_eyes(0.5) from _call_open_eyes_7
    "I get to my feet and gently poke her."
    _am ec ma ba "Yep, she's fast asleep."
    show ellen mj bg:
        pass
    with NonBlockingTransition(fastfade)
    "A few prods later and she starts to stir."
    _am ec bi md "Come on, I'm not leaving you here, and you're too big for me to carry you back to your room these days..."
    e ea md "Hm...?"
    show ellen mc with say_dissolve
    am ba mb "Wakey wakey, doofus~"
    "My voice is little more than a whisper, but in the silent room it feels louder than thunder."
    e ea bc md "Morning...?"
    e me "Why am I on the floor...?"
    show ellen mc with say_dissolve
    am ec bh me "That's what I was gonna ask you."
    e eb bb nb mi "Oh, right... Right!"
    show ellen mh:
        i11
        yoffset 0
    show layer master
    show bg:
        blur 0.0
    with NonBlockingDissolve(0.2)
    $ say_transition = False
    "She rockets to a sitting position and nods to herself."
    $ autofocus.unblock("ellen")
    e mg "I was waiting for you to finish streaming and come out for your snack, but you didn't!"
    e me bd ed "I waited so long!"
    show ellen mc
    am eb ba me "If it was urgent, you could have just knocked?"
    e ec mg na "No! I can't disturb you."
    show ellen mh
    am ec mb ba "C'mon, dude, it's not that bigga deal."
    "She doesn't meet my gaze."
    am eb me "What is it?"
    e me "I..."
    show ellen mc with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0 
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("ellen")
    "I lean on the wall, patiently waiting for her to find the words she's looking for."
    e me "I don't want you to hate me, Amelia."
    show ellen mc with say_dissolve
    am mb ea bd "El, there is nothing you could do that would make me hate you."
    "Even still, she doesn't look me in the eye."
    e bc ed me "There is."
    show ellen mc with say_dissolve
    am ec bh me "... You didn't sleep with him, did you?"
    e eb bb mf nb "No!"
    e bg ea mj "We- We've hardly kissed!"
    show ellen ba mc na with say_dissolve
    "I hold up my hand, indicating for her to lower her voice."
    show ellen ed bc mh with say_dissolve
    "She takes a moment to compose herself, then continues."

    play music wtdgi

    e me ec "It's hard."
    e ea bd mf "I don't want you to hate me."
    e ec me "But all I seem to be able to do is..."
    e eb mf nb be "With this, with the- The asking about stuff, the..." # im stuff
    e bg ec mg "I know you want to keep it to yourself and that you don't want to talk about it, but I-"
    e ea me "I don't know how to help, or if I even can."
    e md ec bc na "And..."
    e be eb mf "I keep getting this awful feeling that I'm constantly making it worse."
    show ellen mh with say_dissolve
    am eb me ba "Ellen, it's your life. I won't stop you from doing something that makes you happy."
    show ellen ea bd with say_dissolve
    am ea bd mb "... Besides, we all have lessons to learn. You're my sister, and I want to look out for you, but I can't stop you from taking life into your own hands."
    show ellen bg ed mj with say_dissolve
    "She turns toward the wall and thumps her head on it, breathing a heavy sigh."
    camera master
    show bg:
        blur 0.0
    show ellen md
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("ellen")
    e me ec bc "It's not... I don't want you to be upset."
    show ellen mc
    am ec ba me "That's the third time you've said that, El. I know, trust me."
    e bd ea mf "So... why do I feel like I make you mad every time I do anything?"
    show ellen mh
    am ed mh "Not mad. Maybe a little disappointed, but I've never really been mad at you."
    am ee mf "... Maybe when we were younger, but not recently."
    am ec bh me "Kaito's a bad influence, and an awful person, but I won't step in unless he's hurting you."
    $ autofocus.block("ellen")
    e "..."
    $ autofocus.unblock("ellen")
    e ec mf "Why does this all feel like I'm the bad guy here?"
    show ellen mc
    am ed me ba "Well, you are breaking the unwritten rule."
    show ellen ea be
    "She turns her head sideways to glance up at me."
    am mi ec "You're dating my ex. It feels pretty gross just thinking about it."
    $ autofocus.block("ellen")
    e "..."
    $ autofocus.unblock("ellen")
    e ec bc me "You ever just..."
    e ba ea mf "Want to know what it's like inside someone else's head?"
    show ellen mh
    am ec ba mb "All the time~ Why?"
    e bd mf "... I want to know what you're thinking. I want to know why you are the way you are."
    show ellen mh
    am ea bd me "... Please tell me that's not the reason you're dating him."
    e bb nb mf "No! Well-"
    e ec bc mg "Not really. I just- After you two... You left me."
    e ea bd me "We were..."
    show ellen md 
    am ec be "El-"
    show ellen eb bg mg na at hop
    e "No! Don't you 'El' me after all that! Please-"
    e ea mf "Don't just dismiss me again."
    e mg bd "Five years I waited for you to- To talk to me like your sister, like the way we were."
    e be eb mf "We were {i}so{/i} close! I could rely on you for everything!"
    e mj ec bg "But after him, you- You shut me out! You decided I wasn't worth thinking about or talking to!"
    e ea mf "I tried, so hard, for so long to get you to open up to me again!"
    e mj ef "I don't... I don't even know who you are anymore. You won't show anything to me, won't rely on me, won't trust me."
    show ellen md ed
    am ba eb me "I know-"
    e mg ef "So why?"
    e ea bd mf "You're my whole world, Mills. Why do you shut me out of it?"
    show ellen mh
    "For a long time, I don't have an answer for her."
    "For a long time, we simply stand there, at odds."
    am ec me "... Because..."
    am ee bb mf "I won't say I'm doing it to protect you or any crap like that."
    am ed mh "I shut you out because..."
    am ec ba me "You saw in me something that I didn't see in myself."
    show ellen bc
    am ee be mi "I couldn't bear to spoil the image you have of me."
    am ea bd mb "I joke about it, but... you're my baby sister, El. I couldn't bear to see anything hurt you, least of all me."
    $ autofocus.block("ellen")
    e "..."
    "She doesn't need to speak those words."
    "I knew before I'd even said them exactly what she's thinking."
    _am ec ba md "... Honestly, I've known exactly what words she'd say every time she spoke tonight."
    _am ed "Of course I knew how she felt."
    _am ec "I just couldn't bring myself to be the one to bring the knife to bear."
    $ autofocus.unblock("ellen")
    e ec me "... Why do you hate me?"
    e ba mf ea "All this time... you wanted me to believe that you were doing this for me."
    e bg mj "But you just hate him, and you hate the idea of us being together."
    e ec mg "So much so that you'd set your friend up to try and convince me to break up with him."
    show ellen mh
    am bd me "I-"
    e ea mf "Mel wasn't doing it out of spite, I know. She wasn't even doing it intentionally."
    e mj "But you brought her here all the same."
    e ba mg "Why do you hate him?"
    e bg mj eb "Why do you hate {i}me{/i}?"
    e ec bd me "All I ever wanted..."
    e ea be mf "The only thing I ever wanted was you."
    show ellen mh
    am ed ba me "... I know."
    "I breathe a deep, heavy sigh."
    am ee mi "I never hated you. Not once, not a single day in your life have I hated you."
    e ec mf bg "Well... it sure feels like it some nights."
    show ellen ed mh thinking at lhide
    hide ellen
    "She shakes her head, stepping back into her room."
    am ed me ba "... I guess it does."
    "For a few moments, I refuse to tear my eyes away from the door."
    "After that, my appetite long since ruined, I walk back to my own room, nursing the tiny little fragments of my shattered heart."
    
    stop music fadeout 2.5
    scene black with Dissolve(2.0)
    scene bg mc_bedroom_day_closed with mc_pov(True)
    $ set_date(hour=7, minute=13)
    $ set_internet(True)
    $ set_pov("mc")

    "..."
    play sound smack volume 0.5
    pause 0.5
    _mc turned bun naked nostrands mh "Hm?"
    _mc ec "What’s that?"
    play sound smack volume 0.5
    pause 0.5
    _mc ea "Something knocking on my window?"

    scene bg mc_bedroom_day_open with Dissolve(0.5, time_warp=_warper.ease)
    play music a_sunshine

    _mc turned bun naked nostrands ec ma "Oh, would you look at that."
    "Sayori’s looking at me from her window. I should see what she wants."

    show expression split(Transform("bg mc_bedroom_day_open", crop=(0.0, 0.0, 0.5, 1.0), crop_relative=True), "bg s_bedroom_day", vertically=True)
    show sayori turned casual at i22
    with wiperight

    mc ea mb "Morning!"
    show sayori lup rup e3d mc at hop
    s "Yeah! C’mon over! Let’s have breakfast together!"
    show sayori ma
    mc bb "Sure! Give me fifteen minutes to get dressed!"
    s ldown rdown e1a mb "Ehe, sure!"
    show sayori ma

    scene bg mc_bedroom_day_open with wipeleft

    "She closes the window, and beams at me."
    _mc turned bun naked nostrands ec ba ma "Hah, now that’s a way to start the day, eh?"

    scene bg s_living_room with wipeleft_scene
    $ advance_date(minutes=20)

    show sayori turned at t11
    s e3d mc "Heeey! You finally got here!"
    show sayori ma
    mc turned mb "Sure did! So, what’s the occasion?"
    s mb e1a "No occasion, just wanted to hang out!"
    show sayori ma
    mc ed md "That sure sounds like you, doesn’t it?"
    show sayori e3d
    "Her warm smile works wonders on my attitude."
    show sayori e1a
    mc ea mb "Wanna walk to school together after breakfast?"
    s mb e1d b1d "Do I ever?"
    show sayori ma e3d b1a at dip
    "She places a bowl of cereal and a cup of hot chocolate in front of me on the coffee table."
    show sayori e1a
    mc thinking mg "Simple, but outstandingly effective."
    show sayori e1d b1d mj
    mc eg mb ldown "Not the healthiest of meals, but sugar and fibre will definitely jump-start your day."
    s lup mh "C’mon, do you have to read into everything?"
    show sayori md
    mc ed md "Sure I do. One of us has to keep informed~"
    show sayori e3d b1a ma ldown
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.2
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "She sits down next to me, beaming."
    s e1a mh "And you think that isn’t me?"
    show sayori ma with say_dissolve
    mc eg mg "Oh, it’s {i}definitely{/i} you, I just like to try and keep up, sometimes."
    show sayori e3d with say_dissolve
    "She giggles, digging into her own breakfast."
    "I take the opportunity to do the same."

    scene bg residential_day
    show sayori turned e2a:
        ypos 1.03 yanchor 1.0 xcenter 240
        zoom 0.6 yoffset -55 xoffset -20
    show bg:
        blur 3.0
    camera master:
        align (0.0, 0.5) zoom 2.0
    with fade
    $ set_date(hour=8, minute=1)
    $ set_internet(False)

    mc turned mg bb nb "Sayori, wait up!"
    show sayori md e1a with None
    show sayori turned:
        zoom 0.8 offset (0, 0) xalign 0.5
    camera master:
        align (0.5, 0.2) zoom 1.4
    show bg:
        blur 1.8
    with Dissolve(0.4, time_warp=_warper.ease)
    s lup mh "I’m hardly jogging! When did you get so out of shape?"
    show sayori md with say_dissolve
    mc ec bg mg "M- Me? When did you get so {i}in{/i} shape? Did you-"
    "In between my sentence, I pause to heave a deep breath into my lungs."
    mc bf eg ml "-Rejoin the track team, or something?"
    s e1d b1d mh ldown "I didn’t! Just walked to school every day, like you!"
    show sayori md with say_dissolve
    mc ef bg mf "Geez, am I eating too much?"
    "I worry to myself, clicking my tongue."
    show sayori e1a b1a me with say_dissolve
    _mc ec bi mh "Come to think of it, my food supplies have been dropping a hell of a lot faster than they should be. It would make a lot of sense."
    _mc ea ba "Have I just not been noticing?"
    s lup mg e2a b2c "Hey, don’t..."
    show sayori me with say_dissolve
    "She drops back and meets me, biting her lip."
    s b2b e1a mb "Don’t pay it any mind, alright? It’s not you, maybe I have been exercising?"
    show sayori ldown ma with say_dissolve
    mc ef mb "N- No, it’s fine, I just..."
    mc ea ba na mg "I’ve been going through my food faster than I expected. Maybe that’s why."
    s mg b1a "Ah..."
    show sayori ma rup with say_dissolve
    "She puts a hand on my shoulder."
    s mh "Did you want to eat with me more often, then?"
    s mb "Maybe I can help?"
    show sayori ma with say_dissolve
    mc eg mb "Yeah, I think I’d like that."
    "I nod. Out of anyone, she'd know if there was something off."
    "After knowing what I now know about her, I’m a little surprised by her offer, but I’ll be damned if I don’t take the chance to make sure she’s eating."
    _mc ec ma "Besides, I do... want to spend more time with her."
    s rdown mh "Then... Maybe we should have lunch together?"
    show sayori md with say_dissolve
    mc ea ml "I, ah, was actually going to-"
    mc eg mb "No, wait, I’d like that."
    _mc ma "I was going to ask Amelia, but..."
    _mc ec "It’s fine. I’ll have plenty of opportunities to hang out with everyone."
    s me e3c "Hm..."
    "She considers my hesitation for a moment, but brushes it off."
    s mh e1a "If you’re sure."
    show sayori b2c e2a ma with say_dissolve
    mc ea mb "Yeah, I am."
    show sayori e3d b1a with say_dissolve
    "Sayori’s expression clouds over for a moment, before she returns to normal."
    show sayori e2a:
        xcenter 230 zoom 0.58 yoffset -55 xoffset -20
    show bg:
        blur 2.5 zoom 1.07
    camera master:
        align (0.0, 0.5) zoom 1.6
    with Dissolve(0.2)
    "Skipping back along the path, I follow behind her."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc mh "She must have her own hang-ups about what happened between us, but..."
    _mc eg bi "I won’t let something like that be the thing that destroys us again."
    _mc ec "I spent a quarter of my life praying I’d never be forced to talk to her again, for my own sanity, but now that she’s here once more?"
    _mc ea bg ma "There’s nothing I wouldn’t do to keep that smile safe, fake as it might be."
    _mc ef "And perhaps, one day, I’ll plant a new one there. Something she might feel is a little more real."
    "I sigh. After all this time, after everything we’ve been through-"
    _mc eg "I still love her."
    $ say_transition = False

    stop music fadeout 2.0
    scene bg class_2_day
    camera master
    with longfade
    play music school
    $ set_date(hour=10, minute=25)
    $ autofocus.unblock("sayori")

    _mc turned "Chemistry. Always a good class."
    _mc thinking mh "I’m not sure why, but I’ve actually enjoyed it more than most people. Maybe I just picked it up faster?"
    _mc ec "I’m definitely one of the top marks in the class, but..."
    show bg:
        blur 2.0
    show natsuki cross e2a mj:
        zoom 0.57 xcenter 0.78 yalign 1.0
    camera master:
        align (0.8, 0.8) zoom 1.5
    with Dissolve(0.2)
    _mc ldown "I’m still beat out by Natsuki."
    show natsuki b3a e3d mi with say_dissolve
    "..."
    show natsuki b1a e2a mj with say_dissolve
    _mc ma bi "Look at her. She’s hardly even focusing."
    _mc ea thinking ba mh "How does she manage to thrash me so thoroughly every time?"
    _mc ldown eg ma "It’s an absolute mystery to me. At least I study for my grades..."
    _mc ea mh "Still, doesn’t she look... kind of at peace?"
    _mc ec "More so than I’m used to seeing her, at least."
    show natsuki ma b1d with say_dissolve
    _mc bi "That grin, it’s almost like-"
    show natsuki turned e1a with say_dissolve
    _mc ea ba "Hm?"
    show natsuki e1d mn with say_dissolve
    _mc mf "Is she-"
    show natsuki b3a e3b ma with say_dissolve
    _mc ea bd nb mh "She’s totally winking at me."
    show natsuki e3d with None
    hide natsuki
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    _mc bg mj eb "Ah, shoot! I haven’t been paying attention!"
    _mc bd mh "Crap, where are we up to?"
    _mc ec bi "Dipoles... What? No, that was weeks ago!"
    _mc ea ma ba na "No, wait, here!"
    _mc ec mh "The iron atom acts as a Lewis acid, as it is less electronegative than the Bromine, so it will accept an electron from the Bromine, so the Iron Bromide will then-"
    _mc ea "Eh? She..."
    show bg:
        blur 2.0
    show natsuki turned b1d e1d:
        zoom 0.57 xcenter 0.78 yalign 1.0
    camera master:
        align (0.8, 0.8) zoom 1.5
    with Dissolve(0.2)
    _mc ec bi "Why is she looking at me?"
    show natsuki b3a e3c me with say_dissolve
    _mc ma "Oh. She’s taunting me."
    show natsuki e1a b1a mc lhip with say_dissolve
    _mc eg ba "Well, jokes on you, I have to study."
    show natsuki b2a e1b ldown mn with say_dissolve
    _mc bg eb md "..."
    show natsuki cross e2a b1a mj with None
    hide natsuki
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "I pull a silly face and, as I do, the teacher turns around."
    t "MC."
    mc ea mg nb ba "Y- Yes?"
    t "Do you make a habit of pulling faces while my back is turned?"
    mc bd ml "N- No, Miss, I-"
    t "Hmph. See that you don’t. If I catch you slacking off again, there will be consequences."
    mc ec ba na mf "Yes, Miss."
    "She turns back toward the board, and continues talking."
    show bg:
        blur 2.0
    show natsuki turned b2b e1b mn:
        zoom 0.57 xcenter 0.78 yalign 1.0
    camera master:
        align (0.8, 0.8) zoom 1.5
    with Dissolve(0.2)
    _mc bd nb mh eb "Natsuki!"
    _mc mm "How dare you get me in trouble!"
    show natsuki xd b3a mc nb at hop
    _mc ec bi mh "And now she’s {b}laughing{/b}?"
    show natsuki na e3d with say_dissolve
    _mc eg ma na "Unbelievable!"
    _mc ef mh "Ugh, whatever."
    hide natsuki
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "I roll my eyes, returning to my work."
    _mc "... I’ve wasted too much of the lesson on meaningless nonsense already."

    scene bg school_corridor_1_day with wipeleft_scene
    show amelia turned eb mi at t11
    $ set_date(hour=12, minute=10)

    "As I make my way through the halls looking for Sayori, I accidentally bump into Amelia."
    am mf ec bh "Oh, watch where you’re going, Mel!"
    show amelia md
    mc turned ml nb "Yeah, sorry, I just-"
    am me "Zoned out, again?"
    show amelia md
    mc ef mb "... Yeah."
    am eb mb ba "Do you need to sit down? Let’s find a quiet spot and have lunch together."
    show amelia ma
    mc ea ml "N- No, actually, I was..."
    show amelia md
    mc mg bg na "Sorry, I have plans for lunch already."
    am ef bb mb "Oh, do you? That’s okay then! I’ll just go find something else to do~"
    show amelia ed ba ma with None
    hide amelia
    show bg:
        xzoom -1
    with Dissolve(0.3)
    "She starts to bound off, but pauses and turns around again."
    $ say_transition = True
    $ autofocus.block("amelia")
    show bg:
        blur 2.0
    show amelia turned ed md at i11
    camera master:
        align (0.5, 0.15) zoom 1.5
    with Dissolve(0.2)
    am me "Though..."
    am lup mf "I know you’ve got yourself a club, but I was thinking..."
    am eb mb "For old time’s sake, of course, are you free this afternoon?"
    show amelia ldown ma with say_dissolve
    mc ba ml "Me? Yeah, I suppose."
    am mb "Want to hang out with me?"
    show amelia ma with say_dissolve
    "I think about it for a moment. I’m sure the club would be a little upset if I skipped out on them, but at the same time..."
    am ed me "You don’t have to, of course-"
    show amelia eb md with say_dissolve
    mc mb "I’ll do it. See you after class."
    am me "Wait, really?"
    show amelia ma with say_dissolve
    mc eg "Yeah. I have to make an effort to spend time with my friends."
    mc ef mg "... Now that I have them."
    show amelia ec with say_dissolve
    "She gives me a small smile, and a light elbow."
    am eb me "I’ll catch you after class, then."
    show amelia ma with None
    hide amelia
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("amelia")
    "With a knowing wink, she heads off down the hall."
    _mc ec ba ma "... Hah. Maybe this won’t be so bad, trying to balance people."
    _mc eg "Goodness knows I’m out of practice."

    scene bg class_3_day with fade
    $ advance_date(minutes=5)

    "Relaxing into the chair, I place my lunchbox onto the desk in front of me."
    _mc turned ec "Shouldn't be too long now~"
    "My fingers rap impatiently on the desk as I grin giddily."
    "I'm not quite so sure why I'm in such a good mood, but I'll take it."
    "It only takes a moment for the door to slide open, and then-"
    stop music fadeout 3.0
    show kaito turned eb mf be at l11
    k "Sorry I'm late, Homura, I-"
    k me ba ea "Oh."
    show kaito md
    mc mj bi "Sorry to disappoint, but I'm not your daily squeeze."
    "For some reason, Kaito doesn't meet my gaze."
    k ec me "N- No, actually, Homura's one of my mate's sisters, I was gonna show her around-"
    k mf ee "Wait, why do I have to justify anything to you? It doesn't matter what I say, you'd just-"
    show kaito me at dip
    "He sighs."
    k mf "Ugh, forget it."
    show kaito md
    mc ml bg ea nb "I- I'm almost afraid to ask, but- is everything alright?"
    k ec mc bb "Me? Please, as if-"
    k md "..."
    k ba mf ee "Look, not really."
    show kaito md 
    _mc eg bi mj na "Ah, shit, now he's gonna vent. I didn't ask because I was curious..."

    play music pensive

    k ec mf rhip "Have you... Did you talk to Ellen?"
    show kaito md
    mc ml ec "... I might have."
    k ea ba me "Yeah. I might have underestimated you a little."
    show kaito md rdown
    mc eg mb "What, you're gonna tell me now that you actually care?"
    k bg mc "Me? Please, you know me~ Feelings are for the weak."
    k me bb "But, uh, between you and me..."
    k ec mf ba "Words are a weapon, and it seems you're more inclined to use them than I thought."
    k ee me "So..."
    show kaito ea md
    mc ea bd mg "You came crawling back to apologise?"
    k bg mh "God, you're insufferable. This is why you can't get a man, despite your looks."
    show kaito mg
    mc eb ml nb "Despite my- Are you hitting on me?"
    k ee mh "Fuckin'- No! Just- Shut up for a second, aight?"
    k ea me "I just wanted to say that, I guess I have a little more respect for you now."
    k ba ee mf "I didn't realise you could sway Ellen quite that much."
    k bb ea me "She must really look up to you, for some reason."
    show kaito md
    mc thinking md ed bm na "Maybe it's because I'm not you?"
    k ee mf ba "You know what? Forget I said anything. God."
    show sayori turned md at t52
    show natsuki cross me at t51
    show kaito md zorder 3:
        easein 0.2 xoffset -130
        "kaito turned eb bb md"
        parallel:
            hop
        parallel:
            ease 0.2 xoffset -70
    "He throws his arms up and steps out of the room, practically walking into Sayori and Natsuki as he turns around."
    show kaito at lhide zorder 1
    hide kaito
    "Instead of getting upset, he just wordlessly passes by them as they enter the room."
    n b1d mg e1d "... What the heck was that all about?"
    show natsuki me
    s b1b mg e3c "... They don't like each other."
    show sayori mj
    n b4 e1a mh "Why?"
    show natsuki md
    "Natsuki raises an eyebrow, shrugging nonchalantly."
    n turned b1a e2a mh "He looks harmless enough."
    show natsuki md e1a
    s e2a b1a mh "... Because he had a crush on me when we were kids."
    show sayori md e1a
    mc ldown eb bd nb mg "That's not the reason!"
    show sayori b4 e1d
    show natsuki e3d ma at hop
    "Natsuki chuckles, spurred on by Sayori's reaction to my outburst."
    n mc "Oh, god, that sounds exactly like something you'd do, though~"
    show natsuki e1a ma
    show sayori e1a b1a
    mc ec ml bi na "I hate you both."
    s e1b ml b2a "Nooo~"
    show sayori mk
    n mb e3c b2a "How could we have fallen so far~?"
    show sayori xd nb b2c lup rup
    show natsuki ma
    "Both of them dramatically bring their hands to their heads, Sayori swooning at my statement."
    show sayori ml at t55
    s "The calamity~!"
    show sayori mk
    mc eg mm "I swear to god, both of you."
    show natsuki e3d b3a ma at t21
    show sayori mn b1a e3d ldown rdown na at t22
    "They walk over after having their fun."
    n lhip rhip e1d b1d mb "Yeah, yeah. Careful not to cut yourself on all that edge~!"
    show natsuki ma
    _mc mh "I take it back - They haven't finished making fun of me yet."
    _mc ma "This is going to be my whole lunch now, isn't it?"

    stop music fadeout 2.0
    scene bg school_gate_day with longfade
    $ set_date(hour=15, minute=7)
    play music friendly_endeavours

    "After school, I wait by the front gate for Amelia to show."
    _mc turned ec mh "Part of me does feel bad for ditching the club, but I do spend pretty much every day there these days. It’ll be nice to get away and hang out with Amelia a little more."
    
    window auto hide
    camera master:
        zoom 1.4 align (0.0, 1.0)
        ease 7.0 xalign 1.0
    with Dissolve(3.0)
    pause 4.7
    camera master
    with Dissolve(0.3)
    $ advance_date(minutes=6)

    _mc thinking ea "Where is she? Did she get held up?"
    _mc ec "Hmm. She’s not usually one to be late for anything. I hope everything’s alright."
    am "Heey!"
    show amelia turned ef bb ma rup:
        pos (0.2, 0.1) anchor (0.5, 0.0) zoom 0.75
        matrixanchor (0.5, 0.0) matrixtransform RotateMatrix(0, 0, 40)
        xoffset -700 # yes i used the same code :monikk:
                    # recycling is important
        easein 0.7 xoffset 0
    _mc ldown ea mf "Oh, there she is-"
    _mc bd eb mh "Why is she running {b}toward{/b} the school?"
    show amelia ed bd mb:
        easein 0.25:
            matrixtransform RotateMatrix(0, 0, 0)
            xpos 0.5 zoom 0.8 xoffset 0
            yanchor 1.0 ypos 1.03
    am "I, ehe, totally forgot you were coming~"
    show amelia ma rdown
    "I roll my eyes, shaking my head, all while wearing a grin."
    mc ed md bm "Really? What, did you get halfway home and then turn back around?"
    am mb bc "Maaaybe?"
    show amelia ma
    _mc ec ma ba "Geez, she’s laying the Sayori impression on a bit thick, isn’t she?"
    mc eg mb "And you purport to be the intelligent one."
    am eb ba me "Intelligence does not equate wisdom, and nor does it include common sense."
    am lup ed mb "If you wanted either, you’ve come to the wrong person~"
    show amelia ef ma ldown
    mc md ed "Yeah, yeah."
    "With a chuckle, we start off down the road."

    scene bg school_street_day with wipeleft
    $ advance_date(minutes=15)

    "It doesn’t take us long to get to the fork in the road where we usually split."
    show bg:
        align (0.6, 0.3)
        ease 1.4 zoom 2.2
        ease_quad 1.9 align (0.0, 0.9) zoom 1.7
    "One direction takes us toward my house, the other toward Amelia’s and the city."
    show bg:
        blur 2.0
    show amelia turned ef:
        xcenter 0.75 zoom 1.15
        ypos 1.0 yanchor 0.76
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("amelia")
    "Amelia smiles as she drags me down the left path, almost cackling as she does."
    _mc turned ec mh "... Part of me wonders if I should be concerned about what she has in store."
    _mc ea ma "Still, it is what it is. What’s the worst that could happen?"
    show amelia ea with say_dissolve
    mc mg "So... What’s the plan?"
    am me eb "We..."
    show amelia ma with None
    show amelia at i11
    show bg:
        blur 0.0 zoom 1.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("amelia")
    am ef mb "Are going shopping!"
    show amelia ma
    _mc mh "... Shopping?"
    _mc thinking ec "Different."
    _mc ma "Can’t say I was expecting that, to be honest."
    am ba eb me "C’mon! Don’t be a slow poke!"
    show amelia ma ef with None
    show amelia:
        xcenter 0.75 zoom 1.15
        ypos 1.0 yanchor 0.76
    show bg:
        zoom 1.7 blur 2.0
    with Dissolve(0.2)
    "She keeps dragging me until I finally catch up with my pace to match her own."
    mc ed md ldown "Okay, okay! I getcha~"
    hide amelia 
    show bg:
        zoom 1.0 blur 0.0
    with Dissolve(0.2)
    "Finally, she lets me go, and we start walking down the road together."
    
    stop music fadeout 1.5
    scene bg mall_int_2_afternoon
    camera master
    show amelia turned:
        matrixcolor TintMatrix("#ffecdb")
        i11
    with Fade(0.7, 0.2, 0.8)
    $ advance_date(minutes=58)
    $ set_internet(True)
    pause 0.05

    camera master:
        align (0.0, 0.4) zoom 1.7
    show amelia:
        blur 0.0
        linear 0.4 blur 3.0
    with Dissolve(0.3)
    $ say_transition = True
    $ autofocus.block("amelia")
    am eb me "So... See anything you like?"
    show amelia ma with None
    camera master:
        align (1.0, 0.5) zoom 2.0
    show amelia:
        blur 4.0
    with Dissolve(0.2)
    mc turned ec ml "Well..."
    show amelia:
        blur 0.0
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    play music childlikesmile
    am mb bb "How about a puppy?"
    show amelia ma rup with say_dissolve
    "She points at a passerby walking their dog."
    am mb "Imagine if you got one to keep you company at home?"
    show amelia ma with say_dissolve
    mc ef mj "I, ah, well..."
    am ed ba mb rdown "C’mon, wouldn’t it be great?"
    show amelia ma with say_dissolve
    _mc ec mh "... It probably would be really nice to have some company, but..."
    show amelia ea with say_dissolve
    _mc ea "At the same time, it would be expensive to keep one, and my budget is tight as is."
    am eb me "Well?"
    show amelia md with say_dissolve
    mc ef ml "Amelia, I..."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    mc ea mg "That’s not the sort of decision you make on the fly."
    $ autofocus.unblock("amelia")
    am ed me "Yeah, but..."
    show amelia mg
    mc mb "I’ll think about it, I promise."
    am me "Alright..."
    show amelia lup md
    "She looks away, dejected."
    _mc ec mh "I feel a little bad, but I really don’t want to make my life any harder than it already is."
    _mc ea "Besides, I have no idea what I’m doing once I graduate. If I end up continuing the plans Sayori and I made as kids, we’ll be moving to Tokyo, and we won’t have the chance to keep a pet."
    _mc eg bi mm "Dammit."
    mc ea mb bg "Sorry, Amelia, I didn’t mean to snap-"
    am ea me "Hm? Nah, it’s cool. You’ve got your reasons."
    am eb ldown mb "Wanna actually get some shopping done, then?"
    show amelia ef ma
    mc ba "Sure. What did you have in mind?"
    am eb me "I was actually wondering if you’d help me pick out some outfits. I’ve been itching to get something new lately."
    show amelia ma
    mc thinking mg "Really? I mean, I don’t have the strongest fashion sense-"
    am ec me "No, but you do have one hell of an eye for when something doesn’t look right."
    am ee mf "Besides, I’m not after trends, just something I can wear out."
    am eb me "Maybe a little jewellery too..."
    show amelia md
    mc ed md "Feel like dressing up for someone, do we?"
    am ed bd mb "N- No, don’t be ridiculous. I’d never dress up for anyone that isn’t you~"
    show amelia ef bb ma
    "She winks at me, grinning."
    mc ldown bm "Uh-Huh."
    _mc ec ma ba "Good recovery, Meelz."
    _mc eg "She knows how to give it as well as she takes it, that’s for sure."

    scene bg jewellery_store with wipeleft_scene
    $ advance_date(minutes=6)

    _mc turned thinking mh "I wonder what she had in mind?"
    show amelia turned ed md:
        i41
        xoffset -50
    camera master:
        align (0.0, 0.2) zoom 1.4
    show bg:
        blur 1.5
    with Dissolve(0.2)
    "She’s over looking at bracelets now, but she’s been all over the store."
    camera master
    hide amelia
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "I find myself, oddly enough, transfixed on the hairpins."
    camera master:
        align (0.5, 0.5) zoom 1.3
    show bg:    
        blur 2.0
    show expression "mod_assets/MPT/melody/turned_hairclip.png" as gawrgura: # a
        crop (537, 190, 62, 33)
        align (0.5, 0.4) zoom 4.0
    with NonBlockingDissolve(1.0)
    _mc ldown ec "Not quite sure why, if I’m honest, but this small one with a small shark on it strikes me."
    _mc eb ma "It’s just... oddly adorable?"
    _mc ec "Strange thing to say about a shark, I guess."
    camera master
    show amelia turned md at i11
    hide gawrgura
    show bg:
        blur 0.0
    with Dissolve(0.2)
    am eb me "Hey! Whatcha looking at?"
    show amelia md
    mc ml nb ea "Oh, nothing in particular..."
    am ea me "The shark one, right?"
    am eb mb "Have you considered going into marine biology?"
    show amelia ma
    mc ml na "Huh? No, I’d never even thought of it."
    am ed lup me "Well, that’s an option. That or zookeeping."
    show amelia md
    mc ef mb "Zookeeping... Sounds like fun, actually."
    mc ea mg "You’re gonna pursue your streaming career, obviously?"
    am ldown ec mb "Not a doubt in my mind~"
    am eb me "Though, if that falls through... Maybe something like a private investigator?"
    show amelia md
    mc eb bd ml "Huh? Aren’t those two things like..."
    am mb bb "Complete opposite ends of the spectrum? Absolutely."
    am ba me rup "But, honestly... that sorta sums me up, doesn’t it?"
    show amelia ma
    mc ed md ba "True. You’re one of extreme opposites."
    am ec mb rdown "Nothing like you, who obstinately sits in the middle."
    show amelia ma
    mc ef mf "Well..."
    stop music fadeout 4.0
    show amelia ea md
    mc mg "It’s not like I’m indecisive, just..."
    am ed me "I know. You’ve been forced to make decisions, and it’s not really been much of your choice."
    am eb me "Maybe that’s just your body telling you it wants to take it easy."
    show amelia ma
    mc ea mf "You think so?"
    am ed lup me "Better than some people. Imagine how... I dunno, someone like Monika feels. I doubt she’s been allowed to make a decision in her life."
    am ee mf "And then there’s you, with all the choices in the world, and that’s made you always try to pick the option in the middle."
    am ldown ea me "You’re scared of change."
    show amelia md
    mc ef mh "..."   
    
    play music myfeelings

    mc ml "I always have been. It just..."
    show amelia bd
    mc ea bg mg "Scares me. The idea that every day, I’m making uninformed decisions that might change my entire future."
    am rup mb "... Jesus, man. You doing okay?"
    show amelia ma
    mc bi ef "... Yeah. I’m okay. Just a little, well-"
    show amelia ee mc
    mc ea ml bf "Rattled."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    "She bites her lip, placing a hand on my shoulder."
    am bc ea mb "I know I joke about it, but... I am here to help, you know?"
    show amelia ma bd with say_dissolve
    mc eg bg mb "I know. I don’t really understand why, but I know."
    am mb "Because you’re someone special. Whether you realise it or not, you’ve made an impact on the people around you."
    show amelia ma with say_dissolve
    mc ea "... Thanks, Meelz. I appreciate it."
    mc ba mg "By the way... you’re not... coming onto me, are you?"
    show amelia mi bc rdown
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "Her face flushes as she backs up."
    $ autofocus.unblock("amelia")
    $ say_transition = False
    show amelia ed mb bh
    am "Me? H- Hah, in your dreams!"
    show amelia ma
    mc ed md "If this was my dream, this conversation would have gone a whole lot differently..."
    show amelia ea
    show bg:
        blur 1.0
    camera master:
        align (0.5, 0.2) zoom 1.2
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    "I advance toward her as she backs off, matching her stride."
    am ec mb "H- Haha, Mel, funny-"
    show amelia bb md with None
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    mc mg ea "Oh, you think I’m joking?"
    show amelia bb eb mi
    show bg:
        blur 2.5
    camera master:
        align (0.6, 0.2) zoom 3.0
    with Dissolve(0.2)
    "Moving right up to her ear, I whisper."
    mc eg mb "Because I am."
    show amelia bi ec mg 
    show bg:
        blur 0.0
    play sound smack
    camera master at vpunch
    stop music
    "And I receive a well-deserved sock to the gut in return."
    $ autofocus.unblock("amelia")
    $ say_transition = False

    play music daijoubu

    am mi "Jackass."
    show amelia mg
    mc ed md "That's me~ It's why you love me~ I've got all the right curves~"
    show amelia ee at t11
    "I turn away, waving seductively in her direction."
    am ed mb bh "Pff, as if. Everything you’ve got, I’ve got too."
    show amelia ma
    mc eh "But not quite like mine~"
    _mc ec ma "Alright, Mel, that’s enough. Let her off the hook this time."
    show amelia ba ee me at dip
    _mc eg "God, that was a load off my chest, though."
    show amelia md
    _mc ec "Sometimes, it’s nice to just unload all the tension in you through ferociously flirting with someone and watching them squirm."
    show amelia ed at thide
    hide amelia
    _mc eb bd mh "... Am I a sadist?"
    mc ml bg ea "Hey, Meelz, I’m sorry, that was-"
    _mc mh bb ea "Eh?"
    _mc ec ba "She’s not behind me anymore."
    _mc ea "Over at the counter? Is she buying something?"

    #[Full Voice Acting]
    show amelia turned ee bi md at t11
    am "Aww, dammit..."
    show amelia md
    mc ea mg ba "What’s up?"
    "I hear her curse under her breath as I stride over to her."
    am ba me "I forgot my wallet..."
    show amelia md ed
    mc ml "Oh? What were you-"
    show amelia eb mi
    mc mb "Ah, did you like the shark pin too?"
    am ed mb bd "N- No, actually, I was going to buy it for you."
    show amelia ma
    call blink(0.3) from _call_blink_13
    "I blink a couple times, a little confused."
    mc thinking ec bi ml "Weren’t we here to help {i}you{/i} shop?"
    am eb me ba "Well, yes, initially. Come to think of it though, that might be a little hard to do without my wallet, won’t it?"
    show amelia ma
    mc ldown ef ba mf "Ah, true."
    show amelia md
    "I place some coins on the desk and pick up the shark pin, clipping it into my hair."
    $ auto_mel_hairclip = True
    mc ea mb "How’s this?"
    "The clerk, a young woman, probably not much older than us, gives me a nod and sees us off."
    am ed bd me "B- But I..."
    show amelia md
    mc mh "Hm?"
    am ef bb mb "No, never mind. It looks good."
    show amelia ma eb ba
    mc eh md "Thanks!"
    "I can’t wipe a smile off of my face. I suppose Sayori’s been rubbing off on me."
    _mc ec mh "Rubbing..."
    _mc eg bi mm nb "Ah! Melody, what are you thinking?"
    am mb "C’mon, let’s keep going. I reckon we should go to the arcade next!"
    show amelia ma
    mc eb bb mf "Eh?"
    "She drags me outside the complex, while my heart desperately tries to calm itself after that sudden stunt."
    mc ea ml ba "But you don’t have your wallet-"
    am ec me "Dude, I’m a regular! They’ll just put it on my tab!"
    am eb mb "Come on, stop complaining!"
    show amelia ef ma
    "Her grin wears me down. Best to comply, I suppose."
    _mc ec ma ba na "... I’m so far from the person I was when I first met this girl."
    _mc eg "She’s really made something of me, hasn’t she?"

    stop music fadeout 1.0
    scene bg arcade2
    show amelia turned md eb at i11
    with wipeleft_scene
    $ advance_date(minutes=11)
    play music arcade

    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    am bb eb me "Wouldja look at all this stuff..." # im stuff
    am ba ee mf "I swear, every time I come here, they’ve added something new, or changed something up."
    am eb mb "Sure, maybe some people don’t like the feeling of changing things out all the time, but I sure do! Never gets stale, here!"
    show amelia ma ea with say_dissolve
    mc turned mg "You’d be right about that... Woah, is that a-"
    am ef mb "Genuine DDR? Sure is."
    am eb rup "And behind it, along the wall?"
    show amelia ma with say_dissolve
    mc eb bb mb  "A 1948 Triple Action pinball machine? That thing belongs in a museum!"
    mc ba ea "Look, the flippers face outward, rather than inward!"
    mc eh md "I’ve never seen one of these in person before!"
    am mb "Right? The boss here loves antiques. It’s a shame it’s only a replica, but could you imagine how delicate an almost seventy-year-old pinball machine would be?"
    show amelia ma with say_dissolve
    mc bg ml ea "Oh... It’s a replica."
    am ed mb "The good news is, though, that you can actually play it, {i}because{/i} it’s a replica. They sure as hell wouldn’t let you touch an original."
    am ea me "Though, I have to say, I’m surprised you knew about something like that."
    show amelia rdown ma with say_dissolve
    mc ef mb bg "I..."
    _mc ec bi mh "Oh man, whatever you do, don’t let her know you’re more of a nerd than she thought you were!"
    mc ea ml ba "Like old stuff?" # im stuff
    am ec mb "Mhm. Sure, tiger. You can’t hide your nerdiness from me. I’ll bet you spent months of your life in here as a kid, right?"
    show amelia ef ma with say_dissolve
    mc ef mf "... You got me."
    _mc ec ma "It was the best place for Sayori and I to come to after school, after all. Because of how open-plan it is, and how strong the security is here due to all the antiques, we were safer here than out on the streets."
    _mc ef mh "And whenever we didn’t want to be home..."
    _mc ea ma "It was either here or the beach."
    _mc mh "Or the grove. Or the park."
    _mc eg ma "We really had a lot of special places, didn’t we?"
    $ say_transition = False
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("amelia")
    am eb me "So, do you want to give it a go?"
    show amelia ma 
    mc ea mb "Do I? Hell yes I do!"
    show amelia ea at dip
    "Amelia hands me a token, which I push into the slot. A couple of sounds and lights flash, but nothing so sophisticated as a modern machine."
    "Grinning to myself, I launch my first ball. Time to relive some old memories."

    scene bg arcade2
    show arcade_silhouette_1 at i41
    show amelia turned eb bh md at i42
    show goobi at i43
    show arcade_silhouette_2 at i44
    show black:
        on hide:
            alpha 1.0
            linear 3.0 alpha 0.0
    with fade
    $ advance_date(minutes=17)

    "By the time I finally lose my last ball, I can feel a stunned silence."
    hide black
    "Apparently, I’d drawn something of a small crowd."
    camera master:
        align (0.25, 0.2) zoom 1.7
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    am me "Are you... some kind of arcade goddess? All this time, were you going easy on me?"
    show amelia md ec with say_dissolve
    mc turned ml "Huh? No, I just-"
    show amelia ba ea with say_dissolve
    mc mb "Pinball was always the thing I’d play, as a kid."
    am me "... When was the last time you played?"
    show amelia md with say_dissolve
    mc thinking mg "Uh... Probably about five or six years ago? Maybe more?"
    am ee me "... I’m in the presence of a deity."
    am ef mb "A bonafide empress of pinball."
    show amelia ma with say_dissolve
    mc ldown ef mf  "Oh, no, it’s really nothing-"
    show amelia ea with say_dissolve
    mc ea mg "Wait, is that the high score?"
    mc eb bd ml "... By an order of magnitude?!"
    show amelia ec md with say_dissolve
    mc eg bi mb "Geez, you all suck!"
    mc ea bb mg nb "I, ah, mean-"
    show amelia ea ma with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False 
    "Suddenly realising just how many people were around me, I stagger back a little."
    _mc ec mh ba "I’m feeling... extraordinarily crowded."

    scene bg arcade2 with fade
    $ advance_date(minutes=14)
    $ autofocus.unblock("amelia")

    "After a couple minutes of answering questions from the twenty-odd people that had been watching me play for, apparently, almost an hour on a single game of pinball, I finally get some peace."
    "Amelia’s left to visit the bathroom, leaving me with a bottle of water on one of the comfortable sofas."
    "Honestly, I’m a little exhausted. Sure, I deal with questions and the like at work, but there’s a bench between us."
    _mc turned bg eg na "Too many people, too close."
    who "Um, excuse me-"
    "A small voice appears, dragging me out of my thoughts."
    show leo at t11
    mc ea ba ml "I told you lot, I’m not answering any more- Huh?"
    "A small boy, maybe seven years old, tugs gently on my skirt."
    l "I, um..."
    l "I lost something."
    l "C- Can you... help me find it?"
    mc thinking mg "Oh, well... I suppose I can help you look? What was it?"
    l "Um..."
    l "It’s small, and round, and, um..."
    show leo at hop
    l "It looks like this?"
    "He holds up a token used by the arcade."
    mc mb ldown "Oh, you lost a token? Don’t worry, those are easy to replace."
    l "N- No, it was like that, but not. Mummy said it was really important and I shouldn’t lose it, but I did..."
    mc bg "Okay, it’s okay, I’ll help you look."
    show amelia turned eb mb at t21
    show leo at t22
    am "Hey, what’s going-"
    show amelia mi at hop
    mc mj eb bf nb  "Ahh!"
    show amelia ma ed bd
    mc bg eg mb "Geez, Meelz, you startled me!"
    "Amelia, who wandered up behind me, evidently jumped at me jumping at her."
    am rup eb me bb "Huh? What? No, I was asking-"
    show amelia md
    mc ea mg ba na "Eh? Oh, the kid’s lost something and wants a hand finding it."
    am rdown ef ba mb "Oh! Well we can definitely help with that!"
    show amelia ma
    mc ec ml "I mean, I wasn’t gonna like, dedicate my whole-"
    show amelia ec bh mg
    "She glares at me."
    show amelia ea ma ba
    mc eg mg "Fine, fine. We’ll help find the thing."
    l "Ya-ay!"
    am eb me "So, what’s your name, little guy?"
    $ leo_name = _("Leo")
    show amelia md
    l "Leo!"
    mc thinking ml ea "Leo? That’s not a common name around-"
    show amelia mc ec bh at dip
    play sound slap
    extend bg mm eh ldown " Guh-"
    "Amelia elbows me in the ribs."
    am ea ba mb "I see! Well, Leo, what does it look like?"
    show amelia ma
    show leo at hop
    l "It, um, looks like this!"
    am eb me "Oh, a token? If you lost a token, you can just have one of mine-"
    show amelia md
    l "No, no, like that, but not!"
    am bb mb "Ahh, I see! An actual coin, then?"
    show amelia ba ma
    l "Mhm!"
    "He nods in approval."
    am ea mb "Alright! Where did you last see it?"
    show amelia ma
    l "Um..."
    if preferences.language is None:
        $ auto_advance_date_mult = 1.33
    show black onlayer above_master with {"above_master": Dissolve(2.0)}:
        alpha 0.75
    "He thinks really hard to himself. Part of me wants to make a joke about smoke coming out of his ears, but that would be mean."
    show amelia md
    _mc ec ma ba na "... I suppose me thinking about making the joke means I made the joke, though, doesn’t it?"
    show amelia mg bh ec
    _mc ea mh "... Are our minds even real? What is real? Or is what we consider reality just a figment our our imaginations in the first place-"
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    am me "Mel! Focus!"
    show amelia md 
    hide black with {"above_master": Dissolve(0.5)}
    mc ml bb nb "Huh? What? Where am I?"
    am eb mb ba "Have your existential crisis later, we have to find a coin!"
    show amelia ma at dip
    "She pulls me by the arm, flashing me a smile."
    if preferences.language is None:
        $ auto_advance_date_mult = 1.5
    _mc ec ma ba na "... She’s lucky she’s been the only friend I’ve had all this time."
    show amelia eb me
    _mc mh "If I’d had options... well..."
    show amelia md
    _mc eg ma "Yeah, I’d probably still have stuck with her. Maybe?"
    show leo at hop
    show amelia ma
    _mc ea "Eh. Life’s full of twists and turns."
    show amelia md ee bh
    _mc ec mh "Who knows where it’ll lead next?"
    show amelia ea me ba
    _mc ea ma "Oh, right, the coin. I really should focus on that, hey?"
    show amelia eb mb
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    "Before my eyes, I watch Amelia discuss the details with the boy, then start rapidly narrowing down the possible locations."
    am me rup "So, it should be somewhere in this corner of the store, most likely around these two machines here."
    show leo at hop
    show amelia ma ef rdown
    l "Okay!"
    show amelia ea
    "She’s even managed to cheer the boy up, and now tasked him with earnestly searching for the coin alongside her."
    "Oh, right, I should help too."
    _mc ec ma "... I guess I was a little busy admiring how quickly she jumps into serious mode."

    stop music fadeout 2.0
    scene bg am_house_afternoon with Fade(1.0, 0.2, 1.0)
    $ set_date(minute=50)
    play music a_sunshine

    _mc turned ec mh "And here I am, waiting."
    _mc ea ma "She won’t be long; just gonna run in and get some stuff organised." # im stuff
    _mc ef "I don’t really mind; it’s a quiet part of town."
    _mc eg "Nice and relaxed."
    _mc ec "A couple old people have passed by, but that’s about it."
    _mc ea "Oh hey, there’s a boy with white hair over there; he looks kinda like an anime protagonist."
    _mc eg "Hah. Imagine being an anime protagonist. Man, that would suck, being dragged from place to place, lacking any real agency."
    _mc mh "Sometimes, I’m a little glad I’m just me."
    _mc ec thinking "Though, I dunno. Maybe I wouldn’t mind going off on an adventure somewhere."
    _mc ea "I mean, I haven’t had a holiday in... years."
    _mc ef "Since they left me, I suppose."
    _mc eg ldown "Couldn’t afford to, and didn’t have the ability to do so anyway."
    _mc bi ma "I mean, who’s going to accept a booking for a hotel from a fourteen-year-old? That would look extraordinarily suspicious."
    _mc ec ba mh "... I guess, sometimes, we all crave something a little different."
    _mc ea ma "Still, it’s not all bad, being here."
    _mc mh "And hell, if Sayori and I follow our childhood dreams and move to Tokyo for university, I think..."
    _mc eg ma "That would be an adventure, enough for me."
    play sound phone_notification
    phone register "mc_s":
        time auto True
        "s" "When you get home, can you drop by? There’s something I want to talk about"
    mc ea mf "Hm?"
    "I retrieve my phone from my pocket and check my messages."
    phone discussion "mc_s":
        pause
    "I furrow my brow."
    _mc bi ec mh "Well, if that ain’t ominous..."
    "I shrug off the odd feeling it gives me and respond casually. I doubt she intended it to come across that way; if it were urgent or important, she’d have called me."
    phone discussion:
        "mc" "Sure, I can do that, but I’m not sure what time I’ll get home as I’m out for dinner"
        "mc" "Is it urgent?"
        "s" "No, not urgent, just"
        "s" "It’s fine, we’ll talk about it tomorrow"
        "mc" "Aight, if you’re sure"
        "s" "Yep! Enjoy your night!"
    phone end discussion
    "I slide my phone back into my pocket."
    _mc eg ba mf "I swear, that woman is an enigma."
    am turned ec mb "Lost in thought again?"
    show amelia eb ma:
        matrixcolor TintMatrix("#f5d5b6")
        t11()
    "I chuckle."
    mc eg mb "It’s my favourite pastime."
    am mb ed lup "You’re such a dweeb~"
    show amelia ma
    mc ed md "Only because you make me look like better company comparatively~"
    show amelia ee ldown
    "Shaking her head, Amelia grins, before tapping my shoulder and racing down the road."
    show amelia eb mb rup at dip
    am "Tag!"
    show amelia ef bb ma rdown at lhide
    hide amelia
    mc bd ea mg "What are you, five?"
    am turned ef bb mb "Seventeen, but close!"
    "It’s all I can do to chase after her."
    _mc ec ma ba "God, she can be a handful."

    scene bg restaurant1_night with wipeleft_scene
    $ set_date(hour=18, minute=30)
    pause 0.3
    camera master:
        align (0.0, 0.2) zoom 1.4
        ease 7.0 align (1.0, 0.8)
    with Dissolve(1.0)
    pause 6.9
    camera master
    with Dissolve(0.3)

    _mc turned mh "This is new."
    $ autofocus.block("amelia")
    $ say_transition = True
    am turned ec mb "Now, I know what you’re thinking. 'This is new', right?"
    show bg:
        blur 1.5 align (0.8, 0.8) zoom 1.3
    show amelia ma:
        xcenter 0.23 zoom 1.3
        ypos 1.0 yanchor 0.7
    with Dissolve(0.2)
    "I roll my eyes."
    am ef mb "That’s what I thought! So, what better place to go to than somewhere we’ve never been before?"
    show amelia ma with say_dissolve
    mc mg "I mean, the place has been here since... I think since before I started living here, I’ve just never gone."
    am ed me "Neither have I! I can’t explain it, but... I guess it didn’t really strike me."
    am eb mb "But tonight, that ends!"
    show amelia ma ef with None
    show bg:
        align (1.0, 0.5) zoom 1.5 blur 2.0
    show amelia:
        zoom 1.35 xalign 0.5
        yanchor 0.67
    with Dissolve(0.2)
    "She chuckles, sitting back down in her seat after standing up for her big line."
    mc bd mg "You’re gonna get us kicked out before we can even order, dude."
    am bh ec mb "Nah, just you wait! If I wanted to get us kicked out, there’s a whole host of things I could do."
    show amelia ma with say_dissolve
    mc ml ec bi "... Do any of them {i}not{/i} involve run-ins with the police?"
    am ee md bi "Hmm..."
    am eb bb mb "Nope!"
    show amelia ba ma with say_dissolve
    mc eg mf ba "Didn’t think so."
    _mc ec ma "Never does anything by halves, this girl."
    show bg:
        zoom 1.0 blur 0.0
    show amelia at i22
    with Dissolve(0.3)
    "As we settle back into our seats, a waiter approaches us, preparing to take our order."
    show amelia ed md at t11
    "After they take our order, the two of us are left in relative silence."
    show bg:
        blur 2.0 zoom 1.5
    show amelia:
        zoom 1.35 xalign 0.5
        yanchor 0.67 ypos 1.0
    with Dissolve(0.2)
    #[Full Voice Acting]
    am me ea "Hey, so..."
    am ed "I’ve been thinking."
    show amelia ec md bh with say_dissolve
    mc ea ml thinking "Did it hurt?"
    am me "That’s my line!"
    show amelia md with say_dissolve
    "Now it’s my turn to chuckle."
    mc ldown ed md "So, what have you been thinking about?"
    am ed me ba "Well..."
    am eb mb "You know how ducks have wings, right?"
    show amelia md with say_dissolve
    mc ml ea "... Yes?"
    am mb "And their wings cover their backs?"
    show amelia ma with say_dissolve
    mc bi ec mj "This is going to be unbelievably inane, isn’t it?"
    am me "Well... why do we say, 'water off of a duck’s back', when really, it should be 'water off of a duck’s wings'?"
    show amelia ma with say_dissolve
    mc eg mg "... Amelia, that is quite possibly the most stupid thing to have ever left your mouth."
    am ee mb bi lup "... And I’ve had Kaito in there..."
    show amelia ma with say_dissolve
    mc ed md thinking ba "Oooh, self-burn. Those are rare."
    show amelia bd ed ldown with say_dissolve
    "She scrunches her face and looks away."
    mc ldown ml ea bg "Ellen?"
    am ldown ba ee me "... Yeah."
    show amelia md with say_dissolve
    mc ea mg ba "What’d she do?"
    am me "She, well..."
    am ed "Broke up with him, yesterday. After what you said."
    show amelia md with say_dissolve
    mc bb nb "Wait, really?"
    am eb me "Yeah. I don’t know why, but she really listens to you."
    am ed bd mb "I mean, she listens to me, too, but..."
    am me ba "It’s not the same."
    am eb "But he didn’t take it well."
    show amelia md with say_dissolve
    mc ef bi mf na "I could imagine."
    mc eg mg "Geez, what’s that dude thinking? Dating someone younger than him, especially the younger sister of-"
    show amelia bh ec with say_dissolve
    "Amelia shoots me a look to indicate 'change the subject'. I comply."
    show amelia ba with say_dissolve
    mc ef ml ba "I dunno. Just like... people are weird."
    am ed lup me "Sure are."
    show amelia md with say_dissolve
    "An awkward silence ensues."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc ef mh "I know she doesn’t really like talking about Kaito, but... she never really told me why."
    _mc ea thinking "Was their breakup really that bad?"
    _mc ec bi mh ldown "No, this is Kaito we’re talking about. He absolutely did something awful."
    _mc ea bg "Still, it makes me worry. What could he have done to Sayori, all those years ago? What will he do to Ellen, now?"
    _mc ef "She’s a good kid. I’d hate to see her hurt."
    hide black with NonBlockingDissolve(0.2)
    mc ea mb bf "She’ll be alright, Meelz. She’s got you, remember?"
    am ee me "... I know."
    am ed "But you don’t have a younger sister. I guess it’s hard to really understand, without that frame of reference."
    show amelia md ldown with say_dissolve
    mc eg bg mb "Even if I don’t, I still can sympathise."
    show amelia ma with say_dissolve
    mc ef bi ml "I just think about how upset I’d be if someone hurt you."
    am bh mb ee "Hurt me? Hah, please. I’m like the terminator."
    am ef ba "Skin tough as iron and a will of steel."
    show amelia ma with say_dissolve
    mc ed md ba "Which is all well and good until someone comes through with a blowtorch."
    am ed mb "Or a solid knifing~"
    show amelia ma with say_dissolve
    "She chuckles, but for some reason I can’t bring myself to laugh."
    stop music fadeout 4.0
    play ambient int_night fadein 5.0
    _mc ea mh "I’m not sure. Something about this place feels..."
    show amelia eb ma with say_dissolve
    mc mg "Hey, did it get colder for you?"
    am me "Hm? No?"
    show amelia md with None
    hide amelia
    show bg:
        blur 0.0 zoom 1.0
    with Dissolve(0.3)
    "I stand up, looking around."
    "Nothing seems out of the ordinary."
    "Nothing, that is, except-"
    _mc bd mh thinking "Pink?"
    _mc eg bi ma "Maybe I am just crazy, and should enjoy the night I’m having."
    _mc ec mh ba ldown "... Yeah. I’m getting too wrapped up in my own fantasies."
    am turned bd me "Hey, you alright?"
    show amelia md at t11
    mc ef mg "Yeah. Just... I dunno, a little on edge today."
    show amelia turned rup ma with None
    show bg:
        blur 2.0 zoom 1.5
    show amelia:
        zoom 1.35 xalign 0.5
        yanchor 0.67 ypos 1.0
    with Dissolve(0.2)
    "She places a hand on my shoulder, gently pushing me back into my seat."
    am mb "Everything’s fine. I’m here, remember?"
    am bb ef rdown "And I won’t let anything happen to you~"
    show amelia ma with say_dissolve
    "She taps my nose with her finger to both emphasise her point and make fun of me."
    mc ed md "Yeah, yeah. I getcha."
    am eb ba mb "Now c’mon, let’s enjoy our food, yeah?"
    show amelia ma ea with say_dissolve
    mc ea mb "Sure."
    "And with that, we settle in for the evening."
    #[End Voice Acting]

    stop ambient fadeout 2.0
    scene bg city_street_night_off:
        blur 2.0
    camera master:
        align (0.7, 0.4) zoom 1.5
    show amelia turned eb:
        matrixcolor TintMatrix("#4a4ea2")
        xcenter 0.45 zoom 0.75 ypos 1.03 yanchor 1.0
    with wipeleft_scene
    $ set_date(hour=20, minute=59)
    $ set_internet(False)
    play ambient ext_night fadein 1.0

    "We find ourselves wandering home after our meal."
    _mc turned "It was an alright dinner, nothing spectacular."
    _mc ec "If anything, we both felt a little vindicated in having not gone before."
    _mc eg "Even so, it doesn’t detract from how much fun we’ve had today."
    am ea me "So..."
    am eb mb "It got pretty late, didn’t it?"
    show amelia ma with say_dissolve
    mc ea ml "Sure did."
    am ed lup me "Might be a problem getting home."
    show amelia md with say_dissolve
    mc mg "Nah, there’s two of us. We should be okay."
    mc ed ml "Wait."
    _mc ec bi mh "No, she’s right. Sure, {b}one{/b} of us would get home alright, but the other?"
    _mc ea ba "This late on a Thursday? That’s asking for trouble."

    #[Full Voice Acting]
    mc ef bg mj "Ah."
    am bd mb "Yeah..."
    am ldown ee me "Did you wanna..."
    am eb ba "Crash at my place tonight?"
    show amelia md with say_dissolve
    mc ea ba mg "Why yours?"
    show bg:
        blur 1.5
    camera master:
        align (0.1, 0.9) zoom 1.3
    show amelia:
        xcenter 0.63 yanchor 0.9 zoom 0.78
    with Dissolve(0.3)
    am mb "Well, first off, it’s closer, and second, we can get there by following main streets. We don’t have to walk through some darker ends of town, that way."
    show amelia ma with say_dissolve
    mc ec ml "Both are good points."
    mc ef mf bg "... I don’t want to be a bother-"
    am mf "No, no! I’ll set up a blow-up mattress! You can grab some floor in my room."
    am mb ea "I know that look, Mel. It’s the safest option."
    am ed me "Besides, you can borrow one of my uniforms for tomorrow if you need."
    show amelia md with say_dissolve
    mc ea ml ba "I mean-"
    am eb me "Ellen’s about your size, right? You can use her stuff too." # im stuff
    am mb ed lup bd "... My underwear might be a little big for you."
    show amelia ma with say_dissolve
    "My hands instinctively reach toward my chest, but I force them back down. I shouldn’t be jealous."
    mc bg ml ea "W- Wait, no, I don’t need to-"
    am ed ba me "It’s a hell of a long way out of your way to go home and then to school in the morning, right?"
    show amelia ma with say_dissolve
    mc ef mf "... It is."
    am me "So just... be practical."
    am ed mb "Everything’s clean. At least, my stuff is." # im stuff
    am ee me ldown "No promises about Ellen."
    show amelia ma with say_dissolve
    "She chuckles to herself, which unfortunately, does nothing to reassure me."
    am ea mb "Nah, but for real; if we put your clothes on the wash tonight, and get up early to dry them, they should be fine to wear. Just borrow one of my shirts to sleep in."
    show amelia ma with say_dissolve
    mc ed md ba "See, that’s a more practical solution."
    mc ea mb "Wish you’d had led with it."
    am lup ed mb "Ah, but my dear Melly~"
    show amelia ma with say_dissolve
    mc ec bi mf "Don’t call me that-"
    am ef mb "Where’s the fun in that?"
    show amelia ma with say_dissolve
    "She cuts me off, continuing her joke."
    show amelia eb md with say_dissolve
    _mc mh "Only Sayori can call me that."
    _mc eg ma "... I get worked up over the strangest things, don’t I?"
    am ef mb "C’mon, don’t take it so badly."
    show amelia ma ldown with None
    show amelia at i11
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She nudges me, as we continue walking."
    $ autofocus.unblock("amelia")
    am ea mb bd "Geez, you make me feel like I stabbed a puppy sometimes."
    am ed ba me "Or like I said some cheesy one-liner after gouging out someone’s throat, or something."
    am mb bd "Hah, throat."
    show amelia ma
    "I look her way, baffled."
    mc mj "I have literally no idea what goes on in your head, sometimes."
    mc ea ba mg "You have the darkest sense of humour."
    am ef mb bb "Right? Ever wonder if it’ll come back to bite me one day?"
    show amelia eb ba ma
    mc ed md "I’ll bite you."
    am ec bh mb "Oh, don’t threaten me with a good time~"
    show amelia ef ba ma with None
    hide amelia
    camera master:
        align (0.1, 0.9) zoom 1.3
    with Dissolve(0.2)
    "She rushes off down the street, forcing me to play catch-up."
    stop music fadeout 2.0
    #[End Voice Acting]

    stop ambient fadeout 2.0
    scene bg am_bedroom_night_on_closed
    show amelia turned eb at i11
    camera master
    with wipeleft_scene
    $ advance_date(minutes=20)
    $ set_internet(True)
    play music dollaort

    #[Full Voice Acting]
    am ef mb bb "Well, welcome to my abode!"
    show amelia ma with None
    show amelia:
        blur 3.0 xoffset 100
    camera master:
        align (0.3, 0.5) zoom 1.7
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    am lup ed ba mb "The streaming setup is over there in the corner, not that you ever cared to stream with me."
    show amelia ec ma with None
    show amelia:
        blur 0.0 xoffset 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    "I open my mouth to retort, but she grins at me."
    $ autofocus.unblock("amelia")
    am ldown ee mb "Now now, this is no time for platitudes. I’ll get over not having your affections~"
    show amelia eb md
    mc turned mf "Amelia-"
    show amelia bf
    "She frowns."
    am me bg "What?"
    show amelia md bd
    "She throws me a concerned look."
    mc ef bi ml "Look, I think we-"
    mc ea bd mg "We need to talk."
    am eb me bc "Is it about the joking stuff? Sorry, I guess..." # im stuff
    am bd ed mb "I’ve just been feeling a little lonely lately, and I know you can usually take it in stride."
    am eb ba me "So what’s been bothering you?"
    show amelia bc ma
    mc ml bg ea "... It’s just, you’re not usually like this. Teasing, sure, but... All of this stuff?" # im stuff
    am ed bd mb "Like I said, I’ve been lonely, I guess. I, ah..."
    show amelia be mc ee with None
    show bg:
        align (0.9, 0.6) zoom 1.8 blur 1.0
    show amelia:
        xcenter 0.72 zoom 0.95 yanchor 0.92
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    "She sits on the bed, biting her lip."
    am ed bd me "You’re really the only friend I’ve got."
    am eb bc mb "And that friendship kinda..."
    am ec bd "I know you’ve got other people that mean more to you, but..."
    am ed be me "Sometimes it’s just nice to hang around someone that I know cares about me."
    show amelia ma with say_dissolve
    mc mb "Geez, dude, way to lay it on thick."
    show amelia ee bd with None
    camera master:
        xpos 0.5 xanchor 0.72 yoffset -100 zoom 2.0
    show bg:
        blur 1.3
    with Dissolve(0.2)
    "I give her a hug, and she returns in kind."
    mc eg "I’m sorry if I’ve been distant lately. It’s definitely not you, and your efforts to keep up with me aren’t going unnoticed or unappreciated."
    mc ea bf "Thanks, Meelz."
    show amelia ef ba with None
    camera master
    show bg:
        blur 1.0
    with Dissolve(0.2)
    "She chuckles as she lets me go."
    am eb bb mb "See? That’s more like it."
    am ed lup ba "Finally got to your gooey centre."
    show amelia ma with say_dissolve
    mc bi mm eg "Oh, my god..."
    "I roll my eyes."
    am eb me "What? Had to break the hard exterior first."
    am ed mb "I just treated my friendship with you like one of those candies."
    am ec ldown "One day I was gonna get the {i}real{/i} you."
    show amelia ma with None
    show amelia at i11
    show bg:
        blur 0.0 zoom 1.0
    with Dissolve(0.2)
    $ say_transition = False
    "I push her off the bed."
    mc ed md bd "What if the real me was the hard-ass all along?"
    $ autofocus.unblock("amelia")
    am ef mb "Then I was gonna use my saliva to mould that hard-ass into something a little more palatable."
    show amelia eb mi bb
    mc "God, you’re such a weird-"
    "I pause as I notice the flush across her face, along with a sudden flash of surprise."
    am lup ed bd mb "W- Wait, I didn’t mean-"
    show amelia ma
    mc ea ba mf "Mean wh-"
    extend bb mj nb " Ah."
    "The accidental innuendo."

    play music poempanic

    show amelia ldown mi eb bb at hop
    e turned lwaist vest ed mf bg "Oh, just make out already!"
    show amelia mc ed ba at t22
    show ellen mh at t21
    mc eb bd mg "Ellen? How long have you been there?"
    e ea mf "{i}More{/i} than long enough."
    e mb ba ec "C’mon, I’ve got a light meal prepared for you two."
    show ellen ma
    show amelia ma
    mc ba ea na ml "We both already ate-"
    e me ea bg rhip "Are you refusing my cooking?"
    show ellen mh with None
    show ellen:
        alpha 0.0
    show amelia eb
    camera master:
        xalign 0.9 yalign 0.2
        zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    "I throw a glance at Amelia, who’s already recovered."
    am ef mb "Sure, we’ll be right down."
    show amelia ea ma with None
    show ellen:
        alpha 1.0 
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    e ec md bb "And I don’t want to have to remind you, but the wall separating our rooms is paper-thin, so..."
    show amelia bb eb mi
    e bg ea mb lup "I don’t really wanna be feeling the house rocking."
    show ellen ldown ma bg ee at lhide
    hide ellen
    show amelia bi mf rup at hop
    $ autofocus.unblock("amelia")
    am "Oh, my god, Ellen!"
    show amelia ed mc rdown at lhide
    hide amelia
    "She gets up, chasing her little sister down the hall."
    _mc ec ma "... Never a dull moment, eh?"

    $ add_calendar_description(calendar_descriptions["natsuki"][8])

    call week_2_friday_natsuki from _call_week_2_friday_natsuki
    return