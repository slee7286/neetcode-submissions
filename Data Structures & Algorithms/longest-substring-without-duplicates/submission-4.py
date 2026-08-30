class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        charmap = {}

        for r in range(len(s)):
            if s[r] in charmap:
                l = max(charmap[s[r]] + 1, l)
            charmap[s[r]] = r
            best = max(best, r - l + 1)
        return best