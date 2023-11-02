def partition(arr, left, right):
    i = left + 1
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]


    if arr[i] < pivot:
        arr[i], arr[j] = arr[j], arr[i]
    return i

# Example usage:
arr = [11, 4, 20, 45, 32, 60, 98, 70]
left = 0
right = len(arr) - 1
pivot_index = partition(arr, left, right)

print("Array after partitioning:", arr)
print("Pivot element:", arr[pivot_index])
