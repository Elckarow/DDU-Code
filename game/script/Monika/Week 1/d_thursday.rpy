# label connect_four_win:
#     show natsuki md:
#         ease 0.3 xoffset 0
#     _mc "Hah! I win!"
#     mc "Not so much the master now, are you?"
#     n cross e3d mi "A victory is a victory... I’ll let you have this one."
#     show natsuki ma
#     "She grins widely at me."
#     n e1d b1d mb  "I’ll bet you can’t take me again?"
#     show natsuki ma
#     mc "I’ll take you up on that bet, but we’d better let the others have a go first."
#     show natsuki turned b3a md e1a at hop
#     "Natsuki shrugs, standing up and motioning for Sayori to take her place."
#     "It almost looks like she’s sulking, but I can’t quite tell with her, sometimes, as to whether it’s an act or real."

#     return

# label connect_four_loss:
#     show natsuki at t31
#     show monika turned suit at t32
#     show sayori turned hoodie at t33
#     m mb "How are you two getting along?"
#     show monika ma rhip
#     "I’m stunned, but not so stunned that I can’t move to block Monika and Sayori’s view of the grid and its humiliating contents."
#     show monika mc rdown at thide
#     show sayori me
#     n lhip mc "What do you think?"
#     show natsuki e3d mo at thide
#     show sayori e1b md at thide
#     "They gasp."
#     hide sayori
#     hide monika
#     hide natsuki
#     "I bite my lip, eyes downcast." 
#     _mc "Concealing the evidence of my defeat isn’t really going to work now, is it?"
#     _mc "I’ve got loss written all over my face and body language."
#     "Which the others are reading as readily as anything they bring to our club sessions."
#     show monika turned suit mc at t21
#     show sayori turned hoodie e1b lup rup ml at t22
#     s "Holy cow, seriously? That didn’t even take a minute!"
#     show sayori mk
#     m md "Natsuki, how did you manage that?"
#     show sayori e1a ldown rdown me at thide
#     show monika at thide
#     "I hear a clack-clack noise from behind me and turn around to yet another surprise." 
#     hide monika
#     hide sayori
#     show natsuki turned casual e2a md b3a at t11
#     "Natsuki has tipped all the pieces out of the grid and is tidying them up."
#     "Denying the others the chance to see exactly what took place."
#     show natsuki mh at t31
#     show monika turned suit mc at t32
#     show sayori turned hoodie md at t33
#     n "You’ll find out when you play me, but not before."
#     n e1a b1d mb "A magician never reveals her secrets."
#     show natsuki ma b3a at t11
#     show monika md at thide
#     show sayori b4 me at thide
#     hide sayori
#     hide monika
#     "As the others return to their game, all agog and whispering amongst themselves, I sheepishly turn to Natsuki."
#     show natsuki me
#     mc "Hey. Thanks for helping me save some face back there."
#     show natsuki ma b1a e3a
#     "She gives me a conspiratorial wink in response."
#     n lhip e2a b3a mh "Like I mentioned earlier. Never let it be said that I’m not inflexible."
    
#     return

# label connect_four_draw:
#     show natsuki:
#         ease 0.3 xoffset 0
#     "draw. there's no script for that :("

#     return

label week_1_thursday_monika:
    call calendar_transition(day=26, hour=6, minute=30) from _call_calendar_transition_3
    scene bg mc_bedroom_day_closed
    with dissolve_scene_full
    play music anewday

    "I rouse slowly."
    "My eyes feel as heavy as lead."
    _mc turned naked messy nostrands ec bi mj "God... What happened last night?"
    _mc ba mf nb ea "M- Monika?"
    _mc ec mh bi "Something to do with Monika.."
    "As the dream comes back to me I feel a strange mix of embarrassment and... arousal?"
    _mc eg mm "God, Melody, pull yourself together."
    _mc ec na mh "No dawdling in bed and {b}especially{/b} no fantasising over a friend..."
    "I pull myself out of bed, but my mind keeps drifting back to Monika..."

    scene bg mc_bedroom_day_open
    with wipeleft_scene
    $ advance_date(minutes=5)

    phone register "mc_s": 
        time auto True
        "s" "Hey, Melody"
        "s" "Want to come over for breakfast?" 
        "s" "I’m probably gonna have eggs"
        "s" "And bacon!"  
        "s" "And toast!"
        "s" "And orange juice!"   
        "s" "Humph"  
        "s" "Wait.... *pokes you*"  
        "s" "Do you have me...."
        "s" "Muted?"  
        "s" "Meanie!"   
        "s" "No meanies at breakfast. Hmph." 
        "s" "Except you of course!"
        "s" "Just kidding."   
        "s" "So, ah-"
        "s" "Could you bring some toast and eggs and bacon?"  
        "s" "And cook?" 
        "s" "Then I’ll forgive you!"
        "s" "So..."
        "s" "You gonna come over or what?"
        "s" "Don’t tell me you’re still asleep! It’s only like 5am!"
        "s" "What, next you’re gonna say 'normal people aren’t awake at 5am'? Hm?"
        "s" "Well that’s lame, and you have to buy breakfast now."
        "s" "C’mon, I’m waiting."
    
    $ advance_date(minutes=10)
    phone register "mc_s":
        time auto True
        "s" "Wake up already! I will throw rocks at your window if I have to."
        "s" "Is that what you want, oh great princess?"
        "s" "Yeah, I bet it is."
        "s" "Ok, c’mon, please? I promise I’ll buy you juice at school today?"
        "s" "No dice? Alright, how about I dedicate my entire lunch break to hanging out with you?"
        "s" "Eh? Bet you never saw that coming."
        "s" "That’s right, you get to spend the entire day with ME"
    
    $ advance_date(minutes=15)
    phone register "mc_s":
        time auto True
        "s" "Why"
        "s" "Aren’t"
        "s" "You"
        "s" "Responding?"
        "s" "Waaaaaaaaake"
        "s" "Uuuuuuuuuuup"
        "s" "Please?"
        "s" "Pretty please?"
        "s" "I’ll give you a cola?" # chika my beloved
        "s" "... Two colas?"
        "s" "Three colas, final offer."
        "s" "You drive a hard bargain, but I’ll offer you two colas and a hug if you wake up now."
        "s" "Limited time offer!"
        "s" "Well?"
        "s" "You can’t really be asleep."
        "s" "You’re ignoring me."
        "s" "You’re being a huge meanie right now. Just wake up! Respond to my calls!"
        "s" "Ok, ok, I get it, I’ll let you sleep. I’m sorry for getting worked up."
        "s" "I’ll make it up for you today, ok?"
        "s" "So..."
        "s" "Would you mind grabbing me toast, eggs and bacon?"
        "s" "And cooking?"
        "s" "I’ll make it up to you! Promise!"

    "When I’ve finished drying my hair, I check my phone briefly."
    _mc turned tail nostrands eb nb mf "Wh- What?"
    _mc mh bi ec na "54 messages from Sayori?"
    _mc ea mf ba "What the hell’s - Oh."
    "I see the messages."
    $ set_internet(True)
    
    phone discussion "mc_s":
        pause
    phone end discussion
    $ phone_available = True
    
    "I sigh."
    _mc ec ma "Better go buy some eggs."
    
    scene bg s_house_day with wipeleft_scene
    $ advance_date(minutes=32)

    play sound door_knock volume 1.0
    "I knock on Sayori’s door, groceries in hand."
    s "Yowsies!"
    _mc turned tail nostrands eg "Yep, she’s burned herself."
    _mc ea "So inept."

    stop music fadeout 0.75
    scene bg s_kitchen_day with wipeleft
    play music dollaort

    "I force my way through the door she always forgets to lock, and-"
    show sayori turned pyjama e2a b1d md rup at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    _mc turned tail nostrands ec "Yep. Stood by the sink, thumb under water, grumbling under her breath."
    _mc eb bd nb mh "And {b}very{/b} skimpily clad."
    n turned noband e1b b1d mk nb "H- Hey, perv!"
    n e2a b3d mg "Quit it!"
    show natsuki cross mm at i11
    camera master
    hide sayori
    show bg:
        blur 0.0
    with Dissolve(0.2)
    "I whirl round to the small, pink-haired aggressor."
    mc ea mg "Perv? Hey, look, she invited me! Sorry for not knocking..."
    show yuri turned lup e1d mf at t44
    "The second those words leave my mouth, Yuri pokes her head around the door."
    show yuri ldown mh at t22
    show natsuki at t21
    y "MC? You’re here?"
    show yuri e1a ma
    show natsuki mj e1d b1d
    mc ef bi pout "Yeah, unless Natsuki chops my head off first."
    n turned noband mi lhip rhip "Only if you stop ogling Sayori’s behind."
    show natsuki mj
    mc ea bd nb mg "Hey! I wasn’t o-"
    show sayori turned pyjama lup rup e3d mb at t32
    show yuri at t33
    show natsuki b3a e1a md ldown rdown at t31
    s "Hey, betrayer! You made it!"
    show sayori ldown rdown e1a ma
    show natsuki ma
    mc ed md ba na "Only because you sounded like you needed help."
    show yuri e3d
    s lup b1d e2a mh "Meanie muter."
    show sayori md
    show yuri e1a
    mc eh bb "I see you wasted no time burning breakfast."
    show natsuki e2a md b1a:
        blur 1.0 zoom 0.65 xoffset 130
    show yuri:
        blur 1.0 zoom 0.65 xoffset -130
    show sayori e3d ma b1a rup
    camera master:
        align (0.5, 0.2) zoom 1.6
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "She pouts a little, before racing over to hug me."
    s b2b mb "I’m so glad you’re here..."
    show sayori ma with say_dissolve
    "I feel a pang of guilt."
    s e1a mb b2a "That you’re finally back."
    show sayori ma with None
    show natsuki e1a me b3a:
        blur 0.0 zoom 0.8 xoffset 0
    show yuri e2c rup:
        blur 0.0 zoom 0.8 xoffset 0
    show sayori b1a ma ldown rdown at i11
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    $ say_transition = False
    "I don’t have time to dwell on this as half a body peeks out from over the stairs."
    m turned casual nb ed mb "Hello, MC! Give me a second to dress and I’ll be down, ahah."
    "I struggle to work out why Sayori’s in a nightie and Monika’s in a gown."
    show natsuki e1a md
    show yuri e1a md
    mc thinking mm eg bi "So, uh, would someone catch me up?"
    show sayori e1b rup lup ml at t11
    show yuri rdown ma
    show natsuki e3c b2a mn
    $ autofocus.unblock("sayori")
    $ autofocus.force_focus("sayori")
    "Sayori breaks away and starts explaining faster than I can think, practically bursting with bubbly and infectious, if incoherent, excitement. Even Natsuki’s grinning."
    show natsuki e1a b3a ma
    show sayori e1a md 
    $ autofocus.restore_focus("sayori")
    mc ldown ml ec ba "Alright. Now try it more slowly."
    s e2a b1d mb lup rdown "Oh, eheh."
    s e1a b1a mh ldown "Well... We thought we should have more out-of-club stuff going on!" # im stuff
    show sayori md
    n b1d e1d mb "What, with you stealing our President after all~"
    show natsuki ma
    s e3c mh "So I arranged..."
    show sayori lup rup e3d mb at hop
    show natsuki b3a e1a ma lhip rhip
    extend " breakfast!"
    show sayori ma
    n cross noband b3d e2a mc "And had about twenty cinnamon rolls.."
    show natsuki ma
    s ldown rdown mc "So now we can all chat here!"
    show sayori e1b mb at hop
    show natsuki turned noband b1a e1a ma
    s "What do you think what do you think?"
    show sayori ma
    "She’s literally bouncing."
    mc ed ba md na ldown "I think it’s great as long as you don’t go too hyper."
    show sayori:
        "sayori turned pyjama e2a b2b md"
        pause 0.001 # i have achieved comedy
        "sayori turned pyjama e3d"
    "Her face sinks... for about a millisecond."
    s e1a mb rup "Great! Oki-doki! Now, can I have your stuff so I can start {i}cooking{/i}?" # im stuff
    show natsuki b3a me
    s e1d mu rdown "I’m starving~"
    show sayori md e1a
    n b1d mh "Already? How...?"
    show natsuki e1d mj at thide
    show sayori zorder 1:
        subpixel True
        "sayori turned pyjama b1d e2a md lup"
        dip()
        "sayori turned pyjama lup e3d"
        xzoom -1
        easein 0.6 xoffset 1000
    "Sayori pouts, grabs my shopping bag, then scurries off like a happy chipmunk."
    show yuri at thide
    hide yuri
    hide natsuki

    scene bg s_living_room with wipeleft

    "I gently make my way further into the living room and am instantly overcome with a wave of nostalgia."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc turned tail nostrands ec mh "I remember being here with Sayori..."
    _mc ef ma "So often..."
    _mc eg "I miss that."
    "I stop myself from ruminating."
    _mc ec mh "I needn’t yearn any longer."
    _mc ea "I’m back here now, for the foreseeable future, at that."
    _mc ma "With three great friends."
    _mc ef mh "And Natsuki."
    _mc ec ma "Making the most and best of these circumstances is what I should do."
    "Thus reasoning, I sweep back into the kitchen, determined to treat them all to the most delicious breakfast possible."
    if preferences.language is None:
        $ auto_advance_date_mult = 1.33
    hide black with NonBlockingDissolve(0.5)
    mc md ed "Alright. Let’s get down to brass tacks."
    show sayori turned pyjama rup e3c b2a me at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "I glance over at Sayori, still nursing her thumb by sucking it into her mouth."
    show sayori e2c b1d md with say_dissolve
    _mc ec ma "It really should be alright by now, judging by how things looked earlier."
    _mc ea "She DID lug those bags along without any issues, after all."
    "I smirk, knowing full well what her game is."
    _mc ec "She’s trying to elicit some comforting attention from yours truly."
    _mc ea "No matter - I’ll play along. Never let it be said that I’m not sporting."
    show sayori e1a b1a me with say_dissolve
    mc bg mf "Aww. Is someone still nursing an ouchie?"
    s b2b e3c mg "Mm-hmm. All I wanted to do was heat up that cooking oil."
    s rdown b1d e1a mi "It didn’t have to be all nasty-like and spit at me."
    show sayori md with say_dissolve
    mc eg mg "Poor thing. Well, we can turn that frown upside-down, can’t we?"
    show sayori b1a  with say_dissolve
    mc ed md ba "Nothing a nice, big juicy omelette can’t fix."
    show sayori ma e1b with say_dissolve
    "At those words, Sayori’s mournful look undergoes a miraculous transformation into the one of the widest grins I’ve ever seen her sport."
    s lup rup e3d mb "Goody goody gumdrops! I haven’t had those in ages!"
    show sayori ma with None
    show sayori at i33
    show natsuki turned noband b3a md at i32
    show yuri turned md rup at i31
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "So loud are her exclamations of delight that Yuri and Natsuki wander over to find out what she’s so excited about."
    show yuri rdown ma 
    show natsuki lhip mh b4 
    show sayori ldown rdown e1a 
    n "Damn, Sayori. I know you can be hyper, but this is just off the chart. What’s gotten into you?"
    show natsuki ma b1a
    $ autofocus.unblock("sayori")
    s lup mb "Just that Melody’s going to make the best thing that could ever grace your morning."
    show yuri e1d
    s e1b ldown mu "Those omelettes were to die for when she made them way back then, and I don’t see any reason why they’ll be any different now. Just you watch."
    show sayori ma
    n ldown e1d b1d mb "Omelettes to die for, huh? And made by Mel, at that? Now this I have to see."
    show natsuki ma
    y lup rup mb "Goodness. Judging from how thrilled you seem at the prospect of omelettes, Sayori, I think I too would very much like to have a taste."
    show yuri e1a ma
    show sayori e1a
    show natsuki e1a b3a
    "I grin at this favourable reception."
    mc ea mb "You can all go one better. You can help participate in their preparation."
    show sayori e3d at thide
    y mb "That sounds lovely."
    y rdown mh e1d "Lead us on?"
    show yuri ldown ma at thide
    mc eh md "Gladly."
    show natsuki at thide
    hide natsuki
    hide sayori
    hide yuri

    scene bg s_kitchen_day with wipeleft

    "As I enter the kitchen, I turn to Sayori."
    show sayori turned pyjama md at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc turned tail nostrands md ed "Have you, fellow lady, any curry powder?"
    mc mg ea "With which I can spice my eggsicles."
    show sayori e3c lup rup nc ma with say_dissolve
    "She blushes slightly and shakes her head, raising her arms. Looks like she’s playing along."
    s ldown rdown na e1a mh "’Fraid not, good Lady..."
    show sayori ma with None
    show sayori at i22
    show yuri turned e2a ma b1d nc lup at i21
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Yuri {i}also{/i} blushes, though I’ve no idea why."
    mc md ed "Art thou well, dear Yuri?"
    y mk b2b nd "I, uh..."
    y b1a e1d mh nb "I have some."
    y e2c b1d mg "... Uh, on..." 
    show sayori e3d
    y mb e1a na b1a ldown "On my person, I mean."
    show yuri ma
    mc ea mf thinking "Oh?" 
    "I look at her quizzically."    
    _mc ec mh "She’s broken character, but I didn’t really expect her to play along in the first place."
    _mc ea "More than that, I’m confused as to where - and why - she would keep curry powder on her person, but something tells me I won’t find the answers I seek here."
    mc ldown ml "Well, uh, great."
    mc mb "Mind if we use it?"
    show sayori e1a
    y e1d mh "Surely not. Here."
    show yuri b1d e3c md
    "She retrieves a pot from the depths of her blazer pockets."
    show yuri e1a b1a ma at dip
    "She hands it to me, and bows slightly."
    mc mb "Thanks Yuri."
    show yuri at thide
    hide yuri
    show sayori at t11
    mc ec mf "Now..."
    show natsuki turned noband b3a me at t21
    show sayori at t22
    mc ea mg "Natsuki, mind de-shelling a couple of eggs?"
    n e2a b1a mh "If I have to."
    show natsuki md b1d
    "She grumbles, but I sense she’s secretly happy." 
    show natsuki e1d mj
    mc ed md "Oh, and make it seven."
    n cross noband e3c b3a mi "Fiiine."
    show natsuki turned noband e2a md at thide
    hide natsuki
    show sayori at t11
    "She goes and starts preparing those."
    show monika turned at t41
    "Out of the corner of my eye, I watch Monika enter the room."
    show monika mc
    "She glances around and raises an eyebrow at the kerfuffle, so I call out to her."
    show sayori at t22
    show monika at t21
    mc ea mb "Monika, would you slice and fry some onions please?"
    show monika ma
    show sayori e2a md b1d
    mc ed bd md "I don’t trust Sayori with a frying pan."
    show sayori e3d mn
    show monika ed
    "Sayori pouts in response, but after a moment she leads us in a round of laughter."
    show monika eb at thide
    hide monika
    show sayori e1a mb b1a at t11
    $ autofocus.unblock("sayori")
    s "So, what can I do?"
    show sayori md
    mc ea mf ba "You can...." 
    show sayori e1d b1d
    mc md ed "Find the salt and pepper."
    show sayori e2a at thide
    hide sayori
    "She pouts a little before going to retrieve them."
    play sound clatter
    "... And a plate falls on her head."
    s turned pyjama me "Oh..."
    "Her tone surprises me."
    _mc ec mh "It’s as if this is an everyday occurrence."
    "Still, I go to help her; the last thing we need is an injury."
    show sayori md at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc ea bg mb "It’s okay, Sayori."
    mc "Did any glass get you?"
    s e2a mg "No..."
    show sayori ma with say_dissolve
    "She speaks as if holding in laughter."
    mc ba mg "Okay, good. Go and grab a chair and sit down, okay?"
    s e3d mb "Okee!"
    show sayori ma with None
    hide sayori
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("sayori")
    $ say_transition = False
    "She suddenly perks up."
    _mc ec md bi "That crafty little..."
    show yuri turned lup e1d mh at t11
    y "Um, want me to... clear this up?"
    show yuri md
    "Yuri points to the remains of the plate." 
    show yuri e1a ma
    mc ea mg ba "Oh, sure, thanks Yuri."
    show yuri e3c at thide
    hide yuri
    show natsuki turned noband lhip rhip b3a mg at t11
    "Yuri seems to almost immediately have a dustpan in hand. Natsuki also motions that the eggs are done." 
    show natsuki ma at thide
    hide natsuki
    show monika turned mc at t11
    mc mb "Monika, how’re you doing with the onions?"
    m eb mb "Almost done."
    show monika ma at dip
    "I’ve been watching her closely, and that must have been the fifth time she’s smoothed her skirt down."
    show monika at thide
    _mc ec mh "Is she self conscious?"
    hide monika
    "I move closer to her, and take the knife from the block and take the last onion from her hand."
    "And start cutting quickly." 
    "Much to everyone’s amazement, I make extremely quick work of it, with perfectly neat cuts."
    show monika turned mc at t42
    show yuri turned e1d md at t41
    show natsuki turned noband b3a rhip me at t43
    show sayori turned pyjama me at t44
    "I look round at everyone’s faces."
    mc ea mg "What? I cook for myself."
    show sayori ma
    "Sayori’s face changes to happy first."
    show natsuki md
    s e3d mb "At least we have one expert chef!"
    show sayori ma
    show monika ma
    y lup e2a b1d mb "I... know a few recipes too."
    show yuri ma
    m ed mb "So do I!"
    m lpoint ea "You know what, let’s try and have a weekly cooking day."
    show monika ma
    show natsuki ma
    show yuri e1a b1a ldown
    s lup e1a mb "Yeah, sounds fun."
    show sayori ma
    n cross noband e2c b1d mc "Okay... Sure. As long as the host has to buy the ingredients."
    show natsuki ma
    s mb "Don’t worry, I will!"
    show sayori ma ldown
    show natsuki e1a b1a
    "Something tells me that Sayori has enough spare food to keep us all satiated for a hundred years."
    _mc ec ma "Except maybe herself."
    m mb ldown "I’ll happily contribute too. I’m the president, after all."
    show monika md
    n turned noband lhip rhip b3a mo e3d "And we’ll never forget it."
    show monika ma
    "Monika looks momentarily hurt, but then goes back to normal."
    m ec mb "Never, ever."
    show monika ea ma at dip
    show natsuki ldown rdown e2a b1d md
    "On the second ever, she gently taps Natsuki’s nose, much to her annoyance." 
    n cross noband e1d b3d mh "Quit it!"
    show natsuki md
    mc ml ea "Hey, are we going to start cooking or not?"
    show yuri e1d me
    s mb "Yeah, come on guys."
    show natsuki b1a e1a me
    show sayori ma
    "Yuri and Nat both look at her with a feeling of obvious:"
    show yuri lup mh zorder 3
    show natsuki turned noband lhip rhip b1d e1d mi zorder 3
    $ autofocus.force_focus("yuri")
    $ autofocus.force_focus("natsuki")
    "Y & N" "{i}Why are you so constantly, infuriatingly cheery?{/i}"
    $ autofocus.restore_focus("yuri")
    $ autofocus.restore_focus("natsuki")
    show yuri md at thide zorder 2
    show natsuki mj at thide zorder 2
    show monika at thide
    show sayori at thide
    _mc ea ma "Maybe they still could have a friendship after all."
    hide yuri
    hide natsuki
    hide sayori
    hide monika
    "I take Monika’s onions and place them into a pan, in which I’ve been doing what stymied Sayori earlier."
    play sound_loop frying_pan fadein 2.0
    "Heating some oil."
    "A satisfying sizzle ensues as they mingle with the bubbling liquid and steadily fry."
    show sayori turned pyjama mu e1b at t44
    "Music to my ears, and evidently to Sayori’s, too-"
    show sayori ma at t11
    "-For she toddles over, depositing herself on a stool close to me as I turn the onions over with my skiller."
    show sayori e3c md
    "And inhales deeply of the cooking vapour."
    show sayori e3d ma nc lup at thide
    "Eyes wide shut and face flushed with pleasure."
    "The others give her an odd look, but not me."
    "She always used to do this whenever I was cooking."
    "And I can thoroughly relate to where she’s coming from - the smell has a rich homely quality to it."
    _mc ec mh "A comforting reminder of happy times long past."
    hide sayori
    show monika turned mc at t41
    "I turn to Monika, gesturing toward the pan."
    mc ea mb "Want to try a smell?"
    m eb mb "Uh, sure, eheh."
    show monika ec md at t11
    "I step back and gently usher her toward the sizzling pan."
    show monika ma
    "She inhales it gently and a large smile breaks her lips."
    m ea mb "Lovely."
    m rhip ed "I can’t wait to try it!"
    show monika ea ma at thide
    hide monika
    "She steps back and ties up her hair."
    mc mg "You guys need any more guidance?"
    show monika turned eb mc rhip at t31
    show yuri turned at t32
    show sayori turned pyjama mb at t33
    s "Nope!"
    show sayori ma at thide
    y e1d mb "Pour on when golden brown, yes?"
    show yuri e1a ma at thide
    mc ed md "You got it."
    show monika ea rdown mc
    mc ea mg "I’ll go sort the table."
    m mb "I’ll come help."
    show monika ma at thide
    "I nod to her, and we start moving out of the kitchen."
    hide yuri
    hide monika
    hide sayori

    stop sound_loop fadeout 2.0
    scene bg s_living_room
    show monika turned at i11
    with wipeleft

    "We take some cutlery and plates through to the living room."
    "I then start placing seats down at the table."
    m rhip md "So, how’d you get so good at cooking?"
    show monika mc
    "I take a second, her question startling me, before I realise she doesn’t know about the witch."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc turned tail nostrands ec mh "Should I tell her?"
    _mc ea "I realise it’s only fair."
    _mc ef "Sayori knows, Natsuki undoubtedly knows."
    _mc eg ma "I’ve moved on from grieving, anyway."
    show monika md rdown with None
    hide black with NonBlockingDissolve(0.5)
    mc ea mg "Well, uh, my parents left me when I was younger. Cooking on your own really hones your skills."
    show monika eb bb mc
    "She grimaces a little."
    m md "Sorry, I didn’t-"
    show monika ea ba mc
    mc mb "Honestly Monika, don’t worry. I’m past it. Plus, Sayori gets more food to eat."
    show monika ma
    s "Did somebody mention me?"
    show sayori turned pyjama e3d at t21
    show monika eb at t22
    "Sayori bursts through the door and settles in the armchair."
    show monika ma ea
    "Monika looks at me, then continues."
    show sayori e1a
    m lpoint mb "MC was just saying that she likes baking for you. I think it’s sweet."
    show monika ma
    s e1d mh b1d rup "You mean what she makes or that she makes it?"
    show sayori md
    show monika ldown ed
    "Monika chuckles politely."
    show sayori ma b1a e1a rdown
    m mb ea "Well, I think everything about her is kind of sweet."
    show sayori ldown
    show monika ma nb eb
    "She smiles beautifully, then seems to blush and recede."
    "I find myself flush, biting my lip softly."
    "Every time she speaks, or even looks my way..."
    show black with NonBlockingDissolve(0.2):   
        alpha 0.5
    _mc mh ea "Something about her makes me feel so..."
    _mc ec ma "So special."
    _mc "And pretty."
    _mc ea "I’m glad I have her."
    _mc "That we all have her."
    hide black with NonBlockingDissolve(0.5)
    mc mb "Why thank you, Monika. I could say the same of you."
    show monika ec
    "She blushes even harder." 
    show natsuki cross noband e2a b3a mh at t31
    show sayori md at t32
    show monika at t33 
    n "I don’t think you’re cute, Mel."
    show monika ea na
    show sayori e2a b1d md:
        subpixel True
        easein 0.17 xoffset -100
        easeout 0.17 xoffset -50
    show natsuki:
        subpixel True
        pause 0.16
        "natsuki cross noband nb e2b mm b3d"
        easein 0.14 xoffset -20
        easeout 0.14 xoffset 0
    "Natsuki receives a sharp elbow from Sayori. I note that the pink-haired girl still has her face angled away."
    show natsuki e2a b1a md 
    s mh e1a "No being a meanie!"
    show sayori ma b1a
    n turned noband lhip mh b3a "Fine... B- But only because I want the omelette."
    show natsuki ldown md
    mc ed md "Hey, I’ll take that."
    show natsuki e1a ma
    mc ea mg "So, how has everyone’s day been?"
    show natsuki md
    s rup rup e3d mb "Good, because we have the club after school!"
    show sayori e1a rdown ma
    n e2a mh "Eh... We’ve chemistry at least."
    show natsuki b1d md
    s ldown mb e1d b1d "Ehe, yeah you do~"
    show sayori ma
    "We all proceed to ignore her light jab."
    m lpoint mb "Great, we have PE."
    show natsuki e1a b3a me
    show monika mc ldown 
    show sayori e1a b1a md
    "Everybody looks around for a fourth voice."
    "Then realise Yuri’s in the kitchen."
    _mc mf "Ah."
    show sayori b2b
    _mc ec mh "I did not think this through."
    _mc ea ma "I’ll go offer her help."
    show monika ma
    mc mg "I’ll go see if she’s okay."
    show monika mc
    show sayori b1a me
    n e2a mh "Yeah, please."
    show natsuki md
    "We all look at her."
    _mc thinking mh ea "Natsuki? Asking about her wellbeing?"
    _mc ec "What did they talk about in the kitchen whilst we were gone?"
    show natsuki e1a
    _mc ma ea ldown "Still, not that I mind."
    show sayori ma
    n e1b mm b1d "What?"
    n cross noband e2a b3a mh "I just want her to finish our omelette."
    show natsuki mj at thide
    show monika ed ma at thide
    show sayori e3d at thide
    "We smile, and I leave to go get Yuri."
    hide natsuki 
    hide sayori
    hide monika

    scene bg s_kitchen_day
    show yuri turned e2a at i11
    with wipeleft

    "I open the kitchen door to find Yuri the happiest I’ve seen her."
    "She’s washing the pan up, hair and hands covered in bubbles, bobbing to some inaudible tune."
    "She looks so peaceful, I actually consider not saying anything."
    "Until.."
    n cross e2a b3a mh "Hey, Yuri."
    show natsuki mj at t22
    show yuri b2a e1b mk nc lup at t21
    y "Hira- Agh, uuuuuu..."
    _mc turned tail nostrands ec "Ever startled."
    show yuri b2b e2a ma nb
    n turned noband b1d mh "Sorry Yuri, but, well, you just kind of left."
    show natsuki b1a md
    y e3c mb "N- No, it’s quite alright, I should have told you. I simply can’t abide leaving without washing up."
    show yuri e1a ma na
    show natsuki e1a
    mc ea ml "Yes, but Yuri..."
    show yuri b1a me
    "I open a pull-down cupboard."
    show natsuki ma
    mc mb "Sayori has a dishwasher."
    y ldown e2a mh b1d "Oh. Okay."
    y e1d b1a mb "Let me just finish this plate, and I’ll bring the omelette in."
    show yuri ma at thide
    "When I reply 'yes', she brightens considerably."
    mc mg "Come on, Natsuki. She’ll be through in a minute."
    show natsuki b1a mg e3c at dip
    "Natsuki sighs and follows me."
    show natsuki mj at thide
    hide natsuki
    hide yuri

    scene bg s_living_room
    show sayori turned pyjama md at i33
    show monika turned at i32
    show natsuki turned noband b3a at i31
    with wipeleft

    "We sit down and I start to explain." 
    mc turned tail nostrands ml "Basically, Yuri..."
    mc mb "Yuri likes washing up."
    show sayori ma
    mc ed md "She’ll be through in a second."
    $ advance_date(seconds=1) # we love comedy in here
    show yuri turned at t41
    show natsuki at t42
    show monika at t43
    show sayori e1b at t44
    "As I say this, she walks through the door, carrying a large omelette."
    y mb "Here you all go..." 
    show yuri e3c ma at dip
    show sayori mu
    "She places the omelette on the footstall, and we all move closer."
    show yuri e1a at dip
    show monika eb
    "Then she hands us the cutlery and plates Monika and I forgot."
    show sayori e1a ma
    _mc eh bg nb teehee "Ah."
    show monika ea
    s mb lup "I think it only fair that Melody tries some first."
    show sayori e3d ma
    mc ea mb na ba "Happily, but then you all tuck in."
    show sayori e1a ldown
    show natsuki me
    "I gently take a piece on a fork and try it..."
    _mc eg bi ma "Not to blow my own trumpet, but this is delightful!"
    show natsuki e2a ma
    mc ea mb ba "I think you all will like this."
    show natsuki e1a
    s e3d mb "You bet!"
    show sayori e1a ma
    n lhip rhip b1d e3d mo "We made it, after all."
    show natsuki b3a e1a ma ldown rdown
    show sayori lup mg at dip
    "I chuckle and lean back, content to let them enjoy our work."
    show sayori ldown e3d md
    "As Sayori tries some, she squeals and exclaims:"
    show natsuki mg e3c at dip
    s lup rup mt e1b "Oh my God! Just as good as I remember."
    show monika md ed at dip
    n cross e2a b3d mb "Not bad..."
    show sayori ma ldown rdown
    show natsuki ma
    m mb ea "Goodness, MC..."
    show monika ma
    show yuri mg e3c b1d at dip 
    _mc ec mh "And Yuri?"
    show yuri lup rup b1a ma e1d
    "Yuri makes a weird happy clap and a smile."
    y e1a mb "Thank you."
    show yuri ma ldown rdown
    m mb "This is delicious, thank you."
    show monika ma
    show sayori e1a
    "She gently leans closer to me, smiling happily."
    show natsuki b1a e1a md
    show monika mc
    show sayori md
    show yuri me e1d lup
    stop music fadeout 3.0
    mc ed md "Guess we’ll all go to school much more full this morning~"
    m md "School?"
    y mg "O- Oh."
    show yuri md
    show natsuki turned b3a me
    "We all look at each other, it slowly dawning on us."
    _mc ea mh "..."

    play music poempanic

    show sayori ma
    show yuri e2a mk b2b nb
    show natsuki e3c b3d mm
    show monika eb bb at thide
    mc bb eb nb mg "Shoot, we’re going to be late!"
    hide monika 
    show sayori mb e3d at t33
    show natsuki at t32
    show yuri at t31
    s mb e3d "Going to be? Forget that, we already are!"
    show sayori ma at t22
    show yuri at thide
    hide yuri
    show natsuki cross noband b1d e2a mi at t21
    n "Ah, there goes my perfect attendance so far this term."
    show natsuki mm at thide
    show sayori e2c at rhide
    hide sayori
    hide natsuki
    "Sayori rapidly makes her way upstairs to change, and the rest of us scramble to gather our gear."
    _mc ef bg ma "We really waltzed right into this one, didn’t we."
    _mc eg "It’s too bad, the omelette really is something special."
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    
    stop music fadeout 2.0
    scene bg school_corridor_2_day with longfade
    $ set_date(hour=15, minute=5)
    $ set_internet(False)
    play music daijoubu

    _mc turned tail nostrands eg bg mj "Finally... The end of Geography."
    _mc ea ba ma "I can go to the club and chill."
    show yuri turned rup e2b nc mb at t11
    y "Er, h- hi! Uuum..."
    show yuri ma
    _mc mh "Yuri? What’s she doing here?"
    show yuri e2a
    camera master:
        align (0.5, 0.1) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("yuri")
    $ say_transition = True
    mc mb "Oh, hi Yuri."
    mc "How’re you?"
    y nb b1d mb "Fine, thank you. Did you want to walk to the club together?"
    show yuri ma with say_dissolve
    mc ed "Sure."
    show yuri b1a e3c na
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "She sidles up alongside me and we begin to walk."
    $ autofocus.unblock("yuri")
    y rdown e1a mb "S- So, do you like geography?"
    show yuri ma
    mc thinking ec ml "I’m good at it, but I don’t like it."
    mc ea mg "What about you?"
    y e1d mh "I... find it easy, but..."
    y e2a b1d mb "... I’m too nervous to answer any of the questions..."
    show yuri ma
    "Before I can say anything, a snarky voice appears."
    show yuri lup e1d b1a md at t22
    show natsuki turned lhip rhip b3a e3d mo at t21
    n "Maybe I should whip you into shape."
    _mc ea ma ba "Somehow I don’t doubt Natsuki is full of her own special kind of confidence."
    show natsuki e1a ma ldown rdown
    y mg e2a b1d "Oh, er, Natsuki."
    y ldown e1a b1a mb "That’s very kind of you."
    show yuri ma
    n lhip e3c mi "No need to be so submissive, honestly, it’s fine. I’ll happily help you with it."
    show natsuki md
    y e2a mh "Yes, I suppose. I... know you’ve talked about showing me your reading... material in the past... Would you like to?"
    show yuri ma
    show natsuki ldown e1a me
    "Natsuki and I look taken aback."
    _mc thinking mh "What’s gotten into those two today?"
    n cross b1d e2a mh "O- Okay Yuri. I’ll show you in club time."
    show natsuki ma
    show yuri e2c
    "They both start smiling a bit more."
    show natsuki turned ldown b1a ma e1a at thide
    show yuri e1d me at thide
    hide yuri
    hide natsuki
    "... Then Natsuki comes, grabs Yuri’s arm, and leads her off, talking to her about a gruesome manga."
    "I sigh."
    _mc ldown eg mf "At least they’re happy."
    _mc ma "Or, at least Natsuki is."
    
    scene bg club_day with wipeleft_scene
    $ advance_date(minutes=4)

    "I walk into the clubroom, book already in hand."
    _mc turned tail nostrands ec mh "For some reason, the action makes my heart lurch."
    _mc ea "That oddity aside, I could probably do with some alone time. Plus, I’d actually like to read my book."
    show bg class_1_day as class_day:
        align (0.2, 0.55) zoom 3.0
    with Dissolve(0.2)
    "I go over and sit in the lush, leather covered chair."
    "That’s when I question why there’s only one."
    "And realise it’s a teacher’s chair."
    "I go to move, but... well."
    _mc "I don’t really care."
    _mc ea ma "It’s comfy and nobody is even looking."
    play sound door_knock
    "That’s when the knock on the door happens."
    hide class_day
    show bg:
        align (0.4, 1.0) subpixel True
        zoom 2.0
    camera master at vpunch
    play sound slam
    "I jump out of the chair and kick it back with such force I end up hitting the ground hard, face first."
    show bg:
        easein 0.2 zoom 1.0
    "I hastily sit up and look around like a meerkat."
    show mrs_mills at t11
    "As Mrs Mills enters, she gives me a confused look."
    mrs_mills "Hello, girls. Mind if I steal my laptop?"
    show mrs_mills at t21
    show monika turned mb at t22
    m "Go ahead, Miss. We weren’t using it."
    show monika ma at thide
    mrs_mills "Thank you."
    hide monika
    show mrs_mills at t11
    mrs_mills "Oh, and Ms. Nakamura?"
    mc mf nb bb "Yes?"
    show mrs_mills at thide
    mrs_mills "There are more effective ways to clean floors."
    hide mrs_mills
    "She chuckles as she walks away."
    "I blush furiously and reconsider my life choices."

    scene bg club_afternoon with wipeleft_scene
    $ set_date(hour=16, minute=20)

    "As club time draws to a close, I go over to Sayori." 
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc turned tail nostrands ml "Hey, Sayori?"
    s lup mb "Yepsies?"
    show sayori ma with say_dissolve
    "I internally roll my eyes at her overt cheeriness."
    mc mb "I was wondering if I could arrange a group phone call tonight." 
    s e1b mc "Ah!"
    s e1a ldown mb "You might want to speak to Monslie. She’s the President after all."
    show sayori e3d ma with say_dissolve
    mc ed md "Alright, thanks."
    s mb "No problem!"
    show sayori mn with None
    camera master
    show sayori e1b
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Then, as if she can’t hold it in, she bursts out smiling and simply says:"
    show sayori lup rup e3d mb at hop
    $ autofocus.unblock("sayori")
    s "Wibble."
    show sayori ma e1a
    "I raise my eyebrows at her."
    s b1d mh "What? It’s nice to say."
    s rdown e1b b1a mb "Wibble."
    s ldown e1a mh "You try it."
    show sayori ma
    "I roll my eyes and say it." 
    mc mj ec "Wibble."
    show sayori e3d mn
    "I internally cringe."
    show black onlayer above_master with {"above_master": Dissolve(0.2)}:
        alpha 0.5
    _mc ma bi eg "I sound like a certain sardonic British Army captain."
    _mc ec ba "Still, not that I mind."
    _mc ea "It’s just the two of us goofing about..."
    _mc ef "Like we used to."
    "A pang of sadness runs through me before I quash it again."
    "No nostalgia."
    "Just making memories."
    hide black with {"above_master": Dissolve(0.2)}
    s e1a mb "See? Fun!"
    show sayori me
    mc ed ba md "I suppose so, weirdo."
    mc ea mb "Want to walk home with me?"
    show sayori tap eb
    "She pouts."
    s ea md bc "What else were you expecting me to do?"
    show sayori ma
    mc mg ed bm "Be independent?"
    s turned lup e3d mb b1a "No... I have you for that."
    show sayori b2a e1a ma ldown with None
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "I chuckle as she shuffles closer to me."
    s mh "Would you... buy me a snack?"
    show sayori md with say_dissolve
    "Her big blue eyes make me unable to resist."
    show sayori e3d mo b1a with say_dissolve
    mc md ef bi "Sure..."

    stop music fadeout 1.0
    scene bg school_street_afternoon
    camera master
    show sayori turned e3d:
        matrixcolor TintMatrix("#ffeede")
        i11
    with fade
    $ advance_date(minutes=10)
    $ say_transition = False
    play music ohayou

    "And so it is with a light heart - and even lighter wallet - that I find myself trotting off into the sunset with Sayori."
    "Helping ourselves to a carton of piping hot and scrumptiously fluffy takoyaki balls from the seafood place a couple of blocks away from the school."
    show sayori e3b md
    "It’s mostly Sayori who helps herself, although I do manage to pop in a nibble or two edgeways."
    show sayori e3d ma
    _mc turned tail nostrands ec "Just like old times."
    _mc ea "The fun is always worth the price of admission."
    show sayori e1b lup mu
    _mc ec mh "And what silly, spiffing fun it is, to the point where we nearly overlook..."
    show sayori e1a md
    mc mj "... Hold it right there."
    $ autofocus.unblock("sayori")
    s tap md bc "Aww! You can’t NOT toss me that last one, Melly." 
    s turned e3c mi b1d "You promised to let me show off how good I am at catching treats with my hands behind my back."
    show sayori md
    mc ea mg "First things first, Sayori. Home isn’t too far away, and we’ve put off organising tonight’s group chat long enough."
    s e1a mh b2a "But that last ball will get cold, and lonely too. It needs to join its family right down here in the bottomless pit."
    show sayori md
    mc ed md "All the more incentive to get things over and done with double quick then, missy."
    s e2a b1d mg "Hmph. Okay." 
    show sayori e1a b2b ml lup
    "I deftly manoeuvre the final takoyaki ball out of Sayori’s reach as she tries in vain to grab at it, in spite of her claimed resignation."
    show sayori md
    mc thinking ec mf "Now, as for my idea..."
    show sayori b1a ldown
    mc ea mg "We were pretty much segregated into three groups throughout the whole of club time today, each with its own volume."
    s mh "Uh-huh. Monika and myself, Natsuki and Yuri, and you as your own little army of one."
    show sayori md 
    mc mb "Well, I’d love for us to reconfer, the same way we usually do at the end of our sessions."
    s lup mh "Hmm. We didn’t do that this time around, did we?"
    s ldown mb e2a "I guess we all got so engrossed in what we were reading, we just forgot the time and all about the normal base-touching before heading off."
    show sayori e1a ma
    mc ldown mg "The idea I’ve got is for us to have a mini evening book club meet to make up for the omission." 
    show sayori me
    mc mb "Discuss what each group was reading, you know?" 
    mc ml "I mean - If we were all so caught up in our respective materials, I reckon they’re sufficiently interesting for some good discussions to be had."
    show sayori ma e1b
    mc ed md "Besides - something would feel terribly left out if we don’t get back together before the day is over."
    s rup mb "Good idea. But you know what REALLY feels left out? That takoyaki ball you’ve got there in your hand."
    s e3d mc lup "Gimme gimme gimme."
    show sayori ma
    mc mb bd ea nb "You’re incorrigible, you know that, right? Here - have at it. Open wide."
    s ldown rdown mi "Aaah!"
    show sayori ma

    scene bg residential_afternoon
    show sayori turned:
        matrixcolor TintMatrix("#ffeede")
        i11
    with wipeleft_scene
    $ advance_date(minutes=18)
    $ set_internet(True)

    "When we arrive home, I throw one look at Sayori and know what to do."
    mc turned tail nostrands mb "Want to come in?"
    s mb rup "Sure!"
    show sayori ma
    mc ed md "And help me message Monika?"
    s lup e3d mb "Of courselses!"
    show sayori e1a ma ldown rdown at rhide
    hide sayori
    "She pushes past me and through my door."
    _mc ec mh thinking "Wait..."
    mc ea mg "Hang on, Sayori, how did you know my door was unlocked?"
    show sayori turned mb lup e2a:
        matrixcolor TintMatrix("#ffeede")
        t11
    s "I just... did, eheh."
    show sayori ma
    "I raise an eyebrow but don’t question her." 
    s ldown e1a mb "Come on, let’s go call Monslie."
    show sayori ma at thide
    hide sayori
    "I follow her in, grinning."

    scene bg mc_house_entrance_afternoon
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        t11
    with wipeleft

    s mh "So, where’s your phone?"
    show sayori md
    mc turned tail nostrands ml "The landline's in the living room - where it's always been - you goose. In the meantime, I’m gonna go get dressed."
    s mb "Can I borrow some stuff? I want to change too!" # im stuff
    show sayori md
    mc mg bd "Sayori, your house is literally right there."
    s lup b3d e3c mh "I know... But I want to stay here~"
    show sayori md
    mc bi eg mj "Ugh, okay, I’ll go get some from yours."
    s e3d mb ldown b1a "Thank you!"
    show sayori ma at thide
    hide sayori

    stop music fadeout 4.0
    scene bg s_house_afternoon with wipeleft
    $ advance_date(minutes=3)

    "As I approach her door, I feel an overwhelming sense of nostalgia."
    "One which I seek to quash."
    _mc turned tail nostrands mh "I just... want to..."
    _mc ec "Be with Sayori now."
    _mc eg "Actually, that’s not quite true."
    _mc ea ma "I want to be with the whole club."

    play music pensive

    "Now my nostalgia is replaced with self-disgust."
    _mc ec mh "How did I get so pitiful as to be fawning for love from anyone, especially three girls I barely know?"
    _mc "I shouldn’t need love so much."
    _mc eg "I shouldn’t be so pitiful."
    _mc bi "And it’s all her fault."
    _mc mm "The witch."
    _mc ec mh "And my fault."
    "I feel a tear begin to well."
    _mc "But now..."
    _mc ea ba "No matter how much I hate her."
    _mc ma "I have a better family now."
    _mc "A better family than I could ever have hoped for."
    "I open her front door as I allow a few tears to fall."

    scene bg s_house_entrance_afternoon with wipeleft

    "They land upon the carpet and they stain it lightly."
    _mc turned tail nostrands ec mh "She might not notice..."
    _mc ea "But I should go get her clothes."
    _mc mm bi eg "Dammit."

    scene bg s_house_corridor_afternoon with wipeleft

    "As I walk slowly through the house, I feel an emotion I’m not used to."
    "A combination of simmering anger and deep... sorrow? Regret?"
    _mc turned tail nostrands ec mh "It’s just... an aching."
    "I climb the stairs and start to question what’s causing these emotions..." 
    _mc ea "Being back with Sayori?"
    _mc "Reminded of the witch?"
    _mc "Regret over a long-broken kiss?"
    _mc eg "I don’t know..."
    _mc ec "I just... can’t escape this feeling of sadness."
    _mc ea bg "Everything involving Sayori just... carries it."
    _mc "This air that tells me I’m a failure."
    _mc eg "This immense feeling."
    play sound slap
    "I gently hit my cheek."
    _mc ec bi mh "Snap out of it. Get her clothes. Get home."
    "I fumble around with her bedroom door before realising it’s locked."
    _mc ea thinking ba "If I’m Sayori, where would I have put the key...?"

    stop music fadeout 2.0
    scene bg m_bedroom_afternoon
    camera master:
        align (0.05, 0.8) zoom 1.6
    with monika_pov(True)
    $ set_pov("m")
    $ advance_date(minutes=14)
    play sound fall
    play ambient int_day fadein 1.0

    "I collapse onto the bed, exhausted." 
    _m turned md ec nb bb "I’ve been going non-stop since last night."
    _m mc "My essay’s finally done..."
    _m bc "My parents’ second one at least."
    _m ea ba na "Just three more to go."
    _m ma ec bc "Then, I can move to {b}schoolwork{/b}."
    camera master
    with Dissolve(1.0)
    "I stand slowly."
    _m mc ea ba "I should change, now I’m done."
    _m ec "No sense risking a verbal blitzkrieg over getting anything stained when I don’t need to."
    show black:
        alpha 0.0
        ease 6.0 alpha 0.5
    "I slowly allow my blazer to fall past my shoulders and land neatly on the bed."
    "I bring my hands up and slowly begin to undo the buttons."
    "I relish the cool sir on my neck."
    "My shirt now falls about my ribs."
    "I slowly undo the catches at the sleeves, drawing my arms back through the sleeves."
    "As I do, I feel a rush of happiness."
    "The stiffness from my neck and arms gone, I decide to liberate my legs, too."
    "I can wallow in freedom for a moment, at least."
    "I reach down, lift my skirt a little, and roll down the hosiery."
    "I can practically feel my legs rejoice in contact with the air."
    "I take a moment to swing them, as if a child, enjoying the freedom."
    "Then a wave of... something, hits me-"
    _m ea dress "Sadness?"
    _m bb "Nostalgia?"
    _m eb "Regret?"
    "I’m not sure..."
    "Nor why I feel it."
    show melody turned thinking ec mh:
        i11
        flash
    "I can’t help but have my thoughts flicker to Melody."
    _m ea ba mc "Is {b}she{/b} why?"
    _m "..."
    _m ec "No."
    _m eb ma "It’s just... nice to have a new member."
    _m mc "It’s left me feeling... jittery inside."
    _m eg bb nb ma "Besides, it’s rather... inappropriate to think of her in this state."
    "I decide to get changed, then I can go from there."
    
    stop ambient fadeout 2.0
    scene bg residential_afternoon with mc_pov()
    $ set_pov("mc")
    $ advance_date(minutes=5)
    play ambient ext_night fadein 1.0

    "I stand back and wait for Sayori to let me in."
    "While waiting, I take a moment to consider my feelings."
    _mc turned tail nostrands mh "Less melancholy now, certainly."
    _mc ef ma "More just... slightly happy."
    _mc ec mh "But I must stop dwelling."
    _mc ea ma "Time to go make new memories with Sayori..."
    _mc ec mh "If she ever lets me in."
    
    stop ambient fadeout 2.0
    scene bg m_bedroom_afternoon
    show black:
        alpha 0.5
    with monika_pov()
    $ set_pov("m")
    $ advance_date(minutes=6)
    play music faith

    "Undressed, I look around me."
    show bg m_bedroom_afternoon as stuff:
        alpha 0.0 align (0.0, 1.0) zoom 1.5
        parallel:
            ease 17.0 align (1.0, 0.8)
        parallel:
            ease 1.0 alpha 1.0
    _m turned dress bc mc "Oh, how I hate this new room so much. Loathe it with every fibre of my being."
    "Every surface is hot pink, plush, radiating artificial sweet comfort, which truly just disturbs you."
    "A reminder that I'm nothing compared to the heir apparent."
    "Everywhere I look are sickly sweet, overly feminine reminders of my purpose to simply be married off, to not talk back but to do whatever my parents wish."
    "I lean back upon my plush bed and sigh."
    _m ec md "These tears won’t come..."
    _m ea mc "Because this room is a prison against rebellion."
    _m ec "I wish I had the literature club with me now."
    _m "The club room is my only salvation-"
    _m bc "-Its members, my armament."
    _m eb "I wish I could just... talk to them."
    _m bb "Sayori, Yuri, Natsuki... Melody, even."
    _m ec "Just some distraction."
    "I sigh again, almost sobbing."
    _m md "Why am I trapped...?"
    play sound fall
    "I lie flat on my bed."
    call close_eyes() from _call_close_eyes_5
    "I close my eyes and imagine a different place and time."
    _m mc ba "Somewhere I can lie, naked and unburdened in the grass."
    hide black
    _m "People always compare me to unicorns or other sickly girly animals."
    _m "That is not what I am."
    _m bc "I’m a snake."
    _m "I’m ethereal, and pretty, yes."
    _m "But I’m certainly not harmless."
    _m "I don’t want..."
    _m "I don’t want to be seen as the harmless schoolgirl."
    hide stuff
    _m bb "Because something tells me I’m more than that."
    stop music fadeout 4.0
    play ambient int_day fadein 5.0
    call open_eyes() from _call_open_eyes_4
    "I open my eyes slowly and cover my chest."
    "The air is so cold in here."
    "That’s when I see my father watching me through the doorway." 
    m ea md "F- Father..."
    dadm "You have a phone call, {i}daughter{/i}."
    "He practically spits this last word."
    dadm "And come to my office when you’re done. {i}Clothed{/i}."
    dadm "Unless you want me to call them back on speakerphone."
    "He places the phone on my dresser and turns on his heel."
    "Shaking, I slowly walk towards the phone."
    _m md nb bc ea "I don’t know this number..."
    _m mc "Is it Father?"
    _m ec "I’d better answer."
    "I quietly prepare my best reserved, polite voice."
    "I answer it and speak."
    $ mc_name = "???"
    python hide:
        mc = phone.character.character("mc")
        mc.name = "Unknown"
        mc.icon = phone.asset("default_icon.png")
    phone call "mc"
    phone_m ea na mb ba "Good day. Monika Rein here, on behalf of Rein Enterprises. How may I help you?"
    phone_mc "Monika?"
    "{i}Melody?{/i}"
    $ mc_name = "Melody"
    "{i}W- What?{/i}"
    phone_m "How did you...?"
    phone_m "Get this number?"
    phone_mc "Sayori gave it to me. I just wanted to see if we could arrange some kind of club meetup tonight, as we didn’t have that long to discuss literature today."
    phone_mc "Are you okay, Monika? You sound all shaky."
    "I mentally sigh."
    phone_m "Uh, yes, Melody, I’m fine. Just tired from school. And I’m not sure if that’d be possible. I’ll try and call you back if I can, if it’s doable, alright?"
    phone_mc "Sure... Okay." 
    phone_mc "Be safe, Monika, okay?"
    phone_m "I’ll try! Y- You too!"
    phone end call
    "I patiently listen to her breathing for a moment before she hangs up."
    python hide:
        mc = phone.character.character("mc")
        mc.name = "Melody"
        mc.icon = phone.asset("mc_icon.png")
    _m mc bc ea na "I suppose I better go to the office."
    _m nb ba "... I just called her by her name, didn’t I? Shit."
    _m ec bc "Another mistake to add to the pile."

    scene bg m_office_afternoon with wipeleft

    play sound beep
    "I press the button on the study door to notify him that I’m waiting, and take a seat."
    camera master:
        align (0.0, 1.0) zoom 1.8
    with Dissolve(0.2)
    "I wait here, perched awkwardly on the leather seat while I await my fate."
    "I hold my face in my hands as a thousand thoughts swirl." 
    _m turned suit ec bc mc "Why..?"
    dadm "Did I tell you you may sit, girl?"
    "I both physically and mentally flinch. He almost never calls me 'girl.'"
    _m ea "I wonder what will happen with this exception."
    camera master
    with Dissolve(0.15)
    "I stand shakily and reply."
    m md "No, sir."
    m "Apologies."
    m "I’m sorry."
    dadm "You will be."
    dadm "And what you did is inexcusable."
    dadm "And if I catch you submitting to such {i}beastly{/i} impulses again, well. Perhaps I will also have to act on impulse."
    _m nb "I did no such thing!"
    "That is what I wish I’d say, but instead, I utter nothing. After all..."
    _m ma na"I know better than to answer back."
    m ba md "What impulse, sir?"
    dadm "The impulse to remove that club of yours."
    play sound heartbeat
    show black onlayer above_master with {"above_master": Dissolve(0.3)}:
        alpha 0.75
    "I gasp slightly."
    hide black with {"above_master": Dissolve(4.0)}
    _m mc bb nb "Please..."
    dadm "I’m glad that had the intended effect, girl."
    dadm "Now, I assume you wonder what punishment will befall you?" 
    "I recoil again. Threatening to destroy my only lifeline to sanity wasn’t a punishment?"
    dadm "Well..." 
    dadm "We’re going to let you think about your actions first."
    dadm "So why don’t you arrange to stay at a friend’s? I’m sure that if you decline to, they might {i}find out{/i}."
    dadm "This is a big moment, Monika. Your first sleepover."
    camera master:
        blur 0.0
        ease 10.0 blur 1.5
    dadm "I only hope it isn’t spoiled by thoughts of how we may punish a stupid, insolent girl with no self control, such as yourself, whilst you’re there." 
    dadm "Now go and pack for school. And don’t forget your {i}clothes{/i}."
    dadm "We will see you tomorrow evening. I hope you look forward to it."
    camera master:
        ease 3.0 blur 2.5
    "Tears welling, I nod and turn to leave."
    "As I’m about to exit, he calls me."
    dadm "Girl?"
    camera master:
        ease 0.7 blur 0.0
    m md "Y- Yes, sir?"
    dadm "Aren’t you going to curtsey and thank us for letting you see your friend?"

    stop ambient fadeout 2.0

    phone register "lit_club":
        time hour 18 minute 21
        "m" "Hi everyone, would there be any chance someone has a spare bed I can borrow for the night?"
        "n" "Everything alright?" 
        "m"  "Oh, swimmingly so, I just thought it would be nice to get out of the house for a little while, and it appears my family is doing some renovations."   
        "y" "Unfortunately, I’m not exactly in a position to host right now..."   
        "n" "Sorry, I’ve not got anywhere for you either. Maybe Sayori?" 
        time minute 49
        "s" "Me? What about me?" 
        "s" "Ohhh! Yeah, sure, come on over!"  
        "m" "I appreciate it. I’m on my way now."

    scene bg mc_living_room
    show sayori turned hoodie at i11
    with mc_pov(True)
    $ set_pov("mc")
    $ set_date(hour=19, minute=3)
    play music yofukashinouta

    "As Sayori and I settle down to watch the show we haven’t seen together in forever, I almost jump at a sound I also haven’t heard in perhaps just as long."
    play sound doorbell
    _mc turned tail nostrands casual bb nb mf "Nobody ever rings round here..."
    _mc mh ec ba na "A doorknocker? This late?"
    _mc ea "Regardless, I’d better check who it might be..."
    mc mg "Sorry Sayori, I should go grab that."
    s e3d mb "Sure... I’ll go get some more cookies!"
    show sayori ma at thide
    _mc ec ma "Of course. Any interlude is a Sayori excuse for food."
    hide sayori

    scene bg mc_house_entrance_night with wipeleft

    "I get up slowly and amble to the front door."
    camera master:
        align (0.0, 0.55) zoom 1.5
    with Dissolve(0.2)
    "I see through the frosted glass some brown hair..."
    _mc turned casual tail ec mh "Curiouser and curiouser."
    show monika turned suit ed nb:
        xcenter 0.25 ypos 1.0 yanchor 0.95 zoom 0.7
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("monika")
    "I open the door, and to my surprise, see an equally smiley and sweaty Monika."
    m ea mb na "Hey, MC! How’re you?"
    show monika ma with say_dissolve
    mc ml ea "Good, thanks, are you okay?"
    m md "Y- Yes, fine, why?"
    m rhip mb "Thank you for asking."
    show monika mc with say_dissolve
    mc ec mf "Only because I didn’t know you were planning to come round here... or that you knew where I lived."
    m rdown lpoint md "Sayori told me you lived next to her! And I thought you’d have seen the messages on the group chat..."
    show monika mc with say_dissolve
    mc ea ml thinking "What messages?"
    m ldown mb "Oh, I asked about a sleepover."
    show monika mc with say_dissolve
    mc mg "Without asking the host?"
    "There’s a beat before she answers, where she seems slightly confused, before she continues."
    m rhip mb "No, I’ve actually asked Sayori."
    show monika mc with say_dissolve
    mc ldown ec "And you assumed she was here?"
    show monika ec with say_dissolve
    "She seems to take a moment to gather herself." 
    m rdown ea mb "Well, who {i}wouldn’t{/i} want to be with you on a night like this?"
    show monika ma with None
    show monika at i11 
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "Momentarily stunned by her compliment, I step backward."
    _mc ma "She seems okay, if her explanation is a bit fishy."
    mc mb nb ea "W- Well, come in then, no sense staying out in the cold."
    $ autofocus.unblock("monika")
    m ed mb "Gladly."
    show monika ma at rhide
    hide monika
    "She wears a warm smile as she steps inside."

    scene bg mc_living_room
    show sayori turned hoodie at i22
    show monika turned suit at i21
    with wipeleft

    s mb "Hey! Monika!" 
    show sayori me
    m mb "Hey, Sayori! I thought you’d be here!"
    show sayori e3d ma
    show monika ma
    "Sayori looks puzzled, but smiles wider."
    s mc lup "Well, I’m glad I am!"
    s mb ldown e1a "You can come and watch our show with us!"
    show sayori ma
    m rhip md "Well, I thought we could potentially invite Yuri and Natsuki, too, actually."
    show monika ma
    mc turned tail nostrands casual ml ec "Be my guest, though something gives me the feeling that Natsuki might not like being messaged late at night."
    show sayori e1d b1d 
    show monika mc
    "Sayori takes on a devilish grin."
    m rdown md "What, Sayori?"
    show monika mc
    s e2a mb "Well..."
    s e3d b1a "She didn’t mind it when you did it to us the other day~"
    show sayori ma
    "And with us all looking at her questioning if she’s joking, all my worries disappear."

    $ advance_date(minutes=7)
    phone register "lit_club":
        time hour 19 minute 11
        "s" "Do either of you two feel like joining us? We can have a sleepover!"    
        "y" "Oh? While that does sound wonderful, I do have things to attend to here. Perhaps another time?"  
        "n" "On my way!"    
        "s" "Aww, that’s too bad, Yuri. If you have some time later, you’re free to join though!" 
        "y" "I appreciate your offer, but I’m doubtful I will have enough time to myself by any sort of reasonable hour. Enjoy your night, everyone."  
        "s" "We will! I’ll see you tomorrow at school!" 
        "y" "Indeed, yes, you will."

    scene bg mc_living_room
    show sayori turned hoodie md at i33
    show monika turned suit mc at i32
    show natsuki turned casual b3a md at i31
    with fade
    $ advance_date(minutes=20)

    "As we all settle down around the table- Natsuki, Monika, Sayori and I- I can’t help thinking how good I have it."
    camera master:
        align (1.0, 0.225) zoom 1.5
        ease 5.0 xalign 0.0
    show bg:
        blur 2.0
    with Dissolve(0.2)
    "I look around at my friends."
    "With the exception of Yuri. She couldn’t make it, sadly."
    show natsuki e3c b1a me
    "The girls each look at me, expectantly, before Natsuki finally says something."
    show sayori e1b ma 
    show monika ma
    show bg:
        blur 0.0
    camera master
    with Dissolve(0.2)
    n lhip e1a b3a mh "So... Do you want to play a board game?"
    show natsuki ma
    s mb lup "Ooh, good idea!"
    s e1a "What do you want to play?"
    show sayori ldown ma with None
    show monika eb
    camera master:
        align (0.5, 0.2) zoom 1.5
    show bg:
        blur 2.0
    show natsuki:
        alpha 0.0
    show sayori:
        alpha 0.0
    with Dissolve(0.2)
    "I take a quick look at Monika."
    "Her eyes seem to be flitting all over the place."
    _mc turned casual tail ec mh "Perhaps something simpler might be in order."
    camera master
    show natsuki:
        alpha 1.0
    show sayori:
        alpha 1.0
    show bg:
        blur 0.0
    with Dissolve(0.2)
    mc ea mb "What about connect four?"
    show natsuki ldown
    show sayori e3d
    show monika ed
    "This seems to at least partially resonate with those present, so connect four it is."

    scene bg mc_living_room
    show natsuki turned casual e1d mn at t11
    with fastfade
    $ advance_date(minutes=17)

    "After several rounds, Natsuki takes a seat opposite to me, with a smug grin across her features."
    mc turned tail nostrands casual md ed "Looks like it’s you versus me, Natsuki."
    n mb "Ahah. I’m going to relish this."
    n b3a e1a mh "Here - coin flip to see who goes first. Not that it’ll make much of a difference, but still."
    show natsuki ma
    mc ea mb "We’ll see about that. Alright - I call heads."
    show natsuki md
    "Up it goes, shiny silver end over shiny silver end, into the air."
    "Passing the living room’s overhead lamp by."
    show natsuki ma b1a at hop
    play sound slap
    "Before Natsuki, quick as a cobra, snatches the gleaming disk out of the air and slaps it onto the back of her hand."
    show natsuki e1d b1d
    "She smirks as she reveals the result."
    n mo e3d b3a "Tails never fails."
    "I shrug."
    _mc ec mh "No rule against doing that."
    _mc ef "After all... She couldn’t have possibly timed that strike in order to obtain her desired result."
    _mc ec "Nobody’s hand-eye coordination can be THAT fast."
    _mc ea "... Right?"
    _mc ma "Anyway. Not much point in crying over spilled milk."
    show natsuki e1d b1a ma
    "So she goes first. Big deal. In her own words - it isn’t as though that advantage will make much of a difference."
    _mc ec "I mean - all I have to do is arrange four counters in a straight line."
    show natsuki b3a e1a:
        subpixel True
        ease 0.2 xoffset -200
    $ connect_four.show(xanchor=0.0, xpos=0.55, ypos=0.75, yanchor=1.0)
    _mc ea ma "How difficult can it be?"
    show natsuki e3c
    $ connect_four.place(4)
    "Taking our places on either side of the grid, Natsuki opens the dance with a yellow counter right in the bottom of the centre column."
    
    # python hide in connect_four:
    #     while True:
    #         if not _player:
    #             interact()
    #         else:
    #             ai_place()
            
    #         result = board.get_status()
    #         if result is None:
    #             continue
    #         else:
    #             hide()
    #             if result == State.WIN:
    #                 renpy.call("connect_four_win")
    #             elif result == State.LOSS:
    #                 renpy.call("connect_four_loss")
    #             else:
    #                 renpy.call("connect_four_draw")
    #             break
    
    $ connect_four.place(4)
    show natsuki e1a me
    "On top of which I immediately place a red."
    n lhip rhip b1d e1d mb "Oh, trying to assert dominance now, are we?"
    show natsuki ma
    mc ed md "Well. Can’t let you top all the time, now, can I?"
    n rdown e2a b3a mh "Fair is fair."
    show natsuki ldown b1a e1a ma
    $ connect_four.place(5)
    "In goes another yellow counter, this time to the right of the first."
    n mc "Never let it be said that I’m inflexible."
    show natsuki ma
    _mc ea mh "That came as a surprise."
    _mc "I expected her to immediately reassert herself by sandwiching my counter between two of hers."
    n cross casual b1d mc "Feel like building on your advantage? Seeing just how high you can stack this?"
    show natsuki b1a ma
    _mc ec ma "The temptation is too great."
    mc ea mb "Sky’s the limit."
    show natsuki b3a me
    $ connect_four.place(4)
    "In goes my next counter, on top of my first."
    $ connect_four.place(3)
    show natsuki turned casual b1d ma
    "To which Natsuki responds by placing her third counter to the left of her first."
    n mh b3a "Gotta be careful, erecting a structure on top of such an iffy foundation."
    n cross casual e3c mi "One that’s built by somebody else, at that."
    n e2a mh "They might just be able to, you know... pull the rug out from under."
    show natsuki ma
    mc ed md "Nice try, but even a five year old can see that three-in-a-row you’ve just set up."
    $ connect_four.place(2)
    show natsuki b1d
    "Which I promptly block with my third counter, placed to the left of hers."
    mc bd "Denied."
    show natsuki turned casual mn e1d
    "Natsuki’s smirk turns into a broad, sly grin."
    n e3c b3a mi "How many five year olds could have seen THIS coming, I wonder?"
    show natsuki e1d b1d ma
    "Only too late do I see what she’s done."
    mc mf nb ba "No friggin’ way."
    n e1a b3a mc "Speaking of childhood. I think there’s a suitable nursery rhyme for the occasion."
    n e3c mh "Ashes, ashes..." 
    n e1a b1a mb "We all fall..."
    show natsuki ma
    $ connect_four.place(6)
    "Fourth yellow counter to the right of her second."
    n e1d b1d mb "Down."
    show natsuki ma
    mc mm bi eg "I don’t believe it."
    n b3a e3d mo "Seven moves."
    show natsuki e1a mc:
        subpixel True
        ease 0.3 xoffset 0
    $ connect_four.hide()
    n e1a mc "Read ’em and weep ’em."
    show natsuki ma at t31
    show monika turned suit md at t32
    show sayori turned hoodie at t33
    m "How are you two getting along?"
    show monika ma rhip
    "I’m stunned, but not so stunned that I can’t move to block Monika and Sayori’s view of the grid and its humiliating contents."
    show monika mc rdown 
    show sayori me
    n lhip mc "What do you think?"
    show natsuki e3d mo 
    show sayori e1b md
    "They gasp."
    hide sayori
    hide monika
    hide natsuki
    camera master:
        align (0.1, 1.0) zoom 2.3
    with Dissolve(0.2)
    "I bite my lip, eyes downcast." 
    _mc ef mh "Concealing the evidence of my defeat isn’t really going to work now, is it?"
    _mc "I’ve got loss written all over my face and body language."
    "Which the others are reading as readily as anything they bring to our club sessions."
    show monika turned suit mc at i21
    show sayori turned hoodie e1b lup rup mk at i22
    camera master
    with Dissolve(0.2)
    s ml "Holy cow, seriously? That didn’t even take a minute!"
    show sayori mk
    m md "Natsuki, how did you manage that?"
    show sayori e1a ldown rdown me at thide
    show monika at thide
    "I hear a clack-clack noise from behind me and turn around to yet another surprise." 
    hide monika
    hide sayori
    show natsuki turned casual e2a md b3a at t11
    "Natsuki has tipped all the pieces out of the grid and is tidying them up."
    "Denying the others the chance to see exactly what took place."
    show natsuki mh at t31
    show monika turned suit mc at t32
    show sayori turned hoodie md at t33
    n "You’ll find out when you play me, but not before."
    n e1a b1d mb "A magician never reveals her secrets."
    show natsuki ma b3a at t11
    show monika md at thide
    show sayori b4 me at thide
    hide sayori
    hide monika
    "As the others return to their game, all agog and whispering amongst themselves, I sheepishly turn to Natsuki."
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    show natsuki me
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    mc ea bg mb "Hey. Thanks for helping me save some face back there."
    show natsuki ma b1a e3a with say_dissolve
    "She gives me a conspiratorial wink in response."
    n lhip e2a b3a mh "Like I mentioned earlier. Never let it be said that I’m not inflexible."
    show natsuki ma with None
    hide natsuki
    camera master
    show bg:
        blur 0.0
    show sayori turned hoodie lup mn at i22
    show monika turned suit at i21 
    with Dissolve(0.2)
    $ autofocus.unblock("natsuki")
    $ say_transition = False
    "Sayori grabs the set and turns to Monika, an excited grin on her face."
    show monika mc
    s b1d e1d mb "Want to play, Monika?"
    show sayori ma
    m md "Oh, er, sure, Sayori!"
    show monika ma 
    show sayori b1a e3d
    "I stand and let Monika take my chair."
    show monika at dip
    show sayori e1a ldown at dip 
    "She sits and Sayori takes the seat across from her."
    s e3d mb "Yay~ Want to go first, then?"
    show sayori ma
    m md "Yeah, okay."
    show monika ma
    show sayori e1a
    "She slides the disc into the penultimate column."
    show sayori b1d e3c
    "Sayori smiles and proudly plunks her disc in the centre..."
    stop music fadeout 2.0

    scene black with Dissolve(1.5)
    scene black
    show bg m_house_night_mbo_on
    with monika_pov(True)
    $ set_pov("m")
    $ set_date(hour=21, minute=22)
    play ambient ext_night fadein 1.0

    "As my feet patter against the cold concrete of the sidewalk, I feel my dread begin to increase a thousandfold."
    _m turned suit bb nb mc "W- What am I going home to find?"
    _m eb bc na ma "If I still have a home..."
    _m bc ea mc "They sent me away for the night, only to backpedal and recall me a couple hours later."
    _m ec "I cannot overstate how cruel and unusual it must have been for my club members to have prepared for my stay, on my own request, only for me to leave early."
    _m ba ea "What have they planned, and how did they arrange it so quickly?"
    "Every step makes my mind wander viciously."
    "Until..."
    hide black
    call close_eyes(0.0) from _call_close_eyes_6
    call open_eyes(1.0) from _call_open_eyes_5
    "I see our house come into view, the only room illuminated being the office and... my bedroom?"
    _m bb md nb "Why?"
    "My stomach sinks lower than I thought possible."
    play sound beep
    "I walk up to the imposing gates and press the intercom."
    "Then whisper slowly:"
    m bc ec na md "Monika Rein, requesting entrance."
    "The intercom beeps and the gates open."
    camera master:
        align (0.45, 0.8) zoom 3.0
    with Dissolve(0.2)
    "I walk through, hastily trying to make myself seem presentable."
    "I stand by the door, mentally bracing myself as I knock."
    "Father opens the doors with a cold smile."
    dadm "Hello, {i}Monika{/i}."
    dadm "Glad to see you home... so late."
    m ba ea "My apologies, sir, I-"
    dadm "I suppose that in the grand scheme of things.. It’s forgivable."
    dadm "Why don’t you go and get dressed for dinner?"
    "I nod and feel anxiousness rise in my chest."

    stop ambient fadeout 2.0
    scene bg m_house_stairs_night_on
    camera master
    with wipeleft
    pause 0.05
    camera master:
        align (0.65, 0.4) zoom 2.0
    with Dissolve(0.2)

    "As I ascend the stairs I contemplate what’s happened."
    _m turned suit mc "They wouldn’t have forgotten..."
    _m bc "Surely..."

    scene black
    camera master
    with wipeleft

    "It’s at this moment that I arrive at my room."
    "I gently open the door."

    scene bg m_bedroom_closed with Dissolve(0.5)
    play music wtdgi

    "And let out a silent sob as my world comes raining... pink."
    camera master:
        align (1.0, 0.3) zoom 1.8
    with Dissolve(0.2)
    _m turned suit nb md bb "E- Everything..."
    "He heard me say how much I hate pink."
    camera master:
        align (0.3, 0.7) zoom 2.3
    with Dissolve(0.2)
    _m bc ea na mc "And everything in here is the exact shade I hate-"
    _m ba "They..."
    camera master
    with Dissolve(0.2)
    _m bb "Everything, this time, is pink."
    _m eb "Not just most of the decor."
    _m "A million reminders of my place."
    camera master:
        align (0.55, 1.0) zoom 1.5
    with Dissolve(0.2)
    "I step inside and close the door."
    "I have a dreadful feeling."
    _m ea "My clothes. They’re all going to be..."
    _m ec "Pink."
    call close_eyes(1.0, wait=True) from _call_close_eyes_7
    "I slump onto my bed. Defeated and exhausted."
    "I would curl into a foetal position, but that would only attract more punishment."
    camera master
    "Instead, I stand, undress, and promptly slip into a dinner outfit."
    _m dress ma bc "Hell hath no fury like a prison of pink."
    "I draw upon every ounce of strength I have left to prepare myself for dinner as the pit in my stomach only grows ever deeper."

    $ add_calendar_description(calendar_descriptions["monika"][1])

    call week_1_friday_monika from _call_week_1_friday_monika
    return