def mergesort(arr):
    if len(arr)<=1:
        return arr
    left=arr[:len(arr)//2]
    right=arr[len(arr)//2:]
    left=mergesort(left)
    right=mergesort(right)
    return merge(left, right)
def merge(left, right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

arr=[5,3,1,4,8,9,2,6,7]
print(mergesort(arr))
