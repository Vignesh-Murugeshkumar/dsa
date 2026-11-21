class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashset=set()
        result=set()
        for num in nums1:
            hashset.add(num)
        for num in nums2:
            if num in hashset:
                result.add(num)
        return list(result)
arr1=[4,9,5]
arr2=[9,4,9,8,4]
print(Solution().intersection(arr1,arr2))