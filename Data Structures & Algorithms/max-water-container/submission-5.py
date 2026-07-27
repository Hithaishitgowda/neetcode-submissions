class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        i = 0 
        j = len(heights)-1
        while j > i:
            width = j - i
            height = min(heights[i], heights[j])
            area = width * height
            max_area = max(area, max_area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area
        