def quicksort(arr, left, right, x):
    print("nr. ",x,": ",arr)
    x += 1
    if left < right:
        # Partition the array
        pivot_index = partition(arr, left, right)

        # Recursively sort the sub-arrays
        quicksort(arr, left, pivot_index - 1, x)
        quicksort(arr, pivot_index + 1, right, x)

def partition(arr, left, right):
    # Choose the rightmost element as the pivot
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

# Example usage:
x = 0
arr = [38,81,22,48,13,69,93,14,45,58,79,72]
quicksort(arr, 0, len(arr) - 1, x)
print("Sorted array:", arr)
