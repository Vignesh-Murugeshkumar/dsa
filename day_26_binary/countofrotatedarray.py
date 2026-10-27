def countRotatedarray(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        next_idx=mid+1
        prev_idx=mid-1
        if arr[mid]<=arr[next_idx] and arr[mid]<=arr[prev_idx]:
            return mid
        elif arr[mid]<=arr[high]:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=[4,5,6,7,0,1,2]
print(countRotatedarray(arr))