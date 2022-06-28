def factorial(number):
    if number == 1:
        return 1
    else :
        fact = number * factorial(number-1)
    return fact

factorial(int(3))