python early:
    renpy.register_shader("shaders.fading_borders", variables="""
        uniform vec4 u_radius;
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 u_model_size;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec2 uv = (v_tex_coord - 0.5) * 2.0;
        vec2 pos = uv * u_model_size;

        float xradius = ((uv.x < 0.0) ? u_radius.x : u_radius.z) * 2.0;
        float xfade = 1 - smoothstep(u_model_size.x - xradius, u_model_size.x, abs(pos.x));

        float yradius = ((uv.y < 0.0) ? u_radius.y : u_radius.w) * 2.0;
        float yfade = 1 - smoothstep(u_model_size.y - yradius, u_model_size.y, abs(pos.y));

        float fade = xfade * yfade;

        vec4 color = texture2D(tex0, v_tex_coord);
        gl_FragColor = color * fade;
    """)

transform -600 FadingBorders(radius):
    mesh True shader "shaders.fading_borders" u_radius (radius if isinstance(radius, tuple) else (radius,) * 4)