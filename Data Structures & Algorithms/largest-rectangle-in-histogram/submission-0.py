class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  
        maxArea = 0
        n = len(heights)
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea, h * width)
            stack.append(i)
        while stack:
            h = heights[stack.pop()]
            if not stack:
                width = n
            else:
                width = n - stack[-1] - 1
            maxArea = max(maxArea, h * width)
        return maxArea