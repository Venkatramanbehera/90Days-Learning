def rotate_by_one(arr):
    # distant = len(arr) - 1

    # j = 1
    # while(j <= distant):
    #     arr[0], arr[j] = arr[j], arr[0]
    #     j+=1

    # return arr

    last_elem = arr[-1]
    rest_arr = arr[:-1]
    return [last_elem] + rest_arr



print(rotate_by_one([1, 2, 3, 4, 5]))
# print(rotate_arr[1, 2, 3, 4, 5])