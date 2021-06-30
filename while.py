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
