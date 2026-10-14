class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        next_fur = 0
        count = 0
        for i in range(len(nums)):
            if i>furthest:
                count+=1
                furthest = next_fur
            current = i+nums[i]
            next_fur = max(next_fur,current)
        return count