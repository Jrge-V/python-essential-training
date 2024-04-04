# ASCII Art Compression
# Use the "encodeString" and "decodeString" functions from the Chapter 4 challenge, provided below
#
# Read in the ASCII art text file 10_04_challenge_art.txt and write it back to a new file that has a smaller file size than the original file. For example, the original 10_04_challenge_art.txt has a file size of 2.757kB (or 2,757 ASCII characters).
#
# Any compression is great!
# Is there any way you could get this file to 1kb?
# Less than 1kb?
# After compressing the file, make sure to check your work by opening and decoding it again!

import os

import json

# Encodes as a list of (char, count) tuples
def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        try:
            decodedStr = decodedStr + item[0] * item[1]
        except:
            print(item)
    return decodedStr

def encodeFile(filename, newFilename):
    with open(filename) as f:
        data = encodeString(f.read())

    with open(newFilename, 'w') as f:
        f.write(json.dumps(data))


def decodeFile(filename):
    with open(filename) as f:
        data = f.read()
    return decodeString(json.loads(data))



print(f'Original file size: {os.path.getsize("10_04_challenge_art.txt")}')
encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')
print(f'New file size: {os.path.getsize("10_04_challenge_art_encoded.txt")}')
print(decodeFile('10_04_challenge_art_encoded.txt'))