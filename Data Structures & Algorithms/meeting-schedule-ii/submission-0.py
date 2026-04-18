"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if not intervals:
            return 0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        room, res = 0, 0
        i, j = 0, 0
        while i < n and j < n:
            if starts[i] < ends[j]:
                room += 1
                res = max(res, room)
                i += 1
            else:
                room -= 1
                j += 1
        return res