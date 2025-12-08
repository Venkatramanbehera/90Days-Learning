def linearSaerch(arr, target):
    for i, num in enumerate(arr) :
        if num == target:
            return i

    return -1

print(linearSaerch([1, 9, 90, 5], 2))
print(linearSaerch([1, 9, 90, 5], 5))