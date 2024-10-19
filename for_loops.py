fruits = ['apple', 'orange', 'cherry']


for fruit in fruits:
    print(fruit)


for i in fruits:
    print(i + ' pie')


for num in range(1, 100):
    # print(num)
    if num % 3 == 0:
        print(num)


# FIZZBUZZ :

for n in range(1, 100):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)