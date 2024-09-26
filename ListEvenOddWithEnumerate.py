students =["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[],[]]
    for index, student in enumerate(students):
        if index %2==0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

divide_students(students)