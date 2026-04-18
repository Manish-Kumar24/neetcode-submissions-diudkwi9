class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        intervals.sort(key=lambda x:x[0])
        start1, end1 = intervals[0]
        for i in range(1, len(intervals)):
            start2, end2 = intervals[i]
            if start2 <= end1: 
                end1 = max(end1, end2)
            else:
                res.append([start1, end1])
                start1, end1 = start2, end2
        res.append([start1, end1])
        return res