# """
# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:
# """

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        # Step 1: Find Peak
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        peak = low
        # Step 2: Binary Search Left (Ascending)
        def binarySearch(low, high, target, ascending=True):
            while low <= high:
                mid = (low + high) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                if ascending:
                    if val < target:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    if val < target:
                        high = mid - 1
                    else:
                        low = mid + 1
            return -1
        # Search left side
        res = binarySearch(0, peak, target, True)
        if res != -1:
            return res
        # Step 3: Search Right (Descending)
        return binarySearch(peak + 1, n - 1, target, False)