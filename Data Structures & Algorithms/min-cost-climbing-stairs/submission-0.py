class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf')] * (len(cost)+1)
        dp[0] = 0
        i = 2
        dp[1] = 0
        while i < len(dp):
            dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
            i+=1
        print(dp)
        return dp[-1]