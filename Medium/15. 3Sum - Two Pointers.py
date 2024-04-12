class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        passed_numbers = []
        answer = []

        for i in range(len(nums)):
            num = nums[i]
            if i > 0 and num == nums[i - 1]: # if current num is the same as its previous index, this is so avoid duplicates
                continue

            start, end = i + 1, len(nums) - 1 

            while start < end:
                three_sum = num + nums[start] + nums[end] 
                
                if three_sum > (0):
                    end -= 1
                
                elif three_sum < (0):
                    start += 1

                else:
                    answer.append([num, nums[start], nums[end]])
                    # i thought it was to break here

                    start += 1
                    while nums[start] == nums[start - 1] and start < end: # we check here until there are no duplicates in shifting the start
                        start += 1
        return answer

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
print(solution.threeSum([0,1,1]))
print(solution.threeSum([0,0,0]))