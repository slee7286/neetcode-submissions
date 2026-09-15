class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            a, b = nums2.copy(), nums1.copy()
        else:
            a, b = nums1.copy(), nums2.copy()
        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a) - 1

        while True:
            i = (l +  r) // 2 # a
            j = half - i - 2 # b

            aleft = a[i] if i >= 0 else float("-inf")
            aright = a[i + 1] if i + 1 < len(a) else float("inf")
            bleft = b[j] if j >= 0 else float("-inf")
            bright = b[j + 1] if j + 1 < len(b) else float("inf")

            if aleft <= bright and bleft <= aright:
                # odd
                if total % 2:
                    return min(aright, bright)
                # event
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1