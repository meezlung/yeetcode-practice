class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s

        palindrome = ""
        current_max_len = 0

        for center in range(len(s)):

            # odd case
            l, r = center, center
            while l >= 0 and r < len(s) and s[l] == s[r]: # check if in range and check if palindrome (base case)
                # TODO: append to palindrome if its length is greater than the current
                if (r - l + 1) > current_max_len:
                    palindrome = s[l:r+1]
                    current_max_len = r - l + 1

                # TODO: keeping subtracting from l and adding from r until it reaches end
                l -= 1
                r += 1

            # even case
            l, r = center, center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: # check if in range and check if palindrome (base case)
                # TODO: append to palindrome if its length is greater than the current
                if (r - l + 1) > current_max_len:
                    palindrome = s[l:r+1]
                    current_max_len = r - l + 1

                # TODO: keeping subtracting from l and adding from r until it reaches end
                l -= 1
                r += 1  

        return palindrome       
        

solution = Solution()

print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))
print(solution.longestPalindrome("ac"))
print(solution.longestPalindrome("bb"))
print(solution.longestPalindrome("mqizdjrfqtmcsruvvlhdgzfrmxgmmbguroxcbhalzggxhzwfznfkrdwsvzhieqvsrbyedqxwmnvovvnesphgddoikfwuujrhxwcrbttfbmlayrlmpromlzwzrkjkzdvdkpqtbzszrngczvgspzpfnvwuifzjdrmwfadophxscxtbavrhfkadhxrmvlmofbzqshqxazzwjextdpuszwgrxirmmlqitjjpijptmqfbggkwaolpbdglmsvlwdummsrdyjhmgrasrblpjsrpkkgknsucsshjuxunqiouzrdwwooxclutkrujpfebjpoodvhknayilcxjrvnykfjhvsikjabsdnvgguoiyldshbsmsrrlwmkfmyjbbsylhrusubcglaemnurpuvlyyknbqelmkkyamrcmjbncpafchacckhymtasylyfjuribqxsekbjkgzrvzjmjkquxfwopsbjudggnfbuyyfizefgxamocxjgkwxidkgursrcsjwwyeiymoafgyjlhtcdkgrikzzlenqgtdukivvdsalepyvehaklejxxmmoycrtsvzugudwirgywvsxqapxyjedbdhvkkvrxxsgifcldkspgdnjnnzfalaslwqfylmzvbxuscatomnmgarkvuccblpoktlpnazyeazhfucmfpalbujhzbykdgcirnqivdwxnnuznrwdjslwdwgpvjehqcbtjljnxsebtqujhmteknbinrloregnphwhnfidfsqdtaexencwzszlpmxjicoduejjomqzsmrgdgvlrfcrbyfutidkryspmoyzlgfltclmhaeebfbunrwqytzhuxghxkfwtjrfyxavcjwnvbaydjnarrhiyjavlmfsstewtxrcifcllnugldnfyswnsewqwnvbgtatccfeqyjgqbnufwttaokibyrldhoniwqsflvlwnjmffoirzmoxqxunkuepj"))

