class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        start = []

        def backtrack(i):
            if len(start) == len(nums):
                output.append(start.copy())
                return
            for i in range(len(nums)):
                if nums[i] in start:
                    continue

                start.append(nums[i])
                backtrack(i)
                start.pop()

        backtrack(0)
        return output 