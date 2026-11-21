
def merge(arr1, arr2):
    n=len(arr2)
    m=len(arr1) - len(arr2 )  
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:

        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1

        k -= 1

    # Copy remaining elements from B
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1

    return arr1 


# Main
arr1=[1, 4, 7, 10, 0, 0, 0]
arr2=[2, 5, 8]
print(merge(arr1, arr2))
