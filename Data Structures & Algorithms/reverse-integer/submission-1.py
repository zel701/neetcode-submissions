class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = -x
        x = str(x)
        x = list(x)
        x.reverse()
        x = "".join(x)
        x = int(x)
        if negative:
            x = -x
        if abs(x) > 0xFFFFFFFF/2:
            return 0
        return x