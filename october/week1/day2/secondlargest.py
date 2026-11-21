def secondlargestinarray(arr):
    maxvalue=arr[0]
    secondmaxvalue=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maxvalue:
            secondmaxvalue=maxvalue
            maxvalue=arr[i]
        elif arr[i]>secondmaxvalue and arr[i]!=maxvalue:
            secondmaxvalue=arr[i]
    return secondmaxvalue
arr=[4 ,2,1,5,3]
print(secondlargestinarray(arr))