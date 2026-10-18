class Solution:
    def twoSum(self, nums: List[int], target: int) -> [int, int]:
        prev_elem = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_elem:
                return [prev_elem[diff], i]
            prev_elem[num] = i
