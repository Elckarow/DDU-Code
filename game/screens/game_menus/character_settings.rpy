default persistent.amelia_seen = False
default persistent.aika_seen = False
default persistent.boss_seen = False
default persistent.ellen_seen = False
default persistent.kaito_seen = False

init -200 python:
    class CharacterSettings(object):
        def __init__(self, condition="True"):
            self._condition = renpy.python.py_compile(condition, mode="eval")
        
        @property
        def condition(self):
            return renpy.python.py_eval_bytecode(self._condition)
        
        def get_string(self, s):
            return s if self.condition else "???"
    
        def get_image(self, d):
            return Transform(d, blur=0.0, matrixcolor=IdentityMatrix()) if self.condition else CharacterSilhouette(d)
    
    melody_character_settings = CharacterSettings()
    monika_character_settings = CharacterSettings()
    natsuki_character_settings = CharacterSettings()
    yuri_character_settings = CharacterSettings()
    sayori_character_settings = CharacterSettings()
    kaito_character_settings = CharacterSettings("persistent.kaito_seen")
    ellen_character_settings = CharacterSettings("persistent.ellen_seen")
    amelia_character_settings = CharacterSettings("persistent.amelia_seen")
    boss_character_settings = CharacterSettings("persistent.boss_seen")
    aika_character_settings = CharacterSettings("persistent.aika_seen")