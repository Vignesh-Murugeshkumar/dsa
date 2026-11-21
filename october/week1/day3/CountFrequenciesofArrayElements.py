def CountFrequenciesofArrayElements(arr):
    hashmap={}
    for i in range(len(arr)):
        hashmap[arr[i]]=hashmap.get(arr[i],0)+1
    return hashmap
arr=[1,2,3,4,5,1,2,3,4,5]
print(CountFrequenciesofArrayElements(arr))