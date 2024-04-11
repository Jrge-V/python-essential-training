from dataclasses import dataclass

# Def Prime Numbers: Numbers that are only divided by itself and 1
# Def Factors: All Numbers


# Initiating a class that takes in an integer for the variable myNumber
@dataclass
class PrimeFactors:
    myNumber: int

    # pass in the number into my method
    def get_prime_factor(self):
        # Initialize a list of the factors that will be returned later
        list_of_factors = []
        # begin the divisor at 2 since 1 is not a factor
        divisor = 2

        # While loop continues as long as it's less than the number passed in
        while divisor <= self.myNumber:

            # Use modulo to check if my number and divisor returns 0
            if self.myNumber % divisor == 0:
                # if true then append it to the list
                list_of_factors.append(divisor)
                # then divide my number by the divisor
                self.myNumber /= divisor
            else:
                # add a +1 to the divisor to check for the next possible divisor
                divisor += 1

        # finally return the list with appended divisors
        return list_of_factors


# ask for user to input an integer
number = int(input('Enter an Int: '))
# call the parent class and method
prime_checker = PrimeFactors(number).get_prime_factor()
# print out the return statement
print(prime_checker)


# TEST CODE
print(PrimeFactors(630).get_prime_factor())  # [2, 3, 3, 5, 7]
print(PrimeFactors(13).get_prime_factor())  # [13]
