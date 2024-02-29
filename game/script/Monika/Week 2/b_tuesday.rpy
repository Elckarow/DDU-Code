label week_2_tuesday_monika:
    call calendar_transition(day=31, minute=22, hour=9) from _call_calendar_transition_7
    scene black with Dissolve(1.0)
    scene bg class_1_gray with mc_pov(True)
    $ set_pov("mc")
    play music pensive

    "After yesterday, for some reason, I’m feeling pretty exhausted. I didn’t exactly do much; I headed out and worked for a couple hours at the cafe after I got home and changed, but... not much else."
    _mc turned nostrands ec mh tail "Doesn’t really feel like physical exhaustion, either. More like... emotional?"
    _mc ea ma "Oh, wait, I know this feeling! It’s the one I get when I’ve been around people too long. What’d the witch call it, again? Emotionally drained, or something?"
    _mc eg mh "Ah, whatever. Not like it interferes too much with my ability to write things down."
    _mc ec "Just makes me want to ram my pencil down the throat of anyone who looks my way."
    _mc ea "... Yeah, I think I see the problem, now."
    _mc ma "But hey, the good news is, Monika doesn’t hate me."
    _mc ec bi mh thinking "Only... What’s up with Yuri?"
    _mc ba ea "... I mean, I know what’s up. I’d have to be a complete imbecile not to see it."
    _mc ef "More that I just wish there was something I could do."
    _mc ea "Should I back off?"
    _mc bi eg "Hell, can I, at this stage? Not like I’m expecting it to go anywhere, but..."
    _mc ec ba "I sure wouldn’t complain if it did, you know?"
    _mc ea ldown "It just means Yuri gets screwed in the process."
    _mc "I may not know her well, but to me, that seems..."
    _mc ec "A little cruel."
    _mc ea "Alright, here’s what I’m gonna do. I’ll play it safe for the time being. I’ll help Monika with her festival; it’s the right thing to do."
    _mc ma "I won’t do anything stupid or make any moves until after the festival, when we can all have the time to talk it out."
    _mc ec mh "It seems like the smartest move to make, for now. Besides, it gives me time to get to know them both, and the situation, a little better."
    _mc ea "Yeah, let’s do that."
    ".{w=0.2}.{w=0.7}."
    _mc eb mf nb "Wait, how did I get so far behind?!"
    
    scene bg class_2_gray with monika_pov():
        xzoom -1
    $ set_pov("m")

    _m turned ec mc "I can’t quite put my finger on it."
    "I click my tongue, tapping my finger against my temple."
    _m ba "This question has me stumped, and I’m not sure why."
    _m "It’s not exactly impossible; just slightly different when compared to what I’m used to. It makes it challenging to think outside the box to answer it."
    _m eb "Oh, perhaps that’s how I should approach it! By thinking of the question as a box, I should be able to better view it from an angle that might help me."
    _m ma ea "Fascinating, how complex mathematics is able to get at a higher level, at the very least."
    
    scene bg class_2_gray with fastfade:
        xzoom -1
    $ advance_date(minutes=16)

    _m turned mc "And..."
    _m ec nb "There. I can’t believe it took me that long, but at least it’s done."
    _m ea ma na "Nevertheless, it frees up my mind to focus on more important things."
    _m ec bc mc "... More important things than school? Goodness, my mind is falling apart these days."
    _m eb ba "Maybe this club is more trouble than it’s worth, absorbing so much of my study time. Running the Debate Club was at least clean, considering how much of the work there is standardised."
    _m ea "This school hasn’t had a literature club in over seven years; the records that once existed are outdated and obsolete; I looked through them at the start of the year for inspiration, but found nothing."
    _m eb ma "Instead, I had to create everything myself; it was a nightmare. I’m honestly thankful I had Yuri by my side to help me."
    _m mc "... Yuri."
    _m md "I can’t imagine why she would..."
    _m mc bc ec "No, now isn’t the time. I have things that need doing; at the absolute worst case, I can talk to Yuri after the festival."
    _m md "I sigh. Yuri and I have been friends for almost as long as I can remember; we’ve never had a fight this bad. Worse still, I have no idea what caused it."
    _m ea bb mc "Did I do something wrong? Or was she so offended by the idea of a performance that she reacted that way? It’s rare to see her do something so drastic. She never gets so emotionally involved in anything, not unless-"
    _m bc "... Not unless she has something to lose."
    _m eb "Not for herself, of course. Is she trying to protect one of the other members? Was someone reacting superficially in favour, but..."
    _m "Natsuki. It has to be."
    _m ec "I can’t believe I didn’t notice! Natsuki was hesitant at first, no wonder Yuri lashed out!"
    _m ea md nb ba "I... I don’t know what to do! I’ve already submitted the application!"
    _m ec na bc mc "Why did I do that? If only they weren’t due that morning, I could have talked to them about it sooner! Maybe we could have avoided all of this!"
    stop music fadeout 3.0
    _m bb md "Ahh..."
    call close_eyes(0.5) from _call_close_eyes_8
    "I slump into my hands, running my fingers through my hair."
    _m mc "What have I done?"
    _m "I’ve betrayed their trust, pushed everyone away from me."
    _m "Monika, you fool..."

    scene bg club_gray
    camera master
    with wipeleft
    $ set_date(hour=15, minute=33)
    play music playwme

    _m turned mc bc "Tardy, as usual. Most of the members beat me here, I assume-"
    show melody turned tail nostrands thinking ef mh:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    _m ba "What? Only... Melody? How strange."
    m mb "Hey, MC. I assumed I’d be the last one here."
    mc bb mg ea "As did I, actually. I’ve only just arrived myself. Maybe they thought we weren’t coming and left already?"
    show melody ldown mh
    m eb md "... I doubt it."
    show melody ef bf
    "Melody grimaces. It seems she’s thinking the same thing I am."
    _m ea mc "I’d be upset if I weren’t so disappointed. I can’t believe I let this happen, let this get so out of control."
    mc bf mb ea "But hey, we’ve got planning to do. Maybe they’ll show up later?"
    mc bb mf thinking "Or maybe they’re sick?"
    show melody mh
    m md eb "I saw Sayori in Form class, so she’s definitely here."
    mc ef bi mg "... I had chemistry with Natsuki and Form class with Yuri. They’re definitely all here."
    show melody mh
    m ea "Did... any of them say anything to you?"
    mc ldown eg mj "No, not a word."
    show melody ec ba mh
    "I struggle to hide my wince, but Melody catches it regardless."
    mc mb ea be "Hey, it’s not your fault, Monika. Come on, let’s get some stuff planned out. I’m sure Sayori at least has a good reason." # im stuff
    show melody ma
    m bc "... Maybe."
    show melody mh bf
    "She pauses, concerned, but probably because I've done the same."
    mc mf "What is it?"
    show melody mh
    m ea ba "... You’re thinking the same thing I am, right?"
    mc thinking ea ba mg "I don’t think it’s possible that Yuri’s managed to convince {i}both{/i} of them."
    show melody mh
    m ec bc mb "You’re right, I’m... overthinking it."
    mc md lback rback2 eh be nb "Hey, it’s okay. Everyone does when they’re stressed."
    mc mb na ea ba ldown rdown "Come on, I’ve had a couple ideas for how we could lay out the room when it happens."
    show melody ma
    "Her sweet smile helps, but the nagging in the back of my mind won’t leave me that easily. I’ll have to give it some time."
    "Nevertheless, I do appreciate what she’s doing for me."
    _m ma ea ba "I had no idea she was so friendly when I first met her. She was always so cold and distant... Is this what she’s really like when she opens up?"
    _m ec "How sweet."
    
    scene bg club_gray with mc_pov(True)
    $ set_pov("mc")

    "At long last, the other club members arrive."
    show sayori turned b2c:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    "First Sayori,"
    show sayori at thide
    hide sayori
    show natsuki turned e2a b3a mj:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t21
    show yuri turned b1d e2a md:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t22
    extend " then Natsuki, bringing Yuri with her. I suppose that means the two of them were convincing her to come."
    show yuri at thide 
    show natsuki at thide
    hide natsuki
    hide yuri
    show monika turned md lpoint:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    "Monika’s called everyone over once again."
    show monika ldown mc ec at t42
    show sayori turned b2c:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t41
    show yuri turned b1d e2a md:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t44
    show natsuki turned mj:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t43
    _mc turned nostrands tail ec mh "Here goes nothing."
    show monika ea
    n cross b1d mh "All I’m saying is, that we should have the chance to opt-out. If that’s something we can do, perhaps we can support in other ways?"
    show natsuki md
    s mh "But if we do that, there’ll be like one person speaking. That’s not exactly fair, is it?"
    show sayori mj b2b
    n e2a mm "Well, no, but- It’s also not fair to push people to do something they aren’t comfortable with."
    show natsuki md
    show yuri e1b b1a
    mc mf ea "I-"
    show natsuki b1a e1a md
    show monika ma bb
    show sayori md b2c
    stop music fadeout 3.0
    "The conversation drops instantly as all eyes turn to me."
    show bg:
        blur 2.0
    show natsuki:
        alpha 0.0
    show sayori:
        alpha 0.0
    show yuri:
        alpha 0.0
    camera master:
        align (0.2, 0.2) zoom 1.5
    with Dissolve(0.2)
    "Monika’s, pleading with me for my support."
    show monika:
        alpha 0.0
    show sayori:
        alpha 1.0
    camera master:
        xalign 0.0
    with Dissolve(0.2)
    "Sayori’s, who desperately wants to support her friend Monika."
    show natsuki:
        alpha 1.0
    show sayori:
        alpha 0.0
    camera master:
        align (0.8, 0.25)
    with Dissolve(0.2)
    "Natsuki, who wants to find a way to make something happen, but is too self-conscious to admit it."
    show natsuki:
        alpha 0.0
    show yuri:
        alpha 1.0
    camera master:
        align (1.0, 0.1)
    with Dissolve(0.2)
    "And Yuri, who dares me to try."
    show natsuki:
        alpha 1.0
    show sayori:
        alpha 1.0
    show monika:
        alpha 1.0
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    mc thinking mg "I think we really should, at the very least, hear Monika out. We treated her roughly yesterday, and that was unfair."
    show sayori rup e2c b2b
    show natsuki e2a
    show yuri e2b b1d
    "The eyes of the oldest members of the club look toward each-other, then toward Monika."
    show sayori b2c ma

    play music myfeelings

    n turned e3c b3a mh "Monika, I’m sorry for what happened yesterday."
    show natsuki md
    _mc bb mh "Woah, I didn’t know she had it in her to be so direct."
    show natsuki e1a ma
    s e1a rdown mb "Yeah, so am I. It was unfair of us to shoot down your idea without hearing you out."
    show sayori ma
    show yuri e2c
    show monika mc ba
    "Yuri, however, simply looks away."
    show sayori mj
    show natsuki md
    m md "Yuri, I-"
    show monika bb mc
    y e3c b1d mh "I don’t want to hear it, Monika. Please."
    y rup mg e2c b1c "Have your festival stall. I don’t..."
    show natsuki b2b
    y mh e1a b1d "I don’t want any part of it."
    show yuri e3c mj at lhide zorder 1
    hide yuri
    show monika eb nb at t32
    show natsuki e2a at t33
    show sayori md b2a at t31
    "She grabs her bag, making her way out of the room."
    show monika ea md
    "Monika looks toward me, both confused and distressed."
    m mb "I... I don’t know what I did wrong..."
    show monika mc
    show natsuki b1d
    s lup mb b2c "No, it’s not your fault, she’ll come around!"
    show sayori ma
    show natsuki e3c mm
    "Natsuki bites her lip, straightening up."
    n e2a b1a mg lhip "I’ll... go have a chat with her."
    n e1a b1d mb rhip "Just leave it to me; she’ll be on board lickety-split!"
    show natsuki ldown rdown ma e2a at lhide zorder 1
    hide natsuki
    show sayori at t21
    show monika at t22
    "With a small grin, she makes her way out the door, following Yuri. She leaves us behind, giving us a small nod, as she sees Monika trembling against the desk."
    mc ldown bg mb "Hey, Monika, it’s- It’s not your fault, okay?"
    _mc ec mh ba "I dare not breathe a word of what I know. It may cause more trouble than it’s worth."
    s ldown mb "Yeah, listen to Mel. We’re all here for you; if you want to do something with the club, that’s completely fine! We’ll support you, even!"
    show sayori ma
    m ec md na "I just... you’ve no idea how many times I thought about how to broach the topic... How many times I’ve worried about what you might say... and not once did it happen like this."
    show monika mc
    "I grit my teeth. She expected resistance from Natsuki, sure. Maybe the fact that Yuri was so resistant tempered her in some way?"
    _mc ea "But Yuri? Haven’t they been best friends since middle school? I can’t imagine how this might be affecting both of them."
    _mc ef "... Especially with what I know, now."
    _mc ea "But if... if Yuri has these feelings, why would she blow up at Monika? Would that not be counter to a wise decision?"
    show monika ea
    s e3c b2b mh "I know, but sometimes people do unexpected things. You can’t be prepared for everything, Monika. It depends on so many factors you’d never possibly be able to account for them all."
    show sayori e1a ma
    mc ef ml "Not to mention, there are always things you don’t know about people. It could be something that none of us could have ever known, that’s hurting her."
    m eb mb "... Yeah. Yes, you’re right."
    show monika bc md ec at dip
    "She stands up, breathing a sigh."
    m rhip mb bc "I’m truly thankful I have the two of you here. You’re the best friends one could ask for."
    show monika ea ma ba
    s lup e2a mb b2c nb "Of course, Monika. We’ll support you, both as the president of the club and as our friend. I can’t imagine how stressful it would be if you weren’t here, and I had to do it all! Ehe~"
    show sayori ma
    mc ed ba md "Yeah, I don’t know if I’d trust Sayori to run a club, personally."
    show sayori e1d ldown b1d md na
    show monika ed ma 
    "She pouts in response, but Monika starts to form a smile."
    m rdown eb mb "It’s not easy, not with the many personalities here."
    show monika ea ma
    show sayori e1a b1a ma
    mc mb eg "But that’s just it. You find a way to make it work. You always do."
    s mh "And even when you don’t personally know the answer, you have a team here. One that will help you find it."
    s e3c mb "Take Natsuki. She knew she was the best person to try and talk to Yuri, so she did. She’s on your side, no matter what she might say."
    show sayori ma
    mc ea mg "That’s gotta count for something, right?"
    show sayori e1a
    show monika ec at dip
    "Monika nods, agreeing."
    "We continue our discussion, as Monika slowly comes to understand that as much as she needs the club, the club needs her, too."
    
    stop music fadeout 2.0
    scene bg school_library_gray
    show yuri turned lup b1d e2a md:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i11
    with natsuki_pov(True)
    $ set_pov("n")
    $ advance_date(minutes=6)
    $ autofocus.block("yuri")

    n turned e1d b1d mg "I knew I’d find you here."
    y "..."
    n b3a e3c mi "Come on, we both have our moments, and Monika’s far from perfect, but that was uncalled for."
    n e1d b1d mh "She’s trying to do something to create a legacy for herself. That’s very clearly a dream of hers, and the absolute least you could do as her friend is hear her out."
    y "..."
    "I grit my teeth. I’ve always known her to be stubborn, but this takes the cake."
    n mm "You- Of all the arrogant, pig-headed, lazy, stubborn, holier-than-thou cretins I have ever had the displeasure to lay eyes upon, you take the cake! How could you possibly be so cruel to someone you supposedly care about?"
    n e1a b3d mi nb "What the hell is wrong with you?"
    y "..."
    n e1d b1d na mb "Oh, and of course, {i}now{/i} you decide to forget how to speak? The only time I want you to open your mouth?"
    y "..."
    n mm "Un-freaking-believable. And to think, I came all this way because I initially agreed with you. Let me guess, you’re only making a scene because you’re too shy to appear in front of people, so you’d rather take it out on your friend?"
    y "..."
    play sound slam
    show yuri e1a
    camera master at hpunch
    "I drive my fist into the bookshelf next to me, splintering the wood."
    n b3a e1b mh "You’re a freaking lost cause, Yuri. I can’t believe I wanted to be your friend."
    y e3c ldown me "..."
    $ autofocus.unblock("yuri")
    y e2a mg "Did you know Melody went on a date with Monika over the weekend?"
    show yuri md with None
    show black with NonBlockingDissolve(0.5):
        alpha 0.5
    "My blood runs cold as ice."
    n me b2a nb "Wh- "
    extend mg "What...?"
    
    scene bg school_street_gray
    show sayori turned:
        matrixcolor TintMatrix("#d8d8d8") * SaturationMatrix(0.8) * BrightnessMatrix(-0.01)
        i21
    show monika turned eb mc:
        matrixcolor TintMatrix("#d8d8d8") * SaturationMatrix(0.8) * BrightnessMatrix(-0.01)
        i22
    with mc_pov(True)
    $ set_pov("mc")
    $ set_date(hour=16, minute=55)
    play music rgb

    "I find myself walking toward home alongside both Sayori and Monika."
    "It’s been a good afternoon, all things considered. We’ve planned for this festival, gotten a heap of stuff sorted already. I’m actually pretty happy with the work we’ve done, even if Yuri doesn’t want to participate." # im stuff
    _mc turned nostrands tail ef bg mh "... I can’t help but think part of it might be my fault. She must think I’m some kind of monster, driving a wedge between her and Monika."
    _mc ea ba "But what else can I do? I can’t {b}not{/b} side with Monika, but every time I do, it feels like I’m sucking up to her!"
    show sayori md
    _mc eb bb "She’s just... right! There’s nothing wrong with siding with someone you agree with!"
    _mc ec ba "So why do I feel so guilty?"
    show monika ea
    s lup mg "Hey, Mel, you doing okay?"
    show monika ma
    show sayori e1d b1d md ldown
    "I grimace in response."
    s e2a mb "Well, that’s definitive."
    show sayori ma
    m rhip md "What’s bothering you, MC? Perhaps we can help. Goodness knows you’ve done more than enough for me over the last few days to warrant some return."
    show monika mc
    show sayori e1a b1a md
    mc ef mg "... No, it’s fine, I just- Just need some time alone, I think."
    m rdown md eb "Oh, that’s... that’s okay, we can give you some space. I have days like that, I know what it’s like."
    show monika mc
    mc ea bg nb mb "Y- Yeah..."
    play sound phone_notification
    phone register "s_n":
        time auto True
        "n" "Meet me back at school. Urgent."
    show monika ea
    pause 0.5
    s mh "Oh, sorry, that’s me."
    show sayori e2a md lup
    pause 0.8
    s e1a mb rdown "Hm? Natsuki wants me. Sorry guys, I’ll have to catch you tomorrow!"
    show sayori e3d ma at lhide
    hide sayori
    show monika at t11
    "She smiles and darts back in the opposite direction, toward school."
    m lpoint md "I guess I’ll take a slightly different route home and give you some space then, shall I?"
    show monika mc
    mc ml ba "N- No, I-"
    show monika ldown ma
    mc ef mf "..."
    extend mb " Yeah. That’s probably best."
    "As desperately as I don’t want to leave her side, I can’t bring myself to fight for it."
    _mc ec ba mh na "I’m as much a coward as I am a fool."
    m mb "Well, I’ll catch you tomorrow, if I don’t hear from you sooner. And, if you’re feeling better, send me a message! If there’s anything I can do to help, I’ll do it, alright?"
    show monika ma
    mc eh bg md nb "Y- Yeah, thanks Monika!"
    show monika ed at thide
    hide monika
    "I wave her off, and continue on down the road, now more lonely and cold than I was before."
    _mc ec na ba mh "... It’s better this way; gives me time to think about what to do next."
    _mc ea "About how to try and fix the mess I made."
    _mc thinking ec "First thing’s first, I need to try and keep up appearances. Monika needs my help, so I’ll be there for her."
    _mc ea "Second, I should try to talk to Yuri. O- Or shouldn’t I? I have no idea how that might go. I hardly know her, which doesn’t help."
    _mc ef "It’s... not exactly easy, navigating social environments, is it? I suppose that’s why I’ve gone out of my way to avoid it for so long."
    _mc ec "... Maybe I should go to someone who can help."
    _mc ef bg "But if I do, I’d have to tell them everything, and... I can’t do that. Not to either of them."
    "I breathe a heavy sigh, and follow my thoughts. I need to get ready for work."
    
    scene bg city_street_3_night_on with longfade
    $ advance_date(minutes=78)

    _mc turned nostrands coat_casual ma eg tail "I have to say, it’s been a while since I've been able to walk alone like this. It’s kinda refreshing, to an extent."
    _mc ea "I’m looking forward to-"
    show natsuki cross me b1d e2a:
        matrixcolor TintMatrix("#9fbcdd")
        t11
    _mc ec mh "Oh, Natsuki."
    n mg "Hey."
    show natsuki turned mj b1a
    mc mg ea "You were waiting for me? You could have walked with me, you know."
    n lhip b3a e3c mh "I know. But... There’s something I need to confirm for myself."
    show natsuki md
    mc bm mg ed "And what might that be?"
    n ldown e1a b1a mh "... Walk with me."
    show natsuki mj
    "I shrug. I’m not walking in the direction of home, so if she wants to walk, she’ll have to come my way."
    
    scene bg city_street_2_night_on
    show natsuki turned e2a mj:
        matrixcolor TintMatrix("#9fbcdd")
        i11
    with wipeleft_scene
    $ advance_date(minutes=10)

    "A little while later, we find ourselves most of the way to the cafe. Natsuki, all this time, despite wanting to talk to me, has said nothing. It’s making me a little nervous."
    mc turned nostrands coat_casual tail ml "H- Hey, Natsuki, what was it you wanted to-"
    n e3c b3a mg "Monika."
    show natsuki mj
    mc bd mg nb "H- Huh?"
    n e1d b1d mh "Did you go on a date with Monika over the weekend?"
    show natsuki mj
    mc mb eg bi "Christ -" 
    extend ea bd na " Hit me with a sledgehammer, why don'cha?" 
    mc ba mg "Besides, what’s it to you?"
    n b1a e2a mg "... So you did."
    show natsuki mj
    mc bi ef ml "Well, no, I didn’t mean that-"
    n e3c mi b3a "It’s fine. I just wanted to confirm."
    show natsuki me e1a
    mc ea bd mg "So you walked all this way to confirm something that doesn’t even affect you?"
    n cross e1d b1d mh "Well no, it doesn’t affect {i}me{/i}. It affects Yuri. And Sayori, and Monika, and you, and then by proxy, me."
    show natsuki mj
    mc mj eg bi "I still don’t quite understand."
    n mm "Do I have to spell it out?"
    n turned lhip e3c b3a mi "God, fine. Yuri. She’s upset with you, and that’s why she decided to rally so hard against Monika."
    show natsuki mj
    mc turned nostrands ed bm mg "Well, yeah, I knew that already, but what the hell did I {i}actually{/i} do? Is she just jealous, or-"
    n ldown e1d mh "... You stole her best friend."
    show natsuki mj
    mc ef mf ba "... Ah."
    n e2a b1a mh "There’s... a little more to it than that, but the point is, that now, pretty much everyone knows. Everyone, that is, except Monika."
    show natsuki b3a e1a me
    mc ldown bd mg ea "And you want me to tell her that all of her friends had a meeting behind her back to discuss her love life?"
    show natsuki e2a b2a md nb
    "She winces."
    n b2b mg e1a "N- No, it’s not like that, it’s-"
    n e3c b1a mh na "... Look. I don’t want to hurt her feelings. I don’t."
    show natsuki e1a md
    mc ec bi ml "But you have. Just because they haven’t been hurt yet, doesn’t mean that hurt doesn’t exist."
    show natsuki e2a b1d
    "Natsuki looks away."
    n mg "I know."
    show natsuki b3a e3c me at dip
    "She sighs."
    n lhip mb b2b e1a "Okay. I’ll tell her. It wasn’t fair to ask someone who wasn’t involved to cover for us; it’ll just make her upset with you, too."
    show natsuki e1a ma
    "She looks my way, her rosy-coloured eyes, looking directly into mine."
    "I don’t think I’ve ever been this close to her before, and I’ve definitely never truly locked eyes with her."
    n b2a mb "I’m sorry. It... This is my fault, and I’ll take responsibility for it."
    show natsuki ma
    mc ea ba ml "Your fault?"
    n ldown e3c b2b mb "Yeah."
    show natsuki b2a e2a ma nb
    "She looks away once more."
    n cross b3d mb "I’m the idiot who told Sayori about this earlier today, and because of that, she nearly changed her mind about the festival. She only decided to stay for Monika’s sake."
    n mh b3a "... And before that - During clubtime, it took the two of us forever to even find Yuri in the first place. She didn’t want to go to the club room, and well, I know why now..."
    n turned mb b2a e3c na "It was just a huge mess. I’m sorry."
    show natsuki e1a b2b mj
    mc bg mb ea "That last bit wasn’t your fault, Natsuki. It was mine."
    mc ef ml ba "... But, if you still insist on apologising..."
    show natsuki ma na
    mc ea mg "... I’m not the one you should be speaking to."
    n e2a lhip mb b2a "I know, I know. It makes it a little easier to get started, though."
    show natsuki ma
    mc bb eg mg "Yeah, that’s a feeling I know all too well. Sometimes it just gets... hard, to say the things you want to say."
    n ldown mg b1d "... Yeah."
    n e3c b3a mi "Sometimes, I wish it was easier to speak words."
    show natsuki ma
    mc eh md bg nb "The world would be a very different place, huh?"
    n rhip e2c mb "You bet."
    show natsuki ma
    
    scene bg cafe_outside_night_off
    show natsuki turned b3a:
        matrixcolor TintMatrix("#9fbcdd") * SaturationMatrix(0.8)
        i11
    with fade
    $ advance_date(minutes=10)

    "We finally arrive at the cafe, and I turn to Natsuki."
    show natsuki md
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    mc turned nostrands coat_casual tail mg "Well, this is me. I hope you have a good day, but please-"
    n b1a mb "Yeah. I’ll message her now, and see if she can catch up at all."
    show natsuki ma with None
    hide natsuki 
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    "I give her a small smile as she walks away. It’s about all I can muster."
    camera master:
        align (1.0, 0.5) zoom 1.8
    with Dissolve(0.2)
    "Then I pull out my keys, unlock the door, and make my way inside."
    
    scene bg cafe_inside_night
    camera master
    with wipeleft

    _mc turned nostrands casual tail ed md "Alright, time to get started."

    scene bg cafe_kitchen_day with fade
    $ advance_date(minutes=57)

    "As I dust flour off my hands, I nod to myself, a smile of satisfaction returning my gaze in the polished stainless steel in the various implements and decorations around me."
    _mc turned nostrands tail casual apron ec mh "Cleaning, making some of the longer-lasting food, working on some of the monthly checklist: all my regular duties."
    _mc ea ma "I almost always spend at least an hour or two working an afternoon here; it covers what money each week my main Saturday shift can’t."
    _mc "And whatever’s left ends up as savings, which is nice."
    _mc "The old guy trusts me to do my work, this late, and I’ve yet to let him down."
    _mc eh "Shows how much faith he’s got in me, to leave me in the store like this."
    _mc ec "But hey, it’s been that way for... probably the better part of three years now. Keeps me afloat, at the very least."
    _mc mh "I can’t imagine where I’d be if he hadn’t picked me up when he did. Probably the only good thing to happen that entire year, if I’m honest."
    _mc ef bi ma "Who would want some lonely middle-schooler that her own family didn’t want, after all?"
    _mc ec mh ba "... He saved my life, took me in. And I don’t know if I’ll ever repay that debt."
    _mc ef ma "I’ve learned more from him than... well, than I think I ever really learned from my own family."
    _mc ea "He taught me how to cook, do my finances, keep on top of bills, hell, even how to iron my own clothes. Sure, I knew how to do some of that before they left, but..."
    _mc eg "I guess it just made it easier."
    _mc ec "Hah, I guess I got that time to be by myself, after all."
    _mc "Sometimes that’s just... nice."
    _mc ea mh "Lately I’ve been crowded. Surrounded by people who, admittedly, are usually really nice, but it’s... a lot, sometimes."
    _mc ec "Before that, it was really just Amelia, and even then wasn’t all that often."
    _mc ef "We’ve... sorta grown a little apart, even the two of us, lately."
    _mc ea "Not that I don’t like her, I do, but she’s... a handful. She can be more intense than I’d be normally available for."
    _mc eg mj "Ah, Melody- where did it all go so wrong?"
    phone register "mc_m":
        time auto True
        "m" "Hey, I just wanted to apologise. I spoke to Natsuki and she clarified a few things. Apparently everyone was a little concerned about what happened over the weekend, so I wanted to make sure you knew. It was never my intention for that to be a date, and I really hope you didn’t see it that way. I’m sorry if it came across as crass, and if you... well, if you actually thought it might have been one, I’m terribly sorry for the misunderstanding. Melody, you mean quite a lot to me, as a friend, and I would be terribly hurt to lose you, especially like this. With that said, I hope you’ll find it in yourself to forgive me for what I’ve said and done. It was wrong of me to even let you potentially have the assumption that it could have been anything other than just two friends spending time together. And if you... if you feel that way about me, I... I really hope that this doesn’t sour our friendship, though I completely understand if it does.\nI truly hope to see you at the club tomorrow.\nMonika."
    _mc ec mh "Everything... just went a little sideways, somewhere along the line."
    _mc ea "These days, even just keeping track of myself seems an almost impossible task."
    _mc thinking "... Maybe I should lean on my friends a little more? I suppose it couldn’t hurt?"
    _mc ma "If it keeps me away from beings like Kaito, I suppose it might be worth it."
    _mc ec mh "And if there’s one thing I know, it’s that Amelia stays the hell away from him."
    _mc ldown ef bi "I don’t blame her, though. He’s a little sleazy at the best of times, and truly barbaric at the worst."
    _mc ea ba "Still, it seems she hates him more than me. I wonder what’s up with that? We went to the same middle school, from what I’ve gathered, but never talked."
    _mc ec "Whereas Kaito would follow Sayori and I around all the time."
    "I shiver at the memory, at how he would even dare to leer at Sayori."
    "Part of me is disappointed I never took the time to put him back in his place."
    "..."
    _mc ea ma "Ah, that should about do it; extra cleaning’s finished, I made a few new buns and pastries, and checked the ordering list."
    _mc eh "It’s about time I clock out and head home, I think."
    _mc mf ea "Oh?"
    _mc mh "A message? I can’t believe I missed it. Must have been really deep in thought."
    _mc ec "Hmm, Monika."
    stop music fadeout 2.5
    phone discussion "mc_m":
        pause

    play music wtdgi

    _mc eb nb mf nb "Wh- What?"
    _mc bg mh "M- Monika...?"
    _mc mf "I..."
    "Gobsmacked, I stare at the words on my phone."
    _mc ea_b mh "... How could I have been so blind? So stupid? The signs were all there; I just..."
    _mc "Missed every single one of them, and paraded forward anyway."
    _mc eb_b bf "And now Monika, and the whole club, has the wrong impression about me! They think I joined just to get close to Monika!"
    _mc eg bi na "... I wish I had a proper retort to that, actually... I suppose, in a way, that's exactly what I did."
    _mc ea_b "Shit."
    phone end discussion
    camera master:
        align (1.0, 0.9) zoom 1.6
    with Dissolve(0.2)
    play sound fall
    "I slump over a nearby chair."
    camera master
    show expression Gradient("#d8d0cc", "#75696b") zorder 5
    with Dissolve(0.3)
    "My phone drops from my hand, cluttering to the floor, as I stare at the roof."
    _mc ba mh "What have I done?"
    _mc "I allowed myself, for the first time in five years, to fall for someone who could never love me back."
    _mc "... I guess I reap what I sow then, don’t I?"
    _mc eg "Exactly what I deserve."

    $ add_calendar_description(calendar_descriptions["monika"][5])

    return