def bubbleSortWithParity(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-1):
            if arr[j]%2==1 and arr[j+1]%2==0: #if current element is odd and next element is even
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break   
    return arr
arr=[64, 34, 25, 12, 22, 11, 90]
print(bubbleSortWithParity(arr))