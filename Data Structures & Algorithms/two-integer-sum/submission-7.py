class Solution:
    def twoSum(self, nums: List[int], target: int) -> [int, int]:
        # brute force would be to compare each element with all the elements after it.
        # Time O(n^2)

        # Better solution
        prev_elem = {} # Space O(n), n is length of nums

        for i,num in enumerate(nums): # Time O(n), n length of nums
            diff = target - num
            if diff in prev_elem:
                return [prev_elem[diff], i]
            prev_elem[num] = i
        
