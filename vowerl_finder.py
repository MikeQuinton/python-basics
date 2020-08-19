# Vowel reader
while True:
    print("Vowel finder")
    [print(x) for x in input("Enter a message: ").lower() if x in ["a", "e", "u", "i", "o"]]
    print("Consonant finder")
    [print(x) for x in input("Enter a message: ").lower() if x not in ["a", "e", "u", "i", "o"]]
