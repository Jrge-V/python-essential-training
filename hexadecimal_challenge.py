# CONVERTING HEXADECIMALS TO DECIMAL
#
# Hexadecimal or "base 16" uses all of the numbers 0 - 9, plus a few others to signify higher numbers:
# A = 10, B = 11, C = 12, D = 13, E = 14, F = 15
#
# Therefore, the number 'D' in hexadecimal would be 13 in decimal.
#
# The number '1A' in hexadecimal would be 26 in decimal. Just like we have the "tens" place in base 10,
# hexadecimal has the "sixteens" place. So 1A would 16 + 10 or 26.
# Better explanation: '1A' = 2 char so 1 = (16 * 1) and the A is (1 * 10) = 16 + 10 = 26
#
# And just like the decimal has the "hundreds" place (because 10 * 10 is 100), hexadecimal has the "256's" place
# (because 16 * 16 is 256) So 'ABC' in hexadecimal is (256 * 10) + (16 * 11) + (1 * 12) or 2,748

# RULES = Don't use int class for this challenge
# print(int('1A', 16))

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,

}

def hexToDec(hexNum):
    # default case
    if not all(char in hexNumbers for char in hexNum) or (len(hexNum) > 3):
        return None
    else:
        # print(hexNum)
        if len(hexNum) == 1:
            return hexNumbers.get(hexNum)
        elif len(hexNum) == 2:
            return (16 * hexNumbers.get(hexNum[0])) + (1 * hexNumbers.get(hexNum[1]))
        else:
            return (256 * hexNumbers.get(hexNum[0])) + (16 * hexNumbers.get(hexNum[1])) + (1 * hexNumbers.get(hexNum[2]))


# ----- TEST CASES ---- #

# 10
print(hexToDec('A'))

# 0
print(hexToDec('0'))

# 27
print(hexToDec('1B'))

# 960
print(hexToDec('3C0'))

# None
print(hexToDec('A6G'))

# None
print(hexToDec('ZZTOP'))

