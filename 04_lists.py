'''
numbers = []
for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2)

numbers = []
for i  in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)

print(numbers)

numbers_v2 = [i * 2 for i in range(1,11) if i % 2 ==0]
print(numbers)
'''

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)




