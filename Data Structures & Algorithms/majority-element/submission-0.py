class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        candidate = 0
        for num in nums:
            if cnt == 0:
                candidate = num
            if num == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate