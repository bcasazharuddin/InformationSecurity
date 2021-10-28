#Ques 2 : Write a program that can encrypt and decrypt using the Affine Cipher 
#calculate gcd
def egcd(a, b):                 
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y
	
#calculates and returns inverse	
def modinverse(a, m):               
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None
	else:
		return x % m
#create encryption function		
def affineencrypt(text, key):  
    result=""
    for i in text:
        if i!=' ' and i.isupper():
            result+=chr((key[0]*(ord(i)-65)+key[1])%26+65)
        elif i!=' ' and i.islower():
            result+=chr((key[0]*(ord(i)-97)+key[1])%26+97)
        else:
            result+=' '
    return result
 #create decryption function   
def affinedecrypt(cipher, key):   
    result=""
    for i in cipher:
        if i!=' ' and i.isupper():
            result+=chr((modinverse(key[0],26)*(ord(i)-65-key[1]))%26+65)
        elif i!=' ' and i.islower():
            result+=chr((modinverse(key[0],26)*(ord(i)-97-key[1]))%26+97)
        else:
            result+=' '
    return result
 #menu driver     
def menu():                        
    while True:
        choice=int(input("\n\n1.Encrypt\n2.Decrypt\n3.Exit\nChoose : "))
        if choice==1:
            text=input("Enter the Plain Text : ")
            key = [int(x) for x in input('Enter Key(Space separated) : ').split()][:2]
            print("\n\nEncrypted Text: ",affineencrypt(text,key))
        elif choice==2:
            text=input("Enter the encrypted Text : ")
            key = [int(x) for x in input('Enter Key(Space separated) : ').split()][:2]
            print("\n\nDecrypted Text:",affinedecrypt(text,key))
        else:
            break

menu()
