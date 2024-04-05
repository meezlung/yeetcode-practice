class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []

        for i in range(len(nums)):
            left = nums[:i]

            if i < len(nums) - 1:
                right = nums[i + 1:]
            else:
                right = []

            mini_answer = 1
            for j in left + right:
                mini_answer *= j
            
            answer.append(mini_answer)

        return answer

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1,1,0,-3,3]))