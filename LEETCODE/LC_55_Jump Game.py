class Solution:
    def canJump(self, nums: List[int]) -> bool:
        arr = [0]*len(nums)
        for i, num in enumerate(nums):
            arr[i] = i + num
        max_num = 0
        for idx, now in enumerate(arr):
            if idx > max_num:
                break
            else:
                if now >= max_num:
                    max_num = now
        if max_num >= len(nums)-1:
            return True
        else:
            return False