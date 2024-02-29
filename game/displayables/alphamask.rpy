python early:
    class AlphaMask(renpy.Container):
        """
        Improved implementation of AlphaMask.
        """

        offsets = [(0, 0), (0, 0)]
        invert = False

        def __init__(self, child, mask, invert=False, **properties):
            super(AlphaMask, self).__init__(**properties)
     
            self.mask = renpy.easy.displayable(mask)
            self.add(self.mask)
            self.add(child)

            self.invert = invert
         
        def render(self, w, h, st, at):
            cr = renpy.render(self.child, w, h, st, at)
     
            width, height = cr.get_size()
     
            mr = renpy.Render(width, height)
            mr.add_property("color_mask", (False, False, False, True))
            mr.place(self.mask, main=False)
     
            rv = renpy.Render(width, height)
            rv.blit(cr, (0, 0))
            rv.blit(mr, (0, 0), focus=False, main=False)
     
            rv.mesh = True
            rv.add_shader("renpy.mask")
     
            if self.invert:
                rv.add_uniform("u_renpy_mask_multiplier", -1)
                rv.add_uniform("u_renpy_mask_offset", 1)
            else:
                rv.add_uniform("u_renpy_mask_multiplier", 1)
                rv.add_uniform("u_renpy_mask_offset", 0)

            return rv
    
        def visit(self):
            return [self.mask, self.child]
    
    renpy.register_shader("renpy.mask", variables="""
        uniform float u_lod_bias;
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        uniform float u_renpy_mask_multiplier;
        uniform float u_renpy_mask_offset;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec4 src = texture2D(tex0, v_tex_coord.st, u_lod_bias);
        vec4 mask = texture2D(tex1, v_tex_coord.st, u_lod_bias);

        gl_FragColor = src * (mask.a * u_renpy_mask_multiplier + u_renpy_mask_offset);
    """)