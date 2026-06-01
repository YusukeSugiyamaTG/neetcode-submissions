class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # 左のポインターが右のポインターを追い越す場合、ループ終了
        while left <= right:
            # 二分探索するために mid を算出(int を維持)
            mid = (left + right) // 2
            # target と配列[mid]が一致する場合、回答返却
            if target == nums[mid]:
                return mid
            # nums[mid] が target よりも大きい場合、右のポインターを mid で上書きする
            elif nums[mid] > target:
                right = mid - 1
            # nums[mid] が target よりも小さい場合、左のポインターを mid で上書きする
            elif nums[mid] < target:
                left = mid + 1

        return -1