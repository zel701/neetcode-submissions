class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[r] == target:
                return r
            if nums[l] == target:
                return l
            #rotate after mid
            if nums[r]  < nums[mid] and target > nums[mid]:
                l = mid +1
            elif nums[r]  < nums[mid] and target < nums[r] <nums[mid]:
                l = mid +1
            #no rotate after mid, target within range of mid, r
            elif nums[r] > nums[mid] and nums[mid] < target <= nums[r]:
                l = mid +1
            
            
            else:
                r = mid -1
            
        return -1