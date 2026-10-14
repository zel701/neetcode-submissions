class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        current = 0
        for i in nums:
            if current+i < 0:
                current =0
            else:
                current+=i
            current_max = max(current,current_max)
        if current_max == 0 and max(nums) < 0:
            return max(nums)
        return current_max