class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        n = len(heights)

        for i in range(n + 1):
            current = heights[i] if i < n else 0
            start = i

            while stack and stack[-1][1] > current:
                previous_start, height = stack.pop()
                best = max(best, height * (i - previous_start))
                start = previous_start

            if i < n:
                stack.append((start, current))

        return best