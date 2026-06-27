class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques_substring_index = dict()
        max_len = 0
        start_substring = 0
        for i in range(len(s)):
            if uniques_substring_index.get(s[i], -1) >= start_substring:
                start_substring = uniques_substring_index.get(s[i], i)+1
                uniques_substring_index[s[i]] = i
                max_len = max(max_len, i - start_substring +1)
            else:
                uniques_substring_index[s[i]] = i
                max_len = max(max_len, i - start_substring +1)
        return max_len