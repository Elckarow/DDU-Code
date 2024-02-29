image white_flashback = "#ffffff44"

image mc_roof = HBox( # idk. what's shown is != than this. renpy shat itself
    Gradient("#618097", "#64859d", theta=90, xsize=300),
    Gradient("#1d1612", "#231b17", xsize=30),
    Gradient("#618097", "#64859d", theta=-90, xsize=300),
    Gradient("#1d1612", "#231b17", xsize=30),
    Gradient("#618097", "#64859d", theta=90, xsize=300),
    Gradient("#1d1612", "#231b17", xsize=30),
    Gradient("#618097", "#64859d", theta=-90, xsize=300),
    Gradient("#1d1612", "#231b17", xsize=30)
)

init:
    define rain_speed = 0.05

    image rain:
        "mod_assets/BG/rain/1.png"
        rain_speed
        "mod_assets/BG/rain/2.png"
        rain_speed
        "mod_assets/BG/rain/3.png"
        rain_speed
        "mod_assets/BG/rain/4.png"
        rain_speed
        "mod_assets/BG/rain/5.png"
        rain_speed
        "mod_assets/BG/rain/6.png"
        rain_speed
        "mod_assets/BG/rain/7.png"
        rain_speed
        "mod_assets/BG/rain/8.png"
        rain_speed
        repeat

    transform moving_sky(child):
        animation
        HBox(child, Transform(child, xzoom=-1))
        subpixel True
        block:
            xpan 0.0
            linear 750.0 xpan 360.0
            repeat

    image sky_stars:
        "mod_assets/BG/sky_stars.png"
        block:
            alpha 1.0
            easein 3 alpha 0.5
            easeout 2 alpha 1.0
            easein 5 alpha 0.4
            easeout 3 alpha 1.0
            repeat

    python in bgs_stuff:
        from renpy.store import (
            Transform, At, moving_sky, Fixed, SaturationMatrix, TintMatrix, BrightnessMatrix, IdentityMatrix, Matrix,
            config, Null
        )
        import re

        renpy.image("sky_day", "mod_assets/BG/sky_day.png")
        renpy.image("sky_afternoon", "mod_assets/BG/sky_afternoon.png")
        renpy.image("sky_night", Transform("sky_day", matrixcolor=TintMatrix("#0D235C")))
        renpy.image("sky_snow_day", Transform("sky_day", matrixcolor=SaturationMatrix(0.6)))
        renpy.image("sky_gray", Transform("sky_day", matrixcolor=TintMatrix("#caa8a8") * SaturationMatrix(0.2) * BrightnessMatrix(-0.17)))

        colors = {
            "day": IdentityMatrix(),
            "afternoon": SaturationMatrix(0.8) * TintMatrix("#ffa385") * BrightnessMatrix(0.06),
            "night_nostars": SaturationMatrix(0.5) * BrightnessMatrix(-0.1) * TintMatrix("#30366a"),
            "night": SaturationMatrix(0.5) * BrightnessMatrix(-0.08) * TintMatrix("#30366a"),
            "gray": TintMatrix("#b4a2a2") * SaturationMatrix(0.5) * BrightnessMatrix(-0.15),
            "snow_day": IdentityMatrix(),
            "snow_night_nostars": SaturationMatrix(0.5) * BrightnessMatrix(-0.1) * TintMatrix("#262a59"),
            "snow_night": SaturationMatrix(0.5) * BrightnessMatrix(-0.08) * TintMatrix("#262a59"),
        }
        colors["night_on"] = colors["night_off"] = colors["night"]
        colors["night_on_nostars"] = colors["night_off_nostars"] = colors["night_nostars"]

        def image(name, d):
            renpy.image("bg " + name, d)
        
        # help
        def _get_image_variant(d, variant, color):
            if isinstance(d, basestring) and "[" in d:
                sub_variant = variant
                if sub_variant.endswith("_nostars"):
                    sub_variant = sub_variant[:-8]
                if sub_variant.startswith("snow"):
                    sub_variant = "snow"
                d = renpy.substitute(d, scope={"_variant": sub_variant}, translate=False)
            
            if color:
                d = Transform(d, matrixcolor=colors[variant])
            
            return d
        
        def _bg_coroutine(variants):
            for variant in set(variants):
                bg, color = yield variant
                yield _get_image_variant(bg, variant, color)
        
        def background(
            name, base, at_list=(),
            variants=("day", "afternoon", "night_nostars", "night", "gray", "snow_day", "snow_night_nostars", "snow_night"),
            color=True,
            suffix=""
        ):
            cr = _bg_coroutine(variants)

            for variant in cr:
                bg = cr.send((base, color))
                image("{}_{}{}".format(name, variant, suffix), At(bg, *at_list))
        
        def _sky(s):
            return At(s, moving_sky())

        def _get_sky_components(variant):
            if variant.startswith("snow"):
                snow, _, snow_variant = variant.partition("_")
                if snow_variant == "day":
                    yield _sky("sky_snow_day")
                else:
                    # only snow_day is different, the rest are the same
                    for sky_component in _get_sky_components(snow_variant):
                        yield sky_component

            elif variant.startswith("night"):
                yield _sky("sky_night")
                if not variant.endswith("nostars"):
                    yield "sky_stars"

            else:
                yield _sky("sky_" + variant)
            
        def _bg_with_sky_coroutine(variants):
            for variant in set(variants):
                bg, color = yield variant

                images, color_images = yield _get_image_variant(bg, variant, color)
                yield (_get_image_variant(i, variant, color_images) for i in images)

        RAIN_FRONT = 1
        RAIN_BACK = 2

        def background_with_sky(
            name, base, at_list=(),
            variants=("day", "afternoon", "night_nostars", "night", "gray", "snow_day", "snow_night_nostars", "snow_night"),
            images=(), images_at=None,
            color=True, color_images=True,
            suffix="", rain=RAIN_BACK  
        ):
            t = Transform(crop=(0.0, 0.0, 1.0, 1.0), mesh=True)

            cr = _bg_with_sky_coroutine(variants)

            if images_at is None:
                images_at = [[] for _ in images]

            for variant in cr:
                d = Fixed(style="empty")

                for sky_component in _get_sky_components(variant):
                    d.add(sky_component)
                
                bg = cr.send((base, color))
                
                for i, at in zip(cr.send((images, color_images)), images_at):
                    if at is None: at = ()
                    d.add(At(i, *at))

                bg = At(bg, *at_list)
                
                d_rain = d._duplicate(None)

                d.add(bg)

                image("{}_{}{}".format(name, variant, suffix), At(d, t))

                if rain not in (RAIN_BACK, RAIN_FRONT): continue

                if rain == RAIN_BACK: d_rain.add("rain")
                d_rain.add(bg)
                if rain == RAIN_FRONT: d_rain.add("rain")

                image("{}_{}_rain{}".format(name, variant, suffix), At(d_rain, t))

################ School ################
        background_with_sky(
            "school_gate", "mod_assets/BG/school_gate.png",
            variants=("day", "afternoon", "gray", "night", "night_nostars"), rain=RAIN_FRONT
        )

        background_with_sky(
            "school_courtyard", "mod_assets/BG/school_courtyard.png",
            variants=("day", "afternoon", "night_nostars", "night"), rain=RAIN_FRONT
        )
        background_with_sky(
            "school_courtyard", Transform("mod_assets/BG/school_courtyard.png", matrixcolor=TintMatrix("#a79696") * SaturationMatrix(0.4) * BrightnessMatrix(-0.17)),
            variants=("gray",),
            color=False, rain=RAIN_FRONT
        )

        background_with_sky(
            "class_1", "mod_assets/BG/school_class_1_base.png",
            images=("mod_assets/BG/school_courtyard.png",),
            images_at=[[Transform(zoom=0.5, anchor=(200, 0.0), pos=(0.0, 230))]],
            variants=("day", "afternoon", "gray")
        )
        background_with_sky(
            "class_2", "mod_assets/BG/school_class_1_base.png",
            images=("mod_assets/BG/school_courtyard.png",),
            images_at=[[Transform(anchor=(400, 0.0), pos=(0.0, 250), zoom=0.7)]],
            variants=("day", "afternoon", "gray")
        )
        background_with_sky(
            "class_3", "mod_assets/BG/school_class_2_base.png",
            images=("mod_assets/BG/school_courtyard.png",),
            images_at=[[Transform(xpos=1.0, xanchor=0.9, ypos=200, zoom=0.4)]],
            variants=("day", "afternoon", "gray")
        )
        background_with_sky(
            "class_4", "mod_assets/BG/school_class_2_base.png",
            images=("mod_assets/BG/school_courtyard.png",),
            images_at=[[Transform(xpos=1.0, xanchor=0.5, ypos=180, zoom=0.8)]],
            variants=("day", "afternoon", "gray")
        )

        background(
            "music_class", "mod_assets/BG/music_class_[_variant].png",
            variants=("day", "afternoon"), color=False
        )
        background(
            "music_class", "mod_assets/BG/music_class_day.png",
            variants=("gray", "night"),
        )

        background(
            "art_class", "mod_assets/BG/art_class_[_variant].jpg",
            variants=("day", "afternoon", "gray"), color=False
        )

        background_with_sky(
            "club", "mod_assets/BG/school_class_2_base.png",
            images=("mod_assets/BG/school_courtyard.png",),
            images_at=[[Transform(xpos=1.0, xanchor=800, ypos=230, zoom=0.7)]],
            variants=("day", "afternoon", "gray")
        )
        background(
            "club_closet", "bg/closet.png",
            variants=("day", "afternoon", "gray")
        )

        background(
            "school_corridor_1", "bg/corridor.png",
            variants=("day", "afternoon", "gray")
        )
        background_with_sky(
            "school_corridor_1", "mod_assets/BG/school_corridor_[_variant].png",
            variants=("night", "night_nostars"),
            color=False
        )
        background_with_sky(
            "school_corridor_2", "mod_assets/BG/school_corridor_2_[_variant].png",
            variants=("day", "afternoon", "gray"),
            color=False
        )
        background(
            "school_corridor_3", "mod_assets/BG/school_corridor_3.png",
            variants=("day", "afternoon", "gray", "night")
        )

        background_with_sky(
            "school_rooftop", "mod_assets/BG/school_rooftop.png",
            variants=("day", "afternoon", "gray"), rain=RAIN_FRONT
        )

        background_with_sky(
            "school_street", "mod_assets/BG/school_street_[_variant].png",
            variants=("day", "gray", "afternoon", "night_on", "night_off", "night_on_nostars", "night_off_nostars"),
            color=False, rain=RAIN_FRONT
        )

        background(
            "school_lockers", "mod_assets/BG/school_lockers_[_variant].jpg",
            variants=("day", "afternoon"),
            color=False
        )

        background(
            "school_library", "mod_assets/BG/school_library_day.png",
            variants=("day", "afternoon", "gray"),
        )

        background(
            "school_cafeteria", "mod_assets/BG/school_cafeteria.png",
            variants=("day", "afternoon", "gray")
        )

        background(
            "school_vending_machine", "mod_assets/BG/school_vending_machine.png",
            variants=("day", "afternoon", "gray")
        )

        image("school_bathroom", "mod_assets/BG/school_bathroom.png")

################ Houses ################
        background_with_sky(
            "am_house", "mod_assets/BG/am_house_[_variant].png",
            variants=("day", "afternoon", "night_on", "night_off", "night_on_nostars", "night_off_nostars"),
            color=False, rain=RAIN_FRONT
        )
        background(
            "am_kitchen", "mod_assets/BG/am_kitchen_[_variant].jpg",
            variants=("day", "afternoon", "night_on", "snow"),
            color=False
        )
        background(
            "am_kitchen", "mod_assets/BG/am_kitchen_night_on.jpg",
            variants=("night_off",),
        )
        background(
            "am_living_room", "mod_assets/BG/am_living_room_[_variant].jpg",
            variants=("day", "afternoon", "night_on", "night_off", "snow"),
            color=False
        )

        background_with_sky(
            "s_house", "mod_assets/BG/s_house_[_variant].png",
            variants=("day", "afternoon"),
            color=False, rain=RAIN_FRONT
        )
        background_with_sky(
            "s_house", "mod_assets/BG/s_house_[_variant]_off.png",
            variants=("night", "night_nostars"), suffix="_off",
            color=False, rain=RAIN_FRONT
        )
        background_with_sky(
            "s_house", "mod_assets/BG/s_house_[_variant]_on.png",
            variants=("night", "night_nostars"), suffix="_on",
            color=False, rain=RAIN_FRONT
        )

        background(
            "s_house_entrance", "mod_assets/BG/mc_house_entrance_[_variant].png",
            at_list=[Transform(xzoom=-1)],
            variants=("day", "afternoon", "night"), color=False
        )
        background(
            "s_house_corridor", "mod_assets/BG/mc_house_corridor_day.png",
            variants=("day", "afternoon"), at_list=[Transform(xzoom=-1)]
        )

        background_with_sky(
            "s_bedroom", "mod_assets/BG/s_bedroom_base.png",
            images=(
                "mod_assets/BG/s_house_[_variant].png",
                "mod_assets/BG/s_house_[_variant].png",
            ),
            images_at=[
                [Transform(zoom=0.6, xycenter=(1175, 550))],
                [Transform(crop=(0.08, 0.0, 0.28, 1.0)), Transform(zoom=0.59, xycenter=(0.4, 540))]
            ],
            color_images=False,
            variants=("day", "afternoon", "gray"),
        )
        background_with_sky(
            "s_bedroom", "mod_assets/BG/s_bedroom_base.png",
            images=(
                "mod_assets/BG/s_house_night_off.png",
                "mod_assets/BG/s_house_night_off.png",
            ),
            images_at=[
                [Transform(zoom=0.6, xycenter=(1175, 550))],
                [Transform(crop=(0.08, 0.0, 0.28, 1.0)), Transform(zoom=0.59, xycenter=(0.4, 540))]
            ],
            color_images=False,
            variants=("night", "night_nostars"),
            suffix="_off"
        )
        background_with_sky(
            "s_bedroom", "mod_assets/BG/s_bedroom_base.png", color=False, at_list=[Transform(matrixcolor=TintMatrix("#faffc3") * BrightnessMatrix(0.1))],
            images=(
                "mod_assets/BG/s_house_night_off.png",
                "mod_assets/BG/s_house_night_off.png",
                "#d2c8ff31"
            ),
            images_at=[
                [Transform(zoom=0.6, xycenter=(1175, 550))],
                [Transform(crop=(0.08, 0.0, 0.28, 1.0)), Transform(zoom=0.59, xycenter=(0.4, 540))],
                None
            ],
            color_images=False,
            variants=("night", "night_nostars"),
            suffix="_on"
        )

        image("s_spare_bedroom", "mod_assets/BG/s_spare_bedroom.jpg")
        image("s_living_room", "mod_assets/BG/s_living_room.png")

        background(
            "s_kitchen", "bg/kitchen.png",
            at_list=[Transform(xzoom=-1)],
            variants=("day", "afternoon", "night")
        )

        background(
            "s_bathroom", "mod_assets/BG/mc_bathroom_[_variant].jpg",
            variants=("day", "afternoon", "night_on", "night_off"), color=False,
            at_list=[Transform(xzoom=-1)]
        )

        background(
            "mc_kitchen", "bg/kitchen.png",
            variants=("day", "afternoon", "night")
        )

        background(
            "mc_house_entrance", "mod_assets/BG/mc_house_entrance_[_variant].png",
            variants=("day", "afternoon", "night"), color=False
        )
        background(
            "mc_bathroom", "mod_assets/BG/mc_bathroom_[_variant].jpg",
            variants=("day", "afternoon", "night_on", "night_off"), color=False
        )
        image("mc_living_room", "mod_assets/BG/mc_living_room.png")
        background_with_sky(
            "mc_bedroom", "mod_assets/BG/mc_bedroom_open_base.png",
            variants=("day", "afternoon", "gray"),
            at_list=[Transform(matrixcolor=TintMatrix("#daf8fd") * BrightnessMatrix(-0.01))],
            images=[
                "mod_assets/BG/s_house_[_variant].png",
                "#ffffff0c",
            ],
            images_at=[
                [Transform(yzoom=0.8, xzoom=-0.8, xycenter=(0.53, 0.75))],
                []
            ],
            color_images=False,
            suffix="_open"
        )
        background_with_sky(
            "mc_bedroom", "mod_assets/BG/mc_bedroom_open_base.png",
            variants=("night", "night_nostars"),
            at_list=[Transform(matrixcolor=TintMatrix("#daf8fd") * BrightnessMatrix(-0.01))],
            images=[
                "mod_assets/BG/s_house_night_off.png",
                "#ffffff0c",
            ],
            images_at=[
                [Transform(yzoom=0.8, xzoom=-0.8, xycenter=(0.53, 0.75))],
                []
            ],
            color_images=False,
            suffix="_open"
        )
        background(
            "mc_bedroom", "mod_assets/BG/mc_bedroom_closed_base.png",
            variants=("day", "afternoon", "gray"),
            at_list=[Transform(matrixcolor=TintMatrix("#daf8fd") * BrightnessMatrix(-0.03))],
            suffix="_closed"
        )
        background(
            "mc_bedroom", "mod_assets/BG/mc_bedroom_closed_base.png",
            variants=("night",), color=False,
            suffix="_closed_on"
        )
        background(
            "mc_bedroom", "mod_assets/BG/mc_bedroom_closed_base.png",
            variants=("night",),
            suffix="_closed_off"
        )
        background(
            "mc_house_corridor", "mod_assets/BG/mc_house_corridor_day.png",
            variants=("day", "afternoon"),
        )

        background(
            "m_house", "mod_assets/BG/m_house_[_variant].jpg",
            variants=("day", "night_on", "night_off"), color=False
        )
        image("m_house_night_mbo_on", "mod_assets/BG/m_house_night_mbo_on.jpg")
        background(
            "m_office", "mod_assets/BG/m_office_[_variant].jpg",
            variants=("day", "afternoon", "night_on", "night_off"), color=False
        )
        background(
            "m_house_stairs", "mod_assets/BG/m_house_stairs_[_variant].jpg",
            variants=("day", "afternoon", "night_on", "night_off"), color=False
        )

        background_with_sky(
            "y_house", "mod_assets/BG/y_house_[_variant].png",
            variants=("day", "afternoon", "night_on", "night_off"), color=False, rain=RAIN_FRONT
        )

################ Streets ################
        background_with_sky(
            "city_street", "mod_assets/BG/city_street_[_variant].png",
            variants=("day", "afternoon", "night_on", "night_off", "night_on_nostars", "night_off_nostars"),
            color=False, rain=RAIN_FRONT
        )
        background_with_sky(
            "city_street", "mod_assets/BG/city_street_day.png",
            variants=("gray",), rain=RAIN_FRONT
        )

        background_with_sky(
            "city_street_2", "mod_assets/BG/city_street_2_[_variant].png",
            variants=("day", "gray", "afternoon", "night_on", "night_off", "night_on_nostars", "night_off_nostars"),
            color=False, rain=RAIN_FRONT
        )

        background_with_sky(
            "city_street_3", "mod_assets/BG/city_street_3_[_variant].png",
            variants=("day", "gray", "afternoon", "night_on", "night_off", "night_on_nostars", "night_off_nostars"),
            color=False, rain=RAIN_FRONT
        )

        background_with_sky(
            "city_street_4", "mod_assets/BG/city_street_4.png",
            variants=("day", "gray", "afternoon", "night", "night_nostars"), rain=RAIN_FRONT
        )

        background_with_sky(
            "residential", "mod_assets/BG/residential.png",
            variants=("day", "afternoon", "night_nostars", "night", "gray"), rain=RAIN_FRONT
        )
        background_with_sky(
            "residential", "mod_assets/BG/residential_snow.png",
            variants=("snow_day", "snow_night_nostars", "snow_night"), rain=RAIN_FRONT
        )

################ City ################
        image("jewellery_store", "mod_assets/BG/jewellery_store.jpg")

        background_with_sky(
            "park", "mod_assets/BG/park.png",
            variants=("day", "afternoon", "gray", "night", "night_nostars")
        )

        background(
            "cafe_kitchen", "mod_assets/BG/cafe_kitchen_[_variant].jpg",
            variants=("day", "afternoon", "night"), color=False
        ) 

        background(
            "cafe_inside", "mod_assets/BG/cafe_inside_[_variant].jpg",
            variants=("day", "afternoon", "night"), color=False
        )
        background(
            "cafe_inside", "mod_assets/BG/cafe_inside_day.jpg",
            variants=("gray",),
        )
        
        background_with_sky(
            "cafe_outside", "mod_assets/BG/cafe_outside_[_variant].png",
            variants=("day", "afternoon", "night_on", "night_off"), color=False, rain=RAIN_FRONT
        )
        background_with_sky(
            "cafe_outside", "mod_assets/BG/cafe_outside_day.png",
            variants=("gray",), rain=RAIN_FRONT
        )

        image("arcade", "mod_assets/BG/arcade.png")
        image("arcade2", "mod_assets/BG/arcade2.jpg")
        
        background_with_sky(
            "city_center", "mod_assets/BG/city_center_[_variant].png",
            variants=("day", "gray", "afternoon", "night_on", "night_off", "night_on_nostars", "night_off_nostars"),
            color=False
        )

        background(
            "restaurant1", "mod_assets/BG/restaurant1_[_variant].jpg",
            variants=("day", "afternoon", "night"), color=False
        )
        
        image("restaurant_sushi", "mod_assets/BG/restaurant_sushi.jpg")

        image("clothing_store", "mod_assets/BG/clothing_store.png")

        background_with_sky(
            "mall_int_1", "mod_assets/BG/mall_int_1_[_variant].png",
            variants=("day", "afternoon", "night"), color=False
        )
        background(
            "mall_int_2", "mod_assets/BG/mall_int_2_[_variant].png",
            variants=("day", "afternoon", "night"), color=False
        )

####

image black = Solid("#000")
image white = Solid("#fff")

image bg notebook = "bg/notebook.png"

image bg school_infirmary_day = "mod_assets/BG/school_infirmary_day.jpg"
image bg school_infirmary_afternoon = "mod_assets/BG/school_infirmary_afternoon.jpg"
image bg school_infirmary_gray = "mod_assets/BG/school_infirmary_gray.jpg"
image bg school_infirmary_night = Transform("mod_assets/BG/school_infirmary_night.jpg", matrixcolor=SaturationMatrix(0.8) * BrightnessMatrix(-0.06) * ContrastMatrix(1.35))

image bg school_stairs_day = "mod_assets/BG/school_stairs_day.jpg"
image bg school_stairs_gray = Transform("mod_assets/BG/school_stairs_day.jpg", matrixcolor=SaturationMatrix(0.8) * BrightnessMatrix(-0.1) * TintMatrix("#dbdbdb"))

image bg school_rooftop_access_day = "mod_assets/BG/school_rooftop_access_day.jpg"
image bg school_rooftop_access_afternoon = "mod_assets/BG/school_rooftop_access_afternoon.jpg"
image bg school_rooftop_access_gray = "mod_assets/BG/school_rooftop_access_gray.jpg"
image bg school_rooftop_access_night = "mod_assets/BG/school_rooftop_access_night.jpg"

image bg street 2 night snow = "mod_assets/BG/street_2_night_snow.png"

image bg m_bedroom_day = "mod_assets/BG/m_bedroom_day.png"
image bg m_bedroom_afternoon = "mod_assets/BG/m_bedroom_afternoon.png"
image bg m_bedroom_snow = "mod_assets/BG/m_bedroom_snow.png"
image bg m_bedroom_closed = "mod_assets/BG/m_bedroom_closed.png"
image bg m_bedroom_night = "mod_assets/BG/m_bedroom_night.png"

image bg am_bedroom_day_open = "mod_assets/BG/am_bedroom_day_open.jpg"
image bg am_bedroom_day_closed = "mod_assets/BG/am_bedroom_day_closed.jpg"
image bg am_bedroom_afternoon_open = "mod_assets/BG/am_bedroom_afternoon_open.jpg"
image bg am_bedroom_snow_open = "mod_assets/BG/am_bedroom_snow_open.jpg"
image bg am_bedroom_night_on_closed = "mod_assets/BG/am_bedroom_night_on_closed.jpg"
image bg am_bedroom_night_off_closed = "mod_assets/BG/am_bedroom_night_off_closed.jpg"