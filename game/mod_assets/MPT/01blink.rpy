init python:
    class CharacterBlink(object):
        def __init__(self, blink_a, blink_b):
            self.blink_a = blink_a
            self.blink_b = blink_b
        
        def __call__(self, eyes, **kwargs):
            kwargs.update({"blink_a": self.blink_a, "blink_b": self.blink_b})
            return ConditionSwitch(
                "persistent.character_blink", _character_blink(eyes, **kwargs),
                "True", eyes
            )
    
    FixedFitFirst = renpy.partial(Fixed, fit_first=True)

transform _character_blink(eyes, blink_a, blink_b, pause_interval=(20, 100)):
    eyes
    # min(max(renpy.random.randint(*pause_interval) * 0.1, 1.0), 3.0)
    renpy.random.randint(*pause_interval) * 0.1
    choice:
        blink_a
        0.015
        blink_b
        0.035
        blink_a
        0.015
    choice:
        blink_a
        0.015
        blink_b
        0.065
        blink_a
        0.015
    choice:
        blink_a
        0.015
        blink_b
        0.095
        blink_a
        0.015
    choice:
        blink_a
        0.015
        blink_b
        0.035
        blink_a
        0.015
        eyes
        0.15 
        blink_a
        0.015
        blink_b
        0.035
        blink_a
        0.015
    repeat