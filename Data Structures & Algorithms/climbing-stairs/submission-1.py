class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1 # prev
        b = 1 # current

        for i in range(n - 1):
            current = b
            b = a + b # next step
            a = current
        
        return b
