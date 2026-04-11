class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(len(nums)):
            first, second = 1, 1
            for j in range(0, i):
                first *= nums[j]
            for k in range(i+1, n):
                second *= nums[k]
            res.append(first*second)
        return res