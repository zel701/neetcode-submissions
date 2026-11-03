class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if nums[i]>0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left<right:
                total = nums[left]+nums[right]+nums[i]
                if total == 0:
                    res.append([nums[left],nums[right],nums[i]])
                    right-=1
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                else:
                    if total>0:
                        right-=1
                    if total<0:
                        left+=1
                
        return res
