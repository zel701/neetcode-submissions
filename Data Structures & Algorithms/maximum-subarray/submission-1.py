class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        current = nums[0]
        for i in nums[1:]:
            current = max(i, current + i)
            current_max = max(current,current_max)
        return current_max