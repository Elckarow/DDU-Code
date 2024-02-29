label week_1_monday_common:
    call act_card("act_I_card") from _call_act_card
    call calendar_transition from _call_calendar_transition
    scene black with Dissolve(1.0)
    pause 0.3

    play music school
    scene bg residential_day:
        zoom 1.15 align (0.5, 0.7)
        ease_quad 6.5 align (0.0, 0.3)
    with NonBlockingDissolve(1.75, time_warp=_warper.easein)
    pause 2.902
    scene bg school_street_day:
        zoom 2.5 align (0.585, 0.46)
        ease 6.0 zoom 1.5
    with NonBlockingDissolve(0.939)
    pause 3.342
    scene bg school_gate_day:
        zoom 2.0 align (0.4, 0.4)
        easein 5.0 zoom 1.4
    with NonBlockingDissolve(0.7)
    pause 1.717
    scene bg school_corridor_3_day:
        align (0.0, 0.4) zoom 1.2
        easein 6.0 zoom 1.0
    with NonBlockingDissolve(0.5)
    pause 1.803
    scene bg class_1_day:
        align (0.5, 0.4) zoom 2.0
        easeout_quad 3.2 zoom 1.0
    with NonBlockingDissolve(3.2)
    pause 3.2

    phone register "mc_m":
        time auto True
        "m" "I'm on my way~"

    "I linger at my desk as the rest of my class fritters away and files out, chatting amongst themselves."
    _mc turned eg mh "What am I doing?"
    _mc ef "Why am I waiting for her?"
    _mc bb eg "Why would the popular, pretty Monika, the school star, even want to take me to revision practice? It’s just too good to be true..."
    _mc ba ec ma "A pipe dream, set to fade in a puff of smoke."
    _mc mh ef "But I wait anyway, against all common sense."
    _mc ec "Giving her lateness the benefit of the doubt."
    _mc thinking eg bi me "She is, after all, president of a club and presumably busy."
    _mc ea bb mf "What club is she in again? Was it Debate?"
    _mc mh ec ba "No... Literature, that’s it. She quit the Debate Club last year."
    _mc ldown eg ma "All in all, she's very, very..."
    show monika turned mb lpoint at t11
    m "Lovely!"
    show monika ma
    _mc mf ea nb bb "H- How did she know I was going to say that?"
    $ autofocus.block("monika")
    $ say_transition = True
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    m mb ldown rhip "There you are!"
    show monika ma ed with say_dissolve
    _mc eg mh bi "Calm down... She’s just remarking that it’s lovely you’re here. I think."
    mc mb ba ea "H- Hi, Monika!"
    m rdown eb nb mb bb "Sorry, I’ve been looking in the wrong classrooms!"
    m md ec "I’m so forgetful sometimes..."
    show monika mc ea with say_dissolve
    mc md eh bg "It’s perfectly fine, Monika; don’t stress. Knowing me, I probably gave you the wrong classroom number."
    _mc eb bd mh "Why did I say that?! Oh god!"
    m ba na mb ea "I’ll accept that explanation if you insist."
    m ec md "Either way, I'm still sorry for keeping you waiting."
    m ed mb "Time waits for no one, as they say, right Me- MC?"
    show monika ma nb with say_dissolve
    "She catches herself, pausing and correcting her question."
    mc md na ba ed "Ah- Yes, true enough. We have to make the most of the hand we're dealt; even the worst hand can be a winner, if you make enough opponents fold."
    show monika ea na with say_dissolve
    "She chuckles a little, giving me a sincere smile."
    _mc eg ma "It's good to see that I'm not completely awkward - She's at least a little off balance, if she almost called me Melody."
    _mc thinking ef "She must have seen me talking to Amelia or something... Even the faculty doesn't list my name as Melody anymore."
    _mc mh bi "Well, everyone except that primordial sewage drain of a Vice Principal."
    _mc ec ba ldown "Still, it beats being reminded of that witch every time I hear my name."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("monika")
    $ say_transition = False
    m rhip md "All set?"
    show monika mc at thide
    mc ea ml "Yeah, let me just... oh, er..."
    "I quickly tuck my remaining textbooks, notebooks and a few strewn doodles back into my bag."
    "Said doodles had been done while waiting for the teacher to move on after I'd already finished writing and memorising - a common occurance, unfortunately - given my current state of being weeks ahead of the rest of the class."
    show monika ma ed
    mc md eh "Yep!"
    "Shouldering my bookbag, I follow her out."
    hide monika

    scene bg school_corridor_3_day
    show monika turned mc at i11
    with wipeleft
    $ autofocus.block("monika")
    $ say_transition = True

    show monika bb
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.2) zoom 1.5
    with Dissolve(0.2)
    m md rhip "Something on your mind? You’re looking a little... stiff?"
    show monika mc ba rdown with say_dissolve
    mc turned nb mg "M- Me?"
    mc ef bi ml "Stiff, no, not stiff, just- Colour me curious, I guess."
    mc ba ea na thinking mg "I mean, what exactly made you want to host a study group so early in the term? Didn’t think you would need that sort of help, considering you're {i}literally{/i} ranked number one."
    m mb lpoint "Everyone can improve, you know! That's why I thought I’d assist some other people with their learning."
    m md ldown "Besides, the earlier you get on top of things, the less cramming you need to do later."
    show monika ma with say_dissolve
    mc ba eh md ldown "How very humble and generous of you to give your time for us mortals~"
    mc ea mg "Where do I fit in, though?"
    m rhip md ec "We were in the same tutorials last year, so I thought you could lend me a hand with some things. You were also pretty great in that maths competition last term."
    show monika ma ea with say_dissolve
    mc ef ml "Oh. Right. I can certainly try."
    _mc bg eg mj "Did Monika seriously see that competition? I only did it for the extra marks... Oh God, she’s going to expect me to be so smart..."
    _mc eb bb mf "Wait, that sounded rude. Did that sound rude? Say something nice!"
    show monika mc with say_dissolve
    mc mb ea bb "I’m certain you’re no slouch, either."
    m rdown eb md bc "{size=-5}My parents might beg to differ.{/size}"
    show monika mc with say_dissolve
    mc ec ba ml "Pardon?"
    m nb ed mb bb "Nothing. It’s nothing."
    show monika ma na ba with say_dissolve
    _mc thinking ec mh "I wonder what was up with that."
    "I’m tempted to press for answers, but seeing her discomfort, I ultimately err on the side of caution and change the subject."
    show monika ea na with say_dissolve
    mc ea mg ldown "Has your day been alright otherwise, Monika?"
    m rhip ec md "Mmm. Had a pretty interesting PE lesson with some of the girls in my class. Otherwise, nothing out of the ordinary."
    show monika mc ea with say_dissolve
    mc mf "What were you up to?"
    m rdown md "Learning to pole-vault. I’m not too good yet, but I’m far from the worst."
    m mb "I could show you sometime, if you need help with that kind of thing."
    show monika ma with say_dissolve
    mc bg eh md "I’m sure I could still learn a thing or two from you. Athletics isn’t my forte."
    m mb lpoint "No kidding. I saw how you fared on Sports Day."
    show monika ma ed with say_dissolve
    _mc eb mh nb bb "Oh no. She saw that too? Is there anywhere left safe from implicating me as a complete buffoon?"
    "I grimace at the memory."
    mc ef bd ml "Hey!"
    m ldown rhip mb "Relax, I’m just teasing."
    m eb md "You weren’t too bad. Just keep away from the proverbial eggs and spoons and you’ll get through life without a hitch."
    show monika ea ma with say_dissolve
    mc na pout eg bi "Hmmph."
    "Despite myself, I smile at her, and we settle into a comfortable silence for a minute as we walk."
    _mc ef ma na ba "Contrary to what one might think, I'm actually glad in spite of getting a jab thrown at me."
    _mc eg "Monika’s mood has improved markedly, and I can almost relax."
    m rdown md "How about your day? What lessons did you have?"
    show monika ma with say_dissolve
    "The hippopotamus of my memory wallows."
    camera master:
        zoom 1.0
    show bg class_1_day as stuff zorder 4
    show white_flashback
    with Dissolve(0.2)
    "Strange; for some reason my memory doesn't seem to go back all that far, at least not in any meaningful detail."
    "My most vivid recollection is of the waiting I did prior to Monika picking me up."
    _mc mh ec bi "Come on, noggin, don't fail me now! What did I do today...?"
    _mc mf ea ba "I'm really proud of that picture in my history book, even if I only did it because of that American teaching us and his impossible to understand accent..."
    _mc eg thinking bi mm "I always have to re-research everything myself afterwards whenever he's teaching! It doesn't make any sense! Hell, my own bastard of a father has an accent, and I can understand him well enough!"
    _mc eb bj ml "Why do their accents have to be so different?!"
    _mc bb mb ea na "Oh, right, what I was doing...?"
    pause 1.0
    _mc ldown teehee bg eh "Nope, still nothing up here."
    hide white_flashback
    hide stuff
    camera master:
        zoom 1.5
    show monika mc
    with Dissolve(0.2)
    mc ml ea ba "Well, English stands out..."
    m md "You like English?"
    show monika ma with say_dissolve
    "I take a moment to consider the question. Monika seems to have somehow lit up even more."
    m mb ed "Even when it doesn’t appear in manga or visual novels?"
    show monika ma with say_dissolve
    "I stifle a snort."
    "An artful lunge for the jugular."
    _mc ec ba mh nb "The previous jab was good, but this is on another level entirely. How does she even know that about my history?"
    _mc ef bi "I haven't been actively involved in that space since middle- Nevermind. Stay cool."
    mc ea mb na ba "Actually, it’s quite an enjoyable subject for me."
    show bg:
        blur 0.0
    camera master
    show monika ea
    with Dissolve(0.2)
    $ say_transition = False
    "Monika’s smile broadens, tinged with what strikes me as undisguised approval."
    $ autofocus.unblock("monika")
    m mb lpoint "Well, this is it. The venue for the study group."
    show monika ma

    stop music fadeout 0.9
    scene bg school_library_day with wipeleft
    play music okev

    "Monika flings open the door and strides in with me in tow."
    show monika turned lpoint mb at t11
    m "Hello everyone!"
    show monika ma with None
    hide monika
    camera master:
        zoom 1.5 align (0.4, 0.9)
        ease 7.0 align (1.0, 0.8)
    with Dissolve(0.3)
    "General murmurs of greetings emanate from around the room. I manage a small wave."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show monika turned at i11
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    mc turned thinking mg bb "So, Monika... How shall we go about this?"
    m mb eb "We’re pretty free and easy here, so do whatever helps you clear your mind and study optimally."
    m ec md bc "If you need to take a break at any point in time, go right ahead. I might have a thing or two to help us unwind."
    show monika ma ea ldown ba with say_dissolve
    _mc mh ec ldown "Do I want to know what she has in mind?"
    hide monika
    show bg:
        blur 0.0
    camera master:
        align (0.7, 0.7) zoom 1.7
    with Dissolve(0.4)
    $ say_transition = False
    "We go and sit at a nearby table."
    show monika turned at i11
    camera master
    with Dissolve(0.2)
    mc ea ml "So, who's first on your to-do li..."
    show monika mc
    mc mg eb nb bb "I-I mean, {b}what!{/b} {b}What’s{/b} on the list, not er..."
    $ autofocus.unblock("monika")
    m eb nb mb "... I knew what you meant. Perhaps you’d go through some Mathematics with me now, then check my English at the end?"
    show monika ma
    "I skillfully bite back the awkward stuttering that my flustered brain is spitting out, and simply nod."
    mc bg ef mb "Ah, err... sure."
    show monika ec mc bc na
    "She pulls a small, pristine green textbook out of her bag and sets it down on the desk,"
    show monika ea
    extend " before looking at me."
    m md ba "Do you not have a textbook of your own, MC?"
    show monika mc
    _mc eb ba mh "No chance I’m going to whip out my copy, with all my stupid doodles in the page margins or the endless corrections I've had to make to examples and works that {b}should{/b} have been peer-reviewed."
    _mc bi mm eg "I’ve embarrassed myself enough today already, thank you very much!"
    mc ea ml ba "I left mine at home."
    mc ef mf "Sorry."
    m ec md "That’s fine, we can share this one."
    show monika ea ma
    show bg:
        blur 1.0
    camera master:
        align (0.5, 0.2) zoom 1.3
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "I pull my chair round so we’re sitting next to each other."
    _mc eb bf nb mh "How close can I sit without being weird? I need to see the page, but if I accidentally brush against her shoulder, she might think I’m flirting with her..."
    _mc eg bg na ma "Didn’t set this outcome up. Honest."
    _mc ef "Unexpected though it might be, it’s far from unpleasant - Maybe she's genuinely seen my grades and wants my help?"
    "I hear whispers coming from others around the room; whispers about Monika and myself, but even though I normally would-"
    "Right now, I don’t care in the slightest."
    show monika eb mc bc with say_dissolve
    "She gently turns the page and points at one of the questions."
    m ea md "See what I meant before about being able to improve on the fly, like you do? Here, for example, I just don’t fully understand what a periodic function is."
    m ba lpoint "Is it not just a function that repeats itself?"
    show monika mc with say_dissolve
    mc ml ef ba "You could say that, although it’s more accurate to say 'a function that repeats its values with regularity and predictability'."
    m md ldown bc "So, it’s a function that always gives the same outputs if you control the input values?"
    show monika mc with say_dissolve
    _mc ea mh "Wow, she’s fast."
    show monika ma ba with say_dissolve
    mc mb "Yes, namely you can take the 'f of x equals to f of x plus T' formula, which explains that the period of the function is the duration of the wavelength - where it repeats itself-"
    mc ml "-So you can use the formula to understand the relationship between the period in this case- Oh, but I can see from the look on your face you already understand that."
    mc ed mb "Let me show you what I mean, rather than explaining it."

    scene bg school_library_afternoon:
        blur 1.0
    show monika turned eb:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with fade
    $ set_date(hour=16, minute=14)

    "As the session comes to an end and we finish up English, she looks at me."
    show monika ea md bc rhip 
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("monika")
    $ say_transition = False
    m "I was wondering if you might like to read through something I’ve written in my spare time."
    m ea ba rdown "It’s a little... offbeat, but after seeing your appreciation for English, I have the feeling you’ll find value in it."
    show monika ma
    mc turned mb "If you’ll do me the same honour. I might do a bit of creative writing on the side, myself, though I can't say it's much more than some shallowly drafted discord, loosely collected notes more than much else..."
    _mc mh eb "Shit. Why did I admit that?!"
    "Caught in my mumbling, she seems to cut right through the mental backpedalling I'd started myself on."
    m mb "Do you now? I think I would very much like to see what you’ve come up with."
    show monika ma at thide
    "I gingerly hand Monika a copy of a story I penned last week."
    hide monika

    if renpy.random.randint(1, 50) == 1:
        $ show_poem(mc_poem_1_monika, music=False)
    else:
        $ show_poem(mc_poem_1, music=False)

    $ advance_date(minutes=1)
    "She, in turn, passes me hers."

    $ show_poem(monika_story_1)
    $ advance_date(minutes=7)

    "Gracious."
    _mc mh ea bb "She said it would be offbeat, but nothing could have prepared me for THIS."
    _mc bg "I wonder if I might have been wrong to not probe about any possible problems in her life... Is she ok?"
    show monika turned mc:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    "Monika is digesting my story with raised eyebrows and parted lips that murmur softly."
    $ autofocus.block("monika")
    m md "{size=-6}This is brilliant.{/size}"
    show monika mc
    "She looks at me over the top of the paper."
    $ autofocus.unblock("monika")
    m mb "Done with mine, I see. What did you think of it?"
    show monika ma
    mc mf ba "It was... different."
    mc thinking mg bb "I thought it was cleverly constructed, even if the underlying meaning was slightly lost on me."
    m eb nb mb "Haha, well, I wouldn’t expect the meaning to come to someone on the first read, but hopefully it sinks in as time goes on."
    show monika ma
    mc ldown ef mb ba "I certainly hope so."
    m eb bc md na "Now, about yours."
    show monika mc ec
    "I wince slightly, bracing for impact."
    m ea ba md "Could I keep this?"
    show monika mc
    call blink(duration=0.3) from _call_blink
    "I blink at her a few times, unsure how to react."
    m mb rhip "You piqued my curiosity when you told me you liked English."
    m md "Yet now I find out you know Latin as well? How many more languages do you have under your belt?"
    show monika ma
    mc thinking ea mf bm "Well, er... just those two, aside from my native tongue in Japanese..."
    m ed mb rdown "That's still quite impressive! With this composition of yours, you've definitely got my full attention."
    m lpoint ea "I think you’ll be a perfect fit for my Literature Club."
    show monika ma
    "Her response leaves me flabbergasted, but not so much that I can’t recognise an opportunity."
    "A golden opportunity to spend more time with her."
    show monika ea
    _mc ea "But she’s not serious, is she?"
    show monika ldown
    mc ldown ml "Oh, uh, thank you..."
    mc mb "You asked if you could keep the poem, right? It was just uselessly taking up space in my bag anyway, so feel free."
    show monika ed at dip
    "Monika beams and stows the poem in her folder."
    _mc mh eb "Okay, she’s serious."
    show monika ea
    mc ea ml "Is the Literature Club on every day?"
    m lpoint mb "Yes, it is - right after classes."
    m ed "Don’t forget to bring a book to read and discuss - that’s what the club’s about, after all."
    show monika ea ma ldown
    "I rack my brain for any decent literature in my house that I'm familiar enough with, or am not embarrassed by. No luck."
    "What I do manage to come up with, however, is the idea of selecting a book from those strewn on the table."
    mc mb "I’ll keep that in mind, Monika."
    mc mg "Best be off now - see you at the club tomorrow?"
    m mb "Sure thing! Looking forward to seeing what you bring along."
    m ed mb "Do have yourself a nice evening."
    show monika ma at thide
    hide monika
    "I look over the books for one to slip into my bag."

    camera master:
        blur 0.0
        easeout 2.0 blur 1.2

    call screen branch_choice
    
    camera master:
        ease 0.6 blur 0.0

    stop music fadeout 3.0
    $ book = branches.to_book(branches.get_current())
    "Picking [book], I head off towards the lockers."

    scene bg school_lockers_afternoon with wipeleft
    $ advance_date(minutes=5)
    
    "Leaving the library, turning the corner and walking down the hallway, I finally make it to the front of the school where the lockers are."
    "I look around for my locker. Number 236."
    camera master:
        align (0.35, 0.4) zoom 3.0
    with Dissolve(0.2)
    "233..."
    camera master:
        ease 0.5 align (0.4, 0.405) zoom 3.02
    extend " 234..."
    camera master:
        ease 0.5 align (0.45, 0.409) zoom 3.03
    extend " 235..."
    camera master:
        ease 0.5 align (0.48, 0.41) zoom 3.04
    "Ah! There we are. 236."
    camera master
    with Dissolve(0.2)
    "As I take my shoes from my locker, I notice movement to my right."

    play music friendly_endeavours
    python:
        persistent.amelia_seen = True
        persistent.amelia.mark_cg(1)

    show cg amelia 1 at Flatten with cg_dissolve
    $ say_transition = True
    "Next to me is an old acquaintance of mine, Amelia."
    "She is just slightly shorter than me, and her long blonde hair makes her stand out among the other students."
    "Her uniform is much like mine and everyone else’s, albeit more on the loose side."
    "We don’t really speak to each other all that often, but Amelia would probably be one of the only people I know here."
    "Noticing my presence, Amelia speaks from behind me, still facing her locker."
    am turned me ee "Running behind? The 'Going Home' club already left."
    "I let out a light chuckle at her remark."
    mc turned eg mg "No, I’m not. I stopped by the library to pick up a book."
    am ec mb "You, a book? Have I known you to read books?"
    am mf ee "Becoming less and less of a weeb by the day, you are."
    show cg am_b with cg_dissolve
    am ec me bh "Traitor."
    show cg mc_b with cg_dissolve
    mc ed md "You can join me, you know."
    am eb me ba "In reading? Or becoming less of a weeb?"
    show cg am_a mc_a with cg_dissolve
    am ee mb "Either way, I have my streaming career. If that somehow turns out to be a bust, then I’ll consider your offer."
    "Amelia chuckles to herself."
    show amelia turned md eb bb:
        matrixcolor TintMatrix("#f5d5b6")
        i11
    _mc thinking ec mh bm "She makes a fair point. How much money did she make from that, again?"
    _mc eg ma bi "I remember it being more than my annual salary where I work. I’m not jealous though. Of course not."
    show cg mc_b with cg_dissolve
    mc md ed ba ldown "Well, Ms. Streamer, did you have the time to spare for a walk together, while we’re both here?"
    hide cg with cg_dissolve
    $ say_transition = False
    "Amelia finally turns around to face me, shutting her locker. I could see her hovering in my peripheral vision."
    am me "Really? We haven’t walked together for... how long?"
    show amelia ma ba
    "Her surprise worn loosely across her face, she latches her locker. Quickly, however, it fades into a smile."
    am ed mb lup "I’ve been waiting for you to ask that, you know. Come on~"
    show amelia ma

    scene bg school_street_afternoon
    camera master:
        align (0.7, 0.37) zoom 2.0
    with wipeleft
    $ advance_date(minutes=5, seconds=13)

    "Amelia and I began walking on our way back home."
    "Since we live somewhat close to one another, around the start of senior school we'd walk most of the way home together."
    "That hasn’t been the case for a little while, admittedly; at least since the start of the school year in April."
    camera master:
        align (0.0, 0.9) zoom 1.5
    show amelia turned md ed:
        matrixcolor TintMatrix("#ffecdb")
        xcenter 0.17 yanchor 0.8 ypos 1.0 zoom 0.8
    show bg:
        blur 1.5
    with Dissolve(0.2)
    "Taking a glance at Amelia, she seems to be focusing on something. She doesn’t say much; a contrast to how she usually is when I’m around."
    mc turned ml "Something on your mind?"
    show amelia eb with None
    show amelia at i11
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    am me eb "Not so much on my mind, but I’ve been thinking lately."
    show amelia bh ea mg
    mc ed md "Did it hurt?"
    am ed me "Aha, very funny."
    show amelia md
    "Her unamused sarcasm gives me life, I swear."
    am ea ba me "No, but honestly. Look at us. We made it through... how long? Nearly three years of high school now and between us, how many people do we know?"
    show amelia md
    mc ea mg bb "Oh, that’s easy. I know... well, a lot of people. I’m just not friends with any of them."
    am eb bb mb "See, that’s just it."
    am ef "If you consider the two of us from where we started, we’ve essentially gone backwards in our social skills after all this time. Well - {i}I{/i} have - You're about where you started."
    show amelia ma eb 
    mc ml bm ed "Uh-huh."
    mc ea mg ba "Alright, hit me with it."
    am me ba "I’m going to join a club. Sure, we’ve only got a couple months left, but..."
    show amelia md
    "My jaw drops, my eyes alight with incredulity."
    show amelia ma ea
    mc eb bb "No way. The president of the 'Going Home' club is quitting?"
    am ed lup mb bd "Now, I didn’t say that, but-"
    extend ba me " I just think it would be nice to get to know... well, someone at all, before I have to graduate."
    show amelia ldown mg
    "I pause and think for a moment."
    "I see what she’s getting at."
    "Even with all the time I’ve spent occasionally talking with people in my class, like Monika and… Yuri, was it? I still don’t really have anyone I’d call a friend."
    mc ea mb ba "This’ll surprise you, but I was thinking the same thing just earlier today. Monika invited me to join her Literature Club."
    show amelia ea md
    "Now Amelia takes her turn to pause."
    am mb bd ed lup "Really? That’s surprising. I thought only the students with the best grades were allowed entry - Top students in their fields and members of the student council or prefects."
    show amelia ma
    "I feign offence at her implication of my stupidity."
    mc ed md "I’ll have you know that Monika asked me to be her maths tutor today."
    show amelia ef ba ldown
    "She chuckles, clearly not believing me."
    am ed me rup "Sure sure. The point is though, for you - It feels like an odd choice. I would have pinned you for the Home Economics Club or something."
    show amelia md
    mc thinking ec ml "Huh. You know what? I never thought of that."
    show amelia ea md bf
    "She throws me an incredulous look."
    am me bg rdown "You’re kidding. We’ve been here almost three years, and you didn’t once think to look at a club that uses skills you already use on a daily basis?"
    show amelia md
    mc ed bm md "I guess not. Maybe I figured my time was better spent working?"
    show amelia ee ba ma at dip
    "Amelia shrugs. That’s a sentiment she’d agree with, at the very least."
    _mc ldown ba eg mh "Ah well."
    _mc ef ma "To be honest, I enjoy having that extra time to myself."
    _mc bb eg mf "If I were in a club, I’d have to head straight from there to work some days, and that wouldn’t be fun."
    am mb ed "I guess times change, huh? Both of us, growing up, doing bigger things?"
    show amelia ea md bb
    mc mb ba "Well, one of us is, at least."
    show amelia ed bh mc
    # SHE SAID IT
    # SHE SAID THE LINE
    # bruh
    "I snicker at my own comment, while Amelia pouts a little."
    am ec mf "Hey, I get paid more than you do!"
    show amelia mg
    mc ed md "To scream at video games or play stupid dating simulators all evening? Suuure, that sounds like great fun."
    show amelia ed mc bi
    "She clicks her tongue while I roll my eyes, chuckling."
    am lup ba me "Oh yeah. I’ve been thinking about what you said."
    show amelia md
    mc ea ml "Hm? What did I say?"
    am eb bb mb "About getting a house after I move out. I figured, once I graduate, I can stream full-time and find somewhere I can live that isn’t a cramped room."
    show amelia md ba
    "I pause my stride, confused."
    _mc thinking eg bi mh "When did I say that?"
    am ee me ldown "I mean, it was a long time ago, but still. I think it might be smart if I really start working toward something."
    show amelia md
    "Finally, it hits me."
    show amelia eb bb
    mc eb ml bd "Dude, I said that like two years ago! What the hell are you on about, thinking about it now?"
    show amelia ma
    "She simply smiles."
    am mb "Well, yeah, but hey. I gotta think about the future sometime, right? And with graduation coming up? No time like the present!"
    show amelia ma
    "I see where she’s coming from, but when did she grow up?"
    mc ldown ef mf ba "You’ve changed, haven’t you? Since then, I mean."
    am me ed ba "I mean, sure, we both have. That’s how getting older works."
    show amelia ma
    "She shrugs off my statement, but I don’t really mind. It’s odd to think about, really."
    _mc mh "How quickly things around you can shift. Reminds me of..."
    show amelia ea md
    _mc mf eg bi "Hey, let’s not go there today. I’ve been having a good day, thanks."
    show amelia bd
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ say_transition = True
    am me lup "You good? Looks like you’ve seen a ghost."
    show amelia mg with say_dissolve
    mc ef mj ba "It... It’s fine."
    show amelia ma with say_dissolve
    "She throws me a knowing glance. She at least sort of understands where I’m coming from."
    "I don’t think I ever told her, but she worked it out over time, I suppose."
    am bb ea me ldown "Hey, if you need to sit down for a minute, I’ll grab you a drink."
    show amelia ma ba with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She brings me over to a nearby bench, sitting me down on it. I don’t really think it was necessary, but... It’s odd how she seems to care so much for someone like me."
    show amelia ed md at lhide
    hide amelia
    "Then she races off toward the nearby vending machine, while I let my head roll back, and look up at the sky for a moment."
    show sky_afternoon at moving_sky with Dissolve(0.4)
    _mc ec mh "That bastard of a demon just tried to claw its way out again. I’m glad I'm still strong enough to push it back down where it belongs. I’ve been doing well lately, and I’d hate to have to fight it back off so soon after slaying the bloody thing."
    _mc eg ma "... Maybe I should talk to the boss about it again when I see him next."
    $ autofocus.unblock("amelia")
    window auto hide
    pause 1.0
    show black 
    hide sky_afternoon
    with Dissolve(0.3)
    stop music fadeout 2.0
    _mc ec mf "Man, Amelia’s taking her time over there - I wonder if she’s-"
    show bg:
        xalign 0.6 yalign 0.45 zoom 1.0
        ease 2.5 zoom 1.8
    hide black
    with NonBlockingDissolve(2.0)
    _mc bb eb mf "Wait, what the hell is {b}Kaito{/b} doing over there?"
    show amelia turned mg bh ec:
        matrixcolor TintMatrix("#ffecdb")
        t21
    show kaito turned mb bg:
        matrixcolor TintMatrix("#ffeede")
        t22
    $ persistent.kaito_seen = True

    play music ragtime

    "I make my way over to where a black-haired, weedy-looking guy leans up against the vending machine, his smug aura emanating so far out a to reach me from all the way from where I'd been sitting."
    camera master:
        align (0.15, 0.18) zoom 2.2
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("amelia")
    $ autofocus.block("kaito")
    $ say_transition = True
    am mf "You’re kidding, right? Why in the nine hells would I {b}ever{/b} help you?"
    show amelia mg with None
    hide amelia
    camera master:
        align (0.85, 0.1)
    with Dissolve(0.2)
    k lup bb mc "Well, don’t think of it as 'help', more like a sweet exchange between two former flames."
    show kaito ma ba with say_dissolve
    "I gag in my mouth - Former flame? What's he pulling out of his ass this time?"
    hide kaito
    show amelia turned mc ed bh:
        matrixcolor TintMatrix("#ffecdb")
        xcenter 0.23 yanchor 0.72 ypos 1.0 zoom 0.95
    show bg:
        blur 1.5 offset (100, -70)
    camera master:
        align (0.0, 1.0) zoom 1.25
    with Dissolve(0.2)
    "Evidently, so does Amelia, as she brushes him off and starts to walk back to me."
    show kaito turned lup ec mb bc:
        matrixcolor TintMatrix("#ffeede")
        matrixtransform RotateMatrix(0, 0, -25)
        tcommon(x=0.83, z=0.5)
    show amelia:
        blur 0.0
        easein 0.3 blur 1.0 xoffset -100
    camera master:
        easein 0.3 xoffset -50
    show bg:
        easein 0.3 blur 0.4 
    k "Oh, come on, Amelia~ You know what you’re missing, right? I'm sure you hear about it every day."
    show kaito ma ba with say_dissolve
    "I resist the urge to ball my fists, and instead focus on slow, steady breaths. It won’t exactly help to get worked up here."
    show kaito bc eb with None
    hide amelia
    show kaito:
        i11
        matrixtransform RotateMatrix(0, 0, 0)
    camera master:
        align (0.5, 0.1) offset (0, 0) zoom 1.2
    show bg:
        offset (0, 0) blur 2.0
    with Dissolve(0.2)
    k mc "Oh? Would you look at that? Melody, my old friend! How’s Sayori treating you these days?"
    show kaito ea ba ma with say_dissolve
    mc mm eb bj "Don't call me-"
    _mc mh "Alright, that’s it. Kaito’s finally about to find out what cement tastes like."
    camera master:
        zoom 1.6
    with Dissolve(0.2)
    "I march right up to him, raising my fist."
    show bg:
        blur 2.2
    show kaito mg ec:
        blur 2.0
    camera master:
        zoom 1.1 xoffset 100
    show amelia turned rup bh ee md:
        matrixcolor TintMatrix("#ffecdb")
        xcenter 0.37 zoom 1.31 ypos 1.0 yanchor 0.7
    with Dissolve(0.2)
    "Amelia, this time, stops me."
    am ed ba me "He’s not worth it, Mel. Come on, let’s just go."
    show amelia md ed with say_dissolve
    "I grit my teeth, almost unconsciously lashing out at Amelia for doing the same thing Kaito just did."
    show kaito:
        blur 0.0
        i22
    show amelia ec bh mg rdown at i21
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ autofocus.unblock("kaito")
    $ say_transition = False
    k ea me bc "Oh, that’s right. You and strawberry blonde aren’t on speaking terms anymore, no?"
    k ba rhip ee mf "Something about... What was it?"
    k ea me "Oh, right. A small... What was the word you used?"
    extend mb " 'Mistake', on your part?"
    "He gestures to both of us, grinning."
    k rdown mc ef lup bb "I’m amazed anyone would talk to either of you loners. Maybe that’s why you’re so good together, huh?"
    k ba ea mb "But, lucky for you, I’ve got something both of you will like."
    k ec mc ldown "Or, something you’ll both want to hear, at the very least. Come on, don’t be shy - Come a little closer~"
    show kaito ma
    "Again, I fight back the urge to drive my fist into his weedy, brainless face."
    $ autofocus.unblock("amelia")
    am bi mf "Anything you have to say isn’t worth the effort, Kaito. Now get lost."
    show amelia mg
    k bg mh ea "Is that any way to treat me? You know exactly what I’m capable of, Amelia. Surely, you don’t want a repeat?"
    k ba ee mf lup "All I ask is that you hear me out. I’ve heard that someone might be joining a certain book club."
    k ldown bg ea me "Be wary of those girls. They all have something to hide. Especially... Madame Presidente."
    show amelia at t11
    show kaito md at thide
    hide kaito
    "With that, he strides off back toward the school."
    show amelia ed bh me at dip
    "Both Amelia and I let out our held breaths, neither of us aware we were holding them in the first place."
    show amelia bd ea ma 
    _mc mm eg bi "I swear, every time I see his face, I get more angry."
    _mc mh "So much for my good day."
    
    stop music fadeout 2.0
    scene bg mc_living_room with longfade
    $ advance_date(minutes=19, seconds=17)
    play music pensive

    "Finally, I arrive home after seeing Amelia off."
    _mc turned eg mj bi "It’s been too long of a day, I swear..."
    "Shrugging, I sigh to myself as I glance around the room."
    camera master:
        align (0.25, 0.29) zoom 2.2 
    with NonBlockingDissolve(0.5)
    "Books I've never read rest inside their nooks, a television I've not bothered to use in months hangs joylessly upon the wall."
    "A section of the sofa greets me as I snugly relax into it, breathing a heavy sigh itself as my frame sinks into the cushion."
    "My hand arrives without invitation to my face, gently brushing down my features as it drops back to my side."
    _mc mh ec ba "Kaito's been getting to me more lately, hasn't he?"
    camera master:
        ease 5.0 align (0.75, 0.25)
    "My eyes lazily dance across the room, hoping to find something to distract me."
    "What they find, however, is somehow worse."
    "I click my tongue as they come to a rest upon a photo of my family, the only one I've left up over the years."
    "The witch, before she cut and dyed her hair, alongside my bastard of a father, one of the few times he was in the country."
    _mc eg bi ma "Though it's not like anything's really changed since then when you put it that way."
    camera master
    with NonBlockingTransition(fastfade)
    "Shaking my head, I push such thoughts aside and head for the kitchen."
    _mc ec ba mh "I should probably start on dinner, and now's as good a time as any."
    _mc ea "I'll sit down and read [book] as I eat. Probably the best way to do it, so that I don't distract myself with more study."
    "Leaving my bookbag behind, I douse the sobering atmosphere with thoughts of well-cooked meals."
    
    scene bg mc_kitchen_day
    camera master:
        align (0.0, 1.0) zoom 1.7
    with fade
    $ advance_date(minutes=29)
    
    "Around half an hour later, I allow myself a small nod."
    _mc turned ec "Looks like I'll be eating well for the next couple nights~"
    "Serving up a plate for myself, I divide the rest up into some containers - One for lunch, one for dinner tomorrow, and one to freeze for a rainy day."
    _mc eh "Just like I raised me to do~"
    camera master
    with fastfade
    "A few minutes of cleaning and packing later, the kettle finishes boiling."
    "I take a teabag from the box and look over my small collection of mugs, only to frown slightly when my eyes once again dredge up unpleasant memories."
    _mc ed bd mj "Come on, really? Why {b}that{/b} mug?"
    "Sighing, I shrug. It can't hurt me to use it; besides, if I don't, it'll just collect dust."
    "Taking it down, I give it a look over. It's an old, handmade clay mug, with the words 'MC + SK' haphazardly carved into the side."
    "It was a gift from an old friend of mine, something she'd taken weeks to make for my thirteenth birthday, but was so excited that she gave it to me a couple months early."
    _mc ec mh ba "It also was one of the last times I spoke with her..."
    "Shaking my head once more, I move on with brewing the tea, rather than wallowing in nostalgia."
    "Tonight has more important things on the agenda, and I won't be distracted by old memories."

    scene bg mc_living_room with wipeleft_scene
    $ advance_date(minutes=17)

    "After getting through my meal, I finally slide back onto my spot on the sofa and prop [book] between my legs."
    "I turn the first page... and I don’t stop turning until I reach the end."
    "I’m positively hooked on the story."
    "Hooked, potentially even more, on the prospect of joining the club."
    "Tomorrow can’t come soon enough."

    $ add_calendar_description(calendar_descriptions[None][0])

    return