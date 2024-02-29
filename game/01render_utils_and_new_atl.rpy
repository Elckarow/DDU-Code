default persistent.gaussian_blur = False

#################### render functions
python early in render_utils:
    """
    Cool functions for rendering.

    `wrap_render(render)` creates a new render of size `render`'s size, blits the original render onto it, and returns it.

    `blur(render, blur)` blurs the render. the blur used depends on `persistent.gaussian_blur`.

    `default_blur(render, blur)` and `gaussian_blur(render, blur)` each use their respective blur.

    `pixellate(render, p)` pixellates the render.

    `padding(render, padding)` adds padding to the render.

    `flatten(render)` flattens the render into a single texture.

    `crop(render, c)` crops the render.
    """
    from renpy.store import store
    from renpy.display.render import Render, BLIT, DISSOLVE, IMAGEDISSOLVE, PIXELLATE, FLATTEN
    from renpy.display.accelerator import relative
    from math import log, sqrt
    _constant = True

    ###########

    def wrap_render(render):
        rv = Render(*render.get_size())
        rv.blit(render, (0, 0))
        return rv

    ###########

    def default_blur(render, blur):
        rv = wrap_render(render)

        if not blur: return rv

        rv.mesh = True
        rv.add_shader("shaders.renpy_blur")

        rv.add_uniform("u_renpy_blur_log2", log(blur, 2))
        rv.add_uniform("u_lod_bias", 0.5)
        return rv

    def gaussian_blur(render, blur):
        if not blur: return wrap_render(render)

        rv = render

        for direction in ((0.0, 1.0), (1.0, 0.0)):
            rv = wrap_render(rv)
            rv.blit(render, (0.0, 0.0))
            rv.mesh = True
            rv.add_shader("shaders.gaussian_blur")

            sigma = blur / 2.0
            rv.add_uniform("u_radius", blur)
            rv.add_uniform("u_lod_bias", 0.5)
            rv.add_uniform("u_sigma", sigma)
            rv.add_uniform("u_sqr_sigma", sigma * sigma)
            rv.add_uniform("u_direction", direction)

        return rv

    def blur(render, blur):
        if store.persistent.gaussian_blur:
            rv = gaussian_blur(render, blur)
        else:
            blur = sqrt(blur) * 6
            rv = default_blur(render, blur)
        
        return rv

    renpy.register_shader("renpy.blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_renpy_blur_log2;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        gl_FragColor = texture2D(tex0, v_tex_coord);
    """)

    renpy.register_shader("shaders.renpy_blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_renpy_blur_log2;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        gl_FragColor = vec4(0.0);
        float renpy_blur_norm = 0.0;

        for (float i = -5.0; i < 1.0; i += 1.0) {
            float renpy_blur_weight = exp(-0.5 * pow(u_renpy_blur_log2 - i, 2.0));
            renpy_blur_norm += renpy_blur_weight;
        }

        gl_FragColor += renpy_blur_norm * texture2D(tex0, v_tex_coord.xy, 0.0);

        for (float i = 1.0; i < 14.0; i += 1.0) {

            if (i >= u_renpy_blur_log2 + 5.0) {
                break;
            }

            float renpy_blur_weight = exp(-0.5 * pow(u_renpy_blur_log2 - i, 2.0));
            gl_FragColor += renpy_blur_weight * texture2D(tex0, v_tex_coord.xy, i);
            renpy_blur_norm += renpy_blur_weight;
        }

        if (renpy_blur_norm > 0.0) {
            gl_FragColor /= renpy_blur_norm;
        } else {
            gl_FragColor = texture2D(tex0, v_tex_coord.xy, 0.0);
        }
    """)

    # gaussian blur from WM
    renpy.register_shader("shaders.gaussian_blur", variables="""
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

        for (float i=1.0; i <= u_radius; i++) {
            float weight = exp(-i * i / (2.0 * u_sqr_sigma));
            col += texture2D(tex0, v_tex_coord + u_direction * i / res0.xy, u_lod_bias) * weight;
            col += texture2D(tex0, v_tex_coord - u_direction * i / res0.xy, u_lod_bias) * weight;
            sum += weight * 2.0;
        }

        gl_FragColor = col / sum;
    """)

    ###########

    def pixellate(render, p):
        rv = wrap_render(render)

        if not p: return rv

        rv.mesh = True
        rv.add_shader("renpy.texture")
        rv.add_property("texture_scaling", "nearest_mipmap_nearest")
        rv.add_property("anisotropic", False)
        rv.add_uniform("u_lod_bias", p + 1)

        rv.operation = PIXELLATE
        rv.operation_parameter = 2 ** p
        return rv

    ###########

    def padding(render, padding):
        if padding is None:
            return wrap_render(render)

        if not isinstance(padding, tuple):
            raise Exception("padding must be a 2-tuple or a 4-tuple")
        
        l = len(padding)

        if l == 4:
            left, top, right, bottom = padding
        elif l == 2:
            right, bottom = padding
            left = right
            top = bottom
        else:
            raise Exception("padding must be a 2-tuple or a 4-tuple")

        rv = Render(left + render.width + right, top + render.height + bottom)
        rv.subpixel_blit(render, (left, top))

        return rv

    ###########

    def alpha(render, alpha, additive=0.0):
        rv = wrap_render(render)

        over = 1.0 - additive
        rv.alpha = alpha
        rv.over = over

        if (alpha != 1.0) or (over != 1.0):
            rv.add_shader("renpy.alpha")
            rv.add_uniform("u_renpy_alpha", alpha)
            rv.add_uniform("u_renpy_over", over)

        return rv

    ###########

    def flatten(render):
        rv = wrap_render(render)
        rv.mesh = True
        rv.add_shader("renpy.texture")
        rv.operation = FLATTEN
        
        return rv

    ###########

    def crop(render, c):
        width, height = render.get_size()

        x, y, w, h = c
        x = relative(x, width, width)
        y = relative(y, height, height)
        w = relative(w, width, width - x)
        h = relative(h, height, height - y)

        rv = Render(w, h)
        rv.subpixel_blit(render, (-x, -y))
        rv.xclipping = True
        rv.yclipping = True

        return rv

#################### override `Flatten`
python early:
    def Flatten(child, drawable_resolution=True):
        return Transform(child, mesh=True, gl_drawable_resolution=drawable_resolution)

#################### have all styles use `subpixel=True`
python early hide:
    for s in renpy.style.styles.values():
        s.subpixel = True

init 1500 python hide:
    for s in renpy.style.styles.values():
        s.subpixel = True
        
#################### atl stuff (im stuff)
python early in new_atl:
    from renpy.store import store
    from store.render_utils import wrap_render, blur as _blur, pixellate as _pixellate, default_blur as _default_blur, gaussian_blur as _gaussian_blur, padding as _padding
    from renpy.atl import float_or_none, any_object, bool_or_none
    _constant = True

    renpy.display.transform.TransformState.subpixel = True

    ###########

    render_functions = [ ]

    def new_transform_render(self, w, h, st, at):
        state = self.state
        rv = self.default_render(w, h, st, at)

        for f in render_functions:
            rv = f(state, rv)

        return rv

    if not hasattr(renpy.display.transform.Transform, "default_render"):
        renpy.display.transform.Transform.default_render = renpy.display.transform.Transform.render
        renpy.display.transform.Transform.render = new_transform_render
    
    ###########

    renpy.display.transform.add_property("padding", any_object, None)

    def padding(state, render):
        return _padding(render, state.padding)

    render_functions.append(padding)
    
    ###########

    renpy.display.transform.add_property("blur_gaussian", bool_or_none, None)
    
    def blur(state, render):
        blur = state.blur or 0.0
        gaussian = state.blur_gaussian

        if gaussian is None:
            return _blur(render, blur)

        if not gaussian:     
            return _default_blur(render, blur)

        return _gaussian_blur(render, blur)

    render_functions.append(blur)

    ###########

    renpy.display.transform.add_property("pixellate", float_or_none, None)

    def pixellate(state, render):
        return _pixellate(render, state.pixellate)

    render_functions.append(pixellate)