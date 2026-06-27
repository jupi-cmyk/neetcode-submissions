class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            if target - nums[i] not in hashmap:
                hashmap[target - nums[i]] = i
        
        for j in range(len(nums)):

            idx = hashmap.get(nums[j])

            if nums[j] in hashmap and j!=idx:

                return [min(j,idx), max(j,idx)]