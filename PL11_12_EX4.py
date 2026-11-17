def find_two_largest(arr):
    """
    Find the two largest unique numbers in the given array.

    Parameters:
    arr (list): The list of elements to search through.

    Returns:
    tuple: A tuple containing the two largest unique numbers, or None if not enough unique numbers exist.
    """
    unique_numbers = set(arr)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[0], sorted_numbers[1]

numbers = [3, 5, 2, 3, 8, 3, 10]
result = find_two_largest(numbers)

print(result)  # Example usage