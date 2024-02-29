python early:
    def Rectangle(color, border=1, **kwargs):
        return Transform(
            Flatten(
                Fixed(
                    Solid(color, xsize=border, xalign=0.0),
                    Solid(color, xsize=border, xalign=1.0),
                    Solid(color, ysize=border, yalign=0.0),
                    Solid(color, ysize=border, yalign=1.0),
                    **kwargs
                ),
            ),
            nearest=True
        )
    
    renpy.register_sl_displayable("rectangle", Rectangle, "rectangle") \
        .add_positional("color") \
        .add_property("border")
        
style rectangle is empty