class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnList = []

        while len(strs) > 0:
            anagrams = self.checkAnagrams(strs[0], strs)
            returnList.append(anagrams)

            for i in anagrams:
                if i in strs:
                    strs.remove(i)
        
        return(returnList)


    def checkAnagrams(self, word, strs):
        sortedWord = sorted(word)
        return [s for s in strs if sorted(s) == sortedWord]