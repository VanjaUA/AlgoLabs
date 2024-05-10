def is_subarray(array, subarray):

    if len(subarray) > len(array):
        return False

    i = 0
    j = 0

    while i < len(array) and j < len(subarray):
        if array[i] == subarray[j]:
            j += 1
        else:
            j = 0 
        i += 1        

    if j == len(subarray):
        return True
    else:
        return False


print(is_subarray([1, 2, 3, 4, 5,1,2,3,5], [1,2, 3, 5]))