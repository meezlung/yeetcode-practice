import math

class Solution(object):
    def climbStairs(self, n):
        return int((((1+math.sqrt(5))/2)**(n+1) - ((1-math.sqrt(5))/2)**(n+1))/math.sqrt(5))

solution = Solution()
print(solution.climbStairs(2))