class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = 0
        curr = 0
        for i in nums:
            if i != 0:
                curr += 1
            else:
                curr = 0
            streak = max(curr, streak)
        return streak
            
