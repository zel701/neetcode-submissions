class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)-1
        line = -1
        while low<=high:
            mid = (low+high)//2
            if matrix[mid][-1] >= target >= matrix[mid][0]:
                line = mid
                break
            if matrix[mid][-1]<target:
                low = mid+1
            else:
                high = mid-1
        if line != -1:
            l = 0
            r = len(matrix[0])-1
            while l<=r:
                mid = (l+r)//2
                if matrix[line][mid] == target:
                    return True
                elif matrix[line][mid] > target:
                    r = mid-1
                else:
                    l=mid+1
        return False

