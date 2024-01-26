class Solution:
    def isPalindrome(self, x):
        if str(x)[::-1] == str(x):
            return True
        return False
    
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))