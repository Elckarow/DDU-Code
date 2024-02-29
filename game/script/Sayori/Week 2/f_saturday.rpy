label week_2_saturday_sayori:
    call calendar_transition(day=4, hour=6, minute=11) from _call_calendar_transition_34
    scene bg mc_bedroom_day_closed:
        align (1.0, 1.0) zoom 2.0
    camera master:
        blur 3.0 matrixcolor BrightnessMatrix(0.2)
        ease 14.0 blur 0.0 matrixcolor BrightnessMatrix(0.0)
    with dissolve_scene_full
    play music anewday
    
    "As my senses slowly come to, I bring a hand to my head."
    "I've got a splitting headache."
    show bg:
        ease 0.8 zoom 1.9
        easein_back 0.2 zoom 2.0
    play sound ["<silence 0.85>", audio.fall]
    "Slowly sitting up, I almost collapse back down again."
    mc turned messy naked nostrands mj eh bg nb "My hips..."
    mc eb bd mg "What the hell?"
    "Everything from the waist down refuses to cooperate with my brain."
    show bg:
        matrixanchor (0.5, 1.0)
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0) * OffsetMatrix(0.0, 0.0, 0.0)
        ease 10.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0) * OffsetMatrix(50, 0.0, 0.0)
    "Rolling my eyes, I force myself up, sliding out of bed."
    show bg:
        easein 0.3 matrixtransform ScaleMatrix(1.3, 1.3, 1.3) * OffsetMatrix(50, 0.0, 0.0)
    show black onlayer above_master:
        alpha 0.0 
        easein 0.3 alpha 1.0
    play sound ["<silence 0.1>", audio.smack]
    "As I do, I fall flat on my face."
    mc mj eh bg "Oof!"
    mc ea mb bf "Was I doing yoga or something?"
    show white onlayer above_master with NonBlockingDissolve(1.0):
        alpha 0.5
    "In front of my face, now sore from the impact, I see something white."
    "It looks like a piece of fabric, and not something I recognise."
    "The round, relatively flat material reminds me of something, but I can't quite put my finger on it."
    hide white onlayer above_master
    hide black onlayer above_master
    hide bg
    show bg mc_bedroom_day_closed
    with Dissolve(0.2)
    "Picking it up, I finally regain feeling in my legs."
    "I shrug, deciding to examine the thing over breakfast."
    "As I walk out of my door, I see something else lying on my floor."
    "And I pause."
    _mc ec ba na mh "That's not mine."
    "I then look back to the thing in my hand."
    _mc ea mf "Ah."
    "I pick up the fabric and place the object next to it on my bed, and after a moment, find the pair to go with it."
    _mc ec mh "I'll have to give Sayori her bra back later - She might need it if she plans to go out."
    _mc "Including the pads that go with them, of course."
    _mc eg bi "Just thinking about it makes me a little sick, honestly."
    _mc ef ba "The fact that she relies on these things for her own self-worth..."
    _mc eg ma "She doesn't need them. One day I'll have to prove that to her."
    _mc "She's perfect the way she is, at least in my humble opinion."

    scene bg mc_kitchen_day with wipeleft
    play sound_loop frying_pan fadein 1.5

    "I then walk down the stairs, where I can smell something cooking."
    show sayori turned casual lup md e2a b1d at t11
    "Sayori seems concentrating on frying something in the pan, and as much as I don't want to disturb her..."
    _mc turned naked messy nostrands eg bi "Ah, screw it. I can't resist."
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "Sneaking up behind her, I slowly wrap my arms around her waist, pulling her in."
    show sayori rup e1b b1a mh with say_dissolve
    "She lets out a small yelp, as she turns to face me."
    show sayori e1a rdown ma with say_dissolve
    mc ed ba md "Hey."
    s nc mb e2a b2a "You startled me, ehe~"
    s mg "I'm..."
    show sayori ma b1a e3c na ldown with say_dissolve
    "Sayori brings her free hand to her face, placing the spatula she'd been using on the counter."
    s e1d mb "I'm so happy to see you..."
    show sayori ma with None
    camera master:
        zoom 2.0
    show bg:
        blur 2.5
    show sayori rup mg e3d
    with Dissolve(0.2)
    "It seems to then be her turn to bring me in, this time for a kiss."
    show sayori rdown with say_dissolve
    stop sound_loop fadeout 4.0
    "After a few seconds, her arm leaves my face, and I hear the stove turn off."
    "It looks like she's planning for the long haul today."
    "We remain embraced, our food long since forgotten."

    scene bg mc_house_entrance_day
    camera master
    with fade
    $ set_internet(False)
    $ advance_date(minutes=20)
    $ say_transition = False

    show sayori turned casual at t11
    mc turned casual mg "Are you sure you want to walk me to work?"
    mc ml "It's not exactly my idea of fun."
    $ autofocus.unblock("sayori")
    s mb e1d "Well, it'll be with you."
    show sayori ma
    "I can't help but blush."
    "She's never been so overt before."
    "Hell, I'm not sure she's ever even flirted with me before Monday."
    "But, who am I to complain?"
    show sayori e1a at thide
    mc ed md "Alright, let's head off then."
    hide sayori
    "Grabbing my work bag, I lock the front door, and the two of us head off along the road."

    scene bg city_street_2_day 
    show sayori turned casual at i11
    with wipeleft_scene
    $ advance_date(minutes=27)

    "As we walk, we spend little time talking."
    "My mind was far too occupied to talk, after all."
    "All I could think of was last night."
    "I'd never seen Sayori so emboldened, yet shy at the same time."
    "But..."
    "One thing still lingered on my mind."
    show sayori md
    mc turned casual mg "I know we brushed on the topic last night, but..."
    s e1b mk nb b2b lup "Ah, no, not in public, please."
    show sayori mj e1a with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    "Turning to face her, I expected her to be embarrassed, but instead she simply looked uncomfortable."
    $ autofocus.block("sayori")
    mc ml nb "Alright, sure."
    s e2c me "It's..."
    s e2a na b1b mg "Not something I'd want anyone else finding out about."
    show sayori md with say_dissolve
    mc ef na "I could imagine."
    mc ea mg "But it's alright."
    show sayori b4 e1a ldown with say_dissolve
    "Slightly confused, she raises an eyebrow."
    mc ed md "As I said last night, you're perfect."
    show sayori b1b with say_dissolve
    mc eh "Just as you are is the way I like you."
    s b2b "..."
    "It's then that I put two and two together."
    "If the bra's currently on my floor..."
    "That would mean..."
    _mc eb nd bd mh "Sayori isn't wearing it."
    "A quick glance confirmed my suspicion, but I quickly find myself feeling guilty for the action."
    "Though she might have opened up to me, both... well, in many senses of the word last night, it..."
    "It doesn't feel right to make a note of something that's caused her so much strife."
    "I'll have to remind her to collect it when she gets home."
    "Hell, I don't know how she even forgot it in the first place."
    "I open my mouth to remind her, but pause."
    "Not wanting to drag this out any more, as Sayori's expression is starting to weaken, I decide to change the topic."
    show sayori me b1b with say_dissolve
    mc ea mg na ba "But, honestly, who'd have even conceived the idea, eh?"
    mc be eh md nb "Honestly, you took me by surprise."
    camera master
    show bg:
        blur 0.0
    show sayori e2a md
    with Dissolve(0.2)
    $ say_transition = False
    "Sayori pauses for a split second, causing me to follow suit."
    $ autofocus.unblock("sayori")
    s b1a e1a mg "What do you mean, by surprise?"
    show sayori ma with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    "-And she began walking again."
    $ autofocus.block("sayori")
    mc ea ba na mg "I mean, I wasn't expecting that at all, you know?"
    s md e2a b1b "..."
    s mg "After all that, and you..."
    show sayori me e3c with say_dissolve
    "She sighs."
    s mg e1a "What were you expecting?"
    show sayori md with say_dissolve
    mc thinking ml "Honestly?"
    mc ef mg "I was expecting us to just sit down and talk for the evening."
    mc ea mb ldown "I feel like we haven't done that lately, you know?"
    s mg e2a "... I see."
    show sayori md with say_dissolve
    "I see a small cloud covering her expression."
    s e2a mg "Well, we have the sleepover tonight after you finish work, so I don't think we'll get that chance with everyone around."
    show sayori md with say_dissolve
    mc ea mg "Well, it'll be nice for us all to hang out."
    mc ef ml "We're all friends here, after all."
    s mg e1a b1d "Excuse me?"
    show sayori md with None

    stop music fadeout 2.5
    scene bg cafe_outside_day
    show sayori turned casual md b1b at i11
    camera master
    with Fade(0.3, 0.0, 0.25)
    $ say_transition = False
    $ set_internet(True)
    
    "Before I can properly respond to her question, we arrive at the cafe, abruptly iterrupting both our conversation and my train of thought."
    
    scene bg cafe_inside_day with wipeleft
    show boss turned at t11
    $ persistent.boss_seen = True
    play music cafe
    
    "Stepping inside, I see my boss waiting for me."
    b mb "Hey, kid! Good to see yer!"
    b eb bb "Any chance yer could start early? We just had a delivery come in."
    show boss ma
    "Looking at my watch, I figure an extra twenty minutes of pay was worth it."
    show boss ea ba
    mc turned casual mb "Yeah, I'll start early."
    b me rup "Who's this here, by the way?"
    show boss ma
    "My boss motions toward Sayori, currently half-hiding behind me."
    "Smiling awkwardly, I respond by gesturing toward her."
    mc ml nb bb "This is my..."
    mc ef ba mb "My... best friend, Sayori."
    hide boss
    show sayori turned casual md e2c b1b at i22
    camera master:
        align (0.75, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    "As I turn toward her, I see that clouded expression return."
    "As much as I want to ask her about it, it'll have to wait until after I finish work."
    show sayori ma e1a b1a with say_dissolve
    mc ea mb na "Hey Sayori, I'll meet you at your place after I finish, alright?"
    mc mg "You've got my spare key, so just make sure to grab your stuff out of my house, before you forget." # im stuff
    show sayori nb mj b2b e1b shadow with say_dissolve
    "I then see her expression change to one of horror."
    show sayori rup lup e2b nd with say_dissolve
    "Bringing her hands to her chest, she freezes."
    s rdown mg b2a "Oh..."
    s nb mb e1b b1a "I'll see you after work, Melody! I just remembered something!"
    show sayori ma with None
    hide sayori
    show boss turned md bb at i11
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("sayori")
    "And with that, she bolts out of the store."
    mc eg bg mj "Man, I wanted to make her a coffee, too."
    b me ba "There'll be time for that later."
    b lup bc "Besides, I think you've got some explaining to do, there."
    show boss md
    mc ea ml ba "Explaining?"
    mc ec mf bi "Of what, Sayori?"
    b me bb ldown "That'd be right. I've never seen you even mention any friends before, and here you are, bringing one along."
    b mb ba "Especially one you seem so close with."
    show boss md
    mc ea ba mg "Ah, that's true. I don't talk about my life very much, do I?"
    mc ed md "Mostly, I just listen to your tales."
    b ec mb bb "Well, time to spin one of your own, I reckon."
    b ba mc ed "Just don't let it distract you from those crates, mind you."
    "My boss lets out a hearty laugh."
    mc eh "I would never."
    show boss at thide
    hide boss
    "I follow suit, and pick up the first crate, preparing to take it to the fridge."

    scene bg cafe_inside_afternoon with wipeleft_scene
    $ set_date(hour=16, minute=4)

    "Toward the afternoon, I find myself contemplating the events of the past few days."
    show boss turned me bb:
        matrixcolor TintMatrix("#f5e2bb")
        t11
    b "Hey, kid, you're spilling that milk!"
    show boss md
    mc turned casual apron bb nb mg "Oh, ah, sorry! I'll clean it up right now."
    b mb ba "Ah, don't worry too much. We ain't so busy no more, and you look like you've got a lot on your plate."
    show boss ma
    mc bg mb ef "... You're too kind."
    b mc ed "Haha, you're darn right I am."
    "Another laugh escapes his mouth."
    b me ea "But, you still haven't told me yet."
    show boss md
    "Clicking my tongue, I sigh."
    mc ed bm na mg thinking  "Oh? What haven't I told you?"
    b mb "Ohoho, don't play dumb with me. You've got that young lass I'd like to hear more about."
    show boss ma
    mc ef bi mf "Well..."
    "Sighing, I figure it would be faster to get it over with."
    show boss md
    mc ea ba mg "Honestly, I only actually reconnected with her last week."
    mc mb ef ldown "We were thick as thieves as kids, but we sort of drifted apart after we got into high school."
    show boss bb 
    "My boss shoots me a knowing look. "
    b me eb "I know what that means."
    b ec mb "Tell me, though, who did the stupid thing first?"
    show boss md
    mc eh bg md nb "Ahaha, that would have been me."
    b mb ea ba "Hah, with how outgoing you are, that don't surprise me none."
    b me "So, considering she's back by your side, it couldn't have been that bad, aye?"
    show boss md
    mc mg bb ea "No, not as such. It was just..."
    mc ef ba na ml "Poor timing."
    $ autofocus.block("boss")
    b "..."
    "My boss goes silent for a second."
    $ autofocus.unblock("boss")
    b me "It was her, wasn't it?"
    show boss mf ec
    mc bi "... Yeah."
    _mc ec ba mh "I owe a lot to my boss, to be honest."
    _mc ea "He gave me a job when no one else would."
    _mc ef ma "I mean, who would give a job to someone without parents?"
    _mc ec mh "But that's not what he's on about this time."
    b me bb "You know, it ain't your fault."
    b ba ea "People change. Relationships change."
    b bb eb "Someone you knew like the back of your hand one day, will become someone completely different the next."
    b mb ba "That's just a part of life, kid."
    b ea me bb "If she really is the one..."
    b ba "And she's come back to you..."
    b mb "Well, you've really got no choice there, do ya?"
    show boss ma with None
    show boss lup
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.0) zoom 1.5
    with Dissolve(0.2)
    $ autofocus.block("boss")
    $ say_transition = True
    "Placing a hand on my shoulder, he smiles."
    b mb "Now, don't let me down, hey kid?"
    show boss ma with say_dissolve
    mc ef ml "... Yeah."
    b ldown me "And don't let me catch you feeling sorry for yourself over what happened way back with your ma'am, alright?"
    b ec bb "That's its own beast to slay, and you ain't got time to tackle both at once."
    b ba mb ea "Deal with this one first, then start unpacking that. No point burning your candle from both ends."
    show boss md with say_dissolve
    mc mh "..."
    hide boss
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2) 
    $ autofocus.unblock("boss")
    $ say_transition = False
    "Seeing my reluctance, the boss walked to the front of the store, and turned the sign from 'open' to 'closed'."
    show boss turned:
        matrixcolor TintMatrix("#f5e2bb")
        t11
    b mb "Tell ya what, I'll make you a coffee."
    b ec "Yer look like yer need it."
    show boss ma at thide
    hide boss
    "I can't help but smile."    
    "As he makes his way back toward the coffee machine, I pour some milk into a jug for him."
    b turned ed mc "Ah, thanks for that, kid."
    b ea mb "It'll be just a moment; go sit down and make yourself at home."
    b me "In fact, grab that lemon cheesecake. It'll only last to the end of the day anyway."
    mc ed md "Shall do."
    "Grabbing the knife, I take the small cake from the display shelf and cut it in half, placing each slice onto a plate."
    show bg:
        align (1.0, 1.0) zoom 2.0
    with Dissolve(0.2)
    "I then brought the plates out to one of the smaller tables, placing myself down and one of the cakes in front of me."
    "After I get settled, I see the old guy make his way over to me, two mugs in hand."
    show boss lup mb:
        matrixcolor TintMatrix("#f5e2bb")
        t11
    b "There yer are, just the way yer like it."
    show boss ldown ma
    "I look at it."
    "It's very clearly a long black."
    show boss ed mc at dip
    mc ea mf nb "Ah, I don't-"
    "I'm interrupted by his laughter."
    b mb "Ahaha, sorry, I couldn't resist!"
    show boss ma ea at dip
    "Swapping the cup in his hand for mine, it reveals the latte."
    "I nod to myself in approval, taking a sip."
    show bg:
        blur 2.0
    camera master:
        align (0.5, 0.0) zoom 1.5
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("boss")
    b mb "So, tell me yer woes, why don'tcha?"
    show boss ma with say_dissolve
    mc ef ml ba na "... It's something I should probably be fixing on my own."
    b me "Hah, well do ya want my opinion at the very least?"
    show boss ma with say_dissolve
    "I smile. His forceful type of love is something that never fails to bring out the best in me."
    mc mf "Sure."
    b ec mb "Well, if I might sour the mood a little..."
    b ea bb me "Why did ya introduce her as yer friend?"
    show boss md with say_dissolve
    mc ea bd ml "Huh?"
    mc mg ba "What do you mean?"
    b ba me "When ya walked it, it was 'Sayori, my best friend', not 'Sayori, the person I'm currently seeing'."
    b bb "Did yer not want me to know?"
    show boss md with say_dissolve
    mc ef ml "... But she is my best friend."
    b eb ba me "Best friends don't sleep wit' each-other, kid. Not if they value that friendship."
    b ea mb "At least, not if they don't talk it through first."
    b bb me "And you, kid, haven't talked that through."
    show boss md with say_dissolve
    mc mf "I..."
    show boss ec with say_dissolve
    "He shakes his head."
    b me "No, it's not something ya have to prove to me."
    b ea ba "That's a conversation to have with her."
    b mb "I can tell she means a lot to ya, that much is obvious."
    b eb me "But there's been no communication with you two. I could tell from even that short meeting."
    show boss md with say_dissolve
    mc ml ea bg "... How?"
    b ea me bb "Did yer even notice her face when yer introduced her?"
    show boss md with say_dissolve
    mc thinking bm mf "... No?"
    b me ec "All I'm sayin' is, if ya don't talk to her, all you'll be left with is a worse problem than what you had when ya started."
    b ea "What yer had back in middle school, kid."
    show boss mf with say_dissolve
    mc ldown mh ec ba "..."
    b ba me "She's a good lass. Don't you go around hurtin' her, alright?"
    show boss md with say_dissolve
    mc ef ml "I don't plan to."
    b mb ec "Good."
    show boss ma with None
    camera master
    show bg:
        blur 0.0 zoom 1.0
    show boss ea ba
    with Dissolve(0.2)
    $ say_transition = False
    "Smiling, he stands back up, having finished his cake."
    $ autofocus.unblock("boss")
    b mc ed "Now, let's get back to work, shall we?"
    b mb lup "You've been paid for sittin' down, so ya'd better earn that break by working twice as hard, aye?"
    show boss ma at thide
    hide boss
    "Smiling, he waves me off, making his way toward the door."
    mc ea mb "Absolutely."
    "Gathering the remaining cutlery, I watch my boss turn the sign back to 'open', and three people walk inside as soon as he does."
    show boss turned bc md:
        matrixcolor TintMatrix("#f5e2bb")
        t11
    stop music fadeout 2.0
    "Walking back over to me, he whispers,"
    b eb me "And in regards to the other thing..."
    b bb "You aren't her. You know that, deep down."
    show boss md at thide
    hide boss
    "Then he turns to serve the customers."

    # goes back to script.rpy for the sleepover
    return