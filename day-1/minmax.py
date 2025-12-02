def find_min_max(arr):

    min = arr[0]
    max = arr[0]

    for num in arr:
        if num > max: 
            max = num

        if num < min: 
            min = num

    return [min, max]

my_numbers = [12, 45, 2, 9, 100, -5, 56]
minimum, maximum = find_min_max(my_numbers)

print(maximum)
print(minimum)