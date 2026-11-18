def reorganizeString(s):
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    sorted_items = mergesort(list(freq.items()))
    if sorted_items[0][1] > (len(s) + 1) // 2:
        return ""
    result = [""] * len(s)
    idx = 0
    for char, count in sorted_items:
        for _ in range(count):
            if idx >= len(s):
                idx = 1
            result[idx] = char
            idx += 2

    return "".join(result)
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
print(reorganizeString("aab"))   
