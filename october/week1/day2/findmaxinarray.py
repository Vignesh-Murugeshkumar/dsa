def findmaxinarray(arr):
    maxvalue=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maxvalue:
            maxvalue=arr[i]
    return maxvalue
arr=[4 ,2,1,5,3]
print(findmaxinarray(arr))