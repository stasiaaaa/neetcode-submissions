class Solution:
    def isAnagram(self, s: string, t: string) -> bool:
        count = {}

        if len(s) != len(t):
            return False

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            if count.get(c, 0) == 0:
                return False
            count[c] -= 1
                
        return True
        
        
