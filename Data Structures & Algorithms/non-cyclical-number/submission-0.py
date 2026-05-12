class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()
        while n != 1 and n not in vis:
            vis.add(n)
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            n = total
        return n == 1