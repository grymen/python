# This program prints Hello, world!

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
