# Ques : Write a program that can encrypt and Decrypt using a 2*2 Hill Cipher.
keymatrix = [[0] * 2 for i in range(2)]
inversekeymatrix = [[0] * 2 for i in range(2)]

#key matrix for the key string 
def getkeymatrix(key):
    k = 0
    for i in range(2):
        for j in range(2):
            keymatrix[i][j] = ord(key[k]) % 65
            k += 1


def getinversekeymatrix():
    global inversekeymatrix
    det = (keymatrix[0][0] * keymatrix[1][1] - keymatrix[0][1] * keymatrix[1][0]) % 26
    for i in range(26):
        if (det * i) % 26 == 1:
            det = i
            break
    inversekeymatrix = [[keymatrix[1][1] * det % 26, -1 * keymatrix[0][1] * det % 26],
                          [-1 * keymatrix[1][0] * det % 26, keymatrix[0][0] * det % 26]]

#encrypt message
def encrypt(msg):
    result = ""
    msg = msg.replace(" ", "")
    if len(msg) % 2 != 0:
        msg += "0"

    k = 0
    while k < len(msg):
        vector = [ord(msg[k]) - ord('A') + 1, ord(msg[k + 1]) - ord('A') + 1]
        k += 2
        vector = [(keymatrix[0][0] * vector[0] + keymatrix[0][1] * vector[1]) % 26,
                  (keymatrix[1][0] * vector[0] + keymatrix[1][1] * vector[1]) % 26]
        cipher_text = [chr(vector[i] + ord('A') - 1) for i in range(2)]
        result += ''.join(cipher_text)
    return result

#decrypt message 
def decrypt(msg):
    result = ""
    if len(msg) % 2 != 0:
        msg += "0"
    k = 0
    while k < len(msg):
        vector = [ord(msg[k]) - ord('A') + 1, ord(msg[k + 1]) - ord('A') + 1]
        k += 2
        vector = [(inversekeymatrix[0][0] * vector[0] + inversekeymatrix[0][1] * vector[1]) % 26,
                  (inversekeymatrix[1][0] * vector[0] + inversekeymatrix[1][1] * vector[1]) % 26]
        cipher_text = [chr(vector[i] + ord('A') - 1) for i in range(2)]
        result += ''.join(cipher_text)

    return result

#menu driver 
def menu():
    key = 'HILL'
    getkeymatrix(key)
    getinversekeymatrix()

    while True:
        choice=int(input("\n\n1.Encrypt\n2.Decrypt\n3.Exit\nChoose : "))

        if choice == 1:
            msg = input("Enter the message : ")
            encode = encrypt(msg.upper())
            print("Encoded message",encode)

        elif choice == 2:
            msg = input("Enter the encoded-message : ")
            decode = decrypt(msg.upper())
            print("Decoded message",decode)

        

        else:
            break


menu()
