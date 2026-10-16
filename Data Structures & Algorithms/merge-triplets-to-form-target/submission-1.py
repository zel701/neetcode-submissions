class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0,0,0]
        for i,j,k in triplets:
            if i == target[0] and j<=target[1] and k<= target[2]:
                res[0] = i
            if i <= target[0] and j==target[1] and k<= target[2]:
                res[1] = j
            if i <= target[0] and j<=target[1] and k== target[2]:
                res[2] = k
            if target == res:
                return True
        return target == res