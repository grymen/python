# part about name
name = input("What is your name? ")
a = f'Hello {name}!'
print(a)

age = int(input("How old are you? "))
if age > 18:
    print('You are already an adult')
else:
    print('Haha, it\'s too early for you beer')
b = f'Age: {age}'
print(b)

# Mathematical operation
temp = age + 5
print(f'age + 5 = {temp}')
temp = age * 2
print(f'age * 2 = {temp}')
temp = age / 3
print(f'age / 3 = {temp}')
temp += age 
print(f'age += {temp}')
temp = age // 5
print(f'age // 5 = {temp}')
