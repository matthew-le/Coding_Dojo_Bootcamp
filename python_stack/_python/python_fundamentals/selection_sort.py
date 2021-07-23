# use selection sort method to organize numbers
arr = [22, 5, 10, 100, 66, 24]

def select_sort(arr):
    for i in range(len(arr) - 1):
        # Find the minimum element in remaining
        minPosition = i
        for j in range(i+1, len(arr)):
            if arr[minPosition] > arr[j]:
                minPosition = j
        # Swap the found minimum element with minPosition 
        temp = arr[i]
        arr[i] = arr[minPosition]
        arr[minPosition] = temp
    return arr

print(select_sort(arr))