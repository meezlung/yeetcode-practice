class Solution(object):  
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

solution = Solution()
print(solution.containsDuplicate([1,2,3,1])) # => true
print(solution.containsDuplicate([1,2,3,4])) # => false
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # => true