from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        need = Counter(t)
        window = defaultdict(int)

        need_count = len(need)
        have = 0

        left = 0
        best_len = float("inf")
        best_start = 0

        for right, char in enumerate(s):
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1
            
            while have == need_count:
                length = right - left + 1

                if length < best_len:
                    best_len = length
                    best_start = left
                
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                
                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_start:best_start + best_len]