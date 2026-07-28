class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        dp = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]

            result = 0

            for i in range(l, r + 1):

                coins = nums[l - 1] * nums[i] * nums[r + 1]

                coins += dfs(l, i - 1)
                coins += dfs(i + 1, r)

                result = max(result, coins)

            dp[(l, r)] = result

            return result

        return dfs(1, len(nums) - 2)