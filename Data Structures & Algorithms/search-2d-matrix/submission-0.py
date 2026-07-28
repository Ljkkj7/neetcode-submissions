class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                l, r = 0, len(i)-1

                while l <= r:
                    mid = l + (r - l) // 2

                    if i[mid] == target:
                        return True
                    
                    elif i[mid] < target:
                        l = mid + 1
                    
                    else:
                        r = mid - 1
        return False 
            