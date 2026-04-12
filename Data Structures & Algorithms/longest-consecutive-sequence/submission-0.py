class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force -> O(n^2)
        # longest = 0
        # for num in nums:
        #     current = num
        #     count = 1
        #     while current + 1 in nums:
        #         current += 1
        #         count += 1
        #     longest = max(longest, count)
        # return longest

        # Better Approach -> O(nlogn)
        if not nums:
            return 0
        nums.sort()
        longest, cnt = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            else:
                cnt = 1
            longest = max(longest, cnt)
        return longest