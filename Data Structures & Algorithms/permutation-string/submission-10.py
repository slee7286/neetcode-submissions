from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = Counter(s1)
        s2_dict = {}
        l = 0

        for r in range(len(s2)):
            s2_dict[s2[r]] = 1 + s2_dict.get(s2[r], 0)

            # Keep the window exactly <= len(s1)
            if r - l + 1 > len(s1):
                s2_dict[s2[l]] -= 1

                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]

                l += 1

            if s1_dict == s2_dict:
                return True

        return False