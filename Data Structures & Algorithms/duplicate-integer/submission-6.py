class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time: O(n), n number of items in nums
        # Space: O(n), worst case, as long as the number of items in n
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False