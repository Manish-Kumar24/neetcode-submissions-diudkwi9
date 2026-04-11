class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using two loops -> O(n^2)
        # res = []
        # n = len(nums)
        # for i in range(len(nums)):
        #     first, second = 1, 1
        #     for j in range(0, i):
        #         first *= nums[j]
        #     for k in range(i+1, n):
        #         second *= nums[k]
        #     res.append(first*second)
        # return res

        # using prefix and suffix
        n = len(nums)
        pre, suff = [1]*n, [1]*n
        res = [0]*n
        # prefix
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        # suffix
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        for i in range(n):
            res[i] = pre[i] * suff[i]
        return res