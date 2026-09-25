class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        result = [0] * (len(num1)+len(num2))
        for i in range(len(num2)-1,-1,-1):
            for j in range(len(num1)-1,-1,-1):
                c1 = int(num1[j])
                c2 = int(num2[i])
                result[j+i+1] += c1*c2
                result[j+i] += result[j+i+1]//10
                result[j+i+1] %= 10
        for i in range(len(result)):
            result[i] = str(result[i])
        for i in range(len(result)):
            if result[i]!="0":
                result = result[i:]
                break
        return "".join(result)

