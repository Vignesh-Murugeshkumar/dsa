def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=[5,3,1,4,8,9,2,6,7]    
print(selectionSort(arr))