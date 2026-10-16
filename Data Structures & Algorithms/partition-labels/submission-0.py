class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters_pos = defaultdict(int)
        for i in range(len(s)):
            letters_pos[s[i]]=i
        could_end = 0
        count = 0
        res=[]
        for idx in range(len(s)):
            could_end = max(letters_pos[s[idx]],could_end)
            count+=1
            if could_end == idx:
                res.append(count)
                count = 0
                couldend = 0
        return res
        
