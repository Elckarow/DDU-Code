label week_1_saturday_monika:
    call calendar_transition(day=28, hour=6, minute=53) from _call_calendar_transition_5
    scene bg residential_day with dissolve_scene_full 
    $ autofocus.unblock("sayori")
    $ say_transition = False
    $ set_internet(False)
    play music cafe 

    _mc turned casual ec "Time for a good day."
    _mc ea "I’m not quite sure why, but I woke up in a really good mood. I had a good chat with Sayori late last night while we ate some ice-cream; it’s been too long since we last talked like that."
    _mc "Maybe it was just hanging out with her again that put me in such a good mood, but no matter what it was, I won’t complain. A lot better than how I was yesterday."
    _mc mh "But work will certainly help my mood, and then, afterwards..."
    _mc ef ma "Man, hanging out with Monika outside of school? It feels so surreal. I know it was a spur of the moment thing, but man, did that really happen?"
    _mc eb mh "... Wait. Didn’t we say we were getting dinner? Wouldn’t that be considered, like, a date?"
    _mc mf nb "Oh, god, wait- Does that mean if I go through with this, I fail the challenge with Sayori?"
    _mc eg bi mh na "No, no no! I can’t do that! But I also can’t flunk out on Monika, that would be awful..."
    _mc eb bd "What the hell do I do?"
    _mc ec ba "Man, as competitive as I am, I seriously can’t do that to her."
    _mc eg bi "... No, I can’t. I’ll go hang out with Monika, and take the loss."
    _mc ec "That’s just... what’s right. Besides, it’s just friends. We’re just friends. We haven’t even known each-other that long."
    _mc ea bb mf "Oh man, look at the time! I’m gonna be late for work if I don’t scoot!"
    
    scene bg mc_living_room with fade
    $ set_date(hour=17, minute=3)
    $ set_internet(True)

    _mc turned casual eg "Alright, finally home. I’m glad it wasn’t that hectic of a day; it gave me a chance to think about where to go tonight."
    _mc ea mh "I know just the place. I’m pretty sure Amelia mentioned it before. I can’t quite remember why, but I’m sure it’s fine."
    _mc ec ma "Just gotta ring up and reserve a table."
    $ renpy.transition(phone.config.enter_transition)
    $ phone.show_layer_at("phone_call")
    "A man picks up, briefly introducing himself and the restaurant."
    "I quickly state my intentions to book a table for this evening, and wrap up the conversation."
    $ renpy.transition(phone.config.exit_transition)
    $ phone.show_layer_at([])
    "The longer I was on the phone, the more I couldn’t shake the feeling that it feels like a date."
    _mc ec bi mh nb "Why am I so nervous?"
    _mc ea mf ba "Oh geez... I’m sweating bullets. I need a shower."
    _mc mh ec "Wait, gotta text Monika the details first."
    play sound phone_notification
    pause 0.5
    _mc ea mf "... Huh?"
    _mc na ec mh "Wait, that's not Monika, is it?"
    _mc eb bd "Did she read my mind?!"
    _mc eg bi "Calm down, Mel... calm down."
    _mc ec ba "Just check and see if it came from her or not."
    phone register "lit_club":
        time auto True
        "s" "Who wants another sleepover at my place?!"
        "s" "It'll be way bigger this time! A whole party!"
    phone discussion "lit_club":
        "m" "Oh? That sounds like fun. When would it be? I would need to get permission."
    _mc ea mf "Oh... another sleepover?"
    phone discussion:
        "s" "Hmmm"
        "s" "What about Saturday?"
        "n" "I think I should be able to do that."
        "y" "Oh? A sleepover? I did miss the chance to attend your last one..."
        "s" "Yeah! Come join us this time, Yuri!"
        "y" "I suppose I can do that... Saturday, you said? At what time?"
        "s" "Let's do it in the afternoon, at my place."
        "s" "Maybe straight after classes?"
        "m" "I believe I can organise that, but I'll let you know."
        "n" "Yeah, I think I can make that as well."
        "s" "Sweet! I'll see everyone there! Bring some snacks with you, and your stuff for sleeping. There's plenty of room!" # im stuff
        "m" "Alright, see everyone at club tomorrow! I look forward to this event!"
        "y" "Indeed."
    phone end discussion
    "I was so surprised that I hadn't typed up a response yet."
    _mc ec bi mh "Damnit, Mel, get it together!"
    _mc ba "I'll just leave a quick message here, then message Monika separately..."
    phone discussion "lit_club":
        "mc" "I dunno, I've got work that afternoon."
        "mc" "I might be able to come by after work?"
    phone end discussion
    _mc ea ma ba "Alright. Now to... message Monika."
    phone discussion "mc_m":
        time auto True
        "mc" "Hey, I've booked us a table at the place on the beachside north of the estuary for 7pm."
    phone end discussion
    _mc mh ec "There. 7 PM. Hopefully she doesn’t have the wrong idea too..."

    stop music fadeout 2.0
    scene bg mc_bathroom_afternoon with wipeleft_scene
    $ phone_available = False
    $ advance_date(minutes=3)
    phone register "lit_club":
        time auto True
        "s" "That sounds fine to me! Sleepover at 5pm, guys?"
        "n" "Works for me."
        "m" "Looks like I'll be able to attend!"
        "y" "As will I."
    $ advance_date(minutes=17)

    _mc turned messy nostrands naked mj eg "That was the longest shower of my life, geez. I just..."
    _mc ec mh "I dunno, I just got thinking."
    _mc ea "Thinking about tonight, sure, but about everything that’s happened lately."

    play music breeze

    _mc ec "This time last week, the only thing I cared about was getting school out of the way so that I could find work and start my life."
    _mc ef ma "Now, for some reason it feels... further away. Not like a bad feeling, either, but more like everything feels... more."
    _mc ea "I look forward to school more, to seeing people more."
    _mc mh "Maybe it’s because I’ve started to rekindle my friendship with Sayori. Maybe the club just brings out the best in me."
    "I bring my hand to my head, sighing."
    _mc thinking bi eg mj "I just don’t know."
    _mc ec mh ba "..."
    _mc "Sayori..."
    _mc ldown ef "I missed her."
    _mc ec "For so long, all I could think about was how crazy life has been lately. Now, it’s like none of that matters. Not the Witch, or that bastard. Like I can start really thinking for myself."
    _mc ea ma "From the moment I first walked into that clubroom, everything felt... more alive. More colourful."
    _mc mh "It’s crazy that I’ve changed so much in the past few days, but I’m not sure it’s all for the better."
    _mc ef "Sure, life seems good now, but... who knows when that’ll change again."
    _mc ec "... Monika always seems to have it together. I don’t know how she can be so confident and calm."
    _mc ea "It’s like she’s... barely even a person, more a loose collection of character strengths."
    _mc ec "Like she could do no wrong, the universe bending to her will."
    _mc ef ma "Hah, as if such a thing were possible."
    _mc ea mh thinking "I think, if anything, that’d be more likely to happen to someone like the Debate Club president Aika, who’s a little more casual and laid-back. She seems more the type to manipulate things behind the scenes for her own entertainment."
    _mc ec "Monika would be... more direct, I think."
    _mc ef "She’s not one to waste time messing about. She’d just do what she wants done."
    _mc ea ma ldown "Maybe I should strive to be more like her."
    
    scene bg mc_living_room with wipeleft_scene
    $ phone_available = True
    $ advance_date(minutes=30)

    "After finishing my shower, and taking... far too long getting dressed up, I head down to the living room, where I’d accidentally left my phone."
    phone discussion "mc_m"
    _mc turned bangs_b lipstick ec nostrands mh casual "No messages from Monika yet. That’s weird."
    phone end discussion
    _mc thinking ea "I wonder if she didn’t get my message?"
    _mc "Should I call her and check? Or might she still be busy?"
    _mc ec ldown "... I’ll give her another ten minutes, but if she hasn’t seen it, I need to let her know soon so that she can prepare."
    "My face flushes as I think of her 'preparing'."
    _mc eg bi mm nd "Ah, no no no! What am I thinking? Sayori’s bet!"
    _mc ec mh "Wait, why is this bet so important? I thought it would be obvious that I..."
    _mc ea ma na ba"Don’t like her. Because I don’t."
    _mc mh eb "I don’t. Right?"
    _mc mm bi eg "Argh, what is going on with me? Why am I so flustered over everything?"
    _mc ec mh "It reminds me of what happened right before Sayori and I stopped hanging-"
    _mc ba "... Before we stopped hanging out. Around the time I realised my feelings for her."
    "..."
    _mc bi eg "Dammit. Caught by my own logic."

    scene bg mc_living_room with fade
    $ advance_date(minutes=10)

    _mc turned casual bangs_b nostrands lipstick mh "... Still nothing. I’d better call her."

    window auto hide
    $ renpy.transition(phone.config.enter_transition)
    $ phone.show_layer_at("phone_call")
    pause 3.0
    $ renpy.transition(phone.config.exit_transition)
    $ phone.show_layer_at([])
    stop music fadeout 4.0

    _mc ec "Nothing. Very strange."
    _mc ea thinking "Should I head out anyway, even if I don’t hear anything?"
    _mc ec "... I’d rather look like a fool than accidentally stand her up."
    _mc ea "There’s always the chance she’s read the message and just hasn’t had the time to respond."
    _mc ma ldown "Yeah, let’s go with that. Even if that’s not what happened, I’ll still feel better having gone."
    _mc ec mh "Better to have been there and not have her show up, than to have her show up when I’m not there."
    _mc ea "Alright, that settles it. I’ll head off if I don’t hear anything in the next few minutes."

    scene bg restaurant1_night with longfade
    $ advance_date(minutes=40)
    if preferences.language is None:
        $ auto_advance_date_mult = 0.727
    $ set_internet(False)
    play ambient ext_night fadein 1.0

    _mc turned coat_casual nostrands lipstick bangs_b ec mh "Well, she’s definitely not here."
    _mc ea "Still, I’m a little early. Best to wait and see what happens."

    window hide
    camera master:
        align (0.0, 0.2) zoom 1.4
        ease 7.0 align (1.0, 0.8)
    with Dissolve(1.0)
    pause 6.9
    window auto

    "My feet shuffle awkwardly beneath me, and as if to sound a strange harmony in time, my fingers tap restlessly at my side in accompaniment."
    "..."
    _mc eg bi mh "Geez, what the hell is wrong with me? Since when did I start getting flustered so easily?"
    stop ambient fadeout 2.0
    m turned dress md "Oh, you came? I, ah... wasn’t really expecting you to be here."
    "I whirl around, and in front of me is..."
    camera master
    show monika ma eb nb at i11
    with Dissolve(0.2)

    play music tender_moment

    mc eb bb nb mf "Woah..."
    show bg:
        blur 2.5
    camera master:
        align (0.5, 1.0) zoom 1.7
        ease 6.0 yalign 0.2
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "Monika, in a stunning, flowing dress."
    mc bg ea mg "Oh, I, ah, but you didn’t need to-"
    m na eb md "You said something a little fancy, right? I just figured that this would do..."
    show monika mc with say_dissolve
    mc eb ba mg "N- No, I’m not complaining, but I, ah, just didn’t think it was, uh-"
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("monika")
    $ say_transition = False
    m eb rhip bb md "Sorry, I didn’t realise I overdid it... We can just call it a night, I didn’t mean to-"
    show monika ea mc ba
    "I reach out and gently grasp her arm as she tries to turn to leave, and she pauses."
    mc ef bg mg "N- No, what I’m saying is..."
    mc bf ea mb "You look really pretty."
    show monika eb rdown bc
    "She turns back toward me, avoiding my gaze."
    m mb ec nb "You... think so?"
    show monika nb ma
    mc na eh md ba "Yeah."
    show black onlayer above_master with NonBlockingDissolve(1.0):
        alpha 0.5
    "I nod, desperately trying to keep whatever the hell is boiling away inside of me down."
    _mc ec mh "I suppose I get it, now."
    _mc ef "I was trying really hard to push it down, to ignore it, but-"
    _mc ea nc "I have a crush on Monika."
    _mc eb bb "How did this happen?"
    show monika ea ba mc na
    _mc nd "Why am I on a date with Monika?"
    _mc mf "Oh god, what did I do? Do I deserve this?"
    hide black with {"above_master": Dissolve(0.2)}
    m md "Hey, you alright?"
    show monika mc
    mc bg eh md nb "Everything under control, situation normal!"
    mc ea ba mb na "Had a slight weapons malfunction, but uh, everything’s perfectly alright now, we’re fine, we’re all fine here, now, thank you. How are you?"
    m bc md "Uhh..."
    show monika mc
    mc ml "Y’know, Star Wars?"
    m md ba "Star Wars? I think I’ve heard of it, but..."
    show monika mc
    mc ec bi mf "You’re joking."
    m eb md "No, sorry... I know it’s a movie?"
    show monika mc
    mc ea ml ba "Well, actually, it’s six movies - Seven if you count the animated one - But-"
    mc eg mb "No matter. I know what we’re doing when we get back to my place."
    m rhip md ea nb "W- We’re going to your place?"
    show monika mc
    "I pause for a moment, the almost drunken feeling I’d been under since I walked in evaporating in an instant."
    mc eb bb nd mg "W- Wait, no, I didn’t mean like that, I just, ah, thought it would be nice to show you the movie, if you’d never seen it, because that’s like-"
    m rdown bc md ec na "I’m sorry, but I really should be heading home after this, I’ve got a full schedule tomorrow..."
    show monika mc
    mc ef ml bg nb "... I understand, I’m sorry. And I’m sorry for any misunderstandings, I was just-"
    show monika ea ba ma
    "She smiles at me, shaking her head slightly."
    m ed mb "I know, don’t worry. You were just worried that I’d gotten the wrong impression. We’re just spending time together; no need to get so worked up, okay? Just relax with me and let’s enjoy our evening."
    show monika ma
    mc eh md bf nc "Y- Yeah, let’s just... enjoy our evening."
    show monika ma ea ba na
    "Her smile doesn’t diminish in the slightest as the waiter approaches us."
    show monika mb 
    "The man asks for our orders, and after a little deliberation, we pick a shared entrée and each pick a main."
    show monika md lpoint
    "I didn’t go with anything special, but Monika? She leaned into the waiter’s ear to order. I didn’t get the chance to hear."
    m ldown ec mb "I told you, it’s a surprise. No need to look so nervous."
    show monika ma
    mc ea ba na ml "Well, it’s just that I ordered something so plain..."
    "I went with the Chicken Satay. You can always judge a restaurant by how good the satay is. The best places have their own recipes, which are made in-house."
    show monika ea
    _mc ec mh "I’ve never been here before, but it’s something the witch taught me all those years ago. You know, when she was around."
    show bg:
        align (1.0, 0.5) blur 2.0 zoom 1.5
    show monika:
        zoom 1.35 xalign 0.5
        yanchor 0.67 ypos 1.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    mc ea mg "So, Monika... Do you come here often?"
    show monika mc with say_dissolve
    "She gives me something of a blank stare."
    m ec bc mb "You’re joking, right?"
    show monika ea ba ma with say_dissolve
    mc teehee eh bg nb "Well, I, ah, couldn’t think of what to say..."
    show monika ed with say_dissolve
    "She just smiles, a small chuckle escaping her lips."
    m ea md "I know, I get like that too sometimes when I’m around people I don’t know."
    m mb lpoint "But we do know each-other. We worked on a group project together last year."
    show monika ldown ma with say_dissolve
    mc ea na ba mg "Well, yeah, but that was last year, and we didn’t really talk all that much, did we?"
    show monika mc eb with say_dissolve
    "She thinks to herself for a moment."
    m ec rhip md "You’re right, we didn’t, did we? That’s a shame. We’ve shared classes for so long, it’s almost hard to believe we never really talked all that much."
    m ea mb "But I suppose that changes now, doesn’t it, what, with you as a member of my club?"
    show monika ma with say_dissolve
    mc ed md "Hah, yeah. That’s true too."
    show monika mc with say_dissolve
    mc ea bb mg "Oh, I’ve been meaning to ask about that, actually. Why start a club with only a couple members, when you were president of the Debate Club for so long?"
    show monika eb ma nb rdown with say_dissolve
    "She shifts a little uncomfortably in her chair."
    m mb "That’s... a difficult question. More so than you would think."
    show monika ma na with say_dissolve
    mc ba mf "Oh, sorry, we can talk about something else if you want?"
    m ea bb mb "No, it’s fine, I just... was hoping to avoid heavier topics tonight."
    show monika mc ba with say_dissolve
    mc mb bb "Okay, let’s talk about something else. What do you like to do in your free time?"
    "She pauses to think for another moment. While these pauses in conversation are frequent, they aren’t uncomfortable. If anything, it gives me a chance to let out a little steam myself, with the rising pressure within me."
    m eb md "Well, I spend time working for the family, mostly..."
    show monika mc with say_dissolve
    mc ed md ba "Oh, you’re already working? That’s cool! I’ve got a part-time job too, it’s at a café on the other end of town."
    m ea md "Oh, you work at a café? That’s certainly something. I suppose you’d get to interact with a lot of people?"
    show monika ma with say_dissolve
    mc ef mg "I do, yeah. Honestly, I feel more at home there than at school. It’s really nice to just be able to focus on the tasks in front of me, not having to worry about the future all the time..."
    m eb mb "Yeah... That would be nice, wouldn’t it?"
    show monika ma ea with say_dissolve
    mc ea mb "So, tell me a little about yourself, too. I don’t want to hog the conversation."
    m mb "Me? There’s not much to tell, honestly. I go to school, I go home. Sure, I have cram school over the holidays, but that’s almost all over now that we’re about to graduate."
    show monika mc with say_dissolve
    mc ml thinking bb "Yeah... Have you thought about what you want to do?"
    m bc eb md "I have, but... I haven’t decided yet. There’s a lot to pick from."
    show monika mc with say_dissolve
    mc ef mg ba "There sure is, huh? Personally, I’m thinking it would be nice to do something a little more hands-on than university, but I don’t know."
    m rhip ea ba md "You’re good at maths, right? Why don’t you go into robotics?"
    show monika ma with say_dissolve
    mc ea ml bb "Huh, that’s a thought. It’s a rising industry too; it’ll probably have heaps of work in the future."
    m ed rdown mb "There you go, something to consider."
    show monika ma with say_dissolve
    "She smiles at me, nodding her head. I have no idea why, but every time we talk, she steers the conversation back toward me. Or maybe I’m the one doing it? I can’t quite tell."
    m ea md "Oh, I’ve got a question for you. I know that you haven’t really talked with Sayori all that much lately, but was there a reason the two of you stopped talking?"
    m bb mb eb "If it’s personal, you don’t have to tell me, but from the way she talks, at least, it doesn’t really seem like much. I was just curious about your angle."
    show monika ma ea ba with say_dissolve
    mc ba ef ldown mg "Well... That’s a tough one. Sayori and I stopped talking in middle school, long before we met you, or any of the other club members."
    m md "Apparently she met Natsuki not long after that, at least that’s what she told me."
    show monika ma with say_dissolve
    mc ed md "Sure seems like it, considering how tightly the two are glued together."
    show monika ed with say_dissolve
    "We chuckle a little bit, before resuming the conversation."
    show monika ea with say_dissolve
    mc mg bb thinking ea "There’s... not really much to tell. We didn’t have a falling out or anything, just... drifted in different directions."
    show monika mc with say_dissolve
    mc ef ba ml "Part of it was my family situation, I’ll admit..."
    m eb md bc "Oh, I’m sorry, I didn’t mean to pry into personal matters."
    show monika ba ea mc with say_dissolve
    mc ldown ea bb ml "It’s completely fine, you had no way of knowing. Besides, it’s not like it bothers me now. I just... live on my own, these days."
    m mb "Really? I can’t imagine what that might be like."
    show monika ma with say_dissolve
    mc ef ba mb "It’s not all that bad; you just have to make sure you’re making proper meals for yourself, paying each of your bills on time - I keep a spreadsheet for that, actually - and that your income is enough to match those expenses."
    m lpoint md "So your part-time wage is enough to cover all that?"
    show monika ldown ma with say_dissolve
    mc ea mg bb "Well, I work a couple hours most evenings, cleaning up the café, setting things up, doing what baking I can for things that’ll last until the morning, and I have my major Saturday shift."
    mc ec ml ba "Sometimes I’ll do the odd Sunday, too, when I need the money."
    mc ea mb bb "The house was paid off six or seven years ago, so I never needed to worry about the mortgage repayments, but yeah, it’s enough to keep just me afloat."
    mc md ed ba "Even have a little savings, which is always nice to have for emergencies."
    m ed mb "I would have never guessed you were so organised. That’s incredible!"
    show monika ma with say_dissolve
    mc eh bg md "Oh, honestly, it’s just life. When life gives you those lemons, you just gotta... make do, you know?"
    m eb mb "Amazing... I know it came from unfortunate circumstances, but that’s just... I can’t believe someone our age is so mature."
    show monika ma ea with say_dissolve
    mc ef ml "Oh, ah, well..."
    _mc eb nc bb mh "Wait, why is she complimenting me? What do I do?"
    mc ef mb na ba "It’s nothing, really. I just live my life like anyone else would. I’m honestly thankful to have a roof over my head some nights."
    m eb mb "... It must be hard. Living paycheck to paycheck."
    show monika mc with say_dissolve
    mc ea mg "Well, it’s not like I don’t have that buffer, I could live for a couple months off of that if I desperately needed to. It just gives me some security."
    m ea bc md "But there are also people who would... who would take all of that from you, in an instant, without a second thought."
    show monika mc with say_dissolve
    mc thinking ec ml "Oh, I’ve never been robbed or anything, my place doesn’t have enough stuff in it to look like a good target-" # im stuff
    mc ea mf "Wait, you mean..."
    m ec md "Yeah. People who have the money in the first place."
    show monika ea mc with say_dissolve
    mc ef bi mg "I... guess I’ve never really thought about it too hard. If I ignore them, maybe I’ll stay under the radar, you know?"
    m ec md "I don’t think that’s how it works..."
    m lpoint ba mb ed "But hey, let’s talk about something a little less depressing, shall we?"
    m ea ldown "Oh, I’ve got it! What’s your favourite subject?"
    show monika ma with say_dissolve
    mc ldown ba mf "At school? Man, I don’t know."
    m bc mb "Don’t you say lunch now, haha!"
    show monika ma with say_dissolve
    mc ldown ed md "Welp, you got me there!"
    show monika ed ba with say_dissolve
    "We chuckle."
    show monika ea with say_dissolve
    mc ea mb "No, but I have to think it’s probably physics. It’s crazy seeing how the world works, and how the universe is just a sequence of increasingly unlikely events that coalesced into what we see around us every day."
    m md "That’s fascinating, actually. I have to say, for me it would be either English or Music. I’ve gotten... a lot more into music lately."
    show monika ma with say_dissolve
    mc ml thinking "Oh, really? Why’s that?"
    m lpoint mb "Well, that’s some of Aika’s influence, believe it or not. She always wanted me to play an instrument with her when she was younger..."
    m ldown eb "I only recently picked up the piano, but I’ve been practising pretty hard whenever I get time."
    m rhip ec md bc "You should hear her play, though... It’s just amazing."
    show monika ea ba ma with say_dissolve
    mc ldown ef mg "I would have never picked Aika as the musical type, actually. I wonder why that is?"
    m rdown na md "Oh, she doesn’t have time to play anymore. Her family doesn’t own a piano, so she could only use the one at school, and running the club doesn’t give her the free time to use it."
    show monika mc with say_dissolve
    mc bg ml ea "That’s a real shame! Maybe we should do something about that..."
    m lpoint md "What, you want to join the Debate Club so she can pick up piano again?"
    show monika mc with say_dissolve
    mc bb eb mg nb "N- No, that’s not what I mean, I was more thinking, maybe we should come together to buy her a piano so she can play at home?"
    m ldown md ec "Do you have any idea how much those cost?"
    show monika mc with say_dissolve
    mc ef bi mf na "Well, no, but... I suppose that’s fair."
    m rhip eb md "I know, it was a nice sentiment, but if she really wanted to, she would have bought herself a keyboard. I think she’s content to just let it... drift away."
    show monika mc with say_dissolve
    mc ea bg mg "But we’ll be graduating in a few months. If she never gets the chance to play again, just because she has to run a stupid club-"
    show monika bb ma with say_dissolve
    "Monika’s eyes grow cloudy."
    show monika at i11
    show bg:
        blur 0.0 zoom 1.0
    with Dissolve(0.2)
    $ autofocus.unblock("monika")
    $ say_transition = False
    m ec md "Stop...  Please, stop."
    m ea mb "I know you’re trying to help, but... The reason she was forced to run the club was because I left."
    m eb md nb rdown "I’m the reason she dropped piano."
    show monika mc
    mc ef bg mf "... I see."
    mc ea bf mb "I’m sorry..."
    _mc eg bi mh "What the hell is wrong with me? Why am I saying all the things to upset her tonight?"
    m ba ec md na "Looks like the entrée is here, at least."
    show monika ed ma
    "Her misty look vanishes behind a mask of fortitude, as the waiter drops off the spring rolls we ordered."
    m ea mb "Please, enjoy some with me. It won’t be long before the main arrives."
    show monika ma
    "Her smile now taking centre stage upon her face, I can’t help but wonder how much of everything she wears is simply a mask."
    _mc ec ba "But don’t we all wear them, from time to time?"
    
    window hide
    with None
    with fade
    window auto
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    $ advance_date(minutes=6)

    "We spend a little time simply passing some small talk between us, little things like our favourite foods and colours, music tastes, and so on."
    _mc turned nostrands bangs_b coat_casual lipstick mh "Honestly, while we have some things in common, I’m actually a little surprised how few things we really match on. Not that it’s a bad thing; it gives us stuff to talk about." # im stuff
    _mc ec ma "We can’t agree on everything, after all."
    show monika md
    _mc ea "It’d be a little boring, you know?"
    m mb "Oh, look. Our mains are coming out."
    show monika ma
    "In front of me is placed a truly divine smelling satay. I can’t wait to taste it."
    "Monika, though-"
    mc mf "Is that-"
    m mb "Sure is."
    show monika ma
    mc bm ed ml "Ratatouille?"
    m lpoint md "See, I’ve seen a movie in my life!"
    show monika ed ldown ma
    "We both burst out into laughter, as we start to dig into our meals."
    
    scene sky_night at moving_sky
    show sky_stars
    with Dissolve(3.0)
    pause 2.0
    scene bg city_street_night_on
    show monika turned dress at i11
    with Dissolve(2.0)
    $ advance_date(minutes=37)

    m mb "Thank you again for a lovely night, I had a wonderful time."
    show monika ma
    mc turned nostrands bangs_b coat_casual lipstick mb "Oh, my pleasure, honestly. It was nice getting to know you a little better."
    show monika ec nb
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "She smiles, giving me a bit of an awkward hug before taking off. She has somewhere to be, it seems."
    hide monika
    camera master
    show bg:    
        blur 0.0
    with Dissolve(0.2)
    "All I can do is watch her figure grow smaller and smaller into the night."

    $ add_calendar_description(calendar_descriptions["monika"][3])

    call week_2_monday_monika from _call_week_2_monday_monika
    return