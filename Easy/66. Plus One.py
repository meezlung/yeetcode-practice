class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        return [int(digit_real) for digit_real in str(int(''.join([str(digit) for digit in digits])) + 1)]
            
solution = Solution()
print(solution.plusOne([1, 2, 3]))
print(solution.plusOne([4, 3, 2, 1]))
print(solution.plusOne([9]))
print(solution.plusOne([0]))
print(solution.plusOne([-1]))