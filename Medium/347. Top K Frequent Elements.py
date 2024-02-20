class Solution(object):
    def charCount(self, nums):
        all_possible_numbers = []
        char_count_dict = {}

        for num in nums:
            if num not in all_possible_numbers:
                all_possible_numbers.append(num)

        for possible_number in all_possible_numbers:
            char_count_dict[possible_number] = nums.count(possible_number)

        return char_count_dict


    def topKFrequent(self, nums, k):
        char_count = self.charCount(nums)
        sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
        final_list = []

        for i in range(k):
            final_list.append(sorted_char_count[i][0])

        return final_list

solution = Solution()

print(solution.topKFrequent([1,1,1,2,2,3,3,3,3], 2)) # => [1, 2]
print(solution.topKFrequent([1], 1)) # => [1]