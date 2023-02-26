label week_1_monday_common:
    $ week = 1
    $ day = _("Monday")
    stop music fadeout 2.0
    scene bg class_day
    with dissolve_scene_full
    $ set_pov("mc")
    play music ohayou

    "I linger at my desk as the rest of my class fritters away and files out, chatting amongst themselves."
    "{i}What am I doing?{/i}"
    "{i}Why am I waiting for her?{/i}"
    "{i}Why would the popular, pretty Monika, the school star, even want to take me to revision practice? It’s just too good to be true...{/i}"
    "{i}A pipe dream, set to fade in a puff of smoke.{/i}"
    "{i}But I wait anyway, against all common sense.{/i}"
    "{i}Giving her lateness the benefit of the doubt.{/i}"
    "{i}She is, after all, President of a club and presumably busy.{/i}"
    "{i}What club is she in again? Was it Debate?{/i}"
    "{i}No... Literature, that’s it. She quit the Debate Club last year.{/i}"
    "{i}All in all, she's very, very...{/i}"
    show monika turned mb lpoint at t11
    m "Lovely!"
    show monika ma
    "{i}H- How did she know I was going to say that?{/i}"
    m mb ldown rhip "There you are!"
    show monika ma ed
    "{i}Calm down... She’s just remarking that it’s lovely you’re here. I think.{/i}"
    mc "H- Hi, Monika!"
    m rdown eb nb mb bb "Sorry, I’ve been looking in the wrong classrooms!"
    m md ec "I’m so forgetful sometimes..."
    show monika mc ea
    mc "It’s perfectly fine, Monika; don’t stress. Knowing me, I probably gave you the wrong classroom number."
    "{i}Why did I say that?! Oh god!{/i}"
    m ba na mb ea "I’ll accept that explanation if you insist."
    m rhip md "All set?"
    show monika mc at thide
    mc "Yeah, let me just... Oh, er..."
    "I quickly tuck my Akita Shonen volume (Love MAX, a perennial classic) back into my bag with a blush, trying to avoid Monika’s twinkly-eyed gaze."
    show monika ma ed
    mc "Yep!"
    "Shouldering my bookbag, I follow her out."
    hide monika

    scene bg school_corridor_day
    show monika turned bb mc at t11
    with wipeleft

    m md rhip "Something on your mind? You’re looking a little... Stiff?"
    show monika mc ba rdown
    mc "Not stiff, no, just curious."
    mc "I mean, what made you want to host a revision group? Didn’t think you, of all people, would need that sort of help."
    m mb lpoint "Everyone can improve. Also, I thought I’d assist some other people with their learning."
    show monika ma
    mc "How very humble and generous of you."
    mc "Where do I fit in, though?"
    m ldown md ec "We were in the same tutorials last year, so I thought you could lend me a hand with some things. You were pretty great in that maths competition last term."
    show monika ma ea
    mc "Oh. Right. I can certainly try."
    "{i}Did Monika seriously see that competition? I only did it for the extra marks... Oh God, she’s going to expect me to be so smart...{/i}"
    "{i}Wait, that sounded rude. Did that sound rude? Say something nice!{/i}"
    show monika mc
    mc "I’m certain you’re no slouch, either."
    $ Autofocus.Zoom = False
    m eb md bc "{size=-5}My parents might beg to differ.{/size}"
    show monika mc
    mc "Pardon?"
    $ Autofocus.Zoom = True
    m nb ed mb bb "Nothing. It’s nothing."
    show monika ma na ba
    "{i}I wonder what was up with that.{/i}"
    "I’m tempted to press for answers, but seeing her discomfort I ultimately err on the side of caution and change the subject."
    show monika ea na
    mc "Has your day been alright otherwise, Monika?"
    m rhip ec md "Mmm. Had a pretty interesting PE lesson with some of the girls in my class. Otherwise, nothing out of the ordinary."
    show monika mc ea
    mc "What were you up to?"
    m rdown md "Learning to pole-vault. I’m not too good yet, but I’m far from the worst."
    m mb "I could show you sometime, if you need help with that kind of thing."
    show monika ma
    mc "I’m sure I could still learn a thing or two from you. Athletics isn’t my forte."
    m mb lpoint "No kidding. I saw how you fared on Sports Day."
    show monika ma ed
    "{i}Oh no. She saw that too? Is there anywhere safe from looking like a complete idiot to her?{/i}"
    "I grimace at the memory."
    mc "Hey!"
    m ldown rhip mb "Relax, I’m just teasing."
    m eb md "You weren’t too bad. Just keep away from eggs and spoons and you’ll get through life without a hitch."
    show monika ea ma
    mc "Hmmph."
    "I smile at her, and we settle into a comfortable silence for a minute."
    "{i}Contrary to what one might think, I'm actually glad in spite of getting a jab thrown at me.{/i}"
    "{i}Monika’s mood has improved markedly, and I can almost relax.”{/i}"
    m rdown md "How about your day? What lessons did you have?"
    show monika ma
    "The hippopotamus of my memory wallows."
    "My most vivid recollection is of the waiting I did prior to Monika picking me up."
    "{i}Come on, noggin - don’t fail me now. What did I do today? I’m really proud of that picture in my history book... No! Not saying that! Uh...{/i}"
    show monika mc
    mc "Well, English stands out..."
    m md "You like English?"
    show monika mc
    "I take a moment to consider the question. Monika seems to have somehow lit up even more."
    m mb "Even when it doesn’t appear in manga or visual novels?"
    show monika ma ed
    "I stifle a snort."
    "An artful lunge for the jugular."
    "{i}The previous jab was good, but this is on another level entirely. How does she even know that? Nevermind. Stay cool.{/i}"
    mc "Actually, it’s quite an enjoyable subject for me."
    show monika ea
    "Monika’s smile broadens, tinged with what strikes me as undisguised approval."
    m mb lpoint "Well this is it. The venue for the study group."
    show monika ma

    stop music fadeout 0.8
    scene bg school_library_day with wipeleft
    play music okev

    "Monika flings open the door and strides in with me in tow."
    show monika turned lpoint mb at t11
    m "Hello everyone!"
    show monika ma
    "General murmurs of greetings emanate from around the room. I manage a small wave."
    mc "So, Monika... How shall we go about this?"
    m mb eb "We’re pretty free and easy here, so do whatever helps you clear your mind and study optimally."
    m ec md bc "If you need to take a break at any point in time, go right ahead. I might have a thing or two to help us unwind."
    show monika ma ea ldown ba
    "{i}Do I want to know what she has in mind?{/i}"
    "We go and sit at a nearby table."
    show monika at dip
    mc "So, who's first on your to-do li..."
    mc "I-I mean, {b}what!{/b} {b}What’s{/b} on the list, not er..."
    m eb nb mb "... I knew what you meant. Perhaps you’d go through Math with me now, then check my English at the end?"
    show monika ma
    "I skillfully bite back the awkward stuttering that my flustered brain is spitting out, and simply nod."
    mc "Ah, err... Sure."
    show monika ec mc bc na
    "She pulls a small, pristine green textbook out of her bag and sets it down on the desk,"
    show monika ea
    extend " before looking at me."
    m md ba "Do you not have a textbook of your own, MC?"
    show monika mc
    "{i}No chance I’m going to whip out my copy, with all my idle manga doodles in the page margins. I’ve already embarrassed myself enough today, thank you very much!{/i}"
    mc "I left mine at home."
    mc "Sorry."
    m ec md "That’s fine, we can share this one."

    show monika ea ma:
        subpixel True
        easein 0.5 zoom 1.0 yoffset 100

    "I pull my chair round so we’re sitting next to each other."
    "{i}How close can I sit without being weird? I need to see the page, but if I touch her shoulder, she might think I’m flirting back...{/i}"
    "{i}Didn’t set this outcome up. Honest.{/i}"
    "{i}Unexpected though it is, it’s definitely not unpleasant... Maybe she genuinely thinks I’m smart and wants my help?{/i}"
    "I hear whispers coming from the others. Whispers about Monika and myself. But I don’t care in the slightest."
    show monika eb mc bc
    "She gently turns the page and points at one of the questions."
    m ea md "See what I meant about being able to improve? I don’t understand what a periodic function is."
    m ba lpoint "Is it just like a function that repeats itself?"
    show monika mc
    mc "You could say that, although it’s more accurate to say 'a function that repeats its values regularly'."
    m md ldown bc "So, it’s a function that always gives the same outputs if you control the input values?"
    show monika mc
    "{i}Wow, she’s fast.{/i}"
    show monika ma ba
    mc "Yes, namely 'f of x equals to f of x plus T, where T is the period of the function'..."

    scene bg school_library_afternoon
    show monika turned afternoon at i11
    show monika:
        subpixel True zoom 1.0 yoffset 100
    with wipeleft_scene

    show monika at t11
    "As the session comes to an end and we finish up English, she looks at me."
    show monika eb md bc rhip 
    m "I was wondering if you might like to read through something I’ve written in my spare time."
    m ea ba rdown "It’s a little... Offbeat, but after seeing your appreciation for English, I have the feeling you’ll find value in it."
    show monika ma
    mc "If you’ll do me the same honour. I might do a bit of creative writing on the side, myself."
    "{i}Shit. Why did I admit that?!{/i}"
    m mb "Do you now? I think I would very much like to see what you’ve come up with."
    show monika ma at thide
    "I gingerly hand Monika a copy of a story I penned last week."
    hide monika

    if renpy.random.randint(1, 50) == 1:
        $ show_poem(mc_poem_1_monika, music=False)
    else:
        $ show_poem(mc_poem_1, music=False)

    "She, in turn, passes me hers."

    $ show_poem(monika_story_1)

    "Gracious."
    "{i}She said it would be offbeat, but nothing could have prepared me for THIS.{/i}"
    "{i}I wonder if I might have been wrong to not probe about any possible problems in her life... Is she ok?{/i}"
    show monika turned afternoon mc at t11
    "Monika is digesting my story with raised eyebrows and parted lips that murmur softly."
    $ Autofocus.Zoom = False
    m md "{size=-6}This is brilliant.{/size}"
    show monika mc
    "She looks at me over the top of the sheet of paper."
    $ Autofocus.Zoom = True
    m mb "Done with mine, I see. What did you think of it?"
    show monika ma
    mc "It was... Different."
    mc "I thought it was cleverly constructed, even if the underlying meaning was slightly lost on me."
    m eb nb mb "Haha, well, I wouldn’t expect the meaning to come to someone on the first read, but hopefully it sinks in as time goes on."
    show monika ma
    mc "I certainly hope so."
    m eb bc md na "Now, about yours."
    show monika mc ec
    "I wince slightly, bracing for impact."
    m ea ba md "Could I keep this?"
    show monika mc
    show blink
    "{i}I blink at her a few times, unsure how to react.{/i}"
    hide blink
    m mb rhip "You piqued my curiosity when you told me you liked English."
    m ec md "But with your composition right here, you’ve definitely snagged my full attention."
    m lpoint rdown ed mb "I think you’ll be a perfect fit for my Literature Club."
    show monika ma
    "Her response leaves me flabbergasted, but not so much that I can’t recognise an opportunity."
    "A golden opportunity to spend more time with her."
    show monika ea
    "{i}But she’s not serious, is she?{/i}"
    show monika ldown
    mc "Yeah, sure. Go ahead."
    mc "It was just uselessly taking up space in my bag, anyway."
    show monika ed at dip
    "Monika beams and stows the poem in her folder."
    "{i}Ok, she’s serious.{/i}"
    show monika ea
    mc "Is the Literature Club on every day?"
    m lpoint mb "Yes, it is - right after classes."
    m ed "Don’t forget to bring a book to read and discuss - that’s what the club’s about, after all."
    show monika ea ma ldown
    "I rack my brain for any decent literature in my house. No luck."
    "What I do manage to come up with, however, is the idea of selecting a book from those strewn on the table."
    mc "I’ll keep that in mind, Monika."
    mc "Best be off now - see you at the club tomorrow?"
    m mb "Sure thing! Looking forward to seeing what you bring along."
    m ed mb afternoon "Do have yourself a nice evening."
    show monika ma at thide
    hide monika
    "I look over the books for one to slip into my bag."

    python:
        route = route_choice("sayori", "natsuki", "yuri", "monika") # listen... yes i had to make a whole ass function / screen for that oerfbucorea^hi
        book = book_map[route]

    "Picking [book], I head off towards the lockers."

    stop music fadeout 0.8
    scene bg school_lockers_afternoon with wipeleft

    "Leaving the library, turning the corner and walking down the hallway, I finally make it to the front of the school where the lockers are."
    "I look around for my locker. Number 42."
    "39... 40... 41..."
    "Ah! There we are. 42."
    "As I take my shoes from my locker, I notice movement to my right."

    play music playwme
    $ persistent.amelia.mark_cg(1)

    show cg amelia 1 at CG
    "Next to me is an acquaintance of mine, Amelia."
    "She is just slightly shorter than me, and her long blonde hair makes her stand out among the other students."
    "Her uniform is much like mine and everyone else’s, albeit more on the loose side."
    "We don’t really speak to each other all that often, but Amelia would probably be one of the only people I know here."
    "Noticing my presence, Amelia speaks from behind me, still facing her locker."
    cg_am "Running behind? The 'Going Home' club already left."
    "I let out a light chuckle at her remark."
    cg_mc "No, I’m not. I stopped by the library to pick up a book."
    cg_am "You, a book? Have I known you to read books?"
    cg_am "Becoming less and less of a weeb by the day, you are."
    cg_am am_b "Traitor."
    cg_mc mc_b "You can join me, you know."
    cg_am "In reading? Or becoming less of a weeb?"
    cg_am am_a mc_a "Either way, I have my streaming career. If that somehow turns out to be a bust, then I’ll consider your offer."
    "Amelia chuckles to herself."
    show amelia turned afternoon md eb bb at i11
    "{i}She makes a fair point. How much money did she make from that, again?{/i}"
    "{i}I remember it being more than my annual salary where I work. I’m not jealous though. Of course not.{/i}"
    cg_mc mc_b "Well, Ms. Streamer, did you have the time to spare for a walk together, while we’re both here?"
    hide cg
    "Amelia finally turns around to face me, shutting her locker. I could see her hovering in my peripheral vision."
    am me "Really? We haven’t walked together for... How long?"
    show amelia ma ba
    "Her surprise worn loosely across her face, she latches her locker. Quickly, however, it fades into a smile."
    am ed mb lup "I’ve been waiting for you to ask that, you know. Come on~"
    show amelia ma

    stop music fadeout 0.7
    scene bg street_afternoon
    with wipeleft
    play music ohayou

    "Amelia and I began walking on our way back home."
    "Since we live somewhat close to one another, we used to walk most of the way home together."
    "Hasn’t been the case for a while though."
    show amelia turned afternoon md ec at t11
    "Taking a glance at Amelia, she seems to be focusing on something. She doesn’t say much; a contrast to how she usually is when I’m around."
    mc "Something on your mind?"
    am me eb "Not so much on my mind, but I’ve been thinking lately."
    show amelia bh ea mg
    mc "Did it hurt?"
    am ed me "Aha, very funny."
    am ea ba "No, but honestly. Look at us. We made it through... How long? Nearly three years of high school and between us, how many people do we know?"
    show amelia md
    mc "Oh, that’s easy. I know... Well, a lot of people. I’m just not friends with any of them."
    am eb bb mb "See, that’s just it."
    am "If you consider us two, we’ve essentially gone backwards in our social skills after all this time."
    show amelia ma
    mc "Alright, shoot."
    am me ba "I’m going to join a club. Sure, we’ve only got a couple months left, but..."
    show amelia md
    "My jaw drops."
    show amelia ma ea
    mc "No way. The president of the 'Going Home' club is quitting?"
    am ed lup mb bc "Now, I didn’t say that, but-"
    extend ba me " I just think it would be nice to get to know... Well, someone at all, before I have to graduate."
    show amelia ldown mg
    "I pause and think for a moment."
    "I see what she’s getting at."
    "Even with all the time I’ve spent occasionally talking with people in my class, like Monika and… Yuri, was it? I still don’t really have anyone I’d call a friend."
    mc "This’ll surprise you, but I was thinking the same thing just earlier today. Monika invited me to join her Literature Club."
    show amelia ea md
    "Now Amelia takes her turn to pause."
    am mb bc ed lup "Really? That’s surprising. I thought only the students with the best grades were allowed entry."
    show amelia ma
    "I feign offence at her implication of my stupidity."
    mc "I’ll have you know that Monika asked me to be her maths tutor today."
    show amelia ef ba ldown
    "She chuckles, clearly not believing me."
    am ed me rup "Sure sure. The point is, it’s an odd choice. I would have pinned you for the Home Ec club or something."
    show amelia md
    mc "Huh. You know what? I never thought of that."
    show amelia ea md bf
    "She throws me an incredulous look."
    am me bg rdown "You’re kidding. We’ve been here almost three years, and you didn’t once think to look at a club that you use on a daily basis?"
    show amelia md
    mc "I guess not. Maybe I figured my time was better spent working?"
    show amelia ee ba ma at dip
    "Amelia shrugs. That’s a sentiment she’d agree with, at the very least."
    "{i}Ah well.{/i}"
    "{i}To be honest, I enjoy having that extra time to myself.{/i}"
    "{i}If I were in a club, I’d have to head straight from there to work some days, and that wouldn’t be fun.{/i}"
    am mb ed "I guess times change, huh? Both of us, growing up, doing bigger things?"
    show amelia ea md bb
    mc "Well, one of us is, at least."
    show amelia ed bh mc
    "I snicker at my own comment, while Amelia pouts a little."
    am ec mf "Hey, I get paid more than you do!"
    show amelia mg
    mc "To scream at video games or play stupid dating simulators all evening? Suuure, that sounds like great fun."
    show amelia ed mc bi
    "She clicks her tongue while I roll my eyes, chuckling."
    am lup ba me "Oh yeah. I’ve been thinking about what you said."
    show amelia md
    mc "Hm? What did I say?"
    am eb bb mb "About getting a house after I move out. I figured, once I graduate, I can stream full-time and find somewhere I can live that isn’t a cramped room."
    show amelia md ba
    "I pause my stride, confused."
    "{i}When did I say that?{/i}"
    am ee me ldown "I mean, it was a long time ago, but still. I think it might be smart if I really start working toward something."
    show amelia md
    "Finally, it hits me."
    show amelia eb bb
    mc "Dude, I said that like two years ago! What the hell are you on about, thinking about it now?"
    show amelia ma
    "She simply smiles."
    am mb "Well, yeah, but hey. I gotta think about the future sometime, right? And with graduation coming up? No time like the present!"
    show amelia ma
    "I see where she’s coming from, but when did she grow up?"
    mc "You’ve changed, haven’t you? Since then, I mean."
    am me ed ba "I mean, sure, we both have. That’s how getting older works."
    show amelia ma
    "She shrugs off my statement, but I don’t really mind. It’s odd to think about, really."
    "How quickly things around you can shift. Reminds me of..."
    show amelia ea md
    "{i}Hey, let’s not go there today. I’ve been having a good day, thanks.{/i}"
    am bc me lup "You good? Looks like you’ve seen a ghost."
    show amelia bd mg
    mc "It... It’s fine."
    show amelia ma be
    "She throws me a knowing glance. She at least sort of understands where I’m coming from."
    "I don’t think I ever told her, but she worked it out over time, I suppose."
    am bb ea me ldown "Hey, if you need to sit down for a minute, I’ll grab you a drink."
    show amelia ma ba at dip
    "She brings me over to a nearby bench, sitting me down on it. I don’t really think it was necessary, but... It’s odd how she seems to care so much for someone like me."
    show amelia ed md at lhide
    hide amelia
    "Then she races off toward the nearby vending machine, while I let my head roll back, and look up at the sky for a moment."
    "{i}That’s a hell of a demon that tried to claw its way out today. I’m glad I pushed it back down where it belongs. I’ve been doing well lately, and I’d hate to have to fight it back off so soon after slaying it once again.{/i}"
    "{i}... Maybe I should talk to the boss about it again when I see him next.{/i}"
    "..."
    "..."
    "{i}Man, Amelia’s taking her time. I wonder if she’s-{/i}"

    stop music fadeout 2.0

    "{i}Wait, what’s Kaito doing over there?{/i}"
    show amelia turned afternoon mg bh ec at t21
    show kaito turned afternoon mb bg at t22
    "I make my way over to where a black-haired, weedy-looking guy leans up against the vending machine, his smug aura emanating from as far away as I am."
    am mf "You’re kidding, right? Why in the nine hells would I {b}ever{/b} help you?"
    show amelia mg
    k lup bb mc "Well, don’t think of it as 'help', more like a sweet exchange between two former flames."
    show kaito ma ba
    "I gag in my mouth."
    show amelia mc ed at dip
    "Evidently, so does Amelia, as she brushes him off and starts to walk back to me."
    k ldown ec mb bc "Oh, come on, Amelia~ You know what you’re missing, right? You hear about it every day."
    show kaito ma ba
    "I resist the urge to ball my fists. It won’t exactly help here."
    show amelia bi
    k eb bc mc "Oh? Would you look at that? Melody, my old friend! How’s Sayori treating you these days?"
    show kaito ea ba ma
    "{i}Alright, that’s it. Kaito’s finally about to find out what cement tastes like.{/i}"
    show amelia me ea bb 
    "I march right up to him, raising my fist."
    show amelia rup bd ma at dip
    "Amelia, this time, stops me."
    show kaito mg ec
    am ee ba me "He’s not worth it. Come on, let’s just go."
    show amelia md ed
    "I grit my teeth."
    show amelia ec bh mg rdown
    k ea me bc "Oh, that’s right. You two aren’t on speaking terms, are you?"
    k ba rhip ee mf "Something about... What was it?"
    k ea me "Oh, right. A small... What was the word you used?"
    extend mb " 'Mistake', on your part?"
    k rdown mc ef lup bb "I’m amazed anyone would talk to either of you loners. Maybe that’s why you’re so good together, huh?"
    k ba ea mb "But, lucky for you, I’ve got something both of you will like."
    k ec mc ldown "Something you’ll both want to hear, at the very least. Come on, don’t be shy. Come a little closer."
    show kaito ma
    "Again, I fight the urge to drive my fist into his weedy, brainless face."
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
    "{i}I swear, every time I see his face, I get more angry.{/i}"
    "{i}So much for my good day.{/i}"

    scene bg mc_living_room with wipeleft_scene

    "Finally, I arrive home after seeing Amelia off. It’s been too long of a day, I swear..."
    "Putting Kaito’s 'advice' somewhere never to be seen again, I slide into my armchair and prop [book] between my legs."
    "I turn the first page... And I don’t stop turning until I reach the end."
    "I’m positively hooked on the story."
    "Hooked, potentially even more, on the prospect of joining the club."
    "Tomorrow can’t come soon enough."

    return
