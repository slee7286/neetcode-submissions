class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for j in range(len(nums)):
            diff = target - nums[j]
            if diff in dict1:
                return [dict1[diff], j]
            dict1[nums[j]] = j