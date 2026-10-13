class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        minimum=min(nums)
        maximum=max(nums)

        for i in range(minimum,maximum+1):
            if nums.count(i)>1:
                return i
        
        