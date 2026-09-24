class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        current = 0
        for i in nums:
            current = 0
            if i-1 not in numset:
                currentNum = i
                current +=1
                longest = max(current,longest)
                while currentNum+1 in numset:
                    current+=1
                    currentNum+=1
                    longest = max(current,longest)
        return longest