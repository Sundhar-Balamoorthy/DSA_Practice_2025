def sort(arr):
    n = len(arr)
    low = 0
    high = n - 1
    middle = 0
    
    while middle <= high:
        if arr[middle] == 0:
            arr[low], arr[middle] = arr[middle], arr[low]
            low += 1
            middle += 1
        elif arr[middle] == 1:
            middle += 1
        else:
            arr[middle], arr[high] = arr[high], arr[middle]
            high -= 1

arr = [0, 1, 2, 0, 2, 1, 0]
sort(arr)
print(arr)
