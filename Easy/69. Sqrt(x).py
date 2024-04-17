from math import sqrt

class Solution(object):
    def mySqrtWithBuiltIn(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(sqrt(x))
    
    def mySqrt(self, x): # binary search
        """
        :type x: int
        :rtype: int
        """
        
        def binary_search(left, right):
            mid = (left + right) // 2

            if left > right:
                return right

            if mid * mid == x:
                return mid
            
            if mid * mid > x:
                return binary_search(left, mid-1)

            if mid * mid < x:
                return binary_search(mid+1, right)

        return binary_search(0, x)

    
solution = Solution()
print(solution.mySqrt(4))
print(solution.mySqrt(8))
print(solution.mySqrt(16))