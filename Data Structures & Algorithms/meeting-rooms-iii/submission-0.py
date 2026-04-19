class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # sort by start time
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        busy_rooms = []  # (end_time, room_id)
        count = [0] * n
        for start, end in meetings:
            # Step 1: free up rooms
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            # Step 2: assign room
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                # delay meeting
                end_time, room = heapq.heappop(busy_rooms)
                duration = end - start
                new_end = end_time + duration
                heapq.heappush(busy_rooms, (new_end, room))
            count[room] += 1
        # Step 3: find max usage room
        return count.index(max(count))