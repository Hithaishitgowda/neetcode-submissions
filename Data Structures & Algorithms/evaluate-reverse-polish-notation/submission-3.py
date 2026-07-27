class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit():
                stack.append(int(i))
            elif i in ["+","-","*","/"]:
                if i == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)
                if i == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                if i == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                if i == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
            else:
                stack.append(int(i))
        return stack.pop()
