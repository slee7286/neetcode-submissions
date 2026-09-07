class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = {n:0 for n in range(1,len(nums))}
        for num in nums:
            if hash_map[num] == 1:
                return num
            else:
                hash_map[num] = 1