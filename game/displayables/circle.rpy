python early:
    class CircleDisplayable(ShaderDisplayable):
        def __init__(self, border=None, radius=None, color="#fff", length=1.0, rotate=0, **kwargs):
            uniforms = {
                "u_color":  self.normalize_color(Color(color)),
                "u_length": min(max(length, 0.0), 1.0),
                "u_rotate": -90 + (rotate % 360)
            }
            super(CircleDisplayable, self).__init__("shaders.circle", uniforms, **kwargs)

            self.border = border
            self.radius = radius

        def render(self, w, h, st, at):
            if self.radius is None:
                radius = min(w, h) / 2.0
            else:
                radius = self.radius
            
            width = height = radius * 2.0
            
            border = self.border or radius
            if not border: return renpy.Render(width, height)

            self.set_dynamic_uniform("u_border", border)

            return super(CircleDisplayable, self).render(width, height, st, at)
    
    # modified code from https://www.shadertoy.com/view/Mll3D4
    renpy.register_shader("shaders.circle", variables="""
        uniform float u_border;
        uniform float u_rotate;
        uniform float u_length;
        uniform vec4 u_color;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 u_model_size;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        mat2 rotate_matrix(float x) {
            float radians_x = radians(x);
            return mat2(
                cos(radians_x), sin(radians_x),
                -sin(radians_x), cos(radians_x)
            );
        }

        mat2 rotate_to_top(float lenght) {
            float point_to_move = 1.0 - ((1.0 - lenght) / 2.0);
            float angle = -(point_to_move - 0.5) * 360;
            return rotate_matrix(angle);
        }
    """, fragment_200="""
        float kInvPi = 1.0 / 3.141592;

        vec2 center = u_model_size.xy / 2.0;
        vec2 uv = (v_tex_coord.xy * u_model_size.xy) - center;

        if (u_length < 1.0) {
            uv = (uv * 2.0) - 1.0;
            uv *= rotate_to_top(u_length);
            uv *= rotate_matrix(u_rotate);
            uv = (uv + 1.0) / 2.0;
        }

        float bluriness = 0.5;

        float d = length(uv);
        float wd = bluriness * fwidth(d);

        float radius = (min(u_model_size.x, u_model_size.y) / 2.0) - bluriness;
        float circle = smoothstep(radius + wd, radius - wd, d);
        
        float inner = radius - u_border;
        circle -= smoothstep(inner + wd, inner - wd, d);
        
        float angle = (atan(uv.x, uv.y) * kInvPi) / 2.0;
        angle = fract(angle);
        float wa = bluriness * fwidth(angle);

        float segment = smoothstep(u_length + wa, u_length - wa, angle);
        segment *= smoothstep(0.0, 2.0 * wa, angle);    
        circle *= mix(segment, 1.0, step(1.0, u_length));
    
        gl_FragColor = u_color * circle;
    """)

    renpy.register_sl_displayable("circle", CircleDisplayable, "circle") \
        .add_property("border") \
        .add_property("radius") \
        .add_property("color") \
        .add_property("length") \
        .add_property("rotate")

style circle is empty