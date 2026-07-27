class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        start =[]
        output = []

        def backtrack(i):
            if sum(start) == target:
                output.append(start.copy())
                return 

            if (i >= len(nums)) or sum(start) > target:
                return

            start.append(nums[i])
            backtrack(i)

            start.pop()

            backtrack(i+1)

        backtrack(0)
        return output