class Solution:
    def isAnagram(self, s: string, t: string) -> bool:
        # Time: O(n log n) for using sorted, if lookups are O(1)
        # Space: O(2n) = O(n), sorted builds two new lists
        if len(s) != len(t):
            return False
        a = sorted(s)
        b = sorted(t)
        
        return a == b

        
        
