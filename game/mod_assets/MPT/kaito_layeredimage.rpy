define kaitoblink = CharacterBlink("mod_assets/MPT/kaito/turned_eyes_f.png", "mod_assets/MPT/kaito/turned_eyes_e.png")

layeredimage _kaito turned:
    always "mod_assets/MPT/kaito/turned_facebase.png"

    group outfits:
        attribute uniform default null
    
    group left:
        attribute ldown default if_any "uniform":
            "mod_assets/MPT/kaito/outfits/turned_uniform_ldown.png"
        
        attribute lup if_any "uniform":
            "mod_assets/MPT/kaito/outfits/turned_uniform_lup.png"
    
    group right:
        attribute rdown default if_any "uniform":
            "mod_assets/MPT/kaito/outfits/turned_uniform_rdown.png"
        
        attribute rhip if_any "uniform":
            "mod_assets/MPT/kaito/outfits/turned_uniform_rhip.png"
    
    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/kaito/turned_nose_b.png"
    
    group mouth:
        attribute ma default:
            "mod_assets/MPT/kaito/turned_mouth_a.png" # smiling
        attribute mb:
            "mod_assets/MPT/kaito/turned_mouth_b.png" # grin
        attribute mc:
            "mod_assets/MPT/kaito/turned_mouth_c.png" # talking + big grin
        attribute md:
            "mod_assets/MPT/kaito/turned_mouth_d.png" # closed
        attribute me:
            "mod_assets/MPT/kaito/turned_mouth_e.png" # talking + neutral
        attribute mf:
            "mod_assets/MPT/kaito/turned_mouth_f.png" # talking + neutral 2
        attribute mg:
            "mod_assets/MPT/kaito/turned_mouth_g.png" # :(
        attribute mh:
            "mod_assets/MPT/kaito/turned_mouth_h.png" # mad (cuz bad)
    
    group blink:
        attribute blink default null
        attribute noblink null

    group eyes:
        attribute ea default if_any "blink":
            kaitoblink("mod_assets/MPT/kaito/turned_eyes_a.png") # neutral
        attribute eb if_any "blink":
            kaitoblink("mod_assets/MPT/kaito/turned_eyes_b.png") # surprised
        attribute ec if_any "blink":
            kaitoblink("mod_assets/MPT/kaito/turned_eyes_c.png") # frowning
        attribute ed if_any "blink":
            kaitoblink("mod_assets/MPT/kaito/turned_eyes_d.png") # crazy
        
        attribute ea default if_not "blink":
            "mod_assets/MPT/kaito/turned_eyes_a.png" 
        attribute eb if_not "blink":
            "mod_assets/MPT/kaito/turned_eyes_b.png" 
        attribute ec if_not "blink":
            "mod_assets/MPT/kaito/turned_eyes_c.png" 
        attribute ed if_not "blink":
            "mod_assets/MPT/kaito/turned_eyes_d.png" 

        attribute ee:
            "mod_assets/MPT/kaito/turned_eyes_e.png" # closed
        attribute ef:
            "mod_assets/MPT/kaito/turned_eyes_f.png" # closed + happy
        
        # # same as above but teary
        # attribute e2a:
        #     "mod_assets/MPT/kaito/turned_eyes_2a.png"
        # attribute e2b:
        #     "mod_assets/MPT/kaito/turned_eyes_2b.png"
        # attribute e2c:
        #     "mod_assets/MPT/kaito/turned_eyes_2c.png"
        # attribute e2d:
        #     "mod_assets/MPT/kaito/turned_eyes_2d.png"
        # attribute e2e:
        #     "mod_assets/MPT/kaito/turned_eyes_2e.png"
        # attribute e2f:
        #     "mod_assets/MPT/kaito/turned_eyes_2f.png"
    
        # # same as above but crying his eyes out
        # attribute e3a:
        #     "mod_assets/MPT/kaito/turned_eyes_3a.png"
        # attribute e3b:
        #     "mod_assets/MPT/kaito/turned_eyes_3b.png"
        # attribute e3c:
        #     "mod_assets/MPT/kaito/turned_eyes_3c.png"
        # attribute e3d:
        #     "mod_assets/MPT/kaito/turned_eyes_3d.png"
        # attribute e3e:
        #     "mod_assets/MPT/kaito/turned_eyes_3e.png"
        # attribute e3f:
        #     "mod_assets/MPT/kaito/turned_eyes_3f.png"

    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/kaito/turned_eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/kaito/turned_eyebrows_b.png" # surprised 1
        attribute bc:
            "mod_assets/MPT/kaito/turned_eyebrows_c.png" # surprised 2
        attribute bd:
            "mod_assets/MPT/kaito/turned_eyebrows_d.png" # worried 1
        attribute be:
            "mod_assets/MPT/kaito/turned_eyebrows_e.png" # worried 2
        attribute bf:
            "mod_assets/MPT/kaito/turned_eyebrows_f.png" # worried 3
        attribute bg:
            "mod_assets/MPT/kaito/turned_eyebrows_g.png" # serious
        attribute bh:
            "mod_assets/MPT/kaito/turned_eyebrows_h.png" # kinda mad
        attribute bi:
            "mod_assets/MPT/kaito/turned_eyebrows_i.png" # anger

image kaito turned = LayeredImageProxy("_kaito turned", (renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="kaito")))

image side kaito turned = CharacterSideImage("_kaito turned", renpy.partial(Flatten, drawable_resolution=False))