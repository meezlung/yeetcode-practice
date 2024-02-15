class Solution(object):
    def canJump(self, nums):
        can = False

        if len(nums) == 1:
            return True

        for i in range(len(nums)):
            print()
            if nums[i] != nums[-1] and i + nums[i] >= len(nums) - 1:
                can = True

        return can
        
solution = Solution()
print(solution.canJump([2,3,1,1,4]))
print(solution.canJump([3,2,1,0,4]))
print(solution.canJump([1]))
print(solution.canJump([2, 1]))
print(solution.canJump([0, 2, 3]))