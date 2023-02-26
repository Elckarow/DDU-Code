python early:
    class CharacterCompletion(object):
        """
        A class used to know how far the player is in the route completion of a certain character.

        `name`: str
            The name of the character.
        
        `endings`: int
            The number of endings the character has.
        
        `cgs`: int
            The number of cgs the character has.
        """

        def __init__(self, name, endings, cgs):
            self.name = name

            self._endings = [False] * endings
            self._cgs = [False] * cgs
        
        def mark_ending(self, i):
            """
            Marks the `i`th ending as 'reached', then saves the persistent data.
            """
            i -= 1
            if self._endings[i]: return
            self._endings[i] = True
            renpy.save_persistent()

        def mark_cg(self, i):
            """
            Marks the `i`th cg as 'seen', then saves the persistent data.
            """
            i -= 1
            if self._cgs[i]: return
            self._cgs[i] = True
            renpy.save_persistent()
        
        @property
        def completed(self):
            """
            Returns if the character route has been completed (if every cg has been seen and if every ending has been reached).
            """
            return all(self._endings) and all(self._cgs)
        
        def get_completion(self, rounded=2, percentage=False, string=False):
            """
            Returns a value representing the progress of the character route.
            
            `rounded`: int
                Rounds the value to that level of precision when needed.
            
            `percentage`: bool
                If true, multiplies the value by `100`.
            
            `string`: bool
                If true, the value returned will be a string of the value found (which is a float).
                If `percentage` is true, ' %' is appended at the end of the string.
            """
            d = float(len(self._endings) + len(self._cgs))

            if d == 0.0:
                rv = 1.0

            else:
                # we can do that safely because bool is a subclass of int
                # True == 1
                # False == 0
                completed = float(sum(self._endings + self._cgs))
 
                rv = completed / d
            
            rv = round(float(rv), rounded)

            if percentage:
                rv *= 100

            if string:
                rv = str(rv)

                if percentage:
                    rv += " %"

            return rv
        
        def force_complete(self):
            """
            Sets everything to `True`.
            Can only be used with developper mode on (obviously).
            """
            if not config.developer: return

            self._endings = [True] * len(self._endings)
            self._cgs = [True] * len(self._cgs)
            renpy.save_persistent()
        
        @classmethod
        def _reconstruct(cls, name, endings, cgs):
            """
            Reconstructs the pickled instance.
            """
            rv = cls(name, 0, 0)
            rv._endings = endings
            rv._cgs = cgs
            return rv

        def __reduce__(self):
            """
            Needed for pickling since persistent data will have an instance of this class as value.
            """
            return (self._reconstruct, (self.name, self._endings, self._cgs))
        
        def __eq__(self, other):
            if type(self) is not type(other): return False
            return (
                self.name == other.name
                and self._endings == other._endings
                and self._cgs == other._cgs
            )
        
        def __ne__(self, other):
            return not self == other

# init 100 python:
#     persistent.mc.force_complete()
#     persistent.amelia.force_complete()
#     persistent.yuri.force_complete()
#     persistent.monika.force_complete()
#     persistent.natsuki.force_complete()
#     persistent.sayori.force_complete()

default persistent.mc      = CharacterCompletion("mc", 0, 2)
default persistent.amelia  = CharacterCompletion("amelia", 0, 1)
default persistent.yuri    = CharacterCompletion("yuri", 1, 1)
default persistent.monika  = CharacterCompletion("monika", 1, 1)
default persistent.natsuki = CharacterCompletion("natsuki", 1, 1)
default persistent.sayori  = CharacterCompletion("sayori", 1, 1)
