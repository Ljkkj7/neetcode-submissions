class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = []
        list_asc = sorted(nums)
        index = 0
        max_len = 0

        if len(nums) == 0:
            return(0)

        while index < len(list_asc):
            if index == len(list_asc)-1:
                break
            
            if list_asc[index]+1 == list_asc[index+1] or list_asc[index] == list_asc[index+1]:
                sequence.append(list_asc[index])
                sequence.append(list_asc[index+1])
            else:
                sequence = []
            check_len = len(set(sequence))
            if check_len > max_len:
                max_len = len(set(sequence))
            index += 1
        
        if max_len > 0:
            return max_len
        else:
            return(1)


            

               