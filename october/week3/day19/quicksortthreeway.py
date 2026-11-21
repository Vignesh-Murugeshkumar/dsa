def quicksort_three_way(arr, low, high):
    if low < high:
        lt, gt = partition(arr, low, high)
        quicksort_three_way(arr, low, lt - 1)
        quicksort_three_way(arr, gt + 1, high)
def partition(arr, low, high):
    pivot=arr[high]
    i=low
    lt=low
    gt=high
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    return lt, gt

arr=[2,3,7,6,5,4,8,9,1]
quicksort_three_way(arr,0,len(arr)-1)
print(arr)