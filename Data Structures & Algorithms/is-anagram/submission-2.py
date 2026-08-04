class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}

        if not t:
            return False
        if not s:
            return False
        
        for i in s:
            if i in s_chars:
                s_chars[i] += 1
            else:                
                s_chars[i] = 1

        for i in t:
            if i in t_chars:
                t_chars[i] += 1
            else:
                t_chars[i] = 1

            if i not in s_chars:
                return False
            
            if t_chars[i] > s_chars[i]:
                return False

        for i in s_chars:
            if i not in t_chars:
                return False

            if t_chars[i] < s_chars[i]:
                return False

        return True
        
            