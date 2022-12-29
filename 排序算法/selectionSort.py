def selectSort(arr):
    for i in range(len(arr)-1):
        minIndex = i 
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            arr[minIndex],arr[i] = arr[i],arr[minIndex]
       
    return arr           
array = [33,32,42,84,82,3]
print(selectSort(array))
