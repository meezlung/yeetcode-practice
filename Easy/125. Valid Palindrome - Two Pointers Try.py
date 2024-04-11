class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_string = ''.join(char.lower() for char in s if char.isalnum())

        start, end = 0, len(clean_string) - 1

        while start < end:
            
            if clean_string[start] != clean_string[end]:
                return False
            
            start += 1
            end -= 1
            
        return True
            
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))