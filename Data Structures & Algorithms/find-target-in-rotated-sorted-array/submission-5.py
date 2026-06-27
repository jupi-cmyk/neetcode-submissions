class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import bisect

        left, right = 0, len(nums)-1
        if nums[left] < nums[right]:
            i = bisect.bisect_left(nums, target)
            if i < len(nums) and nums[i] == target:
                return i
            else:
                return -1

        while left < right:
            middle = (left + right) // 2
            L = nums[left]
            R = nums[right]
            M = nums[middle]
            if M == target:
                return middle
            if M < R:
                if M > target:
                    right = middle
                else:
                    if target > R:
                        right = middle
                    else:
                        left = middle + 1
            else:
                if target > M:
                    left = middle +1
                else:
                    if target < L:
                        left = middle + 1
                    else:
                        right = middle
        
        if nums[left] == target:
            return left
        else:
            return -1
