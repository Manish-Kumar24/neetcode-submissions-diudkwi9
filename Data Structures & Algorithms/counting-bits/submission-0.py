class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            cnt = 0
            x = num
            while x:
                x &= (x-1)
                cnt += 1
            res.append(cnt)
        return res