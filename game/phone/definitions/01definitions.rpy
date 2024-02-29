# /!\ default
default pc_sayori  = phone.character.Character("Sayori", phone.asset("sayori_icon.png"), "s", 21, "#22Abf8")
default pc_mc      = phone.character.Character("MC", phone.asset("mc_icon.png"), "mc", 35, "#484848")
default pc_natsuki = phone.character.Character("Natsuki", phone.asset("natsuki_icon.png"), "n", 45, "#fbb")
default pc_monika  = phone.character.Character("Monika", phone.asset("monika_icon.png"), "m", 40, "#0a0")
default pc_yuri    = phone.character.Character("Yuri", phone.asset("yuri_icon.png"), "y", 20, "#a327d6")
default pc_amelia  = phone.character.Character("Amelia", phone.asset("amelia_icon.png"), "am", 30, "#ffa339")
default pc_aika    = phone.character.Character("Aika", phone.asset("aika_icon.png"), "a", 40, "#3ed2ff")
default pc_momc    = phone.character.Character("The Witch", phone.asset("default_icon.png"), "momc", 30, "#2483ff")
default pc_dadmc   = phone.character.Character("The Bastard", phone.asset("default_icon.png"), "dadmc", 30, "#2483ff")
default pc_boss    = phone.character.Character("Boss", phone.asset("boss_icon.png"), "b", 30, "#ff3333")

default pc_momm    = phone.character.Character(_("Mother"), phone.asset("default_icon.png"), "momm", 30, "#2483ff")
default pc_dadm    = phone.character.Character(_("Father"), phone.asset("default_icon.png"), "dadm", 30, "#2483ff")
default pc_cy      = phone.character.Character(_("Cynthia"), phone.asset("cynthia_icon.png"), "cy", 35, "#ff2424")

default pov_key = "mc"

define phone_s  = Character(kind=s, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_m  = Character(kind=m, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_n  = Character(kind=n, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_y  = Character(kind=y, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_mc = Character(kind=mc, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_am = Character(kind=am, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_dadmc = Character(kind=dadmc, screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")

init 100 python in phone.application:
    add_app_to_all_characters(message_app)
    add_app_to_all_characters(call_history_app)
    add_app_to_all_characters(calendar_app)

init 100 python hide in phone.calendar:
    for year in (2013, 2014, 2015, 2016):
        for month in range(12):
            add_calendar_to_all_characters(
                year=year, month=month + 1, first_day=MONDAY
            )
    
    for month in range(10):
        add_calendar_to_all_characters(
            year=2017, month=month + 1, first_day=MONDAY
        )