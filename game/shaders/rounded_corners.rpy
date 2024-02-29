python early:
    _rounded_corners_relative = {
        None: 0.0,
        "min": 1.0,
        "max": 2.0,
        "width": 3.0,
        "height": 4.0,
    }

    renpy.register_shader("shaders.rounded_corners", variables="""
        uniform vec4 u_radius;
        uniform float u_relative;
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 u_model_size;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        float rounded_rectangle(vec2 uv_minus_center, vec2 center, float radius) {
            return length(max(abs(uv_minus_center) - center + radius, 0.0)) - radius;
        }

        float get_radius(vec2 uv_minus_center, vec4 radius) {
            vec2 xy = (uv_minus_center.x > 0.0) ? radius.xy : radius.zw;
            float r = (uv_minus_center.y > 0.0) ? xy.x : xy.y;
            return r;
        }
    """, fragment_200="""
        vec2 center = u_model_size.xy / 2.0;
        vec2 uv = (v_tex_coord.xy * u_model_size.xy);

        vec2 uv_minus_center = uv - center;
        float radius = get_radius(uv_minus_center, u_radius);

        if (u_relative != 0.0) {
            float side_size;
            if (u_relative == 1.0) {
                side_size = u_model_size.x;
            } else if (u_relative == 2.0) {
                side_size = u_model_size.y;
            } else if (u_relative == 3.0) {
                side_size = min(u_model_size.x, u_model_size.y);
            } else {
                side_size = max(u_model_size.x, u_model_size.y);
            }

            radius *= side_size;
        }

        float crop = rounded_rectangle(uv_minus_center, center, radius);

        vec4 color = texture2D(tex0, v_tex_coord);
        gl_FragColor = mix(color, vec4(0.0), smoothstep(0.0, 1.0, crop));
    """)

transform -600 RoundedCorners(radius, relative=None):
    mesh True shader "shaders.rounded_corners"
    u_radius (radius if isinstance(radius, tuple) else (radius,) * 4) u_relative _rounded_corners_relative.get(relative, 0.0)