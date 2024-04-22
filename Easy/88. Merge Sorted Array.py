class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # approach start backwards
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            curr_num1 = nums1[i]
            curr_num2 = nums2[j]
            # print(curr_num1)
            # print(curr_num2)
            # print()
            if i >= 0 and curr_num1 > curr_num2:
                nums1[k] = curr_num1
                # print('yes')
                # print(nums1)
                # print('k', k, 'i', i)
                # print()
                k -= 1
                i -= 1
            else:
                nums1[k] = curr_num2
                # print('no')
                # print(nums1)
                # print('k', k, 'j', j)
                # print()
                k -= 1
                j -= 1

        return nums1

solution = Solution()
print(solution.merge([1,2,3,0,0,0,0], 3, [2,4,5,6], 4))