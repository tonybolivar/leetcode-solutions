class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        seen = {}
        
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        for char in t:
            seen[char] = seen.get(char, 1) - 1
        
        for v in seen.values():
            if v != 0:
                return False
        return True