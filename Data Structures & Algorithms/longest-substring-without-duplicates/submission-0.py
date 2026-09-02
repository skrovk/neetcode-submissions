class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = dict()

        longest = 0
        curr_len = 0

        while right < len(s):
            if (seen.get(s[right]) is not None) and (seen[s[right]] >= left):
                left = seen[s[right]] + 1
                seen[s[right]] = right
                longest = curr_len if curr_len > longest else longest
                curr_len = right - left + 1
            else:
                seen[s[right]] = right
                curr_len += 1

            right += 1

        longest = curr_len if curr_len > longest else longest
            
        return longest

