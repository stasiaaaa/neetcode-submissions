class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time complexity O(n) : grows with input
        # Space complexity O(n): we store newStr, size of n
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]

        


        
        
      