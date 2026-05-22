from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
import os
import sys



yourinput = input("please add a key to encrypt: ")

if len(yourinput) != 16:
    print("Error: please add just 16 characters !")
    sys.exit()

key = yourinput.encode('ascii')

path = input("please add your path file(just(.txt)): ")

counter = Counter.new(128)
c = AES.new(key,AES.MODE_CTR,counter=counter)
try:
   with open(path,'r+b') as f:
    plaintext = f.read(16)

    while plaintext:
        f.seek(-len(plaintext),1)
        f.write(c.decrypt(plaintext))
        plaintext=f.read(16)

    print("___________________________________________________________________________________")
    print("")
    print("Done(If you need to decrypt or encrypt, just use the same steps And the Same key)")
    print("")
    print("___________________________________________________________________________________")

except FileNotFoundError:
    print("\nError: File not found! Please check the path and try again.")


except PermissionError:
    print("\nError: Permission denied! You don't have the right to modify this file.")


except Exception as e:
    print(f"\nUnexpected Error: {e}")