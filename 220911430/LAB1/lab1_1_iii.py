def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inv(a, m):
    if m == 1:
        return 0
    for i in range (1, m):
    	if (a*i) % m == 1:
    		x1=i
    return x1

def char_to_int(c):
    return ord(c) - ord('a')

def int_to_char(n):
    return chr(n + ord('a'))

def encrypt_char(plain_char, a, b):
    if plain_char.isalpha():
        plaintext_int = char_to_int(plain_char.lower())
        encrypted_int = (a * plaintext_int + b) % 26
        return int_to_char(encrypted_int)
    return plain_char

def decrypt_char(cipher_char, a, b):
    if cipher_char.isalpha():
        ciphertext_int = char_to_int(cipher_char.lower())
        a_inv = mod_inv(a, 26)
        decrypted_int = (a_inv * (ciphertext_int - b)) % 26
        return int_to_char(decrypted_int)
    return cipher_char

def msg_proc(message, a, b, mode):
    if gcd(a, 26) != 1:
        raise ValueError("Key '1' must be coprime with 26")
    
    message = message.replace(" ", "").lower()
    processed_chars = []
    
    if mode == 'encrypt':
        for char in message:
            processed_chars.append(encrypt_char(char, a, b))
    elif mode == 'decrypt':
        for char in message:
            processed_chars.append(decrypt_char(char, a, b))
    
    return ''.join(processed_chars)

message = "I am learning information security"
a = 15
b = 20

encrypted_msg = msg_proc(message, a, b, 'encrypt')
print("Encrypted message:", encrypted_msg)

decrypted_msg = msg_proc(encrypted_msg, a, b, 'decrypt')
print("Decrypted message:", decrypted_msg)

