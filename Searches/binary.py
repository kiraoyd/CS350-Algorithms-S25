#A search that can be done over a previously sorted array
def binary_search(array, target, n):
    low = 0 #tracks beginning index of search space
    high = n-1 #tracks last index of search space
    while low <= high:
        mid = (low + high) // 2 #integer divide
        if array[mid] == target:
            #found, stop search
            return mid
        if array[mid] < target:
            #keep searching, but only in the right half
            low = mid + 1 #move low to one past mid, the new search spaces beginning index
        if array[mid] > target:
            #keep searching, but only in the left half
            high = mid - 1 #move high to one behind mid, the new search spaces last index

    return -1 #error-flag, target not in array data