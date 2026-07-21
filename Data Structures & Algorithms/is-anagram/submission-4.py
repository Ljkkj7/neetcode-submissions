class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = [x for x in s]
        tArr = [y for y in t]
        flag = True

        if len(sArr) != len(tArr):
            return False

        sArr.sort()
        tArr.sort()

        for i in range(len(sArr)):
            if sArr[i] == tArr[i]:
                continue
            else:
                flag = False
        
        return flag
