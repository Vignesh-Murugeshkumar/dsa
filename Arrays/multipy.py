class Solution:
    def updateArray(self, arr):
        original = arr.copy()
        n = len(arr)
        if n==1:
            return arr
        for i in range(n):
            if i == 0:
                arr[i] = original[i]*original[i+1]
            elif i == n - 1:
                arr[i] = original[i]*original[i-1]
            else:
                arr[i] = original[i] * original[i-1]*original[i+1]

        return arr