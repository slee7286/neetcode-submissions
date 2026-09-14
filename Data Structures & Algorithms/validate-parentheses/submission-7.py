class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        stack = []

        for char in s:
            if char in matching:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return (len(stack) == 0)