class Solution(object):
    def missingNumber(self, nums):
        nums_len = len(nums)
        complete_numbers = []
        answer = 0

        for i in range(nums_len + 1):
            complete_numbers.append(i)

        for num in complete_numbers:
            if num not in nums:
                answer = num

        return answer


solution = Solution()
print(solution.missingNumber([3,0,1]))
print(solution.missingNumber([0,1]))
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))