class Solution:
    def isPalindrome(self, s: str) -> bool:
        string  = "".join(char for char in s if char.isalnum()).lower()
        
        r_pointer = len(string)-1
        l_pointer = 0

        while l_pointer < r_pointer:
            if string[l_pointer] != string[r_pointer]:
                return False
            r_pointer -= 1
            l_pointer += 1
            print(r_pointer, l_pointer)

        return True