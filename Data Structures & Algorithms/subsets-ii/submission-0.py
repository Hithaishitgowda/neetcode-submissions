class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        start = []

        nums.sort()
        def backtrack(i):
            if i == len(nums):
                output.append(start.copy())
                return

            start.append(nums[i])
            backtrack(i+1)

            while i+1 < len(nums) and nums[i+1] in start:
                i += 1

            start.pop()
            backtrack(i+1)

        backtrack(0)
        return output