class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = 0
        for i in range(len(nums)):
            s += nums[i]
        if s%2 != 0:
            return False
        ss = s//2
        def dfs(i,target):
            if target == 0:
                return True 

            if i == len(nums):
                return False

            return (dfs(i+1,target-nums[i]) or dfs(i+1,target))
        return dfs(0,ss)