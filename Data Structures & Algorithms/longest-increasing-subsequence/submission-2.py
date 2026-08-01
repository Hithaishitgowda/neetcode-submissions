class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bin_ser(array,num):
            i = 0
            j = len(array) - 1
            while i <= j:
                mid = (i+j)//2
                if array[mid] == num:
                    return mid
                if array[mid] < num:
                    i = mid + 1
                else:
                    j = mid - 1
            return i
        stack = []
        stack.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i] <= stack[-1]:
                idx = bin_ser(stack, nums[i])
                stack[idx] = nums[i]

            else:
                stack.append(nums[i])

        return len(stack)