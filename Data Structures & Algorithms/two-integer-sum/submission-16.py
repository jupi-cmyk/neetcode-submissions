class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            if target - nums[i] not in hashmap:
                hashmap[target - nums[i]] = i
        
        keys = hashmap.keys()

        for j in range(len(nums)):

            idx = hashmap.get(nums[j])

            if nums[j] in keys and j!=idx:

                return [min(j,idx), max(j,idx)]