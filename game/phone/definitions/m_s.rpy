init python:
    def get_m_s_gc_name():
        return "Sayori" if pov_key == "m" else _("{#sayori gives monika this weird ahh nickname}Monslie")

init phone register:
    define get_m_s_gc_name:
        add "m" add "s" 
        icon ConditionSwitch(
            "pov_key =='s'", phone.asset("monika_icon.png"),
            "True", phone.asset("sayori_icon.png")
        ) 
        key "m_s" as m_s_gc
    
    time day 9 month 7 year 2017 hour 8 minute 11
    "s" "Morning Prez!"
    "m" "Morning, VP~"
    "s" "So, ehe, would it be alright if I left a little early today? I have a friend from the Jazz club who wants me to watch them practice for the Arts Day performance next week."
    "m" "Sure, that's alright!"
    "s" "I just feel bad because I’m supposed to be setting an example, so…"
    "m" "Don't worry! We all have other commitments sometimes!"
    "s" "Still, I’ll try and be better in the future"
    "m" "No pressure! You know we're pretty chill, so no need to push yourself."
    "s" "Sure!"

    time day 21 hour 12 minute 43
    "m" "Hey Sayori, you're Natsuki’s friend right?"
    "s" "Best friend~"
    "s" "You're asking where she is today?"
    "s" "I dunno"
    "s" "She's working this week"
    "m" "She mentioned, but she never mentioned what she does."
    "s" "Maybe ask her, instead of me?"
    "m" "So you don't know either?"
    "s" "Haha, got me."
    "s" "No idea. It's just…"
    "s" "She’s a little mysterious."
    "m" "Maybe she likes it that way?"
    "s" "Oh, she does! You can tell"
    "m" "Aha, nothing to worry about then~ I just thought she was being cryptic, but if that’s part of the bit then"
    "s" "Yeah! It's a bit!"

    time day 28 hour 17 minute 3
    "s" "Before you ask, no, I don't know"
    "m" "You got me"
    "s" "She always does that, vanish for a week and come home covered in cuts, burns and bruises. She hides it with makeup, but"
    "s" "She can't hide them from me."
    "m" "Maybe you should talk to her about it?"
    "s" "She won't. She always, always brushes it off."
    "s" "Plus, that's a lot coming from you."
    "m" "Ouch"
    "s" "I’m just saying, you should talk to your friends sometime instead of just pretending everything is fine."
    "m" "You’re perceptive, aren't you?"
    "s" "I grew up around Melody."
    "m" "Melody…"
    "m" "Wait, the girl from my class? Brown hair, quiet, moody?"
    "s" "Yeah, that's her."
    "s" "At least, it is now."
    "m" "she was different, I take it?"
    "s" "It's a long story. A lot of the past."
    "s" "But she’s good, I promise."
    "m" "Isn't she also ranked like fourth?"
    "s" "You, Natsuki, Chiaki, then her, yep. I remember."
    "m" "Odd piece of trivia to remember."
    "s" "Not really. Natsuki’s my best friend, Chiaki’s one of hers, and well"
    "s" "Besides, as the bottom rung, it’s… Useful."
    "m" "Why would you put yourself down like that?"
    "s" "Like what?"
    "m" "You don't even realise, do you?"
    "s" "Realise what?"
    "m" "Nevermind, don't worry."
    "m" "Either way, thank you for talking to me about it."
    "s" "Sure!"
    "s" "Just don't tell Natsuki"
    "m" "Ah. That's how it is?"
    "s" "Sorry"
    "m" "Seems we're both keeping secrets."
    "s" "Seems so"
    "s" "Thanks, Monika"
    "m" "Naturally~"

    time day 26 month 8 hour 17 minute 22
    "s" "hey so"
    "s" "was thinking"
    "s" "are Natsuki and I in the way?"
    "m" "Of what?"
    "s" "I dunno, just feels like"
    "s" "didn’t wanna talk about it with everyone around but it feels like we’re interfering somehow"
    "m" "No, there’s no problem."
    "s" "like she’s warmed up to us but it still feels a little like she doesn’t want us around"
    "m" "I want you around."
    "s" "Yeah?"
    "s" "I guess it’s okay then?"
    "m" "Yuri’s just slow to get used to people, promise"
    "s" "Then I’ll trust you"
    "s" "Sorry, just felt like we were imposing"
    "m" "If anything, you two were here first"
    "s" "I guess that’s also true, isn’t it?"
    "m" "So don’t take it personally, she’s just shy. Maybe if you read with her she’ll warm up to you?"
    "s" "I’ll try that!"
    "s" "Thanks prez!"
    "m" "You’re welcome~"

    time day 28 hour 16 minute 55
    "s" "Sorry I rushed off early today, I just remembered there was some stuff I had to do at home. I did wanna say though, I tried reading with Yuri today, dunno if you saw"
    "m" "I did - It went well, no?"
    "s" "Super well!"
    "s" "Thank you!"
    "m" "Naturally! I’m just glad she’s finally warming up to you two."

    time day 5 month 9 hour 14 minute 47
    "s" "Oh, right, I’m sick today so I can’t come to club"
    "m" "I was wondering why you aren’t in class. I’ll send Natsuki with some notes for you."
    "s" "Thank youuuu"

    time day 6 month 10 minute 34 hour 18
    "s" "I’m sorry, I should have kept better control of the club. It was my failing as the VP."
    "s" "I had no idea it was getting out of hand until it already was."
    "m" "It’s alright, it happens."
    "m" "I had no idea they could get that heated…"
    "s" "Neither did I"
    "s" "It kinda came out of nowhere. They’ve had arguments before, but it feels kinda like they both took it personally this time."
    "m" "We should chat with them"
    "s" "Yeah"  

    time day 14 minute 56 hour 19
    "s" "Hey so"
    "s" "I noticed you and Yuri haven’t really talked since it happened"
    "m" "It’s fine. We’re just in a bit of a rough patch."
    "m" "It never lasts long, and honestly, it’s given me some time to reassess things."
    "m" "Yuri’s my best friend, but she can be a lot sometimes."
    "m" "I just want her to understand that."
    "s" "Okay, but if you don’t talk, you’ll run out of time."
    "s" "That’s… A lesson I know all too well."
    "m" "You’re right. I’ll talk to her when I see her next."
    "m" "Thanks, Sayori."
    "s" "I didn’t really do anything, but sure~"
    "m" "No, you did. You gave me a little perspective."
    "m" "Thank you"
    "s" "It’s what I do~!"  
