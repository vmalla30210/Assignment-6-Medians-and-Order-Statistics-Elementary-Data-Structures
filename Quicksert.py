import random

def partition_random(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return partition(arr, low, high, high)

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = partition_random(arr, low, high)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

# Test case
arr = [12, 3, 5, 7, 4, 19, 26]
k = 3
result = quickselect(arr, 0, len(arr)-1, k)
print(f"The {k+1}th smallest element is {result}")
