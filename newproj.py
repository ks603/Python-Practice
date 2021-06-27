# This program says hello and asks for my name

print('Hello World')
print('What is your name')  # ask for their name
myName = input()
print('It is good to mee you ' + myName)
print('The length of you name is:')
print(len(myName))
print('What is your age?')  # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')


print(42 == 42)
print(42 == 'hello')
print(42 == 41)
print(2 != 3)
print(42 < 100)
print(42 >= 100)
print(42 < 42)
print(42 <= 42)
myAge = 26
print(myAge < 30)
print(42 == '42')
print(42.0 == 42)
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print(not True)
print(not False)

myAge = 26
myPet = 'cat'
print(myAge > 20 and myPet == 'cat')
