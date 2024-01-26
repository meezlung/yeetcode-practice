class Solution():
    def addTwoNumbers(self, l1, l2):
        l1.reverse()
        l2.reverse()

        newl1 = ''.join(map(str, l1))
        newl2 = ''.join(map(str, l2))

        sum = int(newl1) + int(newl2)

        str_sum = [x for x in str(sum)]
        str_sum.reverse()

        return str_sum


solution = Solution()
print(solution.addTwoNumbers([2,4,3], [5,6,4])) # 342 + 465 = 807 => [7,0,8]
print(solution.addTwoNumbers([0], [0]))
print(solution.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))