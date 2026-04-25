class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = -1
        def canSplit(limit):
            cnt = 1
            currSum = 0
            for i in range(n):
                if currSum + nums[i] <= limit:
                    currSum += nums[i]
                else:
                    cnt += 1
                    currSum = nums[i]
                    if cnt > k:
                        return False
            return True
        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if canSplit(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res