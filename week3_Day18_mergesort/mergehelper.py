def mergehelper(left,right):
    result=[0]*(len(left)+len(right))
    i=0
    j=0
    k=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result[k]=left[i]
            i+=1
        else:
            result[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        result[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        result[k]=right[j]
        j+=1
        k+=1
    return result
left=[1,3,5,7]
right=[2,4,6,8]
print(mergehelper(left,right))