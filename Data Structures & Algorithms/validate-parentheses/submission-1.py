class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if ((i == '(') or (i == '[') or (i == '{')):
                stack.append(i)
                continue

            if not stack:
                return False

            left = stack.pop()

            if (i == ')') and (left != '('):
                return False

            if (i == ']') and (left != '['):
                return False

            if (i == '}') and (left != '{'):
                return False

        if stack:
            return False

        return True

            

            

            