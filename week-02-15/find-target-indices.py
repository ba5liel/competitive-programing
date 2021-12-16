class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        self.isort(nums)
        res = []
        for idx, val in enumerate(nums):
            if val == target:
                res.append(idx)
        return res
    
    def isort(self, arr: List[int]):
        #insertion
        for i in range(1, len(arr)):
            current = arr[i]
            for j in range(i - 1, -1, -1):
                if arr[j] > current:
                    arr[j+1] = arr[j]
                    arr[j] = current
                else:
                    arr[j+1] = current
                    break
                