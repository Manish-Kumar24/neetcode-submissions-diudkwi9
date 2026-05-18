class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            ch = chr(ord('A') + rem)
            res.append(ch)
            columnNumber //= 26
        return "".join(res[::-1])