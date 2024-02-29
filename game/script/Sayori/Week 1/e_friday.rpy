label week_1_friday_sayori:
    call calendar_transition(day=27, hour=6, minute=0) from _call_calendar_transition_27
    scene black with Dissolve(1.0)
    play sound_loop phone_alarm fadein 5.0
    pause 4.0

    _mc turned messy naked eg bi mh "I don't deserve to get up."
    _mc "I don't deserve to get up."
    "I don't..."
    "Deserve."
    "To get up."
    _mc "Not after what I've done."
    _mc bg "How could I?"
    _mc "Sayori..."
    _mc "She trusted me."
    "And I betrayed that trust."
    "I did the unthinkable."
    _mc "No..."
    _mc "Why?"
    _mc bi "Why did I do that?"
    _mc "Why did I allow myself to..."
    "Ugh."

    stop sound_loop
    scene bg mc_bedroom_day_closed with Dissolve(0.3)

    "Forcing myself upright, I glance down at my hands."
    "Still shaking."
    "No, quivering."
    _mc turned messy naked eb be mf "What..."

    play music myconfession

    _mc eg bg mh "What have I done?"
    _mc ea bf "Sayori..."
    _mc "I'm..."
    _mc ef "What..."
    _mc eg bg "What do I say?"
    _mc ea be "What can I say, to make it..."
    _mc eg bi "No, after that..."
    _mc mm "There is nothing."
    "I can't."
    _mc mh "I..."
    _mc ea be "I don't think I'll be able to look her in the eyes, not after that."
    _mc bi eg "What the hell have I done?"
    _mc ec "I let my thoughts get ahold of me, and it manifested into that dream..."
    _mc mm eg "Argh!"

    play sound fall
    camera master at vpunch

    "I drive my fist into the bed, before collapsing back onto it."
    call close_eyes(0.4) from _call_close_eyes_14
    _mc mf "Dammit."
    _mc ba mh "It's..."
    _mc ea bb "It's not that big of a deal, right?"
    camera master
    _mc ef "I mean, I don't think I'll ever be able to look at her the same way, but..."
    _mc ba eg "If I keep my mouth shut, she won't find out."
    _mc ma "... I'll just have to live with myself."
    _mc ec mh "You know, if the past five years have taught me anything, it's this."
    _mc ef "I never was able to get her off my mind."
    _mc eg ma "She was always there, supporting me from the sidelines."
    _mc mh "I saw her there. Maybe not the loudest cheer, but she was there."
    _mc "She always spared time for me, even if she couldn't talk to me."
    _mc ea "And what have I done?"
    _mc bi eg mh "This."
    _mc mm "I treated my best friend like an object."
    _mc mh "It's not like I'm planning on remaining celibate, or anything. It's that I can't think of her that way."
    _mc ba ec "I've known her my whole life."
    _mc ef "It's... unthinkable that we'd..."
    _mc bg "Be together like that."
    _mc bi eg  "As much as I wish for it, I need to stop projecting my fantasies onto her."
    "..."
    _mc ec ba "I need to take a step back, and look at it logically."
    _mc thinking ea "Sayori means the world to me. She always has."
    _mc ec "But I can't let my feelings get in the way of our friendship."
    _mc ef "Right?"
    _mc ldown eg "She'll never return these feelings, so it's best to lock them away, and never think about them again."
    _mc ma "Yeah. Take this as a lesson."
    _mc ec mh "A lesson in control."
    _mc ea be "Sayori..."
    _mc ef bf "I'm sorry. I won't ever let it happen again."

    scene bg s_house_day with wipeleft_scene
    $ set_internet(False)
    $ set_date(hour=7, minute=55)

    _mc turned bun nostrands ec bg mh "I'm sorry, Sayori."
    _mc ef "I can't..."
    _mc eg "I can't wait for you today."
    _mc "It would be..."
    _mc mf "Too much."
    "..."
    _mc ec ba mh "Best get to school before she catches me."
    show bg residential_day with NonBlockingDissolve(0.3)
    "As I trudge off down the road, head hung in shame, I hear a sound behind me."
    _mc eb be nb mf "Oh, no..."
    stop music fadeout 2.0
    play ambient ext_day fadein 2.0
    s turned e3c b1d mi nb "Heeeeeeeeeeyyyy!"
    show sayori at r11
    s "You were gonna leave me behind! I'm not even late today! That's just mean!"
    show sayori md
    "She catches up to me within seconds."
    s e1a b4 mi "C'mon, why'd you do that? If I hadn't already been putting on my shoes, I wouldn't have caught you."
    s b2a mh e1b na "Don't tell me you're not planning on walking with me, right after we agreed to start walking together?"
    s e2c b2a mg rup "... Meanie."
    show sayori md
    mc mg "N- No, it's not that, it's..."
    s b1a e1a mg rdown "What, did you have a dream about me?"
    show sayori md
    mc mj ed bf "Urk-"
    s b2b lup mh "Oh? Was it a nightmare?"
    s mg ldown e3c "No, you poor thing!"
    show sayori md with None
    camera master:
        align (0.5, 0.2) zoom 1.7
    show bg:
        blur 2.0
    show sayori me e1a b1a rup
    with Dissolve(0.2)
    $ say_transition = True
    $ autofocus.block("sayori")
    "She places her forehead onto mine, checking my temperature."
    s mj b1d e3c "Hmm..."
    camera master
    show bg:
        blur 0.0
    show sayori rdown
    with Dissolve(0.2)
    $ say_transition = False
    $ autofocus.unblock("sayori")
    s e3d mn b1a "Yeah, I don't know how this works, ehe~"
    s e1a mb "But I assure you, I'm safe and sound! As long as you're feeling better, everything is fine, right?"
    show sayori ma
    mc na ef ba mf "I..."
    s lup b2a mh "... You are feeling better, right?"
    show sayori md
    mc md eh be nb "Y- Yeah, of course I am..."
    s ldown e1d b1d mh "You can't convince me if you aren't convinced yourself. C'mon, back inside."
    show sayori rup md 
    mc eb mg "What-"
    show sayori e2c at i44
    show bg:
        align (1.0, 0.8) xzoom -1.9 yzoom 1.9
    with Dissolve(0.2) 
    "Grabbing me by the arm, she drags me back toward the house."
    s mk xd "Stop- Resisting! I'm gonna take care of you, so just come quietly!"
    mc bd ed ml "No- hold-"
    camera master:
        align (0.65, 0.2) zoom 1.8
    show bg:
        blur 2.0
    show sayori b3d mm at i43
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    "Out of nowhere, she gains a burst of strength, forcing me forward and toward her."
    s b1a e1b ml nb "Ooof!"
    stop ambient fadeout 2.0
    camera master:
        easein_cubic 0.6 zoom 2.3
    pause 0.1
    play sound fall2
    camera master 
    show sayori xd b2c mk nb rdown:
        xcenter 0.5 zoom 1.4
        ypos 1.0 yanchor 0.65
    show bg:
        blur 0.0 xzoom 1.0 yzoom 1.0
    show expression Gradient("#646a6d", "#6c7376") as stuff
    with Fade(0.3, 0.0, 0.3)
    "Unprepared for it, she falls backward, dragging me along with her, and we crumple into a heap."

    play music myfeelings

    mc eb be mg "Sayori, are you alright?"
    show sayori b2a e3a lup at i11
    hide stuff
    with Dissolve(0.2)
    $ say_transition = False
    "I quickly right myself, pulling her to her feet."
    $ autofocus.unblock("sayori")
    s ldown b2b mh e3c "Yeah, I just... hit my head."
    show sayori rup lup xd b2c mk:
        xoffset 0.0
        easeout 0.3 xoffset -14
        easein 0.12 xoffset 14
        easein 0.12 xoffset -14
        easein 0.12 xoffset 14
        ease 0.15 xoffset 0
    "She wobbles about a little, and I have to catch her."
    mc na ef ml bg "Ah, geez, I'm sorry. I didn't mean for you to fall."
    s b2a mb e3a rdown na "Nono, I shouldn't have pulled you like that. My bad."
    s e2a mg ldown "But, I, uh..."
    show sayori md
    mc thinking ea bb ml "You don't feel so good?"
    mc ec ba mf "You don't look it, either."
    mc ldown ea mg"Come on, I'll take you back inside."
    s e1a mh "B- But what about school?"
    show sayori md
    "I ignore that our positions have reversed in an instant; she's clearly hit her head."
    mc ec ml "I haven't had a day off since the start of the year."
    mc eg bi mb "I'm sure one day won't make that much of a difference."
    mc ea bb mg "Come on, I've gotta make sure you aren't bleeding anywhere."
    mc thinking ba ml "Then check for a concussion."
    s e2a mb "Ehe... Alright."
    show sayori b1a e1b rup mk:
        xoffset 0.0
        easeout 0.3 xoffset -14
        easein 0.12 xoffset 14
        easein 0.12 xoffset -14
        easein 0.12 xoffset 14
        ease 0.15 xoffset 0
    "She wobbles from side to side, kept standing only by my grip on her shoulder."
    s e2a mg b2b "Yeah, I, uhh..."
    show sayori me
    mc ldown be ml "Geez, do you want me to call an ambulance?"
    s e2b b2a mh "No, just, gotta..."
    show sayori b2b e3c mg:
        easein_cubic 0.5 yoffset 40
    s "Sit down for a little while..."
    show sayori md e1a
    mc mg ba "Alright. But if you pass out, I'm calling, alright?"
    s e2a mg b2a "Yeah. Sure..."
    show sayori me with None
    show black with NonBlockingDissolve(1.0)
    "Slowly and carefully, we make our way back to her house between rest breaks."
    _mc ec ba mh "I hope she's alright."
    _mc ef bi ma "I suppose this is what I deserve, after all that this morning."
    _mc eg "My just deserts."

    scene bg s_house_entrance_day with wipeleft
    $ set_internet(True)
    pause 0.02
    scene bg s_living_room with wipeleft

    "It surprises me how light Sayori is, to be honest."
    "She's not what I would call a heavy build; I'm pretty sure I weigh more than she does by at least a decent chunk."
    "But geez, either I'm stronger than I look, or she's mostly air."
    "She feels lighter compared to when we were kids, which is... odd."
    _mc turned bun nostrands thinking ec mh "I hope she's eating alright, at least."
    _mc mf ea "Maybe that's part of it."
    _mc ma "Perhaps I could start making extra lunch and bringing it along for her. At least that way I know she's eating something."
    _mc ldown "I'll mention it when she gets up, I think."
    show bg:
        align (0.0, 0.8) zoom 2.5
    show sayori turned b1b e3c me:
        xcenter 0.5 zoom 1.4
        ypos 1.0 yanchor 0.65
        block:
            linear 2.02 yoffset -3
            easein_cubic 0.9 yoffset 2
            repeat
    with NonBlockingDissolve(0.4)
    "At the moment she's sleeping on the couch, and I don't want to disturb her."
    _mc thinking ec mh "Hmm. Maybe I'll make something for lunch?"
    _mc ea ma "Yeah, something for her to eat."
    _mc mf ldown "If she's just had a concussion, it'll need to be something light, maybe a stew?"
    _mc eb bb ma "Oh, a pumpkin soup would do nicely."
    _mc ec mh ba "I wonder if she'll like it though."
    _mc ef ma "She never was a fan of veggies."
    _mc thinking ea mh "Hmm. Perhaps I should make something a little safer?"
    _mc ec "No, she'll need something good for her, even if she doesn't like it."
    _mc "It's just sensible."
    _mc ldown ea "If she doesn't eat properly, it'll take her longer to recover."
    hide sayori
    show bg:
        zoom 1.0
    with Dissolve(0.2)
    "With something of a half smile forming on my face, I make my way toward the kitchen."

    scene bg s_kitchen_day with wipeleft

    _mc turned bun nostrands ec mh "Huh. There's a lot less here than I expected."
    _mc ea thinking "It's not so barren that I'd think she's not eating, but..."
    _mc ec "It does beg the question. Something that's been on the back of my mind for a few days."
    _mc ea "Where are her parents?"
    _mc ec "I know Sayori's an only child, like I am, but her parents certainly didn't abandon her."
    _mc "At least, I don't think they would."
    _mc ldown eg "I suppose I don't really know."
    _mc ec "But they don't appear to be around. There sure isn't enough food in here to feed three people."
    _mc ea "If she's living on her own, that's news to me, at least."
    _mc thinking "Maybe they're just on vacation?"
    _mc eg bi "No, they would have brought her with them, you'd think."
    _mc ec ba "Come to think of it, it would be weird to go on vacation in the middle of the school term."
    _mc bi mh ldown "Yeah, something doesn't quite sit right."
    _mc ef ba ma "From memory, they were always kind to me, and good to her."
    _mc ea bb thinking "I wonder what happened? Perhaps they moved for work, and decided to let her finish school?"
    _mc ec ba mh "Hmm. That makes a lot of sense, actually."
    _mc ldown eg "I suppose that's what I'll stick with, until told otherwise."
    show black with NonBlockingDissolve(0.6)
    $ advance_date(minutes=10)
    "After a few minutes, I throw together a relatively simple stew. The ingredients list is barren, at least compared to my place."
    _mc ea ma "Ah well. She's not going to be able to eat a stew, so the best thing for it will be to blend it into a soup."
    hide black with Dissolve(0.2)
    _mc "And... There."
    _mc eh "That should be perfect."
    camera master:
        align (0.2, 0.6) zoom 2.0
    with Dissolve(0.2)
    _mc md "I'll even add a dollop of cream for her, hehe."
    _mc ec ma "That's sure to cheer her up."
    camera master:
        align (0.7, 0.4) zoom 2.5
    with Dissolve(0.2)
    _mc thinking ea mh "I wonder if there's anything else I can throw in here to make her smile..."
    camera master:
        align (0.45, 0.3) zoom 3.0
    with Dissolve(0.2)
    _mc ma "Oh, there's something."
    _mc ldown eh "A pack of jelly!"
    _mc "Perfect!"
    camera master:
        align (0.2, 0.6) zoom 2.0
    with Dissolve(0.2)
    _mc ec "If I mix that together, while it might take a few hours to set, it'll make for a fantastic dessert tonight~"
    camera master
    with Dissolve(0.2)
    _mc ef "Huh. I'm even starting to sound more like her again."
    _mc "I guess that's a good thing, I mean..."
    _mc mh "Considering what we've been through, it doesn't surprise me how well we still blend together."
    _mc eg "It reminds me of something..."
    show black with NonBlockingDissolve(5.0)
    _mc "Something that witch said once."
    _mc "She said we were practically the same person, that if we'd dressed up to look the same, and swapped houses for a night, they would have been none the wiser."
    _mc ma "Hah. I'm surprised we never actually did that, now that I think about it."
    _mc ea mh "It might be a little harder now, though."
    _mc ec "I'd have to pin up my hair. Her's is shorter now."
    _mc ef "Not to mention..."
    _mc bi eg "She's grown up... A little more than I have."
    hide black with NonBlockingDissolve(1.0)
    "I look down at my... less than impressive volume."
    _mc thinking ea mf bb "Ah well, I could always pad them?"
    _mc mm nb ldown eg bi "N- No, that'd be stupid. I'd feel bad for trying that."
    _mc mh "Geez, what am I gonna do with myself? Getting jealous of her like that..."

    stop music fadeout 1.5
    scene bg s_kitchen_day with wipeleft_scene
    $ advance_date(hours=1)

    _mc turned bun nostrands ec mh "Well, it could be worse."
    _mc ea "Not sure how, but..."
    camera master:
        xoffset 0.0
        easeout 0.3 xoffset -14
        easein 0.12 xoffset 14
        easein 0.12 xoffset -14
        easein 0.12 xoffset 14
        ease 0.15 xoffset 0
    _mc eb be mj nb "Ah shoot!"
    _mc "The soup's spilling!"
    _mc ma bi eg "That's what I get for getting distracted!"
 
    scene bg s_living_room
    camera master
    with wipeleft

    _mc turned bun nostrands mh "Alright, here's the soup. I took as much time as I could to blend everything; too bad I couldn't use the blender. It'd make too much noise, and I really want to let her sleep."
    _mc ec "Instead, I had to do it with a fork. As you could imagine, it's far from the most efficient method."
    _mc "No, it probably took me a good ten minutes to properly get all the lumps out."
    _mc ea ma "But none of that matters, when I consider how nice the final product looks. The cream gives it both personality and texture."
    _mc "I'm sure she'll love it."
    show bg:
        align (0.0, 0.8) zoom 2.5
    show sayori turned b1b e3c me:
        xcenter 0.5 zoom 1.4
        ypos 1.0 yanchor 0.65
        block:
            linear 2.02 yoffset -3
            easein_cubic 0.9 yoffset 2
            repeat
    with Dissolve(0.2)
    $ autofocus.block("sayori")
    $ say_transition = True
    mc mb "Hey, Sayori, you feeling any better?"
    show sayori md e1d:
        pass
    "She stirs, clearly half-awake."
    
    play music a_sunshine

    s me "Mmm..."
    s b1a e3c mg "N- No, not the elephant..."
    s mu "That would go poorly with the broccoli..."
    mc mh "..."
    _mc ec bi mf "Uhh... What?"
    mc ec ml bi "Earth to Sayori?"
    s mh "Ground control..."
    s mb "This is Major Tom..."
    show sayori ma with say_dissolve
    mc md "Hey, c'mon, I know you're awake now."
    mc ea ba mb "I've made you some soup."
    s mg b1b "... Mmm... I can smell it."
    show sayori md with None
    show sayori:
        i11
        yoffset 0
    show bg:
        zoom 1.0
    with Dissolve(0.2)
    $ say_transition = False
    "She rises like a zombie from a grave to a sitting position, her eyes still closed."
    $ autofocus.unblock("sayori")
    s mu "Po... Ta... To..."
    mc ed md "Boil 'em, mash 'em, put 'em in a stew?"
    s mg "Yeah..."
    s ms "Stew..."
    s mu b1a "Hasselback..."
    s mb e3d "Yeah..."
    show sayori ma
    mc "Sorry, no hasselbacks today. I'll make some next time, I promise."
    mc ea mg "This one's gonna go down a lot more easily, though."
    show sayori md e3c b1d
    "Sayori pouts a little, but can't hide her smile."
    s lup e2a mg "Alright, you win."
    show sayori rup e1b b1a ma at hop
    "Instantly bouncing up, she takes the bowl."
    mc eb bb ml nb "Woah, slow down. You straight passed out a little while ago."
    s rdown ldown mh  "Well yeah, but you're here, so it's fine."
    show sayori ma
    mc ec mf bi "Wh- What's that supposed to mean?"
    s e3d mb "It means that if I fall over, you'll catch me."
    show sayori ma
    mc ml ba na ea "I mean, yeah, but..."
    s mb "And if I get hurt, you'll save me."
    show sayori ma
    mc mh "..."
    s mh e2a "Because that's just you."
    s mb e1a "You're always there when I need you."
    show sayori ma
    mc ef ml "... Yeah. Yeah, I am."
    show sayori mn e3d
    "She grins at me."
    s mo "And you make me food."
    show sayori mn
    mc ed md "Hah, that's true."
    show sayori mg lup e3c
    "She brings the spoon to her mouth, and begins to practically inhale the soup."
    show sayori ma e3d
    "I figure I should give her a moment, so I give her a soft wave and return to the kitchen for my own bowl."

    scene sky_day at moving_sky with Dissolve(2.5)
    pause 2.0
    scene bg s_living_room
    show sayori turned md at i11
    with Dissolve(2.5)
    $ advance_date(minutes=63)

    s lup mh "Soooo..."
    show sayori ma
    mc turned bun nostrands md ed "You know, I was just about to say that."
    s rup mn e3d "Ehe, we're in sync!"
    show sayori ma ldown rdown
    "I can't help but let out a chuckle."
    "We've just been sitting on the couch for the past hour. Not even watching TV, just..."
    "Chilling."
    show sayori e2a
    "It's a good feeling."
    "Possibly the best feeling."
    "It takes me right back to when we were kids."
    mc ea ml "Hey Sayori..."
    s e1a mh "Yeah, I remember. The tent, right?"
    show sayori ma
    mc mb "Yeah, that's exactly it."
    s tap na ma eb bc "I'm still upset with you, you know."
    mc be eb mf "Urk-"
    show sayori ea
    mc bd mg ea "It wasn't my fault! I thought it was a good idea at the time!"
    s md "The one time I let you pick the spot? You realised we both could have died, right?"
    show sayori ma
    mc ef bi mf "W- Well, yes, but..."
    mc ea ml ba "We didn't?"
    s nb md ee "Only because we were out near the river at the time, which, may I remind you, was my idea."
    show sayori mc
    mc ec mh "..."
    extend ef mf " Yeah..."
    s turned mg na "That reminds me, too."
    s b4 mh e1d lup "Seeing as you owe me your life, I reckon you should start doing more work around here."
    show sayori md
    mc ec ml "Now wait, hold on-"
    s ldown e3c mi b1d "No, no holding on. I've waited over five years for you to pay up on that life debt."
    show sayori mj
    mc thinking ml ea "Wait, what about the one you owe me?"
    s mk b1a nc e1b lup "Urk-"
    show sayori b2a e2b nd ma
    "Sayori's face crumples as she bashfully turns away."
    mc ldown bi ec ml "I broke my foot over that, remember?"
    mc bd ea mg "And the thanks I get?"
    show sayori rup xd b2b nc ml
    s "No, wait, I made you a cake!"
    show sayori mk
    mc ba ed md "No, you made me a lump of charcoal."
    show sayori tap eb nb ma ba
    "She pouts and looks away once more."
    s bc md na ea "But at least I tried!"
    show sayori mc
    mc ef ml "I mean, that is true."
    mc ed md "It was good tasting charcoal."
    $ autofocus.block("sayori")
    s nd ma eb "..."
    "She whispers something under her breath."
    "Unfortunately for her, I know her too well. Simply reading her lips is enough."
    show sayori mc
    mc ef ml "Of course I ate it. You made it for me."
    $ autofocus.unblock("sayori")
    s turned na lup b2c e2a mh "B- But..."
    show sayori me
    mc ea be mb "Sayori, you tried to make something nice for me. That's all that matters."
    $ autofocus.block("sayori")
    s e1a b2a ma ldown "..."
    "A small smile crosses her face. This one, I'm sure, is a genuine one."
    $ autofocus.unblock("sayori")
    s mg b2b e3c "Thank you. For just..."
    show sayori md
    mc ml ba "Everything?"
    s e1a b1a mb "Yeah."
    show sayori md
    mc mb be "And thank you. I couldn't have done it without you."
    s b4 rup mg "Done what?"
    show sayori md
    mc eh md "Lived as long as I have, haha~"
    s rdown e3d mn b1d "Not with me saving your butt all the time, no~"
    show sayori ma
    "I can help but smile."
    mc mb ea ba "But, despite all the crazy stuff that happened, we're still here." # im stuff
    s e1a mh b1a "Right? I swear you should have dropped dead chasing me around so much."
    show sayori ma
    mc ed md "Oh, I don't die that easily."
    s b1d e1d mb "Tell me about it. I've been trying for years!"
    show sayori ma
    "I shoot her a sidelong glance, as a wicked grin crosses her face-"
    show sayori e1a b1a
    "And disappears just as quickly."
    s mb lup "Admit it, you'd be lost without me."
    show sayori ma
    mc "As lost as you'd be without me, I suppose."
    s ldown e2a mb "True."
    show sayori ma with None
    show mc_roof zorder 5 with NonBlockingDissolve(4.0)
    "A silence falls over us. Far from an uncomfortable one, more just..."
    "Happy."
    "As I stare softly at the roof, just soaking in the silence, I feel a presence upon my shoulder."
    "And, softly, one form in my hand."

    $ add_calendar_description(calendar_descriptions["sayori"][2])

    call week_1_sunday_sayori from _call_week_1_sunday_sayori
    return