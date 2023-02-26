init -100 python:
    # RoundedFrame by pseurae
    # https://gist.github.com/Pseurae/661e6084f756fc917b2889a386b16664
    # modified by yours truly (i don't know shit about OpenGL)

    renpy.register_shader("shader.rounded_corners", variables="""
        uniform vec4 u_radius;
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform vec2 u_model_size;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        // https://www.iquilezles.org/www/articles/distfunctions/distfunctions2d.htm
        float rounded_rectangle(in vec2 p, in vec2 b, in vec4 r)
        {
            r.xy = (p.x > 0.0) ? r.xy : r.zw;
            r.x  = (p.y > 0.0) ? r.x  : r.y;
            vec2 q = abs(p) - b + r.x;
            return min(max(q.x, q.y), 0.0) + length(max(q, 0.0)) - r.x;
        }
    """, fragment_200="""
        vec2 center = u_model_size.xy / 2.0;
        vec2 uv = (v_tex_coord.xy * u_model_size.xy);
        float crop = rounded_rectangle(uv - center, center, u_radius);
        vec4 color = texture2D(tex0, v_tex_coord);
        gl_FragColor = mix(vec4(0.0), color, smoothstep(1.0, 0.0, crop));
    """)
    
    # Blur and DropShadow from Wintermute
    # https://github.com/WretchedTeam/WintermuteV3

    renpy.register_shader("shaders.gaussian_blur_linear", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform float u_lod_bias;
        uniform float u_radius;
        uniform float u_sigma;
        uniform float u_sqr_sigma;
        uniform vec2 u_direction;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec4 col = texture2D(tex0, v_tex_coord, u_lod_bias);
        float sum = 1.0;
        for (float i=1.0; i <= u_radius; i+=2.0) {
            float weight1 = exp(-i * i / (2.0 * u_sqr_sigma));
            float i2 = (i + 1.0);
            float weight2 = exp(-i2 * i2 / (2.0 * u_sqr_sigma));
            vec2 offset1 = u_direction * (vec2(i) / res0.xy);
            vec2 offset2 = u_direction * (vec2(i2) / res0.xy);
            float weight = weight1 + weight2;
            vec2 offset = (offset1 * weight1 + offset2 * weight2) / weight;
            col += texture2D(tex0, v_tex_coord + offset, u_lod_bias) * weight;
            col += texture2D(tex0, v_tex_coord - offset, u_lod_bias) * weight;
            sum += weight * 2.0;
        }
        gl_FragColor = col / sum;
    """)

    renpy.register_shader("shaders.silhouette", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec4 u_color;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_400="""
        gl_FragColor = texture2D(tex0, v_tex_coord.xy).a * u_color;
    """)