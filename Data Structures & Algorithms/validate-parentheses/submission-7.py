class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        close_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for c in s:
            if c not in close_open:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if close_open[c] != stack.pop():
                        return False
        if stack:
            return False
        return True
