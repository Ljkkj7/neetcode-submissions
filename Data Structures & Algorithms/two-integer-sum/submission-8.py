class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 0
        arr = []

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        index1 = i
                        index2 = j
                        arr.append([index1, index2])
            
        return min(arr)