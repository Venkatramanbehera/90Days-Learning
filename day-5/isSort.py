def isSort(arr):
    length_arr = len(arr)
    if length_arr == 1:
        return True
    for i in range (length_arr-1):
        if arr[i] > arr[i + 1]:
            return False
        
    return True


print(isSort([1]))
print(isSort([2, 1, 7, 3, 9]))
print(isSort([ 1, 3, 9, 11]))