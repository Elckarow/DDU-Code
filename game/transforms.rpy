init python in atl_utils:
    @renpy.pure
    def yoffset(y=0.0, z=0.8, r=1.0):
        """
        +- 5 yoffset every 0.01 zoom
        """
        return y + ((5 * ((z - 0.8) / 0.01)) * r)

transform tcommon(x=640, y=0, z=0.8):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z * 0.95 alpha 0.0
        xcenter x yoffset atl_utils.yoffset(y - 20, z)
        easein 0.25 yoffset atl_utils.yoffset(y, z) zoom z alpha 1.0
    on replace:
        alpha 1.0
        parallel:
            easein 0.25 xcenter x zoom z
        parallel:
            easein 0.15 yoffset atl_utils.yoffset(y, z) ypos 1.03

transform tinstant(x=640, y=0, z=0.8):
    subpixel True xcenter x yoffset atl_utils.yoffset(y, z) zoom z alpha 1.0 yanchor 1.0 ypos 1.03

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

transform leftin(x=640, y=0, z=0.8):
    subpixel True xcenter -300 yoffset atl_utils.yoffset(y, z) yanchor 1.0 ypos 1.03 zoom z alpha 1.0 subpixel True
    easein 0.25 xcenter x

transform rightin(x=640, y=0, z=0.8):
    subpixel True xcenter config.screen_width + 300 yoffset atl_utils.yoffset(y, z) yanchor 1.0 ypos 1.03 zoom z alpha 1.0 subpixel True
    easein 0.25 xcenter x

transform thide(y=0, z=0.8):
    subpixel True
    on hide:
        easein 0.25 zoom z * 0.95 alpha 0.0 yoffset atl_utils.yoffset(y, z * 0.95)

transform lhide:
    subpixel True
    on hide:
        easeout 0.25 xcenter -300

transform rhide:
    subpixel True
    on hide:
        easeout 0.25 xcenter config.screen_width + 300

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


transform t51(y=0, z=0.8):
    tcommon(170, y=y, z=z)
transform t52(y=0, z=0.8):
    tcommon(405, y=y, z=z)
transform t53(y=0, z=0.8):
    tcommon(640, y=y, z=z)
transform t54(y=0, z=0.8):
    tcommon(875, y=y, z=z)
transform t55(y=0, z=0.8):
    tcommon(1110, y=y, z=z)

transform t41(y=0, z=0.8):
    tcommon(200, y=y, z=z)
transform t42(y=0, z=0.8):
    tcommon(493, y=y, z=z)
transform t43(y=0, z=0.8):
    tcommon(786, y=y, z=z)
transform t44(y=0, z=0.8):
    tcommon(1080, y=y, z=z)

transform t31(y=0, z=0.8):
    tcommon(240, y=y, z=z)
transform t32(y=0, z=0.8):
    tcommon(640, y=y, z=z)
transform t33(y=0, z=0.8):
    tcommon(1040, y=y, z=z)

transform t21(y=0, z=0.8):
    tcommon(400, y=y, z=z)
transform t22(y=0, z=0.8):
    tcommon(880, y=y, z=z)

transform t11(y=0, z=0.8):
    tcommon(640, y=y, z=z)

transform i51(y=0, z=0.8):
    tinstant(170, y=y, z=z)
transform i52(y=0, z=0.8):
    tinstant(405, y=y, z=z)
transform i53(y=0, z=0.8):
    tinstant(640, y=y, z=z)
transform i54(y=0, z=0.8):
    tinstant(875, y=y, z=z)
transform i55(y=0, z=0.8):
    tinstant(1110, y=y, z=z)

transform i41(y=0, z=0.8):
    tinstant(200, y=y, z=z)
transform i42(y=0, z=0.8):
    tinstant(493, y=y, z=z)
transform i43(y=0, z=0.8):
    tinstant(786, y=y, z=z)
transform i44(y=0, z=0.8):
    tinstant(1080, y=y, z=z)

transform i31(y=0, z=0.8):
    tinstant(240, y=y, z=z)
transform i32(y=0, z=0.8):
    tinstant(640, y=y, z=z)
transform i33(y=0, z=0.8):
    tinstant(1040, y=y, z=z)

transform i21(y=0, z=0.8):
    tinstant(400, y=y, z=z)
transform i22(y=0, z=0.8):
    tinstant(880, y=y, z=z)

transform i11(y=0, z=0.8):
    tinstant(640, y=y, z=z)

transform l51(y=0, z=0.8):
    leftin(170, y=y, z=z)
transform l52(y=0, z=0.8):
    leftin(405, y=y, z=z)
transform l53(y=0, z=0.8):
    leftin(640, y=y, z=z)
transform l54(y=0, z=0.8):
    leftin(875, y=y, z=z)
transform l55(y=0, z=0.8):
    leftin(1110, y=y, z=z)

transform l41(y=0, z=0.8):
    leftin(200, y=y, z=z)
transform l42(y=0, z=0.8):
    leftin(493, y=y, z=z)
transform l43(y=0, z=0.8):
    leftin(786, y=y, z=z)
transform l44(y=0, z=0.8):
    leftin(1080, y=y, z=z)

transform l31(y=0, z=0.8):
    leftin(240, y=y, z=z)
transform l32(y=0, z=0.8):
    leftin(640, y=y, z=z)
transform l33(y=0, z=0.8):
    leftin(1040, y=y, z=z)

transform l21(y=0, z=0.8):
    leftin(400, y=y, z=z)
transform l22(y=0, z=0.8):
    leftin(880, y=y, z=z)

transform l11(y=0, z=0.8):
    leftin(640, y=y, z=z)

transform r51(y=0, z=0.8):
    rightin(170, y=y, z=z)
transform r52(y=0, z=0.8):
    rightin(405, y=y, z=z)
transform r53(y=0, z=0.8):
    rightin(640, y=y, z=z)
transform r54(y=0, z=0.8):
    rightin(875, y=y, z=z)
transform r55(y=0, z=0.8):
    rightin(1110, y=y, z=z)

transform r41(y=0, z=0.8):
    rightin(200, y=y, z=z)
transform r42(y=0, z=0.8):
    rightin(493, y=y, z=z)
transform r43(y=0, z=0.8):
    rightin(786, y=y, z=z)
transform r44(y=0, z=0.8):
    rightin(1080, y=y, z=z)

transform r31(y=0, z=0.8):
    rightin(240, y=y, z=z)
transform r32(y=0, z=0.8):
    rightin(640, y=y, z=z)
transform r33(y=0, z=0.8):
    rightin(1040, y=y, z=z)

transform r21(y=0, z=0.8):
    rightin(400, y=y, z=z)
transform r22(y=0, z=0.8):
    rightin(880, y=y, z=z)

transform r11(y=0, z=0.8):
    rightin(640, y=y, z=z)




transform flash(t=0.3):
    alpha 0.0 mesh True
    ease t alpha 1.0
    ease t alpha 0.0