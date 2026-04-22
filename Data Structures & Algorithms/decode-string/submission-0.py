class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currStr = ""
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((currStr, num))
                currStr = ""
                num = 0
            elif ch == "]":
                prevStr, k = stack.pop()
                currStr = prevStr + k * currStr
            else:
                currStr += ch
        return currStr