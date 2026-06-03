class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        strSet = set()
        maxLen = 0

        for right in range(len(s)):
            # 文字セットの中にある文字と重複がある場合は除去して左ポインターをずらす
            while s[right] in strSet:
                strSet.remove(s[left])
                left += 1
            # 右ポインターの文字を文字セットに格納
            strSet.add(s[right])
            # 最大文字数を現在のポインターが囲っている範囲の文字数と比較して更新判定
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen