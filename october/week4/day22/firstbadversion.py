# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while left<right:
            mid=(left+right)//2
            if isBadVersion(mid):
                right=mid
            else:
                left=mid+1
        return left
def isBadVersion(version):
    if version>=4:
        return True
    else:
        return False

arr=[1,2,3,4,5,6,7,8,9]
print(Solution().firstBadVersion(9))