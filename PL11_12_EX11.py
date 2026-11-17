students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]  

def sort_by_score(students):
    for i in range(len(students)):
        for j in range(len(students) - 1):
            if students[j][1] < students[j + 1][1]:
                students[j], students[j + 1] = students[j + 1], students[j]
    return students


print(sort_by_score(students))



