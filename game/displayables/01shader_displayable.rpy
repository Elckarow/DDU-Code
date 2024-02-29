python early:
    # taken from
    # https://github.com/WretchedTeam/WintermuteV3/blob/main/game/mod_code/backend/displayables.rpy
    class ShaderDisplayable(renpy.Displayable):
        """
        A displayable that uses a shader to create an image.
        """
        def __init__(self, shader, uniforms=None, properties=None, **kwargs):
            super(ShaderDisplayable, self).__init__(**kwargs)
            self.style.subpixel = True

            self.shader = shader
            self.uniforms = uniforms or {}
            self.properties = properties or {}

            # uniforms set in the render function
            # cleared after rendering
            self.dynamic_uniforms = {}
        
        def set_dynamic_uniform(self, name, value):
            self.dynamic_uniforms[name] = value
        
        def render(self, w, h, st, at):
            rv = renpy.Render(w, h)
            rv.mesh = renpy.gl2.gl2mesh2.Mesh2.texture_rectangle(
                0, 0, w, h,
                0.0, 0.0, 1.0, 1.0,
            )

            rv.add_shader(self.shader)
            for u_name, uniform in self.expand_dict(self.uniforms):
                rv.add_uniform(u_name, uniform)
            for u_name, uniform in self.expand_dict(self.dynamic_uniforms):
                rv.add_uniform(u_name, uniform)
            for p_name, property in self.expand_dict(self.properties):
                rv.add_property(p_name, property)
            
            self.dynamic_uniforms.clear()
            
            rv.add_property("gl_pixel_perfect", True)
            rv.add_property("gl_mipmap", False)
            return rv
        
        # some helper functions
        @staticmethod
        def expand_dict(d):
            for k, v in d.items():
                if isinstance(v, ColorMatrix):
                    v = v(None, 1.0)
                yield (k, v)
        
        @staticmethod
        def to_float(x, room):
            return x / room if type(x) is not float else x
    
        @staticmethod
        def to_absolute(x, room):
            return float(x * room if type(x) is float else x)
    
        @staticmethod
        def normalize_color(col):
            a = col[3] / 255.0        
            r = a * col[0] / 255.0        
            g = a * col[1] / 255.0        
            b = a * col[2] / 255.0        
            return (r, g, b, a)
        
        # always use subpixel=True
        def get_placement(self):
            xpos, ypos, xanchor, yanchor, xoffset, yoffset, _subpixel = super(ShaderDisplayable, self).get_placement()
            return (xpos, ypos, xanchor, yanchor, xoffset, yoffset, True)