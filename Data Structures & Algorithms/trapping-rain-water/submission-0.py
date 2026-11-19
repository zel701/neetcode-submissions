class Solution:
    def trap(self, height: List[int]) -> int:
        heights = defaultdict(list)
        max_left = 0
        for i in range(len(height)):
            heights[i].append(max_left)
            max_left = max(max_left,height[i])
        max_right = 0
        for i in range(len(height)-1,-1,-1):
            heights[i].append(max_right)
            max_right = max(max_right,height[i])
        water = 0
        for i in range(len(height)):
            water += max(min(heights[i][0],heights[i][1])-height[i],0)
        return water