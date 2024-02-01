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

"""
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""