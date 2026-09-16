class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Add entry for each element.
        # If element already in set, break and return true.
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False