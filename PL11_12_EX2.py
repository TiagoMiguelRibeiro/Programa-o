def linear_search_count(arr, target):
    """
    Perform a linear search on the given array to find the target value.

    Parameters:
    arr (list): The list of elements to search through.
    target: The value to search for in the array.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    count = 0
    for index, value in enumerate(arr):
        if value == target:
            count += 1
    return count

numbers = [3, 5, 2, 3, 8, 3, 10]

print(linear_search_count(numbers, 3))  # Example usage
