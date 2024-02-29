init python:
    def get_mc_y_gc_name():
        return "Yuri" if pov_key == "mc" else "MC"

init phone register:
    define get_mc_y_gc_name:
        icon ConditionSwitch(
            "pov_key =='y'", phone.asset("mc_icon.png"),
            "True", phone.asset("yuri_icon.png")
        ) 
        key "mc_y"
        add "mc" add "y" as mc_y_gc