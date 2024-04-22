class Solution(object):
    def maxDepth(self, s):
        max_depth = 0
        score = 0

        for i in s:
            if i == "(":
                score += 1
            elif i == ")":
                max_depth: int = max(score, max_depth)
                score -= 1

        return max_depth
            
solution = Solution()
print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))
print(solution.maxDepth("(1)+((2))+(((3)))"))
print(solution.maxDepth("()"))
print(solution.maxDepth("(())"))
print(solution.maxDepth("(1())"))