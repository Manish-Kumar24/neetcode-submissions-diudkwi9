class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [0] * 1001
        for p, start, end in trips:
            changes[start] += p
            changes[end] -= p
        curr = 0
        for x in changes:
            curr += x
            if curr > capacity:
                return False
        return True