class Solution(object):
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        stack_nums = {}
        i = 0
        k = 0

        while i < len(nums):
            curr_num = nums[i]

            if curr_num not in stack_nums.values():
                stack_nums[i] = curr_num
                k += 1
                i += 1

            else:
                nums.remove(curr_num)

        return k

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # nums = sorted(set(nums)) # this doesnt work because im creating another nums 
                                   # which is passed on by the original unchanged nums
        nums[:] = sorted(set(nums)) # the [:] knows that it's an existing list which you need to put new stuff into it
        return len(nums)
    
solution = Solution()
print(solution.removeDuplicates([1,1,2]), 2)
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]), 5)
print(solution.removeDuplicates([1]))
print(solution.removeDuplicates([]))