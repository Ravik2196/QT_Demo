import sys
import platform

print(sys.version)
print(sys.platform)
print(platform.system())

def is_palindrom(number):
        num = number
        count = 1
        while num != 0:
            num = num / 10
            count += 1
            print(num)
        pal = number / (10 ^ count)

        print (number)
        print(pal)

is_palindrom(121)