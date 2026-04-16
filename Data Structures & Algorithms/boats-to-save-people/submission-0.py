class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Two Pointers -> O(n)/O(1)
        n = len(people)
        boats = 0
        people.sort()
        l, r = 0, n -1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        return boats