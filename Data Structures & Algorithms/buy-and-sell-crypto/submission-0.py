class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 最安値(最初の価格で初期化)
        min_price = prices[0]
        # 利益
        profit = 0

        for current_price in prices:
            # 今日の金額が最安値より安ければ更新
            if current_price < min_price:
                min_price = current_price
            # 今日の販売学が今までの利益より大きいならば更新
            elif current_price - min_price > profit:
                profit = current_price - min_price

        return profit