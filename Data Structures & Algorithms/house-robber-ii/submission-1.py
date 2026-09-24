class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robhouses(houses):
            if len(houses) == 1:
                return houses[0]
            prev2 = houses[0]
            prev = max(houses[0],houses[1])
            i = 2
            while i < len(houses):
                current = max(prev2 + houses[i],prev)
                prev2 = prev
                prev = current
                i+=1
            return prev
        return max(robhouses(nums[1:]),robhouses(nums[:-1]))