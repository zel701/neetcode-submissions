class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = ""
        maxlen = 0
        currentlen = 0
        i = 0
        l = 0 
        r = 0
        while i < len(s):
            l = i
            r = i
            currentlen = 1
            while l-1 >=0 and s[l-1] == s[r]:
                currentlen +=1
                l -= 1
            while l-1 >=0 and r+1 < len(s) and s[l-1] == s[r+1]:
                currentlen += 2
                l-=1
                r+=1
            if currentlen > maxlen:
                maxlen = currentlen
                res = s[l:r+1]
            currentlen = 0
            i+=1
        return res
                

        