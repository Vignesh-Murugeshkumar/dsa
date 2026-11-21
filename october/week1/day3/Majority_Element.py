def majorityelemnt(arr):
    count={}
    for i in range(len(arr)):
        if arr[i] in count:
            count[arr[i]]+=1
        else:
            count[arr[i]]=1
    for key in count:
        if count[key]>len(arr)//2:
            return key
    return -1
arr=[3,2,3]