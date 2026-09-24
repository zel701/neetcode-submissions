class Solution:
    def rob(self, nums: List[int]) -> int:
        i = 2
        if len(nums) == 1:
            return nums[0]
        current = 0
        prev2 = nums[0]
        prev = max(nums[0],nums[1])
        while i < len(nums):

            current = max(prev,prev2+nums[i])
            prev2 = prev
            prev = current
            i+=1
        return prev