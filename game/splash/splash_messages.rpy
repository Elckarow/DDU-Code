init -10 python in splash_message:
    from renpy.store import persistent, random, datetime, _, Text, Dissolve, DDU_multi_persistent, config, store

    date_messages = {
        "3/10": _("""\
Another year, yet a whole lifetime ahead of us...
Maybe I can show you some of the drawings on my tablet? Or some of my older violin sheets I used to play?
However you choose to spend this day, thank you so much for at least paying me a visit.

Keiko"""),

        "11/28": _("""\
Oh, geez, it's that time again. I'm a year older, you're... older, we're both getting up in years.
Hell, if I weren't so chill, I'd probably start growing grey hairs soon! Haha!
Nah, I've got an ageless beauty, don't I? Was that a laugh?!

Amelia"""),

        "09/23": _("""\
Y- You remembered... I had no idea you thought of me so much...
Th- Thank you for coming to see me on my birthday...
Would you... like to share some tea with me?

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

    default_splash_message = _("Gone, swept into the Undercurrents.")

    splash_messages = (
        default_splash_message,
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
        "NullPointerException",
        _("Break a leg! And maybe a kneecap or two."),
        _("Tiffany is typing..."),
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
        _("{a=https://dokidokiundercurrents.com}Come visit our Website!{/a}"),
        _("Like alcoholism, but less productive"),
        _("Welp, there go the Lemmings!"),
        _("Not the Lemmings!"),
        _("Colonel Sanders Berating Simulator"),
        _("In at Number 9: The Tories with Party Rock"),
        _("Ass Whooping in a Parking Lot (Gone Danny)"),
        _("Calling my ex AT 3 A.M! (Gone Wrong!!!!!)"),
        _("You hurt Jack White's feelings"),
        _("Orchestra not included"),
        _("Help I'm trapped in a Splash Text Factory"),
        _("Monika route when?"),
        _("i sayor"),
        _("This turn ain't big enough for the both of us..."),
        _("AAAH THE BONES"),
        _("Don't."),
        _("Noodles are great"),
        _("Also try Blue Skies!"),
        _("Playtesters are like kiwis"),
        _("Chicken nugget"),
        _("Sometimes we have the problem when we take the path to avoid it."),
        _("lilly has brain damage. please help her"),
        _("My snake is really good at printing. He's a python"),
        _("Putting the butt into butter"),
        _("""\
NFT? What does it stand for? 

Does it stand for NEKO FLAP TIME???"""),
        _("""\
Simp for Foxian Beauties today!
Only at the Xianshou Luofu!"""),
        _("""\
All warfare is based
- Sun Tzu"""),
        _("""\
anger? widenekoflap
embarrassment? widenekoflap
happiness? widenekoflap
depression? widenekoflap
anxiety? widenekoflap"""),
        _("""\
the pen is mightier than the sword. 

if you give your pen sharpness 5, that is"""),
        _("Industrial Strength Raid: Now for Bugs and Beas"),
        _("Mangos do not belong in the toaster"),
        "world.execute(mc);",
        _("TardLilly, as usual."),
        _("Osoi! Yowai!"),
        _("loved it when haicma said \"it's revelation time\" and started revelating all over the radiant marcher"),
        _("It's never Lupus..."),
        """\
SOMETIMES
I THINK YOU WILL FOLLOW MY PACE
TO THE END OF THE WORLD
EVERY TIME
EVERY TIME YOU GO AWAY
I'M CHASING YOU
YOU ARE MY REVELATION""",
        _("Man, a watermelon!"),
        _("The potato should go in the front."),
        _("Don't choke on your WcChicken!"),
        _("Daga otoko da."),
        _("U.N.Owen was Ronald?"),
        _("""\
Lilly is trying to see
Please wait warmly
"""),
        _("Stuff count: [persistent.stuff]"),
        _("""\
Do you see how things change?
You used to be my flame."""),
        """\
YOKOSO
KIRAKIRA DOKIDOKI
MOCHIMOCHI PUYOPUYO
WAKUWAKU WASHOI
WANDAESTEIYEI""",
        _("Levy never fails to talk about chess."),
        _("You're in control, rid of the monsters inside your head.")
)

    splash_messages_none_completed = (
        _("Don't take it too seriously, it's just a silly and goofy mod."),
    )

    splash_messages_any_completed = (
        _("If it ain't suffering, it ain't us!"),
        _("Like Melody's mother, our directors ran away from home."),
        _("Oops."),
        _("""\
This mod is for educational purposes only. 

Please do not repeat any actions shown in the game without guidance from a trained professional."""),
        _("""\
No Dokis were harmed in the production of this game.






Just kidding-"""),
        _("A slice of life game isn't completely without someone's life getting sliced."),
        _("Subway Surfers not included."),
    )

    splash_messages_all_completed = (
        _("Can't find a good ending? Perhaps the archives are incomplete."),
    )

    splash_messages_sayori_not_completed = (
        _("Sayori's parents arent home! arent you interested?"),
    )

    splash_messages_sayori_completed = (
        _("Okay, it's like a minute or two. That's not that long."),
    )

    splash_messages_natsuki_not_completed = (
        
    )

    splash_messages_natsuki_completed = (
        _("Cupcake frostings not included"),
    )

    splash_messages_yuri_not_completed = (
        _("Google Yuri for route advice"),
    )

    splash_messages_yuri_completed = (
    )

    splash_messages_monika_not_completed = (
    )

    splash_messages_monika_completed = (
    )

    splash_messages_ending_reached = (
    )

    def get_splash():
        """
        Returns a splash message. (no shit)
        """
        if not persistent.tos: return default_splash_message

        date = datetime.datetime.now().strftime("%m/%d")

        if date in date_messages:
            rv = date_messages[date]

        else:
            messages = list(splash_messages)

            if any((persistent.sayori.completed, persistent.monika.completed, persistent.natsuki.completed, persistent.yuri.completed)):
                messages.extend(splash_messages_any_completed)
            else:
                messages.extend(splash_messages_none_completed)
        
            if all((persistent.sayori.completed, persistent.monika.completed, persistent.natsuki.completed, persistent.yuri.completed)):
                messages.extend(splash_messages_all_completed)
        
            if persistent.sayori.completed:
                messages.extend(splash_messages_sayori_completed)
            else:
                messages.extend(splash_messages_sayori_not_completed)
        
            if persistent.natsuki.completed:
                messages.extend(splash_messages_natsuki_completed)
            else:
                messages.extend(splash_messages_natsuki_not_completed)
        
            if persistent.yuri.completed:
                messages.extend(splash_messages_yuri_completed)
            else:
                messages.extend(splash_messages_yuri_not_completed)
        
            if persistent.monika.completed:
                messages.extend(splash_messages_monika_completed)
            else:
                messages.extend(splash_messages_monika_not_completed)
        
            if all((config.version.split()[0] == "full", DDU_multi_persistent.demo1, DDU_multi_persistent.demo2)):
                messages.append(_("Completionist, much?"))
        
            if persistent.end:
                messages.extend(splash_messages_ending_reached)
        
            if config.version.split()[0] == "demo" and DDU_multi_persistent.full_release:
                messages.extend(
                    _("What are you doing playing the demo? You already have the full release!")
                    for _i in range(len(messages) // 3)
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
        renpy.with_statement(Dissolve(0.485825))

style splash_warning:
    align (0.5, 0.5)
    text_align 0.5
    size 24
    color "#000"
    font gui.default_font
    outlines []
    hyperlink_functions hyperlink_functions_style("splash_warning_hyperlink")

style splash_warning_hyperlink is splash_warning:
    underline True