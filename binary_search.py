def binary_search(number_list, target):
    """
    Return the index of target in a sorted list, or -1 if it is not present.
    """
    left = 0
    right = len(number_list) - 1

    while left <= right:
        middle = (left + right) // 2
        if number_list[middle] == target:
            return middle
        if number_list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

print(binary_search([1, 2, 3, 4, 5], 3))  # Example usage