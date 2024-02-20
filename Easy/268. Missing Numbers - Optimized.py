class Solution(object):
    def missingNumber(self, nums):
        nums_len = len(nums)
        binary = [-1] * (nums_len + 1)

        for num in nums:
            binary[num] = num

        for i in range(len(binary)):
            if binary[i] == -1:
                return i
        
        return 0

solution = Solution()
print(solution.missingNumber([3,0,1]))
print(solution.missingNumber([0,1]))
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))