class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_pointer = 0
        r_pointer = len(heights)-1
        max_area = 0

        while l_pointer < r_pointer:
            height = min(heights[l_pointer], heights[r_pointer])
            area = height * (r_pointer - l_pointer)

            if area > max_area:
                max_area = area

            if heights[l_pointer] < heights[r_pointer]:
                l_pointer += 1
            else:
                r_pointer -= 1
            
        return max_area
        