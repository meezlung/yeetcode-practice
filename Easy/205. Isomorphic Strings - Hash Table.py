class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return [s.index(char) for char in s] == [t.index(char) for char in t] # takes note of index of each character
        
    
solution = Solution()
print(solution.isIsomorphic('egg', 'add'))
print(solution.isIsomorphic('foo', 'bar'))
print(solution.isIsomorphic('paper', 'title'))
print(solution.isIsomorphic("bbbaaaba", "aaabbbba"))