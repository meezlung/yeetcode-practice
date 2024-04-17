from math import sqrt

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(sqrt(x))

    
solution = Solution()
print(solution.mySqrt(4))
print(solution.mySqrt(8))
print(solution.mySqrt(16))