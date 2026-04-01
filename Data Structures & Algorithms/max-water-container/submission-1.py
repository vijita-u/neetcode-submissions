class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights)-1
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            area = h * w
            res = max(res, area)
            if heights[l] < heights[r]:
                # Update left until value > current left height
                l += 1
                while l < r and heights[l] < heights[l-1]:
                    l += 1
            else:
                # Update right until value > current right height
                r -= 1
                while r > l and heights[r] < heights[r+1]:
                    r -= 1
        return res