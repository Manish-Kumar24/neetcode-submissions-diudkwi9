class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Using Hashmap -> O(n)/O(n)
        # n = len(nums)
        # res = []
        # mp = {}
        # for i in range(n):
        #     mp[nums[i]] = mp.get(nums[i], 0) + 1
        # for ele, freq in mp.items():
        #     if freq > n//3:
        #         res.append(ele)
        # return res

        # Using Boyer-Moore-Voting -> O(n)O(1)
        cnt1, cnt2 = 0, 0
        cand1, cand2 = None, None
        for num in nums:
            if num == cand1: cnt1 += 1
            elif num == cand2: cnt2 += 1
            elif cnt1 == 0: 
                cand1 = num
                cnt1 = 1
            elif cnt2 == 0:
                cand2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        res = []
        for c in [cand1, cand2]:
            if nums.count(c) > len(nums) // 3:
                res.append(c)
        return res