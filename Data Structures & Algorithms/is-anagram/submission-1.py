class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i], 0) + 1
            dict1[t[i]] = dict1.get(t[i], 0) - 1
        return all(v == 0 for v in dict1.values())