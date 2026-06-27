class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        initial_subarray = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                max_num = max(max_num, i-initial_subarray+1)
            else:
                initial_subarray=i+1
        return max_num