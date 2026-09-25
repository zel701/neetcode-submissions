class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        left =0
        right = 0
        string = [] 
        for i in nums:
            left =0
            right = len(string)
            while left < right:
                mid = (left+right)//2
                if string[mid] >= i:
                    right = mid
                else:
                    left = mid+1

            if left == len(string):
                string.append(i)
            else:
                string[left] = i
        print(string)
        return len(string)