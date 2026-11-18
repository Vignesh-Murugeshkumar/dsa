def sortcharbyfrequency(s):
    dict={}
    for i in s:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    sorted_dict=mergesort(list(dict.items()))
    result=""
    for i in sorted_dict:
        result+=i[0]*i[1]
    return result
def mergesort(dict):
    if len(dict)<=1:
        return dict
    mid=len(dict)//2
    left=mergesort(dict[:mid])
    right=mergesort(dict[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i][1]>right[j][1]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

s="tree"
print(sortcharbyfrequency(s))