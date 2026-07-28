class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, h = stack.pop()

                area = h * (i - index)
                result = max(result, area)

                start = index

            stack.append((start, height))

        for index, height in stack:
            area = height * (len(heights) - index)
            result = max(result, area)

        return result     