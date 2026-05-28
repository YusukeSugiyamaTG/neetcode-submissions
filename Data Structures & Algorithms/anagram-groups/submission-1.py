class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        # strs から順番に文字列取り出し
        for s in strs:
            # 取り出した文字列をソートしてキーとする
            key = "".join(sorted(s))
            if key in groups:
                # key が存在すればリストに s を追加(同じアナグラム)
                groups[key].append(s)
            else:
                # key が groups に存在しなければ空リストに文字列追加(異なるアナグラム)
                groups[key] = [s]
        
        # リストに dict の値を設定して返す
        return list(groups.values())
        