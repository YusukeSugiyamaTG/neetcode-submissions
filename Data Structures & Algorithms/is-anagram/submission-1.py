class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # early return
        if len(s) != len(t):
            return False

        s_str = {}
        t_str = {}

        # loop s
        for x in s:
            if x in s_str:
                s_str[x] += 1
            else:
                s_str[x] = 1

        # loop t
        for y in t:
            if y in t_str:
                t_str[y] += 1
            else:
                t_str[y] = 1
        
        return s_str == t_str
