class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        result = []

        def backtracking(openN, closedN):
            if openN == closedN == n: # base case
                result.append("".join(stack))
                return 
            
            # keep adding "(" and ")" until it reaches base case

            # keep adding openN as long as its less than n
            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtracking(openN, closedN + 1)
                stack.pop()
        
        backtracking(0, 0)
        return result


solution = Solution()
print(solution.generateParenthesis(3))
print(solution.generateParenthesis(1))