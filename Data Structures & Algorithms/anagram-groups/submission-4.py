class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in out:
                out[key].append(s)
            else:
                out[key] = [s]
        return list(out.values())
