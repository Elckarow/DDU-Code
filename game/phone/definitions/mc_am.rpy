init python:
    def get_mc_am_gc_name():
        return "Amelia" if pov_key == "mc" else "Melody"

init phone register:
    define get_mc_am_gc_name:
        icon ConditionSwitch(
            "pov_key =='am'", phone.asset("mc_icon.png"),
            "True", phone.asset("amelia_icon.png")
        ) 
        key "mc_am"
        add "mc" add "am" as mc_am_gc
 
    time month 8 day 30 year 2015 hour 17 minute 23
    "am" "Happy birthday, Melody! I know I don't usually text you, but I'm out right now so I couldn't send you a message like I normally do. Also I didn't want to forget."
    "am" "Enjoy the rest of your day! Wanna go out to karaoke tomorrow to celebrate?"
    "mc" "Sure, I'm down for that"
    "mc" "I'll meet you for lunch tomorrow and we can discuss it more"
    "am" "Sounds like a plan!"

    time month 1 day 1 year 2016 hour 0 minute 0
    "am" "Happy new year, Melody!"
    "mc" "Happy new year, Meelz"

    time month 1 day 1 year 2017 hour 0 minute 0
    "am" "Happy birthday!"
    "am" "Nah, jokes, happy new year"
    "mc" "Almost got me."
    "am" "I am nothing if not spontaneous!"
    "mc" "You can say that again"

    time month 8 day 30 hour 7 minute 45
    "am" "Happy birthday! Felt like texting today, rather than messaging you. Wanna hang out?"
    "mc" "Oh, maybe not today, sorry, it's..."
    "mc" "I've got family visiting, so it'll be a long day."
    "am" "Ohh, the big one-eight, yeah."
    "am" "Well, let me know when, and I'll make time, 'kay?"
    "mc" "Sounds good. Sometime over next week, possibly?"
    "am" "Hell yeah!"
    "mc" "Don't you go stealing my lines too..."
    "am" "Too? Who else is stealing your identity?"
    "mc" "No, it's no-one, don't worry about it."
    "mc" "Just reminiscing."
    "am" "Okay?"
    "am" "Well, let me know if there's anything I can do to help!"
    "mc" "I will."