class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        windowCount = defaultdict(int)
        currentMaxCount = 0
        maximum = 0
        while r<len(s):
            windowCount[s[r]]+=1
            currentMaxCount = max(currentMaxCount,windowCount[s[r]])
            r+=1
            while r-l-currentMaxCount > k:
                print(maximum,l,r)
                windowCount[s[l]]-=1
                l+=1
            maximum = max(maximum,r-l)
        return maximum