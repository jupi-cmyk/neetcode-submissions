class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in reversed(range(len(arr))):
            if i == len(arr) - 1:
                current = arr[i]
                arr[i] = -1
            elif i == len(arr) - 2:
                current, arr[i] = arr[i], current
            else:
                current, arr[i] = arr[i], max(current, arr[i+1])
        return arr