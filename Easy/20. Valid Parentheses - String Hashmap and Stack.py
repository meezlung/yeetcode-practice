class Solution(object):
    def isValid(self, s):
        stack = []
        hash = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in hash.keys(): # identify if open parenthesis
                stack.append(char)
            elif char in hash.values(): # identify if close parenthesis
                # if stack is null or if the counter parenthesis of the last opening parenthesis in the stack is not equal to the current char
                if not stack or hash[stack.pop()] != char:
                    return False
            else: # identify if non-parenthesis for input checking
                return False
          
        return not stack # if not empty, False. else, True.

solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("{[]}"))