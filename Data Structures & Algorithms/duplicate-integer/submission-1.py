class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0) 
        for j in count.values():
            if j > 1:
                return True 
        
        return False
         

