init offset = 1

layeredimage cg yuri 1:
    at Transform(matrixcolor=BrightnessMatrix(0.05) * TintMatrix((235, 195, 165)))

    always "mod_assets/CG/yuri/1/cg_y_1.png"

layeredimage cg yuri 2:
    group cg:
        attribute neutral default:
            "mod_assets/CG/yuri/2/cg_y_1.png"
        attribute smile:
            "mod_assets/CG/yuri/2/cg_y_2.png"
        attribute turn:
            "mod_assets/CG/yuri/2/cg_y_3.png"
        attribute understand:
            "mod_assets/CG/yuri/2/cg_y_4.png"

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
    at Transform(matrixcolor=SaturationMatrix(0.47) * BrightnessMatrix(-0.028) * TintMatrix("#b4caaf")) 
    
    group cg:
        attribute towel1 default:
            "mod_assets/CG/mc/1/cg_1.png"
        attribute towel2:
            "mod_assets/CG/mc/1/cg_2.png"
        attribute uniform:
            "mod_assets/CG/mc/1/cg_3.png"

layeredimage cg melody 2:
    at Transform(matrixcolor=SaturationMatrix(0.64) * BrightnessMatrix(-0.12) * TintMatrix("#cfcfcf")) 

    always "mod_assets/CG/mc/2/background.png"

    group mc:
        attribute mc default:
            "mod_assets/CG/mc/2/mc.png"
        attribute no_mc null
    
layeredimage cg sayori 1:
    at Transform(matrixcolor=BrightnessMatrix(0.05) * TintMatrix((235, 195, 165)))

    always "mod_assets/CG/sayori/1/base.png"

    group eyes:
        attribute ea default:
            "mod_assets/CG/sayori/1/eyes_a.png"
        attribute eb:
            "mod_assets/CG/sayori/1/eyes_b.png"
    
    group eyebrows:
        attribute ba default:
            "mod_assets/CG/sayori/1/eyebrows_a.png"
    
    group mouth:
        attribute ma default:
            "mod_assets/CG/sayori/1/mouth_a.png"
        attribute mb:
            "mod_assets/CG/sayori/1/mouth_b.png"

layeredimage cg sayori 2:
    group sayori:
        attribute normal default:
            "mod_assets/CG/sayori/2/cg_1.jpg"
        attribute smiling:
            "mod_assets/CG/sayori/2/cg_2.jpg"
        attribute pizza:
            "mod_assets/CG/sayori/2/cg_3.jpg"

layeredimage cg sayori 3:
    group sayori:
        attribute ea default:
            "mod_assets/CG/sayori/3/cg_1.png"
        attribute eb:
            "mod_assets/CG/sayori/3/cg_2.png"

layeredimage cg monika 1:
    always "mod_assets/CG/monika/1/base.png"

    group blush:
        attribute na default null
        attribute nb:
            "mod_assets/CG/monika/1/nose_b.png"

    group eyes:
        attribute ea default:
            "mod_assets/CG/monika/1/eyes_a.png"
        attribute eb:
            "mod_assets/CG/monika/1/eyes_b.png"
        attribute ec:
            "mod_assets/CG/monika/1/eyes_c.png"
    
    group eyebrows:
        attribute ba default:
            "mod_assets/CG/monika/1/eyebrows_a.png"
    
    group mouth:
        attribute ma default:
            "mod_assets/CG/monika/1/mouth_a.png"

layeredimage cg natsuki 1:
    at Transform(matrixcolor=BrightnessMatrix(0.05) * TintMatrix((235, 195, 165)))

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

layeredimage cg natsuki 2:
    at Transform(
        matrixcolor=BrightnessMatrix(-0.03) * TintMatrix("#5d9be0")
    )

    always "mod_assets/CG/natsuki/2/base.png"

    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/CG/natsuki/2/nose_b.png"
    
    group mouth:
        attribute ma default:
            "mod_assets/CG/natsuki/2/mouth_a.png"
        attribute mb:
            "mod_assets/CG/natsuki/2/mouth_b.png"
    
    group eyes:
        attribute ea default:
            "mod_assets/CG/natsuki/2/eyes_a.png"
        attribute eb:
            "mod_assets/CG/natsuki/2/eyes_b.png"
        attribute ec:
            "mod_assets/CG/natsuki/2/eyes_c.png"
    
    group eyebrows:
        attribute ba default:
            "mod_assets/CG/natsuki/2/eyebrows_a.png"
        attribute bb:
            "mod_assets/CG/natsuki/2/eyebrows_b.png"
        attribute bc:
            "mod_assets/CG/natsuki/2/eyebrows_c.png"

layeredimage cg sleepover 1:
    always "mod_assets/CG/sleepover/1/cg_sleepover_1.png"

layeredimage cg sleepover 2:
    always "mod_assets/CG/sleepover/2/cg_sleepover_2.png"

    if not main_menu and branches.is_current(branches.FATE):
        "mod_assets/CG/sleepover/2/scar.png"
    else:
        Null()

layeredimage cg sleepover 3:
    always "mod_assets/CG/sleepover/3/base.png"

    group eyes:
        attribute ea default null
        attribute eb:
            "mod_assets/CG/sleepover/3/eb.png"
    
    group mouth:
        attribute ma default null
        attribute mb:
            "mod_assets/CG/sleepover/3/mb.png"
    
layeredimage cg sleepover 4:
    always "mod_assets/CG/sleepover/4/cg_sleepover_4.png"