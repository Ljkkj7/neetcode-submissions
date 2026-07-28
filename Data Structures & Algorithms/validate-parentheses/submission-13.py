class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in pairs:                      # it's a closer
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:                               # it's an opener
                stack.append(c)

        return not stack