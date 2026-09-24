class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum = max(piles)
        low = 1
        res = max(piles)
        def timeNeed(piles,k):
            time = 0
            for i in piles:
                if i%k!=0:
                    time+=(i//k) +1
                else:
                    time+=i//k
            return time
        while low<=minimum:
            
            time = 0
            mid = (low+minimum)//2
            time = timeNeed(piles,mid)
            print(mid)
            if time == h:
                if mid ==1:
                    return 1
                if timeNeed(piles,mid-1) > h:
                    return mid
                else:
                    res = mid
                    minimum = mid-1
            elif time > h:
                low = mid+1
            else:
                res = mid
                minimum = mid-1
        return res


