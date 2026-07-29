class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        twoMid = len(nums3) % 2

        if twoMid == 0:
            return ((nums3[len(nums3)//2] + nums3[(len(nums3)//2)-1]) / 2)
        else:
            return nums3[len(nums3)//2]