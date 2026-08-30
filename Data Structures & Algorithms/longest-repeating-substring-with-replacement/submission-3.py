class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        chardict = dict()
        l = 0
        maxf = 0
        for r, char in enumerate(s):
            chardict[char] = 1 + chardict.get(char, 0)
            maxf = max(maxf, chardict[char])

            while r - l + 1 > maxf + k:
                chardict[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best