init offset = 1

transform _cg_dissolve:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0 

init python:
    def CG(child):
        if store.main_menu: return Flatten(child)
        return At(child, Flatten, _cg_dissolve)

layeredimage cg yuri 1:
    at afternoon

    always "mod_assets/CG/yuri/1/cg_y_1.png"

layeredimage cg amelia 1:
    always "mod_assets/CG/amelia/1/base.png"

    group mc:
        attribute mc_a default null
        attribute mc_b:
            "mod_assets/CG/amelia/1/mc_b.png"

    group am:
        attribute am_a default null
        attribute am_b:
            "mod_assets/CG/amelia/1/am_b.png"

layeredimage cg melody 1:
    at variant(0.47, -0.028, "#b4caaf")
    
    group cg:
        attribute towel1 default:
            "mod_assets/CG/mc/1/cg_1.png"
        attribute towel2:
            "mod_assets/CG/mc/1/cg_2.png"
        attribute uniform:
            "mod_assets/CG/mc/1/cg_3.png"

layeredimage cg melody 2:
    at variant(0.64, -0.12, "#cfcfcf")

    always "mod_assets/CG/mc/2/background.png"

    group mc:
        attribute mc default:
            "mod_assets/CG/mc/2/mc.png"
        attribute no_mc null

layeredimage cg sayori 1:
    at afternoon

    always "mod_assets/CG/sayori/1/base.png"

    group eyebrows:
        attribute ba default:
            "mod_assets/CG/sayori/1/eyebrows_a.png"

    group eyes:
        attribute ea default:
            "mod_assets/CG/sayori/1/eyes_a.png"
        attribute eb:
            "mod_assets/CG/sayori/1/eyes_b.png"
    
    group mouth:
        attribute ma default:
            "mod_assets/CG/sayori/1/mouth_a.png"
        attribute mb:
            "mod_assets/CG/sayori/1/mouth_b.png"

layeredimage cg monika 1:
    always "mod_assets/CG/monika/1/base.png"

    group blush:
        attribute na default null
        attribute nb:
            "mod_assets/CG/monika/1/nose_b.png"
    
    group eyebrows:
        attribute ba default:
            "mod_assets/CG/monika/1/eyebrows_a.png"

    group eyes:
        attribute ea default:
            "mod_assets/CG/monika/1/eyes_a.png"
        attribute eb:
            "mod_assets/CG/monika/1/eyes_b.png"
        attribute ec:
            "mod_assets/CG/monika/1/eyes_c.png"
    
    group mouth:
        attribute ma default:
            "mod_assets/CG/monika/1/mouth_a.png"

layeredimage cg natsuki 1:
    at afternoon

    group head:
        attribute side default null
        attribute front null
    
    always "mod_assets/CG/natsuki/1/base_side.png" if_any "side"
    always "mod_assets/CG/natsuki/1/base_front.png" if_any "front"

    group nose:
        attribute na default null
        attribute nb if_any "side":
            "mod_assets/CG/natsuki/1/side_nose_b.png"
        attribute nb if_any "front":
            "mod_assets/CG/natsuki/1/front_nose_b.png"
    
    group mouth:
        attribute ma default if_any "side":
            "mod_assets/CG/natsuki/1/side_mouth_a.png"
        attribute mb if_any "side":
            "mod_assets/CG/natsuki/1/side_mouth_b.png"
        attribute mc if_any "side":
            "mod_assets/CG/natsuki/1/side_mouth_c.png"
        
        attribute ma default if_any "front":
            "mod_assets/CG/natsuki/1/front_mouth_a.png"
        attribute mb if_any "front":
            "mod_assets/CG/natsuki/1/front_mouth_b.png"
        attribute mc if_any "front":
            "mod_assets/CG/natsuki/1/front_mouth_c.png"
    
    group eyes:
        attribute ea default if_any "side":
            "mod_assets/CG/natsuki/1/side_eyes_a.png"
        attribute eb if_any "side":
            "mod_assets/CG/natsuki/1/side_eyes_b.png"
        attribute ec if_any "side":
            "mod_assets/CG/natsuki/1/side_eyes_c.png"
        
        attribute ea default if_any "front":
            "mod_assets/CG/natsuki/1/front_eyes_a.png"
        attribute eb if_any "front":
            "mod_assets/CG/natsuki/1/front_eyes_b.png"
        attribute ec if_any "front":
            "mod_assets/CG/natsuki/1/front_eyes_c.png"
    
    group eyebrows:
        attribute ba default if_any "side":
            "mod_assets/CG/natsuki/1/side_eyebrows_a.png"
        attribute bb if_any "side":
            "mod_assets/CG/natsuki/1/side_eyebrows_b.png"
        attribute bc if_any "side":
            "mod_assets/CG/natsuki/1/side_eyebrows_c.png"
        
        attribute ba default if_any "front":
            "mod_assets/CG/natsuki/1/front_eyebrows_a.png"
        attribute bb if_any "front":
            "mod_assets/CG/natsuki/1/front_eyebrows_b.png"        