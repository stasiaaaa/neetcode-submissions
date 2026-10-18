class Solution:
    def isAnagram(self, s: string, t: string) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for c in s:
            counter[c] = counter.get(c,0) + 1
        
        for c in t:
            if counter.get(c,0) == 0:
                return False
            counter[c] -= 1

        return True

