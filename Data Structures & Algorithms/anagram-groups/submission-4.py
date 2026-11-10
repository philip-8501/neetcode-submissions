class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s)) 
            dictionary[sorted_str].append(s)
        
        return list(dictionary.values())