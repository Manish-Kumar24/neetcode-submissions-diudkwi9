class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        currMin = currMax = res = nums[0]
        for i in range(1, n):
            tempMax = max(
                nums[i], currMin * nums[i], currMax * nums[i]
            )
            currMin = min(
                nums[i], currMin * nums[i], currMax * nums[i]
            )
            currMax = tempMax
            res = max(res, currMax)
        return res