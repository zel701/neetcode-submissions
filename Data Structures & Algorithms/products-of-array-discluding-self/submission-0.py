class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * (len(nums))
        current = 1
        for i in range(len(nums)):
            sol[i] *= current
            current *= nums[i]
        current = 1
        for i in range(len(nums)-1,-1,-1):
            sol[i] *= current
            current *= nums[i]
        return sol
