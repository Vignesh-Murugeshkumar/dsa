def selectionSortK(arr,k):
    n=len(arr)
    for i in range(k): # sort only the first k elements
        for j in range(i,n):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=[5,3,1,4,8,9,2,6,7]
k=5
print(selectionSortK(arr,k))