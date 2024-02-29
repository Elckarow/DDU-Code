init python:
    class Parallax(object):
        """
        A modifed version of parallax from another personal project.
        """
        __author__ = "RyzekNoavek#0624"

        def __init__(self, dist, speed=2.5):
            """
            `dist`
                The maximum allowance for the parallax movement.

            `speed`
                The speed multiplier for the effect to reach the max distance.
                Set to 2.5 by default.
            """

            self.dist = dist
            self.__last_st = 0.0
            self.final_x, self.final_y = 0, 0
            self.speed = speed

        def __call__(self, trans, st, at):
            x, y = renpy.get_mouse_pos()
            width, height = config.screen_width / 2., config.screen_height / 2.

            delta = st - self.__last_st
            self.__last_st = st

            x = x - width
            y = y - height

            x = self.dist * -(x / width)
            y = self.dist * -(y / height)

            if st < 0.0001:
                self.final_x, self.final_y = x, y

            else:
                self.final_x = self.final_x + ((x - self.final_x) * delta * self.speed)
                self.final_y = self.final_y + ((y - self.final_y) * delta * self.speed)

            trans.xoffset = self.final_x
            trans.yoffset = self.final_y
            return 0.0

    class ParallaxRotate(object):
        def __init__(self, mul):
            self.st = self.xrot = self.yrot = 0
            self.mul = mul

        def __call__(self, trans, st, at):
            delta = st - self.st
            self.st = st

            mx, my = renpy.get_mouse_pos()
            trans.perspective = True

            half_width = config.screen_width / 2.0
            half_height = config.screen_height / 2.0

            xrot = min((half_height - my) / half_height, 1.0) * 15.0 * self.mul
            yrot = min(-(half_width - mx) / half_width, 1.0) * 15.0 * self.mul

            self.xrot += (xrot - self.xrot) * delta
            self.yrot += (yrot - self.yrot) * delta

            trans.matrixtransform = RotateMatrix(self.xrot, self.yrot, 0.0)(None, 1.0)

            trans.xoffset = self.xrot * 7 ## OPTIONAL (moves camera on the x axis)
            trans.yoffset = self.yrot * -7 ## OPTIONAL (moves camera on the y axis)

            return 0.0
            
    class RotateMouseSmooth(object):
        def __init__(self, dist, speed=2.5, xpos=None, ypos=None):
            self.dist = dist
            self.speed = speed

            self.xpos = (xpos if xpos is not None else config.screen_width / 2.0)
            self.ypos = (ypos if ypos is not None else config.screen_height / 2.0)

            self.final_x = self.final_y = 0.0
            self.rot_x = self.rot_y = 0.0

            self.__last_st = 0.0

        def get_angle(self, x, y):
            return math.degrees(math.atan2(y, x)) + 90

        def __call__(self, trans, st, at):
            delta = st - self.__last_st
            self.__last_st = st

            x, y = renpy.get_mouse_pos()

            x -= self.xpos
            y -= self.ypos

            dx = self.dist * -(x / self.xpos)
            dy = self.dist * -(y / self.ypos)

            self.final_x += (dx - self.final_x) * delta * self.speed
            self.final_y += (dy - self.final_y) * delta * self.speed

            trans.xoffset = self.final_x
            trans.yoffset = self.final_y

            self.rot_x += (x - self.rot_x) * delta * self.speed
            self.rot_y += (y - self.rot_y) * delta * self.speed

            trans.rotate = self.get_angle(self.rot_x, self.rot_y)
            return 0.0