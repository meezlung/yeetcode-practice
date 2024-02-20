class Solution(object):  
    def getInfo(self, string):
        # TODO: Return char count as key, and return string as item
        char_count = {}

        for char in string:
            char_count[char] = char_count.get(char, 0) + 1

        return sorted(char_count.items()), string

    def groupAnagrams(self, strs):
        all_possible_keys = []

        # Make all keys that are possible
        for string in strs:
            key, item = self.getInfo(string)
            if key not in all_possible_keys:
                all_possible_keys.append(key)

        final_list = [[] for _ in range(len(all_possible_keys))]

        # Iterate all string in strs and check if there's a matching key
        for string in strs:
            key, item = self.getInfo(string)
            for i in range(len(all_possible_keys)):
                if all_possible_keys[i] == key:
                    final_list[i].append(item)
                
        return final_list



        
            

solution = Solution()

print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # => [["bat"],["nat","tan"],["ate","eat","tea"]]     
print(solution.groupAnagrams([""])) # => [[""]]
print(solution.groupAnagrams(["a"])) # => [["a"]]
