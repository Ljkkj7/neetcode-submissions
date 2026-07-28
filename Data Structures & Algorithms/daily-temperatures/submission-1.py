class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        distances = []

        for i in range(len(temperatures)):
            count = self.distance_calculate(temperatures, temperatures[i], i)
            distances.append(count)
        
        return distances
    
    def distance_calculate(self, temperatures, anchor, i):
        count = 1
        stack = temperatures[i+1::]

        while len(stack) > 0:
            if stack.pop(0) > anchor:
                return count
            count += 1

        if len(stack) == 0 and count > 0:
            count = 0

        return count

                
