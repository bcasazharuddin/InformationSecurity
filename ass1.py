#Ques 1 : Write a program that can encrypt and decrypt using the Additive Cipher
# create encrypt  funtion
def encrypttext(text,shift):      
  encrypted_text=""  #empty string
  #traverse text
  for k in text:
   # encrypt uppercase characters
    if (k.isupper()):
      encrypted_text += chr((ord(k) + shift-65) % 26 + 65)
     # encrypt lowercase characters
    else:
      encrypted_text += chr((ord(k) + shift - 97) % 26 + 97)
  return encrypted_text
# create decrypts function  
def decrypttext(text,shift):    
  decrypted_text=""   #empty string
  for k in text:
    if (k.isupper()):
      decrypted_text += chr((ord(k) - shift-65) % 26 + 65)
    else:
      decrypted_text += chr((ord(k) - shift - 97) % 26 + 97)
  return decrypted_text
#menu  driver   
def menu():              
  while True:
    choice=int(input("\n\n1.Encrypt\n2.Decrypt\n3.Exit\nChoose : "))
    if choice==1:
      text=input("Enter the Plain Text : ")
      shift=int(input("Enter the Shift Value : "))
      print("\n\nEncrypted Text : ",encrypttext(text,shift))
    elif choice==2:
      text=input("Enter the encrypted Text : ")
      shift=int(input("Enter the Shift Value : "))
      print("\n\nDecrypted Text :",decrypttext(text,shift))
    else:
      break

menu()
