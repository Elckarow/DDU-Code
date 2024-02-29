layeredimage _widenekoflap:
    always "mod_assets/MPT/widenekoflap/base.png"
    
    group widenekoflap:
        attribute ma default null
        attribute mb:
            "mod_assets/MPT/widenekoflap/mb.png"
        attribute mc:
            "mod_assets/MPT/widenekoflap/mc.png"

image widenekoflap = LayeredImageProxy("_widenekoflap", renpy.partial(Flatten, drawable_resolution=False))