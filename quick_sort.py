def quicksort(arr) -> list:
    if len(arr) <= 1:
        return arr  # Base case: a list of 0 or 1 elements is already sorted

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quicksort(left) + middle + quicksort(right)  # Recursively sort sublists

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)
