class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        best = 0
        
        while l < r:

            width = r - l
            water = min(heights[l], heights[r]) * width

            if water > best:
                best = water

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return best
        