from math import floor

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binary_search(target, start, end):
            if start > end:
                return start
            
            middle = int(floor((start + end) / 2))

            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                return binary_search(target, start, middle-1)
            
            if nums[middle] < target:
                return binary_search(target, middle+1, end)
            
        return binary_search(target, 0, len(nums)-1)


solution = Solution()
print(solution.searchInsert([1,3,5,6], 5))
print(solution.searchInsert([1,3,5,6], 2))
print(solution.searchInsert([1,3,5,6], 7))