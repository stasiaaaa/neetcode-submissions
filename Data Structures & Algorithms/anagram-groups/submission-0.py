from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0]*26
            #print("Counts: ", counts)
        
            for char in word:
                index = ord(char) - ord("a")
                counts[index] += 1
            signature = tuple(counts)
            #print("Sign:", signature)
            groups[signature].append(word)
            #print("Groups:", groups)
        return list(groups.values())


        