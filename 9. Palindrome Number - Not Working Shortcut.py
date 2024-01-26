class Solution:
    def isPalindrome(self, x):
        if str(x)[::-1] == str(x):
            return 'true'
        return 'false'
    
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))

