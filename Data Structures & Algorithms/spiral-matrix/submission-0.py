class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        w = len(matrix[0])-1
        h = len(matrix)-1
        left = 0
        right = w+1
        top = 0
        bottom = h +1
        remain = (w+1)*(h+1)
        res = []
        while remain>0:
            print(res)
            for x in range(left,right):
                res.append(matrix[top][x])
                remain-=1
            top+=1
            for x in range(top,bottom):
                res.append(matrix[x][right-1])
                remain-=1
            right-=1
            if remain == 0:
                break
            for x in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][x])
                remain-=1
            bottom-=1
            for x in range(bottom-1,top-1,-1):
                res.append(matrix[x][left])
                remain-=1
            left+=1
        return res