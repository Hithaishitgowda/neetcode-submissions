class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False

                x = stack.pop()

                if ch == ")" and x != "(":
                    return False
                elif ch == "}" and x != "{":
                    return False
                elif ch == "]" and x != "[":
                    return False

        return len(stack) == 0
            
