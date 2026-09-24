class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 31
        while count >= 0:
            current = n & 1
            if current:
                res |= (1 << count)
            n >>= 1
            count -=1 
        return res