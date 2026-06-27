class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        max_water = min(heights[left], heights[right]) * (right-left)
        while left < right:
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -=1
            else:
                left +=1
                right -=1
            max_water = max(max_water, min(heights[left], heights[right]) * (right-left))
        return max_water
