
def partition(array, start, end):
    index = start
    pivot_spot = start
    pivot_value = array[end]
    while index < end:
        if array[index] <= pivot_value:
            #swap
            temp = array[index]
            array[index] = array[pivot_spot]
            array[pivot_spot] = temp
            #advance pivot_spot
            pivot_spot += 1
        index += 1

    #final swap between the pivot value and the value at pivot_spot
    array[end] = array[pivot_spot]
    array[pivot_spot] = pivot_value

    return pivot_spot
def quicksort(array, start, end):
    if start >= end:
        return

    mid = partition(array, start, end)
    #go left
    quicksort(array, start, mid-1)
    #go right
    quicksort(array, mid+1, end)

def main():
    array = [8, 2, 7, 8, 8, 3, 5, 10, 1, 0]
    start = 0
    end = len(array) - 1
    quicksort(array, start, end)
    print(f"The sorted array: {array}")

main()
