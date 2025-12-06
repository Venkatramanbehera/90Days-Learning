def oddEven(arr):
    oddCount = 0
    evenCount = 0

    for num in arr:
        if num % 2 == 0:
            evenCount = evenCount + 1
        else:
            oddCount = oddCount + 1

    return oddCount, evenCount


print(oddEven([1,2,3,4,5]))
            