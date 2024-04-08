class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums = set(nums) 
        # converting lists into sets is much more faster than 
        # converting lists into hashmap one by one

        for num in nums:
            # check if the num smaller than the current num
            # is in keys, then stop because what we need is to
            # find the minimum

            if num - 1 in nums: continue 

            current = 1
            while num + 1 in nums:
                num += 1 # bruh we can manipulate the num here
                current += 1
            
            count = max(current, count)

        return count


# thats crazy ah - ethan mislang 2024
        
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, -1, 0]))
print(solution.longestConsecutive([100,4,200,1,3,2]))
print(solution.longestConsecutive([100,200,201,202,2,3]))
