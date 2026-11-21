class Solution:
    def isSorted(self, arr):
        n=len(arr)
        for i in range (1,n):
            if(arr[i-1]>arr[i]):
                 return False
        return True
