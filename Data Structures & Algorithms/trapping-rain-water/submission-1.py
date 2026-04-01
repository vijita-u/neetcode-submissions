class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = height[0]
        r_max = height[len(height)-1]

        # Initialize pointers
        l = 0
        r = len(height)-1

        ans = 0
        while l < r:
            # Calculate the boundaries
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            # If left boundary < right boundary -> left becomes deciding factor
            if l_max < r_max:
                ans += l_max - height[l]
                l += 1
            else:
                ans += r_max - height[r]
                r -= 1
        return ans

