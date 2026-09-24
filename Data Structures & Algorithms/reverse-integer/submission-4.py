class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        negative = False
        MIN = -2 ** 31
        MAX = 2** 31 -1
        if x<0:
            negative = True
            if x<MIN:
                return 0
            x = -x
        while x!=0:
            if res>MAX//10:
                return 0
            res*=10
            res += x%10
            x//=10
        if negative:
            return -res
        return res