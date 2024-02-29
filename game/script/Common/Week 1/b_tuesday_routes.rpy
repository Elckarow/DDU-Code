#############################################################################################################
#############################################################################################################
#############################################################################################################

label week_1_tuesday_monika_1:
    show monika turned eb bb ma:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "Whatever funk came over Monika earlier still seems to be there."
    "I can see it written all over her as she twirls that distinctive pen of hers between her fingers."
    "For a moment, I consider approaching her to see if I can help-"
    show monika ec bc mc with say_dissolve
    "-Only for something to happen."
    show monika ea with say_dissolve
    "With a sudden effort, she straightens up in her seat and stops fidgeting, her face purposeful."
    "Looking much more like the star student that she is, she commits line after line to the paper."
    "Almost with nary a beat, and definitely with nary a correction."
    "It’s impressive to watch..."
    show monika ec md with say_dissolve
    "When she’s finally done, she pauses a moment and draws a small sigh,"
    show monika ed ma ba with say_dissolve
    extend " before flashing me a gorgeous smile, as if reassuring me that all is well."
    _mc eb nb mh bb "Darn. Did she know that I was watching her all this while out of the corner of my eye?"
    "In retrospect, I shouldn’t have expected anything less, really."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False

    return

label week_1_tuesday_monika_right:
    show monika turned md:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    m "You..."
    m "... You figured it out."
    show monika mc
    "I permit myself to beam with satisfaction."
    "It isn’t every day that I get to emerge from a bout of mental gymnastics on par with the school's resident prodigy."
    m ec md bb "I’m so glad."
    m mb eb nb "Here I was worrying that I might have ventured a little far off from my usual tack this time around."
    show monika ma
    mc thinking ea mg "It wasn’t all that obvious to me at the start, I must admit, but-"
    mc ldown mb "-I thought back to the story you showed me yesterday, and on close observation, some of the stylistic elements lined up."
    mc ef ml "The abstract format. The stream-of-consciousness style."
    show monika ea
    mc ea mb "So I latched onto those clues and made my choice."
    m ed na mb ba "Merely 'okay' in English, hmm?"
    show monika ma
    mc mg ef "Oh, you know. One really shouldn’t blow one’s own trumpet."
    m lpoint ea mb "Sometimes there’s no harm in making it known that you actually have a trumpet."
    show monika ma
    "I’m blushing now, though not simply from embarrassment, and can’t help but avert my eyes from Monika’s dancing emerald ones."
    "As flattered as I am, it almost feels like a little too much."
    m ldown eb bc md "I have to ask, though, MC..."
    show monika mc
    mc mf bm ea "Yes?"
    m ea md "... Was it just the style that gave me away?"
    m rhip ea "Or was there... anything else?"
    show monika mc
    call blink(0.4) from _call_blink_3
    "I blink, perplexed."
    show monika ea ba
    mc thinking bd mf ed "I’m not sure I follow."
    m rdown bb eb nb mb "Sometimes it’s more than just the writing style that makes an author’s work identifiable as theirs."
    show monika ma
    mc ml ed ba "You mean like... a personalised touch? Some elements from their own experiences?"
    mc ldown ea "A dash of their heart and soul?"
    m mb "It can be more than just a dash, sometimes."
    m ea ba na md "But yes, you’ve got the right idea."
    m lpoint ea mb "An outpouring of deep-seated emotion that infuses the work, linking it inextricably with the author’s own being."
    m ec md "Like Shakespeare once said: 'For I knew I could take my broken heart and place it on the stage of The Globe, and make the pit cry tears of their own.'"
    show monika ldown ma ea
    call blink(0.4) from _call_blink_4
    "I blink again, pondering her words."
    mc bg eh md nb "Good to know that I'm on the right path, at least - Makes me feel a little less lost."
    mc ea mg na ba "To answer your original question, however - No, I can’t say that anything apart from the style was what clued me in."
    "That may be the gospel truth, though the more I think about it, the more seeds of doubt begin to slowly creep up the vines of my mind."
    _mc ec mh "I’d be hard pressed to equate anything about Monika with the content of the poem itself, the contents of which being somewhat morbid, the more I consider it."
    show monika eb bb nb
    "Monika wears an odd expression as she considers my answer."
    "She looks almost relieved to hear it, and yet... disappointed, as well?"
    m mb "That’s... That’s good, then."
    m ec ba md na "Thank you, MC... for being so insightful."
    m ea mb "You really are shaping up to be a great fit for this Club."
    show monika ma
    mc ea mb "You’re very welcome, Monika. The pleasure is all mine."
    "I think that the whole exercise ended well."
    "Although as with yesterday, I’m left wondering about more than a few things."

    return

label week_1_tuesday_monika_wrong:
    show monika turned eb bb nb:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    "The moment I see Monika’s expression, I already know I’ve chosen wrongly."
    "And judging from the look itself, the true author’s identity is pretty obvious."
    "I bite my lip and shift uncomfortably in my seat."
    _mc bg mi nb "So much for being a good fit for the Literature Club."
    show monika ea
    mc be ed ml "I’m sorry, Monika."
    mc bf ef na mb "I really should have known, especially since I took a gander at something else that you wrote yesterday."
    "To my surprise and relief, Monika’s subsequent words are far from chagrined."
    m ma ed na rhip "Ahahah, it’s alright, MC."
    m eb nb mb "I can’t truly blame you; this poem’s admittedly rather different from the story I showed you."
    show monika ma
    mc ea mg bb "Not all that different, now that I look back and compare."
    mc thinking ba ec ml "The abstract format and the stream-of-consciousness style of the earlier story are actually present here, as well."
    mc bg eh md nb ldown "I guess I was trying to read too deeply into this poem to see the clues that were staring me right in the face."
    m md ea ba na rdown "Oh?"
    show monika mc
    mc ea ba na mg "Yeah. You know what they sometimes say about how there’s a little bit of the author’s heart and soul in their work?"
    mc ml "A touch of their personal experience?"
    mc ed mb "I was trying to look for that as I analysed the poem."
    show monika bc
    mc ef bf "And I ended up concluding that something with such a... well, morbid theme couldn’t possibly be associated with you."
    "Monika is looking at me very intently as I speak."
    "Which makes me belatedly realise the flaw in my reasoning."
    mc eb bb nb mg "Then again, I was probably presumptuous to associate it with any of the others, either."
    mc eg bi mj "I, ah- I think I’ll just shut up now."
    show monika ba
    "There is a brief, tense silence, during which I brace myself to have more dirt fill the hole I’ve just dug myself into."
    "But once again, the outcome is entirely unexpected."
    m md "That’s... a much more intuitive, empathy-driven approach to appraising literature than I would have given you credit for, MC."
    m bb mb eb "Sure, it didn’t net you the correct answer this time around, and even you yourself can appreciate that there’s pitfalls to the method."
    m ea ma ba "But I certainly don’t think any less of you for that."
    m ed mb lpoint "In fact, I’m pleased to see someone take a different tack and think outside of the box."
    m ma "We’re all here to learn and improve ourselves."
    m ea mb "And I’m positive you’ll eventually be in for great things."
    show monika ma
    mc ef bf mb na "You’re too kind, Monika."
    show monika ldown
    mc ea mb ba "I’ll try harder next time, and do my very best."
    _mc ma "Such a wise, nuanced response."
    _mc eg "I can readily see how she became President."

    return

label week_1_tuesday_monika_2:
    show monika turned md:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    "As her gaze falls upon the title of the book I retrieve from my bag, Monika’s expression changes."
    show monika mc bc
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("monika")
    $ say_transition = True
    "An entire range of emotions seem to flow through her pretty features within the span of just a few seconds."
    show monika ec ba ma with say_dissolve
    "Recognition, wonderment... Possibly even a note of sorrow?"
    show monika eb bb with say_dissolve
    "When her smile eventually returns, it’s not the same as it previously was."
    "It’s now tinged with wistfulness. Bittersweet."
    "The lingering suspicions I had yesterday are brought to the fore once again."
    "And this time around, I cannot help but voice my concern."
    show monika ec nb
    camera master
    show bg:   
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    mc mg "Is everything alright, Monika?"
    $ autofocus.unblock("monika")
    m na md lpoint ea ba "... Just pleasantly surprised, is all."
    m mb "I didn’t think I’d ever find anyone else who also appreciated Mishima."
    show monika ma
    _mc thinking ec mh "Again, I’m not sure if there isn’t more to this."
    _mc ea ma ldown "But in the interest of dispelling any awkwardness and keeping things positive, I bite."
    show monika ldown
    mc mb "Well, there’s certainly plenty to appreciate."
    show cg monika 1
    hide monika
    with cg_dissolve
    $ persistent.monika.mark_cg(1)
    $ say_transition = True
    "Monika inches closer. Her body language conveys an air to her I’ve never seen before."
    _mc mh "An air of vulnerability."
    show cg ec with cg_dissolve
    m turned ec mb "Do tell. I’m all ears."
    show cg ea with cg_dissolve
    "Shrugging aside my bemusement, I oblige her."
    mc ec ml "He really knows how to paint a tragic picture."
    mc ea mg bb "I don’t think I’ve ever encountered a more tortured, repressed individual in any work of literature than poor Kochan here."
    #lol just wait until you meet Nat
    # breh
    "Monika nods solemnly."
    show cg ec with cg_dissolve
    m md "It’s difficult enough to bare one’s true self in this day and age. I can only imagine what it must have been like back in the Forties."
    show cg ea with cg_dissolve
    mc mb ba eg "Mmm. Such a hypermasculine period in time, what with the war and all that."
    mc mg ea "And yet... That’s precisely what Mishima managed to do with this book. Bare himself."
    show cg eb with cg_dissolve
    "Her smile broadens, if only for a moment."
    m eb mb "You figured it out too, huh. That the story’s at least partly autobiographical in nature."
    mc ef mg "Even if you’re not familiar with Mishima the man, a lot of the story still feels much too raw, much too visceral to be purely made up."
    show cg ea with cg_dissolve
    m ea "Indeed. One can tell that it comes from within - that a good chunk of it is born of hard experience."
    show cg eb with cg_dissolve
    m eb md "That personal touch is what makes it speak to me."
    m mb "So personal that it’s sometimes impossible to read the book without feeling that I’m an intruder into Mishima’s life."
    show cg ec with cg_dissolve
    m ec md "A fly on the wall."
    show cg ea with cg_dissolve
    mc ea mb "Which brings to mind what we spoke about earlier - about an author’s emotions and experiences infusing their work."
    mc thinking bi eg mg "Granted, he literally masked the entire thing as a novel. But it still took a lot of guts to pour his innermost thoughts and fantasies onto paper."
    mc ef ba ml "... Not to mention go on to then publish them."
    show cg eb with cg_dissolve
    m eb md "It did. If only some of us were so courageous."
    "Silence descends again. I eventually break it by clearing my throat."
    mc ea mg "Moving back to Kochan."
    show cg ea with cg_dissolve
    m ea ma "Yes."
    mc ldown "While I pity the guy for having to conceal his true nature from the world... I can’t help but feel sorry for Sonoko, as well."
    "Monika sucks in her breath."
    m md "It’s a difficult situation for both of them, definitely. If only things could have worked out a different way."
    mc ml thinking ec bd "On the subject of Sonoko... I found it odd that Kochan would seek his mother’s counsel about marrying her."
    m mb "Did you now?"
    mc mg ea ba "Yeah. I mean, the story establishes almost from the get-go that he and his mother aren’t close."
    mc ml ef ldown "And yet there he goes, seeking her opinion about such an important decision."
    "There’s that pang of hurt again, crossing her face."
    show cg eb with cg_dissolve
    m eb md "Maybe he’s afraid."
    m mb "Maybe he’s hoping that his mother will advise him not to marry Sonoko, so he won’t have to refuse the poor girl himself."
    show cg ea with cg_dissolve
    m ea md "That way it would be her decision and responsibility, not his."
    show cg ec with cg_dissolve
    "Monika closes her eyes for a few seconds."
    show cg eb with cg_dissolve
    "When they open again, it’s as though she’s gazing off into a different reality entirely."
    m mb eb "I guess children can never really cut themselves free from their parents’ apron strings, can they? No matter how contentious their relationship is."
    "She bites her lip and glances away."
    "Meanwhile, I do my best to not grit my teeth at her statement; this entire topic has been digging heels into me."
    show cg ea nb with cg_dissolve
    m nb bb mb ea "Sorry for rambling. I... tend to get really caught up in stories that resonate with me."
    show cg ec with cg_dissolve
    "I immediately move to reassure her."
    _mc eb bf mh nb "How could I not? If she's in anything like a situation akin to mine, I..."
    _mc bg eg mi "I wouldn't wish such a thing upon anyone."
    show cg ea with cg_dissolve
    mc na mb ea ba "No worries, Monika. It’s always nice to see somebody so immersed in and passionate about a book they like."
    show cg na with cg_dissolve
    mc ec md "After all... This is the Literature Club, is it not? And what would a Literature Club be without that sort of spirit, hey?"
    "Monika seems to perk up at my words."
    m ba na "You’re a great listener, MC. And a fine connoisseur of literature to boot."
    show cg ec with cg_dissolve
    m ec md "I knew I wouldn’t regret inviting you to join me."
    show cg nb with cg_dissolve
    "A faint blush reddens her cheeks."
    show cg ea with cg_dissolve
    m ea nb "Did I say 'me'?"
    show cg na with cg_dissolve
    m mb na "Sorry, 'us'. I meant 'us'."
    "Before I have a chance to respond further, she swiftly composes herself and rises to her feet."
    $ renpy.set_tag_attributes("monika ma ba ea na")
    hide cg with cg_dissolve

    $ say_transition = False
    return

#############################################################################################################
#############################################################################################################
#############################################################################################################

label week_1_tuesday_yuri_1:
    show yuri shy bc eb mb:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i11
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "Of all the girls, Yuri seems to be having the most difficulty proceeding with her poem-writing."
    "I find this ironic, considering she was the one who suggested that we stick to a theme in the first place."
    show yuri ma ee with say_dissolve
    "For several moments, it seems as though she can barely even look down at the paper before her."
    show yuri turned e3c me b3d with say_dissolve
    "She anxiously shifts in her seat, brows knitted, lips pursed."
    show yuri lup e1d b3b with say_dissolve
    "When she finally puts pen to paper, the strokes are hesitant, jerky."
    "I’m on the verge of rising to my feet and walking over to ask her if she needs help..."
    show yuri ldown b3d mj e3c with say_dissolve
    "... When she abruptly rips up the paper and tosses it aside."
    "The unexpected noise makes everybody flinch, myself included."
    y e2b mb nd b2b rup "S- Sorry!"
    show yuri ma with None
    show yuri at i21
    show natsuki turned b3d mi:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i22
    camera master:
        yalign 0.15 zoom 1.3
    show bg:
        blur 1.2
    with Dissolve(0.2)
    "Natsuki snaps her head around and scowls,"
    show natsuki b1d e2c md nb at thide
    hide natsuki
    extend " but holds her tongue upon seeing how uneasy Yuri looks."
    camera master
    show bg:
        blur 0.0
    show yuri at i11
    with Dissolve(0.2)
    $ say_transition = False
    "I think I speak for the entire club when I cautiously ask."
    mc mg "Is everything alright, Yuri?"
    $ autofocus.unblock("yuri")
    y nc mb e1a b2a "I-It’s nothing, MC."
    y e3c mg b2b "I’m fine; just give me a moment..."
    show yuri mg nb b1d
    "Eyes closed, Yuri takes several deep breaths as if to steady herself, to focus."
    show yuri e2a b1a md
    "Before producing a fresh sheet and leaping right back into it."
    "Still not all that fluidly, but far better this time around."
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "I stand down and observe as she finally completes her task."
    show yuri shy ea na bc mc with say_dissolve
    "When she’s done, she looks up at me and flashes me a small smile."
    "It seems slightly forced..."
    "Also of note is the fact that she isn’t so much as briefly looking back upon what she’s written..."
    "As if she can’t bear to do so - as if the result isn’t entirely to her satisfaction."
    "But I can’t do much else but take her at face value, lest I come across as intrusive."
    _mc thinking mf ec "Perhaps it was just a bit of writer’s block."
    _mc mh eg "And as for not being entirely satisfied with what’s been committed to paper..."
    hide yuri
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    _mc ef ma ldown "... What author hasn’t been there, really?"

    return

label week_1_tuesday_yuri_right:
    show yuri turned e1d nc mh:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    y "Y- Yes, MC. That’s correct."
    y na mb "I must ask... How did you know?"
    show yuri e1a ma
    mc thinking mg "Well, I’ve read some of Monika’s writing prior and it didn’t fit with her style."
    show yuri e3d
    mc ec bi md "It definitely sounds too grim to be Sayori, either."
    "Was that Yuri stifling an amused smile at that last line?"
    show yuri e1a
    mc ldown ea mb ba "I have to admit, though, that what really gave it away was the mood. Gothic stories tend to convey that."
    show yuri e1d mf
    "Part of me braces for impact as I finish."
    "But much to my relief, Yuri is far from displeased."
    y e3d mc lup rup "That’s... very perceptive. A move worthy of Dupin himself."
    y e1a ldown mb "You must be one for Poe or the like, to recognize that theme... I’m surprised."
    y shy nc ea mc "Not in a bad way, of course..."
    "She fiddles with her hair."
    mc eh bb md "No problem, I know what you mean."
    _mc eb ba mh "She's a fan of gothic literature? Shoot, maybe I should have brought my collection... I thought it'd be too crass for a Literature Club..."
    "I grin softly to myself, before returning Yuri's gaze."
    mc ea mb "It’s a pleasure to find somebody else who appreciates his work."
    show yuri

    return

label week_1_tuesday_yuri_wrong:
    show yuri turned e2a b1d mg nb lup:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    y "No, um, MC. That poem isn’t hers - it’s mine."
    y b1a e1a mb "W- What made you think otherwise?"
    show yuri ma
    "I wince inwardly."
    mc eb mj nb "Um. Well."
    "When in doubt, tell the truth."
    show yuri e3c mj na
    mc ea mg na "I suppose I just never thought that something so dark could leave the pen of someone so..."
    stop music fadeout 2.0
    y mh b1d "Timid? Retiring?"
    show yuri mj
    "Yuri seems a little put out. I quickly move to placate her."
    mc mb "Hardly. I was actually about to say gentle and composed."
    y e1d b1b mk nc "Oh."

    play music myfeelings

    y e2b b2a mb nd ldown "S- Sorry. I didn’t mean to put words in your mouth. I just..."
    show yuri shy nd mb eb bc
    "She looks away, her frustration transforming into sadness."
    y md "I’m just tired of people presuming that, you know. That there isn’t more to me than being the quiet, introverted girl."
    y ee mb "That still waters can’t run deep."
    "I won’t lie. This gets to me."
    "I've just gone and done the same thing everyone else does, it seems... The same thing I'm constantly frustrated of others doing to me."
    "So I press on, giving her all the empathy I have to offer."
    show yuri ea
    mc mb eg bg "No, no, forgive me. I hear you completely."
    mc bf ea "I really shouldn’t have made such an assumption about you to start with."
    mc ea ba ml "I violated that age old rule of literature. You know - to not judge a book by its cover?"
    mc ec bi mg "It’s a mistake I definitely won’t make again."
    show yuri turned b2c nc ma lup rup
    "She turns back to me with an expression that tugs at my heartstrings."
    y mb "P- Promise?"
    show yuri ma b2a at thide
    "I offer the warmest smile I can muster."
    mc ed md ba "Cross my heart."
    hide yuri

    return

label week_1_tuesday_yuri_2:
    show yuri turned e2a lup:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "Now that Monika has let us off to read, my mind wanders to Yuri."
    "Sitting quietly at a desk with her nose buried in her Poe volume."
    _mc thinking mh "Our shared taste in reading material leads me to think that she and I might be able to bond further."
    show yuri b1d md with say_dissolve
    _mc ma "Plus, her poetry was beguilingly dark."
    _mc ldown ed "I’d like to see some more of that enchanting darkness peek out from beneath her soft exterior."
    _mc ef "Not too much, though. That gentle demeanour is rather cute."
    _mc eb mh "Speaking of cute... The way she intermittently twirls a lock of her hair as she reads?"
    _mc eh ma "Surpisingly endearing."
    show yuri:
        alpha 0.0
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "I go to my bag and retrieve my copy of {i}The Black Cat{/i}."
    _mc ea mh thinking "I think it’s an easy bet that she’s read it, too, if she's a fan of the Gothic."
    _mc ma "Discussing it, therefore, should be the perfect ice-breaker."
    show yuri:
        alpha 1.0
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    "I move over towards her, admiring how deeply engrossed she is in her tome."
    "Her eyes trained steadfastly on the pages."
    "As if willing herself to be transported into whatever magical world lies within."
    "I wait until I’m standing right next to her and gently tap her shoulder."
    mc ml ldown "Yuri?"
    show yuri rup e1d b2a mk nc with say_dissolve
    stop music fadeout 1.0
    "She startles and looks up at me, flustered."
    y e2a mb nb b2b "Oh! It’s you, MC."

    play music playwme

    show yuri ma with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("yuri")
    $ say_transition = False
    y ldown rdown e1a b1a mb "Is there something I can help you with?"
    show yuri ma
    mc mg  "I was wondering if you would like to discuss some horror."
    mc mb "Your poetry gives me the impression that you’d be something of an authority on it here."
    show yuri shy mc eb nc
    "She blushes at my statement."
    y na ma ea "I think 'authority' might be a bit of a stretch."
    y ee "But I’ll concede that out of everybody here, I’m the one who likes that genre the most."
    y turned e1d mh "Surreal horror, in particular. It can be very effective at changing your view on the world, if only for a moment."
    y e1a mb rup "Is there anything in particular you’d like to talk about?"
    show yuri ma
    "I produce my copy of {i}The Black Cat{/i}."
    mc mb "Whatever you’d like to, really, but I reckon Poe’s {i}The Black Cat{/i} might be a good place to start."
    mc mg "I read it yesterday; perhaps you’ve done so before, too?"
    show yuri rdown e1d
    "Her meekness fades."
    "I can see that she finds both confidence and comfort in her passions."
    y e1a mb "I’m familiar with that one, yes."
    show yuri ma
    _mc ed ma "Bingo."
    y e3c mh "I find it such a haunting story... Such a stark commentary on guilt, morality and the human condition in general."
    show yuri md
    with None
    show cg yuri 1 
    hide yuri
    with cg_dissolve
    $ persistent.yuri.mark_cg(1)
    "Yuri’s speech and tone have undergone a dramatic change, her words now fluent and precise."
    "As if she was knowledgeable on this topic, discussing it many times before."
    "I am captivated."
    mc md ed "Do go on. I’m all ears."
    y turned e2a mh "The narrator commits some truly unspeakable acts of violence. His pets, his wife - all of them suffer terribly at his hands."
    y mg e3c b1d "He professes guilt and shame after the fact."
    y e1a mh "And yet... his immediate impulse is to solve the problem by removing what he perceives to be the source of his guilt. His victims."
    "I stare at her, impressed by her insightful observation."
    mc ea ml "You’re absolutely right. It’s classic projectional behaviour."
    mc mb "And you know what they say - There’s an immediate solution to every problem, which is almost always the wrong one."
    mc ml "His remedies were nowhere as permanent as he thought they would be."
    y mg e1d b1a "Yes. After all, Pluto apparently returned in the form of the second cat, and his wife’s murder was eventually uncovered."
    y e2a mb "I suppose guilt just follows you around, doesn’t it? One way or another."
    mc ml "It needn’t necessarily have."
    mc mg "What happened in the end could have been averted if he repented and desisted after his very first misdeed."
    y e3c b1d mh "Or if the coward realised that the source of his guilt actually lay within himself."
    y mg "And if he directed his destructive impulses inwardly instead."
    _mc mh "I won’t lie."
    _mc ed bf ma nb "I’m slightly taken aback by Yuri’s feverish intensity as she utters those foreboding words."
    _mc na ba mh "In a bid to lighten things up a little, I raise what I hope is a valid counterpoint..."
    _mc ea ma "... One with a note of positivity."
    mc mg "Is anyone truly beyond redemption, though? Even him?"
    mc thinking ec ml "If the narrator is to be believed, he was once a decent human being, still capable of kindness."
    mc eg mb "Deep down inside, that good person might very well still be there."
    mc ml ec "Sure, what you’re suggesting is a means of solving the problem."
    mc ea mg "But is it anywhere more right or anywhere less cowardly than what he did?"
    mc ldown ec mb "I think there’s an argument that it requires more courage to own up and redeem oneself, rather than take the shortcut to eternity, so to speak."
    "I wince ever so slightly at my own words, finding it difficult to believe them, myself."
    _mc ef mh "After all... some people probably don't deserve second chances."
    "I fight to stop my gaze from drifting to the girl in the corner of the room; the one who could do no wrong."
    "The one who would forgive me as easily as the wind might pluck the seeds of a dandelion."
    "My attention returns to my front when Yuri nods, her face solemn."
    y e2a b1a "You make some good points."
    y mh b1d "It’s open to debate just where the line should be drawn for a chance at redemption, though."
    "She sighs."
    y mg e3c "And the narrator is admittedly so unreliable, addled by drink, that it’s perhaps worth taking his claims of prior normalcy with a pinch of salt."
    show yuri shy eb bc:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    hide cg
    with cg_dissolve
    "With that, Yuri’s shy demeanour seems to return."
    y mc "Do, er, you want to go and speak with your friends? To Monika or Sayori?"
    "I look at her, puzzled. Have I upset her? Why would she change so hastily?"
    "Did she see me glancing that direction, by chance?"
    mc ea mb "I was enjoying discussing the story with you, actually. Your views are very insightful."
    show yuri ea ma
    mc ml "But if you’d like me to go speak with them, then sure."
    show yuri turned rup me e1d
    "Her expression is a mixture of surprise and relief."
    y rdown mg e3c "No, I just... didn’t think you’d want to discuss with me further after I had such a... dissenting opinion."
    show yuri e2a b2b ma
    "I frown."
    _mc bd ea mh thinking "Is this what she expects? To be ignored or dismissed for disagreeing?"
    _mc eb mf "Has she been on the receiving end of this in the past?"
    _mc ldown ec bi mh "That’s just wrong."
    show yuri e1d b1a me
    mc ba ea mg "Why on Earth would I stop now?"
    mc mb "After all, isn’t the whole point of discussion that of debating viewpoints?"
    mc mg "And the ones you raised were very intricate and thought-provoking."
    show yuri e3c ma
    mc ml "All it’s done is make me want to talk with you all the more."
    mc mg "Just because I don’t wholeheartedly agree with you doesn’t mean I should neglect or think any less of you."
    show yuri e2a b2a nc
    "She is clearly touched."
    y mb e2c "That... That’s so very kind. Thank you, I err..."
    show yuri ma
    "She stumbles over her words, and I patiently wait for her to figure out what she’s trying to say."
    y rup e1a mh "Truth be told... I’d like to keep talking with you, too."
    y mg e3c b2b nd "Apologies for being so difficult and for zoning out all the time..."
    show yuri e1a ma
    mc ea mg "It’s not a problem. You’re genuinely not being difficult."
    mc ed md "Take all the time you need to get your feelings across. It’s no inconvenience."
    y shy eb mc nd ba "Would you care to start a new book with me at some stage?"
    "She noticeably fidgets."
    y ea "So we’d have more to... talk about?"
    "I sense she is venturing slightly out of her comfort zone with this request."
    "I make sure to respond with as much enthusiasm as I can muster."
    _mc eb mh "That kind of boldness deserves to be rewarded."
    show yuri turned e1d b2a ma nc
    mc ea mb "That would be fantastic, Yuri. Do you have a particular title in mind? Seeing as I sort of chose this one."
    show yuri nd e2a b2b
    "Her face flushes and she ponders for a moment."
    y e1d nc b1a mh lup "Does a little Ray Bradbury sound alright with you?"
    show yuri ma
    "I grin. That I have somewhere at home; I'll have to dig it out."
    mc ed md "I’d love that. Haven’t delved into his stuff all that much, but... no time like the present, hey." # im stuff
    y e2a b1d mb "Better late than never, yes. I... I’ll bring something of his tomorrow, then?"
    show yuri ma at thide
    mc eh bb "Too easy."
    _mc ea ma "I’m not sure who is being rewarded more. Her by my agreement, or me by her smile."
    hide yuri

    return

#############################################################################################################
#############################################################################################################
#############################################################################################################

label week_1_tuesday_sayori_1:
    show bg:
        align (1.0, 0.6) zoom 1.8 blur 2.0
    show sayori turned e2c mj b2b:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i44
    camera master:
        align (1.0, 0.2) zoom 1.4
    with Dissolve(0.2)
    "Sayori is looking out the window, seemingly lost in her thoughts."
    "Her expression is difficult to decipher..."
    show sayori ma b2c with say_dissolve
    "Although largely wistful, I spot it being punctuated by what look like little twinges of hopefulness."
    "Little bursts of nostalgic mirth, as indicated by the intermittently upturning corners of her mouth."
    "Or maybe I’m just projecting how I’m feeling onto her..."
    "Hoping that she’s feeling the same complex mix of emotions that’s been welling up within me the moment I saw her here."
    "The feelings swell as I watch her scribbling on her paper."
    "Her posture and hand movements are practically unchanged from how they used to be."
    show sayori md with say_dissolve
    _mc ec mh "Back when she wrote all those so-bad-they-were-good pastiche scripts of the stuff we used to watch on the TV..." # im stuff
    _mc ef ma "Hoping they would win her the Pulitzer, or at least get her hired as showrunner."
    hide sayori
    show bg:
        blur 0.0 zoom 1.0
    camera master
    with Dissolve(0.2)
    "I sigh and turn away."
    _mc mh "Such fun times, those were..."
    _mc bb "Will they ever be ours to know again?"
    _mc mj ba eg "Who knows, really..."

    return

label week_1_tuesday_sayori_right:
    show sayori turned ma b2a:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    s "..."
    s mb e2a "... Oh, Melody."
    s e1a b1a lup "Somehow, I just knew you’d guess correctly."
    show sayori ma ldown
    mc bg md nb eh "Ahah, it wasn’t as easy as it seemed, Sayori."
    mc mb bf ef "It took a while for me to connect the dots, but that’s only because the 'voice' you’ve found here is a tad different."
    mc ea mg ba na "Not the bad kind of different, mind you - the change shows that you’ve really grown and matured as a writer."
    show sayori e3d
    "Sayori seems pleased by my answer."
    _mc ef ma "In actual fact, however, I’m sort of downplaying the whole thing."
    _mc eg "To recognise Sayori’s writing style is just like swimming."
    _mc ed "You don’t forget easily."
    _mc ef mh "I’ve been apart from her for that long, yes."
    show sayori e1a
    _mc thinking ec "But when I look at the words on the paper..."
    _mc eg ma "... I can again envision and associate the characteristic word choices and sentence structure that I became familiar with all those years ago."
    _mc bb "The little details that a... good friend commits to memory."
    _mc ea "Besides, the message she’s trying to get across is a dead giveaway."
    _mc ldown bf "That pining tone. That air of self depreciation."
    _mc ef bg "No prizes as to what - or rather, who - the boat represents."
    _mc eg bi mh "I can’t rest on my laurels after deciphering her veiled outpouring of feelings."
    _mc bd ed "This is the opportunity for me to set things right."
    _mc eg "Resolve, don’t fail me now."

    return

label week_1_tuesday_sayori_wrong:
    stop music fadeout 2.0
    show sayori turned e2a b2a mj:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    "It’s clear from Sayori’s dejected expression that I’ve guessed wrongly."
    "That the poem was, in fact, hers."
    "Thinking back, I really should have known."
    "I was so caught up in trying to recognise the style, that I could not see the forest for the trees."
    "The true giveaway was right there, in the poem’s underlying message of a poignant reunion."
    play music myfeelings
    "I bite my lip and swear under my breath."
    show sayori e1a md
    _mc bd eb mi "What the hell is wrong with me? This is Sayori we're talking about! How do I mess something like this up?"
    show sayori ma
    "Evidently I did not swear quietly enough, for Sayori catches my eye and flashes me a smile in spite of it all."
    s b2c mb "It’s okay, Melly."
    s e3c mg b2a "I can’t really hold it against you - nobody can or should."
    s e2a lup mb "It HAS been that many years since we last hung out, after all - let alone since we did any writing together."
    s e1a mb "I wouldn’t expect you to remember what my poetry’s like, especially now that I’ve found my 'voice' after those prior baby steps."
    s ldown e2a "At least I think I have~"
    show sayori ma
    mc ef bg mj "... You’re too kind, Sayori."
    mc ed mb bf "I promise I’ll use the time spent here to better familiarise myself with how far you’ve come."
    "As well-meaning as Sayori sounds, her reassurance doesn’t really do anything to make me feel better."
    "If anything, it only worsens my guilt."
    _mc bi eg mm "Enough of this cringeworthy fumbling already, MC."
    _mc ec mh "It’s high time you set things right."

    return

label week_1_tuesday_sayori_2:
    "Grabbing my book from my bag, I look around the room."
    "There’s a solemn quietness to the air, like a sombre violin melody."
    "I wouldn’t go so far as to call it sad, by any stretch, but relaxing?"
    _mc ec mh "Not likely."
    "The girls have all sat down, taking out their own books."
    "I’m on the verge of following suit, but I know there’s something I need to do first."
    _mc ef "Something I should have done, a long, long time ago."
    show sayori turned rup e2d b2a ma:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    camera master at vpunch
    "Without so much as a warning, I plonk my seat next to Sayori."
    "It’s a little crowded, but that had never bothered us before, had it?"
    show sayori e2b 
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "As I look toward her, she tenses up."
    show sayori b2a e1a rdown with say_dissolve
    "Looking my way, her hair swishes with the movement."
    s lup e2a b2a mb "H- Hey, Melly!"
    s e2c "How’s it going?"
    show sayori ma with say_dissolve
    mc md ed "Yeah, alright. I figured it would be a good time to catch up, you know?"
    "Something about Sayori’s demeanour catches me a little off-guard."
    show sayori e2a with say_dissolve
    "While seemingly amenable to my presence earlier, she seems uncomfortable now that we’re this close up."
    _mc eb mh "I mean, no kidding."
    _mc bi eg mm "I haven’t talked to her in years, of course she’d be weirded out by me just plonking my ass right next to her!"
    _mc mh "What was I thinking?"
    _mc ec ba "Just... be cool, me."
    _mc ma ea "Just pretend like no time has passed! It’ll be fine!"
    camera master:
        zoom 1.0
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    mc mg "I mean, if you don’t want to, I can give you some spa-"
    $ autofocus.unblock("sayori")
    s ldown e1b b1a mk "Nonono, it’s fine!"
    show sayori rup e1a ma b2c
    "She violently grabs my sleeve as I attempt to get up."
    s mg "Don’t..."
    show sayori ma
    mc mf "Don’t? Don’t what?"
    s rdown e2a mb "Ah, nevermind."
    s ma "Ehe."
    "Her smile is probably the most forced thing I’ve ever seen, but she really wants me to stay."
    camera master:
        zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc mb "Alright, you win. What are you reading?"
    s b1a e1a mh "Oh, uh, it’s a book."
    show sayori md with say_dissolve
    mc ec mf "Yeah, I got that."
    s e2a mg b1b "It’s, um, about a..."
    show sayori lup rup b1a mc e3d with say_dissolve
    s "A kid!"
    s rdown e1a mb "Yeah, a kid who..."
    show sayori md with say_dissolve
    mc thinking ml "You... haven’t read the book, have you?"
    s ldown "..."
    s tap eb nb ma "No..."
    _mc eg mh bi "Unbelievable."
    _mc ba ma "And yet, that’s so like her."
    show sayori turned md na e1a b1a with say_dissolve
    mc ea ldown mb "Well, if you haven’t started yours, did you want to read with me?"
    s e2a mb "I... Ah, yeah. Sure!"
    show sayori e1a ma with say_dissolve
    "Her smile is sweet, and it reminds me of the sweet girl I-"
    show sayori md with say_dissolve
    _mc eg bi mi "No, not opening that can of worms. Not today."
    s mh "... Is something wrong, Mel?"
    show sayori md with say_dissolve
    _mc eb ba nb mf "'Mel'? Shit, that's nostalgic..."
    mc mb ea na "I was about to ask you the same thing, actually."
    s mb "Well, assuming both of our answers would be the same, let’s skip over that. Wanna read with me?"
    show sayori ma with say_dissolve
    mc mb "Yeah, that was why I walked over."
    s e3d "Ehe~"
    camera master:
        zoom 1.6
    with Dissolve(0.2)
    "I shuffle closer to Sayori, clutching my own book."
    "Holding it out, I turn the page."
    show sayori e1a
    camera master:
        zoom 1.65
    with Dissolve(0.2)
    "As I do, she inches even closer to me."
    "It’s almost like we’re connected at the hip."
    show sayori e2a with say_dissolve
    "We slowly read through the first chapter."
    "It isn’t my usual cup of tea, but I read the entire thing last night, so I’m pretty familiar with it."
    show sayori e3c md b1b with say_dissolve
    "As I continue reading, I hardly notice the proximity to Sayori. It was as if we were meant to be that nearby."
    show sayori e2a with say_dissolve
    "That is, until something changes."
    stop music fadeout 2.0
    show sayori e3c me with say_dissolve:
        subpixel True
        block:
            linear 2.02 yoffset -3
            easein_cubic 0.9 yoffset 2
            repeat
    "I feel a soft pressure on my shoulder, and my body tenses."
    "Glancing through my peripheral, I see her head neatly resting on my shoulder."
    "Her face is right next to mine."
    _mc eb mh bf nb "W- What do I do?"
    _mc mf ef "Do I leave her there?"
    _mc ea mh na "Is she still reading?"
    show sayori b3d mj with say_dissolve
    _mc eb "Would that be rude?"
    s "..."
    s b1a mu "zzz..."
    mc ed bg mb "You can’t be serious."
    _mc ba ec mh "I don’t want to disturb her, but..."
    _mc ea mf bb "Oh."

    play music myfeelings

    _mc eb bb nb mj "Ah."
    "As the reality in front of me starts to sink in, something becomes abundantly clear to me."
    "Her shampoo is wafting into my nose, and I can’t describe it outside of..."
    _mc eg na ma "Sweet."
    "It smells like roses, like someone took a sample of the most beautiful things in the world, and combined them."
    _mc eb bc mj nb "Ah, no, no!"
    _mc bi eg mm na "Stop it, you can’t do that again!"
    show sayori b1d e1d me with say_dissolve:
        pass
    s "... H- Huh...?"
    show sayori turned e1b lup rup b1a nb mk at i11
    show bg:
        blur 0.0
    camera master at vpunch
    play sound fall
    $ autofocus.unblock("sayori")
    $ say_transition = False
    "My sudden movement disturbs Sayori, causing me to panic more."
    "The jerk causes the chair to lean backward, and I instinctively reach for the closest thing to support me."
    s ml "Ah-"
    show sayori nd mk
    "Sayori turns beet red."
    "As I look, I notice my hand is holding her hip."
    mc be eb mg nc "Sorry, I-"
    "As I start to pull away, I feel a hand, placed on my own."
    s nd mb b2a e2a ldown rdown "It’s alright."
    show sayori ma
    _mc mh nb "No, no it isn’t!"
    show sayori e1a ma
    _mc nd "I’m going to have a nosebleed in a second, Sayori!"
    "In my infinite wisdom, I start to pull away again."
    "And this time, with Sayori attached, I realised, too late..."
    show sayori e2a nc
    "... That if I keep going, we’re both going down."
    show sayori e1a rup lup
    "Sayori, clasping my hand, pulls me closer, angling herself upright."
    "It’s enough to prevent us from falling, but now..."
    show cg sayori 1 at Flatten onlayer above_master with cg_dissolve
    $ persistent.sayori.mark_cg(1)
    "We’re centimetres from each other’s faces."
    _mc mj "Red alert! All hands, retreat!"
    _mc ea mh nc ba "And yet..."
    _mc eg bg "I can’t stop myself."
    _mc ba "It just feels..."
    _mc ma "So right."
    _mc ed nd "It’s been so long since we were this close..."
    _mc ef mh "I can’t help but feel like this was..."
    _mc ma "Meant to be."
    show cg:  
        align (0.5, 0.2) zoom 1.0
        linear 5.0 zoom 1.2
    "I start to lean closer."
    _mc eb be mh "Oh, how I’ve agonised over this..."
    _mc mf "Do I dare to even gaze upon such long-since-undisturbed soil?"
    _mc ef bf mh "How... How can I even dare to think such a thing, after..."
    show cg eb mb:
        zoom 1.35
    with Dissolve(0.2)
    "I focus my eyes, and I realise something."
    "Her eyes are closed."
    _mc eb ba nb "Is she giving me permission? Is that what this is?"
    _mc ed na "Or am I misinterpreting this?"
    mc ea mf "Sayori..."
    "I can’t help but gaze at her."
    "I can’t see her eyes, but her soft hair, begging me to reach out..."
    "Her soft hands, still clasping mine..."
    show sayori turned e3c me nc b1a
    camera master:
        align (0.5, 0.2) zoom 1.65
    $ autofocus.block("sayori")
    "And her soft smile... They all beckon me."
    _mc mf "But..."
    _mc bg eg mh "I can’t. Not this time."
    show bg:
        blur 2.0
    $ clear_layers("above_master")
    with cg_dissolve
    $ say_transition = True
    "I place a hand on her shoulder."
    show sayori e1a b2a mj nd with say_dissolve
    "Her eyes flutter open, and a sad look crosses her face,"
    show sayori e2a nc ma with say_dissolve
    extend " before it turns a shade of embarrassment."
    s mb "I- uh-"
    show sayori e1a mj b2c with say_dissolve
    "She moves to get up, but I gently grab her hand."
    mc ef bf mg "I’m sorry, but, can you stay here for a while?"
    s mk e2a b2a "Oh, ah, uh..."
    s b2c e3c mb "Y- Yeah. Ehe..."
    show sayori ma with None
    show sayori e2a ldown ma b2a 
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Sayori sits back next to me, a small, but noticeable, distance away."
    show sayori at thide
    "It feels lonely, over here, somehow."
    hide sayori

    return

#############################################################################################################
#############################################################################################################
#############################################################################################################

label week_1_tuesday_natsuki_1:
    show natsuki cross e2a b3d mj:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        i11
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "Natsuki’s brow is furrowed as she scribbles furiously."
    show natsuki e3c mm b3b with say_dissolve
    "Perhaps a bit too furrowed and a bit too furiously..."
    "Almost as though she’s trying very hard to seem engrossed in her work."
    camera master
    show bg:
        blur 0.0 zoom 1.5 align (0.7, 0.7)
    show natsuki e2a md b3d:
        xcenter 0.07 zoom 0.76 ypos 1.0 yanchor 0.95
        blur 2.0
    with Dissolve(0.3)
    "Turning back to my writing, I look over at her again, much more subtly this time."
    "..."
    "..."
    show natsuki e1a
    "..."
    show natsuki turned e1b mm b3a nc:
        blur 0.0
    show bg:
        blur 2.0
    with say_dissolve
    "And my eyes meet a beady pair of pink ones that frantically snap away almost the very moment contact is made."
    show natsuki e2b b3d with say_dissolve
    _mc ec "There we go. Caught her."
    hide natsuki
    show bg:
        blur 0.0 zoom 1.0
    with Dissolve(0.2)
    $ say_transition = False
    "She’s been stealing glances at me all throughout..."
    _mc thinking ea mh bb "Curiosity?"
    _mc ec mf ba "Or something else?"
    _mc mh ldown ef "Who can tell, really..."
    hide natsuki

    return

label week_1_tuesday_natsuki_right:
    show natsuki turned mh:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    n "Wow. You..."
    n mg "... You did it."
    n cross md b1d "Huh."
    n e2a mh "Beginner’s luck really is a thing, I suppose."
    show natsuki mj
    "The urge to refute Natsuki’s statement is irresistible."
    _mc bi ec mi "I’m not going to have my success dismissed as a mere fluke."
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    "Drawing myself up to full height - not really difficult given how petite she is by comparison - I say, in my best sagely tone..."
    show natsuki b3d e1a with say_dissolve
    mc bd ea mg "In my experience, there’s no such thing as luck."
    n turned b1d mh e1d "... Is that a fact now."
    n b3a e3c mi "Then enlighten me, oh wise one - just how did you figure me out as the author?"
    show natsuki e1a mj b1d with say_dissolve
    mc mf "..."
    n lhip rhip b3d mi "Well, come on already - I haven’t got all day."
    show natsuki mj with say_dissolve
    mc ml "It’s the way you speak."
    n me "Hmm?"
    show natsuki md with say_dissolve
    mc ba "Yeah. You know - direct. To the point."
    mc bb eg mg "Never using six words or great big bombastic terms where three or fewer ordinary ones will do."
    mc thinking ba ea ml "And that manner of speech is reflected in your writing."
    mc ed mb "A deceptively simple style that’s actually very succinct."
    show natsuki nc with say_dissolve
    mc mg ldown ea "That still manages to paint an effective picture."
    n "..."
    n e2a mm "... I don’t know if you cooked that up on the spot or what, but even if you did..."
    n cross e2a mh na b3d "... I have to admit that takes talent of sorts."
    n e1a mi "If nothing else, you might just do well at improv verse or open mic."
    show natsuki md with say_dissolve
    mc ed md "Thank you. You’ll find, once you get to know me better, that I’m more than just a pretty face."
    show natsuki b1a ma with None
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Natsuki gives a derisive snort."
    $ autofocus.unblock("natsuki")
    n turned mb e1d b1d "Don’t get too much of a big head about this, alright?"
    show natsuki ma
    "But she’s smiling as she says so."
    "I can’t help but chuckle too."

    return

label week_1_tuesday_natsuki_wrong:
    play music poempanic

    show natsuki turned lhip rhip mi b3d:
        matrixcolor TintMatrix("#a3a3a3") * SaturationMatrix(0.8) * BrightnessMatrix(-0.07)
        t11
    n "Oh for crying out loud - really?"
    show natsuki mj
    "I recoil at Natsuki’s outburst, both physically and inwardly."
    "If the true identity of the poem’s author wasn’t apparent to me earlier, it sure is now."
    "Frantically, I scramble to defend myself."
    "I may have chosen wrongly, but surely that doesn’t mean I deserve getting my head bitten off."
    mc eb mg bd "Hey, let up on me, alright?"
    n e3c nc mi "What - just because you’re new?"
    show natsuki e1a mm
    mc ec bi ml "No, because you can’t presume anything these days."
    show natsuki e1a mj na b1d
    mc ba ef mg "I mean, sure - the poem’s writing style is similar to how you speak."
    mc bj ml "Direct, succinct."
    mc thinking ea mg ba "But wouldn’t it be presumptuous or even shallow of me to conclude you’re the author purely based on that?"
    $ autofocus.block("natsuki")
    n cross b3d md "..."
    "Natsuki seems to falter at this point."
    "Seeing this opening, I seized the opportunity to press on."
    mc ldown mb "You know, I think you ought to be glad that I guessed wrong."
    mc bd ed md "Because it would mean that to the casual reader such as myself, you aren’t so easily pinpointed or pigeonholed."
    mc mg ea ba "And surely the last thing a poet wants to be is predictable, to be a one-trick pony."
    mc mb eh bb "... Right?"
    show natsuki e2a mm
    "I can practically hear the cogs in Natsuki’s head turning as she processes my impromptu excuse."
    "Possibly even the steam exiting her ears, too."
    "For several tense moments, I keep all my toes and fingers crossed."
    $ autofocus.unblock("natsuki")
    n mg "... Oh, whatever."
    show natsuki mj
    mc ba ea mf "... Whatever?"
    n turned lhip rhip b3d mi e1a "Yeah, you heard me. Forget about it."
    show natsuki mj
    "And with that, I breathe again."
    n rdown e2a mh b1d "I have to admit, that was a pretty speech."
    n b3d e1a mi "But don’t you try that nonsense with me ever again, you hear, because it’s not going to fly twice."
    show natsuki md
    mc mb "Thank you. I’ll remember that for sure."
    n ldown e2a mg "You’d better."
    show natsuki md

    return

label week_1_tuesday_natsuki_2:
    show bg:
        align (1.0, 0.6) zoom 1.8
    show monika turned mc ec:
        matrixcolor TintMatrix("#f1d6bb")
        i44
    with Dissolve(0.2)
    "I plonk my butt in a nearby chair, opposite to Monika."
    _mc thinking mh "I don’t know why, but her presence seems to be comforting."
    _mc ef "It’s not like I’m not having fun, quite the contrary, but..."
    show bg club_closet_afternoon:
        zoom 1.0
    hide monika
    show sayori turned lup b1b md e2a:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    with Dissolve(0.2)
    _mc ldown "Sayori being here is really distracting."
    _mc ea "Not in a bad way, but I just..."
    _mc ef ma bf "Can’t help but feel bad, you know?"
    _mc bg eg "It’s been a long, long time since I’ve spoken even a word to her, and now we’re in the same club?"
    show bg club_afternoon:
        align (0.0, 0.8) zoom 1.9
    hide sayori
    show yuri turned e2a b1d:
        matrixcolor TintMatrix("#f1d6bb")
        i42
    with Dissolve(0.2)
    _mc ea mh ba "Then again, Yuri seems nice."
    _mc ma "She’s a bit on the shy side, but she’s... You can tell she’s passionate about this stuff." # im stuff
    show bg:
        zoom 1.0
    hide yuri
    with Dissolve(0.2)
    _mc mh "As for Natsuki-"

    play music playwme

# {Full Voice Acting Including Narrator}
    show natsuki turned mh rhip:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    n "What’cha reading, Melody?"
    show natsuki mj b3d
    mc ec mj "Wha- Huh. Speak of the devil."
    n e1d mh b1d "Huh? What, were you thinking about me or something?"
    show natsuki md
    mc eb mg "Ah- No, of course not."
    n e3c b1a mi rhip "Good, because that would be weird."
    show natsuki ldown rdown e1d b1d mj
    mc ed ml "Why’s that?"
    n b4 mh "Uh, because I don’t know you?"
    show natsuki md b3d
    mc ef mf "Fair point."
    show natsuki e1a b1a
    mc ea mb "Well, would you like to?"
    n b1d mg "Huh? What?"
    show natsuki nb md
    mc ed md "Get to know me."
    mc ea mg  "I mean, you did call me by name, rather than what people are {i}supposed{/i} to call me, so you must have something rattling around in that brain of yours."
    mc ed md "So what'll it be? Here for the view? Or are you after more than that~?"
    n e1b b3d mi nc "N- No I didn’t! Wh- Where did that come from?"
    n e2a mm "Did you think you could just come here, with your smooth words, and get me to read with you?"
    _mc ea ma bm "My smooth words? Well, if you insist..."
    mc ed mb bb "Well, looking at the fact that you’re over here, without a book, and starting a conversation with me..."
    n b1a e2c mi "W- Well, you’re in luck, because I just so happen to need that book for class. So I might as well read it with you."
    show natsuki md
    mc bm md "Uh huh. So you need the book that we studied like, six years ago, now?"
    n e1a b3d mi "Whatever, just move over, alright?"
    show natsuki mj
    _mc eb ba mh "Wow, she doesn’t mess around, does she?"
    _mc ec ma "Ah well, it’s not like I was able to really concentrate anyway. May as well humour her."
    show natsuki e1b ml nd b1d
    stop music fadeout 1.0
    mc ef mb "She’s cute, too."
    _mc eb bb nb mh "Ah, shoot. That didn’t just come out of my mouth, did it?"
    n mk "Wh- Wh-" 
    _mc bi mj eg "Ah yes, here we go."

    play music2 poempanic

    show natsuki b3d xd ml at hop
    n "Who are you calling cute?"
    _mc ec mh ba na "Alright, I have one shot at this. Play it off as deliberate, and lay it on thick, and maybe it’ll work out."
    show natsuki e1a mm nc
    _mc ea "Otherwise, pretend I said nothing."
    _mc ef ma "Either way, I’m probably screwed if I'm not decisive."
    show natsuki e3c
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "I take a glance in Natsuki’s way. She looks flustered."
    _mc eb mh "Alright, option one it is! All or nothing!"
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    show natsuki b1d e1b
    mc ea mb "You, of course."
    n e2b "Wh- I-"
    show natsuki b1a xd ml at hop
    n "I’m not cute!"
    mc ed md "I don’t believe you."
    n e1a b3d mm "Wh- What’s that supposed to mean?"
    "She’s gone beet red. Looks like that was the right call, now to pull it back."
    mc ea mb bb "Exactly what I said. Now are we reading, or not?"
    n e1b mi "I- Bu-"
    show natsuki e2a mm
    "Natsuki blinks a couple of times, trying to gauge me."
    stop music2 fadeout 4.0
    n cross mi "Ah, of course, yes, let’s read."

    play music playwme

    show natsuki md
    show cg natsuki 1 nb ec bb at Flatten with cg_dissolve
    $ say_transition = True
    $ persistent.natsuki.mark_cg(1)

    "Natsuki moves her chair closer to mine, and leans over to see the book."
    "If I were to move the book slightly to the side, she’d have to practically sit in my lap to read it; though judging from how her leg is already resting atop mine..."
    "Shaking my head, I banish the thought."
    show cg ba na with cg_dissolve
    "As I look at the girl, I start to notice something."
    "Despite her rough demeanour, and what I said before, she’s {b}actually{/b} pretty cute."
    "She’s small and delicate, like a cat."
    "And the way she’s leaning my way, she’s almost leaning {i}into{/i} me."
    show cg ea ba with cg_dissolve
    "I feel my cheeks start to flush, so I bring the book closer to Natsuki."
    show cg front with cg_dissolve
    "She shifts to a more comfortable position, and then looks up at me."
    hide natsuki
    "Her hair is a soft, gentle pink colour, and her fringe is held to one side by a simple but effective hair pin."
    "Her eyes are a whole different ball game, though."
    "The depth to them is remarkable. She looks like she’s lived a thousand lifetimes in those eyes."
    "The eyes, the colour of her hair, shimmer as the light of the afternoon sun dances across them."
    mc mf nb "I... Uh..."
    show cg eb nb mc with cg_dissolve
    n turned e1b b3a nb mg "Ah! Oh, um-"
    show cg side ec na bb mc with cg_dissolve
    n e2a b1d mi "A- Are you going to turn the page, or what?"
    mc bf eh md nb "Ah, yeah, right! The book! Of course!"
    show cg side eb bc mb with cg_dissolve
    n mg e2c "What the hell else would you be thinking about?"
    mc ef mb bg "No- Nothing!?"
    show cg front mc bb ea with cg_dissolve
    n mi e1a "That’s what I thought."
    show cg side nb mc nb ec with cg_dissolve
    "I quickly turn my attention back toward the book."
    "It’s then that I realise."
    $ renpy.set_tag_attributes("natsuki ma b1a e1a na")
    "The sun is starting to dim, meaning club time is almost over..."
    "... And I’m still on the first page."
    hide cg with cg_dissolve

    $ say_transition = False
    return

#############################################################################################################
#############################################################################################################
#############################################################################################################
