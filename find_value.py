def find_value(number_list, target):
    """
    This function takes a list of numbers and a target number as input.
    It returns True if the target number is found in the list, otherwise it returns False.
    """
    for number in number_list:
        if number == target:
            return True
    return False

result = find_value([1, 2, 3, 4, 5], 4)  # Example usage
print(result)  # Output: True