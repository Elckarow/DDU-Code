init -100 python hide:
    for archive in ['audio','images','fonts']:
        if not archive in config.archives:
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")


style splash_warning:
    align (0.5, 0.5)
    text_align 0.5
    size 24
    color "#000"
    font gui.default_font
    outlines []
    hyperlink_functions hyperlink_functions_style("splash_warning_hyperlink")

style splash_warning_hyperlink is splash_warning:
    hover_underline True

init -10 python in splash_message:
    from renpy.store import persistent, random, datetime, _, Text, Dissolve, DDU_multi_persistent, config

    date_messages = {
        "11/28": _("""\
Oh, geez, it's that time again. I'm a year older, you're... Older, we're both getting up in years.
Hell, if I weren't so chill, I'd probably start growing grey hairs soon! Haha!
Nah, I've got an ageless beauty, don't I? Was that a laugh?!

Amelia"""),

        "09/23": _("""\
Y- You remembered... I had no idea you thought of me so much...
Th- Thank you for coming to see me on my birthday...
Would you... Like to share some tea with me?

Yuri"""),

        "08/30": _("""\
... I don't really know how to say this, but, here goes.
You remembered my birthday, and chose to spend it with me? I... Appreciate that.
I- I appreciate you, okay? Don't... Don't make it weird.

Melody"""),

        "01/16": _("""\
Ah, another day, another year. I'm glad I'm able to spend this time with you.
It's been a wild ride, and it will continue to be just that.
Here's to another wild year with you, hey?

Aika"""),

        "02/02": _("""\
Geez, it's not like I wanted to spend time with you on my birthday, or anything.
But because you're here, I'm baking cupcakes. No, I will not take no as an answer!
You will take my cupcakes, and you will like them! Ehe~

Natsuki"""),

        "07/03": _("""\
Ehe~ You're not supposed to be here, you should be out hanging with your friends on a day like today!
Huh? Wait, is it my birthday already? And you wanted to spend it with me?
Aww, you shouldn't have...

Sayori"""),

        "09/22": _("""\
You remembered my birthday? I'm so happy.
Thank you for coming to share this moment with me.

Monika"""),
    }

    _christmas = object()
    date_messages["12/25"] = _christmas

    christmas_messages = (
        _("Merry Christmas!"),
        _("""\
Hashiresori yo
Kaze no You ni
Tsukimihara wo
PADORU PADORU"""),
    )

    _new_year = object()
    date_messages["01/01"] = _new_year

    new_year_messages = (
        _("May you be blessed with lots of nekos!"),
        _("Happy New Year!"),
        _("Amelia route coming this year *copium*")
    )

    _april_fools = object()
    date_messages["05/01"] = _april_fools

    april_fools_messages = (
        _("Check Discord..."),
        _("{a=https://www.youtube.com/watch?v=xvFZjo5PgG0}Come visit our Website!{/a}"),
    )


    splash_messages = (
        _("Gone, swept into the Undercurrents."),
        _("Just Aika."),
        _("Amelia route when?"),
        _("Tiffany sus, as always..."),
        _("Sangonomiyard Kasumilly, Divine Priestess of the Tardlilly Island."),
        _("Do it for Aika."),
        _("Ye who enter this door, abandon all hope."),
        _("""\
Because, in the end, who has more power?
A god, or the one with the source code to the universe?"""),
        _("Set this world ablaze, for it is nothing but a hollow memory of anguish."),
        _("""\
Quit? Don't quit.

Noodles? Don't noodles."""),
        _("Kneel before the almighty Neko."),
        _("Don't take it too seriously, it's just a silly and goofy mod."),
        "NullPointerException",
        _("Break a leg! And maybe a kneecap or two."),
        _("Tiffany is typing..."),
        _("Like Melody's mother, our directors ran away from home."),
        _("""\
According to a survey by the University of Michigan in 2018,
the biggest consumer globally by weight per capita of copium is currently Aika."""),
        _("Everything is daijoubu... Until the copium runs out..."),
        _("I remember when this was a short project."),
        _("monikk is watching you code."),
        _("if you're a bad kid, you won't get any coolyoris."),
        _("I'll Sayori you in a minute."),
        _("Some yuri with Yuri."),
        _("Sounds really depressing, I love it!"),
        _("Hi, if you're reading this, I need your help."),
        _("I know you. You can help us, right?"),
        _("I just want my friends to live like normal human beings."),
        _("Doki Doki!"),
        _("{a=https://undercurrentsmod.weebly.com}Come visit our Website!{/a}"),
        _("purple burglar alarm")
    )

    splash_messages_any_completed = (
        _("If it ain't suffering, it ain't us!"),
        _("""\
No Dokis were harmed in the production of this game.






Just kidding-""")
    )

    splash_messages_all_completed = (
        _("Can't find a good ending? Perhaps the archives are incomplete."),
    )

    def get_splash():
        """
        Returns a splash message. (no shit)
        """
        if not persistent.first_run: return splash_messages[0]

        date = datetime.datetime.now().strftime("%m/%d")

        if date in date_messages:
            return date_messages[date]

        messages = list(splash_messages)

        if any((persistent.sayori.completed, persistent.monika.completed, persistent.natsuki.completed, persistent.yuri.completed)):
            messages.extend(splash_messages_any_completed)
        
        if all((persistent.sayori.completed, persistent.monika.completed, persistent.natsuki.completed, persistent.yuri.completed)):
            messages.extend(splash_messages_all_completed)
        
        if all((config.version.split()[0] == "full", DDU_multi_persistent.demo1, DDU_multi_persistent.demo2)):
            messages.append(_("Completionist, much?"))
        
        if config.version.split()[0] == "demo" and DDU_multi_persistent.full_release:
            messages.extend(
                _("What are you doing playing the demo? You already have the full release!")
                for i in range(len(messages) // 3)
            )
        
        rv = random.choice(messages)

        if rv is _christmas:
            rv = random.choice(christmas_messages)
        
        elif rv is _new_year:
            rv = random.choice(new_year_messages)
        
        elif rv is _april_fools:
            rv = random.choice(april_fools_messages)

        return rv
    
    def splash_message():
        """
        Shows a splash message. (no shit)²
        """
        message = get_splash()

        if message == april_fools_messages[0]:
            renpy.sound.play("mod_assets/tomfoolery/discord.mp3")
        
        renpy.show("splash_warning", what=Text(message, style="splash_warning"))
        renpy.with_statement(Dissolve(0.485825, alpha=True))

default persistent.first_run = False

label splashscreen:
    $ custom_keymap.allowed = False
    $ config.allow_skipping = False

    if not persistent.first_run:
        $ preferences.volumes["ambient"] = DEFAULT_AMBIENT_VOLUME
        $ preferences.volumes["voice"] = DEFAULT_VOICE_VOLUME
        $ quick_menu = False
        camera master:  
            matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(-0.1)
        scene expression "mod_assets/STUFF/main_menu/main_menu_bg.png" zorder 0
        with Dissolve(1.5)
        pause 1.0
        window auto
        "[config.name!ti] is a Doki Doki Literature Club fan mod that is not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
        "Game files for DDLC are required to play this mod and can be downloaded for free at: http://ddlc.moe or from Steam."
        menu:
            "By playing [config.name!ti] you agree that you have completed DDLC."
            "I agree.":
                pass
        window hide
        camera master:
            linear 1.7 matrixcolor SaturationMatrix(1.0) * BrightnessMatrix(0.0)
        pause 3.5
        call week_0 from _call_week_0

    $ basedir = config.basedir.replace('\\', '/')

    play music config.main_menu_music

    scene white zorder 0
    with None

    show expression "mod_assets/STUFF/studiosilver.png":
        subpixel True xsize 270 fit "contain"
        align (0.5, 0.5)
    
    with Dissolve(0.5, alpha=True)
    pause 3.494817
    scene white zorder 0 with Dissolve(0.983882, alpha=True)

    $ splash_message.splash_message()

    if not persistent.first_run:
        $ persistent.first_run = True
        show text _("Click to proceed"):
            subpixel True
            anchor (1.0, 1.0) pos (0.97, 0.97)
            alpha 0.0
            block:
                easein 0.8 alpha 1.0
                easeout 0.8 alpha 0.0
                repeat
        
    $ pause()

    scene white with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    $ custom_keymap.allowed = True
    window auto
    return

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    return

label before_main_menu:
    return

label quit:
    return

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
