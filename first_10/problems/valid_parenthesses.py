class Solution(object):
    def isValid(self, s):
        stack = []
        dec = {"{":"}","[":"]","(":")"}
        for c in s:
            if stack and c not in dec.values():
                stack.append(c)
            else:
                if c in dec.values():
                    stack.append(c)
                elif c in dec and c == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return True
        return False


        
