# def insertionsort(lst):
#     # 0번째 요소는 이미 정렬되어있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
#     for cur in range(1, len(lst)):
#         # 비교지점이 cur-1 ~ 0(=cur-cur)까지 내려간다.
#         for delta in range(1, cur + 1):
#             cmp = cur - delta
#             if lst[cmp] > lst[cmp + 1]:
#                 lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
#             else:
#                 break
#     return lst





def insertionsort(arr):
    for i in range(len(arr)-1):
        for j in reversed(range(1,i+2)):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else :
                break
    return arr





assert insertionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]