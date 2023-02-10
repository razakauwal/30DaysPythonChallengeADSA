#Day 10





for i in range(11):

    print(i)

    



i = 0

while i < 11:

    print(i)

    i += 1





for i in range(10, -1, -1):

    print(i)





i = 10

while i >= 0:

    print(i)

    i -= 1





# triangle

for i in range(1, 8):

    print('#' * i)





for i in range(8):

    for j in range(16):

        if j % 2 == 0:

            print('#', end=' ')

        else:

            print(' ', end=' ')

    print('')





for i in range(11):

    print(f"{i} x {i} = {i*i}")





skills = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in skills:

    print(item)





for i in range(101):

    if i % 2 == 0:

        print(i)





for i in range(101):

    if i % 2 != 0:

        print(i)





sum = 0

for i in range(101):

    sum += i

print("The sum of all numbers from 0 to 100 is:", sum)





odd_sum = 0

for i in range(101):

    if i % 2 == 0:

      odd_sum += i

print("The sum of all odd numbers from 0 to 100 is:", odd_sum)





fruits = ['banana', 'orange', 'mango', 'lemon']

reversed_fruits = []

for fruit in fruits:

    reversed_fruits.insert(0, fruit)

print(reversed_fruits)

