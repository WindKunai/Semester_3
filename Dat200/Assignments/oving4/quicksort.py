def quicksort(arr, left, right, x):
    if left < right:
        x += 1
        partition_pos = partition(arr, left, right)
        if x == 2:
            print("after one attmpt")
            return arr
        
        quicksort(arr, left, partition_pos - 1, x)
        quicksort(arr, partition_pos + 1, right, x)
    
    return arr  # Return the array in the base case

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i

A = [38, 81, 22, 48, 13, 69, 93, 14, 45, 58, 79, 72]
index_A = 0
x = 0
print(quicksort(A, index_A, len(A) - 1, x))
