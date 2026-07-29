class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def robber(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]

            if len(arr) == 1:
                return dp[0]

            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], arr[i] + dp[i-2])

            return dp[-1]

        return max(robber(nums[:-1]), robber(nums[1:]))