class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        stack = []
        pairs = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in pairs: # exit
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else: # opener
                stack.append(c)
        
        return not stack
        

            