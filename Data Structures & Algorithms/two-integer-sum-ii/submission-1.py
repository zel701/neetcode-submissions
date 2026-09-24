class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        right = len(numbers)-1
        while l<right:
            if numbers[l]+numbers[right] == target:
                return [l+1,right+1]
            elif numbers[l]+numbers[right] > target:
                right-=1
            elif numbers[l]+numbers[right] < target:
                l+=1
            