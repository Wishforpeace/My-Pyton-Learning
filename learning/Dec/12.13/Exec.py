def Selection_sort(array_list):
    length = len(array_list)
    for i in range(length):
        k = i
        for j in range(i+1,length):
            if array_list[k]>array_list[j]:
                k = j
            array_list[k],array_list[i] = array_list[i],array_list[k]
        print(array_list)
array = [6,3,5,7,0]
Selection_sort(array)
print(array)
