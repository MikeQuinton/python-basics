import random
import math

offset = []
keyCode = ""

def encrypt():
    encryption = ""
    counter = 0
    message = input("Enter a message to encrypt: ")
    for letter in message:
        num = random.randint(0,9)
        offset.append(num)
        [random.randint(0,9) if dup == 0 else dup for dup in offset]
        encryption += chr(ord(letter) + offset[counter])
        counter = counter + 1
    print(offset)
    print(encryption)

def decrypt():
    global keyCode
    decryption = ""
    counter = 0
    message = input("Enter a message to decrypt: ")
    for letter in message:
        decryption += chr(ord(letter) - offset[counter])
        counter = counter + 1
    keyCode += decryption
    print(offset)
    print(decryption)

































def saveKey():
    global keyCode
    print("Please specify a name for the .txt file the key will be saved too")
    key = input("Name of file: ")
    key += ".txt"
    keyFile = open(key, "a")
    keyFile.write(str(offset))
    keyFile.close()
    print(keyCode)

def fileDecrypt():
    offset = []
    findKey = input("Choose which key to load: ")
    findKey += ".txt"
    keyFile = open(findKey, "r")
    for line in keyFile:
        if line != 0:
            offset = eval(line)
    keyFile.close()
    encryption = ""
    counter = 0
    message = input("Enter the encrypted key: ")
    for letter in message:
        encryption += chr(ord(letter) - offset[counter])
        counter = counter + 1
    print(offset)
    print(encryption)
    print(keyCode)

encrypt()
decrypt()
# saveKey()
# fileDecrypt()
