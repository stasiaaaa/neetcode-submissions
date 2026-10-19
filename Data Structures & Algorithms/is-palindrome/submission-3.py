class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Space complexity: O(n)
        # Time complexity: O(n)
        s = "".join(l for l in s if l.isalnum())
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


        


        
        
      