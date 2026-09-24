class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        currentMax= nums[0]
        currentMin = nums[0]
        for i in range(1,len(nums)):
            premax = currentMax
            premin = currentMin
            currentMax = max(nums[i],nums[i]*premax,nums[i]*premin)
            currentMin = min(nums[i],nums[i]*premax,nums[i]*premin)
            ans = max(ans,currentMax)
        return ans