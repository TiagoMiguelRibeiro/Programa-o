def sorted_numbers(number_list):
    """
    This function takes a list of numbers as input and returns a new list containing the numbers sorted in ascending order.
    """
    return sorted(number_list)

numeros = [5, 2, 9, 1, 5, 6]

sorted_list = sorted_numbers(numeros)
print(sorted_list)  # Output: [1, 2, 5, 5, 6, 9]

