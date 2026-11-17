def find_student(students, student):
    for nome, score in students:
        if nome == student:
            return score


def median(numbers):
    ordered_numbers = sorted(numbers)
    if not ordered_numbers:
        raise ValueError("A mediana não está definida para uma lista vazia")

    middle = len(ordered_numbers) // 2
    if len(ordered_numbers) % 2 == 0:
        return (ordered_numbers[middle - 1] + ordered_numbers[middle]) / 2
    return ordered_numbers[middle]



students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]


resultado = find_student(students, "Alice")


if resultado is None:

    print("Student not found")

else:
    print(resultado)
    


