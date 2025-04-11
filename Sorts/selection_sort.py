# Selection sort
def selection_sort_inplace(array, n):
    start = 0
    while start < n: #go until start has checked all the positions in the list
        index = start + 1 #walk the rest of the array to the end
        min = start #will hold the location of the smallest value 'index' comes across
        while index < n:
            if array[index] < array[min]: #if something is smaller
                min = index #save the minimum values location
            index += 1
        #swap the minimum value into the start position
        temp = array[start]
        array[start] = array[min]
        array[min] = temp
        #move start forward to do it all again for the next unsorted position
        start += 1