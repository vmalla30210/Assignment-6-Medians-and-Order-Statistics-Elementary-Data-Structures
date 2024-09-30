def partition(arr, low, high, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def select(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot = median_of_medians(arr, low, high)
    pivot_index = partition(arr, low, high, pivot)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return select(arr, low, pivot_index - 1, k)
    else:
        return select(arr, pivot_index + 1, high, k)

def median_of_medians(arr, low, high):
    n = high - low + 1
    if n < 10:
        return sorted(arr[low:high+1])[n//2]
    
    medians = []
    for i in range(low, high + 1, 5):
        group = sorted(arr[i:i + 5])
        medians.append(group[len(group)//2])
    
    return select(medians, 0, len(medians) - 1, len(medians)//2)

# Test case
arr = [12, 3, 5, 7, 4, 19, 26]
k = 3
result = select(arr, 0, len(arr)-1, k)
print(f"The {k+1}th smallest element is {result}")
