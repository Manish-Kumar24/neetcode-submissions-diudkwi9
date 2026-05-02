class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        nums.sort(reverse=True)
        cases = [0] * k
        def backtrack(idx):
            if idx == len(nums):
                return all(case == target for case in cases)
            for i in range(k):
                if cases[i] + nums[idx] <= target:
                    cases[i] += nums[idx]
                    if backtrack(idx + 1):
                        return True
                    cases[i] -= nums[idx]
                if cases[i] == 0:
                    break
            return False
        return backtrack(0)