define aikablink = CharacterBlink("mod_assets/MPT/aika/turned_eyes_c.png", "mod_assets/MPT/aika/turned_eyes_b.png")

layeredimage _aika turned:
    always "mod_assets/MPT/aika/turned_facebase.png"

    group outfit:
        attribute uniform default null

    group left:
        attribute ldown default if_any "uniform":
            "mod_assets/MPT/aika/outfits/turned_uniform_ldown.png"

        attribute lpoint if_any "uniform":
            "mod_assets/MPT/aika/outfits/turned_uniform_lpoint.png"
    
    group right:
        attribute rdown default if_any "uniform":
            "mod_assets/MPT/aika/outfits/turned_uniform_rdown.png"
        
        attribute rhip if_any "uniform":
            "mod_assets/MPT/aika/outfits/turned_uniform_rhip.png"

    group nose: 
        attribute na default null
        attribute nb:
            "mod_assets/MPT/aika/turned_nose_b.png" # sweat drop
        attribute nc:
            "mod_assets/MPT/aika/turned_nose_c.png" # blush
        attribute nd:
            "mod_assets/MPT/aika/turned_nose_d.png" # blush + sweat drop
        attribute ne:
            "mod_assets/MPT/aika/turned_nose_e.png" # big blush 
        attribute nf:
            "mod_assets/MPT/aika/turned_nose_f.png" # big blush + sweat drop

    group mouth:
        attribute ma default:
            "mod_assets/MPT/aika/turned_mouth_a.png" # smile
        attribute mb:
            "mod_assets/MPT/aika/turned_mouth_b.png" # talking + smile
        attribute mc:
            "mod_assets/MPT/aika/turned_mouth_c.png" # talking + big smile
        attribute md:
            "mod_assets/MPT/aika/turned_mouth_d.png" # grin
        attribute me:
            "mod_assets/MPT/aika/turned_mouth_e.png" # closed
        attribute mf:
            "mod_assets/MPT/aika/turned_mouth_f.png" # slightly open
        attribute mg:
            "mod_assets/MPT/aika/turned_mouth_g.png" # embarassed
        attribute mh:
            "mod_assets/MPT/aika/turned_mouth_h.png" # mad

    group eyes:
        attribute ea default if_any "blink":
            aikablink("mod_assets/MPT/aika/turned_eyes_a.png") # neutral
        attribute ed if_any "blink":
            aikablink("mod_assets/MPT/aika/turned_eyes_d.png") # left

        attribute ea default if_not "blink":
            "mod_assets/MPT/aika/turned_eyes_a.png"
        attribute ed if_not "blink":
            "mod_assets/MPT/aika/turned_eyes_d.png"  

        attribute eb:
            "mod_assets/MPT/aika/turned_eyes_b.png" # closed
        attribute ec:
            "mod_assets/MPT/aika/turned_eyes_c.png" # closed + happy
    
    group eyebrow:
        attribute ba default:
            "mod_assets/MPT/aika/turned_eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/aika/turned_eyebrows_b.png" # raised
        attribute bc:
            "mod_assets/MPT/aika/turned_eyebrows_c.png" # worried
        attribute bd:
            "mod_assets/MPT/aika/turned_eyebrows_d.png" # mad
    
    group head:
        attribute clip default:
            "mod_assets/MPT/aika/turned_head_clip.png"
        attribute cap:
            "mod_assets/MPT/aika/turned_head_cap.png"
        attribute noclip null

    group blink:
        attribute blink default null
        attribute noblink null 

layeredimage _aika smug:    
    always "mod_assets/MPT/aika/smug_facebase.png"

    group center:
        attribute uniform default:
            "mod_assets/MPT/aika/outfits/smug_uniform.png"

    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/aika/smug_nose_b.png" # blush

    group mouth:
        attribute ma default:
            "mod_assets/MPT/aika/smug_mouth_a.png" # smile
        attribute mb:
            "mod_assets/MPT/aika/smug_mouth_b.png" # talking + smile
    
    group eyes:
        attribute ea default:
            "mod_assets/MPT/aika/smug_eyes_a.png" # neutral

    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/aika/smug_eyebrows_a.png" # neutral

    group head:
        attribute clip default:
            "mod_assets/MPT/aika/smug_head_clip.png"
        attribute cap:
            "mod_assets/MPT/aika/smug_head_cap.png"
        attribute noclip null
    
    group blink:
        attribute blink default null
        attribute noblink null


image aika turned = LayeredImageProxy("_aika turned", (renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="aika")))
image aika smug = LayeredImageProxy("_aika smug", (renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="aika")))

image side aika turned = CharacterSideImage("_aika turned", renpy.partial(Flatten, drawable_resolution=False))
image side aika smug = CharacterSideImage("_aika smug", renpy.partial(Flatten, drawable_resolution=False))