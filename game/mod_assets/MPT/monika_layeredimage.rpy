define monikablinkturned = CharacterBlink("mod_assets/MPT/monika/turned_eyes_d.png", "mod_assets/MPT/monika/turned_eyes_c.png")

layeredimage _monika turned:    
    always "mod_assets/MPT/monika/turned_facebase.png"
    
    group outfit:
        attribute uniform default null
        attribute casual null
        attribute dress null
        attribute suit null

        attribute coat_uniform null
        attribute coat_casual null
        attribute coat_dress null
        attribute coat_suit null
    
    group left:
        attribute ldown default if_any "uniform":
            "mod_assets/MPT/monika/outfits/turned_uniform_ldown.png"
        attribute ldown default if_any "casual":
            "mod_assets/MPT/monika/outfits/turned_casual_ldown.png"
        attribute ldown default if_any "dress":
            "mod_assets/MPT/monika/outfits/turned_dress_ldown.png"
        attribute ldown default if_any "suit":
            "mod_assets/MPT/monika/outfits/turned_suit_ldown.png"
        attribute ldown default if_any ["coat_uniform", "coat_casual", "coat_dress", "coat_suit"]:
            "mod_assets/MPT/monika/outfits/turned_coat_ldown.png"

        attribute lpoint if_any "uniform":
            "mod_assets/MPT/monika/outfits/turned_uniform_lpoint.png"
        attribute lpoint if_any "casual":
            "mod_assets/MPT/monika/outfits/turned_casual_lpoint.png"
        attribute lpoint if_any "dress":
            "mod_assets/MPT/monika/outfits/turned_dress_lpoint.png"
        attribute lpoint if_any "suit":
            "mod_assets/MPT/monika/outfits/turned_suit_lpoint.png"
        attribute lpoint if_any ["coat_uniform", "coat_casual", "coat_dress", "coat_suit"]:
            "mod_assets/MPT/monika/outfits/turned_coat_lpoint.png"
    
    group right:
        attribute rdown default if_any "uniform":
            "mod_assets/MPT/monika/outfits/turned_uniform_rdown.png"
        attribute rdown default if_any "casual":
            "mod_assets/MPT/monika/outfits/turned_casual_rdown.png"
        attribute rdown default if_any "dress":
            "mod_assets/MPT/monika/outfits/turned_dress_rdown.png"
        attribute rdown default if_any "suit":
            "mod_assets/MPT/monika/outfits/turned_suit_rdown.png"
        attribute rdown default if_any ["coat_uniform", "coat_casual", "coat_dress", "coat_suit"]:
            "mod_assets/MPT/monika/outfits/turned_coat_rdown.png"
        
        attribute rhip if_any "uniform":
            "mod_assets/MPT/monika/outfits/turned_uniform_rhip.png"
        attribute rhip if_any "casual":
            "mod_assets/MPT/monika/outfits/turned_casual_rhip.png"
        attribute rhip if_any "dress":
            "mod_assets/MPT/monika/outfits/turned_dress_rhip.png"
        attribute rhip if_any "suit":
            "mod_assets/MPT/monika/outfits/turned_suit_rhip.png"
        attribute rhip if_any ["coat_uniform", "coat_casual", "coat_dress", "coat_suit"]:
            "mod_assets/MPT/monika/outfits/turned_coat_rhip.png"
    
    always "mod_assets/MPT/monika/outfits/turned_coat_other_uniform.png" if_any "coat_uniform"
    always "mod_assets/MPT/monika/outfits/turned_coat_other_casual.png" if_any "coat_casual"
    always "mod_assets/MPT/monika/outfits/turned_coat_other_suit.png" if_any "coat_suit"
    
    group bow:
        attribute bow default:
            "mod_assets/MPT/monika/turned_bow.png"
        attribute nobow null
    
    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/monika/turned_nose_b.png"  
    
    group mouth:
        attribute ma default:
            "mod_assets/MPT/monika/turned_mouth_a.png" # smiling
        attribute mb:        
            "mod_assets/MPT/monika/turned_mouth_b.png" # talking + smiling
        attribute mc:        
            "mod_assets/MPT/monika/turned_mouth_c.png" # closed
        attribute md:        
            "mod_assets/MPT/monika/turned_mouth_d.png" # slightly open
    
    group blink:
        attribute blink default null
        attribute noblink null
    
    group eyes:
        attribute ea default if_any "blink":
            monikablinkturned("mod_assets/MPT/monika/turned_eyes_a.png") # neutral
        attribute eb if_any "blink":        
            monikablinkturned("mod_assets/MPT/monika/turned_eyes_b.png") # left
        
        attribute ea default if_not "blink":
            "mod_assets/MPT/monika/turned_eyes_a.png"
        attribute eb if_not "blink":        
            "mod_assets/MPT/monika/turned_eyes_b.png"

        attribute ec:        
            "mod_assets/MPT/monika/turned_eyes_c.png" # closed 
        attribute ed:        
            "mod_assets/MPT/monika/turned_eyes_d.png" # closed + happy

    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/monika/turned_eyebrows_a.png" # neutral
        attribute bb:        
            "mod_assets/MPT/monika/turned_eyebrows_b.png" # worried
        attribute bc:        
            "mod_assets/MPT/monika/turned_eyebrows_c.png" # serious

define -500 monika_yoffset_cem_babyrage = -20
image monika turned = LayeredImageProxy("_monika turned", (renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="monika"), Transform(yoffset=monika_yoffset_cem_babyrage)))

image side monika turned = CharacterSideImage("_monika turned", renpy.partial(Flatten, drawable_resolution=False))