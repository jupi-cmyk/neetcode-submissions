class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2, n3 = 0, 1, 0
        if n == 1:
            return 1
        for i in range( n):
            n3 = n1 + n2
            n1, n2 = n2, n3
        return n3