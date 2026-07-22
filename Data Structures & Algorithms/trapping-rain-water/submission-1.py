class Solution:
    def trap(self, height: List[int]) -> int:
        distances = self.calculate_traps(height)
        areas = []
        max_area = 0

        for i in distances:
            limit = min(i[0], i[-1])

            spikes = 0
            distance = 0
            area = 0

            for j in range(1, len(i) - 1):
                distance += 1
                spikes += i[j]

            area = (distance * limit) - spikes
            areas.append(max(0, area))
        
        for i in areas:
            max_area += i
        
        return max_area

    def calculate_traps(self, height):
        l, r = 0, 1
        distances = []

        while r < len(height):
            if height[l] <= height[r]:
                area_points = []
                for i in range(l, r+1):
                    area_points.append(height[i])
                distances.append(area_points)
                l = r
                r += 1
            else:
                r += 1
        
        if l < len(height) - 1:
            r = len(height) - 1
            peak = r
            while r >= l:
                if height[r] >= height[peak]:
                    if r != peak:
                        distances.append(height[r:peak+1][::-1])
                    peak = r
                r -= 1

        return distances