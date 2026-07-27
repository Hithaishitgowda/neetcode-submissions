class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        for i in range (len(heights)-1):
            j = len(heights)-1
            while j > i:
                width = j - i
                height = min(heights[i], heights[j])
                area = width * height
                max_area = max(area, max_area)
                j -= 1
        return max_area
        