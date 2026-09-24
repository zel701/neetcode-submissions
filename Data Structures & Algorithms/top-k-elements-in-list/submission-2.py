class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] +=1
        numlist = list(set(nums))
        buckets = [[] for _ in range(len(nums)+1)]
        for i in numlist:
            buckets[count[i]].append(i)
        res = []
        for i in range(len(nums),-1,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res

        
