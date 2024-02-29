python early:
    class TriangleDisplayable(ShaderDisplayable):
        def __init__(self, pointA=(0.0, 1.0), pointB=(0.5, 0.0), pointC=(1.0, 1.0), color="#fff", **kwargs):
            uniforms = {
                "u_color": self.normalize_color(Color(color)),
                "u_border": 0.0,
            }
            super(TriangleDisplayable, self).__init__("shaders.triangle", uniforms=uniforms, **kwargs)
            
            self.pointA = pointA
            self.pointB = pointB
            self.pointC = pointC
        
        def render(self, w, h, st, at):              
            self.set_dynamic_uniform("u_pointA" , (self.to_float(self.pointA[0], w), self.to_float(self.pointA[1], h)))
            self.set_dynamic_uniform("u_pointB" , (self.to_float(self.pointB[0], w), self.to_float(self.pointB[1], h)))
            self.set_dynamic_uniform("u_pointC" , (self.to_float(self.pointC[0], w), self.to_float(self.pointC[1], h)))
            
            return super(TriangleDisplayable, self).render(w, h, st, at)
            
    renpy.register_shader("shaders.triangle", variables="""
        uniform float u_border;
        uniform vec4 u_color;
        uniform vec2 u_pointA;
        uniform vec2 u_pointB;
        uniform vec2 u_pointC;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 u_model_size;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec2 tA = u_pointA;
        vec2 tB = u_pointB;
        vec2 tC = u_pointC;

        vec2 vA = tC - tA;
        vec2 vB = tB - tA;
        vec2 vC = v_tex_coord - tA;
    
        float dotAA = dot(vA, vA);
        float dotAB = dot(vA, vB);
        float dotAC = dot(vA, vC);
        float dotBB = dot(vB, vB);
        float dotCB = dot(vB, vC);

        float invDenom = 1.0 / (dotAA * dotBB - dotAB * dotAB);
        float baryX = (dotBB * dotAC - dotAB * dotCB) * invDenom;
        float baryY = (dotAA * dotCB - dotAB * dotAC) * invDenom;

        float triangle = ((baryX >= 0.0) && (baryY >= 0.0) && (baryX + baryY <= 1.0)) ? 1.0 : 0.0;
        gl_FragColor = u_color * triangle;
    """)

    renpy.register_sl_displayable("triangle", TriangleDisplayable, "triangle") \
        .add_property("pointA") \
        .add_property("pointB") \
        .add_property("pointC") \
        .add_property("border") \
        .add_property("color")

style triangle is empty