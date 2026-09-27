class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        sr = source[0]
        sc = source[1]
        tr = target[0]
        tc = target[1]

        if sr == tr and sc == tc:
            return 0
        elif sr == tr or sc == tc:
            return 1
        elif abs(sr-tr) == abs(sc-tc):
            return 1
        elif (sr+sc) == (tr+tc):
            return 1
        else:
            return 2
        