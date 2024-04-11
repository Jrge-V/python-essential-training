from dataclasses import dataclass

# Def Prime Numbers: Numbers that are only divided by itself and 1
# Def Factors: All Numbers

# TODO: Check if number is prime


@dataclass
class PrimeFactors:
    myNumber: int



    def is_prime_number(self):
        num = self.myNumber - 1

        while num > 1:
            if self.myNumber % num == 0:
                return f'{self.myNumber} is not a prime number!'
            num -= 1
        return f'{self.myNumber} is a prime number!'



number = int(input('Enter an Int: '))
prime_checker = PrimeFactors(number).is_prime_number()
print(prime_checker)






