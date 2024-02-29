python early:
    class Completion(object):
        def __init__(self, endings, cgs):
            self.endings = array.array("b", [0] * endings)
            self.cgs = array.array("b", [0] * cgs)
        
        def mark_ending(self, i):
            """
            Marks the `i`th ending as 'reached', then saves the persistent data.
            """
            i -= 1
            if self.endings[i]: return
            self.endings[i] = 1
            renpy.save_persistent()

        def mark_cg(self, i):
            """
            Marks the `i`th cg as 'seen', then saves the persistent data.
            """
            i -= 1
            if self.cgs[i]: return
            self.cgs[i] = 1
            renpy.save_persistent()
        
        @property
        def completed(self):
            return all(self.endings) and all(self.cgs)
        
        def force_complete(self):
            """
            Sets everything to `True`.
            Can only be used with developper mode on (obviously).
            """
            if not config.developer: return

            for i in range(len(self.endings)):
                self.endings[i] = 1
            
            for i in range(len(self.cgs)):
                self.cgs[i] = 1

            renpy.save_persistent()
        
        @classmethod
        def _reconstruct(cls, endings, cgs):
            """
            Reconstructs the pickled instance.
            """
            rv = cls(0, 0)
            rv.endings = endings
            rv.cgs = cgs
            return rv

        def __reduce__(self):
            return (self._reconstruct, (self.endings, self.cgs))
        
        def __eq__(self, other):
            if type(self) is not type(other): return False
            return (
                self.endings == other.endings
                and self.cgs == other.cgs
            )
        
        def __ne__(self, other):
            return not self == other

default persistent.mc        = Completion(0, 2)
default persistent.amelia    = Completion(0, 1)
default persistent.yuri      = Completion(1, 2)
default persistent.monika    = Completion(1, 1)
default persistent.natsuki   = Completion(1, 2)
default persistent.sayori    = Completion(1, 3)
default persistent.sleepover = Completion(0, 4)

init python:
    def _force_all_complete():
        persistent.mc.force_complete()
        persistent.amelia.force_complete()
        persistent.yuri.force_complete()
        persistent.monika.force_complete()
        persistent.natsuki.force_complete()
        persistent.sayori.force_complete()
        persistent.sleepover.force_complete()