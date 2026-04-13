class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Brute Force(compare original and reverse str) -> O(n)/O(n)
        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]

        # Optimal Approach(two pointer) -> O(n)/O(1)
        low, high = 0, len(s)-1
        while low < high:
            if not s[low].isalnum():
                low += 1
                continue
            if not s[high].isalnum():
                high -= 1
                continue
            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -= 1
        return True