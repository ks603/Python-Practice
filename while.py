spam = 0
while spam < 5:
    print('Hello World')
    spam = spam + 1

name = ''
while name != 'kevin':
    print('Please type your name.')
    name = input()
print('Thank you!')

while True:
    print('Please type your favorite color.')
    name = input()
    if name == ('green'):
        break
print('Thank you!')


spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))


x = 0
while x < 100:
    x = x + 1
    if (x % 3 == 0) and (x % 5 == 0):
        print('fizzbuzz')
    elif x % 3 == 0:
        print('fizz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print(x)
