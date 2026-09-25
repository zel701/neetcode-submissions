class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total / 2
        dp = set()
        dp.add(0)
        for i in nums:
            newdp = []
            for j in dp:
                if i + j == half:
                    return True
                if i + j < half:
                    newdp.append(i+j)
            for k in newdp:
                if k not in dp:
                    dp.add(k)
        return False