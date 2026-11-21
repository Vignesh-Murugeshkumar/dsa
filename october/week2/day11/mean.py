
def trimMean(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    remove=n//20
    total=0
    count=0
    for i in range(remove,n-remove):
        total+=arr[i]
        count+=1
    return total/count

arr=[6,2,7,5,1,2,0,1,9,15]
print(trimMean(arr))
