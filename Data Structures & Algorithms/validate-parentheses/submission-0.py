class Solution:
    def isValid(self, s: str) -> bool:
        d = {
        ")": "(",
        "}": "{",
        "]": "["
        }
        stack = []
        for v in s:
            if v in d.values():
                stack.append(v)
            elif v not in d.values():
                if  not stack or d[v] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False