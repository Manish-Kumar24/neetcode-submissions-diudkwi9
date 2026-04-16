class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Better Approach -> O(n)/O(n)
        n = len(nums)
        k = k % n
        res = [0] * n
        for i in range(n):
            res[(i+k)%n] = nums[i]
        nums[:] = res