class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if sum(nums) % 4 != 0:
            return False
        target = sum(nums) // 4
        nums.sort(reverse=True)  
        sides = [0] * 4
        def backtrack(idx):
            if idx == len(nums):
                return all(side == target for side in sides)
            for i in range(4):
                if sides[i] + nums[idx] <= target:
                    sides[i] += nums[idx]
                    if backtrack(idx + 1):
                        return True
                    sides[i] -= nums[idx]
            return False
        return backtrack(0)