class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        ans = 1
        curr = 1
        prev_cmp = 0
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                cmp = 1
            elif arr[i] < arr[i - 1]:
                cmp = -1
            else:
                cmp = 0
            if cmp == 0:
                curr = 1
            elif cmp * prev_cmp == -1:
                curr += 1
            else:
                curr = 2
            ans = max(ans, curr)
            prev_cmp = cmp
        return ans