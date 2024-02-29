label week_2_tuesday_natsuki:
    call calendar_transition(day=31, hour=7, minute=50) from _call_calendar_transition_19
    scene bg mc_kitchen_day
    with dissolve_scene_full
    play ambient int_day fadein 1.0

    _mc turned thinking mh "Hm. That’s odd. I could have sworn I had quite a bit more in the way of supplies. It looks like... what, two days worth have just vanished?"
    _mc ec "... Was I that hungry? Probably."
    _mc ef "Maybe I eat when I’m stressed, without noticing?"
    _mc ea "Yeah, that seems possible, but have I really been that stressed lately?"
    _mc ec "I suppose social interactions like I have been doing would be pretty far out of the norm for me."
    _mc "Still, odd to think it’s made me stress eat, but the evidence is right in front of me: I have less food than I should. I’ve eaten about the same for the past five years since my parents left."
    _mc ea "So I would know."
    _mc ef ma "... You’d think, at least."
    _mc ldown eg "Ah, it's probably fine. It would only be a problem if it keeps on happening, as my financial budgeting would take a hit."
    _mc ea "As a one-off though, it's far from the end of the world."
    camera master:
        align (0.0, 1.0) zoom 1.7
    with Dissolve(0.2)
    pause 0.5
    camera master
    with Dissolve(0.2)
    _mc "... And there. That’s a list of all the things I need."
    _mc ec "Now to get myself to school."

    stop ambient fadeout 2.0
    scene bg residential_day with wipeleft_scene
    play music ohayou
    $ advance_date(minutes=10)
    $ set_internet(False)

    "..."

    $ autofocus.block("sayori")
    $ say_transition = True
    show sayori turned e2a at i31:
        zoom 0.71 yoffset -55 xoffset -20
    show bg:
        blur 2
    camera master:
        align (0.0, 0.5) zoom 2.0
    with Dissolve(0.2)

    _mc turned mf "Oh, there’s Sayori. I wonder how she got ahead of me."
    mc mg "Sayori, wait up!"
    s e1a me "Hm?"
    show sayori ma at i11
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    "She turns around, surprised to hear my voice, and waits for me."
    $ say_transition = False
    mc "Didn’t feel like walking together?"
    $ autofocus.unblock("sayori")
    s mh "No, it wasn’t that, I just felt like going to school. Didn’t really think too hard about it."
    show sayori md
    mc eg mb "Yeah, I know that feeling. Too used to going on your own, right?"
    s e3d ma "Mhm!"
    mc ea "Well, would you mind walking with me?"
    s e1a mb lup "Not at all!"
    show sayori ma ldown with None
    hide sayori
    show black
    with NonBlockingDissolve(0.5, time_warp=_warper.ease)
    $ advance_date(minutes=4)
    "We head off, practically wordlessly, with a steady and comfortable atmosphere."
    "... At least, it would be a comfortable atmosphere, if I didn’t get the feeling I was being watched."
    show bg school_street_day
    hide black
    with NonBlockingDissolve(1.0)
    "I turn around, half expecting to see Amelia tailing us, trying to catch up."
    "But no, there’s no-one there."
    _mc ec mh "... Weird. Must just be my brain having an off day."
    show sayori turned mg e1a at t11
    s "All good?"
    show sayori md
    mc ea mg "Yeah, just... You ever get the feeling you’re being watched?"
    $ autofocus.block("sayori")
    s "Hm..."
    $ autofocus.unblock("sayori")
    s mb "Nope!"
    show sayori ma
    mc eg mb "Probably a good thing, then."
    s e1d b1d mb "Wanna try and catch whoever’s watching you?"
    show sayori ma
    mc ea ml "That... I mean, it’s probably nothing."
    show sayori e1a mj
    "She frowns."
    s b2b lup mh "If you’re worried about it, we should probably do something."
    s b1a mb "But if it is just a feeling, it should go away, right?"
    show sayori ldown ma
    mc ef mg "True. If I still have it tomorrow, then we can talk about it."
    s mb "Sounds good!"
    show sayori ma
    _mc ec ma "Good ol’ Sayori, knowing when to make me smile."

    scene bg school_corridor_2_day with fade
    pause 0.03
    $ set_date(hour=10, minute=35)

    show natsuki turned nc e1b b3a mm at i11
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.25) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    "As I pass between classes, I practically bump into an excitable lump of pink."
    n e2a b1a mc "O- Oh! Th- There you are! I, I ah, well, I, um-"
    show natsuki mm with say_dissolve
    mc turned ec ml "Slow down a sec, and let the words form."
    n e1a b1d mh lhip rhip "Lunch, roof."
    show natsuki md with say_dissolve
    mc "Sure. I’ll see you there."
    show natsuki e3c ldown rdown nb
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    "She nods, seemingly not willing to risk more confusion with continuing to speak."
    show natsuki e2a b1a at lhide
    hide natsuki
    "Then, she departs, racing off into the crowd."
    _mc thinking ec bi mh "Geez, what’s going on? She’s acting like a teenager with a crush."
    $ autofocus.unblock("natsuki")
    _mc ea ba "No, there’s no way. As far as I recall, she’s older than I am; she’s got to be more composed than that."
    _mc ec "She was probably just distracted, and I’m reading too much into it."
    _mc ldown ef ma "... Either way, it probably would be wise to keep an open mind."
    _mc ec mh "If that possibility exists, I should probably be aware of it to make sure no-one does anything stupid."

    stop music fadeout 2.0
    scene bg school_rooftop_day with wipeleft_scene
    pause 0.1
    show bg with Dissolve(0.2):
        align (0.2, 1.0) zoom 1.4
    $ set_date(hour=12, minute=6)
    play ambient ext_day fadein 2.0

    _mc turned mh "Well, here I am, but..."
    show bg with Dissolve(0.2):
        align (1.0, 0.49) zoom 2.0
    _mc ec "She’s not here."
    show bg with Dissolve(0.2):
        zoom 1.0
    _mc thinking ea "I don’t know what class she had, perhaps it was further away?"
    _mc ldown eg "Ah, not worth worrying about. She’ll get here when she gets here."
    _mc ec ma "... Shows how excited I must have been to get here."
    _mc ea "Still, best to pick a spot and settle."
    show bg:
        align (0.45, 0.0) zoom 1.0
        ease 6.5 zoom 2.0
    scene sky_day at moving_sky with Dissolve(3.0, time_warp=_warper.ease):
        zoom 1.3
    pause 3.0
    stop ambient fadeout 6.0
    scene bg school_rooftop_day with Dissolve(3.0, time_warp=_warper.ease_quad):
        align (0.45, 0.2) zoom 1.7
        ease 3.3 align (0.4, 0.5) zoom 2.5
    $ advance_date(minutes=7)
    "The door cracks open, and a head pokes out."
    show bg:
        zoom 1.0
    show natsuki turned b1c md nd at i11
    with Dissolve(0.2)
    
    play music playwme

    n mg "O- Oh, you’re already-"
    extend cross e3c b3d mi " I mean, yeah, of course you are! It’s not like I was looking for you, or anything!"
    show natsuki mm e1a
    mc turned ed bm mg "Uh-huh. C’mon, sit."
    show natsuki e2a
    _mc ba ec mh "I don’t know why she’s putting so much effort into this tsundere act. Can’t she just act like she’s happy to hang out?"
    _mc ea ma "I don’t particularly mind; she’s a close friend of Sayori’s. If she’s good enough for her, she’s good enough for me."
    "Eventually, she makes up her mind and sits down opposite to me."
    n turned mh nb b1d "I made you lunch."
    show natsuki mj
    mc ml "Like you said you would, yeah."
    n lhip b1a mi "So... You better enjoy it, okay? You should be grateful!"
    show natsuki mj
    mc mb "Sure am."
    mc ef mg "Less work for me to do."
    show natsuki ldown e1a md na
    "I take the lunchbox and crack it open."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc ec mh "Hm."
    _mc ea "I have to admit, it smells... half decent."
    _mc ma "I’ll have to taste it to know though."
    "..."
    _mc ec mh "Well, it’s not offensive."
    _mc ea "I’m pretty sure my cooking, bland as it is, is still easier on the palate."
    hide black with NonBlockingDissolve(0.5)
    _mc "Still though, I don’t think it’s catastrophic by any means."
    n mg "... Well?"
    show natsuki md
    mc eg "Hm."
    show natsuki b3a
    mc ea mg "I’d eat this."
    n mh "Would you?"
    show natsuki b1a mj e2a
    mc ml "I suppose, yeah."
    n mg "... Alright."
    show natsuki mj e1a
    "She says no more until I finish the meal, then quickly snatches it away from me."
    n b1d mh "Don’t make lunch tomorrow."
    show natsuki md
    mc mg "Why?"
    _mc ec mh "Of course, I know why, but..."
    _mc ef ma "Best to ask."
    n e2a mg b1a "Just... don’t."
    n e1a b2b mh "You better not, you hear me?"
    show natsuki mj nb at dip
    "She grabs my sleeve, looking up at me with a surprisingly vulnerable expression."
    mc ml bg ea "Okay, okay, I won’t."
    show natsuki na b1d md
    "And as soon as it left, the rough persona returns."
    n mh "Good."
    n b1a e2a mi "I’ll see you at the club."
    show natsuki mj at thide
    hide natsuki
    "And there she goes."
    "..."
    _mc eb bd mf "I... What?"

    scene bg club_day with fade
    pause 0.03

    $ autofocus.block("sayori")
    $ say_transition = True
    show bg:
        blur 2
    show sayori turned e2a at i11
    camera master:
        align (0.5, 0.2) zoom 1.6
    with Dissolve(0.2)
    $ set_date(hour=15, minute=42)

    "While we sit and read, I shuffle over to Sayori."
    _mc turned ec mh "As much as I don’t want to give anything away, I need to get some answers."
    show sayori md e1a with say_dissolve
    mc ea mg "Hey, has Nat been acting weird lately?"
    s mg "Nat?"
    show sayori md with say_dissolve
    mc ec ml "Natsuki."
    s mh lup "I know what you meant, it’s just... When did you two get so close?"
    show sayori md with say_dissolve
    mc bd ea mf "Huh?"
    s mh "You called her Nat. That’s a little odd."
    s e2a mb b1d "Though, she calls you Mel, so I suppose you’re even."
    show sayori ma with say_dissolve
    mc ef ml ba "... I, ah..."
    s b2a mb nb "Yeah. I know I shouldn’t, but old habits, you know?"
    show sayori ma with say_dissolve
    mc mg "... Of all people, you’d be the only one I’d let call me that."
    s na e1a lup b1a mh "... You never did tell me why."
    show sayori md with say_dissolve
    mc ml "Well, I-"
    mc ea mb "Huh. That’s true. When we’re walking home, I guess I’ll tell you a tale."
    show sayori e3d ma ldown with say_dissolve
    "She gives me a small smile, and a slight nudge with her elbow."
    s e1a mb "Deal."
    show sayori ma with None

    hide sayori
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False

    "I return to my own book. I’d almost rather be studying now, but sometimes I need to put all that aside."
    _mc thinking ma "I’ll have plenty of time to study over the coming weeks, anyway. The exams are about five weeks away; what’s the harm?"
    _mc ec mh "Still, makes me wonder-"
    
    $ say_transition = True
    show bg:
        blur 2
    show sayori turned at i11
    camera master:
        align (0.5, 0.2) zoom 1.6
    with Dissolve(0.2)

    "My gaze returns to Sayori."
    show sayori md with say_dissolve
    mc ldown mg bm ed "You didn’t answer the question."
    s e2a nb mb b2b lup "Hehe, nothing gets by you, eh?"
    show sayori ma with say_dissolve
    mc ea ba ml "So, what’s the deal?"
    s md "..."
    s b2a mk nd "I, uh-"
    show sayori md with say_dissolve
    "She shifts uncomfortably in her seat."
    s mg b2c "... Shouldn’t really be snitching on anything."
    show sayori mj ldown with say_dissolve
    "I nod. If Sayori knows and isn’t overly bothered by it, then it should be fine."
    "Besides, if she wanted to tell me, she’d tell me."
    _mc ec mh "... Probably. Unless it is what I suspect."
    s b2a e1a mb nb "She’s okay, though."
    show sayori ma with say_dissolve
    mc ea "Hm?"
    s b2c mh lup "You keep drifting off into your own thoughts. Are {i}you{/i} the one who isn’t okay?"
    show sayori mj with say_dissolve
    mc mb ef "Haha, well..."
    show sayori ma with say_dissolve
    "She brings a hand to my face, gently brushing it across my cheek."
    "I can’t help but lean into the touch; it’s been so long since we’ve been this close."
    s e2a ldown mg na "You can talk to me about it, y’know?"
    show sayori mj with say_dissolve
    mc ml "... I know."
    mc eg mg "I’m just a little concerned, but I don’t know if I should be. I’ve hardly known her a week."
    mc ea ml "It makes me wonder if my first impression was really that far off."
    s b2a e1a mb "Well, give it time, okay? She’s not my closest confidante for no reason."
    show sayori mj b1a with say_dissolve
    "I chuckle at her choice of words. It sounds like something Yuri would say; she’s really learning and growing here, isn’t she?"
    s mg b4 "What?"
    show sayori me with say_dissolve
    "She raises an eyebrow at my laughter."
    show sayori e1a md with say_dissolve
    mc eh mb "No, it’s nothing. I’m just amazed at both how much you’ve changed, and how much you’ve stayed the same."
    stop music fadeout 3.0
    s e2a b2b mh "Well, you’re one to talk. You’ve only grown more stubborn."
    show sayori mj with say_dissolve
    mc ef mg "I know. I've changed, and not in any of the good ways, haven't I?"
    show sayori b1b with say_dissolve
    "Her expression grows grim."
    "I guess I know where this is going."
    mc ea "Do you... think there's a way for me to get out of this rut?"
    mc ec ml "I've been floundering for so long that I..."

    #[Full Voice Acting]
    s mg "You..."
    show sayori md with None

    play music myfeelings
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False

    s b2a mh e2a "You’re stronger, a little colder, and a whole lot angrier than I’ve ever seen you."
    show sayori md
    mc ef bi mf "... Way to cut me down..."
    s lup b2c e1a mi "But it shows, Melody. You’ve changed so much, and not for the better."
    show sayori mj with None
    hide sayori
    camera master:
        align (0.0, 1.0) zoom 2.0
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "I look away. Normally, if someone said that to me, I’d get upset, but that’s exactly what she’s talking about-"
    "-And I know that this is something I need to understand for me to be able to address it. She's being blunt because she knows it will stick."
    s turned e2a b1b mh "You’re impatient and condescending, these days. I don’t know what happened- No, that’s a lie. I know exactly what happened."
    mc ba mh "..."
    s e1a b2a mb "But you can’t let that rule you, okay?"
    $ autofocus.block("sayori")
    $ say_transition = True
    show sayori e3c ma nb at i11
    show bg:
        blur 2
    camera master:
        align (0.5, 0.2) zoom 1.9
    with Dissolve(0.2)
    "This time she pulls me in for a hug."
    s mb "Mel, you’re better than that."
    show sayori ma with say_dissolve
    "Her serious tone gone from her voice, she now holds me in the same way Aunt Katsuragi would."
    _mc ea bg mh "Oh, my god - Everything she just said was like her mother - She's been emulating Misato."
    mc ef "..."
    mc mf "But... What if I’m not?"
    show sayori b1d e1a me 
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    "Sayori lets go, a confused shock crossing her features as she locks eyes with me."
    mc ea bf mg "... What if I’m not better than that? Better than them?"
    show sayori b2c mj na 
    mc ef bg ml "What if I... never amount to anything?"
    mc ea mg "I’m just me, you know? Just..."
    mc bf mb "Mel."
    mc bi eg "Even changing my name didn’t fix that."
    show sayori e1b me b2a nb 
    "Her eyes widen."
    $ autofocus.unblock("sayori")
    s mg "MC..."
    show sayori me 
    mc ef bg mb "... Pretentious, isn’t it?"
    mc bb eg mg "Melody Charlotte Nakamura. A half-Japanese, half-American."
    mc ef ba ml "I thought, by going to all that effort to make myself... {i}not{/i} me - maybe I could be someone worth paying attention to."
    show sayori e1a tears_a b2c mj 
    mc bg mf "Maybe I could be the main character of my own story."
    show sayori e3c rup
    camera master:
        zoom 2.0 align (0.5, 0.2)
    show bg:
        blur 2.5
    with Dissolve(0.3)
    $ autofocus.block("sayori")
    $ say_transition = True
    "Sayori pulls me in once more, running her fingers through my hair."
    "This time, it's a hug I recognise. This one's from Sayori herself."
    mc ml "But here I am, just..."
    mc mb ea bf "Melody."
    mc bg eg "That’s all I’ll ever be, isn’t it?"
    s e1a b2a mh na  "No, you’re not just you... You {i}are{/i} you."
    s b2c e3c mg "And all that potential is within you."
    s b1a mh notears "Imagine what you could become if you embraced that? If you followed the path you pave for yourself?"
    show sayori md with say_dissolve
    mc ef mf "... Can I even do that?"
    mc bf ea mg "I wasn’t even enough for my own parents to care about."
    s e3c tears_a mb nd "But you’re enough for me, Mel."
    show sayori ma with say_dissolve
    "She squeezes me tightly."
    s mb "You’re enough for me."
    show sayori ma with say_dissolve
    "..."

    #[End Voice Acting]
    scene bg school_street_afternoon
    show sayori turned b2a e2a md:
        matrixcolor TintMatrix("#ffeede")
        i11
    with Dissolve(1.5, time_warp=_warper.ease)
    $ set_date(hour=16, minute=34)

    "Sayori and I walk home in silence."
    _mc turned ec mh "It wouldn’t be the first time, but it still weighs on me."
    _mc ef bg "She’s the most friendly, bubbly person I know, and her mood is being brought down just by my being here."
    camera master
    show sayori e1a
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    stop music fadeout 2.0
    s b2c mb "I’m not bothered, you know?"
    show sayori md b1a
    "..."
    s lup mb "Don’t act surprised. You know I’m psychic~"
    show sayori ma
    mc eg ba mg "Hah, sure sure."
    s ldown e1d b1d mh "You doubt me?"
    show sayori mj
    mc ec ml "Now, I didn’t say that."
    s b1c e3c mh "But you thought it. I know, I’m psychic."
    show sayori md
    play music friendly_endeavours fadein 0.05
    mc eg ml "Alright, what am I-"
    mc ea mf "-Thinking of..."
    show sayori e1a b1a
    _mc ec mh "Huh. I just got the weirdest sense of deja vu."
    s lup mh "Huh, me too."
    show sayori ma
    mc eg mb ba nb "OK, that’s enough, it’s starting to get weird!"
    s ldown e3d mb "What, me reading your mind or the feeling that we’ve had this conversation before?"
    show sayori ma
    mc ef "... Yeah."
    s e1d b1d mb "Well, that’s sure weird."
    show amelia turned ef bb mb:
        matrixcolor TintMatrix("#ffecdb")
        t21
    show sayori lup rup e1b b1a mk at t22
    am "He-ey~ What am I missing?"
    show amelia ma 
    _mc mf bd eb "A- Amelia?"
    _mc na ea ba mh "Where did she come from?"
    $ autofocus.block("sayori")
    $ autofocus.block("amelia")
    $ say_transition = True
    show sayori mn rdown e1a
    show bg:
        blur 2
    camera master:
        align (0.15, 0.18) zoom 2.2
    with Dissolve(0.2)
    am eb mb "What’s the happs, my dude?"
    show amelia ef ma with None
    camera master:
        xalign 0.85
    show sayori lup rup e3d
    with Dissolve(0.2)
    show sayori mc at hop
    s "Fo shizzle!"
    show sayori ma with say_dissolve
    mc ec mg "... What are you both, twelve?"
    show amelia ea ba
    s ldown e1a mb "Would a twelve-year-old listen to rap music that old?"
    show sayori ma with say_dissolve
    mc ef mf "... Fair point."
    show sayori ldown
    show amelia ec
    camera master:
        xalign 0.15 
    with Dissolve(0.2)
    mc ea mg "So, Meelz, what’s your excuse?"
    am bd ed mb lup "I’m a kid at heart?"
    show amelia ldown eb bb mi with say_dissolve
    mc ed md "Bull. I’ve read the stuff you put in that diary of yours." # im stuff
    am bh mf "You swore you’d never mention that again!"
    show amelia mg with say_dissolve
    mc eg mg "No, I swore I’d never use it to blackmail you."
    show amelia ee bi mc with say_dissolve
    "Amelia wiggles her nose, a tic that tells me she’s upset, but not furious."
    show amelia ea ba md
    camera master:
        xalign 0.85
    with Dissolve(0.2)
    s mb "If it helps, Mel and I used to co-author each-other’s diaries?"
    show sayori ma with None
    camera master:
        xalign 0.15 
    with Dissolve(0.2)
    am ec me "What’s the point of diaries if you’re writing them with each-other?"
    show amelia ea md with say_dissolve
    mc ea mb "Well, we could never think of the words we wanted to use, so the other one would know exactly what we were thinking."
    am ed bb me "Ahh..."
    show amelia md with say_dissolve
    mc ml "Did you ever have a friend like that, Amelia?"
    show sayori me with say_dissolve
    am ed ba me "... Yeah, I guess, but it was a long time ago..."
    show amelia mc with say_dissolve
    "The souring of her expression tells us both that we shouldn’t pry, but just as we go to change the subject, she starts talking once more."
    show sayori md with say_dissolve
    camera master
    show bg: 
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("amelia")
    $ say_transition = False
    am ec me "I... had a best friend. She stopped talking to me after..."
    am mc ed "Kaito."
    $ autofocus.unblock("sayori")
    s mg "Kaito?"
    show sayori md
    "As Sayori goes to ask, I shake my head."
    _mc ec bi mh "Goddamn. I had no idea."
    show amelia ea md
    mc ea bg mg "I’m sorry."
    show sayori e2a
    am me bd "For what? You didn’t do it."
    show amelia ma
    show sayori e1a
    mc ef ml "... For being inconsiderate."
    s e2a mg "I..."
    show sayori md with None
    show sayori rdown
    camera master:
        align (0.85, 0.15) zoom 2.2
    show bg:
        blur 2
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ autofocus.block("amelia")
    $ say_transition = True
    "Sayori, who’s eyes have been darting confusedly between us for quite a while, starts to speak, before returning to silence once more."
    show sayori e1a with say_dissolve
    mc ea bf mb "It’s alright, don’t worry about it."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    am me ee ba "... This is my turn."
    show amelia md with None
    camera master:
        align (0.15, 0.15) zoom 2.2
    show bg:
        blur 2
    with Dissolve(0.2)
    am bb eb mb "Hey, Mel, would you... mind walking me home?"
    show amelia ma with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    mc ba mb ea "Of course. Sorry Sayori, but I’ll join you for dinner, alright?"
    $ autofocus.unblock("sayori")
    s e3c me "Mhm."
    show sayori ma e1a lup at dip
    show amelia ef
    "She nods as she gives me a small wave."
    show sayori at thide
    hide sayori
    show amelia ed at t11
    mc thinking ml ea "So, what’s up?"
    $ autofocus.unblock("amelia")
    am eb me "No, nothing in particular, I just felt like company."
    show amelia ec mg bi
    mc ec mg "I’m amazed you can lie so poorly, considering your career choice."
    am bh mf "Hey, acting is different to lying."
    show amelia ma ea at dip
    "She gives me a light elbow."
    am bb ee mf "When you lie, you’re deceiving someone with malice."
    am eb mb "When you act, it’s for show."
    show amelia ea ba md
    mc ea mg ldown "I see. So how much of what you do is an act, and how much a lie?"
    am ed lup me "... About as much as yours."
    show amelia md
    "I nod. That makes sense; of course she’d see through me. Sayori does, too."
    mc ef ml "So why don’t I see it?"
    am ec me "Because you don’t pay enough attention."
    show amelia md
    mc ec bi mf "What’s that supposed to mean?"
    am ldown ee mf bb "Nothing so sinister, just that you tend to get wrapped up in your own thoughts and zone out a lot."
    show amelia md
    _mc mh ba "I do do that."
    am me ea ba "So you often miss the things going around you."
    am ed mb "Though, not always, I’ll admit. You’re usually there when it counts."
    show amelia eb md bb
    mc ef mf "... Yeah."
    am bd ea mb "Hey, it’s alright, you know?"
    am rup "Everyone has their flaws, you know."
    am eb ba me "Yours just happen to be stuff that involve people and doing things. At least you don’t have medical stuff?" # im stuff
    show amelia md rdown
    mc mb "Huh, true."
    am ec mb "Better than me. Did I tell you I’m allergic to water?"
    show amelia ma
    mc ea mg "Oh yeah, that’s right! Of all the things, you’re allergic to the thing you need to live."
    mc mb "Skin allergy, right?"
    am ed lup me "Yep. Means I can’t take baths, only very quick showers."
    am ee bb mf ldown "And I need to take pills to reduce the rashes."
    show amelia ea ba md
    mc ml "It’s also why rain is really bad for you, too."
    am ed me "Sure is! So hey, there are things you can do to get around it."
    am mb eb bb "It’s honestly not so bad when you’re used to it!"
    show amelia ma
    mc ec thinking ml "... So you’re saying that I’ll get used to these feelings?"
    show amelia ed ba lup md
    "She brings a finger to her mouth in thought."
    am eb me "I mean, I was just talking about me, but sure, you can take it that way."
    show amelia ma
    mc mf "Makes me wonder just what people should be able to get used to."
    mc ea mg "Like, do soldiers ever get used to what they do?"
    am ldown ed mi "I, ah, wouldn’t have a clue."
    am eb bb me "But you make a good point, honestly. I sure wouldn’t want to get used to that kind of thing."
    am ec ba mf "But Jesus, that’s dark, Mel. Where did that even come from?"
    show amelia mg ea
    mc ldown ef mg ba "... I dunno. I was just thinking about things I wouldn’t want to get used to, and that was the first thing that came to me."
    show amelia md
    mc ml "Just like I wouldn’t want to get used to the feeling of waking up in an empty house."
    am me bd "Mel, are you sure you’re okay?"
    am eb bb mb "Tell you what, come visit my place for dinner. My parents won’t be back until late, but my little sister will be there."
    show amelia ef ma at lhide
    mc eg bi mg "Amelia, I’m fine-"
    hide amelia
    "She doesn’t even dignify my protest with a response, simply marching off."
    am turned eb mb "Come on, don’t make me drag you, dude."
    "I sigh. I know better than anyone to test her patience."

    stop music fadeout 2.0
    scene bg am_living_room_afternoon
    with longfade
    python:
        set_date(hour=17, minute=38)
        phone.system.internet_connection = True
        phone.system.cellular_data = False       
        persistent.ellen_seen = True
    play music yofukashinouta

    "As I sit waiting on the sofa, I notice a pair of eyes staring at me from the crack in the door."
    show ellen turned vest mc at t41 
    mc turned mb "Hey there, Ellen. Long time no see, right?"
    e ec bd mb lwaist "Oh, ah, hi..."
    show ellen ma nb at t11
    "Clearly surprised that she’s been caught, she steps out from behind the door."
    e bb ea me "I, well, wasn’t expecting you, so seeing you here was quite a shock..."
    show ellen na md
    mc eh bg md "Yeah, I wasn’t expecting to be here, myself, but you know your sister."
    show ellen ma ee ba ldown
    camera master:  
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("ellen")
    "She chuckles a little, sitting next to me."
    e ec bc mb "That I do."
    e ea ba me "Still, I doubt she’d drag you here for no reason."
    show ellen mc with say_dissolve
    mc ea mg ba "... I mean, spontaneity is in her nature, it is a possibility."
    show ellen ma bd with say_dissolve
    "Ellen gives me a small smile. She’s already caught on."
    _mc ec mh "Time to change the subject before this gets awkward."
    show ellen ba mc with say_dissolve
    mc ea mg "So, how’s school?"
    e rhip me bb "It’s going alright. High school isn’t anything like I expected, not from all the stories that Amelia and Kaito-"
    e bd mb ec rwaist "-Tell me..."
    show ellen ma nb with say_dissolve
    _mc ec bi mh "That’s right, she’s gotten involved with {b}him{/b}."
    "I guess she knows something, because she stumbles off of her words from then on."
    e eb bb mf rdown "It’s not like that, I just..."
    show ellen md ea ba with say_dissolve
    mc ef mg ba "Hey, it’s your life. I sure won’t stop you. I’m just surprised your sister hasn’t yet."
    e bg me ec na "... She’s tried."
    show ellen mh with say_dissolve
    mc ea ml "Really? And you defied her?"
    e ba me "Well, no, not exactly, I just..."
    e mb ea "He isn’t whatever he was back then. To me, he’s kind, friendly, and cheerful."
    e md ec bd "I enjoy his company, that’s all. It’s not like we’ve... We’ve..."
    show ellen mc with say_dissolve
    mc bg mb ea "Alright, alright, I believe you."
    show ellen ea ma with say_dissolve
    "A small smile returns to her face."
    e ba mf "My big sis doesn’t, though. She can’t see anything but a slimy, awful monster."
    show ellen bc mh with say_dissolve
    mc ef bi ml "... I don’t blame her. I don’t know what he did, but I know what he’s capable of."
    e bg mf nb "But he’s not that person anymore! I swear!"
    e thinking ed mj "The entire time, he’s been friendly, and- I don’t know what to say to change your mind!"
    show ellen mh with say_dissolve
    mc ba eg mg "I’m not sure there is anything, Ellen. But don’t worry about it. I’m not the one you have to convince."
    e be ec mg "... I don’t know what to do."
    e ldown ea bb mf "Am I making a mistake?"
    show ellen md with say_dissolve
    mc ea mf "I-..."
    "I cut myself off. She’s not looking for sentiment here, she’s looking for genuine advice."
    show ellen mc with say_dissolve
    mc eg ml "I don’t know. I can’t say, because I can’t see the future. But, if you want my opinion, I think you are."
    show ellen ec bc mh na with say_dissolve
    "A shadow crosses her features when I speak."
    mc thinking ec mg "He might be kind to you now, but do you know how long that will last?"
    e ba me "It could last forever, though, right?"
    show ellen mc with say_dissolve
    mc ldown bd ea mg "... Ellen, you and I both know high-school relationships are bogus. One second you’re on top of the world, the next you’re in the dumps."
    e bd "..."
    mc ba ml "You’re putting yourself in a difficult situation here. Sure, maybe he’s different with you, but at the same time, maybe he’s not?"
    e mf ea be "I- I’ve seen it, I swear!"
    show ellen mh with say_dissolve
    mc eg mg "Then perhaps it’s worth pursuing. But you know that your sister and I share the same opinion."
    show ellen mc bd with say_dissolve
    mc ml thinking "Besides... Do you really want to keep dating someone who your sister already dated?"
    mc ec bi mj "Do you want her sloppy seconds?"
    show ellen bc ed mj with say_dissolve
    "Ellen cringes at the thought."
    e bd ea me "B- But, if he’s good enough for Amelia, he’s good enough for me, right?"
    show ellen mc with say_dissolve
    mc ldown ec bi ml "I think the point was that he {i}wasn’t{/i} good enough for your sister."
    e ec me "... I... I’ll think about it."
    show ellen mc with None
    hide ellen
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("ellen")
    "She shrinks off, back to her own room."
    _mc bi eg mm "God, I feel terrible for doing that. I feel like I was delivering news that someone’s dog got run over."
    _mc mh "She doesn’t deserve to be shut down like that. She has to make her own mistakes to grow."
    _mc ec "... Just not with him."

    show amelia turned bh:
        pos (0.2, 0.1) anchor (0.5, 0.0) zoom 0.75
        matrixanchor (0.5, 0.0) matrixtransform RotateMatrix(0, 0, 40)
        xoffset -260
        easein 3.6 xoffset -120
        0.13
        easein 0.45 xoffset -20
    window hide
    pause 3.0
    camera master:
        zoom 1.7 align (0.0, 0.4)
    show bg am_living_room_afternoon as stuff zorder 0:
        blur 2.0
        on hide:
            easein 0.25 blur 0.0
    with Dissolve(0.3)
    window auto

    am mb "Nyehehe."
    show amelia ma
    mc ea bd mm nb "... You rat bastard. You set me up!"
    hide stuff
    show amelia ef bb lup mb:
        easein 0.25:
            matrixtransform RotateMatrix(0, 0, 0)
            xpos 0.5 zoom 0.8 xoffset 0
            yanchor 1.0 ypos 1.03
    camera master:
        easein 0.25 zoom 1.0 yalign 0.5
    am "Did I? Wouldn’t that be cruel and unusual?"
    show amelia eb me ba
    mc mg eb "And here I thought you were trying to help me, but no, you dragged me here to help talk your sister out of dating Kaito!"
    show amelia mj ldown rup ec bh at dip
    am "Shh! Jesus, you’re loud."
    am me rdown bi "If she hears, it’ll undo all the work you just did. Do you really want her to end up with him?"
    show amelia mg
    mc ml ea na "... She can do a lot better."
    am mf bh ea "Exactly."
    show amelia mg
    mc ec bi mg "Now, are you done making fun of me?"
    am lup ed ba mb "Me? Never."
    show amelia ma
    mc mb eg "That’s what I thought."
    am ea mb "I did bring you tea, though. Make yourself at home; dinner will be ready shortly."
    show amelia ma at thide
    hide amelia
    _mc mj  "Ugh. She reminds me of me, when she pulls that smug face."
    _mc ec ba mh "... She does remind me of me, doesn’t she?"
    _mc ea ma "I guess we’re more alike than I thought."
    "As she walks back out the door, I hear a distinct noise come from her."
    show amelia turned ef mb bd rup:
        zoom 0.8 xanchor 0.8 xpos 0.0 yanchor 1.0 ypos 0.98
        matrixanchor (0.5, 1.0) matrixtransform RotateMatrix(0, 0, 0) xoffset 0
        easein 0.3 matrixtransform RotateMatrix(0, 0, 30) xoffset 70
    am "Teehee~"
    show amelia ma 
    mc md ed bm "What do you mean, 'teehee'?"
    am bh ea mb rdown "That’s what I call... gottem."
    show amelia ma bb ef:
        on hide:
            easein 0.3 xoffset -170
    hide amelia
    "With that, she turns back toward me, winks, and closes the door behind her."
    _mc eg ma bi "... Un-freakin-believable."
    _mc ec "This is what I have to put up with."

    scene bg am_kitchen_night_on
    show ellen turned vest ec bc mc at i11
    with wipeleft_scene
    $ set_date(hour=19, minute=17)

    "I find myself waiting, somewhat patiently, with Ellen at the table."
    "She’s texting someone on her phone, which is unsurprising. Kaito, I’d assume."
    mc turned mg  "So, how is he?"
    e me "... I’m not texting him."
    show ellen mh
    mc ml "Why not?"
    $ autofocus.block("ellen")
    e nb "..."
    show ellen bf mj ed
    "She shuffles uncomfortably on the chair, shaking her head."
    $ autofocus.unblock("ellen")
    e bc ec me na "I don’t wanna talk about it."
    show ellen mc
    "I shrug. There’s no point pressing her further; it would only sour her mood more."
    $ autofocus.block("ellen")
    e "..."
    e ea ba "..."
    e ec "..."
    $ autofocus.unblock("ellen")
    e bg lwaist rwaist mf ea "Well? Aren’t you going to ask?"
    show ellen mh 
    mc thinking bd ea ml "... No?"
    e ed ldown rdown ba mc "Hmph."
    e ec me "Amelia would."
    show ellen mc
    mc ldown ef mg ba "Of course she would; she’s your sister."
    e ea mb "She knows exactly what I’m thinking."
    e me bb "Watch."
    show ellen ec ma
    "She turns toward the pantry, and bellows out:"
    e lup mi "Mills, what am I thinking about right now?"
    show ellen ma
    am turned ef bb mb "Food! Specifically fried rice!"
    show ellen ldown ea bg
    "She then turns to me, a smug look upon her face."
    e mb bb "See?"
    show ellen ma
    mc mb ea ba "I didn’t question you; she knows you well."
    show ellen md bc
    mc mg "It’s the same reason why you wish you knew her half as well as she knows you."
    show ellen ec bg
    "Averting her gaze, Ellen frowns."
    e me "And what would you know?"
    show ellen mc
    mc ef ml "Because she does the same to me. I wish I knew her half as well as she knows me."
    e bb ea mf "Wait, really?"
    show ellen mc
    mc ea mg "Yeah. She’s just that good at reading people and learning about them."
    mc mb "She has to be, to do her job correctly."
    e md ba "... You think so?"
    show ellen mc
    mc eg mg "Look, what she does isn’t for everyone. I sure as hell couldn’t do it. She’s developed a skill to determine what people she’s never met before are thinking, and worked out how to exploit it, before they even know she’s there."
    mc ed md "That’s why she’s so good at her games."
    mc eg mb "She might be skilled with her hands, but she’s even better at outwitting and outsmarting her opponents."
    mc ea "That’s why she plays at such a high level, more often than not."
    show ellen ma
    mc eg mg "Sure, arcade games might be her passion, but she’s better at FPS and strategy games than anyone I’ve ever met."
    e ed mb "She’s been playing for as long as she could move her hands, so it makes sense."
    e me ea bb "One of my earliest memories is of her playing an old Quake game against some of our uncles... She didn’t win, of course, but she didn’t lose as badly as you’d think."
    show ellen ma
    mc eg mb "I’m not sure that even surprises me, to be honest. It’s just something she’s always had a knack for."
    show ellen mb eb at hop
    e "Right? I could never beat her at anything. She’s beyond amazing!"
    e ea "Imagine how good she would be at school if she applied herself half as much..."
    show ellen ba md
    mc ea ml thinking "You, worried about school?"
    e lwaist rwaist mf bg "For her, duh! She graduates in less than six months! If she doesn’t do well in her final rounds of exams..."
    show ellen eb nb ldown rdown bd md
    "Ellen shudders at the thought."
    e bg ec mf na "I don’t even wanna think about it!"
    e bc me "But like..."
    e ba mf ea "Isn’t she something out of like, a manga? Smart, pretty, stupid good at games..."
    e mb bb "It’s like the winning heroine!"
    show ellen ma
    mc ml ef "I, ah, well, suppose she is a lot of those things..."
    e ba me "You don’t think so?"
    show ellen mc
    mc ldown bb ea nb mg "N- No, I do, yeah, definitely, more that I-"
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show ellen bg lwaist rwaist mh
    with Dissolve(0.2)
    $ autofocus.block("ellen")
    $ say_transition = True
    e mf "You don’t think my sister is the coolest person ever?"
    show ellen mh with say_dissolve
    "Her voice raised, she’s practically grabbing my blazer and forcing her words down my throat."
    mc ef ml ba "Well, she’s right up there, I’ll admit-"
    e ldown rdown mf "What do you mean, 'right up there'? Who else could possibly compare?"
    show ellen mc with say_dissolve
    mc ea mg na "I mean, if you think about it, you’ve got all her genes, which means you’re bound to be basically as good as her in all those categories-"
    show ellen ba
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She pauses, loosening her grip."
    $ autofocus.unblock("ellen")
    e eb bd mf "Are you... coming on to me?"
    show ellen md
    mc bd mg nb "Eh? No! I was just stating a fact-"
    e ec mf "But... you said that I was as good as her, and if she’s basically a goddess, then that means-"
    stop music fadeout 2.0
    show ellen be mj nb at hop
    e "!!"
    show ellen mc bd
    show amelia eb md ba at t41
    "Ellen jumps, whirling at the sight of her older sister, who has now entered the room, a look of pure shock upon her face."
    am ed bd mi "I, well, um..."
    am ea mb bc "Let’s just call it a day, shall we?"
    show amelia ma
    mc ba ml "But we haven’t eaten yet-"
    hide ellen
    show amelia bh md ec at i11
    show bg:
        blur 2.5
    camera master:
        align (0.5, 0.2) zoom 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    am ef bb mb rup "Mhm, what a lovely meal! Yes, how truly spectacular!"
    show amelia mf with say_dissolve
    "She grabs me by the arm, shouting strange things, as she drags me toward the door."

    scene bg am_house_night_on
    camera master
    with wipeleft
    show bg:
        blur 2.5 align (0.7, 0.7) zoom 1.7
    show amelia turned mg bh:
        xalign 0.5 ypos 1.0 yanchor 0.7 zoom 1.3
        matrixcolor TintMatrix("#1a4d83")
    with Dissolve(0.2)
    play ambient ext_night fadein 1.0

    am me "Care to explain?"
    show amelia md with say_dissolve
    mc turned bd mg "Me? Shouldn’t you be asking the obsessive sibling?"
    am ed bi me "I meant how you even got onto the topic in the first place!"
    show amelia mg with say_dissolve
    mc ef ml ba "Oh. Well, that I... don’t remember."
    am ea mf "Seriously? What do you expect me to do?"
    show amelia md with say_dissolve
    mc bd ea ml "Explain to her that you’re not perfect?"
    am ba ee me "And shatter her perception of me? Never."
    show amelia ed ma with say_dissolve
    "She rolls her eyes, a little smug grin flashing across her features."
    am ec bf me "No, what do you expect me to do about the problem with Kaito?"
    am bb ee mf "I know she’s like that with me, and I’m okay with it to an extent because it reinforces that she shouldn’t be like that with boys. It prevents her from doing the same to Kaito."
    show amelia ea ba md with say_dissolve
    mc ef mf ba "So that’s why her mood was sour."
    am ee mi "... Most likely."
    am ed me "I... I think Kaito’s just using her to get back at me, but I can’t be certain."
    show amelia md with say_dissolve
    mc eb bd mg "That makes... way too much sense."
    am ea mf bh "Right? But they’ve been 'dating' for almost six months. I don’t even know how they met!"
    show amelia md with say_dissolve
    mc thinking mg ea ba "... It’s a difficult one, isn’t it. Have you talked to your parents about it?"
    am ed ba me "... If I did, then they’d..."
    am lup "I’d have to tell them what initially happened."
    show amelia md with say_dissolve
    mc ef ml "... You haven’t even told me."
    am ed bd mb ldown "... Yeah."
    stop music fadeout 1.0
    show amelia ma with None
    show bg:
        blur 0.0 align (0.0, 0.4) zoom 1.3
    show amelia ea ba:
        xcenter 0.4 alpha 0.0
    with Dissolve(0.2)
    "She turns back toward the door."
    show amelia:
        alpha 1.0
    show bg:
        blur 1.0
    with Dissolve(0.2)
    am eb mb "You should get home before it gets any darker."
    am ee bd me "I’m sorry you missed out on the dinner; I’ll bring some as a lunch for you tomorrow."
    show amelia bd ea ma with say_dissolve
    mc ldown mb "Oh, sure. I appreciate it."
    hide amelia
    show bg:
        zoom 1.0 blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("amelia")
    $ say_transition = False
    "I wave her off, starting back down the road."
    _mc ec ma "What a hell of a day."

    stop ambient fadeout 2.0
    scene bg mc_living_room
    camera master:
        blur 0.0 matrixcolor BrightnessMatrix(0.0)
        1.0
        block:
            easein 2.0 blur 5.0 matrixcolor BrightnessMatrix(-0.1)
            ease_cubic 1.0 blur 0.0 matrixcolor BrightnessMatrix(0.0)
            repeat
    with fade
    $ advance_date(minutes=50)

    "My head aches, throbbing with a distant pain."
    scene bg mc_kitchen_day with wipeleft
    "My bag finds itself flying toward the sofa as I walk past the living room, headed to the kitchen."
    play sound fall
    "... Only, it seems to stop early."
    who "Oof!"
    who "Meanie..."
    "In my pained daze, I turn to face the noise."

    scene bg mc_living_room
    show sayori turned b1d e2a md rup at i11
    with wipeleft
    play music rgb

    mc turned ec bi mj "Sayori?"
    s e3c me "Hmph."
    show sayori md rdown at dip
    "She pouts as she gently places my bag down."
    s mg e1a "You threw your bag at me!"
    show sayori md
    mc mg eg "No, I threw it on the sofa."
    show bg:
        blur 2.0 align (0.5, 0.0) zoom 0.9
    show layer master:
        align (0.5, 0.2) zoom 1.8
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "She strides up to me, still pouting."
    s mh "But you hit me, instead."
    show sayori b1a me with say_dissolve
    mc mm "Sure, whatever, sorry."
    s lup mh b2c "... What’s up?"
    show sayori mj with say_dissolve
    "Her playful tone vanishes, replaced by a look of concern."
    mc mg "I’ve got a massive headache."
    s ldown b1a mh e2a "Oh. Well, sit down, and I’ll make you something for it, okay?"
    show sayori md with say_dissolve
    mc ba ea ml "No, no, I’ve got-"
    s b1d e1d mg "Sit down."
    s mh e1a b1a rup "And I’ll make something for it."
    show sayori ma with say_dissolve
    mc mh ec "..."
    hide sayori 
    show bg:
        blur 0.0 zoom 1.0
    show layer master
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    "I shrug, accepting her offer."
    mc ea ml "Wait, Sayori-"
    show sayori turned md at t11
    "She turns back toward me."
    mc ef bg mg "Sorry, I didn’t mean to be so blunt. Not feeling well is no excuse to be rude to you."
    mc mb ea "... Especially when you were waiting for me, right?"
    s e3c mb "... It’s fine, I don’t mind."
    show sayori e1a ma
    mc eg "Still, even if you don’t, I have to be a little better to you."
    show sayori me
    mc ea bf "You mean a lot to me, you know?"
    s mc nc e2a b2c "E- Eh? W- Well-"
    show sayori ma at thide
    hide sayori
    "She turns back around, heading toward the kitchen."
    s turned b2b e2a mb nb "{size=-5}I’m glad you feel that way.{/size}"
    play sound fall
    "I slump into the couch, letting the exhaustion from the day finally wash over me."

    scene black
    camera master:
        align (0.5, 0.2) zoom 1.5
        blur 0.0 matrixcolor BrightnessMatrix(0.0)
        block:
            easein 4.0 blur 1.0 matrixcolor BrightnessMatrix(-0.05)
            ease_cubic 3.0 blur 0.0 matrixcolor BrightnessMatrix(0.0)
            repeat
    with Dissolve(1.0)
    pause 2.5
    $ autofocus.block("sayori")
    $ say_transition = True

    who "...dy?"
    who "...ody?"
    s turned mh "Melody?"
    mc turned ec mf "Hm?"
    show bg mc_living_room:
        blur 1.2 align (0.5, 0.0) zoom 0.97
    show sayori ma at i11
    hide black
    with Dissolve(0.4)
    "My eyes flutter open at the sound of Sayori’s voice."
    show sayori mb rup with say_dissolve
    s "Here, I made you some tea, and got you some painkillers."
    show sayori ma rdown with say_dissolve
    mc ea ml "Oh, thanks..."
    "I take the cup of tea and drink it. Odd taste, I have to say."
    mc mg "What is this?"
    s mh "It’s some sage tea. You brew tea with sage leaves, then add a little lemon and honey, and it works wonders for treating stuff like ear infections, sore throats, and sometimes headaches, depending on where they are." # im stuff
    s mb e3d "Besides, it tastes pretty good!"
    s mh e1a "Then there’s the painkillers, which will help too."
    show sayori ma with say_dissolve
    mc ec mf "I see..."
    "My mind is still fuzzy, not really letting me process anything."
    s lup mh "So... Did you have a good day?"
    show sayori rup e1b ml at hop
    camera master:
        easein 0.3 blur 0.0 matrixcolor BrightnessMatrix(0.0) zoom 1.0
    show bg:
        easein 0.3 blur 0.0 zoom 1.0
    $ autofocus.unblock("sayori")
    $ say_transition = False
    mc eb bd nb mf "Pff-"
    "I almost spill my tea as my senses return in an instant."
    show sayori e1a nb ldown rdown me
    mc mg ea "Dude, you were with me the whole time!"
    s mh "Well, yeah, but I didn’t ask how your day was."
    show sayori md
    mc ec na bi ml "... I mean, it was alright."
    mc ea ba mg "Your friend, Natsuki? She’s an interesting one."
    s mh na "She is, yeah. I’m surprised she doesn’t have more friends."
    s e3c mb "She’s really quite friendly, when you get to know her."
    show sayori e1a ma
    mc eg mg "Sure seems that way, yeah."
    show sayori e3c at dip
    "I nod along."
    s e1a lup mh "But how did things go with Amelia? You definitely didn’t just walk her home, with how long you were gone."
    show sayori ma
    mc ea ml "No, she invited me in, and then we got talking, and-"
    s ldown e1b b1d mh "Oh my god, you didn’t sleep with her, did you?"
    show sayori me
    mc bf eb nb mg "Wh- What? No! What gave you that impression? Her sister was home!"
    s b4 e1a mh "So you would have if she hadn’t been there?"
    show sayori e1d md b1d
    mc ea bd "Where is this coming from? No! We just talked!"
    s me "... Hm."
    s e2a b1a mh "The way you worded it made it seem like you were gonna say that."
    show sayori mj
    mc ea ml thinking ba na "Besides, I wasn’t gone for that long, was I?"
    show sayori md e1a
    "Sayori ponders the question for a moment."
    s e2a mh "Hm, I suppose not. Would explain your exhaustion, though."
    show sayori mj
    mc mg bd ldown "Sayori, I didn’t sleep with her, okay?"
    show sayori md e1a
    mc ba "Nor do I have any plans to."
    s mh "Really? I would have thought she’d be right up your alley. You talk all the time, and seem to really know a lot about each-other."
    show sayori mj
    mc bd ml "It’s called being friends?"
    s e1d b1d mh "Look, if it were anyone else, sure, but knowing your track record with the word 'friends', and how you seem incapable of being platonic."
    show sayori mj
    mc ef bg mb "I- Well- It- Look-"
    mc ea bf mg "One time!"
    "I shuffle uncomfortably on the sofa."
    "It’s the first time we’ve talked about it since it happened."
    show sayori e1a b1a md
    mc ef bg mg "... Only once, and only..."
    mc ml "Only you."
    show sayori e3c me lup
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.8
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "She sighs, bringing her hand to mine, and gently clasping it."
    s e1a b2c mh "I’m sorry. There was a better way to broach the topic."
    show sayori ma with say_dissolve
    mc bf ea mg "No, no, it had to be said."
    mc ef ml bg "... It really did."
    mc ea mb "But hey, let’s not... bring down the mood, okay?"
    show sayori e3c ldown with say_dissolve
    "She gives me a small but warm smile."
    s e1a b1a mb "Sure. It’s ancient history, right?"
    show sayori ma with say_dissolve
    mc ef mb ba "Yeah."
    show sayori e3d with say_dissolve
    "We both stand, and make our way to the kitchen. It’s time for dinner."
    $ say_transition = False

    $ add_calendar_description(calendar_descriptions["natsuki"][6])

    return