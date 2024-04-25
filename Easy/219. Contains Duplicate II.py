class Solution(object):
    def containsNearbyDuplicate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i != j and nums[i] == nums[j] and abs(i - j) <= k:
                    return True
            
        return False
    
    def containsNearbyDuplicate(self, nums, k):
    
solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))
print(solution.containsNearbyDuplicate([1,0,1,1], 1))
print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))