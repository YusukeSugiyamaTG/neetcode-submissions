class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # [{a, 2}, {c, 2}, {e, 1}, {r, 2}]
        sdict = {}
        tdict = {}

        for x in s:
            if x in sdict:
                sdict[x] += 1
            else:
                sdict[x] = 1
        
        for y in t:
            if y in tdict:
                tdict[y] += 1
            else:
                tdict[y] = 1

        return sdict == tdict