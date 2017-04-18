# make sure set.py from the Examples/Lecture7 directory is
# in your PYTHONPATH (copy file here, or add dir to env var)

from set import Set

class MultiSet(Set):
    """
    inherits all Set names, but extends intersect
    and union to support multiple operands; note
    that "self" is still the first argument (stored
    in the *args argument now); also note that the
    inherited & and | operators call the new methods
    here with 2 arguments, but processing more than 
    2 requires a method call, not an expression:
    """

    def intersect(self, *others):
        res = []
        for x in self:                     # scan first sequence
            for other in others:           # for all other args
                if x not in other: break   # item in each one?
            else:                          # no:  break out of loop
                res.append(x)              # yes: add item to end
        return Set(res)

    def union(*args):                      # self is args[0]
        res = []
        for seq in args:                   # for all args
            for x in seq:                  # for all nodes
                if not x in res:
                    res.append(x)          # add new items to result
        return Set(res)
