class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0

        for i in range(len(s)):
            a = set()   # reset for each starting index

            for j in range(i, len(s)):
                if s[j] in a:
                    break
                a.add(s[j])
                length = max(length, len(a))

        return length
        