def solution(arr):
    if len(arr)==0: #if the array is empty, return the array
        return arr
    i=0 #assigning the first index to i, which will be used to keep track of the unique elements in the array
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]: #if the current elemnt is not equal to the arr[i],then its is a uniqe element and we will increment the i value to the next value which current j vlaue
            i+=1
            arr[i]=arr[j] # assign the current element to the next unique position
    return arr[:i+1] # return the array with the unique elements
array=[1,1,2,2,3,4,4,5]
print(solution(array))