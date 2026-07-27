class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        start = []
        output = []

        def backtrack(i, total):
            if total == target:
                output.append(start.copy())
                return

            if total > target or i >= len(nums):
                return

            start.append(nums[i])
            backtrack(i, total + nums[i])  
            start.pop()

            backtrack(i + 1, total)

        backtrack(0, 0)
        return output