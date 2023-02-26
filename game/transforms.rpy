transform tcommon(x=640, z=0.8):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z * 0.95 alpha 0.0
        xcenter x yoffset -20
        easein 0.25 yoffset 0 zoom z alpha 1.0
    on replace:
        alpha 1.0
        parallel:
            easein 0.25 xcenter x zoom z
        parallel:
            easein 0.15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.8):
    subpixel True
    xcenter x yoffset 0 zoom z alpha 1.0 yanchor 1.0 ypos 1.03

transform sinstant(x=640, z=0.8):
    subpixel True
    xcenter x yoffset 0 zoom z alpha 1.0 yanchor 1.0 ypos 1.06

transform finstant(x=640, z=0.8):
    subpixel True
    xcenter x yoffset 0 zoom z * 1.05 alpha 1.0 yanchor 1.0 ypos 1.03

transform focus(x=640, z=0.8):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:
        zoom z * 0.95 alpha 0.0
        xcenter x yoffset -20
        easein 0.25 yoffset 0 zoom z * 1.05 alpha 1.0
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.0
        parallel:
            easein 0.25 xcenter x zoom z * 1.05
        parallel:
            easein 0.15 yoffset 0

transform face(z=0.8, y=570, x=640, e_i=0.15, r=1):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z * 0.95 alpha 0.0
        xcenter x 
        easein 0.25 yoffset y zoom z * 2.1 alpha 1.0
    on replace:
        alpha 1.0
        parallel:
            easein 0.25 * r xcenter x  zoom z * 2.1
        parallel:
            easein e_i * r yoffset y

transform sink(x=640, z=0.8):
    subpixel True
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z alpha 1.0 subpixel True
    easein 0.5 ypos 1.06

transform hopfocus(x=640, z=0.8):
    subpixel True
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 alpha 1.0 subpixel True
    easein 0.1 yoffset -21 zoom z * 1.05
    easeout 0.1 yoffset 0

transform leftin(x=640, z=0.8):
    subpixel True
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z * 1.00 alpha 1.0 subpixel True
    easein 0.25 xcenter x

transform thide(z=0.8):
    subpixel True
    on hide:
        easein 0.25 zoom z * 0.95 alpha 0.0 yoffset -20

transform lhide:
    subpixel True
    on hide:
        easeout 0.25 xcenter -300

transform rhide:
    subpixel True
    on hide:
        easeout 0.25 xcenter 1700

transform hop(y=0):
    subpixel True
    easein 0.1 yoffset (y - 20)
    easeout 0.1 yoffset y
    
transform dip(y=0):
    subpixel True
    easein 0.15 yoffset (y + 25)
    easeout 0.15 yoffset y 

###############################################################################################
###Positions with animation###
###############################################################################################

transform hug:
    face(e_i=0.21, r=0.7, y=600)


transform t51:
    tcommon(170)
transform t52:
    tcommon(405)
transform t53:
    tcommon(640)
transform t54:
    tcommon(875)
transform t55:
    tcommon(1110)

transform t41:
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44:
    tcommon(1080)

transform t31:
    tcommon(240)
transform t32:
    tcommon(640)
transform t33:
    tcommon(1040)

transform t21:
    tcommon(400)
transform t22:
    tcommon(880)

transform t11:
    tcommon(640)

transform i51:
    tinstant(170)
transform i52:
    tinstant(405)
transform i53:
    tinstant(640)
transform i54:
    tinstant(875)
transform i55:
    tinstant(1110)

transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)

transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)

transform i21:
    tinstant(400)
transform i22:
    tinstant(880)

transform i11:
    tinstant(640)

transform f51:
    focus(170)
transform f52:
    focus(405)
transform f53:
    focus(640)
transform f54:
    focus(875)
transform f55:
    focus(1110)

transform f41:
    focus(200)
transform f42:
    focus(493)
transform f43:
    focus(786)
transform f44:
    focus(1080)

transform f31:
    focus(240)
transform f32:
    focus(640)
transform f33:
    focus(1040)

transform f21:
    focus(400)
transform f22:
    focus(880)

transform f11:
    focus(640)

transform if51:
    finstant(170)
transform if52:
    finstant(405)
transform if53:
    finstant(640)
transform if54:
    finstant(875)
transform if55:
    finstant(1110)

transform if41:
    finstant(200)
transform if42:
    finstant(493)
transform if43:
    finstant(786)
transform if44:
    finstant(1080)

transform if31:
    finstant(240)
transform if32:
    finstant(640)
transform if33:
    finstant(1040)

transform if21:
    finstant(400)
transform if22:
    finstant(880)

transform if11:
    finstant(640)

transform s51:
    sink(170)
transform s52:
    sink(405)
transform s53:
    sink(640)
transform s54:
    sink(875)
transform s55:
    sink(1110)

transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)

transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)

transform s21:
    sink(400)
transform s22:
    sink(880)

transform s11:
    sink(640)

transform si51:
    sinstant(170)
transform si52:
    sinstant(405)
transform si53:
    sinstant(640)
transform si54:
    sinstant(875)
transform si55:
    sinstant(1110)

transform si41:
    sinstant(200)
transform si42:
    sinstant(493)
transform si43:
    sinstant(786)
transform si44:
    sinstant(1080)

transform si31:
    sinstant(240)
transform si32:
    sinstant(640)
transform si33:
    sinstant(1040)

transform si21:
    sinstant(400)
transform si22:
    sinstant(880)

transform si11:
    sinstant(640)

transform h51:
    hop(170)
transform h52:
    hop(405)
transform h53:
    hop(640)
transform h54:
    hop(875)
transform h55:
    hop(1110)

transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)

transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)

transform h21:
    hop(400)
transform h22:
    hop(880)

transform h11:
    hop(640)

transform hf51:
    hopfocus(170)
transform hf52:
    hopfocus(405)
transform hf53:
    hopfocus(640)
transform hf54:
    hopfocus(875)
transform hf55:
    hopfocus(1110)

transform hf41:
    hopfocus(200)
transform hf42:
    hopfocus(493)
transform hf43:
    hopfocus(786)
transform hf44:
    hopfocus(1080)

transform hf31:
    hopfocus(240)
transform hf32:
    hopfocus(640)
transform hf33:
    hopfocus(1040)

transform hf21:
    hopfocus(400)
transform hf22:
    hopfocus(880)

transform hf11:
    hopfocus(640)

transform d51:
    dip(170)
transform d52:
    dip(405)
transform d53:
    dip(640)
transform d54:
    dip(875)
transform d55:
    dip(1110)

transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)

transform d31:
    dip(240)
transform d32:
    dip(640)
transform d33:
    dip(1040)

transform d21:
    dip(400)
transform d22:
    dip(880)

transform d11:
    dip(640)

transform l51:
    leftin(170)
transform l52:
    leftin(405)
transform l53:
    leftin(640)
transform l54:
    leftin(875)
transform l55:
    leftin(1110)

transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l44:
    leftin(1080)

transform l31:
    leftin(240)
transform l32:
    leftin(640)
transform l33:
    leftin(1040)

transform l21:
    leftin(400)
transform l22:
    leftin(880)

transform l11:
    leftin(640)

###############################################################################################
###Transitions for scenes###
###############################################################################################

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)
define wiperight = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64, reverse=True)

define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])

define flashback_scene = MultipleTransition([
    False, Dissolve(0.1),
    Solid("#fff"), Pause(2.1),
    Solid("#fff"), Dissolve(3.55),
    True])

define back_flashback_scene = MultipleTransition([
    False, Dissolve(3.55),
    Solid("#fff"), Pause(2.1),
    Solid("#fff"), Dissolve(0.1),
    True])

define fast_flashback_scene = MultipleTransition([
    False, Dissolve(0.09),
    Solid("#fff"), Pause(0.3),
    Solid("#fff"), Dissolve(0.3),
    True])

define fast_back_flashback_scene = MultipleTransition([
    False, Dissolve(0.3),
    Solid("#fff"), Pause(0.3),
    Solid("#fff"), Dissolve(0.09),
    True]) 

transform variant(saturation=1.0, light=0.0, color=(255, 255, 255)):
    matrixcolor SaturationMatrix(saturation) * BrightnessMatrix(light) * TintMatrix(color)

transform day:
    variant()

transform gray:
    variant(0.4, -0.15, "#cfcfcf")

transform afternoon:
    variant(light=0.05, color=(235, 195, 165))

transform night:
    variant(saturation=0.8, light=-0.03, color=(115, 115, 165))

transform night2:
    variant(saturation=0.97, light=-0.04, color=(115, 115, 185))



transform focus(i_brightness, f_brightness, i_blur, f_blur, t, warper=_warper.linear):
    matrixcolor BrightnessMatrix(i_brightness) blur i_blur
    warp warper t matrixcolor BrightnessMatrix(f_brightness) blur f_blur