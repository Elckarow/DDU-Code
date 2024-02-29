define ameliablink = CharacterBlink("mod_assets/MPT/amelia/turned_eyes_f.png", "mod_assets/MPT/amelia/turned_eyes_e.png")

layeredimage _amelia turned:    
    group facebase:
        attribute downtail default:
            "mod_assets/MPT/amelia/turned_facebase_downtail.png"
        attribute ponytail:
            "mod_assets/MPT/amelia/turned_facebase_ponytail.png"
        attribute hairdown:
            "mod_assets/MPT/amelia/turned_facebase_hairdown.png"
    
    group outfit:
        attribute uniform default null
        attribute casual null
    
    group left:
        attribute ldown default if_any "uniform":
            "mod_assets/MPT/amelia/outfits/turned_uniform_ldown.png"
        attribute ldown default if_any "casual":
            "mod_assets/MPT/amelia/outfits/turned_casual_ldown.png"

        attribute lup if_any "uniform":
            "mod_assets/MPT/amelia/outfits/turned_uniform_lup.png"
        attribute lup if_any "casual":
            "mod_assets/MPT/amelia/outfits/turned_casual_lup.png"
        
        attribute lpocket if_any "casual":
            "mod_assets/MPT/amelia/outfits/turned_casual_lpocket.png"

    group right:
        attribute rdown default if_any "uniform":
            "mod_assets/MPT/amelia/outfits/turned_uniform_rdown.png"
        attribute rdown default if_any "casual":
            "mod_assets/MPT/amelia/outfits/turned_casual_rdown.png"

        attribute rup if_any "uniform":
            "mod_assets/MPT/amelia/outfits/turned_uniform_rup.png"
        attribute rup if_any "casual":
            "mod_assets/MPT/amelia/outfits/turned_casual_rup.png"
        
        attribute rpocket if_any "casual":
            "mod_assets/MPT/amelia/outfits/turned_casual_rpocket.png"
    
    group nose:
        attribute na default null
    
    group mouth:
        attribute ma default:
            "mod_assets/MPT/amelia/turned_mouth_a.png" # smiling
        attribute mb:
            "mod_assets/MPT/amelia/turned_mouth_b.png" # talking + smiling
        attribute mc:
            "mod_assets/MPT/amelia/turned_mouth_c.png" # slight grin / pouting
        attribute md:
            "mod_assets/MPT/amelia/turned_mouth_d.png" # closed
        attribute me:
            "mod_assets/MPT/amelia/turned_mouth_e.png" # talking + neutral
        attribute mf:
            "mod_assets/MPT/amelia/turned_mouth_f.png" # talking 2 (similar to "natsuki mi")
        attribute mg:
            "mod_assets/MPT/amelia/turned_mouth_g.png" # closed 2 ("natsuki mj")
        attribute mh:
            "mod_assets/MPT/amelia/turned_mouth_h.png" # talking 3
        attribute mi:
            "mod_assets/MPT/amelia/turned_mouth_i.png" # embarassed
        attribute mj:
            "mod_assets/MPT/amelia/turned_mouth_j.png" # embarassed 2 / scared
        attribute mk:
            "mod_assets/MPT/amelia/turned_mouth_k.png" # yelling
    
    group blink:
        attribute blink default null
        attribute noblink null

    group eyes:
        attribute ea default if_any "blink":
            ameliablink("mod_assets/MPT/amelia/turned_eyes_a.png") # neutral
        attribute eb if_any "blink":
            ameliablink("mod_assets/MPT/amelia/turned_eyes_b.png") # surprised
        attribute ec if_any "blink":
            ameliablink("mod_assets/MPT/amelia/turned_eyes_c.png") # frowning
        attribute ed if_any "blink":
            ameliablink("mod_assets/MPT/amelia/turned_eyes_d.png") # left
        attribute eg if_any "blink":
            ameliablink("mod_assets/MPT/amelia/turned_eyes_g.png") # scared
        
        attribute ea default if_not "blink":
            "mod_assets/MPT/amelia/turned_eyes_a.png"
        attribute eb if_not "blink":
            "mod_assets/MPT/amelia/turned_eyes_b.png"
        attribute ec if_not "blink":
            "mod_assets/MPT/amelia/turned_eyes_c.png"
        attribute ed if_not "blink":
            "mod_assets/MPT/amelia/turned_eyes_d.png"
        attribute eg if_not "blink":
            "mod_assets/MPT/amelia/turned_eyes_g.png"

        attribute ee:
            "mod_assets/MPT/amelia/turned_eyes_e.png" # closed
        attribute ef:
            "mod_assets/MPT/amelia/turned_eyes_f.png" # closed + happy
    
    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/amelia/turned_eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/amelia/turned_eyebrows_b.png" # surprised
        attribute bc:
            "mod_assets/MPT/amelia/turned_eyebrows_c.png" # worried 1
        attribute bd:
            "mod_assets/MPT/amelia/turned_eyebrows_d.png" # worried 2
        attribute be:
            "mod_assets/MPT/amelia/turned_eyebrows_e.png" # worried 3
        attribute bf:
            "mod_assets/MPT/amelia/turned_eyebrows_f.png" # the rock 1
        attribute bg:
            "mod_assets/MPT/amelia/turned_eyebrows_g.png" # the rock 2
        attribute bh:
            "mod_assets/MPT/amelia/turned_eyebrows_h.png" # anger 1
        attribute bi:
            "mod_assets/MPT/amelia/turned_eyebrows_i.png" # anger 2

image amelia turned = LayeredImageProxy("_amelia turned", (renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="amelia")))

image side amelia turned = CharacterSideImage("_amelia turned", renpy.partial(Flatten, drawable_resolution=False))