def search(values, target) -> int:
    """
    Binary search for a target value in a sorted list of values.
    :param values: A sorted list of values.
    :param target: The target value to search for.
    :return: The index of the target value in the list, or -1 if not found.
    """

    left, right = 0, len(values) - 1

    while left <= right:
        mid = (left + right) // 2
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
values = [1, 2, 3, 4, 5]
target = 3
index = search(values, target)
print(f'Target {target} found at index {index}')