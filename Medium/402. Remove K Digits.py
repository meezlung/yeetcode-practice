from itertools import combinations

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        index = []

        for i in range(len(num)):
            index.append(i)

        combinations_of_index = combinations(index, k)

        possible_combinations = []

        for combination in combinations_of_index:

            temporary = []

            for i in range(len(num)):
                if i not in combination:
                    temporary.append(num[i])

            if ''.join(temporary) != '':
                possible_combinations.append(''.join(temporary))

        return str(int(min(possible_combinations))) if possible_combinations else "0"

        # possible_numbers = []

        # for i in range(0, len(num) - k + 1):
        #     print(num[i:i+k])
        #     if num[:i] + num[i+k:]:
        #         print(num[:i] + num[i+k:])
        #         print(int(num[:i] + num[i+k:]))
        #         print()
        #         possible_numbers.append(int(num[:i] + num[i+k:]))
        # print()
        # return str(min(possible_numbers)) if possible_numbers else "0"



solution = Solution()
print(solution.removeKdigits("1432219", 3))
print(solution.removeKdigits("10200", 1))
print(solution.removeKdigits("10",2))
print(solution.removeKdigits("10001", 4))
print(solution.removeKdigits("10001", 3))