class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0
        start1, end1 = newInterval
        # Step 1: add non-overlapping (before)
        while i < n and intervals[i][1] < start1:
            res.append(intervals[i])
            i += 1
        # Step 2: merge overlapping
        while i < n and intervals[i][0] <= end1:
            start2, end2 = intervals[i]
            start1 = min(start1, start2)
            end1 = max(end1, end2)
            i += 1
        res.append([start1, end1])
        # Step 3: add remaining
        while i < n:
            res.append(intervals[i])
            i += 1
        return res