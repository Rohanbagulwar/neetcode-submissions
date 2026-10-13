class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pt1 = 0
        height=heights
        pt2 = len(height) - 1
        ans = 0

        while pt1 < pt2:
            temp_ans = min(height[pt1], height[pt2]) * (pt2 - pt1)
            ans = max(ans, temp_ans)

            if height[pt1] <= height[pt2]:
                pt1 += 1
            else:
                pt2 -= 1
        return ans