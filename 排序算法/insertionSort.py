def insertSort(arr):
    for i in range(len(arr)):
        preIndex = i -1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1]=arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr
array = [3,5,2,15,36,7,30,50,22]
print(insertSort(array))
