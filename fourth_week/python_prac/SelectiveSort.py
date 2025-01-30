# def selectionsort(lst):
#     iters = len(lst) - 1
#     for iter in range(iters):
#         minimun = iter
#         for cur in range(iter + 1, len(lst)):
#             if lst[cur] < lst[minimun]:
#                 minimun = cur
#
#         if minimun != iter:
#             lst[minimun], lst[iter] = lst[iter], lst[minimun]
#
#     return lst

def selectionsort(arr):
    for i in range(len(arr)-1):
        min = i    #가정
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
            if min != i :
                arr[min], arr[i] = arr[i], arr[min]

    return arr


assert selectionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert selectionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]