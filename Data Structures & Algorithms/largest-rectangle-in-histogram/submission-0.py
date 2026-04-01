class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            if not stack:
                stack.append([i, h])
            else:
                if h < stack[-1][-1]:
                    while stack and h <= stack[-1][-1]:
                        top = stack.pop()
                        height = top[-1]
                        width = i - top[0]
                        max_area = max(max_area, (height*width))
                    # Append this new bar
                    stack.append([top[0], h])
                else:
                    stack.append([i, h])

        # Iterate through remaining items in the stack till the very end
        for i, h in stack:
            height = h
            width = len(heights)-i
            max_area = max(max_area, (height*width))

        return max_area
        
        
