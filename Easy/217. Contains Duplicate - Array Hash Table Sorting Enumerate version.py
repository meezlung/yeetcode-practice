class Solution(object):  
    def containsDuplicate(self, nums):
        hash_map = {}

        for index, num in enumerate(nums):
            if num in hash_map:
                return True
            else:
                hash_map[num] = index

        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,1])) # => true
print(solution.containsDuplicate([1,2,3,4])) # => false
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # => true