# Faster and Optimized Solution, instead of using Recursion
class Solution(object):
    def climbStairs(self, n):
        n1, n2 = 1, 1 # Shifted Fibonacci

        for _ in range(n):
            nth = n1 + n2
            # Update the values
            n1 = n2
            n2 = nth

        return n1
                
solution = Solution()
print(solution.climbStairs(4))