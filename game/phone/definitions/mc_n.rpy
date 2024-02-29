init python:
    def get_mc_n_gc_name():
        return "Natsuki" if pov_key == "mc" else "Melody"

init phone register:
    define get_mc_n_gc_name:
        icon ConditionSwitch(
            "pov_key =='n'", phone.asset("mc_icon.png"),
            "True", phone.asset("natsuki_icon.png")
        ) 
        key "mc_n"
        add "mc" add "n" as mc_n_gc