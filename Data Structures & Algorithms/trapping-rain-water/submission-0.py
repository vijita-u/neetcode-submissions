class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]*len(height)
        right_max = [0]*len(height)

        # Calculate left max for each height: l -> r
        l_max = height[0]
        for i in range(len(height)):
            left_max[i] = max(l_max, height[i])
            l_max = left_max[i]

        # Calculate right max for each height: r -> l
        r_max = height[len(height)-1]
        for j in range(len(height)-1, -1, -1):
            right_max[j] = max(r_max, height[j])
            r_max = right_max[j]

        # Calculate answer
        ans = 0
        for k in range(len(height)):
            ans += min(left_max[k], right_max[k]) - height[k]

        return ans

