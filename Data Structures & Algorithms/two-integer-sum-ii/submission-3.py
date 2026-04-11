class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        low, high = 0, n-1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low+1, high+1]
            elif total < target:
                low += 1
            else:
                high -= 1