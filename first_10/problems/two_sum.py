class Solution(object):
    def twoSum(self, nums, target):
        srt_nums=sorted(nums)
        i=0
        j=len(nums)-1
        cond=False
        while i < j and cond == False:
            if(srt_nums[i] + srt_nums[j] == target):
                num1=srt_nums[i]
                num2=srt_nums[j]
                cond=True
            elif(srt_nums[i] + srt_nums[j] > target):
                j=j-1
            else:
                i=i+1
        if cond == False:
            return False
        res=[]
        for x in range(0,len(nums)):
            if len(res)==2:
                return res
            if nums[x] == num1 or nums[x] == num2:
                res.append(x)
        return res            
            


        


        
