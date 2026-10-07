class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_pair = {')': '(', ']': '[', '}':'{'}

        for i in s:
            if i in open_pair.values():
                stack.append(i)
                continue

            if not stack:
                return False

            left = stack.pop()

            if open_pair.get(i, None) != left:
                return False

        if stack:
            return False

        return True

            

            

            