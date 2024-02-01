class Solution(object):  
    def containsDuplicate(self, nums):
        hash_map = {}

        for index in range(len(nums)):
            if nums[index] in hash_map.keys(): # base step
                return True
            else: # recursive step
                hash_map[nums[index]] = index

        return False # if no duplicates were found

solution = Solution()
print(solution.containsDuplicate([1,2,3,1])) # => true
print(solution.containsDuplicate([1,2,3,4])) # => false
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # => true