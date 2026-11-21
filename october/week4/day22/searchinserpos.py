def searchinsertpos(arr,target):
    low=0
    high=len(arr)-1
    for i in range(len(arr)):
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return low
arr=[2,3,4,5,6,8,9]
target=2
print(searchinsertpos(arr,target))
print(searchinsertpos(arr,7))
print(searchinsertpos(arr,1))