class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, middle, right = 0, 0, len(nums)-1
        while left < right:
            L = nums[left]
            R = nums[right]
            if L < R:
                return L
            if right -left<=1:
                return min(L,R)
            middle = (left + right) // 2
            M = nums[middle]
            if M < R:
                right = middle
            else:
                left = middle
        
        return nums[middle]