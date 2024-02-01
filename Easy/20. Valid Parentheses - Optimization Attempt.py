class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    closeToOpen = {')': '(', ']': '[', '}': '{'}

    for c in s:
      if c in closeToOpen.keys():
        if not stack or stack.pop() != closeToOpen[c]:
          return False
      else:
        stack.append(c)
  
    return True if not stack else False
  
solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("{[]}"))

"""
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
"""