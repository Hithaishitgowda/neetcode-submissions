class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def fab(i):
            if i == len(nums)-1:
                return nums[i]
            dp = [1] * (len(nums)-i)
            dp[0] = nums[i]
            res = dp[0]
            for j in range(i+1,len(nums)):
                dp[j-i] =  nums[j] * dp[(j-i)-1]
                res = max(res,dp[j-i])
            return res
        maxy = -float('inf')
        for k in range(len(nums)):
            maxy = max(maxy,fab(k))
        return maxy

        
