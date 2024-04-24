class Solution(object):
    def tribonacci_recursion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 2:
            return n
        
        dp = [0, 1, 1]

        for _ in range(3, n+1):
            dp[0], dp[1], dp[2] = dp[1], dp[2], sum(dp)

        return dp[2]
        
solution = Solution()
print(solution.tribonacci(4))
print(solution.tribonacci(25))
print(solution.tribonacci(30))