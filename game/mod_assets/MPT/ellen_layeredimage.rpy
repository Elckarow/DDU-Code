define ellenblink = CharacterBlink("mod_assets/MPT/ellen/turned_eyes_e.png", "mod_assets/MPT/ellen/turned_eyes_d.png")

layeredimage _ellen turned:    
    group facebase:
        attribute downtail default:
            "mod_assets/MPT/ellen/turned_facebase_downtail.png"
        attribute ponytail:
            "mod_assets/MPT/ellen/turned_facebase_ponytail.png"
        attribute hairdown:
            "mod_assets/MPT/ellen/turned_facebase_hairdown.png"
    
    group outfit:
        attribute casual default null
        attribute uniform null
        attribute vest null
    
    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/ellen/turned_nose_b.png"
    
    group left:
        attribute ldown default if_any "uniform":
            "mod_assets/MPT/ellen/outfits/turned_uniform_ldown.png"
        attribute ldown default if_any "casual":
            "mod_assets/MPT/ellen/outfits/turned_casual_ldown.png"
        attribute ldown default if_any "vest":
            "mod_assets/MPT/ellen/outfits/turned_vest_ldown.png"

        attribute lup if_any "uniform":
            "mod_assets/MPT/ellen/outfits/turned_uniform_lup.png"
        attribute lup if_any "casual":
            "mod_assets/MPT/ellen/outfits/turned_casual_lup.png"
        attribute lup if_any "vest":
            "mod_assets/MPT/ellen/outfits/turned_vest_lup.png"
        
        attribute lwaist if_any "uniform":
            "mod_assets/MPT/ellen/outfits/turned_uniform_lwaist.png"
        attribute lwaist if_any "casual":
            "mod_assets/MPT/ellen/outfits/turned_casual_lwaist.png"
        attribute lwaist if_any "vest":
            "mod_assets/MPT/ellen/outfits/turned_vest_lwaist.png"
        
        attribute thinking if_any "uniform":
            "mod_assets/MPT/ellen/outfits/turned_uniform_thinking.png"
        attribute thinking if_any "casual":
            "mod_assets/MPT/ellen/outfits/turned_casual_thinking.png"
        attribute thinking if_any "vest":
            "mod_assets/MPT/ellen/outfits/turned_vest_thinking.png"

    group right:
        attribute rdown default if_any "uniform" if_not "thinking":
            "mod_assets/MPT/ellen/outfits/turned_uniform_rdown.png"
        attribute rdown default if_any "casual" if_not "thinking":
            "mod_assets/MPT/ellen/outfits/turned_casual_rdown.png"
        attribute rdown default if_any "vest" if_not "thinking":
            "mod_assets/MPT/ellen/outfits/turned_vest_rdown.png"

        attribute rhip if_any "uniform" if_not "thinking":
            "mod_assets/MPT/ellen/outfits/turned_uniform_rhip.png"
        attribute rhip if_any "casual" if_not "thinking":
            "mod_assets/MPT/ellen/outfits/turned_casual_rhip.png"
        attribute rhip if_any "vest" if_not "thinking":
            "mod_assets/MPT/ellen/outfits/turned_vest_rhip.png"
        
        attribute rwaist if_any "uniform" if_not "thinking":
            "mod_assets/MPT/ellen/outfits/turned_uniform_rwaist.png"
        attribute rwaist if_any "casual" if_not "thinking":
            "mod_assets/MPT/ellen/outfits/turned_casual_rwaist.png"
        attribute rwaist if_any "vest" if_not "thinking":
            "mod_assets/MPT/ellen/outfits/turned_vest_rwaist.png"
    
    group mouth:
        attribute ma default:
            "mod_assets/MPT/ellen/turned_mouth_a.png" # smiling
        attribute mb:
            "mod_assets/MPT/ellen/turned_mouth_b.png" # talking + smiling
        attribute mc:
            "mod_assets/MPT/ellen/turned_mouth_c.png" # closed "md"
        attribute md:
            "mod_assets/MPT/ellen/turned_mouth_d.png" # slightly open
        attribute me:
            "mod_assets/MPT/ellen/turned_mouth_e.png" # talking + neutral
        attribute mf:
            "mod_assets/MPT/ellen/turned_mouth_f.png" # talking 2 (similar to "natsuki mi")
        attribute mg:
            "mod_assets/MPT/ellen/turned_mouth_g.png" # idk it's like amelia mh but angrier
        attribute mh:
            "mod_assets/MPT/ellen/turned_mouth_h.png" # closed "mj"
        attribute mi:
            "mod_assets/MPT/ellen/turned_mouth_i.png" # amleia "mf"
        attribute mj:
            "mod_assets/MPT/ellen/turned_mouth_j.png" # angwy 
    
    group blink:
        attribute blink default null
        attribute noblink null
    
    group eyes:
        attribute ea default:
            ellenblink("mod_assets/MPT/ellen/turned_eyes_a.png") # neutral
        attribute eb:
            ellenblink("mod_assets/MPT/ellen/turned_eyes_b.png") # surprised
        attribute ec:
            ellenblink("mod_assets/MPT/ellen/turned_eyes_c.png") # left
        attribute ef:
            ellenblink("mod_assets/MPT/ellen/turned_eyes_f.png") # teary
        attribute eg:
            ellenblink("mod_assets/MPT/ellen/turned_eyes_g.png") # yandere bitch
        
        attribute ea default if_not "blink":
            "mod_assets/MPT/ellen/turned_eyes_a.png"
        attribute eb if_not "blink":
            "mod_assets/MPT/ellen/turned_eyes_b.png"
        attribute ec if_not "blink":
            "mod_assets/MPT/ellen/turned_eyes_c.png"
        attribute ef if_not "blink":
            "mod_assets/MPT/ellen/turned_eyes_f.png"
        attribute eg if_not "blink":
            "mod_assets/MPT/ellen/turned_eyes_g.png" 

        attribute ed:
            "mod_assets/MPT/ellen/turned_eyes_d.png" # closed
        attribute ee:
            "mod_assets/MPT/ellen/turned_eyes_e.png" # closed + happy

    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/ellen/turned_eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/ellen/turned_eyebrows_b.png" # surprised
        attribute bc:
            "mod_assets/MPT/ellen/turned_eyebrows_c.png" # b1d :tardlilly: it makes sense to me
        attribute bd:
            "mod_assets/MPT/ellen/turned_eyebrows_d.png" # worried 1
        attribute be:
            "mod_assets/MPT/ellen/turned_eyebrows_e.png" # worried 2
        attribute bf:
            "mod_assets/MPT/ellen/turned_eyebrows_f.png" # anger 1 / pouting
        attribute bg:
            "mod_assets/MPT/ellen/turned_eyebrows_g.png" # anger 2

image ellen turned = LayeredImageProxy("_ellen turned", (renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="ellen")))

image side ellen turned = CharacterSideImage("_ellen turned", renpy.partial(Flatten, drawable_resolution=False))