class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        water = 0
        low, high = 0, n-1
        while low < high:
            height = min(heights[low], heights[high])
            width = high - low
            area = height * width
            water = max(area, water)
            if heights[low] < heights[high]:
                low += 1
            else:
                high -= 1
        return water