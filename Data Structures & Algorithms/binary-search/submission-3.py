class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time: O(log n), the search space is halved
        # Space: O(1)
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1