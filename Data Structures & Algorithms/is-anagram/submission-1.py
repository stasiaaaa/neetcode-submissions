class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Space: O(1), CONSTRAINT 26 english letters, constant, dict store distinct characters k
        # Time: n + m = O(n + m), loop through chars of strings with different sizes
        count_s = {}
        count_t = {}

        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
        
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1
        
        if count_s == count_t:
            return True
        return False