class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            peek = i
            sumTotal = 1
            for j in range(len(nums)):
                if peek != j:
                    sumTotal *= nums[j]
            output.append(sumTotal)
        return(output)