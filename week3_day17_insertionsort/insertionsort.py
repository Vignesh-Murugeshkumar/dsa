def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1    
        arr[j+1]=key
    return arr
arr=[6,4,3,9,8,7,5,2,1]
print(insertionsort(arr))
