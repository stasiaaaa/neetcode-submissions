class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Choose starting key (girst string)
        # For next word, go each letter, if same on same position continue, if a letter if not same, remove that letter from the key string
        key = strs[0]

        for word in strs: # Loop each word
            for i, letter in enumerate(key): # For each letter in the key
                if i >= len(word) or word[i] != letter: # Check if letter/position is same as key, and that the key length is greater that word
                    key = key[:i] # Remove the last letter if not
        
        return key # Return the lcp