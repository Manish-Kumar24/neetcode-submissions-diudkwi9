class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [False] * n
        reachable[0] = True
        count = 0
        for i in range(1, n):
            if i - minJump >= 0:
                count += reachable[i - minJump]
            if i - maxJump - 1 >= 0:
                count -= reachable[i - maxJump - 1]
            if s[i] == '0' and count > 0:
                reachable[i] = True
        return reachable[-1]