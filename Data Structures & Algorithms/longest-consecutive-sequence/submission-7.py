class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        
        temp_ls=list(set(nums))
        temp_ls.sort()
        print(temp_ls)
        ans=1
        count=1
        for i in range(1,len(temp_ls)):
            if temp_ls[i]==temp_ls[i-1]+1:
                print(temp_ls[i])
                count+=1
            else:
                count=1
            ans = max(ans,count)
        # count+=1
        return ans
        