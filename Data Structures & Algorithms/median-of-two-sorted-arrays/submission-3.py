class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combine=nums1+nums2
        combine.sort()
        length=len(combine)

        if length%2==0:
            return (combine[int(length/2)-1]+combine[int(length/2)])/2
        else:
            return combine[int(length/2)]
        