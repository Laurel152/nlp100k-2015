def cipher(plaintext):
    ciphertext = ""
    for c in plaintext:
        if c.islower():
            ciphertext = ciphertext + chr(219 - ord(c))
        else:
            ciphertext = ciphertext + c
    return ciphertext

str_in = "Hello, World!"
str_cipher = cipher(str_in)
print(str_cipher)
print(cipher(str_cipher))
