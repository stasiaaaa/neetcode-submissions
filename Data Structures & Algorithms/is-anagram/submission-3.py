class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Anagrams same length, same amount of letters
        counter = {}

        if len(s) != len(t):
            return False
        
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        for c in t:
            if c in counter:
                counter[c] -= 1
                if counter[c] < 0:
                    return False
            else:
                return False
        
        return True
        


        