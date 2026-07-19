class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        outList = []

        for i in nums:
            key = i

            if key not in freqDict:
                freqDict[key] = 1
            else:
                freqDict[key] += 1

        while len(outList) < k:
            highFreq = 0
            lock = 0

            for key, v in freqDict.items():
                if v > highFreq:
                    highFreq = v
                    lock = key

            outList.append(lock)
            del freqDict[lock]
                

        return(outList)
        
        