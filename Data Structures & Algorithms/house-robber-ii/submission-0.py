class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            dp[i] = max(dp[i-1],nums[i] + dp[i-2])

        nums1 = nums[::-1]

        m = len(nums1)
        dp1 = [0] * (m)
        dp1[0] = nums1[0]
        if len(nums1) == 1:
            return dp1[0]
        dp1[1] = max(nums1[0],nums1[1])
        for j in range(2,len(nums1)-1):
            dp1[j] = max(dp1[j-1],nums1[j] + dp1[j-2])

        return max(dp[n-2],dp1[n-2])