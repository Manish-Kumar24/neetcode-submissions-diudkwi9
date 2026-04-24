class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        ans = ""
        arr = self.store[key]
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        return ans