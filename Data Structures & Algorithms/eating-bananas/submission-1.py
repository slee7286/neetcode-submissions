class Solution:
    def eating(self, piles: List[int], s: int) -> int:
        return sum([-(b // -s) for b in piles])

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            hours = self.eating(piles, mid)
            if hours > h:
                l = mid + 1
            elif hours <= h:
                r = mid - 1
        return l