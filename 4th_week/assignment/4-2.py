def meetingMax(list):
    count = 1
    for i in range(len(list)-1):
        min = i
        for j in range(i+1,len(list)):
            if list[min][1] > list[j][1]:
                min = j
            if min != i :
                list[min], list[i] = list[i], list[min]

    while i<len(list):
        start = 0
        if list[start][1] <= list[i][0]:
            start = i
            i= start+1
            count+=1

    return count

# print(meetingMax([(1, 3), (2, 4), (5, 8), (6, 10), (8, 11), (10, 12)]))
assert meetingMax([(1, 3), (2, 4), (5, 8), (6, 10), (8, 11), (10, 12)]) == 3