class Solution(object):
    def singleNumber(self, nums):
        st = set()
        for c in nums: 
            x = nums.pop()
            if x not in st:
                st.add(x)
            else:
                st.remove(x)
        return st.pop()




        
