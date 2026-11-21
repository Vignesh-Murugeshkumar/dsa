def sqrt(x):
    if x<=2:
        return x
    low=2
    high=x//2
    ans=1
    while low<=high:
        mid=(low+high)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            ans=mid
            low=mid+1
        else:
            high=mid-1 
    return ans
arr=[1,2,3,4,5,6,7,8,9]
for i in arr:
    print(sqrt(i))