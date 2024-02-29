label week_2_friday_natsuki:
    call calendar_transition(day=3, hour=7, minute=3) from _call_calendar_transition_22
    scene black
    show bg am_bedroom_day_open:
        align (0.9, 0.6) zoom 1.8 blur 2.0
    show amelia turned ec mb hairdown:
        xalign 0.5 ypos 1.0 yanchor 0.55 zoom 1.8
    with Dissolve(1.5)
    $ autofocus.block("amelia")
    $ say_transition = True
    play ambient int_day fadein 7.0

    _mc turned casual messy nostrands nohairclip mj eg bi "Oh, my back..."
    _mc ec mh "What is happening? I never sleep so poorly..."
    _mc ea mf ba "Huh?"
    _mc ec mh "This isn’t my room-"
    _mc ea "... Ah."
    _mc eg ma "That’s right, I slept with Amelia last night."
    _mc eb bf nb "Wait- I, ah, slept in her bed?"
    _mc ec bg "No, that’s not it- I mean, it is, I did, but she wasn’t- We didn’t-"
    stop ambient
    hide black
    am "Finally awake, are we?"
    show amelia ma with say_dissolve
    "And there she is, uncomfortably close to my face."

    play music daijoubu

    mc mj bi eg "Geez, Meelz, I just woke up..."
    am mb "And now, you’re gonna come down for breakfast."
    am eb me "Don’t wanna be late for school now, do we?"
    am ea mb "C’mon, your uniform’s dry and ready to wear."
    am ee lup me "And yes, I know what you’re thinking: I {i}would{/i} be the perfect wife."
    show amelia ma with None
    hide amelia
    show bg:
        zoom 1.0 blur 0.0
    with Dissolve(0.2)
    $ autofocus.unblock("amelia")
    $ say_transition = False
    "I roll my eyes as she leaves the room, with my uniform hanging on the door-handle."
    _mc ec ma ba na "I swear, she’s changed so much since I first met her."
    _mc ea "Seriously, she was so quiet and jumpy."
    _mc ec "I’m glad to see she’s tempered out since then."
    _mc eg "... Best to get ready for school."

    scene bg class_1_day with wipeleft_scene
    $ set_date(hour=10, minute=8)
    $ set_internet(False)

    "As I sit at my desk, I wonder what it is that Sayori was so interested in telling me yesterday."
    _mc turned tail nostrands mh thinking "Her message sounded important. Is it to do with the sleepover tomorrow?"
    _mc ec "I wonder why she didn’t just tell me what it was."
    _mc ea bf "... Maybe she’s upset because I skipped out on the club and didn’t walk home with her?"
    _mc ldown eg bi "Nah, that’s not quite like her."
    _mc ec "She’s be disappointed, but not upset with me."
    _mc ea ma ba "I swear, that girl has an endless fuse."
    _mc eg "I guess I’ll have to wait until lunch to find out, won’t I?"
    _mc ea bb "Oh, I know! I could text Natsuki. She’ll definitely know what’s up."
    phone discussion "mc_n":
        time auto True
        "mc" "Hey, Natsuki, what’d I miss yesterday? I think Sayori wanted to talk to me about it."
    _mc ec ba "There we go. Now to wait for a response."
    "..."
    _mc bi mh "Respond faster, dammit."
    "..."
    phone discussion:
        type "n" value 1.5 delay 0.1
    _mc eb ma ba "Aha!"
    phone discussion:
        "n" "Hm? Oh, yesterday Monika announced that we’d be participating in the Culture Festival on Monday."
        "n" "We had a discussion about it afterward, and decided that while we weren’t keen on the idea, it’d be nice to support something Monika’s passionate about."
        "n" "She was probably just checking to see if you’re okay with it too."
        "mc" "Oh, sure, I can do that."
        "mc" "I wonder why she left it this long to mention something like that though; haven’t most clubs been planning for this for months?"
        "n" "It was really short notice, yeah, but we’re not planning anything major. Just gonna chill in the clubroom and do some poetry readings. I’m gonna make some cupcakes and we’re gonna decorate the room a little."
        "mc" "That sounds like fun. Is that what we’re doing in club time today?"
        "n" "Sure is! So, we’ll see you there this time?"
    _mc ec mh "I knew she’d be upset. She’s not as forgiving as Sayori, from what I’ve seen."
    phone discussion:
        "mc" "Yeah, I’ll be there. Still F4, right?"
        "n" "Ha ha. Just for that, you’d better walk Sayori home, you hear me?"
        "mc" "What, for my bad joke?"
        "n" "... Yes."
        "n" "Among other things."
        "mc" "Alright, alright. I was gonna have lunch with her today, anyway."
        "n" "Oh, you were?"
        "n" "Right, I see."
        "mc" "What’s up?"
        "n" "No, it’s nothing."
        "n" "She just didn’t say she had plans, is all."
        "n" "Not that she’s not allowed to have plans, I was just..."
        "mc" "Ah, I see."
        "mc" "No, we hadn’t organised anything, I was just going to ask her."
        "mc" "But I’ve got a better idea, now."
        "mc" "Meet me by the lockers."
        "n" "When?"
        "mc" "Start of lunch, duh."
        "n" "Oh, right."
        "n" "Should I be concerned?"
        "mc" "Only if you like the taste of your internal organs."
    "..."
    phone discussion:
        "mc" "Sorry, stupid inside joke."
        "mc" "Ask Sayori about it, sometime."
        "n" "I’m afraid to ask."
        "n" "When were you eating yourself?"
        "mc" "No no, I was eating Sayori."
        "mc" "Wait, that came out wrong"
        "n" "No no, that came out exactly how I expected it to."
        "n" "See you at lunch."
    phone end discussion
    "I shake my head."
    _mc ea mh "She’s gotten a whole lot wiser to my type of sass lately."
    _mc ef bi "... Either she’s a quick learner, or someone’s been giving her pointers."

    scene bg school_lockers_day with fade
    $ set_date(hour=12, minute=15)

    _mc turned tail nostrands ec mh "... She’s late."
    "..."
    show natsuki turned xd mk nb b2a at t11
    n "Sorry, had to run an errand for the teacher!"
    mc ea ml "Student Council duties?"
    n e1a b3a mh na "Yeah. Also... I won’t be able to hang around for long; I’ve got a meeting in about 10 minutes."
    show natsuki mj
    mc ef mg "Ah, that’s a shame."
    n b4 mh "Why?"
    show natsuki md
    mc ed md "I was gonna force you to come with me when we hang out with Sayori~"
    n e1d b1d lhip rhip mi "Huh? Why would I-"
    show natsuki e1a b1a md
    show natsuki ldown
    mc eg mb "Don’t you play dumb."
    show natsuki rdown me e1b
    mc ea ml "I know."
    n mg "Kn- Know?"
    n e1a mh b1d "What do you know?"
    show natsuki me e1a
    "I throw her a knowing wink."
    mc ed md "More than you realise."
    n cross b1a e2a mg "I, ah, have no idea-"
    n turned b3a e1b mh "Wait!"
    n mi b1d e1a "I’m supposed to be upset with you!"
    n b3a mc "I just remembered!"
    show natsuki rhip lhip mj e1d b1d
    mc bd ea mg "Huh? Where did that come from?"
    n mh "You! You went out yesterday without inviting Sayori!"
    show natsuki mj
    mc bg ml nb "Y- Yeah?"
    n cross e1a mi "After you promised to spend more time with her!"
    show natsuki mj
    mc thinking ba mg ea na "... Did I make that promise?"
    n b1d e1b mi "You said that you felt bad that she was left out, because you’ve been spending so much time with Amelia this week!"
    show natsuki mj
    mc ldown ef ml "Well, yeah, I felt bad, but-"
    n e1a b1a mh "So you’re not sorry?"
    show natsuki mj
    mc ea mg "No, I’m sorry, I just-"
    n e3c b3a mh "Typical! Making excuses!"
    show natsuki b3d mj
    mc ec ml bi "No, it was-"
    n turned e1b mi b1d "Ridiculous! Imagine blowing off Sayori!"
    n b3d e2a nb mh "... B- Blowing-"
    show natsuki e1b b3a mj nd
    mc ed md bm "Uh-huh. Choose your words a little more carefully, eh?"
    mc ea mb ba "C’mon, let’s get you to your meeting then."
    n mi b1d "B- But I-"
    show natsuki nc mm
    mc eh "Fantasise later!"
    show natsuki mi b3a at thide
    hide natsuki
    "I start walking down the hallway, toward the student council room, dragging a half-dazed Natsuki behind me."

    stop music fadeout 2.0
    scene bg school_rooftop_day
    show sayori turned at i11
    with Fade(0.7, 0.3, 0.7)
    $ set_date(minute=48)
    play music a_sunshine

    s mb "So, what brings you up here?"
    show sayori ma
    mc turned tail nostrands ml "A couple things."
    s mh lup b4 "... Such as?"
    show sayori me b1a
    mc ef mg "Well, I wanted to hang out with you, for one."
    mc ea mb "Got time to hang?"
    s rup e3d mb "Silly, I’ll always make time to hang with you."
    s ldown rdown mb e1a "So, what’s up?"
    show sayori ma
    mc ml "Well, I was talking to Nat earlier, and she... Actually, on second thought?"
    show sayori md
    mc eg mb "Nevermind. It’s not important."
    _mc ec mh "... If my hunch is correct, it would be cruel to oust her."
    _mc ea "Best to leave her be."
    s b4 mh lup "... Okay?"
    show sayori md b1a ldown
    mc mg "Honestly, I just wanted an excuse to spend some time with you."
    mc ef bg mb "I feel like I haven’t had enough time to do that, even since we’ve been reunited."
    show sayori e2a ma nd
    "She looks away, but this time without a cloudy expression."
    "Instead, I see a faint blush form across her features."
    mc ed md ba "So, I wanted to take some time to give some attention to my best friend."
    s mh e1a nb "... I thought Amelia was your best friend."
    show sayori na md
    mc eg mb "I think I’ve room enough for two in this black heart of mine."
    s lup mn e1d b1d "Pff~ So edgy~"
    show sayori ma
    mc ed md "Careful, though, you might... cut yourself on all this edge."
    s mb "Ooooo~ Scary~"
    show sayori b1a e3d ma rup
    camera master:
        align (0.5, 0.3) blur 0.0 zoom 1.0
        ease_quart 0.3 blur 10.0 zoom 1.7
        0.1
        blur 0.0 yalign 0.2 zoom 2.5
    show sky_day at moving_sky zorder 1 as stuff:
        alpha 0.0
        0.4
        alpha 1.0
    show black:
        alpha 0.0
        ease 0.3 alpha 1.0
        0.2
        ease 1.0 alpha 0.0
    play sound ["<silence 0.3>", audio.fall]
    "She leans over and pushes me to the ground."
    $ autofocus.block("sayori")
    $ say_transition = True
    s e1d b1d mb ldown rdown "Close enough to be cut yet?"
    show sayori ma with say_dissolve
    "Her face is... obscenely close to mine."
    _mc ec ma "But for the first time? I’m not flustered. Not like I used to be."
    mc ea mb "Not you. For you, I’ll hide those edges, only ever exposing you to the flat of the blade."
    show sayori lup rup b1a e3d with say_dissolve
    "She smiles, wrapping her arms around me."
    s b2c mb e3c nb "God, I missed you, Bard."
    show sayori ma e1a na with say_dissolve
    mc eg mb bg "And I don’t know what I’d do without my Mage."
    show sayori b1a e3d ldown rdown with say_dissolve
    "I return in kind, and the two of us simply remain still for a little while."
    s b2a mb e3c nd "Thanks... for not changing so much on me."
    show sayori ma with say_dissolve
    mc ea mg ba "You make me who I am, you know? And you know..."
    mc ed md "You are what you eat~"
    s b1a nb e3d mc rup "No, no no!~"
    show sayori mo with say_dissolve
    "I bite down gently on the nape of her neck, growling like a cat."
    s mc "Don’t eat meee~"
    rooftop_teacher "Ahem."
    show sayori e1b b1a mj rdown nc with say_dissolve
    "Both of us freeze, looking up."
    rooftop_teacher "I’m afraid to ask, but..."
    rooftop_teacher "Whatever you’re doing seems highly inappropriate."
    hide stuff
    camera master
    show sayori:
        xcenter 0.67 yanchor 0.45 zoom 2.5 blur 3.0
    show bg:
        align (0.5, 0.6) zoom 1.8 blur 0.0
    show rooftop_teacher_silhouette:
        xcenter 0.22 yalign 1.0 zoom 0.65
    with Dissolve(0.2)
    "A teacher has walked out onto the rooftop, probably simply on their travel path."
    show sayori e1a with say_dissolve
    mc bg nb ml ea "N- No, actually, it-"
    rooftop_teacher "And I’d rather not hear any details. Both of you to the vice-principal’s office."
    show sayori mh b2a:
        blur 0.0
    show bg:
        blur 2.0
    show rooftop_teacher_silhouette:
        blur 2.0
    with say_dissolve
    s "E- Eh? But we-"
    show sayori md b1a:
        blur 3.0
    show bg:
        blur 0.0
    show rooftop_teacher_silhouette:
        blur 0.0
    with say_dissolve
    rooftop_teacher "Immediately."

    scene bg school_corridor_3_day:
        blur 2.0
    show sayori turned e2a at i11
    camera master:
        align (0.5, 0.2) zoom 1.5
    with wipeleft
    $ advance_date(minutes=5)

    mc turned tail nostrands teehee nb eh bg "Sorry..."
    "As we walk in near silence to the office, I almost whisper an apology."
    s mb e3c "No, it was my fault. I definitely started it."
    s e1a mh "I guess what seems to us like innocent fun is..."
    show sayori e2a ma with say_dissolve
    mc ef mb nc "Less so, at our age, yeah."
    show sayori nd with say_dissolve
    "We both blush. Neither of us had even considered the connotations before the teacher pointed us out."
    s nb lup e1a b2c mb "Still... We should probably have known better."
    show sayori ma with say_dissolve
    mc ea mb nb ba "Nah. Imagine how good of a story it’ll make!"
    s e1d na b1d mh "What, us getting suspended right before the Culture Festival because we were being 'inappropriate'? Yeah, cool story."
    show sayori mj ldown with say_dissolve
    mc na eh md "No, you gotta think of the comedic factor! Us getting suspended because we were re-enacting a childhood joke!"
    s e2a mh b1b "... Still, I’d rather not be suspended at all."
    show sayori mj with say_dissolve
    mc ef ml ba "No, not with Monika’s plan for the Festival. That would suck."
    s lup b1a mh e1a "Oh, you know about that?"
    show sayori ma with say_dissolve
    mc ea mg "Yeah, Nat told me."
    s ldown mb "Oh, good. So what was your take?"
    show sayori ma with say_dissolve
    mc mb "I’m definitely down to mess around and have a little fun as a club. No complaints here."
    s e3d mc "Cool!"
    s e1a mb "I’ll tell Monika we’re all in."
    s e1d lup b1d mh "... If we don’t {i}actually{/i} get suspended, that is."
    show sayori b1a e1a ma with say_dissolve
    mc eg mb "Nah, it’ll be fine. Just trust me."
    show sayori md with say_dissolve
    mc ed md "Besides, we’ve got a member of the student council to back us up."
    s mh b4 "You mean Natsuki? You don’t think she’d rat us out for the fun of it?"
    show sayori md with say_dissolve
    mc ea mf "Now that you mention it..."
    show sayori e3d b1a ma with say_dissolve
    mc eg mb "Yeah, let’s not lean on Natsuki for help."

    scene bg school_corridor_3_day:
        blur 2.0
    show sayori turned md at i11
    with fade
    $ advance_date(minutes=11)

    mc turned tail nostrands eh md "See? I told you she’d go easy on us!"
    mc ea mb "She let us off with a warning!"
    s e1d b1d mh "Only because you {i}insisted{/i} on being as insufferable as possible. She probably would have just let us go entirely if you weren’t so..."
    s e1a b1a mb "You."
    show sayori ma with say_dissolve
    mc ed md "But hey, that’s what makes me fun, right?"
    show sayori mb e3c b1d with say_dissolve
    "She chuckles, shaking her head."
    s mc e1a b1a lup "True. And neither of us would have been here if it hadn’t been for both of us making that silly mistake."
    show sayori md with say_dissolve
    mc ea mb "We’re just lucky the teacher caught us, and not Natsuki."
    s mh "Huh? Why would she-"
    stop music fadeout 3.0
    show sayori e1b nb me with say_dissolve
    "She bites her lip."
    s ldown b2b mh e2a "Oh, you know."
    show sayori ma b2a with say_dissolve
    mc ea ml "... I mean, I had a strong suspicion."

    play music myconfession

    s e1a nc mb b2c "Don’t... Don’t tell anyone, okay?"
    s mh lup b2b "Least of all her."
    s ldown b2a e2a mh "If she knew that I knew, it’d... break her heart."
    show sayori mj with say_dissolve
    mc ec "... What are you planning on doing about it?"
    s mg na "I... I don’t know yet."
    s e1a mh b2c "I don’t think I feel the same way she does."
    s mb "But I’m gonna wait until after school, before doing anything. I won’t do anything to cause her grades to suffer at the last minute."
    show sayori ma with say_dissolve
    mc thinking mg ea "So you don’t like her?"
    s mb e2a b2a nb "... I don’t know."
    s b2c e1a lup mh "I do, I really do, but-"
    show sayori mj na with say_dissolve
    mc ef ldown "You aren’t sure if you like her to the same extent she likes you."
    s ldown b1a mh e2a "... Yeah."
    s e1a b2c mb "I’m her best friend, you know?"
    s e2a b2a mh "And... I just keep wondering if something’s wrong with me."
    s mb nb "That’s two for two, you know?"
    s e2c mh b2c "Maybe I’m just terrible at being a good friend."
    show sayori mj e1a with say_dissolve
    mc ea "You’re worried about the fact that both of your best friends that you’ve ever had have fallen in love with you?"
    s mg na "... Yeah."
    s mh b1a lup "Like... What do I even do?"
    show sayori md ldown with say_dissolve
    mc eg "Well, I think it’s time you consider what she means to you. If you do indeed like her, act upon it."
    s mh "But-"
    show sayori b2a mj with say_dissolve
    mc ec ml "No buts. Just... consider it."
    mc ea mb "The sleepover is tomorrow, right?"
    show sayori nb with say_dissolve
    mc mg "Maybe you should take some time to talk with her then."
    mc ml "And, personally?"
    show sayori e1a tears_a ma na with say_dissolve
    "Sayori looks up at me, a little wetness stirring in her eyes."
    mc ed md "I don’t think you’re a bad friend. In fact, I’d take it as a compliment that you’ve done so well."
    mc ea mg "After all, both of them have decided that you, and you alone, were worth their attention."
    mc eg mb "You’re special, Sayori. I’ve never known anyone quite like you."
    show sayori e1a notears with say_dissolve
    mc ef mb nc "And honestly? I’m glad you were the first person I fell for."
    s mh b1a "... First?"
    show sayori md with say_dissolve
    mc ea ml nb "... Well, at this stage, only, but-"
    show sayori e3d lup rup mc with say_dissolve
    s "Hah! I knew it!"
    show sayori mo with say_dissolve
    "She grins from ear to ear."
    s ldown rdown e1a mb "I’m still number one!"
    show sayori ma with say_dissolve
    "I shake my head, ruffling her hair."
    mc ed md "You’ve always been number one, silly."
    show sayori e3d with say_dissolve
    mc eg mb "That’s what makes you my best friend."

    stop music fadeout 2.0
    scene bg club_day
    camera master
    with longfade
    $ autofocus.unblock("sayori")
    $ say_transition = False
    $ set_date(hour=15, minute=17)
    play music ohayou

    "As I walk into the clubroom, I see everyone already gathered."
    show monika turned mb at t11
    m "Oh, MC! It’s been a while!"
    show monika ma at t21
    show natsuki turned lhip rhip e1d b1d mh at t22
    n "She missed one day, Monika."
    show natsuki md
    show monika ed
    "Monika throws me a warm smile."
    show natsuki e2a b1a mj ldown rdown
    m mb "And it felt much longer."
    show monika ea ma at t42
    show natsuki at t43
    show sayori turned at t41
    show yuri turned at t44
    mc turned tail nostrands mb "Hey, guys. How’s the day been?"
    show natsuki e1a b3a ma
    s mb "We’ve been working on preparing for the festival!"
    show sayori e3d ma
    mc mg "I can see that, yeah. It’s looking great!"
    m lpoint eb mb "I know it was short notice, but I appreciate all of you being on board."
    show monika ma ea ldown
    show sayori at thide
    show natsuki at thide
    show yuri at thide
    mc mb "Of course, why wouldn’t we?"
    hide sayori
    hide natsuki
    hide yuri
    show monika ec at t11
    "I move over and help her lift a string of lights over the curtain rings."
    m md eb "Well..."
    show monika mc
    "She shrugs."
    show yuri turned e2a b1c mh lup at t44
    show natsuki turned b3a at t42
    show sayori turned at t41
    show monika turned ea at t43
    y "Our personal opinions should be laid aside, for now. We’ve got work to do."
    show yuri md
    show monika ma
    s lup rup mc e3d "If we put our heads together, there’s nothing we can’t do!"
    show sayori ma
    show yuri e1a b1a ma
    mc ed md "It’s true. This is our last Culture Festival; why not go out with a bang?"
    show monika ec
    "Monika smiles at us."
    show sayori ldown rdown e1a
    m ea mb "Thank you, all of you. I couldn’t ask for better club members."
    show monika ea ma
    n cross e3d b3a mo "You’re darn right, you couldn’t."
    show sayori e3d
    show natsuki ma
    show natsuki:
        subpixel True
        pause 0.2
        "natsuki cross mm e2a b3d nb"
    show monika ec:
        subpixel True
        easein 0.15 xoffset -50
    "Monika ruffles Natsuki’s hair, causing her to growl cutely."
    n nd e2a b1d mh "N- No, that’s not-"
    show natsuki md
    m ea mb "I’m proud of all of you."
    show monika ec ma
    show natsuki turned e3d b3a mj na
    "She keeps ruffling Natsuki’s hair, who I swear is about to start purring any second."
    s mb lup "Me too! Just think, in only six months we’ve gone from two members to five!"
    s mc rup e3d "And, even better, we’re about to make our debut at the Culture Festival!"
    s ldown rdown e1a mb "I think that’s the perfect time for a celebration."
    show sayori ma e3d
    mc ea mg "Is that why you’re so set on your sleepover tomorrow?"
    s mc lup "Sure is!"
    show sayori e3d mo ldown
    "She’s grinning from ear to ear."
    s e1a mb "It’ll be a great time!"
    show sayori ma
    y e1d mb "Yes, I believe it will. I’m looking forward to it."
    show yuri ma
    m mb "As am I. It’ll be an excellent bonding experience before our chance to expand."
    show monika ea ma:
        subpixel True
        easein 0.15 xoffset 0.0
    show natsuki cross e2a b1d mj
    "We all smile, as Monika finally releases Natsuki from her iron grip."
    show sayori me
    show monika mc
    n mh "Maybe I’ll skip-"
    show natsuki md
    s lup rup b1d mh "Don’t even joke about it."
    show monika ma
    show sayori rdown b1a ma
    n turned lhip rhip b3a mo e3d "Okay, okay! You know I’ll be there, geez~"
    show natsuki ma
    show yuri e1a at thide
    s e3d ldown mb "Hehe~"
    show natsuki e1a ldown rdown at thide
    show sayori ma at thide
    m lpoint mb "Now come on, everyone. We’ve got more decorations to put up!"
    show monika ldown ma at thide
    hide sayori
    hide natsuki
    hide monika
    hide yuri
    "We break, all moving to our assigned posts."
    show black with NonBlockingDissolve(0.2):
        alpha 0.5
    _mc ec ma "Excited wouldn’t even begin to cover it."
    _mc ea mh "Sure, there’s apprehension, as most of us aren’t... what you would call 'people' people, but that doesn’t change the fact that there’s a little excitement hidden here."
    _mc ec bi "Maybe we aren’t super excited at the prospect of growing the club, not to the extent Monika is, but at the same time, this is a chance to prove ourselves."
    _mc ef ba "Even if it’ll only be on a small scale, doing something for the Culture Festival is a rite of passage. An act of legitimacy."
    _mc ea "And that’s what Monika is aiming for."
    _mc ec ma "I think all of us understand that well."
    _mc ea "So, all we can do is help her to bring that vision to life."
    
    stop music fadeout 1.5
    scene bg club_afternoon with wipeleft_scene
    $ set_date(hour=17, minute=20)
    play music okev_m

    m turned mb "Alright, everyone!"
    show yuri turned:
        matrixcolor TintMatrix("#f1d6bb")
        t41
    show sayori turned:
        matrixcolor TintMatrix("#f1d6bb")
        t42
    show monika ma:
        matrixcolor TintMatrix("#f1d6bb")
        t43
    show natsuki turned b3a:
        matrixcolor TintMatrix("#f1d6bb")
        t44
    "She calls us over to the front of the room as we finish most of our tasks."
    show natsuki me
    m lpoint mb "Everything else I’ll get finished on Sunday. There’s not much left, and I can’t really ask you to pick up all that slack."
    show monika mc
    n mh "Hey, if you want a hand, we’d be-"
    show natsuki e1a md
    show sayori md
    m md ldown ec "No, it’s quite alright. I’m burdening you all with this, I’d best be the one to carry it."
    show monika ea mc
    s lup mh "What she’s saying, Monika, is that it’s a team effort. We’ll carry as much weight as you’ll let us."
    show sayori md
    show monika ec ma
    "Monika considers this for a moment, before smiling at us."
    m mb bb "Just knowing that you all care about this so much means more to me than you could imagine."
    m ea md rhip ba "If I need any help, I’ll be sure to call you, alright?"
    m ea rdown mb "But before that, we’ve got a sleepover!"
    show monika ma
    show natsuki ma
    show sayori ldown e1b mg
    "A smile washes over all of us, as Sayori beams with excitement."
    s lup rup mc e3d "I can’t wait! I’ve got so many things planned!"
    show sayori ma
    mc turned tail nostrands ed md "I’ll bet. You haven’t even let me in on any of the 'secret activities'."
    mc ea mg "What about you, Natsuki?"
    show sayori ldown rdown e1a
    n e1d b1d mb "You think she’d tell me? No, half her fun is keeping me in the dark and springing it on me last!"
    show natsuki ma
    s mb e3d "Ehe~"
    show natsuki e1a b1a at thide
    s lup e1a mc "So I’ll see you all tomorrow?"
    show sayori ma at thide
    mc mb "Sounds good to me!"
    y mb "I’ll be there with bells and whistles."
    show yuri ma at thide
    m ed mb "Wouldn’t miss it for the world!"
    show monika ma ea at thide
    hide natsuki
    hide sayori
    hide yuri
    hide monika
    "And with that, we all make our way out of the clubroom, with Monika locking the door behind us."

    scene bg school_corridor_1_afternoon with wipeleft

    show monika turned md:
        matrixcolor TintMatrix("#f1d6bb")
        t44
    m mb "Natsuki, would you mind taking the key back to the office?"
    show monika ma
    show natsuki turned b3a mh :
        matrixcolor TintMatrix("#f1d6bb")
        t41
    n "Oh, sure. We stayed late, so there probably won’t be any teachers there, right?"
    show natsuki ma
    m md "Indeed. You have permission to enter the office without a teacher present, so..."
    show monika ma
    n e2a mg "Yeah, I gotcha."
    n b1a e1a mc "I’ll catch you all tomorrow, alright?"
    show natsuki e2a mj
    show monika ed at thide
    hide monika
    mc turned tail nostrands ml "Oh, actually, Nat."
    show natsuki me b3a at t11
    n "Hm?"
    show natsuki md
    mc mb "Mind if I walk with you?"
    show natsuki me e1a
    "She eyes me curiously."
    n lhip mh "Not at all, but why?"
    show natsuki md
    mc mg "Nothing in particular, I guess I just wanted to talk about stuff." # :):):):):):):):):):):)
    n ldown mc "Then yeah, let’s walk and talk."
    show natsuki ma e3d with None
    show natsuki:
        alpha 0.0
    show bg:
        xzoom -1
    show sayori turned lup e3d:
        matrixcolor TintMatrix("#f1d6bb")
        i11
    with Dissolve(0.2)
    "She shrugs to Sayori, who waves us off."
    "The other two have already gone their separate ways by this point."
    hide sayori
    show bg:
        xzoom 1
    show natsuki:
        alpha 1.0
    with Dissolve(0.2)
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    play music2 add_playback_info(audio.okev, get_pos()) fadein 2.0
    stop music fadeout 2.0
    n mh e1a "So, what’s on your mind?"
    show natsuki mj with say_dissolve
    mc eg mg "Honestly, I just wanted an excuse to hang out with you."
    show natsuki md e2a b1d with say_dissolve
    "She blinks a couple times, backing away."
    mc ed md "Hah, nah, I’m just messing with you."
    show natsuki mj b3a e1a with say_dissolve
    mc ea mg "I was actually curious about the student council."
    n e2a mh "Oh, I see."
    n cross mi e3c "Yeah, there’s not much to say; Chiaki really does most of the actual work, and I'm the one who handles the bookkeeping. Usually it's just approving budgets and Chiaki's many structural reworks."
    n e2a b1a mh "Aside from that, mostly I’m on hall monitor duties, helping teachers keep problem students in line, and working with the disciplinary council."
    n b3a e1a mc "Though a couple times a week I’m involved with meetings that keep me pretty busy; plus I have to get to school early most days to get through all the paperwork that I couldn't the previous day."
    n mh "It’s like..."
    n turned rhip e3d mc "Basically having a job while also at school."
    n e2c mh b1a "... That you don’t get paid for."
    show natsuki e1a md with say_dissolve
    mc thinking ml "Then why do you do it?"
    n me b3a "Hm?"
    show natsuki cross mj e3c b1d with say_dissolve
    "She ponders the question for a moment, as if unsure if she even has a reason herself."
    n b3a mi "I guess I do it because I’m curious about my limits."
    n e2a b1a mh "About what I can handle."
    n mg b1d "My..."
    n b3a e1a mh "My regular job is pretty physically and emotionally taxing, which is different to what I do here in everyday life."
    n turned lhip e2a b1a mb "Like, school is completely different. I can be someone here than I’m not anywhere else-"
    n ldown mg b3a "I..."
    show natsuki b3d e3c mj with say_dissolve
    "She shakes her head."
    n mm "No, forget I said anything."
    mc bg mg ldown "Is everything alright?"
    n mi "... If everything was alright, I wouldn’t have said anything."
    n b1d e2a mh "Then again, if it wasn’t, would I really be here?"
    n e1d mg "... Huh."
    n cross e1a b3d mi "You’re really making me think, today. And you’re not even trying to do it."
    n turned e2c rhip b3a mh "... Just bringing out some weird, wacky emotions in me, I suppose."
    show natsuki md with say_dissolve
    mc eg mb ba "I have that effect on people, I find. Either people hate me, or can’t get enough of me."
    mc ef ml ba "It’s honestly a little taxing in and of itself."
    mc bi mf "I mean, I’m..."
    show natsuki e1a b1a me with say_dissolve
    stop music2 fadeout 3.0
    mc ea ba mg "Look, can I be honest with you for a moment?"
    n rdown e3c b3a mh "Sure."
    show natsuki mj with say_dissolve
    "She shrugs, but I can tell she’s sincere."
    show natsuki e1a b1a with say_dissolve
    mc bi ef ml "... I don’t have many friends. I think that much is obvious."
    mc ea mg thinking ba "But the real thing that matters is {i}why{/i}."
    mc eg ldown "Because, if I’m honest, I don’t really like people all that much."
    show natsuki ma with say_dissolve
    mc ec ml "And I don’t mean in the edgy, teenager 'grr people' kind of way, I just..."
    mc ea mb "I dunno, I like being alone."
    mc eg "I enjoy my own company."
    n e2a mb b3a "I totally get that, honestly."
    n cross mc b1d "I’m blunt, and sometimes that bites me. But it’s also a lot less stressful to not dance around your words, to not think everything you say through a million times before you say it."
    n b1a mh "Kinda like Yuri does."
    n b3a e1a mb "Kinda like you."
    show natsuki ma with say_dissolve
    "I look away, a little embarrassed at being read so easily."
    n turned mh b1d "I’m not saying it’s a bad thing. What I’m saying is a bad thing is letting your insecurities lord over you."
    n e3c b3a mi "Sure, you might have done some bad things, or maybe bad things happened to you, but if you let those things rule you, then what are you?"
    n cross mh b1d e1a "A person, or an empty husk of what you wished you could be?"
    show natsuki mj with say_dissolve
    mc ef mh ba "..."
    n turned e2a b1a mi "Trust me. I wish I was stronger, faster, wiser, more intelligent, more charismatic, more caring, all of those things."
    n e1a b3a mh "But the one thing I don’t wish I was more of?"
    n mb "Sentimental."

    play music dawn fadein 2.0

    n b2a mc "You’re immensely sentimental, Melody."
    n mh b2b "One day, getting wrapped up in all of that suffering inside your head will hurt you."
    n e2a b2a nb "... And I don’t know if someone is gonna be around to pull you back out when it happens."
    n b3a mc e1a na "You’re a surprisingly good friend, for all your angst and victimhood."
    n b2a mb "Don’t go wasting that."
    show natsuki ma with say_dissolve
    _mc bi "... I want to be insulted."
    _mc eg ma "Obviously."
    _mc ea mh ba "But she speaks the truth. Not even an uncomfortable one, just..."
    mc eg ml "Yeah."
    mc mb "I think I understand."
    show natsuki b3a e3c with say_dissolve
    mc ea mg "There’s a time to worry about the past, and a time to worry about the future."
    n mb "And a time not to worry at all."
    n b1a e1a mh "Sometimes, it’s best not to think too hard. Just let things happen."
    n b1d lhip rhip mi "Or, take the time to follow your gut and just act."
    n rdown mh b3a "It could save your life, one day."
    show natsuki mj b1a with say_dissolve
    mc ml "You think?"
    n e2a md "..."
    n b1d mg "Yeah."
    n cross b3d mi "Life won’t give you a chance to breathe when your back is against the wall."
    n mh b1d "Sometimes, you need to just act."
    n e1a mi "No matter what you do, stick by your decision."
    n b1a mb "But, at the same time, don’t be afraid to backpedal."
    n b3a e2a mh "If you’ve messed up, make it right by stepping back and finding an exit."
    show natsuki mj with say_dissolve
    mc ed md "You’re full of advice, aren’t you?"
    n b1d mh "... Someone’s gotta be."
    n turned ldown b3d e1a mi "Do you know how much experience I have with pulling others from the dirt?"
    show natsuki mj with say_dissolve
    mc ea ml "... You mean metaphorically?"
    show natsuki b3a me with say_dissolve
    "She blinks a couple times, as if unaware of what she’d said."
    n mg "I..."
    extend mb e2a " Yeah."
    n b1a mh "Metaphorically speaking."
    show natsuki ma with say_dissolve
    mc ef mg "I’d imagine a lot."
    n e1a mh "... You’ve known Sayori your whole life. You know what she gets up to."
    show natsuki mj with say_dissolve
    mc bi mb "Boy, do I ever."
    show natsuki b4 md with say_dissolve
    mc ea bg ml "... Sometimes, it’s that exact worry that bothers me."
    n mg "Huh?"
    show natsuki md with say_dissolve
    mc ea mf ba "... Sayori."
    show natsuki b3a mj with say_dissolve
    mc ef mg "She’s strong, independent and unimaginably brave."
    mc ea mb "She’s a lot like my friend Amelia in that regard."
    mc mh "..."
    mc ef bi ml "But she’s also reckless, and it’s gotten us into trouble more than once."
    mc eg mg ba "... Even so, it was her strong spirit that really brought her to me in the first place."
    mc mb "She meant everything to me."
    n mh "She still does, doesn’t she?"
    show natsuki b1a md with say_dissolve
    mc ef mh bg "..."
    n e2a nb mg "I-"
    show natsuki me with say_dissolve
    mc ea ml bf "Natsuki, I..."
    n b2c e3c mc "No, it’s okay."
    n mb e1a b2a "... I won’t get in the way."
    n lhip na e2a b3a mh "The mark of a good friend is being able to see the bigger picture."
    show natsuki ma with say_dissolve
    mc ef bg mh "..."
    show natsuki b2a e1a with say_dissolve
    mc bi eg mj "We wouldn’t work. I think we both know that."
    mc ef ml "Besides, it was a long, long time ago."
    show natsuki e2a mj ldown with say_dissolve
    mc ea mb bg "I’m willing to leave it in the past."
    show natsuki cross e3c b1d mm with say_dissolve
    "Natsuki bites her lip."
    n e1a mg "... You’re..."
    n e2a mh nb "Braver than I am."
    show natsuki mm e3c with say_dissolve
    mc ef bi ml "... No, I’d call it cowardice."
    mc eg mg "I never had the strength to pursue it, even when I was unchallenged."
    n mb e1a b1d na "... Hah. You know, I figured that I’d have a hard time if someone ever challenged me like this."
    n turned b1a mh e3c "But now I think I understand."
    n lhip e1a mi "It’s not really about that, for either of us."
    show natsuki mj with say_dissolve
    mc ef ml ba "No, it’s not."
    show natsuki ma with say_dissolve
    mc ea mg "To us, she’s just our best friend."
    mc eg mb "And we’d do anything to see her smile."
    n mc b3a ldown "She’s worth more than some petty squabble."
    n mh "And if she picked one of us, then-"
    show natsuki ma e3c with say_dissolve
    mc ef mb "We’d both be happy for it."
    show natsuki e1d b1d mj with say_dissolve
    mc ml "... Even if she picked neither of us."
    show natsuki mn rhip with say_dissolve
    "Natsuki elbows me lightly."
    n rdown b1a mh e1a "Yeah."
    n cross b3a mc "We really are both stupid, aren’t we?"
    n e2a mb b1d "Giving up our own happiness for someone we care about."
    show natsuki ma with say_dissolve
    mc ed md "Hey, you said it."
    mc mg eg "... Honestly, sometimes it might pay to be a little more selfish."
    n b1a e1a mc "You miss the shots you don’t take, right?"
    n turned e2a mh "Well, if it helps, I’m not really one for shots."
    n lhip e3c b3d mb "... More of a cider girl, myself."
    n mn b3a e3d ldown "Mhm, gimme strawberry cider."
    mc mj ec ba "Geez, what are you, like twelve?"
    n e1a b1a mc "Nineteen in a couple months, actually~"
    show natsuki ma with say_dissolve
    mc bb mg nb ea "Wait, really? I got the feeling you were older, but geez..."
    n mh b3a "Yeah, I’m older than Sayori too."
    show natsuki ma with say_dissolve
    mc ef bi ml "Jesus. I owe one of those voices in my head an apology."
    show natsuki e3d mn with say_dissolve
    "She lets out a hearty chuckle as we continue walking."
    n e1a b1a mc "I get that a lot, don’t worry."
    show natsuki ma with say_dissolve
    mc ed md ba na "Hah, I’m sure you do."
    camera master
    show bg:
        blur 0.0
    show natsuki cross e2a b1d md 
    with Dissolve(0.2)
    $ say_transition = False
    "After a few more steps, she pauses, then frowns."
    $ autofocus.unblock("natsuki")
    n mh "Also... Remember the chat we had the other day?"
    n e2c mg b1a "... I don't really want to dwell on it, but-"
    n turned b2a mc e1a lhip "Thanks. For letting me be honest."
    show natsuki ma
    mc mb ea ba na "Of course. You're welcome to vent, yeah?"
    mc ef ml bi "... If you're gonna be, well..."
    show natsuki md ldown b1a
    mc ba mg "If you're gonna be the one looking after Sayori, I guess as the person who's known her longest, I-"
    show black 
    hide natsuki 
    with NonBlockingDissolve(0.5)
    "I sigh, looking at my feet."
    mc eg mg "I guess I feel a little responsible for her."
    n cross b1d mh "Why would you feel responsible? She's an adult."
    show sayori turned zorder 6:
        i11
        flash(0.5)
    mc ec ml "... For the same reason she's the one you see when you close your eyes."
    show natsuki e2b me:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    hide black 
    with NonBlockingDissolve(0.5)
    "Her eyes widen for a moment before she looks away."
    n e2a mg "With all the care she has for the people around her, it's hard not to care about her back."
    hide sayori
    n mi b1a "She pours her heart and soul into every relationship she has."
    show natsuki mj
    "I nod, biting my lip."
    mc mf ef bg "That's gonna explain a lot, I guess."
    n mb e1a "I don't have to say it, do I?"
    show natsuki ma
    mc ea mb bg "Nah."
    mc eg "I get you."
    mc ef ba ml "So..."
    show natsuki me
    mc ea mb "Wanna get some ice-cream?"
    n turned e1d b4 mh lhip "Hah?"
    show natsuki me
    "She raises an eyebrow."
    mc mg "I know this great place Sayori and I used to go that's on the way to the cafe."
    n lean b1d mb  "Are you asking me out on a date~?"
    show natsuki mn
    mc ed md "Please, if I were asking you out on a date, I'd be much less casual about it~"
    n b3a e3d mb "Then perhaps I'll be the one to ask you~?"
    show natsuki ma with None
    show black with NonBlockingDissolve(0.5)
    "She chuckles as she steps behind me, and where I expect some kind of light bullying, she instead-"
    "-Grabs my hand with both of hers."
    hide natsuki
    n turned ldown b2a e3c nc mh "Th- Thanks. Having someone who understands is..."
    n e1a mb "It's nice."
    mc ea bg mb "Y- Yeah. It's nice to be understood."
    n e2a b1a na mh "So..."
    n mg b1d nb "If anything happens..."
    n e1a b2a mb "Just know that I'm happy you're around."
    mc ml "Natsuki?"
    show natsuki turned b1a e3c ma na:
        i11
        matrixcolor TintMatrix("#f1d6bb")
    hide black
    with NonBlockingDissolve(0.5)
    "I turn to face her, but she's already released my hand and turned her back to me."
    n cross e2a b2a mb "Nothing. Just... Being sentimental."
    n b1a mh "W- Wanna... get that ice-cream?"
    show natsuki mj with None
    show natsuki e1a md
    camera master:
        align (0.5, 0.25) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("natsuki")
    $ say_transition = True
    "I tap her on the shoulder as I step beside her, taking her hand in mine and giving it a gentle squeeze."
    show natsuki turned e3c ma with say_dissolve
    "She responds in kind, and from this angle I can see a strong, if small smile grow across her features."
    mc eg mb ba "Of course. A friend of Sayori's is a friend of mine, after all."
    n e2a b1d mb "If that's true, she's in good hands."
    show natsuki ma with say_dissolve
    mc ea ml "... You going somewhere?"
    show natsuki md e3c with say_dissolve
    "Her eyes darken, but she blinks them away."
    n rhip e2c b1a mh "... Not for a while yet, but maybe."
    show natsuki md with say_dissolve
    mc mb "Why not bring her with you, when the time comes?"
    n b1d mg "... Where I go..."
    n rdown e1a b3a mh "I want her to do something because {i}she{/i} chooses. That's why I haven't said anything to her."
    show natsuki md with say_dissolve
    mc ec bi mj "If you don't tell her before we graduate, I swear to god I'll do it for you."
    camera master
    show bg:
        blur 0.0
    show natsuki b2a e1b nc me
    with Dissolve(0.2)
    $ say_transition = False
    "She lets go of my hand, her face flushing."
    $ autofocus.unblock("natsuki")
    n mg e1a "W- Wait, no-"
    n cross b1d e1d mh nd "... You're an ass."
    show natsuki md e2a
    mc ed md ba "Hah, ya got me~"
    show natsuki ma nb
    "Once she got a good look at my face, she clearly realised I was kidding."
    _mc ec mh "I don't feel like being the catalyst when I know Sayori's already aware."
    _mc ea "If something happens, then all I can do is be happy for the both of them."
    n b1a na mg "{size=-5}I'll keep her safe.{/size}"
    show natsuki mj
    mc mg ba ec "You will, but not because you feel responsible."
    show natsuki turned md b1d e3c nb
    "She closes her eyes, frowning."
    n na mh "Because I care about her."
    show natsuki md
    mc ed md "Besides, she's not something to protect - She's pretty tough, herself."
    n e2a mg b1a "... Yeah."
    n mb b1d "I guess I just need to..."
    n e1a b3a mh "Remember that- if anything happens..."
    show natsuki me
    mc ml ba ea "-You'll offer an arm. The difference between a superhero and a dictator is that one steps in when people ask, and the other steps in when they don't."
    n lhip e2a b1a mh "... I'll try and remember that."
    show natsuki mj
    mc eg mg ba "I don't know about you, but I'd want to make my mistakes and learn from them, even if it means getting hurt."
    mc ea mb "Sayori feels the same way."
    n ldown b3a mb e1a "Then I guess that's something we disagree on."
    show natsuki ma
    mc thinking mg "If you're perfect at everything, will you ever really learn?"
    n cross b4 e1d mh "And if you fail at everything, will you ever really be confident enough to try?"
    show natsuki e1a b1a md
    mc ec ml "You only fail if you give up - Lacking success doesn't make you a failure."
    mc ea ldown mg "It just means you've room to grow."
    n e2a mg "I see."
    show natsuki mj
    mc mb "Is that how you felt when you didn't get the presidency?"
    n mg b1d "... Maybe."
    n e1a b3a mh "But I guess I did kinda learn from it."
    show natsuki mj
    mc eg bi ml "... I'm just sorry I forgot."
    n turned lhip b4 mh "Forgot what?"
    show natsuki me
    mc eh md bg nb "N- Nothing!"
    show black with NonBlockingDissolve(0.5)
    "I laugh it off, stepping outside the door."
    _mc bd eb nb mh "Yikes, that'd kill the mood right quick, wouldn't it?"
    _mc ec ba ma na "I'm sure she'd get over it, but best not to give her a reason to mock me, no?"
    
    stop music fadeout 2.5
    scene black
    show bg mc_living_room
    camera master
    with Dissolve(2.5)
    pause 0.9
    $ set_date(hour=19, minute=46)
    $ say_transition = False
    $ autofocus.unblock("natsuki")
    play ambient int_night fadein 1.2
    hide black with Dissolve(1.2)

    "As I finally arrive home after some work in the café, I relax on the sofa, kicking up my feet."
    "I’m not exhausted today, which is a nice change of pace. Instead, I’m simply a lot more relaxed."
    _mc turned casual tail nostrands ec mh "Over the past week, I’ve been stressing so much over how much I’ve been run ragged and how quickly I was becoming emotionally drained."
    _mc eg ma "Now, though? I feel much, much more at peace."
    _mc ec ma "Knowing that everyone in the club feels pretty much the same way I do, with ups and downs, made me realise something."
    _mc ea "I’m far from alone on this journey. Sure, maybe it took a while for me to come to terms with it, but here I am."
    _mc ef bg "... Something Amelia’s been trying to show me for years, I guess."
    _mc eg "I’ll have to apologise for that too, next time I see her."
    _mc ea ba "Even so, I’m still impressed. I never thought I’d adapt so quickly and easily. Every one of them gives me a reason to look forward to going again the next day."
    _mc ef "I genuinely can’t remember the last time I was this happy."
    _mc mh bi "Not in recent memory, at the very least."
    _mc ma ba "So it brings a smile to my face."
    _mc ea "I should probably get my chores done and have an early night; I don’t want to be tired for work in the morning."
    _mc ec "Not to mention the sleepover tomorrow. I don’t think they’d let me live it down if I was tired through that."

    $ add_calendar_description(calendar_descriptions["natsuki"][9])

    call week_2_saturday_natsuki from _call_week_2_saturday_natsuki
    return