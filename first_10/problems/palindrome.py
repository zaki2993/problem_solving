class Solution(object):
    def isPalindrome(self, s):
        result=""
        for x in s:
            if x.isalnum():
                result+=x.lower()
        pal=result[::-1]
        if result == pal:
            return True
        return False
