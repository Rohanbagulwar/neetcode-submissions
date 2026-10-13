class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag=False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target-nums[i]==nums[j]:
                    print(nums[i],nums[j])
                    flag=True
                    break
            if flag==True:
                break
        return [i,j]

        