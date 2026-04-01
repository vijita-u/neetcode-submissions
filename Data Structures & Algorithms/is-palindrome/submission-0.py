class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            while l < r and not self.isAlpha(s[l]):
                l += 1
            while r > l and not self.isAlpha(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

    def isAlpha(self, c: str) -> bool:
        if (ord('a') <= ord(c.lower()) <= ord('z') or ord('0') <= ord(c.lower()) <= ord('9')):
            return True
        return False
        