python early:
    class WaveDisplayable(renpy.Displayable):
        def __init__(self, color, thickness, amplitude=None, period=0.1, vertical=True, time_bias=1.0, offset=0.0, **kwargs):
            super(WaveDisplayable, self).__init__(**kwargs)
            self.color = Color(color)
            self.thickness = thickness
            self.amplitude = amplitude
            self.period = period
            self.vertical = vertical
            self.time_bias = time_bias
            self.offset = offset
        
        def render(self, w, h, st, at):
            thickness = self.thickness
            amplitude = self.amplitude
            vertical = self.vertical

            if vertical:
                if amplitude: amplitude *= 2
                else: amplitude = w
                rv = renpy.Render(thickness + amplitude, h)
                cr = renpy.Render(*rv.get_size())
                tex = renpy.display.draw.solid_texture(thickness, h, self.color) 
                cr.subpixel_blit(tex, (amplitude / 2.0, 0.0))
                rv.blit(cr, (0, 0))
                rv.add_uniform("u_direction", (1.0, 0.0))
            else:
                if amplitude: amplitude *= 2
                else: amplitude = h
                rv = renpy.Render(w, thickness + amplitude)
                cr = renpy.Render(*rv.get_size())
                tex = renpy.display.draw.solid_texture(w, thickness, self.color) 
                cr.subpixel_blit(tex, (0.0, amplitude / 2.0))
                rv.blit(cr, (0, 0))
                rv.add_uniform("u_direction", (0.0, 1.0))
            
            rv.mesh = True
            rv.add_shader("shaders.wave")
            rv.add_uniform("u_period", self.period)
            rv.add_uniform("u_time_bias", self.time_bias)
            rv.add_uniform("u_offset", self.offset)
            rv.add_property("gl_pixel_perfect", True)
            rv.add_property("gl_mipmap", False)
            
            renpy.redraw(self, 0.0)
            return rv
    
    renpy.register_shader("shaders.wave", variables="""
            uniform float u_time;
            uniform float u_period;
            uniform vec2 u_direction;
            uniform float u_time_bias;
            uniform float u_offset;
            uniform sampler2D tex0;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
            uniform vec2 u_model_size;
        """, vertex_400="""
            v_tex_coord = a_tex_coord;
        """, fragment_400="""
            vec2 uv = v_tex_coord;

            float time = u_time * u_time_bias;
            vec2 correction = 0.0545 * (200 + 200 + 10) / u_model_size.xy;

            vec2 vu = vec2(uv.y, uv.x) + u_offset;
            uv += (sin(vu / u_period + time) / (2.0 + correction)) * u_direction;

            vec4 color = vec4(1.0);
            color.a = (sin(time) + 1.0) / 2.0;

            gl_FragColor = texture2D(tex0, uv) * color;
        """)
    
    renpy.register_sl_displayable("wave", WaveDisplayable, "wave") \
        .add_property("color") \
        .add_property("thickness") \
        .add_property("amplitude") \
        .add_property("period") \
        .add_property("vertical") \
        .add_property("time_bias") \
        .add_property("offset")

style wave is empty