class Solution:

    def isPalindrome(self, s: str) -> bool:

        front=0
        back=len(s)-1
        string=''
        reverse=''

        for char in range(int(len(s))):
            if s[char].isalnum():
                string+=s[char].lower()

            if s[back].isalnum():
                reverse+=s[back].lower()
                
            back-=1
        if string==reverse:
            return True
        else:
            return False
    