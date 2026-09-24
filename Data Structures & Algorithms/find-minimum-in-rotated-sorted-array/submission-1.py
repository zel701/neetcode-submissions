class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            print(mid)
            if mid == l:
                if nums[mid]<nums[mid+1]:
                    return nums[mid]
                else:
                    return nums[mid+1]
            elif nums[r] < nums[mid]:
                l = mid
            else:
                r = mid
        return nums[r]