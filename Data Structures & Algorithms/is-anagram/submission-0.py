class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(len(s)+len(t))
        # Another solution: Use one dictionary, subtract for letters in seconds string. (Still same worst case)
        s_letters = {}
        for letter in s:
            if letter in s_letters:
                s_letters[letter] += 1
            else:
                s_letters[letter] = 1

        t_letters = {}
        for letter in t:
            if letter in t_letters:
                t_letters[letter] += 1
            else:
                t_letters[letter] = 1

        if s_letters == t_letters:
            return True
        return False

        