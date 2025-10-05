## List Compprihension demo

numbers = [1,4,7,9]


for number in numbers:
    square = []
    square.append(number * number)
    print (square)

print ([number * number for number in numbers])


for number in numbers:
    square = []
    if number % 2 != 0:
        square.append(number * number)
        print (square)

print([number * number for number in numbers if number % 2 != 0])

"""
with List coprehension we can achieve single line code in python

"""