from itertools import combinations

class Solution(object):
    def twoSum(self, nums, target):
        nums = {index: value for index, value in enumerate(nums)}

        for index_pair in combinations(nums, 2):
            if nums[index_pair[0]] + nums[index_pair[1]] == target:
                return (index_pair[0], index_pair[1])
        
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([3, 3], 6))

"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""