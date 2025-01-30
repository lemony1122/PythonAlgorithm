def sorting(arr1,arr2):
    if arr1[0]>arr2[0]:
        result = arr2 + arr1
    else :
        result = arr1 + arr2

    for i in range(len(result)-1):
        checked = False
        for j in range(len(result)-1-i):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1],result[j]
                checked = True
        if not checked:
            break
    return result

assert sorting([1,3,5],[2,4,6]) == [1,2,3,4,5,6]