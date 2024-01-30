# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""

        for i in range(len(strs[0])):
            for str in strs:
                # if out of bounds or if the current character is not equal to the current character in the first string
                if i == len(str) or str[i] != strs[0][i]: 
                    print(res)
                    # return res
            res += strs[0][i]
        print(res)

        # return res
                

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))