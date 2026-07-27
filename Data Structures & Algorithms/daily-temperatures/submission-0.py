class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            stack.append(0)
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    stack[i] = j - i
                    break
        return stack