label week_1_saturday_natsuki:
    call calendar_transition(day=28, hour=7, minute=6) from _call_calendar_transition_16
    scene bg cafe_inside_day
    with dissolve_scene_full
    if preferences.language is None:
        $ auto_advance_date_mult = 1.0
    $ set_internet(False)

    "As I make my way into the cafe I call work, I’m greeted by a most unfamiliar sight;"
    show rc at t21
    show boss turned bb md at t22
    $ persistent.boss_seen = True
    
    play music cafe
    
    "Someone appears to be making a scene."
    "The boss is just sitting behind the counter, listening quietly while some blonde rants and raves about something or other."
    _mc turned casual thinking mh "Hm. Perhaps something’s happening? I’ve never really known my boss to just stay silent."
    show rc at hop
    rc "Who fixed this coffee? It tastes absolutely horrendous!"
    rc "I want to speak to them right now! Where are they?!"
    b ba mb "That would be me, miss. What may I help yer with?"
    show boss ma
    rc "Oh good, {i}someone{/i} finally answered me."
    show rc at hop
    rc "You messed up my coffee. I asked for extra dark and extra sugar! There’s hardly {i}any{/i} sugar in this disgusting mug, and it’s not {i}nearly{/i} dark enough either! It tastes absolutely horrible, and I want to speak to your manager."
    b ec mb "Aye, that would be me. Now, if yer’d like, I would gladly remake the coffee for yer. It was a long black, two sugars and a slight dash of milk, correct?"
    show boss ma
    rc "Yes, if you can hear and read, that’s exactly what I asked for."
    show rc at dip
    "The rude lady snaps her fingers, as if expecting her coffee to be remade for her just like that."
    _mc bi ec ldown "I almost want to dump an entire bag of sugar into her coffee, given how rude she’s been to the Boss."
    b ed mb "Aye, I’ll get right on that then."
    show rc at thide
    hide rc
    show boss ea me at t11
    b "Ah, kiddo. Would yer kindly start early? Get yerself set up; yer can take over out back when yer’ ready."
    show boss ma
    "The old guy notices me, giving me a small smile."
    rc "Excuse me? I was just speaking to you. Who is this? Another customer?"
    show rc at t21
    show boss at t22
    "The lady turns in my direction, as if I made her day worse just by stepping foot into the cafe."
    b rup mb "That’s my best employee. A charming young lass who would love to help yer out, right?"
    show boss ma
    mc mg ea ba "Ah, y- yeah, I would-?"
    show boss rdown at thide
    show rc at thide
    "He gives me a small wink. Ah. This is a learning experience, is it?"
    hide boss
    hide rc
    "Taking his hint, I walk behind the counter, wash my hands under the sink, and don my apron, prepped for work."
    _mc ec mh apron "As much as I would like to teach this lady a lesson in karma, I don’t want to cause the boss any further problems."
    show rc at t11
    rc "So now you’re not even making the coffee yourself, but having your little employee do it instead? Just how incompetent are you?"
    mc mg ea "Actually, I’ve been making coffee for around five years-"
    rc "Five years, five smears, whatever. I don’t care, just fix my stupid coffee already."
    "My lip twitches as I settle into the station, with my boss stepping back. I have a feeling I know what’s going on here, but would it not have been better if he’d fixed the order himself?"
    show black with NonBlockingDissolve(0.2):
        alpha 0.6
    "Sighing, I start grinding the beans. Long black, two sugars, and a dash of milk."
    "It takes mere seconds for the grinder to finish, and for me to start the process of making the coffee itself. I pour the sugar in first to allow it to melt into the base as it pours, which will let the sugar blend evenly."
    "After that, I top the mug up with hot water, as a long black should be. If she’s going to complain about the coffee being bitter, she shouldn’t have ordered a long black."
    hide black with NonBlockingDissolve(0.5)
    "... And there. With a tiny dash of cold milk, the coffee is complete. I hand it over, before getting another glare."
    show rc at dip
    "The lady takes one sip of the coffee I fixed with precision."
    rc "Excuse me? Just how bitter did you make this thing? And it’s not dark enough! I said I wanted extra dark! Where’s the sugar I asked for?!"
    "The lady continues ranting, her words slurring together until I could no longer make out what she was complaining about."
    _mc eg bi mj "I’m sorry lady, I can’t help you if you continue to act like this."
    mc ea mg ba "My apologies, but you asked for a long black, which is inherently a bitter coffee. If you would like, I could add some caramel or vanilla flavouring to offset the-"
    rc "Uh, excuse me? Do you know just how many carbs that is?"
    mc ef mf bi "{size=-7}And yet you wanted two sugars...{/size}"
    "I mumble under my breath, inaudible to anyone around me."
    mc eg bi mg "Well, that is simply the coffee you ordered."
    "The lady tips her cup over, spilling the entire mug’s contents onto the floor."
    rc "I don’t want this anymore. I want a refund."
    "I start to bite my tongue, but change my mind."
    mc ea bd mg "Of all the disrespectful, arrogant, pig-headed cretins I have had the displeasure of serving, you have now topped the list. I tried being polite. I tried playing it your way. I’ve had enough."
    rc "How rude! I’m speaking to your manager. Bring him back here, this instant."
    mc ec bi ml "You know what? No. I don’t think I will. Get out of my shop."
    "The lady huffs, not budging."
    rc "{i}Your{/i} shop? Even if it {i}was{/i} your shop, what are you going to do? You can’t make me leave. I want my extra dark, extra sugar coffee, and I’m not leaving until I get what I dese"
    mc bd ea mb "What you {i}deserve{/i}? Be careful what you wish for."
    rc "Is that a threat? I have a right as a customer to order here. Now, make my coffee like I asked!"
    mc mm eb "And, as I attempted to explain through your thick skull, you didn’t want the coffee you ordered! You can’t have a black coffee without it being bitter!"
    "My fists clench as I grind my teeth. I’ve had more than my fill of this woman."
    show boss turned rup at i11
    hide rc
    camera master:
        align (0.5, 0.0) zoom 1.5
    show bg:
        blur 2.0
    with Dissolve(0.2)
    $ autofocus.block("boss")
    $ say_transition = True
    "A hand upon my shoulder is enough to cause me to whirl around, only to be greeted by the warm smile of my boss."
    b me bb "That’s enough, kid. Yer did yer best."
    b ba rdown mb "Miss, I’m kindly going to have to ask you to leave. Here’s your refund; all sorted for you. I appreciate that you didn’t receive the coffee you ordered, so if you would like, I would be happy to make something new, at no cost."
    show boss ma with say_dissolve
    mc mg nb "Wait, you’re just-"
    show boss ec
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    "He gives me a nod, and I step away from the barista machine. I’m sure he’s got this all figured out; best to leave it to him."
    show rc at t21
    show boss ea at t22
    "What surprises me more is that the woman suddenly calms down considerably."
    rc "Why thank you, finally. I’ll take a vanilla frappuccino, since no one here seems to know how to make coffee."
    show boss ec
    "The boss simply gets to work making the frappé. He waves me off to get some of the tasks out the back complete, and I comply. Anything to get away from this raving lunatic."

    scene bg cafe_inside_afternoon
    with wipeleft_scene
    $ set_date(hour=16, minute=10)
    camera master:
        align (0.5, 0.0) zoom 1.5
    show bg:
        blur 2.0
    show boss turned md:
        matrixcolor TintMatrix("#f5e2bb")
        i11
    with Dissolve(0.2)
    $ say_transition = True

    "During my break that afternoon, the boss takes five to sit down with me."
    b me bb "Do yer understand why I did what I did?"
    show boss md with say_dissolve
    mc turned casual apron ef mg "I suppose so, it just... came out of nowhere, I suppose."
    b eb me "Life does that, kid. It’ll sneak up on yer, grab yer by the ankles, and rip yer away from whatever yer were doing before. If yer can’t roll with the punches and find solutions, it’ll be harder for yer to keep up."
    show boss md with say_dissolve
    mc ea ml "So..."
    b ba me "So if yer can’t find a way to defuse a situation, what can yer do?"
    show boss md with say_dissolve
    mc thinking mg "Call for backup?"
    b ec mb "Aye, or look for another solution. What do yer think yer could have done better, today?"
    show boss ea md with say_dissolve
    mc ml ec "Well, as soon as you came back, she started to chill, right? Did you know that would happen?"
    b mb "Aye. Yer see, a narcissism complex doesn’t rear its head all the time. More often than not, these people are lovely to be around. It’s when something happens that they can’t control that things get out of wack."
    show boss md with say_dissolve
    mc ea mg "So she got a coffee that she wasn’t expecting, and because of that, rather than own up to the mistake of ordering the wrong thing, she doubled down, hoping that you would crack first?"
    show boss ma with say_dissolve
    "He gives me a smile."
    b ec mb "Now yer’ve got it. Yer won’t win when someone’s like this. Best to let them have their little victory; if yer fight them, all they’ll do is storm out and leave a bad review, which can hurt your business."
    show boss ma with say_dissolve
    mc ldown bd mb "So it’s better to go along with them? Isn’t that the same as letting them win?"
    b ea mb "It’s exactly the same; because them winning, is you winning."
    b me "It’s not you against the customers, it’s you working with them to make everyone’s lives better. That’s what the service industry is, Melody."
    show boss ma with say_dissolve
    "I shrink back a little at him using my name. It reminds me of my parents, calling me that. He doesn’t do it often; only to make a very serious point."
    mc ea mg ba "I understand. It’s better to make the customers feel respected, so that they become repeat customers, right?"
    b mc ed "It’s much easier to get a customer to come back, than it is to get them to walk in for the first time. Get yer regulars coming regularly, and the business will succeed."
    mc ef ml "Right. I guess it makes sense?"
    b mb ea "Yer’ only young. I don’t expect yer to have the answers yet, only that yer’re willing to work toward them. Give it time, kid."
    show boss ma with say_dissolve
    "I give him a small smile. He went out of his way to teach me something today, even at the expense of potentially damaging his business’ image. I should be thankful."
    camera master
    show bg:
        blur 0.0
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("boss")
    b mb "I best be getting back to the floor, eh? Enjoy yer break, kid. There’ll be plenty of work left by the time yer return."
    show boss ma at thide
    mc ea mb  "Aye. I’ll see you out there shortly."
    hide boss
    "He wanders off, seemingly happy with what he’s taught me. Let’s just hope it sticks."

    stop music fadeout 2.0
    scene bg mc_living_room
    show bg mc_living_room as stuff:
        align (0.35, 0.2) zoom 1.7 alpha 1.0
    with longfade
    $ set_date(hour=20, minute=10)
    $ set_internet(True)
    pause 0.3
    play sound doorbell
    pause 1.0
    play music dollaort

    _mc turned casual mf "Hm?"
    hide stuff with Dissolve(0.2)
    "I pause the show I find myself idly watching and sit up. Turns out I’d spread myself across the sofa, lazing about like I owned the place."
    _mc ec bi ma "Joke’s on them, I do own the place."
    _mc eg "Take that, people who didn’t ask."
    _mc bb eb nb mf "Oh, right, the doorbell!"

    scene bg mc_house_entrance_night with wipeleft
    show sayori turned lup rup e3d at t11

    s mc "He-ey~"
    show sayori ma
    mc turned casual mb "Hey Sayori! What’s up?"
    s mb ldown rdown e1d b1d "You, silly! You’re taller!"
    show sayori b1a e3d ma lup
    "I chuckle as she brings her hand from the top of her head to mine to demonstrate."
    mc ed md "By about an inch!"
    s ldown mb e1a "Still! You’ve grown since we hung out as kids. I was once the taller one!"
    show sayori ma
    mc ea mg "This is true; Comes with being so much older, huh?"
    s tap "Boo, you’re calling me old..."
    mc ed md "Back when you were my age, you could run a whole mile!"

    scene bg mc_living_room with wipeleft
    play sound fall
    show sayori turned b2b mj e3c at t11

    "Sayori pouts, sitting down on the sofa."
    s b1d mi "Ruuuude."
    show sayori mj
    mc turned casual mg "Never said I wasn’t."
    s rup e1a b1a mh "What if I called you young, hmm? How would that feel?"
    show sayori ma rdown
    mc eg mb "Means I’ve still got my good looks and charm, and that I’ll live longer."
    show sayori e3c:
        xalign 0.5 yanchor 0.68 ypos 1.0
        zoom 1.3
    show bg:
        align (0.8, 0.69) zoom 2.3 blur 2.5
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("sayori")
    "I sit down next to her, gently elbowing her shoulder. In response, she sidles up to me, resting against my arm."
    s mh "So... What are we watching?"
    show sayori md with say_dissolve
    mc ml ea "Not sure, yet. What do you feel like?"
    s mg e1a "I think I could watch... something romantic."
    show sayori ma with say_dissolve
    mc ed md "Oh? Been bitten by the {i}looove bug{/i}?"
    show sayori b1d e1d mj
    camera master:
        align (0.5, 0.1) zoom 1.0
        easein 0.1 zoom 1.03
        easeout 0.1 zoom 1.0
    "I chuckle, tapping her head with mine."
    s e2a mh b1a "No, but someone I know might have been. Gonna do some research for them."
    show sayori md with say_dissolve
    "I let out a small grin. That’s so like her, too. I wonder who that friend is, but best not to ask. Someone from the club, perhaps?"
    show sayori e1a me with say_dissolve
    mc ea mg "Alright, how’s this one?"
    "I bring up something that looks overly cheesy, thinking she’ll laugh it off, but to my surprise, she jumps at it."
    s lup rup ml e1b "Oh! No way! I can’t believe you remembered!"
    show sayori e1a me with say_dissolve
    mc ml nb "R- Remembered what?"
    s b4 e1d mh rdown "... The movie we watched together for my thirteenth birthday?"
    show sayori mj b1d with say_dissolve
    mc ef mf "I, ah-"
    _mc eb bd mh "I have no idea what she’s talking about. Her thirteenth? I thought we went to the park for that..."
    s b1a mh e1a "When we got back and snuck up to your bedroom to hide under the sheets?"
    show sayori ma with say_dissolve
    mc bb mg "OH! And we stayed up all night watching movies! I remember!"
    mc ea na mb ba "That was the best! I had so much fun!"
    show sayori e3d ldown with say_dissolve
    "Sayori beams at me, happy to see me relive the memory."
    _mc ec ma "God, I don’t think I’ve thought about that in five years!"
    s lup mc e1a "Do you remember when we were almost caught, and I disguised myself as your legs?"
    show sayori ma with say_dissolve
    mc eh bg md "Do I ever! I don’t think I could ever forget! You were right up... Ah, uh-"
    s mh ldown "I was, wasn’t I? But hey, it worked!"
    show sayori ma with None

    camera master:
        offset (850, 250)
    show bg:
        blur 0.0
    hide sayori 
    with Dissolve(0.2)

    "My voice, as well as my mind, trails off, thinking of a particular moment during our frantic hiding. Now that I think about it, it’s pretty likely they knew anyway, and just humoured us."
    "But I think that was one of the moments when I realised..."
    _mc ef ba mh "When I realised just what Sayori meant to me at the time."
    s turned mg "You okay, Mel?"
    mc nb mg "Y- Yeah, I, ah..."
    mc ea ml ba na "Sayori?"
    show sayori ma

    camera master
    show bg:
        blur 2.5
    show sayori turned:
        xalign 0.5 yanchor 0.68 ypos 1.0
        zoom 1.3
    with Dissolve(0.2)

    "I turn to face her, and she pauses to look at me with her sapphire eyes."
    show sayori md with say_dissolve
    mc mb "I’m glad you’re back."
    "She flashes a confused look,"
    show sayori ma with say_dissolve
    extend " before replacing it with one of understanding."
    s mb e3c "Yeah. Me too."
    show sayori ma with say_dissolve
    "She snuggles back into me, and we settle down to watch the movie."
    "I put my arm around her and we relax for a while. Even if things aren't perfect, I'm truly thankful she's back."
    "And this time, I won't let her go. She's still my best friend, even if we'll never be together."
    "That means more to me than any relationship ever could..."
    _mc ec ma "So let us have this, whatever gods that exist. Let us just... have a moment."
    $ say_transition = False

    $ add_calendar_description(calendar_descriptions["natsuki"][3])
    stop music fadeout 1.5

    call week_1_sunday_natsuki from _call_week_1_sunday_natsuki
    return