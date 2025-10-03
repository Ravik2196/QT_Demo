


class number:
    def __init__(self, number):
        self.__number = number 
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        self.__number = value 

    def is_even (self):
        return self.__number % 2 ==0
    
    def is_prime(self):
        result = True
        for index in range (2,self.__number):
            if self.__number%index == 0:
                result = False
                break
        return result
    
    def is_palindrom(self):
        original = self.__number
        reversed_num = 0
        while original > 0:
            digit = original % 10
            reversed_num = reversed_num * 10 + digit
            original = original // 10
        return self.__number == reversed_num



    
    num = int(input ('Enter number to check : '))
    
    is_even(num)
    is_palindrom(num)
    is_prime(num)



    