class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for i in nums:
            if i not in numset:
                numset.add(i)
            else:
                return True
        return False
