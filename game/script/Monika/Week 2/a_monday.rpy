label week_2_monday_monika:
    call calendar_transition(hour=15, minute=1, day=30) from _call_calendar_transition_6
    scene bg class_1_gray with dissolve_scene_full
    play music playwme

    "Back at school again. Normally I wouldn’t complain, but I can’t help but find myself distracted."
    "Hell, I haven’t heard so much as a peep out of Monika since she left on Saturday!"
    _mc turned tail nostrands mh "How am I supposed to take that? What should I do?"
    _mc eb nb bb "... Oh God, what if she was waiting for me to message first, and I didn’t?"
    _mc eg bi mm "That’d be awful! It’d make me seem like I’m not interested at all!"
    _mc ea thinking ba na mh "What do I do? Seek her out during lunch? Wouldn’t that be weird?"
    _mc eg "Ok, think about this. Before we can really work out how to respond, we need to work out whether that was actually a date or not."
    _mc ec "Just because I took it that way doesn’t mean it is, but at the same time, she did get all dressed up for it..."
    _mc ea "What do I do? Pretend nothing happened until she brings it up?"
    _mc ldown ec "Maybe, but if she’s expecting me to talk about it, would it not make that worse?"
    show yuri turned e1d mh:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    y "Is everything-"
    show yuri mk b2a lup rup nb at hop
    camera master at vpunch
    play sound chairmoving
    "!!"
    "Both of us jump at the sound of her voice, albeit for slightly different reasons."
    y b2b mb e2b "S- Sorry!"
    show yuri ma
    mc bg ef nb mb "N- No, that’s my fault! I was just too deep in thought..."
    y rdown e3c b1d mh "Y- Yes, speaking of..."
    y ldown e1a b1a mb na "I just wanted to ensure you were alright. You seemed out of it all lesson."
    show yuri ma
    mc ea na ba mf "Oh, well..."
    y lup mh e1d "You can... talk to me about it, if you want to?"
    show yuri md
    mc ec bi "... Yeah, I think that would be nice. I just have no idea where to begin."
    y mb "Well, what’s currently on your mind? Perhaps you could start with that?"
    show yuri ldown e1a ma
    mc ea ba "I, ah..."
    _mc ec mh "Should I tell her? It might change her opinion of me..."
    show yuri md
    mc ef ml "I’m a little concerned about a friend."
    y b1d e2a mg "Mhm. I see."
    show yuri md
    _mc ec mh "Yeah, she’s not buying that at all."
    show yuri e1a b1a
    mc ea ml "Anyway, my friend hung out with another friend a couple nights ago, and now isn’t sure how they stand."
    show yuri e1d me
    mc ef mg "Like, it felt like a date, but was it? There wasn’t exactly much communication, so she... just isn’t sure. They haven’t talked since. It didn’t go poorly, but I guess she’s just a little awkward."
    y mg e1b "... Wait, that was you?"
    show yuri me
    mc ea bd ml "Huh? No, this was a friend."
    show yuri shy mb eb nd bc
    "She almost vanishes into her bangs."
    y bb md ea "You’re the one that went on a date with Monika? Why didn’t she..."
    show yuri mb
    mc eb mg nb "Hold on, it wasn’t- Wait, she told you?"
    show yuri eb nb
    "She looks away from me, clearly a little hurt. As for me, if I hadn’t ousted myself before, I definitely did just then."
    y md "Why did she keep that a secret?"
    show yuri ea bc mb
    mc ea ml ba na "Maybe she just didn’t think it was important?"
    y turned b1d e1a nb lup rup mh "Monika, going on a date? Of course that’s important. She’s never done that before, in all the time I’ve known her. Always avoided it like the plague, fearing how it might affect her reputation."
    y rdown e2a mg "With how elated she was, I’d assumed she’d met a boy that struck her fancy..."
    show yuri md
    mc ef mf "I..."
    _mc eb bd nb mh  "She was happy? Does that mean I have a chance?"
    y b1a e2b mg na "But if it was you, then that means..."
    show yuri shy ed ma nb ba
    "She hides deep within her bangs, but it does little to hide the wetness forming in her eyes."
    mc bg ea mg na "Wait, Yuri, hold on a second - what do you mean by that? What does it mean?"
    show yuri ef bc mb at rhide
    hide yuri
    "She shakes her head, turning on her heel and vanishing out the door."
    "I make to follow her, but by the time I reach the door myself, she’s vanished down the hallway."
    _mc thinking ec ba mh "Maybe she went to the bathroom?"
    _mc ea ldown ma "As much as I want to follow her to make sure she’s okay, I don’t want to invade her privacy. I’m sure she’ll be okay, she’s a big girl."
    _mc ef mh "... I hope. I really didn’t like the look on her face."
    _mc ec "But there’s not much I can do about it now. I just have to hope she doesn’t tell the rest of the club."
    
    scene bg club_gray with wipeleft_scene
    show sayori turned:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    $ advance_date(minutes=22)
    
    "As I walk inside the clubroom, I’m greeted by Sayori."
    s lup e3d mb "Heya, Melody!"
    show sayori ma at thide
    hide sayori
    show yuri shy eb bc mb:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t21
    show monika turned:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t22
    "Yuri hides behind her bangs, and Monika merely gives me a small smile before returning to her book."
    show yuri at thide
    hide yuri
    show monika at thide
    hide monika
    show sayori turned e1d b1d md:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    "Sayori frowns as she walks over to me."
    s mg "Did you do something?"
    show sayori mj e1a
    mc turned nostrands bi ec tail mj "Who, me? Naw..."
    show sayori lup e2a b2b
    "She bites her lip, a little concerned."
    s mh b2c "Sure seems like you did, to get such a lukewarm reception."
    show sayori ma ldown e1a at dip
    mc ef mf ba "Well..."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "She gives me a small smile, grabbing my hand and leading me over to a desk next to where she was sitting down."
    s b2b mb "C’mon, whatever it was, it can’t be that bad, right?"
    show sayori ma with say_dissolve
    mc eg ml "Yeah. Yeah, you’re right."
    _mc ec mh "Best to just let it slide for now, and wait for cooler heads to prevail."
    "At least, that’s what I thought was going to happen, but-"
    show sayori b1a me with say_dissolve
    stop music fadeout 4.0
    m turned mb "Alright everyone, I have an announcement to make."
    show sayori md at i43
    show natsuki turned b3a:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i44
    show yuri turned e2a b1d md:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i41
    show monika ma bc eb:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i42
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "As requested, we all gather around the front of the room. Monika walks out from behind the desk and bites her lip, clearly a little nervous."
    _mc ea "Nervous? What does she have to be nervous about? Wait, it’s not what I think it is, is it?"
    _mc mf ec "Is there something I’m missing here?"
    _mc ea mh "She’s not gonna... no, there’s no way she’d oust me right here in front of everyone. She’s far too..."
    show natsuki md
    m md ec "How do I put this..."
    show monika mc
    play sound heartbeat
    show black onlayer above_master with {"above_master": Dissolve(0.2)}:
        alpha 0.5
    _mc eb nb "Oh god, here it comes-"
    hide black with {"above_master": Dissolve(0.2)}
    show yuri e1b b1a
    show natsuki me
    m lpoint ba ea md "I’ve put our name forward to participate in the culture festival next week."
    show monika ma
    _mc mf "... What?"
    show sayori rup b2c mh zorder 3
    show natsuki b1d mi lhip rhip zorder 3
    show yuri lup rup b2a mk zorder 3
    $ autofocus.unblock("sayori")
    $ autofocus.force_focus("sayori")
    $ autofocus.force_focus("natsuki")
    $ autofocus.force_focus("yuri")
    "S & Y & N" "What?"
    $ autofocus.restore_focus("sayori")
    $ autofocus.restore_focus("natsuki")
    $ autofocus.restore_focus("yuri")
    show sayori me zorder 2
    show natsuki me zorder 2
    show yuri shy eb md nb bb zorder 2

    play music myconfession

    m mb "I know, we’re a new club, but I think it would be really helpful to draw in new members. I’ve been thinking lately, and the only members we have graduate in a few months."
    show yuri mb
    show sayori mj b2b rdown
    m ldown ec md "Is that really how we want the Literature Club to go down in history? A place that lived and died with a few people?"
    show monika mc ea
    n cross mh "Monika, I hear what you’re saying, but we all have duties to our classrooms as well, and you want us to put something on at the club as well?"
    show natsuki mj
    m rhip md "Well, it wouldn’t be something running all day, I was thinking something small that we could run here. Say, something that is nice and easy to get out of the way."
    m mb ed "So, I was thinking about some poetry readings!"
    show monika ma
    show sayori e3c me
    show natsuki e2a
    "I feel a collective shudder from the crowd."
    show sayori mj e1a
    show monika mc ea
    mc ef bg ml na "Monika, I, ah, don’t think that’s a great idea."
    show natsuki e1a
    show yuri bc
    m rdown mb "Why not? It’s something that is easy to do, and would bring in new members. Imagine how well it could go for us!"
    show monika mc
    mc ea mg "Yes, but you’re asking a group of introverts to perform in front of a crowd. That’s a big ask."
    show sayori b2c ma nb
    show natsuki e3c mm
    m lpoint mb "Sayori’s no introvert, and honestly, once Yuri and Natsuki open up, they’re hardly quiet either. She {i}did{/i} run for, and successfully become, a member of the student council, no?"
    m ldown ed "All we have to do is pretend it’s a regular reading in front of the rest of us."
    show natsuki fs tail nb mb eb bb
    m ec md "So, if we could practice over the course of the week, creating and reading poetry, then pick our favourite to read out come Monday, would that not be perfect?"
    show monika mc ea
    s mb lup e2a b2b "I... I’m not sure about this one, Monika."
    show sayori ma
    n turned ff lhip rhip e1a b3d mh "It’s not exactly going to scream, 'this is the literature club' if we read out our own poetry, considering that isn’t really what we’re used to doing."
    show sayori md b2c ldown
    n rdown e2a b1d mg "We’d be better off holding our own regular meeting and inviting people along to that. Besides, do we really need more members? I don’t know if we could fit too many more personalities in this room."
    show natsuki md ldown
    show yuri ee
    "Yuri only silently nods along to Natsuki’s statement."
    show yuri ea
    show sayori e1a ma na
    show natsuki e1a
    show monika bc
    mc mb "I know it feels like a really cool idea, to push our club into the public eye, but it might be more trouble than it’s worth."
    show monika eb ba
    "Monika frowns, then looks away."
    show monika:
        "monika turned bb eb ma"
        0.01
        "monika turned ba ea mc"
    "For a moment, I swear I see a softness shimmer in her eyes, before she blinks it away and turns back to face us."
    show yuri na ec
    m lpoint md "That may be so, but we need to think long-term. If we don’t replace the people we’ve lost, it will reflect poorly on us as a club."
    show monika mc
    show sayori me b1a 
    show natsuki b3a me 
    show monika ea
    y turned lup mh e1b b1a "So this is just publicity to you?"
    show yuri md
    "Suddenly, Yuri speaks up, a harsh tone in her voice."
    show sayori b2b me
    show natsuki md
    y e1d mi b3d "You think that this club, this safe haven, is something to be used as a commodity?"
    show yuri mj
    m bc md ldown "What? Of course not-"
    show monika mc
    y e1c mh b1a ldown "That’s what it feels like, isn’t it? That we’re being used to fuel something that isn’t just the warm environment we’ve grown to love here. Do you have no love for what this place represents to everyone?"
    show yuri md
    m eb bb md "I..."
    show sayori mj at t44
    show monika mc at t43
    show natsuki b1d mj at t42
    show yuri:
        0.21 
        "yuri turned nb lup rup b2c e1b me"
    "Natsuki intervenes, this time, placing a hand on Yuri’s shoulder."
    n e2a mh "Hey, Yuri, she gets the point. It’s not that bad."
    show natsuki md
    show yuri e1b b1d md lup rup nb
    s b2c mb "Yeah, it was only a suggestion, there’s no need to call her out like that."
    show sayori ma
    show yuri md b3c
    _mc ec mh ba "From what I know of Yuri, she would usually back down by now, but there’s something in her eye. Something... more."
    show monika nb
    show sayori md
    y mi e1d "But it wasn’t just a suggestion. You’ve already done it, right?"
    show natsuki e1a b2b mj
    y e2a mh rdown "You go and do whatever you want, with no consideration for the people around you. Is that fair?"
    show yuri e1d ldown mj b3d na
    "She turns to me."
    show sayori b1a 
    y mi "Would you drag someone who’s been in this club less than a week into something like that?"
    show yuri mj
    mc bd ea ml "Wait, hey now, I didn’t actually say-"
    show sayori b2b me
    show natsuki b1d me
    y mi "Or Sayori, would you appreciate being forced to speak in front of the entire school?"
    show yuri mj
    s mb lup nb "I mean, I did run for the Student Council alongside Natsuki, so it’s not-"
    show sayori mj 
    show natsuki mj
    y e1a b3c mh "Or Natsuki. Would you care to stand out of your comfort zone?"
    show yuri mj
    show sayori ldown
    n cross e1d mm "Look, Yuri, I don’t know what’s gotten into-"
    show natsuki b3a e1a me
    y lup mi b1a e1c "WHY? Why do you all regress upon every decision you make? Is it so difficult to settle on a cohesive argument for once?"
    show yuri mm b3c e1b
    show monika ec
    "I’m rendered utterly speechless. In all the time I’ve vaguely known her, Yuri was never, not once, like this."
    show natsuki e2a mm b1d
    s b2c mb lup "Yuri, it’s okay-"
    show sayori mj
    y b1b mi "Is it? Would you allow yourself to be pushed around so easily if it were anyone else?"
    show yuri md
    s ldown e1a tears_a mg "I-"
    show sayori b1a e1a notears me at t33
    show natsuki md at t32
    show yuri ma at t31
    show monika at lhide
    hide monika
    stop music
    play sound_loop running_int
    $ renpy.music.set_volume(0.0, 2.0, "sound_loop")
    "We all pause as Monika wordlessly leaves the room."
    show sayori e1a tears_a b2c md nb at thide
    "I don’t need to see her face to know the absolute anguish she’s suffering."
    show natsuki at thide
    hide natsuki
    hide sayori
    show yuri mj e1c b1a at t11
    "I don’t wait for a response before I follow her out, receiving a surprisingly sharp glare from Yuri."
    show yuri me
    stop sound_loop
    $ renpy.music.set_volume(1.0, 0.0, "sound_loop")
    _mc ec mh ba "'Of course she’d side with her.' That’s what she’s thinking."

    scene bg music_class_gray with Dissolve(2.3, time_warp=_warper.easein_cubic)
    pause 0.6
    play ambient ext_night fadein 2.5
    scene bg school_rooftop_gray
    show monika turned eb bb mc nb:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.7) * BrightnessMatrix(-0.06)
        i44
    with Dissolve(1.5, time_warp=_warper.ease)

    "There she is. I wasn’t entirely sure where she’d go, but I had a feeling it would be here or the music room."
    _mc "Glad to know I was at least right with my second guess."
    
    play music wtdgi 
    stop ambient fadeout 2.0

    show monika ea ba at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    mc turned tail nostrands ml ef "Hey."
    m eb bb "..."
    mc ea mb bg "It’s not your fault, you know?"
    m ec rhip md bc na "How could it not be? You’ve seen... exactly what happened. Everyone hated the idea, but it’s more than that."
    m eb rdown ba "They didn’t just hate the idea; they hated that I’d gone ahead and done it anyway."
    show monika mc with say_dissolve
    "She doesn’t look at me, her eyes drifting off into the wintry sky, listlessly."
    m md bb "I thought I had the agency to lead this club, that I understood what everyone wanted, but I clearly don’t."
    m ec nb mb "How could I lead a club I don’t understand?"
    show monika ma with say_dissolve
    mc mg ba "It’s nothing so spectacular, I assure you. They were just surprised."
    m mb bc "Were they? Even you didn’t like the idea."
    m ea md na "Why are you here, if you don’t support it?"
    show monika mc with say_dissolve
    mc ea mh "..."
    show monika ba with say_dissolve
    mc bg mg "Because I never said I didn’t support it. Neither did Sayori. We were just surprised, is all."
    mc mb "That’s how it goes when you drop a bombshell like that. I want to support you, Monika."
    show monika ec bc md with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She says nothing for a brief moment, before sighing."
    $ autofocus.unblock("monika")
    m rhip ba eb "Would you support someone who makes mistakes?"
    show monika mc
    mc "Of course. Everyone does; what matters is that you come back stronger from those mistakes."
    m bc md rdown "Would you support someone as argumentative and as stubborn as man could be?"
    show monika mc
    mc mg ba "It shows they have a strong will, and a great desire to believe in what they stand for."
    m ec md "And would you support someone who is so self-centred that she would throw every one of her friends under the bus for a small, pathetic little dream she had of a club she founded gaining a little staying power after she’s gone?"
    show monika mc
    mc ec ml "... I would. But that isn’t you."
    mc bg mb ea "You aren’t that person, Monika."
    m md ea "And what the hell would you know?"
    show monika ba mc nb
    "She turns to face me, a flash of utter anguish crossing her features."
    show monika eb bb ma
    "Then, as quickly as it arrives, it softens."
    m md bc "I..."
    m mb ec "You should go."
    show monika mc
    mc ml "Should I? Or should I stay, to keep you company? Even if we say nothing, I’d be happy."
    show monika eb ba mc
    "She looks away for a moment, back toward the drop below."
    m bb mb "You won’t be happy being around me."
    m rhip ec md "As I’m sure Yuri can attest to, I bring nothing but pain to all those who know me, one way or another."
    m ea md "So... Please, just leave me alone for a little while."
    show monika mc rdown
    "I grit my teeth."
    mc ef mf "Alright. Be safe, won’t you?"
    m ec mb "I will."
    show monika ma
    "I take my leave, stepping back into the roof’s entryway."
    
    scene bg school_rooftop_access_gray with wipeleft

    "Rather than returning to the others, I decide to wait just inside the access stairway for her to finally come back down. She can have time to herself, but..."
    _mc turned tail nostrands ec mh "I’m not going to leave her completely. Not if there’s any chance she needs me."
    _mc ef "Maybe that’s forward of me, but I feel like this is something I can’t back down on. Yuri’s like a sister to her; she can’t be taking this well."
    
    scene bg school_rooftop_access_night with Dissolve(3.0, time_warp=_warper.ease_cubic)
    $ set_date(hour=17, minute=57)

    "I’m waiting a while; club time is well and truly over."
    "But at long last, she steps back inside."
    show monika turned md nb:
        matrixcolor TintMatrix("#9fbcdd")
        t11
    m "Huh? MC?"
    show monika mc na
    mc turned tail nostrands bg mb ef nb "Y- Yeah."
    mc ml na ba "I... felt bad for how things turned out, and I wanted to give you some time to be by yourself."
    mc ea mg "But even so, I didn’t really want to leave you completely alone."
    show monika ma
    "She gives me a small smile. I can tell from the state of her eyes that she’s been crying."
    show monika mc
    mc mb "C’mon, I’m sure at least some of them are still waiting. Let’s go talk to them again, hey?"
    m ec md "No, I... I’m done for the day."
    m eb bb mb nb "But... If it isn’t too much to ask, would you mind walking me home?"
    show monika ma
    "Now it’s my turn to smile."
    mc ed md "Of course, it’d be my pleasure."

    stop music fadeout 2.0
    scene bg city_street_night_on with monika_pov(True)
    $ set_pov("m")

    "The streets are practically glittering in the evening light. It’s truly a sight to behold."
    _m turned mc "Part of me wonders just how I came to end up in this situation, but another part would rather simply let it happen, now that it is."
    
    play music dawn
    
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show melody turned tail nostrands mh ef at i11
    with Dissolve(0.2)
    $ autofocus.block("melody")
    $ say_transition = True
    _m "Strange though it may be, I can’t quite put my finger on it. Melody, this young woman beside me: Quite an enigma."
    _m eb bc ma "Striking in her beauty and careful in her finesse, she is quite possibly one of the most arrogant people I’ve ever met, and yet-"
    _m ea ba mc "Yet I can’t quite find it in myself to dislike her. Quite the opposite, in fact; I’ve grown quite attached. She’s more straight-laced than most our age, and carries with her a wisdom far beyond her years."
    _m ec "How curious, then, is it that she also comes across, at least at a glance, as incredibly naïve and short-sighted at times?"
    _m ea "I wonder what life choices, whether her own or otherwise, lead to the creation of one so endearingly passionate, but so adamant that such a fact remain hidden?"
    _m eb "Prior to joining the club, I had no idea she had passion for anything at all, outside of her studies."
    show melody nb with say_dissolve
    _m ea ma "Even then, while she worked in class, it was always as if it was only to serve a greater purpose. Perhaps she has goals beyond school?"
    _m mc "I know she said she hasn’t really decided on anything, but there’s... so much purpose to everything she does. She holds herself with such gravitas."
    mc ea bb mf "Hey, you... gonna say anything?"
    show melody mh with None
    show melody na
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("melody")
    $ say_transition = False
    m md nb "Oh, my apologies, I was just... thinking to myself."
    _m na bc mc na "My apologies? What am I, a diplomat?"
    mc ef mb lback rback2 "That’s alright, feel free. As long as it’s not awkward for you. I don’t really need to be talking to be comfortable."
    mc ba mf "... Usually."
    show melody mh
    "I want to comment, to make sure she’s okay, but my thoughts drift elsewhere."
    _m eb ba "It’s not that I often drift in my thoughts, but today has been... taxing, let’s call it."
    show melody eg ma bb
    _m ea md "Hm? Oh, Melody’s humming."
    mc mf "Some nights I stay up, cashing in my bad luck."
    show melody ma
    m ec mb "Some nights I call it a draw."
    mc ea bc ldown rdown mg nb "Wait, you know that?"
    show melody mh
    "I smile at her."
    m mb ed "Of course I do. It was a hit a couple years back!"
    mc ed ba na md "Sure was. Not sure why, but I’ve been having all sorts of recent songs stuck in my head; usually my music tastes are much older than that."
    show melody ma with None
    show melody ef
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "She says nothing, but wordlessly moves a little closer to me as she walks. I take it as a sign of her approval."
    "We continue on down the road a little ways, before we split. There’s no point in her walking me all the way; it would be dark long before she got home herself."
    "So, with that, we end our night there, a little closer than we’d started."
    stop music fadeout 1.0

    $ add_calendar_description(calendar_descriptions["monika"][4])

    call week_2_tuesday_monika from _call_week_2_tuesday_monika
    return