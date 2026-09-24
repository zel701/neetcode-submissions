class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        sol = [-1,-1]
        for i in range(len(nums)):
            numdict[nums[i]] = i
        print(numdict)
        for j in range(len(nums)):
            if target-nums[j] in numdict:
                if numdict[target-nums[j]] !=j:
                    if numdict[target-nums[j]] > j:
                        sol = [j,numdict[target-nums[j]]]
                    else:
                        sol = [numdict[target-nums[j]],j]
        return sol