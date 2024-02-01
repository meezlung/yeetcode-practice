from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)

solution = Solution()
print(solution.isAnagram("anagram", "nagaram")) # =. true
print(solution.isAnagram("rat", "car")) # => false
print(solution.isAnagram("aacc", "ccac")) # => false