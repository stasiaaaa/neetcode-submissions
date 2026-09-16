class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len) # cmp str length, return shortest word

        for i, letter in enumerate(shortest):
            for word in strs: # Check that every word has the same letter as the shortest
                if word[i] != letter:
                    return shortest[:i] # If not, return the part of the shortest word that was equal in all words.

        return shortest