class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numdict = {}
        for i in nums:
            if i not in numdict:
                numdict[i] = 1
            elif i in numdict:
                return True 
        return False
         