import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        char_left = 0
        char_right = len(s) - 1

        while char_left < char_right:
            if s[char_left] != s[char_right]:
                return False

            char_left += 1
            char_right -= 1 

        return True