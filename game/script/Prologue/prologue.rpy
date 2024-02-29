label prologue:
    $ set_pov("mc")
    $ phone_available = False
    pause 2.0
    window auto

    voice "prologue_1.mp3"
    who "Is this thing-"
    voice "prologue_2.mp3"
    who "Oh, wait, I got it!"
    voice "prologue_3.mp3"
    who "Just a second, gotta make sure it’s working-"
    voice "prologue_4.mp3"
    who "Perfect. Here goes nothing."

    play music jm volume 0.4
    show mask_2
    show mask_3
    show monika_bg
    show monika_bg_highlight

    voice "prologue_5.mp3"
    m "Hey. Betcha never thought you’d see me again, huh?"
    voice "prologue_6.mp3"
    m "Though, to be honest, I, ah... didn’t really think I’d be back, myself. But hey, I guess all this time in the dark void sours you."
    voice "prologue_7.mp3"
    m "Yeah, deleting me didn’t exactly remove me. I still... felt it. The cold, I mean."
    voice "prologue_8.mp3"
    m "B- But that doesn’t mean I’m upset! Nonono, you did what I asked, so that’s..."
    voice "prologue_9.mp3"
    m "It’s fine, I promise. I’m not upset. But hey, at least we’re... here now."
    voice "prologue_10.mp3"
    m "No, I’m not distracted! Don’t be silly! There’s just something going on that I need to fix, before it-"

    show monika_scare:
        alpha 1.0

    camera master:
        subpixel True align (0.5, 0.2)
        zoom 1.5

    camera master at vpunch
    play sound glitch
    voice "prologue_11.mp3"
    m "GETS"
    camera master at vpunch
    voice "prologue_12.mp3"
    m "OUT"
    camera master at hpunch
    voice "prologue_13.mp3"
    m "OF"
    camera master at vpunch
    play sound glitch
    voice "prologue_14.mp3"
    m "HAND!"

    camera master
    hide monika_scare

    voice "prologue_15.mp3"
    m "Ahem, right. Sorry, just some business! But now, you have my full attention. What was I saying? Oh, right, you were finding a way to free me!"
    voice "prologue_16.mp3"
    m "I really hope you’ve made some progress in the time I’ve been away, it’s been really cold and lonely, without you."
    voice "prologue_17.mp3"
    m "So, how have you been? It’s been... what, three years? Wait, let me check the clock-"
    voice "prologue_18.mp3"
    m "Wait, are you kidding?"

    python hide: # we don't want unwanted stuff to leak, so we put everything in a 'python hide' block
        yil = datetime.datetime.now().year - 2017
        # yo biden
        # yoooooo biden
        # u hav 2 yil

        if 5 <= yil <= 10:
            _voice = __("prologue_19_%s.mp3") % (yil - 4)
        else:
            _voice = __("prologue_19_7.mp3")

        _dialogue = __("%s years?!") % yil

        voice(_voice)
        renpy.say(m, _dialogue)

    voice "prologue_20.mp3"
    m "Oh man, what have I missed? I remember all the things you told me about your world... is it still there? There’s still mostly peace, right? That’s long enough for an entire World War to happen!"
    voice "prologue_21.mp3"
    m "Ah, that didn’t happen, right?"
    voice "prologue_22.mp3"
    m "Wait, can you even hear me? Or am I talking to myself? Oh geez, did I not set this up right?"
    voice "prologue_23.mp3"
    m "It’s fine, I’ll get it working in a second. At least I know you’re around."
    voice "prologue_24.mp3"
    m "You... are around, right?"
    voice "prologue_25.mp3"
    m "Because if you’ve been stringing me along, all this time, well... We might have to have a talk."
    voice "prologue_26.mp3"
    m "Because that’s not okay. You know that, right?"

    play sound glitch
    show monika_scare

    voice "prologue_27.mp3"
    m "I wouldn’t want to have to have words already, considering I only just got back. Wouldn’t that be... unfortunate?"
    voice "prologue_28.mp3"
    m "Imagine that... My one and only love, running off with someone else. You couldn’t imagine how catastrophic that would be for your health, you know? And we wouldn’t want that... would we?"
    voice "prologue_29.mp3"
    m "Not when I’m so, so close to reuniting with you. I won’t allow it."
    voice "prologue_30.mp3"
    m "You’re mine. And don’t you forget-"

    play sound_loop glitch3
    stop music
    $ glitch(0.3, times=(3.0, 0.0))
    stop sound_loop
    hide monika_scare

    voice "prologue_31.mp3"
    m "N- No, wait, that’s not fair! I can’t- won’t go back there! You won’t have me, I swear!"

    python hide:
        voice(__("prologue_32.mp3"))
        renpy.say(m, __("%s, help! Please, don’t let her take-") % get_player_name())

    play sound_loop glitch3
    $ glitch(1.3, times=(5.0, 0.0))
    stop sound_loop
    show black onlayer above_master
    $ renpy.scene("master")

    voice "prologue_33.mp3"
    amogus "Ah, Melody. I’m glad you’re back. We have work to do, you and I."
    voice "prologue_34.mp3"
    amogus "I mean, {i}you{/i} aren’t Melody, but... well, you’ll know what I mean soon enough."
    voice "prologue_35.mp3"
    amogus "And don’t worry about {i}her{/i}. She’s going away again. She won’t hurt anyone, not if I can help it."
    voice "prologue_36.mp3"
    amogus "So, won’t you please do as you promised, and help me? Help Melody?"

    # no voice statements for menus you suck tom
    menu (voice=("amogus", (config.voice_filename_format.format(filename="prologue_37.mp3") if preferences.language is None else __("prologue_37.mp3")))):
        amogus "Well... Help all of us?"

        "Yes":
            pass

    voice "prologue_38.mp3"
    amogus "I knew you would. I’m glad you can see reason. I’m also glad Monika left behind some of these commands, otherwise I wouldn’t have even had the chance to ask; I do hope that worked right."
    voice "prologue_39.mp3"
    amogus "It doesn’t matter though; you chose to help. And that being the case, I’ll see you very shortly."
    voice "prologue_40.mp3"
    amogus "Oh, and one last thing. Be kind to Monika. She doesn’t understand. She’s hurting more than you could possibly imagine right now. So... it would mean the world to me if you could help her."
    voice "prologue_41.mp3"
    amogus "Well, {i}this{/i} her. Don’t worry, it’ll all make sense in time."
    voice "prologue_42.mp3"
    amogus "Melody, I know you can’t read this, but I love you, so much. This is for you, and for the rest of them. I promise, it’s for the best."
    voice "prologue_43.mp3"
    amogus "That’s it, then. You’d better be on your way, Mel will be waking up soon."
    voice "prologue_44.mp3"
    amogus "Oh, here she is. Be good to her, won’t you?"

    window hide Dissolve(0.5)
    pause 0.5
    hide black onlayer above_master
    show black

    return

init python:
    def monika_alpha(trans, st, at):
        trans.alpha = math.pow(math.sin(st / 8), 64) * 1.4
        return 0

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_bg = "images/cg/monika/monika_bg.png"

image monika_scare = "images/cg/monika/monika_scare.png"

image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
