students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]  

def sort_by_score(students):

    resulado = sorted(students, key=lambda students: students[1], reverse=True)

    print(resulado)
        

sort_by_score(students)


