# kms
image _mc_tears_a_abij = "mod_assets/MPT/melody/turned_tears_a_abij.png"
image _mc_tears_a_cf   = "mod_assets/MPT/melody/turned_tears_a_cf.png"
image _mc_tears_a_de   = "mod_assets/MPT/melody/turned_tears_a_de.png"
image _mc_tears_a_g    = "mod_assets/MPT/melody/turned_tears_a_g.png"
image _mc_tears_a_h    = "mod_assets/MPT/melody/turned_tears_a_h.png"

image _mc_tears_b_abdeij = "mod_assets/MPT/melody/turned_tears_b_abdeij.png"
image _mc_tears_b_cf     = "mod_assets/MPT/melody/turned_tears_b_cf.png"
image _mc_tears_b_g      = "mod_assets/MPT/melody/turned_tears_b_g.png"
image _mc_tears_b_h      = "mod_assets/MPT/melody/turned_tears_b_h.png"

image _mc_eyes_a  = "mod_assets/MPT/melody/turned_eyes_a.png" # neutral
image _mc_eyes_ab = "mod_assets/MPT/melody/turned_eyes_ab.png" # _b versions don't have the light in the eyes
image _mc_eyes_b  = "mod_assets/MPT/melody/turned_eyes_b.png" # surprised
image _mc_eyes_bb = "mod_assets/MPT/melody/turned_eyes_bb.png"
image _mc_eyes_c  = "mod_assets/MPT/melody/turned_eyes_c.png" # "amelia ec"
image _mc_eyes_d  = "mod_assets/MPT/melody/turned_eyes_d.png" # "e1d"
image _mc_eyes_db = "mod_assets/MPT/melody/turned_eyes_db.png"
image _mc_eyes_e  = "mod_assets/MPT/melody/turned_eyes_e.png" # same but looking fiercer
image _mc_eyes_eb = "mod_assets/MPT/melody/turned_eyes_eb.png"
image _mc_eyes_f  = "mod_assets/MPT/melody/turned_eyes_f.png" # left
image _mc_eyes_g  = "mod_assets/MPT/melody/turned_eyes_g.png" # closed
image _mc_eyes_h  = "mod_assets/MPT/melody/turned_eyes_h.png" # closed + happy
image _mc_eyes_i  = "mod_assets/MPT/melody/turned_eyes_i.png" # crazy 1
image _mc_eyes_j  = "mod_assets/MPT/melody/turned_eyes_j.png" # crazy 2

image _mc_eyes_a_ta  = FixedFitFirst("_mc_eyes_a", "_mc_tears_a_abij")
image _mc_eyes_ab_ta = FixedFitFirst("_mc_eyes_ab", "_mc_tears_a_abij")
image _mc_eyes_b_ta  = FixedFitFirst("_mc_eyes_b", "_mc_tears_a_abij")
image _mc_eyes_bb_ta = FixedFitFirst("_mc_eyes_bb", "_mc_tears_a_abij")
image _mc_eyes_c_ta  = FixedFitFirst("_mc_eyes_c", "_mc_tears_a_cf")
image _mc_eyes_d_ta  = FixedFitFirst("_mc_eyes_d", "_mc_tears_a_de")
image _mc_eyes_db_ta = FixedFitFirst("_mc_eyes_db", "_mc_tears_a_de")
image _mc_eyes_e_ta  = FixedFitFirst("_mc_eyes_e", "_mc_tears_a_de")
image _mc_eyes_eb_ta = FixedFitFirst("_mc_eyes_eb", "_mc_tears_a_de")
image _mc_eyes_f_ta  = FixedFitFirst("_mc_eyes_f", "_mc_tears_a_cf")
image _mc_eyes_g_ta  = FixedFitFirst("_mc_eyes_g", "_mc_tears_a_g")
image _mc_eyes_h_ta  = FixedFitFirst("_mc_eyes_h", "_mc_tears_a_h")
image _mc_eyes_i_ta  = FixedFitFirst("_mc_eyes_i", "_mc_tears_a_abij")
image _mc_eyes_j_ta  = FixedFitFirst("_mc_eyes_j", "_mc_tears_a_abij")

image _mc_eyes_a_tb  = FixedFitFirst("_mc_eyes_a", "_mc_tears_b_abdeij")
image _mc_eyes_ab_tb = FixedFitFirst("_mc_eyes_ab", "_mc_tears_b_abdeij")
image _mc_eyes_b_tb  = FixedFitFirst("_mc_eyes_b", "_mc_tears_b_abdeij")
image _mc_eyes_bb_tb = FixedFitFirst("_mc_eyes_bb", "_mc_tears_b_abdeij")
image _mc_eyes_c_tb  = FixedFitFirst("_mc_eyes_c", "_mc_tears_b_cf")
image _mc_eyes_d_tb  = FixedFitFirst("_mc_eyes_d", "_mc_tears_b_abdeij")
image _mc_eyes_db_tb = FixedFitFirst("_mc_eyes_db", "_mc_tears_b_abdeij")
image _mc_eyes_e_tb  = FixedFitFirst("_mc_eyes_e", "_mc_tears_b_abdeij")
image _mc_eyes_eb_tb = FixedFitFirst("_mc_eyes_eb", "_mc_tears_b_abdeij")
image _mc_eyes_f_tb  = FixedFitFirst("_mc_eyes_f", "_mc_tears_b_cf")
image _mc_eyes_g_tb  = FixedFitFirst("_mc_eyes_g", "_mc_tears_b_g")
image _mc_eyes_h_tb  = FixedFitFirst("_mc_eyes_h", "_mc_tears_b_h")
image _mc_eyes_i_tb  = FixedFitFirst("_mc_eyes_i", "_mc_tears_b_abdeij")
image _mc_eyes_j_tb  = FixedFitFirst("_mc_eyes_j", "_mc_tears_b_abdeij")

init python:
    mc_blink = CharacterBlink("_mc_eyes_h", "_mc_eyes_g")
    mc_blink_ta = CharacterBlink("_mc_eyes_h_ta", "_mc_eyes_g_ta")
    mc_blink_tb = CharacterBlink("_mc_eyes_h_tb", "_mc_eyes_g_tb")

layeredimage _melody turned:    
    group hair:
        attribute messy:
            "mod_assets/MPT/melody/turned_hair_messy.png"
        attribute bun:
            "mod_assets/MPT/melody/turned_hair_bun.png"
        attribute tail:
            "mod_assets/MPT/melody/turned_hair_tail.png"
        attribute braid default:
            "mod_assets/MPT/melody/turned_hair_braid.png"

    always "mod_assets/MPT/melody/turned_facebase.png"

    group bangs:
        attribute bangs_a default:
            "mod_assets/MPT/melody/turned_bangs_a.png"
        attribute bangs_b:
            "mod_assets/MPT/melody/turned_bangs_b.png"

    group hairclip:
        attribute nohairclip default null
        attribute hairclip:
            "mod_assets/MPT/melody/turned_hairclip.png"
    
    group outfit:
        attribute uniform default null
        attribute casual null
        attribute naked null

        attribute coat_uniform null
        attribute coat_casual null
    
    group left:
        attribute ldown default if_any "uniform":
            "mod_assets/MPT/melody/outfits/turned_uniform_ldown.png"
        attribute ldown default if_any "casual":
            "mod_assets/MPT/melody/outfits/turned_casual_ldown.png"
        attribute ldown default if_any "naked":
            "mod_assets/MPT/melody/outfits/turned_naked_ldown.png"
        attribute ldown default if_any "coat_uniform":
            "mod_assets/MPT/melody/outfits/turned_coat_uniform_ldown.png"
        attribute ldown default if_any "coat_casual":
            "mod_assets/MPT/melody/outfits/turned_coat_casual_ldown.png"

        attribute lback if_any "uniform":
            "mod_assets/MPT/melody/outfits/turned_uniform_lback.png"
        attribute lback if_any "casual":
            "mod_assets/MPT/melody/outfits/turned_casual_lback.png"
        attribute lback if_any "naked":
            "mod_assets/MPT/melody/outfits/turned_naked_lback.png"
        attribute lback if_any "coat_uniform":
            "mod_assets/MPT/melody/outfits/turned_coat_uniform_lback.png"
        attribute lback if_any "coat_casual":
            "mod_assets/MPT/melody/outfits/turned_coat_casual_lback.png"
                
        attribute thinking if_any "uniform":
            "mod_assets/MPT/melody/outfits/turned_uniform_thinking_base.png"
        attribute thinking if_any "casual":
            "mod_assets/MPT/melody/outfits/turned_casual_thinking_base.png"
        attribute thinking if_any "naked":
            "mod_assets/MPT/melody/outfits/turned_naked_thinking_base.png"
        attribute thinking if_any "coat_uniform":
            "mod_assets/MPT/melody/outfits/turned_coat_uniform_thinking_base.png"
        attribute thinking if_any "coat_casual":
            "mod_assets/MPT/melody/outfits/turned_coat_casual_thinking_base.png"

    group right:
        attribute rdown default if_any "uniform" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_uniform_rdown.png"
        attribute rdown default if_any "casual" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_casual_rdown.png"
        attribute rdown default if_any "naked" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_naked_rdown.png"
        attribute rdown default if_any "coat_uniform" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_coat_uniform_rdown.png"
        attribute rdown default if_any "coat_casual" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_coat_casual_rdown.png"

        attribute rback if_any "uniform" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_uniform_rback.png"
        attribute rback if_any "casual" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_casual_rback.png"
        attribute rback if_any "naked" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_naked_rback.png"
        attribute rback if_any "coat_uniform" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_coat_uniform_rback.png"
        attribute rback if_any "coat_casual" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_coat_casual_rback.png"
        
        attribute rback2 if_any "uniform" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_uniform_rback2.png"
        attribute rback2 if_any "casual" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_casual_rback2.png"
        attribute rback2 if_any "naked" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_naked_rback2.png"
        attribute rback2 if_any "coat_uniform" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_coat_uniform_rback2.png"
        attribute rback2 if_any "coat_casual" if_not "thinking":
            "mod_assets/MPT/melody/outfits/turned_coat_casual_rback2.png"
    
    group strands:
        attribute strands default if_any "uniform" if_not "apron":
            "mod_assets/MPT/melody/turned_strand_left_uniform.png"
        attribute strands default if_any "casual" if_not "apron":
            "mod_assets/MPT/melody/turned_strand_left_casual.png"
        attribute strands default if_any "naked" if_not "apron":
            "mod_assets/MPT/melody/turned_strand_left_naked.png"
        attribute strands default if_any ["coat_uniform", "coat_casual"] if_not "apron":
            "mod_assets/MPT/melody/turned_strand_left_coat.png"
        attribute strands default if_any "apron":
            "mod_assets/MPT/melody/turned_strand_left_apron.png"
        attribute nostrands null
    
    # only works with the casual outfit
    # sorry but i aint doing all that
    group apron:
        attribute noapron default null
        attribute apron:
            "mod_assets/MPT/melody/outfits/turned_apron.png"
    
    always "mod_assets/MPT/melody/outfits/turned_uniform_thinking_arms.png" if_all ["thinking", "uniform"]
    always "mod_assets/MPT/melody/outfits/turned_casual_thinking_arms.png" if_all ["thinking", "casual"]
    always "mod_assets/MPT/melody/outfits/turned_naked_thinking_arms.png" if_all ["thinking", "naked"]
    always "mod_assets/MPT/melody/outfits/turned_coat_uniform_thinking_arms.png" if_all ["thinking", "coat_uniform"]
    always "mod_assets/MPT/melody/outfits/turned_coat_casual_thinking_arms.png" if_all ["thinking", "coat_casual"]
    
    always "mod_assets/MPT/melody/turned_strand_right.png" if_any "strands"

    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/melody/turned_nose_b.png" # sweat 
        attribute nc:
            "mod_assets/MPT/melody/turned_nose_c.png" # blush
        attribute nd:
            "mod_assets/MPT/melody/turned_nose_d.png" # blush + sweat
    
    group lipstick:
        attribute nolipstick default null
        attribute lipstick null

    group mouth if_not "lipstick":
        attribute ma default:
            "mod_assets/MPT/melody/turned_mouth_a.png" # smiling
        attribute mb:
            "mod_assets/MPT/melody/turned_mouth_b.png" # talking + smiling
        attribute mc:
            "mod_assets/MPT/melody/turned_mouth_c.png" # talking + smiling 2
        attribute md:
            "mod_assets/MPT/melody/turned_mouth_d.png" # big smile
        attribute me:
            "mod_assets/MPT/melody/turned_mouth_e.png" # "god what i'd do for a gun in my mouth"
        attribute mf:
            "mod_assets/MPT/melody/turned_mouth_f.png" # "mh"
        attribute mg:
            "mod_assets/MPT/melody/turned_mouth_g.png" # "mi"
        attribute mh:
            "mod_assets/MPT/melody/turned_mouth_h.png" # "natsuki mj" 
        attribute mi:
            "mod_assets/MPT/melody/turned_mouth_i.png" # :(
        attribute mj:
            "mod_assets/MPT/melody/turned_mouth_j.png" # "amelia mh"
        attribute mk:
            "mod_assets/MPT/melody/turned_mouth_k.png" # ^ but showing teeth
        attribute ml:
            "mod_assets/MPT/melody/turned_mouth_l.png" # "monika turned md" but bigger
        attribute mm:
            "mod_assets/MPT/melody/turned_mouth_m.png" # anger 1
        attribute mn:
            "mod_assets/MPT/melody/turned_mouth_n.png" # anger 2
        attribute mo:
            "mod_assets/MPT/melody/turned_mouth_o.png" # anger 3
        attribute mp:
            "mod_assets/MPT/melody/turned_mouth_p.png" # whatever this is
        attribute teehee:
            "mod_assets/MPT/melody/turned_mouth_teehee.png" # teehee
        attribute uwu:
            "mod_assets/MPT/melody/turned_mouth_uwu.png" # uwu
        attribute pout:
            "mod_assets/MPT/melody/turned_mouth_pout.png" # pout
    
    group mouth if_any "lipstick":
        attribute ma default:
            "mod_assets/MPT/melody/turned_mouth_a_lipstick.png"
        attribute mb:
            "mod_assets/MPT/melody/turned_mouth_b_lipstick.png"
        attribute mc:
            "mod_assets/MPT/melody/turned_mouth_c_lipstick.png"
        attribute md:
            "mod_assets/MPT/melody/turned_mouth_d_lipstick.png"
        attribute me:
            "mod_assets/MPT/melody/turned_mouth_e_lipstick.png"
        attribute mf:
            "mod_assets/MPT/melody/turned_mouth_f_lipstick.png"
        attribute mg:
            "mod_assets/MPT/melody/turned_mouth_g_lipstick.png" 
        attribute mh:
            "mod_assets/MPT/melody/turned_mouth_h_lipstick.png"  
        attribute mi:
            "mod_assets/MPT/melody/turned_mouth_i_lipstick.png"
        attribute mj:
            "mod_assets/MPT/melody/turned_mouth_j_lipstick.png"
        attribute mk:
            "mod_assets/MPT/melody/turned_mouth_k_lipstick.png" 
        attribute ml:
            "mod_assets/MPT/melody/turned_mouth_l_lipstick.png"
        attribute mm:
            "mod_assets/MPT/melody/turned_mouth_m_lipstick.png"
        attribute mn:
            "mod_assets/MPT/melody/turned_mouth_n_lipstick.png"
        attribute mo:
            "mod_assets/MPT/melody/turned_mouth_o_lipstick.png"
        attribute mp:
            "mod_assets/MPT/melody/turned_mouth_p_lipstick.png"
        attribute teehee:
            "mod_assets/MPT/melody/turned_mouth_teehee_lipstick.png"
        attribute uwu:
            "mod_assets/MPT/melody/turned_mouth_uwu_lipstick.png"
        attribute pout:
            "mod_assets/MPT/melody/turned_mouth_pout_lipstick.png"
    
    group tears:
        attribute notears default null
        attribute tears_a null
        attribute tears_b null

    group blink:
        attribute blink default null
        attribute noblink null

    group eyes:
        attribute ea default if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_a") 
        attribute ea_b if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_ab") 
        attribute eb if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_b")
        attribute eb_b if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_bb")
        attribute ec if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_c") 
        attribute ed if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_d") 
        attribute ed_b if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_db")
        attribute ee if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_e") 
        attribute ee_b if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_eb")
        attribute ef if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_f") 
        attribute ei if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_i") 
        attribute ej if_any "blink" if_not ["tears_a", "tears_b"]:
            mc_blink("_mc_eyes_j")
    
        attribute ea default if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_a_ta")
        attribute ea_b if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_ab_ta")
        attribute eb if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_b_ta")
        attribute eb_b if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_bb_ta")
        attribute ec if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_c_ta")
        attribute ed if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_d_ta")
        attribute ed_b if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_db_ta")
        attribute ee if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_e_ta")
        attribute ee_b if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_eb_ta")
        attribute ef if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_f_ta")
        attribute ei if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_i_ta") 
        attribute ej if_all ["blink", "tears_a"] if_not "tears_b":
            mc_blink_ta("_mc_eyes_j_ta")
    
        attribute ea default if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_a_tb")
        attribute ea_b if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_ab_tb")
        attribute eb if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_b_tb")
        attribute eb_b if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_bb_tb")
        attribute ec if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_c_tb")
        attribute ed if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_d_tb")
        attribute ed_b if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_db_tb")
        attribute ee if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_e_tb")
        attribute ee_b if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_eb_tb")
        attribute ef if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_f_tb")
        attribute ei if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_i_tb") 
        attribute ej if_all ["blink", "tears_b"] if_not "tears_a":
            mc_blink_tb("_mc_eyes_j_tb")
    
        attribute ea default if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_a" 
        attribute ea_b if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_ab" 
        attribute eb if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_b" 
        attribute eb_b if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_bb"
        attribute ec if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_c" 
        attribute ed if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_d" 
        attribute ed_b if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_db"
        attribute ee if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_e"
        attribute ee_b if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_eb"
        attribute ef if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_f" 
        attribute ei if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_i" 
        attribute ej if_not ["blink", "tears_a", "tears_b"]:
            "_mc_eyes_j"

        attribute ea default if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_a_ta" 
        attribute ea_b if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_ab_ta" 
        attribute eb if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_b_ta" 
        attribute eb_b if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_bb_ta"
        attribute ec if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_c_ta" 
        attribute ed if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_d_ta" 
        attribute ed_b if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_db_ta"
        attribute ee if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_e_ta"
        attribute ee_b if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_eb_ta"
        attribute ef if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_f_ta" 
        attribute ei if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_i_ta" 
        attribute ej if_not ["blink", "tears_b"] if_any "tears_a":
            "_mc_eyes_j_ta" 

        attribute ea default if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_a_tb" 
        attribute ea_b if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_ab_tb" 
        attribute eb if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_b_tb" 
        attribute eb_b if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_bb_tb"
        attribute ec if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_c_tb" 
        attribute ed if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_d_tb" 
        attribute ed_b if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_db_tb"
        attribute ee if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_e_tb"
        attribute ee_b if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_eb_tb"
        attribute ef if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_f_tb" 
        attribute ei if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_i_tb" 
        attribute ej if_not ["blink", "tears_a"] if_any "tears_b":
            "_mc_eyes_j_tb" 

        attribute eg if_not ["tears_a", "tears_b"]:
            "_mc_eyes_g"
        attribute eh if_not ["tears_a", "tears_b"]:
            "_mc_eyes_h" 
    
        attribute eg if_any "tears_a":
            "_mc_eyes_g_ta"
        attribute eh if_any "tears_a":
            "_mc_eyes_h_ta"
    
        attribute eg if_any "tears_b":
            "_mc_eyes_g_tb"
        attribute eh if_any "tears_b":
            "_mc_eyes_h_tb"

    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/melody/turned_eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/melody/turned_eyebrows_b.png" # surprised 1
        attribute bc:
            "mod_assets/MPT/melody/turned_eyebrows_c.png" # surprised 2
        attribute bd:
            "mod_assets/MPT/melody/turned_eyebrows_d.png" # "b1d". it kinda sucks tho. bj and bi are better
        attribute be:
            "mod_assets/MPT/melody/turned_eyebrows_e.png" # worried 1
        attribute bf:
            "mod_assets/MPT/melody/turned_eyebrows_f.png" # worried 2
        attribute bg:
            "mod_assets/MPT/melody/turned_eyebrows_g.png" # worried 3
        attribute bh:
            "mod_assets/MPT/melody/turned_eyebrows_h.png" # worried 4
        attribute bi:
            "mod_assets/MPT/melody/turned_eyebrows_i.png" # anger 1
        attribute bj:
            "mod_assets/MPT/melody/turned_eyebrows_j.png" # anger 2
        attribute bk:
            "mod_assets/MPT/melody/turned_eyebrows_k.png" # idk 1
        attribute bl:
            "mod_assets/MPT/melody/turned_eyebrows_l.png" # idk 2
        attribute bm:
            "mod_assets/MPT/melody/turned_eyebrows_m.png" # the rock

image melody turned = LayeredImageProxy("_melody turned", (renpy.partial(Flatten, drawable_resolution=False), AutofocusDisplayable(name="melody")))

image side melody turned = CharacterSideImage("_melody turned", renpy.partial(Flatten, drawable_resolution=False))