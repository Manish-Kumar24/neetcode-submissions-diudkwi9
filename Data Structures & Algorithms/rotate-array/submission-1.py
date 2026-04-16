class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Better Approach -> O(n)/O(n)
        # n = len(nums)
        # k = k % n
        # res = [0] * n
        # for i in range(n):
        #     res[(i+k)%n] = nums[i]
        # nums[:] = res

        # In-place -> O(n)/O(1)
        n = len(nums)
        k = k % n
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)