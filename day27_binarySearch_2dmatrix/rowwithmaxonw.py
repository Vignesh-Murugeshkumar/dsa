class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        max_row_idx=0
        max_one_count=0
        for r in range(len(mat)):
            count=sum(mat[r])
            if count>max_one_count:
                max_one_count=count
                max_row_idx=r
        return [max_row_idx,max_one_count]
arr=[[0,1],[1,0]]
print(Solution().rowAndMaximumOnes(arr))