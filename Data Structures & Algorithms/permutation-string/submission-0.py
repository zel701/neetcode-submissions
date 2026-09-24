class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i in s1:
            dict1[i]+=1
        l = 0
        r = 0
        while r<len(s2):
            
            dict2[s2[r]]+=1
            r+=1
            if dict1 == dict2:
                return True
            print(dict2)
            if r-l+1 > len(s1):
                dict2[s2[l]]-=1
                if dict2[s2[l]] == 0:
                    dict2.pop(s2[l])
                l+=1
            
        return False
