class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_left = 0
        max_right = 0
        water = 0
        while left<right:
            if height[left]<height[right]:
                max_left = max(max_left,height[left])
                water += max(max_left-height[left],0)
                left+=1
            else:
                max_right = max(max_right,height[right])
                water += max(max_right-height[right],0)
                right-=1
        return water