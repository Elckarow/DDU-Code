python early:
    class Gradient(ShaderDisplayable):
        def __init__(self, start_color, end_color, theta=0, start_pos=0.0, end_pos=1.0, **kwargs):
            uniforms = {
                "u_start_color": self.normalize_color(Color(start_color)),
                "u_end_color": self.normalize_color(Color(end_color)),
                "u_theta": -theta - 90,
                "u_start_pos": start_pos,
                "u_end_pos": end_pos
            }
            properties = {"texture_scaling": "nearest"}
            super(Gradient, self).__init__("shaders.gradient", uniforms, properties, **kwargs)
    
    # https://github.com/WretchedTeam/WintermuteV3/blob/68415d2e1dd0e9b404361f1bd300084fa39fbfc0/game/mod_code/definitions/shaders/gradient.rpy
    renpy.register_shader("shaders.gradient", variables="""
        uniform float u_theta;
        uniform float u_start_pos;
        uniform float u_end_pos;
        uniform vec4 u_start_color;
        uniform vec4 u_end_color;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        mat2 rotate_matrix(float x) {
            return mat2(
                cos(radians(x)), -sin(radians(x)),
                sin(radians(x)), cos(radians(x))
            );
        }
        
        float map(float value, float min1, float max1, float min2, float max2) {
            return min2 + (value - min1) * (max2 - min2) / (max1 - min1);
        }
    """, fragment_200="""
        // Map it to (-1 and 1)
        vec2 uv = v_tex_coord.xy * 2.0 - 1.0;
        uv *= rotate_matrix(u_theta);
        // Map it back to (0 and 1) 
        uv = (uv + 1.0) / 2.0;
        float coeff = clamp(uv.x, 0.0, 1.0);
        coeff = map(coeff, u_start_pos, u_end_pos, 0.0, 1.0);
        gl_FragColor = mix(u_start_color, u_end_color, clamp(coeff, 0.0, 1.0));
    """)
    
    renpy.register_sl_displayable("gradient", Gradient, "gradient") \
        .add_positional("start_color") \
        .add_positional("end_color") \
        .add_property("theta") \
        .add_property("start_pos") \
        .add_property("end_pos")
        
style gradient is empty