class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            while st and a < 0 and st[-1] > 0:
                if abs(a) > st[-1]:
                    st.pop()
                    continue
                elif abs(a) == st[-1]:
                    st.pop()
                break
            else:
                st.append(a)
        return st