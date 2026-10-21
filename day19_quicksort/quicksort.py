def quicksort(arr,low,high):
    if(low<high): 
        pivot_index=partition(arr,low,high) # slecting picot index
        quicksort(arr,low,pivot_index-1) # sorting elements less than pivot
        quicksort(arr,pivot_index+1,high) # sorting elements greater than pivot

def partition(arr,low,high):
    pivot=arr[high] #pivot as last elemnt 
    i=low-1
    for j in range(low,high):
        if(arr[j]<pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
arr=[2,3,7,6,5,4,8,9,1]
quicksort(arr,0,len(arr)-1)
print(arr)