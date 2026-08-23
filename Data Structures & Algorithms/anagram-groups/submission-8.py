class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = dict()
        result = []
        i = 0
        for str in strs:
            sort_list = sorted(str)
            sort_str = "".join(sort_list)
            if sort_str not in anagram:
                result.append([str])
                anagram[sort_str] = i
                i += 1
            else:
                result[anagram[sort_str]].append(str)
        return result
