def average(arr):
    arr_len = len(arr)

    if arr_len == 0:
        return "CAN not be empty Array."
    
    sum = 0

    for num in arr:
        sum = sum + num

    return sum/arr_len

print(average([]))
print(average([2, 5, 8]))