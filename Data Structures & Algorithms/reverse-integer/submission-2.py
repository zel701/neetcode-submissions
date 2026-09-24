class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        negative = False
        if x<0:
            negative = True
            x = -x
        while x!=0:
            res*=10
            res += x%10
            x//=10
        if res> (0xFFFFFFFF/2):
            return 0
        if negative:
            return -res
        return res