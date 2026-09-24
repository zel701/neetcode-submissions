class Solution:
    def isHappy(self, n: int) -> bool:
        numset = set()
        while n !=1:
            print(numset)
            if n in numset:
                return False
            else:
                numset.add(n)
            nxt = 0
            while n!=0:
                nxt += (n%10)**2
                n=n//10
            n = nxt
        return True