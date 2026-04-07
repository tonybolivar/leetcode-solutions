class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(len(strs)):
            sortedstr = "".join(sorted(strs[i]))
            if (sortedstr not in anagrams):
                anagrams[sortedstr] = []
            anagrams[sortedstr].append(strs[i])
            
        return list(anagrams.values())