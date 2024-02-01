class Solution:
    def isPalindrome(self, x):
        # Base Case
        if x < 0:
            return 'false'
        
        number = x
        reverse = 0 

        # Recursion Reverse
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10

        return 'true' if x == reverse else 'false'
        
    
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))

"""
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""