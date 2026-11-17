def bumble_sort(number_list):
    """
    This function implements the bubble sort algorithm to sort a list of numbers in ascending order.
    """
    n = len(number_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
    return number_list

print(bumble_sort([5, 2, 9, 1, 5, 6]))  # Example usage

