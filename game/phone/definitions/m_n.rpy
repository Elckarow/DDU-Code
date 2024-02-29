init python:
    def get_m_n_gc_name():
        return "Natsuki" if pov_key == "m" else "Monika"

init phone register:
    define get_m_n_gc_name:
        add "m" add "n" 
        icon ConditionSwitch(
            "pov_key =='n'", phone.asset("monika_icon.png"),
            "True", phone.asset("natsuki_icon.png")
        ) 
        key "m_n" as m_n_gc
    
    time day 21 month 5 year 2017 hour 17 minute 56
    "n" "Hey, Monika, I kinda wanted to apologise for being abrupt with you earlier."
    time hour 18 minute 11
    "m" "Oh, you kept my number? I thought you were just doing that as a formality."
    "n" "No, I-"
    "n" "I mean, kinda, but not really?"
    "n" "But back to what I was saying, I was in the middle of a job for Chiaki, and it got a little away from me"
    "m" "I know, I understand."
    "m" "I just hope you’ll consider my offer."
    "n" "I don’t know, this student council business has been..."
    "n" "Taxing."
    "n" "Maybe when it settles down a little?"
    "n" "Don’t get me wrong! I still don’t think I’ll have time, so don’t expect it or anything"
    "m" "I won’t."
    "m" "Thank you for getting back to me, though. I do appreciate it."
    "n" "Of course! It’s part of my duties to be punctual!"
    "m" "Right."
    "m" "In any case, let me know how it goes, and if there’s anything I can help with~"
    "n" "I was about to say the same thing, hahaha"

    time day 8 month 7 hour 15 minute 3
    "n" "Sorry Prez, I’m running an errand for the council. Might be a half hour late."
    "m" "Don't worry, it's fine!"

    time day 21 hour 3 minute 1
    "n" "Sorry, hope this doesn't wake you, but I’m not gonna be able to make club for about a week. Got some work stuff going on."
    time hour 6 minute 3
    "m" "Oh? That's alright. Anything I can help with?"
    time hour 10 minute 15
    "n" "No, not really."

    time day 16 hour 20 minute 24 month 8
    "n" "So"
    "n" "Yuri told me today"
    "n" "Well, about a lot of things, but"
    "n" "Specifically about that thing with her arm"
    "n" "That she does"
    "n" "With the, uh"
    "m" "I get the picture, it’s alright."
    "m" "She told you?"
    "n" "Well no, she didn’t 'tell' me"
    "n" "I mighta walked into the bathroom and well"
    "n" "When you hear strange noises you tend to investigate."
    "n" "She kinda had to tell me after that"
    "n" "I feel bad"
    "m" "Don’t, it’ll probably be good for her."
    "m" "It’ll mean she’ll trust you a little more."
    "n" "She already doesn’t like me, this is just gonna make it worse."
    "m" "She doesn’t dislike you."
    "n" "Pretty sure she does"
    "n" "She always has this kinda cold glare about her whenever I’m in the room"
    "m" "That’s... just her face?"
    "n" "Riiight"
    "n" "Either way, if she doesn’t want to talk, she doesn’t have to."
    "n" "I just kinda wish I knew either way"
    "m" "Trust me, she’ll warm up to you."
    "n" "Mostly I’m concerned about Sayori though. I think she’s probably feeling a little down about it more than I am."
    "m" "Funny, she said the same thing about you earlier today in class"
    "n" "She does that, always putting others first"
    "m" "I’m sure you both got it from each-other, from the looks of it~"
    "n" "Oh no, I definitely got it from her."
    "n" "You should have seen me when we first met"
    "n" "I was a mess"
    "n" "I’m glad I had Sayori around"
    "m" "That so? Maybe we have more in common than we think. Yuri was a bit of a mess before I came around too."
    "n" "Yeah?"
    "m" "Cross my heart"
    "m" "She does mean well, I promise."
    "n" "I’ll hold you to that."
    "n" "Oh and one other thing"
    "n" "I’m gonna probably try and keep Sayori out of the loop on this one, I don’t want her fretting over something else more than she already does"
    "m" "You’d keep secrets?"
    "n" "What’s one more?"
    "m" "I see"
    "m" "Natsuki, say..."
    "m" "This stays between us, but"
    "m" "You know who I am, right?"
    "n" "I take that to imply that you’re going to then tell me you know who I am?"
    "m" "Possibly"
    "n" "Fuck"
    "n" "Okay, now that, that has to stay between us."
    "n" "Please, please don’t ever mention it or bring it up again."
    "m" "I won’t. I just... had to be sure."
    "n" "That’s... This whole thing just got messy"
    "m" "I don’t know any details, I promise"
    "m" "In fact, I’d go so far as to say that I probably know a lot less than you think"
    "m" "I’ve just seen your face before."
    "n" "Oh my god, why didn’t you lead with that?!"
    "n" "You gave me a heart attack!"
    "m" "Geez, it’s not that serious! You’re just working with some contractors as an apprentice, yeah?"
    "n" "Yeah! It’s just... I don’t like people knowing. There’s some crazy people out there, yeah?"
    "m" "Yeah, that’s honestly fair. I’ll keep it to myself, promise"
    "n" "Thanks, prez. I really owe you one"
    "m" "Aha, it’s no big deal~ It’s just some simple work connections, after all."
    "n" "Yep~"

    time day 18 month 9 hour 5 minute 55
    "n" "Oh yeah, I’m gonna probably be late today, I’ve got a meeting with the council"
    "m" "No problem!"
