class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numdict = {}
        for i in nums:
            if i not in numdict:
                numdict[i] = 1
            elif i in numdict:
                numdict[i] = numdict[i]+1
        max = 0
        maxnumber = 0
        for i in numdict:
            if numdict[i]>max:
                max = numdict[i]
                maxnumber = i
        return maxnumber
            