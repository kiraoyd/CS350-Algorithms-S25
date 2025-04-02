#n is the size of the input (number of elements in the array)
#Rough time complexity: 3n + 3
#Three guaranteed constant time operations per loop iterations (3n)
#Three constant time operations outside the n-dependent loop (+3)
#Ultimately, constants don't matter, the highest order term of n dominates
#This runs in Linear Time: in the worst case, Big O(n)
def linear_search(array, target, n):
    index = 0
    while index < n:
        if array[index] == target:
            return index
        index += 1
    return -1 #error-flag, target not found

#If we naiively perform the size determination INSIDE the function:
#Now the rough time complexity is: 3n + 3 + n
#We iterate over the n-sized array once more in the function (+n)
# This is still in the order of growth of 'n', Linear Time: 3n + 3 + n = 4n + 3
def linear_search_and_size(array, target):
    index = 0
    size = len(array) #assume this function iterates through each element to count them
    while index < n:
        if array[index] == target:
            return index
        index += 1
    return -1 #error-flag, target not found



