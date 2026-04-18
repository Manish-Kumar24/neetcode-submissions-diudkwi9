class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        cnt = 0
        start1, end1 = intervals[0]
        for i in range(1, len(intervals)):
            start2, end2 = intervals[i]
            if start2 < end1:
                cnt += 1
            else:
                start1, end1 = start2, end2
        return cnt