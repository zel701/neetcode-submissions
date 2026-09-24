class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        i = 2
        if len(nums) == 1:
            return nums[0]
        dp[1] = max(nums[0],nums[1])
        while i < len(nums):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            i+=1
        return dp[-1]