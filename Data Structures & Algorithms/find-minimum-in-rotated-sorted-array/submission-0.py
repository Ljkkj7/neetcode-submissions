class Solution:
    def findMin(self, nums: List[int]) -> int:
        target = min(nums)
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return nums[mid]
            
            if nums[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        return(target)
        