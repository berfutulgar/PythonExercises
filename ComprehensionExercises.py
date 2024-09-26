#Added squares of even numbers to a dictionary

numbers = range(10)
new_dict = {}

for n in numbers:
    if n %2==0:
        new_dict[n]=n**2

print(new_dict)

#comprehension:

print({n:n**2 for n in numbers if n%2==0})