class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversedStr = "".join(reversed(s))
        reversedStr = ("".join(ch for ch in reversedStr if ch.isalnum())).lower()
        n = len(reversedStr)
        print(reversedStr)
        right = n-1
        for i in range(n):
            if (reversedStr[i] != reversedStr[right]):
                return False
            right -= 1     
        return True