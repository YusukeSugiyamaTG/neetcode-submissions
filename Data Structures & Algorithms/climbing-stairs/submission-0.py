class Solution:
    def climbStairs(self, n: int) -> int:
        # 基底は n=1, n=2 のケース
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        a = 1
        b = 2

        for i in range(3, n + 1):
            current = a + b
            a = b
            b = current
        
        return b