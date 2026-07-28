from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        leftMax = 0
        rightMax = 0
        water = 0

        while i <= j:

            if height[i] <= height[j]:

                if height[i] >= leftMax:
                    leftMax = height[i]
                else:
                    water += leftMax - height[i]

                i += 1

            else:

                if height[j] >= rightMax:
                    rightMax = height[j]
                else:
                    water += rightMax - height[j]

                j -= 1

        return water


    

