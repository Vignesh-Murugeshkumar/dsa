def solution(arr):
    if len(arr)==0:
        return arr
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return arr[:i+1] 
array=[1,1,2,2,3,4,4,5]
print(solution(array))