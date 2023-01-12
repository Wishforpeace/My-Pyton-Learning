def QuickSort(arr):
    #元素少于两个，即为有序
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i>pivot]

        return QuickSort(less)+[pivot]+QuickSort(greater)



print(QuickSort([3,2,1,6,4,9,7,8]))
