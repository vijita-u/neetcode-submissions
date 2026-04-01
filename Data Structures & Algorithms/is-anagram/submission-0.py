class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_sign = self.createSignature(s)
        t_sign = self.createSignature(t)

        if s_sign == t_sign:
            return True
        else:
            return False


    def createSignature(self,s: str) -> tuple:
        count = [0] * 26
        for c in s:
            idx = ord(c.lower()) - ord('a');
            count[idx] += 1
        return tuple(count)