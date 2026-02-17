class Solution(object):
    def isAnagram(self, s, t):
        size = len(s)
        if size != len(t) or   0:
                return False
                
        t1 = {}
        s1 = {}
        for i in range(0,size) :
            if t[i] in t1:
                t1[t[i]]=t1[t[i]]+1
            else :
                t1[t[i]]=1
            if s[i] in s1:
                s1[s[i]]=s1[s[i]]+1
            else :
                s1[s[i]]=1
        if t1 == s1 :
            return True
        return False
