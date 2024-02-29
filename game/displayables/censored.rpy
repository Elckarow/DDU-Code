default persistent.censor = False

python early:
    class Censored(object):
        def __init__(self, *rects, p=3, check_persistent=False, **kwargs):
            if not rects: raise ValueError("expected at least 1 rectangle")
            for rect in rects:
                if len(rect) != 4:
                    raise ValueError("a rect must be a 4-tuple")

            self.rects = rects
            self.p = p
            self.check_persistent = check_persistent
            self.kwargs = kwargs
        
        def __call__(self, child):
            return _Censored(child, self.rects, p=self.p, check_persistent=self.check_persistent, **self.kwargs)

    class _Censored(renpy.Container):
        def __init__(self, child, rects, p, check_persistent, **kwargs):
            super(_Censored, self).__init__(child, **kwargs)

            mask = Flatten(
                Fixed(
                    *[
                        Solid("#fff", xysize=(w, h), pos=(x, y))
                        for x, y, w, h in rects
                    ]
                )
            )

            self.not_pixelated = AlphaMask(self.child, mask, invert=True)
            self.pixelated = AlphaMask(Transform(self.child, pixellate=p), mask)
            self.check_persistent = check_persistent
        
        def render(self, w, h, st, at):
            if self.check_persistent and persistent.censor:
                return renpy.render(self.child, w, h, st, at)
        
            not_pixelated = renpy.render(self.not_pixelated, w, h, st, at)
            pixelated = renpy.render(self.pixelated, w, h, st, at)

            rv = renpy.Render(*not_pixelated.get_size())
            rv.blit(pixelated, (0, 0), focus=False, main=False)
            rv.blit(not_pixelated, (0, 0), focus=True, main=True)

            rv = render_utils.flatten(rv)
            return rv

        def get_placement(self):
            return self.child.get_placement()