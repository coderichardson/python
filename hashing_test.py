# Accepts input from the user to be hashed, prompts user to select a hashing algorithm, 
# hashes the user input with the selected hashing algorithm, prints the hash to the
# screen, and writes the hash to a file.

import hashlib

x = input("Enter text to be hashed: ")
hash_alg = input("\n a. MD5 \n b. SHA1 \n c. SHA256 \n d. SHA512 \n \n Select a hashing algorithm: ")

# MD5
if hash_alg == "a" or hash_alg == "A" or hash_alg == "MD5" or hash_alg == "md5":
    hash_object = hashlib.md5(x.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    with open('hash_result.txt', 'w') as f:
        f.write(hex_dig)
        f.close

# SHA1
if hash_alg == "b" or hash_alg == "B" or hash_alg == "SHA1" or hash_alg == "sha1":
    hash_object = hashlib.sha1(x.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    with open('hash_result.txt', 'w') as f:
        f.write(hex_dig)
        f.close

# SHA256
if hash_alg == "c" or hash_alg == "C" or hash_alg == "SHA256" or hash_alg == "sha256":
    hash_object = hashlib.sha256(x.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    with open('hash_result.txt', 'w') as f:
        f.write(hex_dig)
        f.close

# SHA512
if hash_alg == "d" or hash_alg == "D" or hash_alg == "SHA512" or hash_alg == "sha512":
    hash_object = hashlib.sha512(x.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    with open('hash_result.txt', 'w') as f:
        f.write(hex_dig)
        f.close