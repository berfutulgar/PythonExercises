#Comprehensions

#List Comprehension

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x*20/100 + x

for salary in salaries:
    print(new_salary(salary))


null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary*2))

print(null_list)

#If we use this comprehension method:

print([new_salary(salary*2) if salary < 3000 else new_salary(salary) for salary in salaries]) #[2400.0, 4800.0, 3600.0, 4800.0, 6000.0]

print([salary*2 for salary in salaries]) #[2000, 4000, 6000, 8000, 10000]

print([salary*2 for salary in salaries if salary < 3000]) #[2000, 4000]

print([salary*2 if salary <3000 else salary*0 for salary in salaries]) #[2000, 4000, 0, 0, 0]

print([new_salary(salary*2) if salary <3000 else new_salary(salary*0) for salary in salaries])  #[2400.0, 4800.0, 0.0, 0.0, 0.0]


students = ["John", "Mark", "Venessa", "Mariam"]

students_no = ["John", "Venessa"]

print([student.lower() if student in students_no else student.upper() for student in students]) #['john', 'MARK', 'venessa', 'MARIAM']


#Dict Comprehension

dictionary = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}

print(dictionary.keys()) #dict_keys(['a', 'b', 'c', 'd'])
print(dictionary.values()) #dict_values([1, 2, 3, 4])
print(dictionary.items()) #dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

print({ k: v**2 for (k,v) in dictionary.items()}) #{'a': 1, 'b': 4, 'c': 9, 'd': 16}
print({k.upper(): v for (k,v) in dictionary.items()}) #{'A': 1, 'B': 2, 'C': 3, 'D': 4}