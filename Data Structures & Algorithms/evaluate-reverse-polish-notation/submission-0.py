class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+": "+",
            "-": "-",
            "*": "*",
            "/": "/"
        }
        stack = []
        res = 0
        for i in tokens:
            if i in op.values():
                print(i)
                if i == "+":
                    res = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif i == "-":
                    res = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif i == "*":
                    res = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif i == "/":
                    res = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
            else:
                print(i)
                stack.append(int(i))
        
        return int(stack[0])