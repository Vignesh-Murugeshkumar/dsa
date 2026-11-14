def firstnonreapeatingelement(arr):
    hashmap={}
    for i in range(len(arr)):
        hashmap[arr[i]]=hashmap.get(arr[i],0)+1
    for i in range(len(arr)):
        if hashmap[arr[i]]==1:
            return arr[i]
    return -1
arr=[4,5,1,2,0,4]
print(firstnonreapeatingelement(arr))