class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new_array = sorted(nums1+ nums2)
        n = len(new_array)

        if n%2 == 1:
            return float(new_array[int (n/2)])

        elif n%2 == 0:
            return (new_array[int(n/2-1)]+new_array[int(n/2)])/2

        elif n == 0:
            return float(0)

        
