# partition(A; p; q)
# let x = A[p]
# let i = p 
# for j = p+1 to q:
#     do if A[j]<x,
#         then i = i+1
#         exchange A[i] and A[j]
#         print A
# exchange A[i] ahd A[j]
# print A 
# return 1


# A=[ 6; 10; 13; 5; 8; 3; 2; 11 ]

def partition(A, p, q):
    x = A[p]
    i = p

    for j in range(p + 1, q + 1):
        if A[j] < x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            print(A)

    A[i], A[p] = A[p], A[i]
    print(A)

    return i

A = [6, 10, 13, 5, 8, 3, 2, 11]
pivot_index = 0  # Index of the pivot element (6)

partition_index = partition(A, pivot_index, len(A) - 1)
