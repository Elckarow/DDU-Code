init python:
    def get_mc_m_gc_name():
        return "Monika" if pov_key == "mc" else "MC"

init phone register:
    define get_mc_m_gc_name:
        icon ConditionSwitch(
            "pov_key =='m'", phone.asset("mc_icon.png"),
            "True", phone.asset("monika_icon.png")
        ) key "mc_m"
        add "mc" add "m" as mc_m_gc