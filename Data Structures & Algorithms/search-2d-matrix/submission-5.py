class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        l, r = 0, cols * rows - 1
        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // cols][mid % cols]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
        return False