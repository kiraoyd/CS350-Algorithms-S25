
def merge_sort(array, low, high):
    if low >= high:
        return

    mid = (low + high) //2
    merge_sort(array, low, mid) #left subarray
    merge_sort(array, mid+1, high) #right subarray

    #Once the children return from having sorted THEIR arrays, its time to merge them
    #merge needs low, mid and high because that's how it keeps track of
    #which subarrays represent the left and right children
    merge(array, low, mid, high)

#merges two subarrays
#then copies back to the original array
def merge(array, low, mid, high):
    temp = []

    left = low #start of the left child
    right = mid+1 #start of the right child

    #loop to process both subarrays at the same time
    #stop when one subarray is exghausted
    while left <= mid and right <= high:
        if array[left] < array[right]:
            #left has the smallest data, add it
            temp.append(array[left])
            left += 1
        elif array[left] > array[right]:
            #right has the smallest data, add it
            temp.append(array[right])
            right += 1

    #One of the subarrays is now fully copied to temp,
    #and the other still has data to process

    #if it's the left subarray...
    while left <= mid:
        temp.append(array[left])
        left += 1

    #if it's the right sub array...
    while right <= high:
        temp.append(array[right])
        right += 1

    #now we've processed everything in temp
    #copy back all data from temp to array
    temp_index = 0
    copy_to = low
    while temp_index < len(temp): #iterate through temp
        array[copy_to] = temp[temp_index]
        copy_to += 1
        temp_index += 1
