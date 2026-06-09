class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for str in strs:
            sorted_str = "".join(sorted(str))

            if anagrams.get(sorted_str) != None:
                anagrams[sorted_str].append(str)
            else:
                anagrams[sorted_str] = [str]
        
        print(list(anagrams.values()))
        return list(anagrams.values())
        