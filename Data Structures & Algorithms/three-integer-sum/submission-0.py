class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time O(n log n) for the sort + O(n^2) for the loops -> O(n^2)
        # Space O(1), sort is O(n) worst case
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # Skip if number the same as previous
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


        
        