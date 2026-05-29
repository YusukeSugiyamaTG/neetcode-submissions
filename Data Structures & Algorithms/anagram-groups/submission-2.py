class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for x in strs:
            key = "".join(sorted(x))
            if key in groups:
                groups[key].append(x)
            else:
                groups[key] = [x]
        return list(groups.values())