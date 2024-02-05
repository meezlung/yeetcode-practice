class Solution(object):
    def isPalindrome(self, s):
        clean_string = ''.join(char.lower() for char in s if char.isalnum())
        return clean_string == clean_string[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))