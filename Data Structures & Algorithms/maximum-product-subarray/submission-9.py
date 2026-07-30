class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [1] * (len(nums))
        dp2 = [1] * (len(nums))
        dp1[0] = nums[0]
        dp2[0] = nums[0] 
        res = nums[0]
        for i in range(1,len(nums)):
            dp1[i] = max(nums[i], nums[i] * dp1[i-1], nums[i]*dp2[i-1])
            dp2[i] = min(nums[i],nums[i] * dp1[i-1], nums[i] * dp2[i-1])
            res = max(res, dp1[i])
        return res
