# Factorial Challenge
# Ex:
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

#Return the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    if type(num) is not int:
        return None

    elif num < 0:
        return None

    else:
        fac = 1
        while num != 0:
            fac *= num
            num -= 1
        return fac

# 120
print(factorial(5))

# 720
print(factorial(6))

# 1
print(factorial(0))

# None
print(factorial(-2))

# None
print(factorial(1.2))

# None
print(factorial('spam spam spam spam spam spam'))

