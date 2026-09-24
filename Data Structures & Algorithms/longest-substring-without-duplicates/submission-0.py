class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = set()
        l = 0
        r = 0
        currentLen = 0
        maxLen = 0
        while r < len(s):
            if s[r] not in current:
                currentLen+=1
                current.add(s[r])
                maxLen = max(currentLen,maxLen)
                r+=1
            else:
                while s[r] in current:
                    current.remove(s[l])
                    l+=1
                    currentLen-=1
        return maxLen