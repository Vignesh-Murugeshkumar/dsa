def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            #check whether the current element is greater than the next element
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j] #perform simultaneous swap 
    return arr
arr=[64, 34, 25, 12, 22, 11, 90]
print(bubblesort(arr))