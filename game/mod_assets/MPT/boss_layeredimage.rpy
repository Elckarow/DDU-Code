define bossblink = CharacterBlink("mod_assets/MPT/boss/turned_eyes_d.png", "mod_assets/MPT/boss/turned_eyes_c.png")

layeredimage _boss turned:    
    group outfit:
        attribute work default null
    
    group left:
        attribute ldown default if_any "work":
            "mod_assets/MPT/boss/outfits/turned_ldown.png"

        attribute lup if_any "work":
            "mod_assets/MPT/boss/outfits/turned_lup.png"

    group right:
        attribute rdown default if_any "work":
            "mod_assets/MPT/boss/outfits/turned_rdown.png"

        attribute rup if_any "work":
            "mod_assets/MPT/boss/outfits/turned_rup.png"
    
    group apron:
        attribute apron default:
            "mod_assets/MPT/boss/outfits/turned_apron.png"
        attribute noapron null
    
    group nose:
        attribute na default null
    
    group mouth:
        attribute ma default:
            "mod_assets/MPT/boss/turned_mouth_a.png" # smiling
        attribute mb:
            "mod_assets/MPT/boss/turned_mouth_b.png" # talking + smiling
        attribute mc:
            "mod_assets/MPT/boss/turned_mouth_c.png" # wide smile ("natsuki mo")
        attribute md:
            "mod_assets/MPT/boss/turned_mouth_d.png" # closed
        attribute me:
            "mod_assets/MPT/boss/turned_mouth_e.png" # talking + neutral
        attribute mf:
            "mod_assets/MPT/boss/turned_mouth_f.png" # closed 2 (similar to "natsuki mj")

    group blink:
        attribute blink default null
        attribute noblink null

    group eyes:
        attribute ea default if_any "blink":
            bossblink("mod_assets/MPT/boss/turned_eyes_a.png") # neutral
        attribute eb if_any "blink":
            bossblink("mod_assets/MPT/boss/turned_eyes_b.png") # left
        
        attribute ea default if_not "blink":
            "mod_assets/MPT/boss/turned_eyes_a.png"
        attribute eb if_not "blink":
            "mod_assets/MPT/boss/turned_eyes_b.png"

        attribute ec:
            "mod_assets/MPT/boss/turned_eyes_c.png" # closed
        attribute ed:
            "mod_assets/MPT/boss/turned_eyes_d.png" # closed + happy

    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/boss/turned_eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/boss/turned_eyebrows_b.png" # anger
        attribute bc:
            "mod_assets/MPT/boss/turned_eyebrows_c.png" # serious

image boss turned = LayeredImageProxy("_boss turned", (renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="boss")))

image side boss turned = CharacterSideImage("_boss turned", renpy.partial(Flatten, drawable_resolution=False))