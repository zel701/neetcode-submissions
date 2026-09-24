class Solution:
    def isPalindrome(self, s: str) -> bool:
        olds = s.replace(" ","")
        olds = s.lower()
        s = []
        for i in olds:
            if i.isalpha() or i.isnumeric():
                s.append(i)
        mid = len(s)//2

        def expand(i,j,s):
            while i>=0:
                if s[i]!=s[j]:
                    return False
                i-=1
                j+=1
            return True
        if len(s)%2 == 1:
            return expand(mid,mid,s)
        else:
            return expand(mid-1,mid,s)
