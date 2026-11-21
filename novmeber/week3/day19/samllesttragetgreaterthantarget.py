def smallestletter_greater_than_target(letters, target):
    n=len(letters)
    low=0
    high=n
    while low<=high:
        mid=(low+high)//2
        if letters[mid]<=target:
            low=mid+1  
        else:
            high=mid
    return letters[low] if low < n else letters[0]

s=["c", "f", "j"]
target="a"
print(smallestletter_greater_than_target(s, target))  