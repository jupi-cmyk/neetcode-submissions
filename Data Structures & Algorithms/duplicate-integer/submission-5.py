class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        # for i in range(len(nums)):
        #     if nums[i] not in unique_nums:
        #         unique_nums.append(nums[i])
        #         i+=1
        #     else:
        #         return True
        # return False
        for num in nums:
            if num not in unique_nums:
                unique_nums.add(num)
            else:
                return True
        return False