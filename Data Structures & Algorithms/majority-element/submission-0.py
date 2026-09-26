from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        highest = nums[len(nums)//2]
        return highest