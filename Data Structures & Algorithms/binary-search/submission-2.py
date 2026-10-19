class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time: O(log n), the search space is halved each iteration
        # Space: O(1), we only keep three variables l, r and m
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m  
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1