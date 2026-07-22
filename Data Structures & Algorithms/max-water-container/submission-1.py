class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                distance = min(heights[i],heights[j])
                width = j - i
                area = distance * width
                if area > max_area:
                    max_area = area
        
        return max_area

        