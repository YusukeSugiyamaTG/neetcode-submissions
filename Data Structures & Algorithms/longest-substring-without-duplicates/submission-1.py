class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_str = 0
        str_set = set()

        for right in range(len(s)):
            while s[right] in str_set:
                str_set.remove(s[left])
                left += 1
            str_set.add(s[right])
            max_str = max(max_str, right - left + 1)
        return max_str