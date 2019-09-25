import random
number = input('Enter your number from 0 to 10 :')
number_2 = random.randint(1, 10)
number_2 = str(number_2)
a = number in number_2
print(a)
print('it was ', number_2)
