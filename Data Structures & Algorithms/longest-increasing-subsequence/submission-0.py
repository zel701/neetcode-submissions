class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            currentM = 0
            for j in range(i,-1,-1):
                if nums[j] < nums[i]:
                    currentM = max(currentM,dp[j]+1)
            dp[i] = max(dp[i],currentM)
        return max(dp)