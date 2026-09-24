class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        product = math.factorial(len(nums))
        zero = False
        for i in nums:
            if i == 0:
                zero = True
            else:
                product /= i
        if not zero:
            return 0
        return int(product)