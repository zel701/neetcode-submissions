class Solution:
    def numDecodings(self, s: str) -> int:
        ways = [0] * len(s)
        valid = set()
        for i in range(1,27):
            valid.add(str(i))
        previous = s[0]
        if previous == "0":
            return 0
        ways[0] = 1
        for i in range(1,len(s)):
            current = previous + s[i]
            if s[i] in valid:
                ways[i] += ways[i-1]
            if current in valid:
                if i>=2:
                    ways[i] += ways[i-2]
                else:
                    ways[i] +=1
            previous = s[i]
        return ways[-1]