def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)/2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left)+middle+quicksort(right)

print quicksort([2, 12, 3,4,5,1,1])
