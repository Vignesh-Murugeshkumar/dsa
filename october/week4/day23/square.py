class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<2:
            return True
        left,right=2,num//2
        while left<=right:
            mid=left+(right-left)//2
            sq=mid*mid
            if sq==num:
                return True
            elif sq<num:
                left=mid+1
            else:
                right=mid-1
        return False
arr=[1,2,3,4,5,6,7,8,9]
for i in arr:
    print(Solution().isPerfectSquare(i))