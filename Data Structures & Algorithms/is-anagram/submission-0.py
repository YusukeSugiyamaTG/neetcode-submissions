class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # 文字数違う場合はアーリーリターン
        if len(s) != len(t):
            return False
        
        # dict
        s_dict = {}
        t_dict = {}

        # s 取り出し
        for x in s:
            if x in s_dict:
                s_dict[x] += 1
            else:
                s_dict[x] = 1
        
        # t 取り出し
        for y in t:
            if y in t_dict:
                t_dict[y] += 1
            else:
                t_dict[y] = 1
        
        # dict match
        return s_dict == t_dict