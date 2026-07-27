class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = []

        for i in range(len(numbers)):
            j = len(numbers) - 1
            while j > i:
                if numbers[i] + numbers[j] == target:
                    l.append(i+1)
                    l.append(j+1)
                j -= 1

        return l