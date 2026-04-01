class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = [] # [(temp, index)]

        for i in range(n):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                prev_t = stack.pop()
                # Update the result array
                res[prev_t[1]] = i - prev_t[1]
            # Push t to the stack
            stack.append((t, i))
        return res
                
