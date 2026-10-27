class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m,n=len(matrix),len(matrix[0])
        low,high=0,m*n-1
        while low<=high:
            mid=low+(high-low)//2
            row,col=mid//n,mid%n
            val=matrix[row][col]
            if val==target:
                return True
            elif val<target:
                low=mid+1
            else:
                high=mid-1
        return False
arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
print(Solution().searchMatrix(arr,target))