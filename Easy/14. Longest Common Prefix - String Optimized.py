# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                print('j', j)
                print('i', i)
                print(strs[j])
                print('yes', strs[0][i])
                print('ye2', strs[j][i])

                print()

                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[j][:i]
                
        return strs[0]
                

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))

"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""