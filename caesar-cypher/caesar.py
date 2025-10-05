
def ceasar(plaintext, key):
    ciphertext = ""
    minuser = 0
    basePointOfList = 0 # unused if not using vigenere
    print(" ")
    print("plaintext is:  {}".format(plaintext))
    
    for i in range(len(plaintext)):
        if plaintext[i] == " ":
            ciphertext = ciphertext + " "
            continue

        letterToConvert = plaintext[i]
        numberVersion = ord(letterToConvert)

        if letterToConvert.isupper() == True:
            minuser = 65
        else:
            minuser = 97

        numberVersion = numberVersion - minuser
        if vigen == 0:
            numberVersion = (numberVersion + key[basePointOfList]) % 26
        else:
            numberVersion = (numberVersion + key) % 26
        
        numberVersion = numberVersion + minuser
        encryptedCharacter = chr(numberVersion)
        ciphertext = ciphertext + encryptedCharacter

        if vigen == 0:
            basePointOfList = (basePointOfList + 1) % len(key)



    print("ciphertext is:  {}".format(ciphertext))
    print(" ")
    print("thank for using program")



vigenList = []
print("welcome user")
vigen = int(input("do you wanna do vigenere cypher, 0 for yes, 1 for no: "))
plaintext = input("gib me your plain text: ")
if vigen == 0:
    key = input("gib me a key, spaces will be truncated: ")
    for i in range(len(key)):
        if key[i] == " ":
            continue

        letterin = ord(key[i].lower())
        letterin = letterin - 97
        vigenList.append(letterin)
    ceasar(plaintext, vigenList)
else:
    key = int(input("gib me a number key, single number only: "))
    ceasar(plaintext, key)
