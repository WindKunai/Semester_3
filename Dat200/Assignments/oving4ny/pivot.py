def partition(arr, left, right):
    i = left
    j = right-1
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


arr = [11, 4, 20 ,45 ,32 ,60 ,98 ,70]
A_index = 0

print(partition(arr, A_index, len(arr)-1))