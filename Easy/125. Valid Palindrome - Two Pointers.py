class Solution(object):
    def isPalindrome(self, s):
        final_string = ""
        for char in s:
            if char.isalnum():
                final_string += char
        return True if final_string.lower()[::-1] == final_string.lower() else False


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))