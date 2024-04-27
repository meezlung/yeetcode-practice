class Solution(object):
    def containsNearbyDuplicate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        for i in range(1, len(nums)):
            for j in range(i):
                if i != j and nums[i] == nums[j] and abs(i - j) <= k:
                    return True
            
        return False
    
    def containsNearbyDuplicate(self, nums, k):
        seen = set()

        for i, num in enumerate(nums):
            print(i, num)
            if i > k:
                print(nums[i - k - 1])
                seen.remove(nums[i - k - 1]) # makes it faster removes the index that has been kth times, and - 1 for indexing
            if num in seen:
                return True
            seen.add(num)

        return False

solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))
print(solution.containsNearbyDuplicate([1,0,1,1], 1))
print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))