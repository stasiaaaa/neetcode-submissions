class Solution:
    def isAnagram(self, s: string, t: string) -> bool:
        seen = {}
        if len(s) != len(t):
            return False

        for c in s:
            seen[c] = seen.get(c, 0) + 1
        
        for c in t:
            seen[c] = seen.get(c, 0) - 1
            if seen[c] < 0:
                return False
        
        return True

        
        
