class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time complexity: O(n^2), we loop through the whole nums and then all values in occurences, which is at worst n if all numbers are different
        # Space complexity: O(n), we story dictionary occurences
        occurences = {}

        for num in nums:
            if num in occurences:
                occurences[num] += 1
            else:
                occurences[num] = 1

        for value in occurences.values():
            if value > 1:
                return True

        return False