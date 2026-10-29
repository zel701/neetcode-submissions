class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        w = len(text1)
        h = len(text2)
        dp = [[0]*(w+1) for _ in range(h+1)]
        for i in range(1,h+1):
            for j in range(1,w+1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i][j])
                
        return dp[h][w]

