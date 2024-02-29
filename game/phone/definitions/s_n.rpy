init python:
    def get_s_n_gc_name():
        return _("Nat") if pov_key == "s" else "Sayori"

init phone register:
    define get_s_n_gc_name:
        add "s" add "n" key "s_n"
        as nat_sayor_gc
        icon ConditionSwitch(
            "pov_key =='s'", phone.asset("natsuki_icon.png"),
            "True", phone.asset("sayori_icon.png")
        ) 