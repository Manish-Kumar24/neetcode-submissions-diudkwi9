class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for op in tokens:
            if op in "+-*/":
                b, a = st.pop(), st.pop()
                if op == "+":
                    st.append(a + b)
                elif op == "-":
                    st.append(a - b)
                elif op == "*":
                    st.append(a * b)
                else:
                    st.append(int(a/b))
            else:
                st.append(int(op))
        return st[-1]