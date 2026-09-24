class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxL = 0
        for i in wordDict:
            maxL = max(maxL,len(i))
        wordDict = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(dp)):
            for j in range(i,-1,-1):
                print(s[j:i])
                if s[j:i] in wordDict:
                    if dp[j]:
                        dp[i] = True
                if i-j > maxL:
                    break
        return dp[-1]