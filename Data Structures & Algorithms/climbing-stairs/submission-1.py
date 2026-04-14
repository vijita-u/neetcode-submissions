class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        S = [0] * (n+1)
        # Base case
        for i in range(n+1):
            if i == 0:
                S[i] = 0
            elif i == 1:
                S[i] = 1
            elif i == 2:
                S[i] = 2
            else:
                S[i] = S[i-1] + S[i-2]
        return S[n]