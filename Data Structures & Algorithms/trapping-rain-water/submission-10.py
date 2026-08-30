class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        l_height = height[left]
        r_height = height[right]
        water = 0
        while left < right:
            if l_height < r_height:
                left += 1
                l_height = max(l_height, height[left])
                water += l_height - height[left]
            else:
                right -= 1
                r_height = max(r_height, height[right])
                water += r_height - height[right]
        return water
                

            