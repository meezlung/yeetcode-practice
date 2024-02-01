from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1 # counts every letter in s

        for char in t:
            # if current char in t is in char_count; or
            # if the current count of char in char_count is 0, which implies if it is non-existent in char_count
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1 # keeps on subtracting until it makes sense in the end

        return True

solution = Solution()
print(solution.isAnagram("anagram", "nagaram")) # =. true
print(solution.isAnagram("rat", "car")) # => false
print(solution.isAnagram("aacc", "ccac")) # => false