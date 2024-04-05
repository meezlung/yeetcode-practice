class Solution(object):
    def maxDepth(self, s):
        max_number = 0 

        for i in range(len(s)):
            if s[i] not in {"(", ")"}:
                left = s[:i].count("(")
                right = s[:i].count(")")

                depth = left - right

                if depth > max_number:
                    max_number = depth

            elif i < len(s) - 1 and s[i] == "(" and s[i + 1] == ")":
                left = s[:i+1].count("(")
                max_number = left

        return max_number
            
solution = Solution()
print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))
print(solution.maxDepth("(1)+((2))+(((3)))"))
print(solution.maxDepth("()"))
print(solution.maxDepth("(())"))
print(solution.maxDepth("(1())"))