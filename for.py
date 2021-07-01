print('My name is')
for i in range(12, 16):
    print('Kevin Five Times ' + str(i))

total = 0
for num in range(101):
    total = total + num
print(total)

print('my name is')
i = 0
while i < 5:
    i = i + 1
    print('Kevin Five Times ' + str(i))

print('My name is')
for i in range(0, 10, 1):
    print('Kevin Five Times ' + str(i))


print('My name is')
for i in range(5, -1, -1):
    print('Kevin Five Times ' + str(i))


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
